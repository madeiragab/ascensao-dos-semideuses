"""Motor de combate por turnos do Ascensão dos Semideuses (livro v0).

Modela fielmente o que o livro define hoje: iniciativa 1d20+DES, um ataque por
ação, Vantagem/Desvantagem por 2d20, crítico no 20 natural dobrando os dados,
erro automático no 1 natural, e as técnicas de nível 1 das três classes.

O que o livro NÃO define e portanto está assumido aqui (marcado com ASSUMIDO):
- 0 PV = fora de combate, sem regra de morte ou testes de agonia;
- nenhuma armadura existe, então DEF = 10 + DES para todos;
- ataque de oportunidade não é modelado (o livro não tem a regra);
- posicionamento e distância não são modelados: todos se alcançam.
"""

import random
from dataclasses import dataclass, field

from dados import media_dado
from fichas import Ficha, Monstro


def rola(faces: int) -> int:
    return random.randint(1, faces)


def rola_d20(vantagem: bool = False, desvantagem: bool = False) -> int:
    """Vantagem e Desvantagem se anulam (regra 14)."""
    if vantagem and desvantagem:
        vantagem = desvantagem = False
    if vantagem:
        return max(rola(20), rola(20))
    if desvantagem:
        return min(rola(20), rola(20))
    return rola(20)


@dataclass
class Lutador:
    """Estado mutável de um participante do combate."""

    nome: str
    lado: str                     # "herois" ou "monstros"
    pv_max: int
    defesa: int
    bonus_ataque: int
    dados_dano: list[int]
    dano_fixo: int
    iniciativa_bonus: int
    prof: int = 2
    sp_max: int = 0
    mp_max: int = 0
    ataques_por_turno: int = 1
    brutal: bool = False
    classe: str = "monstro"
    mod_sabedoria: int = 0
    tecnicas: list[str] = field(default_factory=list)
    regras: str = "v0"            # "v0" = livro atual, "v1" = proposta corrigida
    critico_em: int = 20          # Coração de Ares baixa para 19
    # Interruptores para testes A/B
    usar_feroz: bool = True
    usar_pesado: bool = True

    def __post_init__(self):
        self.pv = self.pv_max
        self.sp = self.sp_max
        self.mp = self.mp_max
        self.reacao_disponivel = True
        # Condições ativas: nome -> rodadas restantes. O motor entende três
        # famílias, que é o suficiente para medir o preço delas:
        #   perde_turno    Atordoado, Paralisado, Incapacitado
        #   cega           Amedrontado, Cego  (Desvantagem nos ataques)
        #   sangra_N       perde N PV no fim do próprio turno
        self.condicoes: dict[str, int] = {}
        # Quantos ataques contra mim ainda têm Vantagem por causa do Ataque
        # Feroz. No v0 a marca vale para TODOS os ataques até meu próximo
        # turno; no v1 vale só para o primeiro.
        self.ataques_com_vantagem_contra_mim = 0
        self.dano_causado = 0
        self.furia = 0            # Fúria Crescente: +1 por rodada, até +3
        self.furia_gasta = False
        self.golpe_duplo_usado = False
        self.muralha_usada = False       # Segunda Muralha
        self.furia_cega_usada = False
        self.olho_usado = False
        self.rede_usada = False
        self.folego_usado = False
        self.bencao = 0                  # Bênção da Coragem: +1d4 no ataque
        self.aliados: list = []          # preenchido por combate()
        self.protegido = None            # Juramento do Portão
        self.marcado_por = None          # Postura Desafiadora

    @property
    def vivo(self) -> bool:
        return self.pv > 0

    # -- construtores ------------------------------------------------------
    @classmethod
    def de_ficha(cls, f: Ficha, **kw) -> "Lutador":
        return cls(
            nome=f.nome, lado="herois", pv_max=f.pv_max, defesa=f.defesa,
            bonus_ataque=f.bonus_ataque, dados_dano=list(f.dados_arma),
            dano_fixo=f.dano_fixo, iniciativa_bonus=f.iniciativa_bonus,
            prof=f.prof, sp_max=f.sp_max, mp_max=f.mp_max,
            brutal="Machado grande" in f.arma, classe=f.classe,
            mod_sabedoria=f.mods["sabedoria"], tecnicas=list(f.tecnicas), **kw
        )

    def consumir_vantagem(self) -> bool:
        """O atacante pergunta se este alvo está exposto (Ataque Feroz)."""
        if self.ataques_com_vantagem_contra_mim > 0:
            self.ataques_com_vantagem_contra_mim -= 1
            return True
        return False

    # -- condições ---------------------------------------------------------
    def aplicar_condicao(self, nome: str, rodadas: int = 1) -> None:
        """Condições não se acumulam com elas mesmas: fica a maior duração."""
        self.condicoes[nome] = max(self.condicoes.get(nome, 0), rodadas)

    @property
    def perde_o_turno(self) -> bool:
        return self.condicoes.get("perde_turno", 0) > 0

    @property
    def ataca_com_desvantagem(self) -> bool:
        return self.condicoes.get("cega", 0) > 0

    def resolver_fim_de_turno(self) -> None:
        """Sangramento cobra aqui; depois toda condição perde uma rodada."""
        sangra = next((int(k.split("_")[1]) for k in self.condicoes
                       if k.startswith("sangra_") and self.condicoes[k] > 0), 0)
        if sangra:
            self.sofrer(sangra)
        for nome in list(self.condicoes):
            self.condicoes[nome] -= 1
            if self.condicoes[nome] <= 0:
                del self.condicoes[nome]
        if self.bencao:
            self.bencao -= 1

    @classmethod
    def de_monstro(cls, m: Monstro, sufixo: str = "") -> "Lutador":
        return cls(
            nome=m.nome + sufixo, lado="monstros", pv_max=m.pv_max, defesa=m.defesa,
            bonus_ataque=m.bonus_ataque, dados_dano=list(m.dados_dano),
            dano_fixo=m.dano_fixo, iniciativa_bonus=m.iniciativa_bonus,
            ataques_por_turno=m.ataques_por_turno,
        )

    # -- ações -------------------------------------------------------------
    def sofrer(self, dano: int) -> None:
        """Reduções pessoais. Quem chama de fora deve usar receber()."""
        # Bastião: reduz cada golpe em um valor igual à proficiência, enquanto
        # acima de metade dos PV. Metade do dano rendia +13,4% de vitória.
        if "Bastião" in self.tecnicas and self.pv > self.pv_max / 2:
            dano = max(0, dano - self.prof)
        antes = self.pv
        self.pv = max(0, self.pv - dano)
        # Juramento do Portão: o aliado jurado não cai por um golpe só.
        if self.pv == 0 and antes > 1:
            for a in self.aliados:
                if a.vivo and a is not self and a.protegido is self:
                    self.pv = 1
                    break

    def receber(self, dano: int, atacante=None) -> None:
        """Passa pelas reações de aliados antes de doer em mim."""
        guardiao = self._quem_intercepta(dano)
        if guardiao is not None:
            if "Segunda Muralha" in guardiao.tecnicas and not guardiao.muralha_usada:
                guardiao.muralha_usada = True
            else:
                guardiao.reacao_disponivel = False
            # Ascensão do Guardião reduz à metade o que ele assume no lugar
            recebe = dano // 2 if "Muralha" in guardiao.tecnicas else dano
            guardiao.sofrer(recebe)
            if "Represália" in guardiao.tecnicas and atacante is not None:
                atacante.sofrer(guardiao.prof + max(0, guardiao.dano_fixo))
            return
        self.sofrer(dano)

    def _quem_intercepta(self, dano: int):
        """Um Guardião só entra na frente se o golpe derrubaria o aliado — e se
        ele mesmo sobrevive. É a política de quem sabe jogar."""
        if dano < self.pv:
            return None
        for a in self.aliados:
            if a is self or not a.vivo or "Interceptar" not in a.tecnicas:
                continue
            livre = a.reacao_disponivel or (
                "Segunda Muralha" in a.tecnicas and not a.muralha_usada)
            if livre and a.pv > dano:
                return a
        return None

    def defesa_efetiva(self, total_do_ataque: int) -> int:
        """Aplica Escudo Vínculo: reação, 2 SP, +proficiência na DEF.

        Só é gasto quando faria diferença — o Guardião vê a rolagem antes de
        decidir, o que é generoso mas evita desperdício e mede o teto da técnica.
        """
        # Casca Grossa: +2 DEF com metade dos PV ou menos.
        base = self.defesa + (2 if "Casca Grossa" in self.tecnicas
                              and self.pv <= self.pv_max / 2 else 0)
        if (
            "Escudo Vínculo" in self.tecnicas
            and self.reacao_disponivel
            and self.sp >= 2
            and base <= total_do_ataque < base + self.prof
        ):
            self.sp -= 2
            self.reacao_disponivel = False
            return base + self.prof
        return base

    def atacar(
        self,
        alvo: "Lutador",
        vantagem: bool = False,
        desvantagem: bool = False,
        bonus_extra: int = 0,
        dano_extra: int = 0,
    ) -> int:
        if self.ataca_com_desvantagem:
            desvantagem = True
        if self.condicoes.get("favor", 0) > 0:
            vantagem = True
        # Marcado: Desvantagem só contra alvos que não sejam quem marcou.
        if self.marcado_por is not None and self.marcado_por.vivo                 and alvo is not self.marcado_por:
            desvantagem = True
        nat = rola_d20(vantagem, desvantagem)
        total = nat + self.bonus_ataque + bonus_extra

        if nat == 1:
            return 0
        critico = nat >= self.critico_em
        if not critico and total < alvo.defesa_efetiva(total):
            return 0

        vezes = 2 if critico else 1
        dano = 0
        for _ in range(vezes):
            for faces in self.dados_dano:
                r = rola(faces)
                if self.brutal and r == 1:
                    r = rola(faces)
                dano += r
        if self.bencao:
            dano_extra += rola(4)
        dano += self.dano_fixo + dano_extra + self._furia_deste_ataque()
        dano = max(1, dano)
        alvo.receber(dano, self)
        self.dano_causado += dano
        return dano

    def _furia_deste_ataque(self) -> int:
        """Fúria Crescente entra uma vez por turno, no primeiro ataque."""
        if not self.furia or self.furia_gasta:
            return 0
        self.furia_gasta = True
        return self.furia

    # -- turno -------------------------------------------------------------
    def turno(self, aliados: list["Lutador"], inimigos: list["Lutador"]) -> None:
        """Age e depois resolve o fim do turno, por qualquer caminho."""
        try:
            self._agir(aliados, inimigos)
        finally:
            if not self.perde_o_turno:
                self.resolver_fim_de_turno()

    def _agir(self, aliados: list["Lutador"], inimigos: list["Lutador"]) -> None:
        self.reacao_disponivel = True
        self.ataques_com_vantagem_contra_mim = 0   # a marca do Feroz expira aqui
        self.furia_gasta = False
        if "Fúria Crescente" in self.tecnicas:
            self.furia = min(3, self.furia + 1)

        # Quem perdeu o turno ainda sangra e ainda vê a condição expirar.
        if self.perde_o_turno:
            self.resolver_fim_de_turno()
            return

        alvos = [i for i in inimigos if i.vivo]
        if not alvos:
            return

        if self.classe == "oraculo":
            self._turno_oraculo(aliados, alvos)
            return

        alvo = min(alvos, key=lambda a: a.pv)   # foca em quem está mais ferido

        if self.classe == "furioso":
            self._turno_furioso(alvo, inimigos)
            return

        # Postura Desafiadora / Provocação Ampla: o marcado ataca os outros com
        # Desvantagem. No motor, isso vira Desvantagem nos ataques dele.
        if self.classe == "guardiao" and self.sp >= 2:
            quantos = (2 if "Provocação Ampla" in self.tecnicas
                       else 1 if "Postura Desafiadora" in self.tecnicas else 0)
            marcados = 0
            for m in [i for i in inimigos if i.vivo]:
                if marcados >= quantos or self.sp < 2:
                    break
                if m.marcado_por is None:
                    self.sp -= 2
                    m.marcado_por = self
                    marcados += 1
            # Provocação Ampla puxa a atenção de dois: você fica exposto.
            if marcados > 1:
                self.ataques_com_vantagem_contra_mim = 99
        # Fôlego de Ferro: uma vez por combate, recupera SP igual ao nível.
        if ("Fôlego de Ferro" in self.tecnicas and not self.folego_usado
                and self.sp < self.sp_max * 0.4):
            self.folego_usado = True
            self.sp = min(self.sp_max, self.sp + self.prof * 3)

        for _ in range(self.ataques_por_turno):
            if not alvo.vivo:
                restantes = [i for i in inimigos if i.vivo]
                if not restantes:
                    return
                alvo = restantes[0]
            self.atacar(alvo, vantagem=alvo.consumir_vantagem())

    def _turno_furioso(self, alvo: "Lutador", inimigos=None) -> None:
        pv_antes = alvo.pv
        if self.regras == "v0":
            self._feroz_e_pesado_juntos(alvo)
        else:
            self._feroz_ou_pesado(alvo)
        matou = pv_antes > 0 and alvo.pv == 0
        # Rasgo: o Ataque Pesado deixa o alvo sangrando.
        if "Rasgo" in self.tecnicas and alvo.vivo and alvo.pv < pv_antes:
            alvo.aplicar_condicao("sangra_1", 3)
        if "Sede de Sangue" in self.tecnicas and matou:
            self.sp = min(self.sp_max, self.sp + rola(4))

        # Ataque Extra (nível 5+) entra como ataques_por_turno; os extras abaixo
        # são técnicas do Capítulo Nove.
        for _ in range(max(0, self.ataques_por_turno - 1)):
            restantes = [i for i in (inimigos or []) if i.vivo]
            if not restantes:
                break
            a = min(restantes, key=lambda x: x.pv)
            pv2 = a.pv
            self.atacar(a, vantagem=a.consumir_vantagem())
            if "Massacre" in self.tecnicas and pv2 > 0 and a.pv == 0:
                sobra = [i for i in (inimigos or []) if i.vivo]
                if sobra:
                    self.atacar(min(sobra, key=lambda x: x.pv))

        # Massacre pelo primeiro abate
        if "Massacre" in self.tecnicas and matou:
            sobra = [i for i in (inimigos or []) if i.vivo]
            if sobra:
                self.atacar(min(sobra, key=lambda x: x.pv))

        # Fúria Cega: uma vez por combate, um ataque em cada inimigo ao alcance.
        if ("Fúria Cega" in self.tecnicas and not self.furia_cega_usada
                and len([i for i in (inimigos or []) if i.vivo]) >= 2):
            self.furia_cega_usada = True
            # um ataque em cada inimigo, mas todos com Desvantagem: é um golpe
            # largo e descontrolado, não cinco ataques limpos.
            for i in [x for x in (inimigos or []) if x.vivo][:3]:
                self.atacar(i, desvantagem=True)
            self.ataques_com_vantagem_contra_mim = 99

        # Golpe Duplo: ação bônus, 2 SP, −2 na rolagem
        if ("Golpe Duplo" in self.tecnicas and self.sp >= 2
                and not self.golpe_duplo_usado):
            restantes = [i for i in (inimigos or []) if i.vivo]
            if restantes:
                self.sp -= 2
                self.golpe_duplo_usado = True
                # uma vez por combate, e sem o modificador de atributo no dano.
                # Um ataque extra por rodada valia +17,4% e virava obrigatório.
                self.atacar(min(restantes, key=lambda x: x.pv),
                            bonus_extra=-2, dano_extra=-self.dano_fixo)

    def _feroz_e_pesado_juntos(self, alvo: "Lutador") -> None:
        """Livro v0: o texto permite explicitamente combinar os dois (seção 25)."""
        feroz, pesado = self.usar_feroz, self.usar_pesado
        exposto = alvo.consumir_vantagem()
        self.atacar(
            alvo,
            vantagem=feroz or exposto,
            bonus_extra=-2 if pesado else 0,
            dano_extra=5 if pesado else 0,
        )
        if feroz:
            # Marca aberta: TODOS os ataques até o próximo turno dele.
            self.ataques_com_vantagem_contra_mim = 999

    def _feroz_ou_pesado(self, alvo: "Lutador") -> None:
        """Proposta v1: um ou outro, nunca os dois.

        Ataque Feroz: Vantagem, grátis, expõe a UM ataque com Vantagem.
        Ataque Pesado: −2 no ataque, +1 dado da arma no dano, custa 1 SP.

        O Furioso escolhe a opção de maior dano esperado contra aquela DEF —
        é assim que um jogador competente joga, e é o teste mais duro para
        saber se a decisão é de verdade.
        """
        from dados import Ataque

        exposto = alvo.consumir_vantagem()
        dados_pesado = self.dados_dano + [max(self.dados_dano)]

        op_feroz = Ataque(
            "feroz", self.bonus_ataque, self.dados_dano, self.dano_fixo,
            brutal=self.brutal, vantagem=True,
        ).dano_esperado(alvo.defesa)
        op_pesado = Ataque(
            "pesado", self.bonus_ataque - 2, dados_pesado, self.dano_fixo,
            brutal=self.brutal, vantagem=exposto,
        ).dano_esperado(alvo.defesa)

        if ("Ataque Pesado" in self.tecnicas and self.usar_pesado
                and self.sp >= 1 and op_pesado > op_feroz):
            self.sp -= 1
            dados_originais = self.dados_dano
            self.dados_dano = dados_pesado
            try:
                self.atacar(alvo, vantagem=exposto, bonus_extra=-2)
            finally:
                self.dados_dano = dados_originais
        elif self.usar_feroz:
            self.atacar(alvo, vantagem=True)
            self.ataques_com_vantagem_contra_mim = 1   # só o primeiro ataque
        else:
            self.atacar(alvo, vantagem=exposto)

    def _turno_oraculo(self, aliados: list["Lutador"], alvos: list["Lutador"]) -> None:
        # --- Tier 3: Rede do Destino, uma vez por combate, quando o grupo
        # ainda tem gente de pé para aproveitar a Vantagem.
        if ("Rede do Destino" in self.tecnicas and not self.rede_usada
                and sum(1 for a in aliados if a.vivo) >= 2):
            self.rede_usada = True
            for a in aliados:
                if a.vivo and a is not self:
                    a.ataques_com_vantagem_contra_mim = 0
                    a.bencao = 0
                    a.condicoes["favor"] = 2
            # o motor lê "favor" como Vantagem no próximo ataque
        # --- Bênção da Coragem: +1d4 no ataque de um aliado por uma rodada
        if "Bênção da Coragem" in self.tecnicas and self.mp >= 2:
            candidato = next((a for a in aliados
                              if a.vivo and a is not self and not a.bencao), None)
            if candidato is not None:
                self.mp -= 2
                candidato.bencao = 2
        # --- Visão do Infortúnio: Desvantagem no próximo ataque do inimigo
        if "Visão do Infortúnio" in self.tecnicas and self.mp >= 1:
            alvo_v = next((a for a in alvos if a.vivo
                           and a.condicoes.get("cega", 0) == 0), None)
            if alvo_v is not None:
                self.mp -= 1
                alvo_v.aplicar_condicao("cega", 1)
        # --- Olho do Futuro: um turno inteiro a mais, uma vez por combate
        if ("Olho do Futuro" in self.tecnicas and not self.olho_usado):
            self.olho_usado = True
            self._turno_oraculo_base(aliados, alvos)
        return self._turno_oraculo_base(aliados, alvos)

    def _turno_oraculo_base(self, aliados: list["Lutador"], alvos: list["Lutador"]) -> None:
        # Ação bônus: Palavra Curativa no aliado mais ferido, se valer a pena.
        if "Palavra Curativa" in self.tecnicas and self.mp >= 2:
            feridos = [a for a in aliados if a.vivo and a.pv <= a.pv_max // 2]
            if feridos:
                alvo_cura = min(feridos, key=lambda a: a.pv)
                self.mp -= 2
                cura = rola(6) + self.mod_sabedoria
                alvo_cura.pv = min(alvo_cura.pv_max, alvo_cura.pv + cura)
                if "Cura em Cadeia" in self.tecnicas and self.mp >= 1:
                    segundo = next((a for a in feridos if a is not alvo_cura), None)
                    if segundo is not None:
                        self.mp -= 1
                        segundo.pv = min(segundo.pv_max,
                                         segundo.pv + rola(6) + self.mod_sabedoria)
        alvo = min(alvos, key=lambda a: a.pv)
        self.atacar(alvo, vantagem=alvo.consumir_vantagem())


def combate(
    herois: list[Lutador], monstros: list[Lutador], max_rodadas: int = 40
) -> dict:
    """Roda um combate até um lado cair. Devolve o relatório."""
    todos = herois + monstros
    for c in todos:
        c.aliados = herois if c.lado == "herois" else monstros
    # Muro de Escudos: +1 DEF nos aliados enquanto o Guardião estiver de pé.
    for c in herois:
        if "Muro de Escudos" in c.tecnicas:
            for a in herois:
                if a is not c:
                    a.defesa += 1
    # Juramento do Portão: protege quem tem menos PV máximos.
    for c in herois:
        if "Juramento do Portão" in c.tecnicas:
            outros = [a for a in herois if a is not c]
            if outros:
                c.protegido = min(outros, key=lambda a: a.pv_max)

    ordem = sorted(
        todos, key=lambda c: rola_d20() + c.iniciativa_bonus, reverse=True
    )

    for rodada in range(1, max_rodadas + 1):
        for lutador in ordem:
            if not lutador.vivo:
                continue
            if lutador.lado == "herois":
                lutador.turno(herois, monstros)
            else:
                lutador.turno(monstros, herois)

            if not any(h.vivo for h in herois) or not any(m.vivo for m in monstros):
                break

        herois_vivos = any(h.vivo for h in herois)
        monstros_vivos = any(m.vivo for m in monstros)
        if not herois_vivos or not monstros_vivos:
            return {
                "vencedor": "herois" if herois_vivos else "monstros",
                "rodadas": rodada,
                "herois_vivos": sum(1 for h in herois if h.vivo),
                "pv_restante": {h.nome: h.pv for h in herois},
                "dano": {c.nome: c.dano_causado for c in todos},
            }

    return {
        "vencedor": "tempo",
        "rodadas": max_rodadas,
        "herois_vivos": sum(1 for h in herois if h.vivo),
        "pv_restante": {h.nome: h.pv for h in herois},
        "dano": {c.nome: c.dano_causado for c in todos},
    }


def rodar_muitos(
    montar_herois, montar_monstros, n: int = 20000, seed: int | None = 20260726
) -> dict:
    """Repete o combate n vezes e agrega os resultados."""
    if seed is not None:
        random.seed(seed)

    vitorias = 0
    rodadas_total = 0
    sobreviventes = 0
    pv_final: dict[str, float] = {}
    dano_total: dict[str, float] = {}

    for _ in range(n):
        herois = montar_herois()
        monstros = montar_monstros()
        r = combate(herois, monstros)
        vitorias += r["vencedor"] == "herois"
        rodadas_total += r["rodadas"]
        sobreviventes += r["herois_vivos"]
        for nome, pv in r["pv_restante"].items():
            pv_final[nome] = pv_final.get(nome, 0) + pv
        for nome, d in r["dano"].items():
            dano_total[nome] = dano_total.get(nome, 0) + d

    return {
        "n": n,
        "taxa_vitoria": vitorias / n,
        "rodadas_media": rodadas_total / n,
        "sobreviventes_media": sobreviventes / n,
        "pv_final_medio": {k: v / n for k, v in pv_final.items()},
        "dano_medio": {k: v / n for k, v in dano_total.items()},
    }


def dano_medio_por_ataque(dados: list[int], fixo: int, brutal: bool = False) -> float:
    """Utilitário de leitura: dano bruto médio de um acerto, sem crítico."""
    from dados import media_dado_brutal
    f = media_dado_brutal if brutal else media_dado
    return sum(f(d) for d in dados) + fixo

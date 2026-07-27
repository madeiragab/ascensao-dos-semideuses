"""Mede o preço das condições no motor de criação de habilidades.

A pergunta que importa: o motor vende condição forte (Atordoado, Paralisado)
por 4 pontos. Um Oráculo de nível 1 tem 17 MP. Tirar o turno de um inimigo por
4 MP é mais forte que causar 4d8+3 de dano pelo mesmo preço?

Se for muito mais forte, controle vira a única escolha e o dano some do jogo —
o mesmo erro que o Ataque Pesado tinha. Neste caso a solução seria travar as
condições fortes por nível, como o livro original fazia.

Rodar de dentro da pasta sim/:
    python condicoes.py
"""

import random
import sys

from combate import Lutador, combate, rola, rola_d20
from dados import chance_de_acertar
from fichas import bestiario
from fichas_v1 import furioso_v1, guardiao_v1, oraculo_v1
from kleos import monstro_padrao

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

N = 12000


def titulo(t: str) -> None:
    print()
    print("=" * 76)
    print(t)
    print("=" * 76)


class OraculoTatico(Lutador):
    """Oráculo que gasta MP numa tática escolhida, em vez de só curar.

    taticas:
      "cura"       comportamento padrão do motor (referência)
      "dano"       4 MP: 4d8 + mod em alvo único
      "forte"      4 MP: condição forte, Vontade para evitar, repete no fim do turno
      "media"      2 MP: condição média (Cego), mesma resistência
      "sangra"     2 MP: dano contínuo de 1d6 por rodada
    """

    def __init__(self, *a, tatica: str = "cura", cd: int = 13,
                 mod_divino: int = 3, **kw):
        super().__init__(*a, **kw)
        self.tatica = tatica
        self.cd = cd
        self.mod_divino = mod_divino

    def _turno_oraculo(self, aliados, alvos):
        alvo = min(alvos, key=lambda a: a.pv)

        if self.tatica == "cura" or self.mp < 2:
            return super()._turno_oraculo(aliados, alvos)

        if self.tatica == "dano" and self.mp >= 4:
            self.mp -= 4
            dados_originais = self.dados_dano
            fixo_original = self.dano_fixo
            bonus_original = self.bonus_ataque
            self.dados_dano = [8, 8, 8, 8]
            self.dano_fixo = self.mod_divino
            self.bonus_ataque = self.mod_divino + self.prof
            try:
                self.atacar(alvo, vantagem=alvo.consumir_vantagem())
            finally:
                self.dados_dano = dados_originais
                self.dano_fixo = fixo_original
                self.bonus_ataque = bonus_original
            return

        if self.tatica in ("forte", "media"):
            custo = 4 if self.tatica == "forte" else 2
            if self.mp < custo:
                return super()._turno_oraculo(aliados, alvos)
            # não desperdiça em quem já está sob a condição
            chave = "perde_turno" if self.tatica == "forte" else "cega"
            vivos = [a for a in alvos if a.condicoes.get(chave, 0) == 0]
            if not vivos:
                return super()._turno_oraculo(aliados, alvos)
            alvo = min(vivos, key=lambda a: a.pv)
            self.mp -= custo
            # Teste de Vontade do alvo. Monstros de Kleos baixo têm Vontade fraca.
            if rola_d20() + 1 < self.cd:
                alvo.aplicar_condicao(chave, 1)
            return

        if self.tatica == "sangra" and self.mp >= 2:
            self.mp -= 2
            if rola_d20() + 1 < self.cd:
                alvo.aplicar_condicao("sangra_3", 3)
            return

        return super()._turno_oraculo(aliados, alvos)


def trio(tatica: str):
    def montar():
        o = oraculo_v1()
        oraculo = OraculoTatico(
            nome=o.nome, lado="herois", pv_max=o.pv_max, defesa=o.defesa,
            bonus_ataque=o.bonus_ataque, dados_dano=list(o.dados_arma),
            dano_fixo=o.dano_fixo, iniciativa_bonus=o.iniciativa_bonus,
            prof=o.prof, sp_max=o.sp_max, mp_max=o.mp_max, classe="oraculo",
            mod_sabedoria=o.mods["sabedoria"], tecnicas=list(o.tecnicas),
            regras="v1", tatica=tatica,
            cd=8 + o.mods["inteligencia"] + o.prof,
            mod_divino=o.mods["inteligencia"],
        )
        return [
            Lutador.de_ficha(guardiao_v1(), regras="v1"),
            Lutador.de_ficha(furioso_v1(), regras="v1"),
            oraculo,
        ]
    return montar


def rodar(tatica: str, montar_inimigos, n: int = N) -> dict:
    random.seed(90210)
    vitorias = rodadas = sobreviventes = 0
    for _ in range(n):
        r = combate(trio(tatica)(), montar_inimigos())
        vitorias += r["vencedor"] == "herois"
        rodadas += r["rodadas"]
        sobreviventes += r["herois_vivos"]
    return {"vitoria": vitorias / n, "rodadas": rodadas / n,
            "de_pe": sobreviventes / n}


def comparar(nome_encontro, montar) -> None:
    print(f"\n{nome_encontro}")
    print(f"  {'tática do Oráculo':<28} {'custo':>6} {'vitórias':>9} "
          f"{'rodadas':>8} {'de pé':>7}")
    print("  " + "-" * 68)
    linhas = [
        ("cura (referência do livro)", "2 MP", "cura"),
        ("dano, 4d8 + mod", "4 MP", "dano"),
        ("condição média (Cego)", "2 MP", "media"),
        ("condição forte (perde o turno)", "4 MP", "forte"),
        ("dano contínuo, 3 por rodada", "2 MP", "sangra"),
    ]
    base = None
    for rotulo, custo, tat in linhas:
        r = rodar(tat, montar)
        if base is None:
            base = r["vitoria"]
        delta = f"{r['vitoria'] - base:+.1%}" if tat != "cura" else "—"
        print(f"  {rotulo:<28} {custo:>6} {r['vitoria']:>8.1%} "
              f"{r['rodadas']:>8.2f} {r['de_pe']:>7.2f}   {delta}")


def teste_controle_vs_dano() -> None:
    titulo("Controle vale mais que dano pelo mesmo preço?")
    print("Trio de nível 1 (Kleos do grupo = 3). Só a tática do Oráculo muda.")
    print(f"{N} combates por linha.")

    b = bestiario()
    comparar("Contra 1 criatura de Kleos 3 — o combate justo",
             lambda: [Lutador.de_monstro(monstro_padrao(3))])
    comparar("Contra 1 criatura de Kleos 4 — o combate brutal",
             lambda: [Lutador.de_monstro(monstro_padrao(4))])
    comparar("Contra 3 capangas — inimigos numerosos e fracos",
             lambda: [Lutador.de_monstro(b["capanga"], f" {i}") for i in range(1, 4)])


def teste_chance_de_pegar() -> None:
    titulo("Qual a chance de a condição sequer pegar?")
    o = oraculo_v1()
    cd = 8 + o.mods["inteligencia"] + o.prof
    print(f"CD da habilidade do Oráculo de nível 1: {cd}.\n")
    print(f"{'Vontade do alvo':>16} | {'passa no teste':>15} {'condição pega':>15}")
    print("-" * 76)
    for v in (-1, 0, 1, 3, 5, 8, 11):
        p = chance_de_acertar(v, cd)
        print(f"{v:>+16} | {p:>15.0%} {1 - p:>15.0%}")
    print("\nContra alvo de Vontade fraca a condição pega em cerca de metade das")
    print("vezes. Contra um chefe de Kleos alto, quase nunca — e é assim que o")
    print("controle não vira resposta universal.")


if __name__ == "__main__":
    teste_chance_de_pegar()
    teste_controle_vs_dano()
    print()

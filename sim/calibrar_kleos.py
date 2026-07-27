"""Testa a Escala de Kleos em todos os níveis, não só no 1.

A escala foi calibrada contra um trio de nível 1. O Livro II admite que os
degraus de 6 a 11 são extrapolação. Agora que existe progressão, dá para
verificar de verdade.

A promessa a testar: um encontro de Kleos igual ao Kleos do Grupo é um
combate justo e perigoso — vitória por volta de 80%, com gente caindo.

Rodar de dentro da pasta sim/:
    python calibrar_kleos.py
"""

import random
import sys

from combate import Lutador, combate
from fichas import Monstro
from fichas_v1 import furioso_v1, guardiao_v1, oraculo_v1
from kleos import TABUA
from niveis import ataques_por_turno, kleos_do_personagem, personagem, teto_de_custo

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

N = 6000
NIVEIS = (1, 5, 10, 15, 20)


def titulo(t: str) -> None:
    print()
    print("=" * 78)
    print(t)
    print("=" * 78)


def monstro(k: int, tabua=None) -> Monstro:
    pv, defesa, atk, dano, n = (tabua or TABUA)[k]
    fixo = round(dano / n - 5.5)
    return Monstro(f"Kleos {k}", pv_max=pv, defesa=defesa, bonus_ataque=atk,
                   dados_dano=[10], dano_fixo=fixo, ataques_por_turno=n)


class OraculoQueJoga(Lutador):
    """Oráculo que usa MP como uma pessoa usaria: cura quando precisa, e no
    resto do tempo lança a maior habilidade de dano que o teto do nível permite.

    Sem isto o teste mede um grupo que não usa o próprio recurso principal — no
    nível 20 ela tem 95 MP, teto de custo 14, e ficaria cutucando com uma lança.
    """

    def __init__(self, *a, nivel: int = 1, mod_divino: int = 3, teto: int = 5, **kw):
        super().__init__(*a, **kw)
        self.nivel = nivel
        self.mod_divino = mod_divino
        self.teto = teto

    def _turno_oraculo(self, aliados, alvos):
        feridos = [a for a in aliados if a.vivo and a.pv <= a.pv_max * 0.35]
        if feridos and self.mp >= 2:
            return super()._turno_oraculo(aliados, alvos)

        # Orçamento: gastar como se o combate durasse umas quatro rodadas.
        pontos = min(self.teto, max(1, self.mp // 4))
        custo = pontos            # instantânea, alcance curto: custo = pontos
        if self.mp < custo:
            return super()._turno_oraculo(aliados, alvos)

        self.mp -= custo
        alvo = min([a for a in alvos if a.vivo], key=lambda a: a.pv)
        d, f, b = self.dados_dano, self.dano_fixo, self.bonus_ataque
        self.dados_dano = [8] * pontos
        self.dano_fixo = self.mod_divino
        self.bonus_ataque = self.mod_divino + self.prof
        try:
            self.atacar(alvo, vantagem=alvo.consumir_vantagem())
        finally:
            self.dados_dano, self.dano_fixo, self.bonus_ataque = d, f, b


def grupo(nivel: int):
    def montar():
        saida = []
        for base in (guardiao_v1(), furioso_v1(), oraculo_v1()):
            f = personagem(base, nivel)
            if f.classe == "oraculo":
                lut = OraculoQueJoga(
                    nome=f.nome, lado="herois", pv_max=f.pv_max, defesa=f.defesa,
                    bonus_ataque=f.bonus_ataque, dados_dano=list(f.dados_arma),
                    dano_fixo=f.dano_fixo, iniciativa_bonus=f.iniciativa_bonus,
                    prof=f.prof, sp_max=f.sp_max, mp_max=f.mp_max, classe="oraculo",
                    mod_sabedoria=f.mods["sabedoria"], tecnicas=list(f.tecnicas),
                    regras="v1", nivel=nivel, mod_divino=f.mods["inteligencia"],
                    teto=teto_de_custo(nivel),
                )
            else:
                lut = Lutador.de_ficha(f, regras="v1")
            lut.ataques_por_turno = ataques_por_turno(f.classe, nivel)
            saida.append(lut)
        return saida
    return montar


def rodar(nivel: int, k: int, tabua=None, n: int = N) -> dict:
    random.seed(31337)
    v = rod = pe = 0
    for _ in range(n):
        r = combate(grupo(nivel)(), [Lutador.de_monstro(monstro(k, tabua))])
        v += r["vencedor"] == "herois"
        rod += r["rodadas"]
        pe += r["herois_vivos"]
    return {"vitoria": v / n, "rodadas": rod / n, "de_pe": pe / n}


def fichas_por_nivel() -> None:
    titulo("Como o trio cresce")
    print(f"{'nível':>6} {'prof':>5} | "
          f"{'Guardião PV/DEF/atq':>21} {'Furioso PV/DEF/atq':>20} "
          f"{'Oráculo PV/DEF/MP':>19} | {'Kleos do grupo':>14}")
    print("-" * 78)
    for nv in NIVEIS:
        g = personagem(guardiao_v1(), nv)
        f = personagem(furioso_v1(), nv)
        o = personagem(oraculo_v1(), nv)
        kg = 3 * kleos_do_personagem(nv)
        print(f"{nv:>6} {g.prof:>+5} | "
              f"{g.pv_max:>7}/{g.defesa}/{ataques_por_turno('guardiao', nv):<11} "
              f"{f.pv_max:>7}/{f.defesa}/{ataques_por_turno('furioso', nv):<10} "
              f"{o.pv_max:>7}/{o.defesa}/{o.mp_max:<9} | {kg:>14}")


def teste_promessa() -> None:
    titulo("A promessa se sustenta em todos os níveis?")
    print("Trio em cada nível contra o Kleos que a regra chama de combate justo,")
    print(f"e contra os vizinhos. {N} combates por célula.\n")
    print(f"{'nível':>6} {'Kleos grupo':>12} | "
          + "".join(f"{'K'+str(d):>9}" for d in ("-1", "justo", "+1", "+2")))
    print("-" * 78)
    for nv in NIVEIS:
        kg = 3 * kleos_do_personagem(nv)
        linha = []
        for delta in (-1, 0, 1, 2):
            k = kg + delta
            if k < 1 or k > 11:
                linha.append(f"{'—':>9}")
                continue
            linha.append(f"{rodar(nv, k)['vitoria']:>8.1%} ")
        print(f"{nv:>6} {kg:>12} | " + "".join(linha))
    print("\nAlvo: a coluna 'justo' deveria ficar por volta de 80%.")


def detalhe_do_justo() -> None:
    titulo("Detalhe do combate justo em cada nível")
    print(f"{'nível':>6} {'Kleos':>6} | {'vitórias':>9} {'rodadas':>8} "
          f"{'heróis de pé':>13}")
    print("-" * 78)
    for nv in NIVEIS:
        kg = 3 * kleos_do_personagem(nv)
        r = rodar(nv, kg)
        print(f"{nv:>6} {kg:>6} | {r['vitoria']:>8.1%} {r['rodadas']:>8.2f} "
              f"{r['de_pe']:>13.2f}")


if __name__ == "__main__":
    fichas_por_nivel()
    teste_promessa()
    detalhe_do_justo()
    print()

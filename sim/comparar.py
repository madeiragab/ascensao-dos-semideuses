"""Compara o livro v0 com a proposta v1 nos mesmos combates.

Rodar de dentro da pasta sim/:
    python comparar.py
"""

import sys

from dados import Ataque
from combate import Lutador, rodar_muitos
from fichas import bestiario, furioso_ares, guardiao_ares, oraculo_atena
from fichas_v1 import furioso_v1, guardiao_v1, oraculo_v1

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

N = 20000
DEFESAS = [11, 12, 13, 14, 15, 16, 18]


def titulo(t: str) -> None:
    print()
    print("=" * 76)
    print(t)
    print("=" * 76)


def trio_v0():
    return [
        Lutador.de_ficha(guardiao_ares()),
        Lutador.de_ficha(furioso_ares()),
        Lutador.de_ficha(oraculo_atena()),
    ]


def trio_v1():
    return [
        Lutador.de_ficha(guardiao_v1(), regras="v1"),
        Lutador.de_ficha(furioso_v1(), regras="v1"),
        Lutador.de_ficha(oraculo_v1(), regras="v1"),
    ]


def comparar_fichas() -> None:
    titulo("FICHAS: v0 (livro) vs v1 (proposta)")
    print(f"{'':<10} {'PV v0':>6} {'PV v1':>6} | {'SP v0':>6} {'SP v1':>6} | "
          f"{'MP v0':>6} {'MP v1':>6} | {'DEF v0':>7} {'DEF v1':>7}")
    print("-" * 76)
    for a, b in zip(
        [guardiao_ares(), furioso_ares(), oraculo_atena()],
        [guardiao_v1(), furioso_v1(), oraculo_v1()],
    ):
        print(f"{a.nome:<10} {a.pv_max:>6} {b.pv_max:>6} | {a.sp_max:>6} {b.sp_max:>6} | "
              f"{a.mp_max:>6} {b.mp_max:>6} | {a.defesa:>7} {b.defesa:>7}")


def comparar_encontros() -> None:
    titulo(f"MESMOS ENCONTROS, {N} combates cada")
    b = bestiario()
    encontros = [
        ("3 capangas", lambda: [Lutador.de_monstro(b["capanga"], f" {i}") for i in range(1, 4)]),
        ("2 cães do inferno", lambda: [Lutador.de_monstro(b["cao"], f" {i}") for i in range(1, 3)]),
        ("1 escorpião", lambda: [Lutador.de_monstro(b["escorpiao"])]),
        ("2 empusas", lambda: [Lutador.de_monstro(b["empusa"], f" {i}") for i in range(1, 3)]),
        ("1 minotauro", lambda: [Lutador.de_monstro(b["minotauro"])]),
    ]

    print(f"{'encontro':<19} | {'vitórias v0→v1':>16} | {'rodadas v0→v1':>15} | "
          f"{'de pé v0→v1':>14}")
    print("-" * 76)
    guardados = {}
    for nome, montar in encontros:
        r0 = rodar_muitos(trio_v0, montar, n=N)
        r1 = rodar_muitos(trio_v1, montar, n=N)
        guardados[nome] = (r0, r1)
        print(f"{nome:<19} | {r0['taxa_vitoria']:>7.1%} → {r1['taxa_vitoria']:>6.1%} | "
              f"{r0['rodadas_media']:>6.2f} → {r1['rodadas_media']:>5.2f} | "
              f"{r0['sobreviventes_media']:>6.2f} → {r1['sobreviventes_media']:>5.2f}")

    titulo("REPARTIÇÃO DO DANO ENTRE AS CLASSES (o Furioso ainda come tudo?)")
    print(f"{'encontro':<19} | {'v0: G / F / O (% do Furioso)':>33} | "
          f"{'v1: G / F / O':>18}")
    print("-" * 76)
    for nome, (r0, r1) in guardados.items():
        def fatia(r):
            d = r["dano_medio"]
            g, f, o = d["Guardião"], d["Furioso"], d["Oráculo"]
            return g, f, o, f / (g + f + o)
        g0, f0, o0, p0 = fatia(r0)
        g1, f1, o1, p1 = fatia(r1)
        print(f"{nome:<19} | {g0:>5.1f} /{f0:>6.1f} /{o0:>5.1f}  ({p0:>4.0%})       | "
              f"{g1:>4.1f} /{f1:>5.1f} /{o1:>4.1f} ({p1:>3.0%})")


def comparar_decisao_do_furioso() -> None:
    titulo("A DECISÃO DO FURIOSO NA v1: Feroz ou Pesado, por DEF do alvo")
    f = furioso_v1()
    print("Ataque Feroz  = Vantagem, grátis, expõe a UM ataque.")
    print("Ataque Pesado = −2 no ataque, +1 dado da arma no dano, 1 SP.")
    print("Não podem ser combinados no mesmo ataque.\n")
    print(f"{'DEF':>4} | {'Feroz (vantagem)':>17} {'Pesado (−2/+1d10)':>18} "
          f"{'melhor escolha':>16}")
    print("-" * 76)
    for d in DEFESAS:
        feroz = Ataque("f", f.bonus_ataque, [10], f.dano_fixo,
                       brutal=True, vantagem=True).dano_esperado(d)
        pesado = Ataque("p", f.bonus_ataque - 2, [10, 10], f.dano_fixo,
                        brutal=True).dano_esperado(d)
        melhor = "Pesado" if pesado > feroz else "Feroz"
        print(f"{d:>4} | {feroz:>17.2f} {pesado:>18.2f} {melhor:>16}")
    print("\nA escolha muda com a DEF do alvo — é isso que faz a técnica existir.")


def calibrar_ataque_pesado() -> None:
    """Qual −X/+Y deixa o Pesado competitivo com o Feroz SEM dominar?

    Na v1 as duas técnicas competem pela mesma ação, então o rival do Ataque
    Pesado não é 'atacar normal' — é 'atacar com Vantagem de graça'.
    """
    titulo("CALIBRAGEM: Ataque Pesado contra a alternativa real (Ataque Feroz)")
    f = furioso_v1()
    print("Baseline = Ataque Feroz (Vantagem, grátis). Números = ganho do Pesado.\n")
    print(f"{'variante':>10} | " + " ".join(f"{d:>6}" for d in DEFESAS) + "   ponto de virada")
    print("-" * 76)
    for pen, dmg in [(1, 5), (2, 5), (2, 6), (3, 5), (2, 4)]:
        base = [
            Ataque("f", f.bonus_ataque, [10], f.dano_fixo,
                   brutal=True, vantagem=True).dano_esperado(d)
            for d in DEFESAS
        ]
        alt = [
            Ataque("p", f.bonus_ataque - pen, [10], f.dano_fixo + dmg,
                   brutal=True).dano_esperado(d)
            for d in DEFESAS
        ]
        ganhos = [a / b - 1 for a, b in zip(alt, base)]
        linha = " ".join(f"{g:>+5.0%}" for g in ganhos)
        virada = next(
            (f"DEF {d}" for d, g in zip(DEFESAS, ganhos) if g < 0), "nunca vira"
        )
        if all(g > 0 for g in ganhos):
            nota = "domina sempre"
        elif all(g < 0 for g in ganhos):
            nota = "técnica morta"
        else:
            nota = f"vira em {virada}"
        print(f"{f'-{pen} / +{dmg}':>10} | {linha}   {nota}")
    print("\nO alvo é uma variante que ganhe contra DEF baixa e perca contra")
    print("DEF alta: aí o jogador precisa olhar o inimigo antes de decidir.")


def comparar_letalidade() -> None:
    titulo("LETALIDADE: quantas rodadas um Furioso leva para derrubar um colega")
    print("Métrica interna ao livro: dano que o livro dá ao Furioso contra os")
    print("PV e a DEF que o livro dá aos personagens. Não usa monstro nenhum.")

    cenarios = [
        # rótulo, fichas, penalidade, dados, vantagem
        ("v0 — Ataque Feroz + Ataque Pesado empilhados (o livro permite)",
         [guardiao_ares(), furioso_ares(), oraculo_atena()], -2, [10], 5, True),
        ("v1 — melhor jogada disponível, sem empilhar",
         [guardiao_v1(), furioso_v1(), oraculo_v1()], 0, [10], 0, True),
    ]
    for rotulo, fichas, pen, dados, fixo_extra, vant in cenarios:
        fur = fichas[1]
        print(f"\n{rotulo}")
        for alvo in fichas:
            feroz = Ataque("f", fur.bonus_ataque + pen, dados,
                           fur.dano_fixo + fixo_extra, brutal=True,
                           vantagem=vant).dano_esperado(alvo.defesa)
            pesado = Ataque("p", fur.bonus_ataque - 2, dados + [10],
                            fur.dano_fixo, brutal=True).dano_esperado(alvo.defesa)
            dpr = max(feroz, pesado) if rotulo.startswith("v1") else feroz
            print(f"   {alvo.nome:<10} PV {alvo.pv_max:>2}, DEF {alvo.defesa:>2} → "
                  f"{dpr:>5.2f} dano/rodada → {alvo.pv_max / dpr:>4.1f} rodadas")


if __name__ == "__main__":
    comparar_fichas()
    calibrar_ataque_pesado()
    comparar_letalidade()
    comparar_decisao_do_furioso()
    comparar_encontros()
    print()

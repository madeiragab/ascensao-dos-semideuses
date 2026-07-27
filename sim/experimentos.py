"""Bateria de testes de balanceamento do livro v0.

Rodar de dentro da pasta sim/:
    python experimentos.py
"""

import sys

from dados import Ataque
from combate import Lutador, rodar_muitos
from fichas import bestiario, furioso_ares, guardiao_ares, oraculo_atena

DEFESAS = [11, 12, 13, 14, 15, 16, 18]
N = 20000

# O console do Windows abre em cp1252 e engasga em acentos e no sinal "−".
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


def titulo(t: str) -> None:
    print()
    print("=" * 74)
    print(t)
    print("=" * 74)


# ---------------------------------------------------------------------------
def teste_ataque_pesado() -> None:
    titulo("1. ATAQUE PESADO (−2 no ataque / +5 no dano) — vale sempre a pena?")
    print("Furioso nível 1: machado grande 1d10 Brutal, FOR 17 (+3), prof +2.")
    print("Dano esperado por ação, já contando erro e crítico.\n")

    dados, fixo = [10], 3
    print(f"{'DEF':>4} | {'sem Pesado':>11} {'com Pesado':>11} {'ganho':>7} "
          f"| {'+Feroz s/P':>11} {'+Feroz c/P':>11} {'ganho':>7}")
    print("-" * 74)
    for d in DEFESAS:
        base = Ataque("base", 5, dados, fixo, brutal=True)
        pesado = Ataque("pesado", 3, dados, fixo + 5, brutal=True)
        base_v = Ataque("base+v", 5, dados, fixo, brutal=True, vantagem=True)
        pesado_v = Ataque("pesado+v", 3, dados, fixo + 5, brutal=True, vantagem=True)

        b, p = base.dano_esperado(d), pesado.dano_esperado(d)
        bv, pv = base_v.dano_esperado(d), pesado_v.dano_esperado(d)
        print(f"{d:>4} | {b:>11.2f} {p:>11.2f} {p / b - 1:>+6.0%} "
              f"| {bv:>11.2f} {pv:>11.2f} {pv / bv - 1:>+6.0%}")

    print("\nSe o 'ganho' é positivo em toda linha, a escolha não existe:")
    print("Ataque Pesado é o botão certo em qualquer situação, sempre.")


# ---------------------------------------------------------------------------
def teste_habilidade_vs_arma() -> None:
    titulo("2. HABILIDADE DE NÍVEL 1 (2 MP) vs ATAQUE DE ARMA (grátis)")
    o = oraculo_atena()
    mod_divino = o.mods["inteligencia"]
    bonus_hab = mod_divino + o.prof

    print(f"Oráculo nível 1: INT 17 (+{mod_divino}), prof +{o.prof}.")
    print(f"  Habilidade nível 1: 1d8 + {mod_divino}, ataque +{bonus_hab}, custa 2 MP")
    print(f"  Espada longa marcial: 1d8 + mod, ataque +mod+{o.prof}, custa 0")
    print(f"  Lança dela (real): 1d6 + {o.mods['destreza']}, "
          f"ataque +{o.bonus_ataque}, custa 0\n")

    print(f"{'DEF':>4} | {'habilidade 2 MP':>16} {'espada longa*':>14} "
          f"{'lança dela':>11} {'dano por MP':>12}")
    print("-" * 74)
    for d in DEFESAS:
        hab = Ataque("hab", bonus_hab, [8], mod_divino).dano_esperado(d)
        espada = Ataque("espada", bonus_hab, [8], mod_divino).dano_esperado(d)
        lanca = Ataque("lanca", o.bonus_ataque, [6], o.mods["destreza"]).dano_esperado(d)
        print(f"{d:>4} | {hab:>16.2f} {espada:>14.2f} {lanca:>11.2f} {hab / 2:>12.2f}")

    print("\n* espada longa nas mãos de quem tem o mesmo modificador de ataque.")
    print(f"Pool de MP do Oráculo: {o.mp_max} → {o.mp_max // 2} usos "
          "de habilidade nível 1 por dia (não há regra de recuperação).")
    print("A habilidade de nível 1 é numericamente idêntica a uma espada longa,")
    print("mas cobra recurso. O MP não compra poder — só compra alcance e elemento.")


# ---------------------------------------------------------------------------
def teste_resistencia_das_classes() -> None:
    titulo("3. AS TRÊS CLASSES AGUENTAM QUANTO? (livro v0)")
    fichas = [guardiao_ares(), furioso_ares(), oraculo_atena()]
    monstros = bestiario()

    print(f"{'classe':<10} {'PV':>4} {'SP':>4} {'MP':>4} {'DEF':>4} "
          f"{'total rec.':>10} | ataques do Escorpião até cair")
    print("-" * 74)
    esc = monstros["escorpiao"]
    for f in fichas:
        dano_por_ataque = Ataque(
            "m", esc.bonus_ataque, esc.dados_dano, esc.dano_fixo
        ).dano_esperado(f.defesa)
        ataques = f.pv_max / dano_por_ataque
        total = f.pv_max + f.sp_max + f.mp_max
        print(f"{f.nome:<10} {f.pv_max:>4} {f.sp_max:>4} {f.mp_max:>4} "
              f"{f.defesa:>4} {total:>10} | {ataques:>4.1f}")

    print("\nO Guardião — classe defensiva — tem os menores PV e o menor")
    print("total de recursos do jogo. E ninguém tem armadura, porque")
    print("o capítulo de armaduras não existe: DEF = 10 + DES para todos.")


# ---------------------------------------------------------------------------
def teste_sacrificio_de_atributo() -> None:
    titulo("4. SACRIFÍCIO DE ATRIBUTO (passivas, seção 17.1)")
    print("A passiva custa −2 no VALOR de um atributo, o que quase sempre")
    print("significa −1 no MODIFICADOR.\n")
    casos = [
        ("Pele de Pedra", "+1 DEF", "DES", 13, "−1 DEF (mod cai de +1 para +0)",
         "líquido 0 em DEF, e ainda perde Reflexos, Iniciativa e Acrobacia"),
        ("Passos Ligeiros", "+1,5 m de movimento", "CON", 15, "−1 PV máximo",
         "troca 1,5 m por PV e por Fortitude"),
        ("Força das Profundezas", "+1 em Atletismo", "INT", 12, "−1 de Memória e MP",
         "perde um espaço de habilidade preparada para +1 numa perícia"),
    ]
    for nome, efeito, atr, valor, custo, veredito in casos:
        antes = (valor - 10) // 2
        depois = (valor - 2 - 10) // 2
        print(f"{nome}: {efeito}  |  sacrifício −2 {atr} "
              f"({valor}→{valor - 2}, mod {antes:+d}→{depois:+d})")
        print(f"   custo real: {custo}")
        print(f"   veredito:   {veredito}\n")


# ---------------------------------------------------------------------------
def teste_furioso_ab() -> None:
    titulo("5. SIMULAÇÃO: Furioso solo vs Escorpião Gigante — 4 combinações")
    print(f"{N} combates por linha. Vantagem/penalidade do Ataque Feroz "
          "e Ataque Pesado ligados e desligados.\n")

    esc = bestiario()["escorpiao"]
    print(f"{'Feroz':>6} {'Pesado':>7} | {'vitórias':>9} {'rodadas':>8} "
          f"{'PV final médio':>15}")
    print("-" * 74)
    for feroz in (False, True):
        for pesado in (False, True):
            r = rodar_muitos(
                lambda f=feroz, p=pesado: [
                    Lutador.de_ficha(furioso_ares(), usar_feroz=f, usar_pesado=p)
                ],
                lambda: [Lutador.de_monstro(esc)],
                n=N,
            )
            print(f"{str(feroz):>6} {str(pesado):>7} | {r['taxa_vitoria']:>8.1%} "
                  f"{r['rodadas_media']:>8.2f} {r['pv_final_medio']['Furioso']:>15.2f}")


# ---------------------------------------------------------------------------
def teste_trio() -> None:
    titulo("6. SIMULAÇÃO: trio de nível 1 vs grupos de monstros")
    print(f"{N} combates por linha. Guardião + Furioso + Oráculo, "
          "regras do livro v0.\n")

    b = bestiario()
    encontros = [
        ("3 capangas", lambda: [Lutador.de_monstro(b["capanga"], f" {i}") for i in range(1, 4)]),
        ("2 cães do inferno", lambda: [Lutador.de_monstro(b["cao"], f" {i}") for i in range(1, 3)]),
        ("1 escorpião", lambda: [Lutador.de_monstro(b["escorpiao"])]),
        ("2 empusas", lambda: [Lutador.de_monstro(b["empusa"], f" {i}") for i in range(1, 3)]),
        ("1 minotauro", lambda: [Lutador.de_monstro(b["minotauro"])]),
    ]

    def trio():
        return [
            Lutador.de_ficha(guardiao_ares()),
            Lutador.de_ficha(furioso_ares()),
            Lutador.de_ficha(oraculo_atena()),
        ]

    print(f"{'encontro':<20} {'vitórias':>9} {'rodadas':>8} {'heróis de pé':>13} "
          f"| dano causado (G / F / O)")
    print("-" * 74)
    for nome, montar in encontros:
        r = rodar_muitos(trio, montar, n=N)
        d = r["dano_medio"]
        print(f"{nome:<20} {r['taxa_vitoria']:>8.1%} {r['rodadas_media']:>8.2f} "
              f"{r['sobreviventes_media']:>13.2f} | "
              f"{d['Guardião']:>5.1f} / {d['Furioso']:>5.1f} / {d['Oráculo']:>5.1f}")

    print("\nDano causado revela o peso real de cada classe no combate.")


# ---------------------------------------------------------------------------
def teste_besta_vs_arco() -> None:
    titulo("7. BESTA LEVE vs ARCO CURTO (as duas são armas simples)")
    print("No nível 1 ninguém tem ataque extra, então a limitação da Recarga")
    print("('um disparo por ação') não custa nada.\n")
    print(f"{'DEF':>4} | {'arco curto 1d6':>15} {'besta leve 1d8':>15} {'ganho':>7}")
    print("-" * 74)
    for d in DEFESAS:
        arco = Ataque("arco", 5, [6], 3).dano_esperado(d)
        besta = Ataque("besta", 5, [8], 3).dano_esperado(d)
        print(f"{d:>4} | {arco:>15.2f} {besta:>15.2f} {besta / arco - 1:>+6.0%}")


# ---------------------------------------------------------------------------
def teste_letalidade_interna() -> None:
    """Esta é a evidência que NÃO depende de monstros inventados.

    Compara o dano que o próprio livro dá aos personagens com os PV que o
    próprio livro dá aos personagens.
    """
    titulo("8. LETALIDADE MEDIDA SÓ COM NÚMEROS DO LIVRO (sem monstros meus)")
    fichas = [guardiao_ares(), furioso_ares(), oraculo_atena()]

    fur = furioso_ares()
    dpr_furioso = Ataque(
        "feroz+pesado", fur.bonus_ataque - 2, [10], fur.dano_fixo + 5,
        brutal=True, vantagem=True,
    ).dano_esperado(11)
    dpr_guardiao = Ataque("espada", 5, [8], 3).dano_esperado(11)

    print(f"Furioso nível 1, Ataque Feroz + Ataque Pesado, contra DEF 11:")
    print(f"  dano esperado por rodada = {dpr_furioso:.2f}")
    print(f"Guardião nível 1, espada longa, contra DEF 11:")
    print(f"  dano esperado por rodada = {dpr_guardiao:.2f}\n")

    print(f"{'alvo':<10} {'PV':>4} | {'rodadas p/ cair (Furioso)':>26} "
          f"{'(Guardião)':>13}")
    print("-" * 74)
    for f in fichas:
        print(f"{f.nome:<10} {f.pv_max:>4} | {f.pv_max / dpr_furioso:>26.1f} "
              f"{f.pv_max / dpr_guardiao:>13.1f}")

    print("\nUm Furioso derruba qualquer personagem do livro em ~1 rodada.")
    print("Todo combate vira corrida de iniciativa: quem age primeiro ganha.")


# ---------------------------------------------------------------------------
def varredura_ataque_pesado(vantagem: bool) -> None:
    """Procura uma combinação penalidade/bônus que gere escolha real.

    Escolha real = vale a pena contra alvos fáceis e NÃO vale contra
    alvos difíceis. Ou seja, o ganho tem que trocar de sinal.
    """
    n = "9" if vantagem else "10"
    com = "COM Vantagem do Ataque Feroz" if vantagem else "SEM Vantagem"
    titulo(f"{n}. VARREDURA ({com}): qual −X / +Y gera decisão?")
    print("Furioso com machado grande 1d10 Brutal, ataque +5.")
    print("Ganho de dano por variante, por DEF do alvo.\n")

    variantes = [(2, 5), (2, 3), (3, 5), (4, 6), (5, 10), (5, 7), (6, 10)]
    print(f"{'variante':>12} | " + " ".join(f"{d:>6}" for d in DEFESAS) + "   veredito")
    print("-" * 74)
    for pen, dmg in variantes:
        base = Ataque("b", 5, [10], 3, brutal=True, vantagem=vantagem)
        linha, ganhos = [], []
        for d in DEFESAS:
            v = Ataque("v", 5 - pen, [10], 3 + dmg, brutal=True, vantagem=vantagem)
            g = v.dano_esperado(d) / base.dano_esperado(d) - 1
            ganhos.append(g)
            linha.append(f"{g:>+5.0%}")
        if all(g > 0.05 for g in ganhos):
            veredito = "sempre usar (sem escolha)"
        elif all(g < -0.05 for g in ganhos):
            veredito = "nunca usar (lixo)"
        else:
            veredito = "DECISÃO REAL"
        print(f"{f'-{pen} / +{dmg}':>12} | " + " ".join(linha) + f"   {veredito}")

    print("\nA penalidade tem que ser grande o bastante para que o bônus de dano")
    print("deixe de compensar contra alvos de DEF alta. Aí nasce a decisão.")


# ---------------------------------------------------------------------------
if __name__ == "__main__":
    teste_ataque_pesado()
    teste_habilidade_vs_arma()
    teste_resistencia_das_classes()
    teste_sacrificio_de_atributo()
    teste_besta_vs_arco()
    teste_letalidade_interna()
    varredura_ataque_pesado(vantagem=True)
    varredura_ataque_pesado(vantagem=False)
    teste_furioso_ab()
    teste_trio()
    print()

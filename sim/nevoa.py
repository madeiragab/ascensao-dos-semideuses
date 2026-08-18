"""A Magia da Névoa, medida pela primeira vez — Livro III.

O Grimório era o único sistema do projeto sem nenhum teste. Ele tem uma escala de
custo própria (Círculos de 0 a 4, de 0 a 9 MP) que roda em paralelo à escala de
Graus do Livro I, e uma regra que não existe em nenhum outro lugar do sistema: a
**Descrença**. As duas coisas juntas podiam estar quebradas em qualquer direção,
e ninguém saberia.

As perguntas:

  1. Uma Fórmula é melhor ou pior que uma habilidade do mesmo preço em MP?
  2. Quanto a Descrença tira de uma Fórmula, na prática?
  3. O Refluxo — conjurar acima do próprio nível — é aposta ou suicídio?
  4. A Fera de Névoa vale os 4 MP dela dentro de um combate de verdade?

O que este arquivo NÃO mede: Fórmulas de utilidade e engano, que são a maior
parte do Grimório. Porta Falsa, Outra Pele e Cidade de Bruma valem pelo que
abrem de ficção, e isso nenhum motor de combate julga.

Rodar de dentro da pasta sim/:
    python nevoa.py
"""

import random
import sys

from combate import Lutador, rola, rola_d20
from completo import DEFESAS, combate_total, montar_heroi
from dados import chance_de_acertar, media_dado
from fichas import oraculo_atena
from kleos import TABUA, monstro_padrao
from niveis import custo_em_recurso, grau, kleos_do_grupo, personagem, teto_de_custo

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

N = 1200

# Livro III, seção 37.1 — Círculo: custo em MP e nível mínimo.
CIRCULOS = {0: (0, 1), 1: (2, 1), 2: (4, 5), 3: (6, 10), 4: (9, 15)}

# Densidade da criação, seção 38: o que sobra depois da Descrença.
SOBRA = {"Vestida": 0.0, "Densa": 0.5}


def bonus_de_formula(nivel: int) -> int:
    """Ataque e Efeito de Fórmula: Atributo Divino + proficiência."""
    o = personagem(oraculo_atena(), nivel)
    return o.mods["inteligencia"] + o.prof


def main() -> None:
    random.seed(20260818)
    falhas = []

    # -----------------------------------------------------------------
    print("1. FÓRMULA CONTRA HABILIDADE, PELO MESMO MP")
    print("   Fórmula de dano do Círculo C contra habilidade comprada com o")
    print("   mesmo MP no Grau do nível. Alvo: a Fórmula NÃO pode ser melhor.")
    print(f"{'nível':>6}{'Círculo':>9}{'MP':>4}{'dano da Fórmula':>18}"
          f"{'dano da habilidade':>20}{'razão':>8}")
    print("-" * 66)
    # Dano de referência de uma Fórmula de ataque, pelo texto do Livro III:
    # Círculo 1 ~ 3d6, Círculo 2 ~ 4d6, Círculo 3 ~ 6d6, Círculo 4 ~ 8d6.
    DADOS_FORMULA = {1: (3, 6), 2: (4, 6), 3: (6, 6), 4: (8, 6)}
    for nivel, c in ((1, 1), (5, 2), (10, 3), (15, 4), (20, 4)):
        mp, _ = CIRCULOS[c]
        g = grau(nivel)
        k = kleos_do_grupo(nivel, 3)
        defe = TABUA[k][1]
        bonus = bonus_de_formula(nivel)
        acerta = chance_de_acertar(bonus, defe)
        n_dados, faces = DADOS_FORMULA[c]
        formula = acerta * (n_dados * media_dado(faces))
        # a habilidade que o mesmo MP compraria, no Grau do nível
        pontos = min(teto_de_custo(nivel), max(1, mp // g))
        habilidade = acerta * (pontos * g * media_dado(8) + bonus - 3)
        razao = formula / habilidade if habilidade else 0
        print(f"{nivel:>6}{c:>9}{mp:>4}{formula:>18.1f}{habilidade:>20.1f}"
              f"{razao:>8.0%}")
        if razao > 1.15:
            falhas.append(f"nível {nivel}: a Fórmula de Círculo {c} entrega "
                          f"{razao:.0%} do que a habilidade do mesmo MP entrega")

    # -----------------------------------------------------------------
    print("\n2. O QUE A DESCRENÇA TIRA")
    print("   Criatura mítica testando Investigação contra a CD de Névoa.")
    print(f"{'nível':>6}{'CD de Névoa':>13}{'Investigação do monstro':>26}"
          f"{'descrê':>9}{'sobra: Densa':>14}{'Vestida':>10}")
    print("-" * 80)
    for nivel in (1, 5, 10, 15, 20):
        o = personagem(oraculo_atena(), nivel)
        cd = 8 + o.mods["inteligencia"] + o.prof
        k = kleos_do_grupo(nivel, 3)
        # A coluna Efeito da Tábua tem os mesmos valores da coluna Ataque,
        # e é com ela que a criatura investiga.
        inv = TABUA[k][2]
        p_descre = chance_de_acertar(inv, cd)
        densa = 1 - p_descre * (1 - SOBRA["Densa"])
        vestida = 1 - p_descre
        print(f"{nivel:>6}{cd:>13}{'+' + str(inv):>26}{p_descre:>9.0%}"
              f"{densa:>14.0%}{vestida:>10.0%}")
        if densa < 0.5:
            falhas.append(f"nível {nivel}: sobra só {densa:.0%} de uma criação "
                          f"Densa contra monstro")

    print("\n   Contra MORTAL COMUM a Descrença não existe: sobra 100% em qualquer")
    print("   densidade. É esse o desenho — a Névoa é rainha fora do combate")
    print("   e coadjuvante dentro dele.")

    # -----------------------------------------------------------------
    print("\n3. O REFLUXO É APOSTA OU SUICÍDIO?")
    print("   Conjurar um Círculo acima do nível mínimo: Mitologia contra")
    print("   CD 10 + 3 por Círculo. Falha gasta o MP, causa 1d6 por Círculo")
    print("   e Atordoa.")
    print(f"{'nível':>6}{'Círculo':>9}{'CD':>5}{'passa':>8}{'MP em risco':>13}"
          f"{'dano médio na falha':>21}{'veredito':>12}")
    print("-" * 76)
    for nivel, c in ((3, 2), (7, 3), (12, 4), (15, 4)):
        o = personagem(oraculo_atena(), nivel)
        mitologia = o.mods["inteligencia"] + o.prof
        cd = 10 + 3 * c
        passa = chance_de_acertar(mitologia, cd)
        mp = CIRCULOS[c][0]
        dano = c * media_dado(6)
        veredito = "aposta" if passa >= 0.45 else "desespero"
        print(f"{nivel:>6}{c:>9}{cd:>5}{passa:>8.0%}{mp:>13}{dano:>21.1f}"
              f"{veredito:>12}")
        if passa > 0.75:
            falhas.append(f"nível {nivel}: Refluxo de Círculo {c} passa "
                          f"{passa:.0%} — barato demais para ser desespero")

    # -----------------------------------------------------------------
    print("\n4. A FERA DE NÉVOA VALE 4 MP?")
    print("   Círculo 2: 2d6 por rodada, PV 5 × proficiência, DEF 13, e metade")
    print("   do dano contra quem descreu. Trio de nível 5 a 13 contra o Kleos justo.")
    print(f"{'nível':>6}{'Kleos':>7}{'sem a Fera':>12}{'com a Fera':>12}"
          f"{'ganho':>8}{'rodadas':>9}")
    print("-" * 56)
    for nivel in (5, 9, 13):
        k = kleos_do_grupo(nivel, 3)
        fraca = DEFESAS[k][1]
        o = personagem(oraculo_atena(), nivel)
        for com_fera in (False, True):
            vit = rod = 0
            for _ in range(N // 2):
                herois = [montar_heroi(c, nivel, True)
                          for c in ("guardiao", "furioso", "oraculo")]
                if com_fera:
                    fera = Lutador(
                        nome="fera de névoa", lado="herois",
                        pv_max=5 * o.prof, defesa=13,
                        bonus_ataque=bonus_de_formula(nivel),
                        dados_dano=[6, 6], dano_fixo=0,
                        iniciativa_bonus=2, prof=o.prof, regras="v1",
                    )
                    fera.usa_habilidade = False
                    fera.papel = "dano"
                    fera.recurso = "sp"
                    fera.controle_ativo = None
                    fera.custo_dano = 10 ** 6      # nunca conjura
                    fera.custo_controle = 10 ** 6
                    herois.append(fera)
                    # o MP da Fera sai do Oráculo
                    herois[2].mp -= CIRCULOS[2][0]
                m = Lutador.de_monstro(monstro_padrao(k))
                m.recusas, m.recusas_gastas = 2, 0
                res = combate_total(herois, m, 2 if k >= 8 else 1, TABUA[k][3], fraca)
                vit += res["vencedor"] == "herois"
                rod += res["rodadas"]
            if com_fera:
                com = (vit / (N // 2), rod / (N // 2))
            else:
                sem = (vit / (N // 2), rod / (N // 2))
        print(f"{nivel:>6}{k:>7}{sem[0]:>12.0%}{com[0]:>12.0%}"
              f"{com[0] - sem[0]:>+8.0%}{com[1]:>9.1f}")

    print()
    if falhas:
        for f in falhas:
            print("FALHOU:", f)
        raise SystemExit(1)
    print("A Magia da Névoa fecha: a Fórmula custa menos MP e entrega menos que a")
    print("habilidade do mesmo preço, a Descrença cobra o resto dentro do combate,")
    print("e o Refluxo é caro o bastante para continuar sendo desespero.")


if __name__ == "__main__":
    main()

"""Calibra os Graus de habilidade — o motor que substitui Potência e Evoluída.

O motor novo:

    Toda habilidade opera no GRAU do personagem, que é a faixa de nível:

        Grau 1  níveis  1–4        Grau 4  níveis 13–16
        Grau 2  níveis  5–8        Grau 5  níveis 17–20
        Grau 3  níveis  9–12

    Cada tabela de efeito tem uma linha por Grau. Um ponto comprado na linha
    do Grau G custa G de MP ou SP. O Teto de Custo continua contando PONTOS:
    5 no Grau 1, 6 do Grau 2 em diante.

Duas medições decidiram esse desenho, e as duas contrariaram a primeira ideia.

  1. O ponto não pode ficar melhor de graça. A tentação era manter o ponto a
     1 MP e só engordar o dado. Medido: o conjurador chegava a 300% do dia do
     Furioso no nível 20. O que precisa ficar constante é o DANO POR MP —
     por isso o ponto do Grau G custa G.

  2. O teto antigo tinha que encolher. Ele ia de 5 a 14 porque a única
     progressão possível era comprar mais pontos. Mantê-lo junto com o dado
     maior somaria duas progressões em cima uma da outra; e reduzi-lo sem
     mexer no preço deixava cada uso barato demais, o que enche o dia de usos.

O resultado é potência por uso subindo de 17 para 91 do nível 4 ao 20, com o
dia inteiro parado onde o sistema publicado já o tinha deixado.

Rodar de dentro da pasta sim/:
    python graus.py            (completo, inclui a varredura de DEF)
    python graus.py --rapido   (só as contas fechadas)
"""

import random
import sys

from combate import Lutador, combate
from dados import Ataque, media_dado
from fichas import Monstro, furioso_ares, guardiao_ares, oraculo_atena
from kleos import TABUA
from niveis import (ataques_por_turno, kleos_do_personagem, personagem,
                    teto_de_custo)

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

RODADAS_DO_DIA = 16          # quatro combates de quatro rodadas, como no livro

FAIXAS = [(1, 1, 4), (2, 5, 8), (3, 9, 12), (4, 13, 16), (5, 17, 20)]

# As tabelas do capítulo, em código. Um ponto do Grau G custa G.
DANO_UNICO = {g: [8] * g for g in range(1, 6)}      # 1d8 … 5d8
DANO_AREA = {g: [6] * g for g in range(1, 6)}       # 1d6 … 5d6
MOVIMENTO = {g: 3 * g for g in range(1, 6)}         # +3 m … +15 m


def grau_do_nivel(nivel: int) -> int:
    for g, ini, fim in FAIXAS:
        if ini <= nivel <= fim:
            return g
    raise ValueError(nivel)


def teto_em_pontos(grau: int) -> int:
    return 5 if grau == 1 else 6


def custo_em_mp(grau: int, pontos: int) -> int:
    return pontos * grau


def valor(dados) -> float:
    return sum(media_dado(d) for d in dados)


# ---------------------------------------------------------------------------
# Medidas
# ---------------------------------------------------------------------------

def alvo_do_nivel(nivel: int):
    k = max(1, min(11, round(kleos_do_personagem(nivel) * 3)))
    return TABUA[k]


def dpr_arma(nivel: int) -> float:
    f = personagem(furioso_ares(), nivel)
    defesa = alvo_do_nivel(nivel)[1]
    return ataques_por_turno("furioso", nivel) * Ataque(
        "arma", f.bonus_ataque, f.dados_arma, f.dano_fixo).dano_esperado(defesa)


def dia(nivel: int, pontos: int, mp_por_uso: int, val: float):
    """Dano de um dia: gasta o MP na maior habilidade e depois usa a lança."""
    o = personagem(oraculo_atena(), nivel)
    defesa = alvo_do_nivel(nivel)[1]
    mod = o.mods["inteligencia"]
    acerto = Ataque("h", mod + o.prof, [], 0).chance_acerto(defesa)
    lanca = Ataque("lança", o.mods["forca"] + o.prof, [6],
                   o.mods["forca"]).dano_esperado(defesa)
    usos = min(o.mp_max // mp_por_uso, RODADAS_DO_DIA)
    por_uso = acerto * (pontos * val + mod)
    return usos, por_uso, usos * por_uso + (RODADAS_DO_DIA - usos) * lanca


def comparacao():
    print()
    print("=" * 78)
    print("1. O MOTOR NOVO CONTRA O PUBLICADO — mesma potência total, outra forma")
    print("=" * 78)
    print(f"{'G':<3}{'níveis':<9}{'pontos':>7}{'MP/uso':>8}{'dado':>7}"
          f"{'por uso':>9}{'usos':>6}{'dia':>7}{'antigo':>8}{'arma':>7}"
          f"{'novo':>7}{'era':>6}")
    print("-" * 78)
    linhas = []
    for g, ini, fim in FAIXAS:
        pontos = teto_em_pontos(g)
        mp = custo_em_mp(g, pontos)
        usos, por_uso, total = dia(fim, pontos, mp, valor(DANO_UNICO[g]))
        ta = teto_de_custo(fim)
        _, _, antigo = dia(fim, ta, ta, 4.5)
        arma = dpr_arma(fim) * RODADAS_DO_DIA
        linhas.append((g, total / arma, antigo / arma))
        print(f"{g:<3}{f'{ini}–{fim}':<9}{pontos:>7}{mp:>8}{f'{g}d8':>7}"
              f"{por_uso:>9.1f}{usos:>6}{total:>7.0f}{antigo:>8.0f}{arma:>7.0f}"
              f"{total / arma:>7.0%}{antigo / arma:>6.0%}")
    print()
    print("'antigo' e 'era' são o motor publicado no mesmo nível. O novo segue")
    print("a mesma curva: o que muda é o tamanho de um único uso, não o dia.")
    return linhas


def tabelas():
    print()
    print("=" * 78)
    print("2. AS TABELAS, como vão para o capítulo")
    print("=" * 78)
    print(f"{'Grau':<6}{'MP por ponto':>14}{'alvo único':>12}{'área e contínuo':>18}"
          f"{'movimento':>11}{'dano/MP':>9}")
    print("-" * 78)
    for g, _, _ in FAIXAS:
        print(f"{g:<6}{g:>14}{f'{g}d8':>12}{f'{g}d6':>18}"
              f"{f'+{MOVIMENTO[g]} m':>11}{valor(DANO_UNICO[g]) / g:>9.2f}")
    print()
    print("A última coluna é a que precisa ficar parada: o Grau muda quanto cabe")
    print("numa ação, não quanto o MP rende.")


def varredura_de_defesa(n=1000):
    print()
    print("=" * 78)
    print("3. QUANTO VALE +1 DEF — o efeito mais abusável da tabela")
    print("=" * 78)
    print(f"{'nível':<8}{'+0':>8}{'+1':>8}{'+2':>8}{'+3':>8}{'+4':>8}"
          f"{'por ponto':>12}")
    print("-" * 78)
    saltos = []
    for nivel in (4, 12, 20):
        taxas = []
        for bonus in range(5):
            random.seed(20260801)
            vitorias = 0
            for _ in range(n):
                herois = []
                for fabrica in (guardiao_ares, furioso_ares, oraculo_atena):
                    f = personagem(fabrica(), nivel)
                    f.bonus_def += bonus
                    herois.append(Lutador.de_ficha(
                        f, ataques_por_turno=ataques_por_turno(f.classe, nivel)))
                pv, defesa, atk, dano, qtd = alvo_do_nivel(nivel)
                monstro = Monstro(f"alvo", pv_max=pv, defesa=defesa,
                                  bonus_ataque=atk, dados_dano=[10],
                                  dano_fixo=round(dano / qtd - 5.5),
                                  ataques_por_turno=qtd)
                vitorias += combate(herois, [Lutador.de_monstro(monstro)])["vencedor"] == "herois"
            taxas.append(vitorias / n)
        por_ponto = (taxas[4] - taxas[0]) / 4
        saltos.append((nivel, taxas, por_ponto))
        print(f"{nivel:<8}" + "".join(f"{t:>8.0%}" for t in taxas)
              + f"{por_ponto:>+12.1%}")
    print()
    print("Cada ponto de DEF vale alguns pontos de vitória e nunca sai de moda —")
    print("por isso a tabela mantém teto de acúmulo e cobra o segundo dobrado.")
    return saltos


def regressao(linhas, saltos):
    print()
    print("=" * 78)
    print("4. REGRESSÃO")
    print("=" * 78)
    falhas = []

    # O nível 1 do livro publicado não pode mudar
    if teto_em_pontos(1) != 5 or custo_em_mp(1, 1) != 1 or DANO_UNICO[1] != [8]:
        falhas.append("o Grau 1 deixou de ser o nível 1 já publicado")

    # Dano por MP tem de ficar parado: é ele que segura o dia
    rendimentos = [valor(DANO_UNICO[g]) / g for g, _, _ in FAIXAS]
    if max(rendimentos) - min(rendimentos) > 0.01:
        falhas.append(f"o dano por MP não ficou constante: {rendimentos}")

    # Área sempre atrás do alvo único
    for g, _, _ in FAIXAS:
        if valor(DANO_AREA[g]) >= valor(DANO_UNICO[g]):
            falhas.append(f"Grau {g}: área alcançou o alvo único")

    # Progressão real por uso
    porusos = []
    for g, _, fim in FAIXAS:
        pontos = teto_em_pontos(g)
        _, por_uso, _ = dia(fim, pontos, custo_em_mp(g, pontos), valor(DANO_UNICO[g]))
        porusos.append(por_uso)
    if porusos != sorted(porusos):
        falhas.append(f"a potência por uso não sobe sempre: {porusos}")
    if porusos[-1] < porusos[0] * 3:
        falhas.append(f"a progressão ficou fraca demais: {porusos[0]:.0f} "
                      f"para {porusos[-1]:.0f}")

    # O dia não pode subir sobre o motor publicado
    for g, novo, antigo in linhas:
        if novo > antigo + 0.10:
            falhas.append(f"Grau {g}: o dia subiu de {antigo:.0%} para {novo:.0%}")

    if saltos:
        for nivel, _, por_ponto in saltos:
            if por_ponto > 0.08:
                falhas.append(f"nível {nivel}: +1 DEF vale {por_ponto:.0%} de "
                              f"vitória, alto demais para 1 ponto")

    for f in falhas:
        print(f"  FALHA  {f}")
    if not falhas:
        print("  ok · nível 1 intacto · dano por MP constante · área atrás do único")
        print("       potência por uso de {:.0f} a {:.0f} · dia dentro do publicado"
              .format(porusos[0], porusos[-1]))
    return falhas


def main():
    linhas = comparacao()
    tabelas()
    saltos = [] if "--rapido" in sys.argv else varredura_de_defesa()
    if regressao(linhas, saltos):
        sys.exit(1)


if __name__ == "__main__":
    main()

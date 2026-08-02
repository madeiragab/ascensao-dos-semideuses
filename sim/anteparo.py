"""Mede o Anteparo — a habilidade de classe que faltava ao Guardião.

Furioso e Oráculo entram na mesa com uma habilidade de classe de graça;
o Guardião não tinha nenhuma. O conserto dele na revisão v1 foi todo
numérico — PV, armadura, defesas treinadas — e a frente qualitativa
ficou anotada em regras/v1-numeros.md como dívida.

O Anteparo:

    Uma vez por rodada, sem ação e sem SP, o dano que atinge um aliado
    adjacente é reduzido pela metade da sua proficiência, mínimo 1.

Por que essa forma e não outra:

  - Não é reação. Interceptar, Escudo Vínculo e Represália já disputam a
    reação do Guardião; mais uma coisa naquela fila não seria escolha, seria
    fila. Sem custo de ação, ela sempre acontece.
  - Reduz o dano em vez de transferi-lo. A dívida escrita dizia exatamente
    isso: "Interceptar transfere dano sem reduzi-lo".
  - Não marca, não provoca, não dá DEF. Não pisa em Postura Desafiadora nem
    em Muro de Escudos, que continuam sendo escolhas de técnica.
  - Metade da proficiência, não a proficiência inteira. Medida cheia, ela dava
    +14,3% de vitória num bando de nível 20 — obrigatória. Ver anteparo_valor().

O limite que ela precisa respeitar é o mesmo das técnicas: alguns pontos de
vitória em pelo menos um cenário, nunca dez ou mais. Acima disso vira a
classe obrigatória do grupo.

Rodar de dentro da pasta sim/:
    python anteparo.py
"""

import random
import sys

import combate
from calibrar_kleos import monstro
from combate import Lutador, combate as lutar
from equilibrio import montar_grupo

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

N = 2000
NIVEIS = (1, 5, 10, 15, 20)


def cenario_chefe(nivel: int):
    k = {1: 3, 5: 5, 10: 7, 15: 8, 20: 9}[nivel]
    return [Lutador.de_monstro(monstro(k))]


# Bandos calibrados um a um até o trio ficar por volta de 80% de vitória sem
# a habilidade. Sem isso a coluna satura em 100% e não mede nada: um bando de
# criaturas fracas some diante de um grupo de nível alto.
BANDOS = {1: (4, 1), 5: (6, 2), 10: (6, 3), 15: (8, 3), 20: (8, 4)}


def cenario_bando(nivel: int):
    qtd, k = BANDOS[nivel]
    return [Lutador.de_monstro(monstro(k), f" {i}") for i in range(qtd)]


def medir(nivel: int, cenario, ligado: bool) -> float:
    combate.ANTEPARO_ATIVO = ligado
    random.seed(31415)
    vitorias = 0
    for _ in range(N):
        grupo = montar_grupo(nivel, [], "guardiao", substituir=False)()
        vitorias += lutar(grupo, cenario(nivel))["vencedor"] == "herois"
    return vitorias / N


def main():
    print("=" * 78)
    print(f"ANTEPARO — habilidade de classe do Guardião · {N} combates por célula")
    print("=" * 78)
    print(f"{'nível':<7}{'chefe sem':>11}{'chefe com':>11}{'Δ':>8}"
          f"{'bando sem':>12}{'bando com':>11}{'Δ':>8}")
    print("-" * 78)

    piores = []
    for nivel in NIVEIS:
        sc = medir(nivel, cenario_chefe, False)
        cc = medir(nivel, cenario_chefe, True)
        sb = medir(nivel, cenario_bando, False)
        cb = medir(nivel, cenario_bando, True)
        piores.append((nivel, cc - sc, cb - sb))
        print(f"{nivel:<7}{sc:>11.1%}{cc:>11.1%}{cc - sc:>+8.1%}"
              f"{sb:>12.1%}{cb:>11.1%}{cb - sb:>+8.1%}")

    combate.ANTEPARO_ATIVO = True

    print()
    print("=" * 78)
    print("REGRESSÃO")
    print("=" * 78)
    falhas = []
    for nivel, dc, db in piores:
        maior = max(dc, db)
        if maior >= 0.10:
            falhas.append(f"nível {nivel}: {maior:+.1%} — forte demais, "
                          f"vira classe obrigatória")
    if max(max(dc, db) for _, dc, db in piores) <= 0.01:
        falhas.append("o Anteparo não mudou nada em nenhum nível: "
                      "ninguém sentiria a habilidade na mesa")

    for f in falhas:
        print(f"  FALHA  {f}")
    if not falhas:
        print("  ok · muda a vitória em algum cenário e em nenhum passa de dez pontos")
    return falhas


if __name__ == "__main__":
    if main():
        sys.exit(1)

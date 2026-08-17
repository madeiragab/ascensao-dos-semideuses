"""Prova que o Grau do item segura a carreira inteira — Parte VII do Livro I.

A dívida que este arquivo fecha: o dano de arma não acompanhava o PV dos
monstros. Do nível 5 ao 20 o ataque com arma crescia 15% enquanto o PV do
monstro do encontro justo crescia 250%, e o combate ia de 2 para 11 rodadas.

O conserto é a tabela de Grau da Forja: o item dá dados de arma e DEF, de graça,
por Grau. Aqui isso é medido em combate simulado, não em média de papel.

Alvos verificados:
  - o combate dura de 2 a 4,5 rodadas do nível 3 ao 20;
  - o trio vence pelo menos 85% dos encontros justos;
  - o monstro acerta o Guardião entre 45% e 60%, sem derreter a DEF;
  - o crítico de habilidade somando metade nunca chega ao dobro do que apagava.

Rodar de dentro da pasta sim/:
    python forja.py
"""

import random
import sys

from combate import Lutador, rodar_muitos
from dados import chance_de_acertar
from fichas import furioso_ares, guardiao_ares, oraculo_atena
from kleos import TABUA, monstro_padrao
from niveis import (ataques_por_turno, grau, kleos_do_grupo, personagem,
                    teto_de_custo)

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

N = 2000
NIVEIS = [1, 3, 5, 7, 9, 11, 13, 15, 17, 20]

# Parte VII, seção 47 — o que o Grau do item dá.
#   nível mínimo, dados de arma somados, bônus de ataque e dano, bônus de DEF
GRAU_ITEM = [
    ("Mortal",     1,  0, 0, 0),
    ("Consagrado", 3,  0, 1, 1),
    ("Heroico",    6,  1, 1, 1),
    ("Mítico",     10, 1, 2, 2),
    ("Lendário",   15, 2, 2, 3),
]

DADO_DA_ARMA = {"furioso": 10, "guardiao": 8, "oraculo": 6}


def item_do_nivel(nivel: int):
    """O melhor Grau que aquele nível consegue usar."""
    melhor = GRAU_ITEM[0]
    for linha in GRAU_ITEM:
        if nivel >= linha[1]:
            melhor = linha
    return melhor


def heroi(classe: str, nivel: int, com_item: bool) -> Lutador:
    f = personagem({"furioso": furioso_ares, "guardiao": guardiao_ares,
                    "oraculo": oraculo_atena}[classe](), nivel)
    _, _, dados_extra, bonus, def_item = item_do_nivel(nivel) if com_item else ("", 0, 0, 0, 0)
    return Lutador(
        nome=classe, lado="herois", pv_max=f.pv_max,
        defesa=f.defesa + def_item,
        bonus_ataque=f.bonus_ataque + bonus,
        dados_dano=[DADO_DA_ARMA[classe]] * (1 + dados_extra),
        dano_fixo=f.dano_fixo + bonus,
        iniciativa_bonus=f.mods["destreza"], prof=f.prof,
        sp_max=f.sp_max, mp_max=f.mp_max,
        ataques_por_turno=ataques_por_turno(classe, nivel),
        brutal=(classe == "furioso"), classe=classe,
        mod_sabedoria=f.mods["sabedoria"], tecnicas=f.tecnicas, regras="v1",
    )


def mede(nivel: int, com_item: bool) -> dict:
    k = kleos_do_grupo(nivel, 3)
    return rodar_muitos(
        lambda: [heroi(c, nivel, com_item) for c in ("guardiao", "furioso", "oraculo")],
        lambda: [Lutador.de_monstro(monstro_padrao(k))],
        n=N,
    )


def main() -> None:
    random.seed(20260816)
    falhas = []

    print("A carreira inteira, contra o monstro do Kleos justo")
    print(f"{'nível':>6}{'Kleos':>7}{'item':>13}"
          f"{'sem item: vitórias':>20}{'rodadas':>9}"
          f"{'com item: vitórias':>20}{'rodadas':>9}")
    print("-" * 84)
    for n in NIVEIS:
        sem, com = mede(n, False), mede(n, True)
        print(f"{n:>6}{kleos_do_grupo(n,3):>7}{item_do_nivel(n)[0]:>13}"
              f"{sem['taxa_vitoria']:>19.0%}{sem['rodadas_media']:>9.1f}"
              f"{com['taxa_vitoria']:>19.0%}{com['rodadas_media']:>9.1f}")
        if n >= 3:
            if not 2.0 <= com["rodadas_media"] <= 4.5:
                falhas.append(f"nível {n}: {com['rodadas_media']:.1f} rodadas, "
                              f"fora da faixa de 2 a 4,5")
            if com["taxa_vitoria"] < 0.85:
                falhas.append(f"nível {n}: só {com['taxa_vitoria']:.0%} de vitórias")

    print("\nA DEF continua importando?")
    print(f"{'nível':>6}{'ataque do monstro':>19}{'DEF':>6}{'ele acerta':>12}")
    print("-" * 45)
    for n in NIVEIS:
        g = personagem(guardiao_ares(), n)
        defesa = g.defesa + item_do_nivel(n)[4]
        p = round(chance_de_acertar(TABUA[kleos_do_grupo(n, 3)][2], defesa), 2)
        print(f"{n:>6}{TABUA[kleos_do_grupo(n,3)][2]:>+19}{defesa:>6}{p:>12.0%}")
        # 60% é o topo aceitável, e ele aparece de verdade nos níveis em que o
        # grupo acabou de mudar de faixa de Kleos: o monstro subiu um degrau e a
        # armadura ainda não. O que não pode voltar é o 70% de antes do conserto.
        if not 0.45 <= p <= 0.60:
            falhas.append(f"nível {n}: o monstro acerta {p:.0%}, fora de 45% a 60%")

    print("\nO crítico de habilidade, dobrando contra somando metade")
    print(f"{'nível':>6}{'dados':>7}{'PV do monstro':>15}{'dobrando':>11}"
          f"{'metade':>9}{'quanto sobrou':>15}")
    print("-" * 64)
    for n in NIVEIS:
        dados = teto_de_custo(n) * grau(n)
        pv = TABUA[kleos_do_grupo(n, 3)][0]
        dobra, meio = dados * 9 + 3, dados * 6.75 + 3
        print(f"{n:>6}{dados:>7}{pv:>15}{dobra/pv:>10.0%}{meio/pv:>9.0%}"
              f"{meio/dobra:>15.0%}")
        if meio >= dobra:
            falhas.append(f"nível {n}: a metade não é menor que o dobro")

    print()
    if falhas:
        for f in falhas:
            print("FALHOU:", f)
        raise SystemExit(1)
    print("A Forja segura os 20 níveis: combate de 2 a 4,5 rodadas, vitória acima")
    print("de 85%, e o monstro acertando entre 45% e 60% o tempo todo.")


if __name__ == "__main__":
    main()

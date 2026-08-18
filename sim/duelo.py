"""Semideus contra semideus — o combate que o sistema nunca mediu.

Todo o balanceamento até aqui olhou para o grupo contra o monstro. Mas a mesa
duela: o rival da mesma casa, a cópia na Soleira, o irmão que escolheu o outro
lado. Um sistema pode estar perfeito contra monstro e podre em duelo, e ninguém
descobre até acontecer.

O que este arquivo mede:

  1. paridade — alguma classe domina o 1x1?
  2. o espelho — a mesma classe contra si mesma deve dar 50%, senão há vantagem
     escondida em quem age primeiro;
  3. quanto a iniciativa vale, que é a suspeita óbvia num duelo curto;
  4. o que o arsenal faz: com e sem habilidade, com e sem controle.

Os dois duelistas entram completos: equipamento no Grau do nível pela tabela da
Forja, habilidade de dano no Teto e, para quem tem o papel, controle por Rolagem
de Efeito contra a defesa passiva do outro.

Rodar de dentro da pasta sim/:
    python duelo.py
"""

import itertools
import random
import sys

from combate import Lutador, rola_d20
from completo import (golpe_de_habilidade, gastar, montar_heroi, recurso_de,
                      rolagem_de_efeito)
from fichas import furioso_ares, guardiao_ares, oraculo_atena
from niveis import personagem

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

N = 2000
NIVEIS = (1, 5, 10, 15, 20)
CLASSES = ("guardiao", "furioso", "oraculo")

# Defesa passiva de um personagem, para a Rolagem de Efeito do outro lado:
# 14 + atributo + proficiência quando treinada, 10 + atributo quando não.
BASE_TREINADA = 14


def defesa_passiva(classe: str, nivel: int) -> int:
    """A defesa passiva mais fraca do duelista — é nela que o controle bate."""
    f = personagem({"guardiao": guardiao_ares, "furioso": furioso_ares,
                    "oraculo": oraculo_atena}[classe](), nivel)
    # cada classe treina duas; a terceira chega no nível 10
    treinadas = {"guardiao": ("constituicao", "sabedoria"),
                 "furioso": ("constituicao", "destreza"),
                 "oraculo": ("sabedoria", "destreza")}[classe]
    fracas = [a for a in ("constituicao", "destreza", "sabedoria")
              if a not in treinadas]
    atr = fracas[0]
    if nivel >= 10:
        return BASE_TREINADA + f.mods[atr] + f.prof
    return 10 + f.mods[atr]


def duelista(classe: str, nivel: int, lado: str, com_habilidade=True,
             com_controle=True) -> Lutador:
    lut = montar_heroi(classe, nivel, com_habilidade)
    lut.lado = lado
    lut.nome = classe
    if not com_controle:
        lut.papel = "dano"
    return lut


def duelo(a: Lutador, b: Lutador, fraca_a: int, fraca_b: int, max_rodadas=30):
    """Um contra um, com o arsenal inteiro dos dois lados."""
    ordem = sorted([a, b], key=lambda c: rola_d20() + c.iniciativa_bonus,
                   reverse=True)
    primeiro = ordem[0]
    for rodada in range(1, max_rodadas + 1):
        for lut in ordem:
            if not lut.vivo:
                continue
            alvo = b if lut is a else a
            fraca_do_alvo = fraca_b if lut is a else fraca_a
            if not alvo.vivo:
                break

            if lut.perde_o_turno:
                lut.resolver_fim_de_turno()
            else:
                agiu = False
                if lut.usa_habilidade:
                    if (lut.papel == "controle"
                            and recurso_de(lut) >= lut.custo_controle
                            and not alvo.perde_o_turno):
                        gastar(lut, lut.custo_controle)
                        if rolagem_de_efeito(lut, alvo, fraca_do_alvo):
                            alvo.aplicar_condicao("perde_turno", 1)
                        agiu = True
                    elif (lut.papel == "dano"
                          and recurso_de(lut) >= lut.custo_dano):
                        gastar(lut, lut.custo_dano)
                        golpe_de_habilidade(lut, alvo)
                        agiu = True
                if not agiu:
                    lut.turno([lut], [alvo])

            if not alvo.vivo:
                return {"vencedor": lut.nome, "rodadas": rodada,
                        "quem_comecou": primeiro.nome,
                        "ganhou_quem_comecou": lut is primeiro}
    return {"vencedor": "tempo", "rodadas": max_rodadas,
            "quem_comecou": primeiro.nome, "ganhou_quem_comecou": False}


def mede(c1: str, c2: str, nivel: int, n=N, **kw) -> dict:
    fraca1, fraca2 = defesa_passiva(c1, nivel), defesa_passiva(c2, nivel)
    vitorias = rodadas = iniciativa = 0
    for _ in range(n):
        a = duelista(c1, nivel, "herois", **kw)
        b = duelista(c2, nivel, "monstros", **kw)
        r = duelo(a, b, fraca1, fraca2)
        vitorias += r["vencedor"] == c1 if c1 != c2 else r["ganhou_quem_comecou"]
        rodadas += r["rodadas"]
        iniciativa += r["ganhou_quem_comecou"]
    return {"vitoria": vitorias / n, "rodadas": rodadas / n,
            "iniciativa": iniciativa / n}


def main() -> None:
    random.seed(20260818)
    falhas = []

    print("1. O ESPELHO — a mesma classe contra si mesma")
    print("   Aqui 'vitória' é de quem começou. Longe de 50% significa que a")
    print("   iniciativa, e não a ficha, decide o duelo.")
    print(f"{'nível':>6}{'Guardião':>11}{'Furioso':>10}{'Oráculo':>10}{'rodadas':>10}")
    print("-" * 48)
    for nivel in NIVEIS:
        linha, rod = [], 0
        for c in CLASSES:
            r = mede(c, c, nivel, n=N // 2)
            linha.append(r["vitoria"])
            rod += r["rodadas"] / 3
        print(f"{nivel:>6}{linha[0]:>11.0%}{linha[1]:>10.0%}{linha[2]:>10.0%}{rod:>10.1f}")
        for c, v in zip(CLASSES, linha):
            if v > 0.75:
                falhas.append(f"nível {nivel}, {c}: quem começa vence {v:.0%} "
                              f"— a iniciativa decide sozinha")

    print("\n2. PARIDADE — cada classe contra cada outra")
    print("   Todo mundo jogando bem: num 1x1 ninguém gasta ação em controle")
    print("   — ver o quadro 3. Percentual é a vitória da classe da LINHA.")
    print(f"{'nível':>6}{'Guardião x Furioso':>21}{'Guardião x Oráculo':>21}"
          f"{'Furioso x Oráculo':>20}")
    print("-" * 68)
    for nivel in NIVEIS:
        vals = []
        for c1, c2 in itertools.combinations(CLASSES, 2):
            r = mede(c1, c2, nivel, n=N // 2, com_controle=False)
            vals.append(r["vitoria"])
        print(f"{nivel:>6}{vals[0]:>21.0%}{vals[1]:>21.0%}{vals[2]:>20.0%}")
        for (c1, c2), v in zip(itertools.combinations(CLASSES, 2), vals):
            if not 0.20 <= v <= 0.80:
                falhas.append(f"nível {nivel}: {c1} x {c2} deu {v:.0%} — "
                              f"o duelo está decidido antes de rolar")

    print("\n3. O QUE O ARSENAL MUDA NUM DUELO")
    print("   Furioso contra Oráculo, mudando só o que o Oráculo faz com a ação.")
    print(f"{'nível':>6}{'os dois só com arma':>21}"
          f"{'Oráculo gasta MP em dano':>26}{'Oráculo controla':>18}")
    print("-" * 56)
    for nivel in NIVEIS:
        so_arma = mede("furioso", "oraculo", nivel, n=N // 2,
                       com_habilidade=False)
        com_hab = mede("furioso", "oraculo", nivel, n=N // 2,
                       com_controle=False)
        completo = mede("furioso", "oraculo", nivel, n=N // 2)
        print(f"{nivel:>6}{so_arma['vitoria']:>21.0%}{com_hab['vitoria']:>26.0%}"
              f"{completo['vitoria']:>18.0%}")
        if completo["vitoria"] < com_hab["vitoria"]:
            falhas.append(f"nível {nivel}: controlar passou a compensar no 1x1")

    print("\n4. QUANTO VALE COMEÇAR")
    print(f"{'nível':>6}{'quem começa vence':>20}{'rodadas do duelo':>19}")
    print("-" * 46)
    for nivel in NIVEIS:
        total = rod = 0
        for c1, c2 in itertools.combinations_with_replacement(CLASSES, 2):
            r = mede(c1, c2, nivel, n=400)
            total += r["iniciativa"] / 6
            rod += r["rodadas"] / 6
        print(f"{nivel:>6}{total:>20.0%}{rod:>19.1f}")
        if total > 0.80:
            falhas.append(f"nível {nivel}: quem começa vence {total:.0%} "
                          f"dos duelos")

    print()
    if falhas:
        for f in falhas:
            print("FALHOU:", f)
        raise SystemExit(1)
    print("O duelo se sustenta: nenhuma classe domina, o espelho fica perto de")
    print("50%, e começar ajuda sem decidir.")


if __name__ == "__main__":
    main()

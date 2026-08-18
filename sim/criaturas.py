"""Quanto valem, em Kleos, os Poderes e as Arremetidas de uma criatura completa.

A Tábua de Kleos foi calibrada com o monstro CRU: só PV, DEF, ataque e dano. O
próprio Livro II avisava que uma criatura de verdade é mais perigosa que isso, e
que os degraus 6 a 11 eram extrapolação. Este arquivo fecha esse buraco: ensina o
motor de combate a usar as duas peças que mais pesam e mede a diferença.

O que entra:

  Arremetidas   ao fim do turno de cada herói, a criatura ataca uma vez. Recarregam
                todas no início do turno dela (Livro II, seção 15).
  Sopro         Poder de área com Recarga 5–6: dano igual ao dano por rodada, e
                metade em quem passa no Teste de Reflexos (seção 14).

O que NÃO entra, e por que: **Recusas** anulam uma Rolagem de Efeito, e os heróis
deste motor só atacam — não existe Efeito para ser recusado. Medir Recusas exige
antes modelar controle no lado dos jogadores.

Rodar de dentro da pasta sim/:
    python criaturas.py
"""

import random
import sys

from combate import Lutador, rola, rola_d20
from fichas import furioso_ares, guardiao_ares, oraculo_atena
from forja import heroi
from kleos import TABUA, monstro_padrao
from niveis import kleos_do_grupo

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

N = 1500
# Nível do trio e o Kleos que o livro chama de encontro justo para ele.
CENARIOS = [(9, 7), (13, 8), (17, 9), (20, 9)]


def sopro_da_tabua(k: int) -> int:
    """Dano do Sopro: uma rodada inteira de dano, em área (seção 14)."""
    return TABUA[k][3]


def combate_completo(herois, monstro, arremetidas=0, sopro=0, reflexos=5):
    """O laço de combate padrão, mais Arremetidas e um Poder de Sopro.

    Devolve o mesmo relatório de combate(), para poder comparar direto.
    """
    todos = herois + [monstro]
    for c in todos:
        c.aliados = herois if c.lado == "herois" else [monstro]

    ordem = sorted(todos, key=lambda c: rola_d20() + c.iniciativa_bonus, reverse=True)
    sopro_pronto = True

    for rodada in range(1, 41):
        restantes = arremetidas          # recarregam no início da rodada
        for lutador in ordem:
            if not lutador.vivo:
                continue

            if lutador is monstro:
                # Recarga 5–6 antes de agir.
                if sopro and not sopro_pronto and rola(6) >= 5:
                    sopro_pronto = True
                if sopro and sopro_pronto:
                    sopro_pronto = False
                    for h in herois:
                        if not h.vivo:
                            continue
                        passou = rola_d20() + reflexos >= 8 + monstro.bonus_ataque
                        h.receber(sopro // 2 if passou else sopro, monstro)
                else:
                    monstro.turno([monstro], herois)
            else:
                lutador.turno(herois, [monstro])
                # Arremetida ao fim do turno de outra criatura.
                if restantes > 0 and monstro.vivo and any(h.vivo for h in herois):
                    restantes -= 1
                    alvo = max((h for h in herois if h.vivo), key=lambda h: h.pv)
                    monstro.atacar(alvo)

            if not any(h.vivo for h in herois) or not monstro.vivo:
                break

        herois_vivos = any(h.vivo for h in herois)
        if not herois_vivos or not monstro.vivo:
            return {"vencedor": "herois" if herois_vivos else "monstros",
                    "rodadas": rodada,
                    "herois_vivos": sum(1 for h in herois if h.vivo)}

    return {"vencedor": "tempo", "rodadas": 40,
            "herois_vivos": sum(1 for h in herois if h.vivo)}


def mede(nivel, k, arremetidas=0, sopro=0, n=N):
    vitorias = rodadas = de_pe = 0
    for _ in range(n):
        herois = [heroi(c, nivel, True) for c in ("guardiao", "furioso", "oraculo")]
        r = combate_completo(herois, Lutador.de_monstro(monstro_padrao(k)),
                             arremetidas, sopro)
        vitorias += r["vencedor"] == "herois"
        rodadas += r["rodadas"]
        de_pe += r["herois_vivos"]
    return {"vitoria": vitorias / n, "rodadas": rodadas / n, "de_pe": de_pe / n}


def main() -> None:
    random.seed(20260816)
    falhas = []

    print("QUANTO PESA CADA PEÇA (trio com equipamento no Grau do nível)")
    print(f"{'nível':>6}{'Kleos':>7}{'cru':>18}{'+ Arremetidas':>16}"
          f"{'+ Sopro':>12}{'as duas':>12}")
    print("-" * 72)
    for nivel, k in CENARIOS:
        arr = 2 if k >= 8 else 1
        cru = mede(nivel, k)
        so_arr = mede(nivel, k, arremetidas=arr)
        so_sopro = mede(nivel, k, sopro=sopro_da_tabua(k))
        ambos = mede(nivel, k, arremetidas=arr, sopro=sopro_da_tabua(k))
        print(f"{nivel:>6}{k:>7}{cru['vitoria']:>17.0%}"
              f"{so_arr['vitoria']:>15.0%}{so_sopro['vitoria']:>12.0%}"
              f"{ambos['vitoria']:>12.0%}")
        if ambos["vitoria"] > cru["vitoria"]:
            falhas.append(f"nível {nivel}: a criatura completa ficou mais fraca que a crua")

    print("\nA CRIATURA COMPLETA VALE QUANTO DE KLEOS A MAIS?")
    print("Compara a completa do Kleos K com a crua dos degraus vizinhos.")
    print(f"{'nível':>6}{'Kleos':>7}{'completa':>10}{'cru K':>8}"
          f"{'cru K+1':>9}{'cru K+2':>9}{'equivale a':>12}")
    print("-" * 64)
    for nivel, k in CENARIOS:
        arr = 2 if k >= 8 else 1
        completa = mede(nivel, k, arremetidas=arr, sopro=sopro_da_tabua(k))
        crus = {d: mede(nivel, min(11, k + d))["vitoria"] for d in (0, 1, 2)}
        # o degrau cru cuja taxa de vitória mais se parece com a da completa
        equiv = min(crus, key=lambda d: abs(crus[d] - completa["vitoria"]))
        print(f"{nivel:>6}{k:>7}{completa['vitoria']:>10.0%}"
              f"{crus[0]:>8.0%}{crus[1]:>9.0%}{crus[2]:>9.0%}"
              f"{'Kleos ' + str(k + equiv):>12}")

    print("\nE O DESGASTE: quantos heróis ficam de pé")
    print(f"{'nível':>6}{'Kleos':>7}{'cru':>10}{'completa':>11}{'rodadas cru':>13}"
          f"{'rodadas completa':>18}")
    print("-" * 66)
    for nivel, k in CENARIOS:
        arr = 2 if k >= 8 else 1
        cru = mede(nivel, k)
        completa = mede(nivel, k, arremetidas=arr, sopro=sopro_da_tabua(k))
        print(f"{nivel:>6}{k:>7}{cru['de_pe']:>10.1f}{completa['de_pe']:>11.1f}"
              f"{cru['rodadas']:>13.1f}{completa['rodadas']:>18.1f}")

    print()
    if falhas:
        for f in falhas:
            print("FALHOU:", f)
        raise SystemExit(1)
    print("Poderes e Arremetidas agora entram na conta. Recusas continuam de fora:")
    print("os heróis deste motor não fazem Rolagem de Efeito, então não há o que recusar.")


if __name__ == "__main__":
    main()

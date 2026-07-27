"""Valida a Escala de Kleos do Livro II.

A afirmação a testar: uma criatura de Kleos N é um combate justo e perigoso
para N semideuses.

Rodar de dentro da pasta sim/:
    python kleos.py
"""

import sys

from combate import Lutador, rodar_muitos
from dados import Ataque
from fichas import Monstro
from fichas_v1 import furioso_v1, guardiao_v1, oraculo_v1

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

N = 8000

# Tábua de Kleos (Livro II, seção 10): PV, DEF, ataque, dano/rodada, ataques
TABUA = {
    1:  (11,  12,  3,   5, 1),
    2:  (22,  13,  4,   9, 1),
    3:  (36,  14,  5,  14, 2),
    4:  (55,  15,  6,  20, 2),
    5:  (80,  16,  7,  27, 2),
    6:  (115, 17,  8,  35, 2),
    7:  (155, 17,  9,  45, 3),
    8:  (210, 18, 10,  56, 3),
    9:  (280, 19, 11,  70, 3),
    10: (370, 20, 13,  88, 3),
    11: (500, 21, 15, 110, 4),
}

DEGRAUS = {
    1: "Rumor", 2: "Boato", 3: "Conto", 4: "Façanha", 5: "Feito",
    6: "Canção", 7: "Lenda", 8: "Mito", 9: "Epopeia",
    10: "Teomaquia", 11: "Cataclisma",
}


def monstro_padrao(k: int) -> Monstro:
    """A criatura genérica daquele Kleos, sem Traços, Poderes nem Arremetidas.

    É deliberadamente a versão mais crua: só PV, DEF, ataque e dano. Uma criatura
    real do bestiário é mais perigosa que isto, porque tem Poderes e (a partir
    de Kleos 6) Arremetidas — que o motor de combate ainda não modela.
    """
    pv, defesa, atk, dano, n = TABUA[k]
    fixo = round(dano / n - 5.5)   # aproxima a média por ataque com 1d10 + fixo
    return Monstro(
        f"Kleos {k}", pv_max=pv, defesa=defesa, bonus_ataque=atk,
        dados_dano=[10], dano_fixo=fixo, ataques_por_turno=n,
    )


def trio():
    """O grupo de referência do Livro I: Kleos do Grupo = 3."""
    return [
        Lutador.de_ficha(f(), regras="v1")
        for f in (guardiao_v1, furioso_v1, oraculo_v1)
    ]


def titulo(t: str) -> None:
    print()
    print("=" * 72)
    print(t)
    print("=" * 72)


def teste_grupo_kleos_3() -> None:
    titulo("A Regra da Moira — trio de nível 1 (Kleos do Grupo = 3)")
    print(f"{N} combates por linha.\n")
    print(f"{'Kleos':>6} {'Degrau':<12} | {'vitórias':>9} {'rodadas':>8} "
          f"{'de pé':>7} | previsto pela regra")
    print("-" * 72)

    previsto = {
        1: "escaramuça", 2: "escaramuça", 3: "COMBATE JUSTO",
        4: "brutal", 5: "derrota",
    }
    for k in range(1, 6):
        r = rodar_muitos(trio, lambda k=k: [Lutador.de_monstro(monstro_padrao(k))], n=N)
        print(f"{k:>6} {DEGRAUS[k]:<12} | {r['taxa_vitoria']:>8.1%} "
              f"{r['rodadas_media']:>8.2f} {r['sobreviventes_media']:>7.2f} | "
              f"{previsto[k]}")


def teste_um_semideus() -> None:
    titulo("Um semideus sozinho (Kleos 1) contra criaturas de Kleos 1 a 3")
    print("A promessa: 'um semideus dá conta de um Kleos 1'.\n")
    print(f"{'Kleos':>6} | {'Guardião':>10} {'Furioso':>10} {'Oráculo':>10}")
    print("-" * 72)
    for k in (1, 2, 3):
        linha = []
        for f in (guardiao_v1, furioso_v1, oraculo_v1):
            r = rodar_muitos(
                lambda f=f: [Lutador.de_ficha(f(), regras="v1")],
                lambda k=k: [Lutador.de_monstro(monstro_padrao(k))],
                n=N,
            )
            linha.append(f"{r['taxa_vitoria']:>9.1%}")
        print(f"{k:>6} | " + " ".join(linha))
    print("\nO Oráculo fica bem abaixo dos outros dois. Kleos pressupõe um grupo")
    print("com quem bate e quem aguenta — um grupo só de suporte deve contar")
    print("seu Kleos como um a menos (Livro II, seção 4).")


def _kleos_efetivo(taxa: float, base: dict[int, float]) -> float:
    """Em que Kleos ÚNICO aquela taxa de vitória cairia, por interpolação."""
    ks = sorted(base)
    for a, b in zip(ks, ks[1:]):
        if base[a] >= taxa >= base[b]:
            if base[a] == base[b]:
                return float(a)
            return a + (base[a] - taxa) / (base[a] - base[b])
    return float(ks[-1])


def _montar(*pares):
    """Monta um encontro a partir de pares (kleos, quantidade)."""
    def f():
        saida = []
        for k, n in pares:
            for i in range(n):
                saida.append(Lutador.de_monstro(monstro_padrao(k), f" {k}-{i}"))
        return saida
    return f


def teste_formulas_de_encontro() -> None:
    titulo("As fórmulas da seção 5 batem com a simulação?")
    print("Bando (Kleos parecido):      soma × 3/4")
    print("Chefe com lacaios:           chefe + metade da soma dos lacaios\n")

    base = {}
    for k in range(1, 6):
        r = rodar_muitos(trio, lambda k=k: [Lutador.de_monstro(monstro_padrao(k))], n=N)
        base[k] = r["taxa_vitoria"]

    casos = [
        ("3 x Kleos 1",        3 * 0.75, _montar((1, 3))),
        ("4 x Kleos 1",        4 * 0.75, _montar((1, 4))),
        ("2 x Kleos 2",        4 * 0.75, _montar((2, 2))),
        ("2 x Kleos 3",        6 * 0.75, _montar((3, 2))),
        ("1 x K2 + 3 x K1",  2 + 3 * 0.5, _montar((2, 1), (1, 3))),
        ("1 x K3 + 2 x K1",  3 + 2 * 0.5, _montar((3, 1), (1, 2))),
        ("1 x K3 + 4 x K1",  3 + 4 * 0.5, _montar((3, 1), (1, 4))),
    ]

    print(f"{'encontro':<20} {'previsto':>9} | {'vitórias':>9} {'medido':>8} "
          f"{'erro':>7}")
    print("-" * 72)
    for nome, previsto, montar in casos:
        r = rodar_muitos(trio, montar, n=N)
        medido = _kleos_efetivo(r["taxa_vitoria"], base)
        print(f"{nome:<20} {previsto:>9.1f} | {r['taxa_vitoria']:>8.1%} "
              f"{medido:>8.1f} {medido - previsto:>+7.1f}")

    print("\nVários inimigos fracos valem MENOS que a soma, não mais: o grupo")
    print("concentra fogo e cada morto para de causar dano para sempre.")


def tabua_de_referencia() -> None:
    titulo("Tábua de Kleos — dano real esperado contra a DEF do grupo")
    print("A Tábua lista dano BRUTO (supondo que todo ataque acerte).")
    print("Abaixo, o dano que de fato sai contra DEF 13 e DEF 17.\n")
    print(f"{'Kleos':>6} {'PV':>5} {'DEF':>4} {'atk':>4} {'bruto':>7} "
          f"{'vs DEF 13':>10} {'vs DEF 17':>10}")
    print("-" * 72)
    for k, (pv, defesa, atk, dano, n) in TABUA.items():
        fixo = round(dano / n - 5.5)
        real13 = sum(
            Ataque("x", atk, [10], fixo).dano_esperado(13) for _ in range(n)
        )
        real17 = sum(
            Ataque("x", atk, [10], fixo).dano_esperado(17) for _ in range(n)
        )
        print(f"{k:>6} {pv:>5} {defesa:>4} {atk:>+4} {dano:>7} "
              f"{real13:>10.1f} {real17:>10.1f}")


if __name__ == "__main__":
    teste_grupo_kleos_3()
    teste_um_semideus()
    teste_formulas_de_encontro()
    tabua_de_referencia()
    print()

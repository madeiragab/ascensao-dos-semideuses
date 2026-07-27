"""Testa as regras de descanso propostas em regras/interludio.md.

A pergunta: o desgaste acumula? Um grupo que já brigou três vezes chega
visivelmente mais fraco na quarta, ou os descansos apagam a conta?

Regras testadas:
- Descanso Curto entre combates: recupera todo o SP, nenhum MP.
- Tratamentos: 2 por Descanso Longo, custam 2 SP, curam 1d6 + CON.
- Descanso Longo: todo o SP e MP, metade dos PV máximos.

Rodar de dentro da pasta sim/:
    python dia_de_aventura.py
"""

import random
import sys

from combate import Lutador, combate, rola
from fichas import bestiario
from fichas_v1 import furioso_v1, guardiao_v1, oraculo_v1

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

N = 5000
MAX_ENCONTROS = 8


def montar_grupo() -> list[Lutador]:
    grupo = []
    for ficha in (guardiao_v1(), furioso_v1(), oraculo_v1()):
        lut = Lutador.de_ficha(ficha, regras="v1")
        lut.mod_con = ficha.mods["constituicao"]
        lut.tratamentos_max = ficha.prof
        lut.tratamentos = ficha.prof
        grupo.append(lut)
    return grupo


def descanso_curto(grupo: list[Lutador]) -> None:
    """SP cheio; depois cada um decide se gasta Tratamento.

    Quem caiu a 0 PV é estabilizado pelo grupo e acorda com 1 PV — é o que a
    seção 26 permite com uma ação e um teste de Intuição CD 10.
    """
    for p in grupo:
        if p.pv == 0:
            p.pv = 1
        p.sp = p.sp_max
        while p.tratamentos > 0 and p.sp >= 2 and p.pv < p.pv_max * 0.7:
            p.tratamentos -= 1
            p.sp -= 2
            p.pv = min(p.pv_max, p.pv + rola(6) + p.mod_con)


def descanso_longo(grupo: list[Lutador]) -> None:
    for p in grupo:
        p.sp = p.sp_max
        p.mp = p.mp_max
        p.tratamentos = p.tratamentos_max
        base = p.pv if p.vivo else 1
        p.pv = min(p.pv_max, base + (p.pv_max + 1) // 2)


def encontro_fixo() -> list[Lutador]:
    """Encontro moderado e sempre igual: isola desgaste de dificuldade."""
    b = bestiario()
    return [Lutador.de_monstro(b["cao"], f" {i}") for i in (1, 2)]


def fracao(grupo, campo, campo_max) -> float:
    total = sum(getattr(p, campo_max) for p in grupo)
    return sum(getattr(p, campo) for p in grupo) / total if total else 0.0


def curva_de_desgaste(dias: int) -> None:
    """Mede o estado do grupo NO INÍCIO de cada encontro."""
    random.seed(4242)

    chegou = [0] * (MAX_ENCONTROS + 1)
    pv_acum = [0.0] * (MAX_ENCONTROS + 1)
    mp_acum = [0.0] * (MAX_ENCONTROS + 1)
    trat_acum = [0.0] * (MAX_ENCONTROS + 1)

    for _ in range(N):
        grupo = montar_grupo()
        n = 0
        vivo = True
        for _dia in range(dias):
            if not vivo:
                break
            for _ in range(MAX_ENCONTROS // dias):
                n += 1
                if n > MAX_ENCONTROS:
                    break
                chegou[n] += 1
                pv_acum[n] += fracao(grupo, "pv", "pv_max")
                mp_acum[n] += fracao(grupo, "mp", "mp_max")
                trat_acum[n] += sum(p.tratamentos for p in grupo) / sum(
                    p.tratamentos_max for p in grupo
                )

                if combate(grupo, encontro_fixo())["vencedor"] != "herois":
                    vivo = False
                    break
                descanso_curto(grupo)
            descanso_longo(grupo)

    rotulo = "tudo no mesmo dia" if dias == 1 else f"repartido em {dias} dias"
    print(f"--- 8 encontros iguais (2 cães do inferno), {rotulo} ---")
    print(f"{'encontro':>9} | {'grupo chega vivo':>17} | {'PV':>6} {'MP':>6} "
          f"{'Tratamentos':>12}")
    print("-" * 66)
    for i in range(1, MAX_ENCONTROS + 1):
        if chegou[i] == 0:
            break
        print(f"{i:>9} | {chegou[i] / N:>16.1%} | "
              f"{pv_acum[i] / chegou[i]:>5.0%} {mp_acum[i] / chegou[i]:>6.0%} "
              f"{trat_acum[i] / chegou[i]:>11.0%}")
    print()


if __name__ == "__main__":
    print("=" * 66)
    print("CURVA DE DESGASTE — as regras de descanso propostas mordem?")
    print("=" * 66)
    print(f"{N} simulações. Grupo de nível 1, regras da v1.")
    print("Recursos medidos NO INÍCIO de cada encontro, em % do máximo.\n")
    curva_de_desgaste(dias=1)
    curva_de_desgaste(dias=2)
    curva_de_desgaste(dias=4)

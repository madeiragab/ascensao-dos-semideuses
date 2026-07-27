"""Personagens de qualquer nível, seguindo a progressão do Capítulo Nove.

Progressão implementada:
  proficiência   +2 (1-4) · +3 (5-8) · +4 (9-12) · +5 (13-16) · +6 (17-20)
  atributos      +2 pontos nos níveis 4, 8, 12, 16 e 19
  recursos       por nível, com o mesmo total de 12 para as três classes:
                   Guardião  PV +6 + CON · SP +4 · MP +1
                   Furioso   PV +5 + CON · SP +5 · MP +1
                   Oráculo   PV +4 + CON · SP +3 · MP +4
  Ataque Extra   nível 5, para Guardião e Furioso

Equipamento assumido, porque o livro ainda não tem itens mágicos: cada classe
usa o pacote inicial, e o Guardião troca para peitoral e escudo assim que o
dinheiro permitiria — do nível 5 em diante.
"""

from dataclasses import replace

from dados import MOD
from fichas import Ficha
from fichas_v1 import def_com_armadura

# Ganhos por nível: (PV, SP, MP). PV ainda soma o modificador de Constituição.
POR_NIVEL = {
    "guardiao": (6, 4, 1),
    "furioso":  (5, 5, 1),
    "oraculo":  (4, 3, 4),
}

# Onde os pontos de atributo vão. Dois pontos por vez, na ordem da lista,
# sem passar de 20 — é o que um jogador competente faria.
PRIORIDADE = {
    "guardiao": ["forca", "constituicao", "destreza"],
    "furioso":  ["forca", "constituicao", "destreza"],
    "oraculo":  ["inteligencia", "constituicao", "destreza"],
}

NIVEIS_DE_ATRIBUTO = (4, 8, 12, 16, 19)


def proficiencia(nivel: int) -> int:
    return 2 + (nivel - 1) // 4


def ataques_por_turno(classe: str, nivel: int) -> int:
    """Ataque Extra no nível 5. O Oráculo recebe Bênção Ampliada no lugar."""
    if classe == "oraculo":
        return 1
    return 2 if nivel >= 5 else 1


def _subir_atributos(f: Ficha, nivel: int) -> None:
    pontos = 2 * sum(1 for n in NIVEIS_DE_ATRIBUTO if nivel >= n)
    for atributo in PRIORIDADE[f.classe]:
        while pontos > 0 and getattr(f, atributo) < 20:
            setattr(f, atributo, getattr(f, atributo) + 1)
            pontos -= 1
        if pontos == 0:
            break


def _equipar(f: Ficha, nivel: int) -> None:
    if f.classe == "guardiao":
        armadura, escudo = ("peitoral", True) if nivel >= 5 else ("escamas", True)
    else:
        armadura, escudo = "couro_batido", False
    f.bonus_def = def_com_armadura(f.mods["destreza"], armadura, escudo) - (
        10 + f.mods["destreza"]
    )


def personagem(base: Ficha, nivel: int) -> Ficha:
    """Aplica a progressão inteira sobre uma ficha de nível 1."""
    f = replace(base)
    f.prof = proficiencia(nivel)
    _subir_atributos(f, nivel)

    pv, sp, mp = POR_NIVEL[f.classe]
    con = f.mods["constituicao"]
    div = f.mods["inteligencia"] if f.classe == "oraculo" else f.mods["sabedoria"]

    # Recalcula do zero para que os aumentos de atributo entrem retroativos,
    # como o Capítulo Nove manda.
    base_pv = {"guardiao": 14, "furioso": 12, "oraculo": 10}[f.classe]
    base_sp = {"guardiao": 12, "furioso": 14, "oraculo": 8}[f.classe]
    base_mp = {"guardiao": 6,  "furioso": 6,  "oraculo": 14}[f.classe]

    f.pv_max = base_pv + con + (nivel - 1) * (pv + con)
    f.sp_max = base_sp + con + (nivel - 1) * sp
    f.mp_max = base_mp + div + (nivel - 1) * mp

    _equipar(f, nivel)
    return f


def teto_de_custo(nivel: int) -> int:
    """Capítulo Nove: custo máximo = 4 + metade do nível, arredondada para cima."""
    return 4 + (nivel + 1) // 2


def kleos_do_personagem(nivel: int) -> int:
    """Livro II, seção 3."""
    if nivel <= 4:
        return 1
    if nivel <= 9:
        return 2
    if nivel <= 14:
        return 3
    return 4

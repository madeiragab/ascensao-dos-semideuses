"""Prova exata da equivalência entre resistências ativas e defesas passivas.

Modelo antigo:
    alvo: 1d20 + defesa >= 8 + efeito
    o efeito funciona quando o alvo falha.

Modelo novo:
    fonte: 1d20 + efeito >= 14 + defesa
    o efeito funciona quando a fonte acerta.

A base 14 preserva a probabilidade para todos os bônus, inclusive com
Vantagem/Desvantagem invertidas.
"""

from itertools import product


FACES = range(1, 21)


def old_applies(effect_bonus: int, defense_bonus: int, roll: int) -> bool:
    return roll + defense_bonus < 8 + effect_bonus


def new_hits(effect_bonus: int, defense_bonus: int, roll: int, base: int = 14) -> bool:
    return roll + effect_bonus >= base + defense_bonus


def chance_one(predicate) -> float:
    return sum(predicate(r) for r in FACES) / 20


def chance_two(predicate, mode: str) -> float:
    outcomes = 0
    for first, second in product(FACES, repeat=2):
        chosen = max(first, second) if mode == "advantage" else min(first, second)
        outcomes += predicate(chosen)
    return outcomes / 400


def verify_exact_equivalence() -> int:
    cases = 0
    for effect_bonus in range(-10, 26):
        for defense_bonus in range(-10, 26):
            old_normal = chance_one(
                lambda r, e=effect_bonus, d=defense_bonus: old_applies(e, d, r)
            )
            new_normal = chance_one(
                lambda r, e=effect_bonus, d=defense_bonus: new_hits(e, d, r)
            )
            assert old_normal == new_normal

            # Vantagem do defensor antigo equivale a Desvantagem da fonte nova.
            old_def_adv = chance_two(
                lambda r, e=effect_bonus, d=defense_bonus: old_applies(e, d, r),
                "advantage",
            )
            new_src_dis = chance_two(
                lambda r, e=effect_bonus, d=defense_bonus: new_hits(e, d, r),
                "disadvantage",
            )
            assert old_def_adv == new_src_dis

            # Desvantagem do defensor antigo equivale a Vantagem da fonte nova.
            old_def_dis = chance_two(
                lambda r, e=effect_bonus, d=defense_bonus: old_applies(e, d, r),
                "disadvantage",
            )
            new_src_adv = chance_two(
                lambda r, e=effect_bonus, d=defense_bonus: new_hits(e, d, r),
                "advantage",
            )
            assert old_def_dis == new_src_adv
            cases += 3
    return cases


def compare_wrong_base() -> tuple[float, float]:
    old = chance_one(lambda r: old_applies(5, 3, r))
    base_10 = chance_one(lambda r: new_hits(5, 3, r, base=10))
    return old, base_10


if __name__ == "__main__":
    verified = verify_exact_equivalence()
    sample_old = chance_one(lambda r: old_applies(5, 3, r))
    sample_new = chance_one(lambda r: new_hits(5, 3, r))
    old, base_10 = compare_wrong_base()

    print(f"OK: {verified} comparações exatas verificadas.")
    print(f"Exemplo Efeito +5 contra defesa +3: antigo={sample_old:.0%}, novo={sample_new:.0%}.")
    print(f"Base 10 no mesmo exemplo seria {base_10:.0%}, contra {old:.0%} do sistema antigo.")
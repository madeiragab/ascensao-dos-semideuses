"""Regressão da regra de Evolução de Habilidades.

Evoluir só altera Potência e custo. O perfil mecânico da habilidade permanece
idêntico, e o número de habilidades marcadas é metade da Memória para baixo.
"""


def limite_evoluidas(memoria: int) -> int:
    return max(1, min(6, memoria)) // 2


def teto_de_custo(nivel: int) -> int:
    nivel = max(1, min(20, nivel))
    return 4 + (nivel + 1) // 2


def elevar(perfil: dict, potencia: int, teto: int, desconto: int = 0) -> tuple[dict, int]:
    natural = perfil["custo"]
    if potencia <= natural:
        raise ValueError("a Potência elevada precisa superar a natural")
    if potencia > teto:
        raise ValueError("a Potência não pode superar o Teto de Custo")
    # Copiar garante que dano, alcance, duração e demais efeitos não mudem.
    return dict(perfil), max(1, potencia - desconto)


def main() -> None:
    esperado = {1: 0, 2: 1, 3: 1, 4: 2, 5: 2, 6: 3}
    obtido = {memoria: limite_evoluidas(memoria) for memoria in range(1, 7)}
    assert obtido == esperado, (obtido, esperado)

    assert {nivel: teto_de_custo(nivel) for nivel in (1, 5, 10, 15, 20)} == {
        1: 5, 5: 7, 10: 9, 15: 12, 20: 14
    }

    dardo = {
        "nome": "Dardo de Sombras",
        "custo": 2,
        "dano": "1d8 + atributo",
        "alcance": "médio",
        "duracao": "instantânea",
        "area": "alvo único",
    }
    perfil_elevado, custo_pago = elevar(dardo, potencia=6, teto=7)
    assert perfil_elevado == dardo
    assert perfil_elevado is not dardo
    assert custo_pago == 6

    assinatura, custo_assinatura = elevar(dardo, potencia=6, teto=7, desconto=1)
    assert assinatura == dardo
    assert custo_assinatura == 5

    for potencia_invalida in (2, 8):
        try:
            elevar(dardo, potencia=potencia_invalida, teto=7)
        except ValueError:
            pass
        else:
            raise AssertionError("Potência inválida foi aceita")

    print("evolução de habilidades: limites, Teto e perfil preservado")


if __name__ == "__main__":
    main()

"""Testa o motor de criação de habilidades por pontos.

O motor proposto:

    CUSTO = DURAÇÃO + EFEITOS ADICIONAIS + ALCANCE

    DURAÇÃO   instantânea 1 · sustentada 2 · cena 4
              (já inclui o PRIMEIRO ponto de efeito)
    ALCANCE   curto 6 m: 0 · médio 12 m: +1 · longo 18 m: +2
    SUSTENTAR custo final ÷ 2, arredondado para baixo, mínimo 1, por rodada

    Cada ponto de efeito compra:
      dano em alvo único ....... 1d8
      dano em área ............. 1d6
      PV temporários ........... 1d8
      +3 m de movimento ........ 1 ponto
      +1 DEF ................... 1 ponto (o segundo custa 2)
      Vantagem em uma rolagem .. 1 ponto
      condição fraca ........... 1 ponto
      condição média ........... 2 pontos
      condição forte ........... 4 pontos

    O modificador do Atributo Divino entra UMA vez em dano ou PV temporários.

As perguntas que este arquivo responde:
  1. Uma habilidade de 1 MP vale mais que um ataque de arma, que é grátis?
  2. A partir de quantos alvos o dano em área passa o dano em alvo único?
  3. Sustentar uma habilidade sai mais barato que reconjurar?
  4. Quanto dano um conjurador entrega num dia, comparado a um espadachim?

Rodar de dentro da pasta sim/:
    python habilidades.py
"""

import sys

from dados import Ataque, chance_de_acertar, media_dado
from fichas_v1 import furioso_v1, oraculo_v1

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

DEFESAS = [11, 12, 13, 14, 15, 16, 18]


def titulo(t: str) -> None:
    print()
    print("=" * 76)
    print(t)
    print("=" * 76)


# ---------------------------------------------------------------------------
# O motor, em código
# ---------------------------------------------------------------------------

DURACAO = {"instantanea": 1, "sustentada": 2, "cena": 4}
ALCANCE = {"pessoal": 0, "toque": 0, "curto": 0, "medio": 1, "longo": 2}


def custo(pontos_de_efeito: int, duracao: str = "instantanea",
          alcance: str = "curto", modificadores: int = 0) -> int:
    """Custo final em MP ou SP. O primeiro ponto de efeito vem na duração."""
    adicionais = max(0, pontos_de_efeito - 1)
    return max(1, DURACAO[duracao] + adicionais + ALCANCE[alcance] + modificadores)


def sustentar(custo_final: int) -> int:
    return max(1, custo_final // 2)


def dano_alvo_unico(pontos: int, mod: int) -> tuple[list[int], int]:
    """1d8 por ponto, mais o modificador uma única vez."""
    return [8] * pontos, mod


def dano_area(pontos: int, mod: int) -> tuple[list[int], int]:
    """1d6 por ponto, mais o modificador uma única vez."""
    return [6] * pontos, mod


# ---------------------------------------------------------------------------
def teste_um_ponto_vs_arma() -> None:
    titulo("1. Uma habilidade de 1 MP vale mais que uma espada, que é de graça?")
    o = oraculo_v1()
    mod = o.mods["inteligencia"]      # Atributo Divino = INT, +3
    bonus = mod + o.prof              # ataque de habilidade = +5

    print(f"Oráculo nível 1, Atributo Divino Inteligência +{mod}, proficiência +{o.prof}.")
    print(f"Ataque de habilidade: 1d20 + {bonus}.  MP máximo: {o.mp_max}.\n")

    print(f"{'DEF':>4} | {'espada longa':>13} {'1 MP (1d8+3)':>14} "
          f"{'2 MP (2d8+3)':>14} {'3 MP (3d8+3)':>14}")
    print("-" * 76)
    for d in DEFESAS:
        espada = Ataque("e", bonus, [8], mod).dano_esperado(d)
        linha = [f"{espada:>13.2f}"]
        for p in (1, 2, 3):
            dados, fixo = dano_alvo_unico(p, mod)
            # p pontos: custo = 1 + (p-1) = p MP no alcance curto
            linha.append(f"{Ataque('h', bonus, dados, fixo).dano_esperado(d):>14.2f}")
        print(f"{d:>4} | " + " ".join(linha))

    print("\nA de 1 MP empata com a espada — o que ela compra a mais é alcance,")
    print("tipo de dano elemental e a possibilidade de levar efeitos junto.")
    print("A de 2 MP já é claramente melhor. Isso é o desenho pretendido:")
    print("gastar recurso tem que comprar poder, mas não pode aposentar a arma.")


# ---------------------------------------------------------------------------
def teste_area_vs_alvo_unico() -> None:
    titulo("2. A partir de quantos alvos a área vale mais que o alvo único?")
    o = oraculo_v1()
    mod = o.mods["inteligencia"]
    bonus = mod + o.prof
    cd = 8 + mod + o.prof
    ref_alvo = 1          # Reflexos típico de um monstro de Kleos baixo

    print(f"CD da habilidade: {cd}.  Reflexos do alvo: +{ref_alvo}.")
    print("Área: falha sofre o dano inteiro, sucesso sofre metade.\n")

    p_passa = chance_de_acertar(ref_alvo, cd)
    print(f"O alvo passa no Teste de Reflexos {p_passa:.0%} das vezes.\n")

    print(f"{'custo':>6} | {'alvo único':>11} | {'área: 1 alvo':>12} {'2 alvos':>9} "
          f"{'3 alvos':>9} {'4 alvos':>9}")
    print("-" * 76)
    for p in (1, 2, 3, 4):
        dados_u, fixo_u = dano_alvo_unico(p, mod)
        unico = Ataque("u", bonus, dados_u, fixo_u).dano_esperado(14)

        dados_a, fixo_a = dano_area(p, mod)
        cheio = sum(media_dado(x) for x in dados_a) + fixo_a
        por_alvo = p_passa * (cheio / 2) + (1 - p_passa) * cheio

        linha = " ".join(f"{por_alvo * n:>9.2f}" for n in (1, 2, 3, 4))
        print(f"{p:>4} MP | {unico:>11.2f} | " + linha)

    print("\nContra um alvo só, o alvo único ganha. A área passa a partir de dois,")
    print("e a vantagem cresce rápido dali. É a relação certa: área é a resposta")
    print("para grupo, não uma versão melhor do ataque comum.")


# ---------------------------------------------------------------------------
def teste_sustentar() -> None:
    titulo("3. Sustentar sai mais barato que reconjurar?")
    print("Sustentada custa 2 (+ efeitos) e manter custa metade do final,")
    print("arredondado para baixo, por rodada.\n")

    print(f"{'pontos':>7} {'custo':>6} {'sustentar':>10} | "
          f"{'3 rodadas sustentando':>22} {'3x reconjurando':>16}")
    print("-" * 76)
    for p in (1, 2, 3, 4, 5):
        c = custo(p, "sustentada")
        s = sustentar(c)
        sustentando = c + s * 2          # ativa na rodada 1, mantém nas 2 e 3
        inst = custo(p, "instantanea")
        reconjurando = inst * 3
        print(f"{p:>7} {c:>6} {s:>10} | {sustentando:>22} {reconjurando:>16}")

    print("\nSustentar é mais barato que reconjurar em quase toda a faixa — e deve")
    print("ser, porque exige Concentração e o personagem só mantém uma por vez.")
    print("Reconjurar é a saída de quem não quer ficar preso a uma Concentração.")


# ---------------------------------------------------------------------------
def teste_orcamento_do_dia() -> None:
    titulo("4. Quanto um conjurador entrega num dia, contra um espadachim?")
    o, f = oraculo_v1(), furioso_v1()
    mod = o.mods["inteligencia"]
    bonus = mod + o.prof

    # Furioso: ataque grátis, com Vantagem do Ataque Feroz, todas as rodadas.
    dpr_furioso = Ataque("f", f.bonus_ataque, [10], f.dano_fixo,
                         brutal=True, vantagem=True).dano_esperado(14)

    print(f"Furioso: machado grande com Ataque Feroz, {dpr_furioso:.2f} de dano")
    print(f"por rodada, para sempre — não gasta recurso.\n")
    print(f"Oráculo: {o.mp_max} MP no total. Um dia de aventura são umas 12 rodadas")
    print("de combate (quatro encontros de três rodadas).\n")

    print(f"{'habilidade':<22} {'custo':>6} {'dano':>7} {'usos/dia':>9} "
          f"{'dano no dia':>12} {'rodadas cobertas':>17}")
    print("-" * 76)
    for p in (1, 2, 3):
        dados, fixo = dano_alvo_unico(p, mod)
        dano = Ataque("h", bonus, dados, fixo).dano_esperado(14)
        c = custo(p, "instantanea")
        usos = o.mp_max // c
        print(f"{'alvo único, ' + str(p) + ' ponto(s)':<22} {c:>6} {dano:>7.2f} "
              f"{usos:>9} {usos * dano:>12.1f} {min(usos, 12):>17}")

    print(f"\n{'Furioso, 12 rodadas':<22} {'—':>6} {dpr_furioso:>7.2f} "
          f"{'∞':>9} {dpr_furioso * 12:>12.1f} {12:>17}")

    print("\nO Furioso ganha em dano acumulado, e deve ganhar: é a classe de dano,")
    print("e ela não gasta nada. Mesmo o Oráculo queimando os 17 MP em ataques de")
    print("1 ponto chega a 80 contra os 97 dele — e chega sem MP para curar,")
    print("proteger ou controlar.")
    print("O que o conjurador compra com MP não é dano bruto: é alcance, área,")
    print("condição e escolha. Se o motor fizesse dele o melhor causador de dano,")
    print("a classe de dano perderia a razão de existir.")


# ---------------------------------------------------------------------------
def teste_exemplos_montados() -> None:
    titulo("5. Habilidades montadas com o motor, para conferir a conta")
    o = oraculo_v1()
    mod = o.mods["inteligencia"]

    exemplos = [
        ("Dardo de Sombras",      1, "instantanea", "medio",  0, "1d8 + 3 de dano"),
        ("Lança de Gelo",         3, "instantanea", "longo",  0, "3d8 + 3 de dano"),
        ("Explosão de Brasa",     2, "instantanea", "medio",  0, "2d6 + 3 em área"),
        ("Raízes Agarradoras",    2, "sustentada",  "medio",  0, "condição média: Preso"),
        ("Couraça de Pedra",      2, "cena",        "pessoal", 0, "2d8 + 3 PV temporários"),
        ("Passo do Vento",        1, "instantanea", "pessoal", 0, "+3 m de movimento"),
        ("Escudo de Água",        3, "sustentada",  "pessoal", 0, "+2 DEF"),
        ("Golpe Trovejante",      3, "instantanea", "curto",  0, "2d8 + 3 e condição fraca"),
    ]

    print(f"{'habilidade':<22} {'efeito':<28} {'dur.':<12} {'alc.':<8} "
          f"{'custo':>6} {'sust.':>6}")
    print("-" * 76)
    for nome, pontos, dur, alc, m, efeito in exemplos:
        c = custo(pontos, dur, alc, m)
        s = sustentar(c) if dur == "sustentada" else 0
        print(f"{nome:<22} {efeito:<28} {dur:<12} {alc:<8} {c:>6} "
              f"{(str(s) if s else '—'):>6}")

    print("\nNenhuma passa de 5 MP, e o Oráculo de nível 1 tem 17. Um Furioso, com")
    print(f"{furioso_v1().mp_max} MP, consegue duas ou três habilidades pequenas por dia — o")
    print("suficiente para ter um truque, não para virar conjurador.")


# ---------------------------------------------------------------------------
def teste_passivas() -> None:
    titulo("6. O custo de uma passiva morde de verdade?")
    print("Proposta: cada passiva custa 1 ponto permanente de Inteligência ou de")
    print("Constituição, E 1 ponto do recurso que aquele atributo alimenta")
    print("(MP para Inteligência, SP para Constituição).\n")

    o = oraculo_v1()
    print(f"Oráculo: INT {o.inteligencia} (+{o.mods['inteligencia']}), "
          f"CON {o.constituicao} (+{o.mods['constituicao']}), "
          f"MP {o.mp_max}, SP {o.sp_max}, "
          f"Memória {2 + o.mods['inteligencia']}\n")

    print(f"{'passivas':>9} | {'INT':>5} {'mod':>5} {'MP':>5} {'Memória':>8} | "
          f"{'CON':>5} {'mod':>5} {'SP':>5} {'PV':>5}")
    print("-" * 76)
    for n in range(0, 4):
        # pagando tudo em Inteligência
        int_v = o.inteligencia - n
        mod_i = (int_v - 10) // 2
        mp = 14 + mod_i - n
        mem = max(1, 2 + mod_i)
        # pagando tudo em Constituição
        con_v = o.constituicao - n
        mod_c = (con_v - 10) // 2
        sp = 8 + mod_c - n
        pv = 10 + mod_c
        print(f"{n:>9} | {int_v:>5} {mod_i:>+5} {mp:>5} {mem:>8} | "
              f"{con_v:>5} {mod_c:>+5} {sp:>5} {pv:>5}")

    print("\nO ponto no recurso é o que garante que o custo nunca seja zero: sem ele,")
    print("um valor ímpar de atributo cairia para par sem mexer no modificador, e a")
    print("passiva sairia de graça. Três passivas custam ao Oráculo 3 de MP e um")
    print("espaço de Memória — o bastante para doer, longe de ser proibitivo.")


if __name__ == "__main__":
    teste_um_ponto_vs_arma()
    teste_area_vs_alvo_unico()
    teste_sustentar()
    teste_orcamento_do_dia()
    teste_exemplos_montados()
    teste_passivas()
    print()

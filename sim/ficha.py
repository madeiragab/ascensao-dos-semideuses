"""A Ficha do Herói contra o simulador — duas implementações da mesma regra.

A ficha calcula PV, SP, MP, proficiência, Grau e Teto de Custo em JavaScript.
O `niveis.py` calcula tudo isso outra vez, em Python, e é sobre o Python que
todo o balanceamento do projeto foi medido. **São duas implementações da mesma
regra, e até aqui ninguém tinha comparado as duas.**

Se elas divergirem, o jogador na mesa fica com o número errado e nenhum dos
outros testes acusa: eles medem o Python contra si mesmo.

Este arquivo lê `template/ficha.html`, extrai as constantes e as fórmulas de lá,
e compara com o Python nos vinte níveis, para as três classes. Compara também os
textos de ajuda que a ficha mostra ao lado de cada número, porque uma explicação
velha ao lado de um valor certo confunde tanto quanto um valor errado.

Rodar de dentro da pasta sim/:
    python ficha.py
"""

import pathlib
import re
import sys

from dados import MOD
from fichas import furioso_ares, guardiao_ares, oraculo_atena
from niveis import grau, personagem, proficiencia, teto_de_custo

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

FICHA = pathlib.Path(__file__).resolve().parent.parent / "template" / "ficha.html"
BASE = {"guardiao": guardiao_ares, "furioso": furioso_ares, "oraculo": oraculo_atena}


def ler_classes(html: str) -> dict:
    """Extrai a tabela CLASSES da ficha: base e ganho por nível de cada recurso."""
    achado = {}
    padrao = re.compile(
        r"(guardiao|furioso|oraculo):\s*\{\s*pv:\s*(\d+),\s*sp:\s*(\d+),\s*mp:\s*(\d+),"
        r"\s*pvN:\s*(\d+),\s*spN:\s*(\d+),\s*mpN:\s*(\d+)")
    for m in padrao.finditer(html):
        classe, *n = m.groups()
        achado[classe] = dict(zip(("pv", "sp", "mp", "pvN", "spN", "mpN"),
                                  (int(x) for x in n)))
    return achado


def ler_formula(html: str, chave: str) -> str:
    """Devolve o texto de ajuda que a ficha mostra ao lado de um campo."""
    m = re.search(r'escreve\("' + chave + r'",[^,]*,\s*\n?\s*"([^"]+)"', html)
    return m.group(1) if m else ""


def main() -> None:
    html = FICHA.read_text(encoding="utf-8")
    falhas = []

    print("A ficha e o simulador calculam a mesma coisa?")
    print()

    # ---- as constantes de classe
    classes = ler_classes(html)
    print("Constantes de classe, lidas da ficha:")
    print(f"{'classe':>10}{'PV base':>9}{'+PV/nível':>11}{'SP base':>9}"
          f"{'+SP/nível':>11}{'MP base':>9}{'+MP/nível':>11}")
    print("-" * 70)
    esperado = {"guardiao": (14, 6, 12, 4, 6, 1),
                "furioso": (12, 5, 14, 5, 6, 1),
                "oraculo": (10, 4, 8, 3, 14, 4)}
    for classe, c in classes.items():
        print(f"{classe:>10}{c['pv']:>9}{c['pvN']:>11}{c['sp']:>9}"
              f"{c['spN']:>11}{c['mp']:>9}{c['mpN']:>11}")
        alvo = esperado[classe]
        atual = (c["pv"], c["pvN"], c["sp"], c["spN"], c["mp"], c["mpN"])
        if atual != alvo:
            falhas.append(f"{classe}: a ficha traz {atual}, o Capítulo Nove diz {alvo}")
    if len(classes) != 3:
        falhas.append(f"a ficha só declarou {len(classes)} classes")

    # ---- os vinte níveis, recurso por recurso
    print("\nOs vinte níveis, comparando ficha contra sim/niveis.py:")
    print(f"{'nível':>6}{'classe':>10}{'PV':>12}{'SP':>12}{'MP':>12}"
          f"{'prof':>7}{'Grau':>6}{'Teto':>6}")
    print("-" * 72)
    for nivel in range(1, 21):
        for classe, c in classes.items():
            f = personagem(BASE[classe](), nivel)
            con = f.mods["constituicao"]
            div = f.mods["inteligencia" if classe == "oraculo" else "sabedoria"]

            # As três fórmulas, como a ficha as escreve nas linhas 1114 a 1123.
            pv_ficha = c["pv"] + con + (nivel - 1) * (c["pvN"] + con)
            sp_ficha = c["sp"] + con + (nivel - 1) * c["spN"]
            mp_ficha = c["mp"] + div + (nivel - 1) * c["mpN"]
            prof_ficha = 2 + (nivel - 1) // 4
            grau_ficha = min(5, (nivel - 1) // 4 + 1)
            teto_ficha = 5 if grau_ficha == 1 else 6

            pares = [("PV", pv_ficha, f.pv_max), ("SP", sp_ficha, f.sp_max),
                     ("MP", mp_ficha, f.mp_max),
                     ("proficiência", prof_ficha, proficiencia(nivel)),
                     ("Grau", grau_ficha, grau(nivel)),
                     ("Teto", teto_ficha, teto_de_custo(nivel))]
            for nome, na_ficha, no_sim in pares:
                if na_ficha != no_sim:
                    falhas.append(f"nível {nivel}, {classe}, {nome}: "
                                  f"ficha {na_ficha} × simulador {no_sim}")

            if nivel in (1, 5, 10, 20) and classe == "guardiao":
                print(f"{nivel:>6}{classe:>10}"
                      f"{f'{pv_ficha} = {f.pv_max}':>12}"
                      f"{f'{sp_ficha} = {f.sp_max}':>12}"
                      f"{f'{mp_ficha} = {f.mp_max}':>12}"
                      f"{prof_ficha:>7}{grau_ficha:>6}{teto_ficha:>6}")

    # ---- os textos de ajuda que a ficha mostra ao lado dos números
    print("\nTextos de ajuda da ficha:")
    textos = {
        "prof": "2 + (nível − 1) ÷ 4, para baixo",
        "teto": "5 pontos no Grau 1, 6 do Grau 2 em diante",
    }
    for chave, esperado_txt in textos.items():
        atual = ler_formula(html, chave)
        estado = "ok" if atual == esperado_txt else "DESATUALIZADO"
        print(f"  {chave:>6}: {atual!r} — {estado}")
        if atual != esperado_txt:
            falhas.append(f"o texto do campo '{chave}' diz {atual!r}, "
                          f"mas a regra é {esperado_txt!r}")

    # ---- Exausto: a ficha tem botões e soma sozinha, e a conta é do livro
    print()
    print("Exausto — livro × ficha:")
    livro = (FICHA.parent / "livro-do-jogador.html").read_text(encoding="utf-8")
    tabela = re.search(r"Três níveis, e cada um soma ao anterior.*?</table>", livro, re.S)
    niveis_livro = re.findall(r'<td class="num">(\d)</td><td>(.*?)</td>',
                              tabela.group(0) if tabela else "")
    print(f"  níveis na tabela do livro: {len(niveis_livro)}")
    if len(niveis_livro) != 3:
        falhas.append(f"a tabela de Exausto do livro tem {len(niveis_livro)} níveis; a ficha assume 3")

    caixas = len(re.findall(r'data-exausto="\d"', html))
    print(f"  caixas na ficha: {caixas}")
    if caixas != len(niveis_livro):
        falhas.append(f"a ficha tem {caixas} caixas de Exausto para {len(niveis_livro)} níveis no livro")

    # em que nível cada corte entra: o livro diz movimento no 2 e PV no 3
    por_nivel = {int(n): texto.lower() for n, texto in niveis_livro}
    corte_mov = next((n for n, t in sorted(por_nivel.items()) if "movimenta" in t and "metade" in t), None)
    corte_pv = next((n for n, t in sorted(por_nivel.items()) if "pv máximos" in t and "metade" in t), None)
    na_ficha_mov = int(re.search(r"if \(exausto >= (\d)\) passos = passos / 2", html).group(1))
    na_ficha_pv = int(re.search(r"if \(exausto >= (\d)\) pvMaximo = Math.floor", html).group(1))
    print(f"  movimento pela metade: livro nível {corte_mov}, ficha nível {na_ficha_mov}")
    print(f"  PV pela metade:        livro nível {corte_pv}, ficha nível {na_ficha_pv}")
    if corte_mov != na_ficha_mov:
        falhas.append(f"a ficha corta o movimento no Exausto {na_ficha_mov}; o livro diz {corte_mov}")
    if corte_pv != na_ficha_pv:
        falhas.append(f"a ficha corta os PV no Exausto {na_ficha_pv}; o livro diz {corte_pv}")

    print()
    if falhas:
        for f in falhas:
            print("FALHOU:", f)
        raise SystemExit(1)
    print("A ficha e o simulador concordam nos vinte níveis, nas três classes,")
    print("em PV, SP, MP, proficiência, Grau e Teto de Custo — e os cortes de")
    print("Exausto entram nos mesmos níveis que o livro manda.")


if __name__ == "__main__":
    main()

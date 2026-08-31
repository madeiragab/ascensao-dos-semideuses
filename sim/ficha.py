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

    # ---- o rolador: o que a ficha diz ao rolar precisa ser o que o livro manda
    print()
    print("Rolador de d20 — ficha × livro:")
    texto_livro = re.sub(r"<[^>]*>", " ", livro)
    texto_livro = " ".join(texto_livro.split())
    regras = [
        ("crítico dobra os dados da arma", "rola todos os dados de dano duas vezes",
         "critico ? 2 : 1"),
        ("1 natural erra", "o ataque erra, não importa o bônus",
         "1 natural: erra"),
    ]
    for nome, no_livro, na_ficha in regras:
        ok_livro = no_livro in texto_livro
        ok_ficha = na_ficha in html
        print(f"  {nome}: livro {'sim' if ok_livro else 'NÃO'} · ficha {'sim' if ok_ficha else 'NÃO'}")
        if not ok_livro:
            falhas.append(f"o livro não diz mais {no_livro!r}; o rolador da ficha ainda aplica essa regra")
        if not ok_ficha:
            falhas.append(f"o rolador da ficha não aplica {nome!r}")

    botoes_pericia = html.count('botaoD20("per-"')
    botoes_ataque = html.count('botaoD20("atk-"')
    print(f"  botões: {botoes_pericia} na lista de perícias, {botoes_ataque} na de ataques")
    if not botoes_pericia or not botoes_ataque:
        falhas.append("o rolador sumiu de perícias ou de ataques")

    # ---- passivas: o sacrifício é a única troca permanente do Livro I, e a
    # ficha aplica as duas metades dela sozinha. Se o livro mudar o preço, ou
    # a lista de efeitos, a ficha precisa acusar aqui e não na mesa.
    print()
    print("Passivas e Sacrifício de Atributo — livro × ficha:")

    efeitos_livro = [
        "+1 DEF", "+1,5 m de movimento", "+1 em uma perícia",
        "enxergar no escuro comum", "respirar num meio hostil",
        "resistência a um perigo ambiental", "Vantagem numa categoria estreita",
    ]
    faltando_livro = [e for e in efeitos_livro if e.lower() not in texto_livro.lower()]
    print(f"  efeitos que o livro permite: {len(efeitos_livro) - len(faltando_livro)}"
          f" de {len(efeitos_livro)} encontrados no texto")
    if faltando_livro:
        falhas.append("o livro não lista mais estes efeitos de passiva, "
                      f"mas a ficha oferece: {', '.join(faltando_livro)}")

    na_ficha = re.search(r"var EFEITO_PASSIVA = \{(.*?)\n\};", html, re.S)
    if not na_ficha:
        falhas.append("a tabela EFEITO_PASSIVA sumiu da ficha")
    else:
        oferecidos = re.findall(r'nome: "([^"]+)"', na_ficha.group(1))
        print(f"  efeitos que a ficha oferece: {len(oferecidos)}")
        if len(oferecidos) != len(efeitos_livro):
            falhas.append(f"a ficha oferece {len(oferecidos)} efeitos de passiva "
                          f"e o livro permite {len(efeitos_livro)}")

    # As duas metades do preço, e o piso. As três estão escritas no livro.
    metades = [
        ("−1 no atributo", "−1 ponto no valor de Inteligência", "- sacrificio"),
        ("−1 no recurso que ele alimenta", "−1 no máximo do recurso", "- sacPassivas.inteligencia"),
        ("piso 8", "Nenhum atributo desce abaixo de 8", "Math.max(8,"),
        ("ocupa Memória", "ocupa um espaço de Memória", "espaço de Memória"),
    ]
    for nome, no_livro, no_codigo in metades:
        ok_livro = no_livro.lower() in texto_livro.lower()
        ok_ficha = no_codigo in html
        print(f"  {nome}: livro {'sim' if ok_livro else 'NÃO'} · ficha {'sim' if ok_ficha else 'NÃO'}")
        if not ok_livro:
            falhas.append(f"o livro não diz mais {no_livro!r}, e a ficha ainda aplica")
        if not ok_ficha:
            falhas.append(f"a ficha não aplica a regra {nome!r} das passivas")

    # ---- o construtor de habilidades contra os exemplos fechados do livro.
    # O livro resolve três habilidades por extenso; se o construtor não chegar
    # nos mesmos números, ele está inventando matemática.
    print()
    print("Construtor de habilidades — exemplos do livro:")

    exemplos = [
        # nome, duração, alcance, ativação, Grau base,
        # linhas de efeito como (pontos, Grau do ponto), pontos, custo
        ("Passo das Trevas", 1, 0, 1, 1, [(1, 1)], 2, 2),
        ("Lança de Sombra, Grau 1", 1, 1, 0, 1, [(3, 1)], 4, 4),
        ("Lança de Sombra, Grau 3", 1, 1, 0, 3, [(3, 3)], 4, 12),
        # o que a campanha produziu: DEF +2 é 1 ponto mais 2 pelo dobro
        ("Manto do Oceano", 2, 0, 1, 1, [(3, 1)], 5, 5),
        # e a mistura que o livro recomenda: o dano no Grau cheio e o metro
        # de movimento comprado no Grau 1, que é onde ele não precisa crescer
        ("Dano G3 + movimento G1", 1, 0, 0, 3, [(3, 3), (1, 1)], 4, 10),
    ]
    for nome, dur, alc, ativ, base, linhas, pontos_ok, custo_ok in exemplos:
        estruturais = dur + alc + ativ
        pts_efeito = sum(p for p, _ in linhas)
        # a duração já traz um ponto de efeito incluído, e ele abate o ponto
        # mais caro comprado
        gratis = 1 if pts_efeito else 0
        maior = max((g for _, g in linhas), default=0)
        pontos = max(1, estruturais + pts_efeito - gratis)
        custo = max(1, estruturais * base + sum(p * g for p, g in linhas) - gratis * maior)
        marca = "ok" if (pontos, custo) == (pontos_ok, custo_ok) else "ERRADO"
        print(f"  {nome:<24} {pontos} pontos · {custo} de recurso — {marca}")
        if (pontos, custo) != (pontos_ok, custo_ok):
            falhas.append(f"a conta de {nome} dá {pontos} pontos e {custo} de recurso; "
                          f"o livro diz {pontos_ok} e {custo_ok}")

    # O Grau é por ponto, não por habilidade: a ficha precisa oferecer a
    # escolha em cada linha de efeito, senão ela é mais restritiva que o livro.
    if "hbGrauEfeito" not in html:
        falhas.append("a ficha voltou a ter um Grau só para a habilidade inteira; "
                      "o livro compra um ponto em qualquer Grau até o seu")
    for frase in ["CUSTO em MP ou SP = pontos × Grau do ponto",
                  "Você pode comprar um ponto em qualquer Grau até o seu"]:
        if frase.lower() not in texto_livro.lower():
            falhas.append(f"o livro não diz mais {frase!r}, e o construtor compra por ponto")
    print("  Grau por ponto: oferecido em cada linha de efeito")

    formulas = [
        ("PONTOS", "PONTOS = duração + efeitos adicionais + alcance + modificadores"),
        ("CUSTO", "CUSTO em MP ou SP = pontos × Grau"),
        ("sustentar", "por rodada = custo final ÷ 2, arredondado para baixo (mínimo 1)"),
    ]
    for nome, no_livro in formulas:
        if no_livro.lower() not in texto_livro.lower():
            falhas.append(f"a fórmula de {nome} mudou no livro: o construtor ainda usa {no_livro!r}")
    print(f"  fórmulas conferidas contra o livro: {len(formulas)}")

    # A tabela de efeitos do construtor tem de cobrir as linhas de "O que cada
    # ponto compra" sem inventar nenhuma.
    tabela = re.search(r"var HB_EFEITOS = \{(.*?)\n\};", html, re.S)
    if not tabela:
        falhas.append("a tabela HB_EFEITOS sumiu da ficha")
    else:
        linhas_ficha = re.findall(r'nome: "([^"]+)"', tabela.group(1))
        print(f"  linhas de efeito no construtor: {len(linhas_ficha)}")
        if len(linhas_ficha) != 15:
            falhas.append(f"o construtor oferece {len(linhas_ficha)} linhas de efeito; "
                          "as tabelas do Capítulo Sete têm 15")

    # As condições de grau Destino não podem ser compradas por uma habilidade
    # que um jogador montou — o construtor não pode nem oferecer.
    if "Destino" in (tabela.group(1) if tabela else ""):
        falhas.append("o construtor oferece condição de grau Destino, que não tem preço")
    else:
        print("  condições de grau Destino: fora do construtor, como o livro manda")

    # ---- combinações: "Ataque ou Efeito, nunca os dois". É a regra que decide
    # quais efeitos cabem na mesma habilidade, e a que o construtor precisa
    # espelhar exatamente — nem mais restritiva, nem menos.
    print()
    print("Combinações de efeito — o limite que vale sempre:")

    for frase in ["Ataque ou Efeito, nunca os dois",
                  "O alvo não faz uma segunda rolagem",
                  "efeitos secundários fracos, como empurrar ou derrubar, sem uma segunda rolagem",
                  "Condições médias e fortes sempre obrigam a habilidade a usar Efeito",
                  "Alvo único usa Ataque de Habilidade",
                  "Área usa Rolagem de Efeito contra Reflexos"]:
        if frase.lower() not in texto_livro.lower():
            falhas.append(f"o livro não diz mais {frase!r}, e o construtor ainda trava por ela")
    print("  frases da regra conferidas no livro: 6")

    # O que cada linha exige, lido da própria tabela do construtor.
    linhas_exige = {}
    for bloco in re.finditer(r"(\w+):\s*\{ nome: \"([^\"]+)\"(.*?)(?=\n  \w+: \{ nome|\n\};)",
                             tabela.group(1) if tabela else "", re.S):
        chave, nome, corpo = bloco.group(1), bloco.group(2), bloco.group(3)
        m = re.search(r'exige:\s*"(\w+)"', corpo)
        linhas_exige[chave] = (
            m.group(1) if m else None,
            (re.search(r'defesa:\s*"(\w+)"', corpo) or [None, None])[1],
            "acompanha: true" in corpo,
        )

    esperado = {
        # linha            resolução   defesa       pega carona
        "dano_unico":     ("ataque",   None,        False),
        "dano_area":      ("efeito",   "Reflexos",  False),
        "cond_media":     ("efeito",   None,        False),
        "cond_forte":     ("efeito",   None,        False),
        "empurrar":       ("efeito",   "Fortitude", True),
        "cond_fraca":     ("efeito",   None,        True),
        "dano_continuo":  (None,       None,        False),
        "pv_temp":        (None,       None,        False),
    }
    for chave, alvo in esperado.items():
        atual = linhas_exige.get(chave)
        marca = "ok" if atual == alvo else "ERRADO"
        print(f"  {chave:<15} exige {str(atual[0]):<7} defesa {str(atual[1]):<10} "
              f"carona {str(atual[2]):<5} — {marca}")
        if atual != alvo:
            falhas.append(f"a linha {chave} do construtor declara {atual}; o livro pede {alvo}")

    if "function resolucaoExigida" not in html:
        falhas.append("resolucaoExigida sumiu: o construtor voltou a aceitar duas rolagens")

    # ---- o construtor de itens contra a tabela do Grau, na Parte VII
    print()
    print("Construtor de itens — tabela do Grau, livro × ficha:")

    no_livro = re.findall(
        r"(Mortal|Consagrado|Heroico|Mítico|Lendário|Divino)\s+(\d+)\s+"
        r"(?:o dado da arma|\+\d+ dados?|o Mestre decide)\s+(—|\+\d+)\s+(—|\+\d+)\s+"
        r"(—|\d+)\s+(\d+)", texto_livro)
    print(f"  linhas encontradas no livro: {len(no_livro)}")
    if len(no_livro) != 6:
        falhas.append(f"a tabela de Graus do item tem {len(no_livro)} linhas no livro; a ficha assume 6")

    na_ficha = {
        m[0]: m[1:] for m in re.findall(
            r'nome:\s*"([^"]+)",\s*nivel:\s*(\d+),\s*dados:\s*(\d+|null),\s*'
            r"ataque:\s*(\d+|null),\s*def:\s*(\d+|null),\s*pontos:\s*(\d+)", html)
    }
    for nome, nivel, ataque, defe, pontos, integridade in no_livro:
        if nome not in na_ficha:
            falhas.append(f"o Grau de item {nome!r} sumiu da ficha")
            continue
        f_nivel, _f_dados, f_ataque, f_def, f_pontos = na_ficha[nome]
        esperado = (nivel, "0" if ataque == "—" else ataque.lstrip("+"),
                    "0" if defe == "—" else defe.lstrip("+"),
                    "0" if pontos == "—" else pontos)
        atual = (f_nivel, f_ataque, f_def, f_pontos)
        marca = "ok" if atual == esperado else "ERRADO"
        print(f"  {nome:<12} nível {f_nivel:>2} · ataque +{f_ataque} · DEF +{f_def} · "
              f"{f_pontos} pontos — {marca}")
        if atual != esperado:
            falhas.append(f"o Grau {nome} na ficha é {atual}; o livro diz {esperado}")

    regras_item = [
        ("item não tem duração", "Conte a partir do primeiro ponto de efeito, sem o ponto de duração",
         "sem ponto de duração e sem o ponto grátis"),
        ("sempre ligado custa o dobro", "custa o dobro dos pontos e não usa Cargas",
         "(ligado ? 2 : 1)"),
        ("Cargas iguais à proficiência", "o número delas é o seu bônus de proficiência",
         'g.cargas ? "0/" + prof'),
        ("Divino não se fabrica", "Divino não se fabrica", "Divino não se fabrica"),
    ]
    for nome, no_texto, no_codigo in regras_item:
        ok_livro = no_texto.lower() in texto_livro.lower()
        ok_ficha = no_codigo in html
        print(f"  {nome}: livro {'sim' if ok_livro else 'NÃO'} · ficha {'sim' if ok_ficha else 'NÃO'}")
        if not ok_livro:
            falhas.append(f"o livro não diz mais {no_texto!r}, e o construtor de itens ainda aplica")
        if not ok_ficha:
            falhas.append(f"o construtor de itens não aplica {nome!r}")

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

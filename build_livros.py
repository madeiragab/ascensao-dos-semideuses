"""Monta os livros em HTML a partir dos markdown e dos templates.

Chamado por build.ps1, que antes disso prepara as capas em .build/*.b64.

    template/livro.css              folha de estilo única dos cinco livros
    template/livro-do-jogador.html  o Livro do Jogador, escrito à mão
    template/bestiario.html         casca do Bestiário
    template/grimorio.html          casca do Grimório
    bestiario/*.md                  conteúdo do Bestiário
    regras/magia-da-nevoa.md        conteúdo do Grimório
    vendor/*.min.js                 geração direta do PDF A4 da ficha

O conversor de markdown não usa bibliotecas externas e cobre apenas o
subconjunto que os nossos arquivos realmente usam — e é proposital: um parser
completo seria mais código para manter sem nenhum ganho aqui.
"""

from __future__ import annotations

import html
import pathlib
import re
import sys
import unicodedata

RAIZ = pathlib.Path(__file__).parent
TEMPLATE = RAIZ / "template"
BUILD = RAIZ / ".build"


# ===========================================================================
# Markdown → HTML
# ===========================================================================

# Rótulos que abrem um bloco dentro da ficha de criatura. A regra é: negrito
# sozinho na linha, escrito em maiúsculas.
RE_ROTULO_BLOCO = re.compile(r"^\*\*([A-ZÀ-ÜÇ0-9][A-ZÀ-ÜÇ0-9 ()—\-/]*)\*\*\s*(.*)$")

# Linhas de estatística da criatura.
STATS = ("PV", "Ataque", "Efeito", "Fortitude", "Resistência", "Resistências",
         "Imune", "Imunidades", "Presença", "Vulnerabilidade", "Cada ave")
RE_STATUS = re.compile(r"^\*\*(" + "|".join(STATS) + r")\*\*")

# Cabeçalho de criatura: "### NOME — Kleos 4 (Façanha)"
RE_CRIATURA = re.compile(r"^###\s+(.+?)\s+—\s+Kleos\s+(\d+)\s*\(([^)]+)\)\s*$")

# Divisor de degrau: "# KLEOS 4 — FAÇANHA"
RE_DEGRAU = re.compile(r"^#\s+KLEOS\s+(\d+)\s+—\s+(.+)$")


def slug(t: str) -> str:
    """Identificador curto, legível e estável para âncoras do livro."""
    t = re.sub(r"[*_`]", "", t)
    t = unicodedata.normalize("NFKD", t).encode("ascii", "ignore").decode("ascii")
    return re.sub(r"[^a-z0-9]+", "-", t.lower()).strip("-")


def id_titulo(t: str) -> str:
    """Seções numeradas viram #secao-37 e #secao-37-1."""
    m = re.match(r"(\d+(?:\.\d+)*)(?:\.\s*|\s+)", re.sub(r"[*_`]", "", t))
    if m:
        return "secao-" + m.group(1).replace(".", "-")
    if slug(t) == "indice-rapido":
        return "indice-rapido"
    return ""


def inline(t: str) -> str:
    """Negrito, itálico, código e links. Escapa HTML primeiro."""
    t = html.escape(t, quote=False)
    t = re.sub(r"`([^`]+)`", r'<span class="dado">\1</span>', t)
    t = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)
    t = re.sub(r"(?<![\*\w])\*([^*\n]+?)\*(?!\*)", r"<em>\1</em>", t)
    t = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', t)
    return t


def tabela(linhas: list[str]) -> str:
    """Converte um bloco de linhas |a|b| em <table>, respeitando alinhamento."""
    def celulas(l: str) -> list[str]:
        return [c.strip() for c in l.strip().strip("|").split("|")]

    cab = celulas(linhas[0])
    alinha = celulas(linhas[1])
    classes = ["num" if a.endswith(":") and not a.startswith(":") else ""
               for a in alinha]

    def td(tag: str, cs: list[str]) -> str:
        out = []
        for i, c in enumerate(cs):
            cl = classes[i] if i < len(classes) else ""
            attr = f' class="{cl}"' if cl else ""
            out.append(f"<{tag}{attr}>{inline(c)}</{tag}>")
        return "<tr>" + "".join(out) + "</tr>"

    corpo = "\n".join(td("td", celulas(l)) for l in linhas[2:] if l.strip())
    return ('<div class="rolagem"><table>\n<thead>' + td("th", cab)
            + "</thead>\n<tbody>\n" + corpo + "\n</tbody>\n</table></div>")


def converter(md: str) -> str:
    """Markdown → HTML, com tratamento especial das fichas de criatura."""
    linhas = md.split("\n")
    saida: list[str] = []
    i = 0
    # pilha de fechamento pendente da ficha de criatura
    criatura_aberta = False

    def fecha_criatura():
        nonlocal criatura_aberta
        if criatura_aberta:
            saida.append("</article>")
            criatura_aberta = False

    while i < len(linhas):
        # Trava de segurança: nenhuma iteração pode terminar sem consumir uma
        # linha. Sem isso, uma construção que nenhum branch reconheça travaria o
        # build em loop infinito em vez de falhar visivelmente.
        i_inicial = i

        l = linhas[i]
        cru = l.strip()

        # ---- linha vazia
        if not cru:
            i += 1
            continue

        # ---- bloco de código cercado por ```
        #
        # Precisa vir antes de tudo. Sem este branch, as duas linhas de crase
        # eram lidas como um par de código *inline*, e o bloco inteiro virava um
        # <span class="dado"> — que tem white-space: nowrap. O resultado era uma
        # linha única de 2.300 px estourando a página do Grimório.
        if cru.startswith("```"):
            i += 1
            corpo_cod: list[str] = []
            while i < len(linhas) and not linhas[i].strip().startswith("```"):
                corpo_cod.append(linhas[i])
                i += 1
            i += 1                      # consome a crase de fechamento
            texto = html.escape("\n".join(corpo_cod), quote=False)
            saida.append(f'<pre class="bloco-codigo">{texto}</pre>')
            continue

        # ---- divisor de degrau (# KLEOS n — NOME)
        m = RE_DEGRAU.match(cru)
        if m:
            fecha_criatura()
            saida.append(f'<div class="degrau" id="kleos-{m.group(1)}"><h2>Kleos {m.group(1)} '
                         f'<span>·</span> {inline(m.group(2).title())}</h2>')
            # a linha em itálico logo abaixo, se houver, é a legenda do degrau
            j = i + 1
            while j < len(linhas) and not linhas[j].strip():
                j += 1
            if j < len(linhas) and linhas[j].strip().startswith("*") \
                    and not linhas[j].strip().startswith("**"):
                leg = linhas[j].strip().strip("*")
                saida.append(f"<p>{inline(leg)}</p>")
                i = j
            saida.append("</div>")
            i += 1
            continue

        # ---- cabeçalho de criatura
        m = RE_CRIATURA.match(cru)
        if m:
            fecha_criatura()
            nome, k, degrau = m.group(1), m.group(2), m.group(3)
            saida.append(f'<article class="criatura" id="criatura-{slug(nome)}">')
            saida.append(f"<h3>{inline(nome)}"
                         f'<span class="kleos">Kleos {k} · {inline(degrau)}</span></h3>')
            criatura_aberta = True
            i += 1
            # linha de tipo em itálico
            if i < len(linhas) and linhas[i].strip().startswith("*") \
                    and not linhas[i].strip().startswith("**"):
                saida.append(f'<p class="tipo">{inline(linhas[i].strip().strip("*"))}</p>')
                i += 1
            # bloco de status
            stat: list[str] = []
            while i < len(linhas) and RE_STATUS.match(linhas[i].strip()):
                stat.append(inline(linhas[i].strip())
                            .replace(" · ", ' <span class="sep">·</span> '))
                i += 1
            if stat:
                saida.append('<p class="status">' + "<br>".join(stat) + "</p>")
            continue

        # ---- cabeçalhos comuns
        if cru.startswith("#"):
            nivel = len(cru) - len(cru.lstrip("#"))
            texto = cru[nivel:].strip()
            fecha_criatura()
            ident = id_titulo(texto)
            attr = f' id="{ident}"' if ident else ""
            if nivel == 1:
                saida.append(f"<h2{attr}>{inline(texto)}</h2>")
            elif nivel == 2:
                saida.append(f"<h2{attr}>{inline(texto)}</h2>")
            elif nivel == 3:
                saida.append(f"<h3{attr}>{inline(texto)}</h3>")
            else:
                saida.append(f"<h4{attr}>{inline(texto)}</h4>")
            i += 1
            continue

        # ---- régua
        if re.fullmatch(r"-{3,}|\*{3,}", cru):
            fecha_criatura()
            saida.append('<div class="ornamento">❖</div>')
            i += 1
            continue

        # ---- citação em bloco
        if cru.startswith(">"):
            bloco = []
            aviso = "⚠️" in cru
            while i < len(linhas) and linhas[i].strip().startswith(">"):
                bloco.append(linhas[i].strip().lstrip(">").strip())
                i += 1
            texto = " ".join(x for x in bloco if x)
            cls = "aviso" if aviso else "destaque"
            saida.append(f'<div class="{cls}"><p>{inline(texto)}</p></div>')
            continue

        # ---- tabela
        if cru.startswith("|"):
            bloco = []
            while i < len(linhas) and linhas[i].strip().startswith("|"):
                bloco.append(linhas[i])
                i += 1
            if len(bloco) >= 2:
                saida.append(tabela(bloco))
            continue

        # ---- rótulo de bloco dentro da criatura (TRAÇOS, AÇÕES, ...)
        #
        # O corpo do bloco é recolhido até o próximo rótulo, cabeçalho ou régua,
        # e convertido pela chamada recursiva. Fazer assim em vez de repetir a
        # lógica de listas, tabelas e citações aqui dentro evita o loop infinito
        # que a primeira versão tinha em citações ">" dentro de uma criatura.
        m = RE_ROTULO_BLOCO.match(cru)
        if m and criatura_aberta:
            rot, resto = m.group(1).strip(), m.group(2).strip()
            classe = ""
            if rot.startswith("FRAQUEZA"):
                classe = "fraqueza"
            elif rot.startswith("AO "):
                classe = "morte"

            i += 1
            corpo: list[str] = []
            while i < len(linhas):
                nxt = linhas[i].strip()
                if (RE_ROTULO_BLOCO.match(nxt) or nxt.startswith("#")
                        or re.fullmatch(r"-{3,}", nxt)):
                    break
                corpo.append(linhas[i])
                i += 1

            if classe:
                saida.append(f'<div class="{classe}">')
            saida.append(f'<p class="rotulo-bloco">{inline(rot)}</p>')
            if resto:
                saida.append(f"<p>{inline(resto)}</p>")
            if any(x.strip() for x in corpo):
                saida.append(converter("\n".join(corpo)))
            if classe:
                saida.append("</div>")
            continue

        # ---- listas
        if cru.startswith(("- ", "* ")):
            itens = []
            while i < len(linhas) and linhas[i].strip().startswith(("- ", "* ")):
                itens.append(f"<li>{inline(linhas[i].strip()[2:])}</li>")
                i += 1
            saida.append("<ul>" + "".join(itens) + "</ul>")
            continue
        if re.match(r"^\d+\.\s", cru):
            itens = []
            while i < len(linhas) and re.match(r"^\d+\.\s", linhas[i].strip()):
                itens.append(f"<li>{inline(re.sub(r'^\d+\.\s*', '', linhas[i].strip()))}</li>")
                i += 1
            saida.append("<ol>" + "".join(itens) + "</ol>")
            continue

        # ---- parágrafo
        par = []
        while i < len(linhas):
            n = linhas[i].strip()
            if not n or n.startswith(("|", "#", ">", "- ", "* ")) \
                    or re.fullmatch(r"-{3,}", n) or re.match(r"^\d+\.\s", n) \
                    or RE_ROTULO_BLOCO.match(n):
                break
            par.append(n)
            i += 1
        if par:
            saida.append(f"<p>{inline(' '.join(par))}</p>")

        if i == i_inicial:
            # Construção não reconhecida: emite como parágrafo e segue, para o
            # build nunca travar silenciosamente.
            print(f"  aviso: linha não reconhecida, emitida como parágrafo: {cru[:60]!r}",
                  file=sys.stderr)
            saida.append(f"<p>{inline(cru)}</p>")
            i += 1

    fecha_criatura()
    return "\n".join(saida)


# ===========================================================================
# Montagem
# ===========================================================================

def ler_b64(nome: str) -> str:
    p = BUILD / f"{nome}.b64"
    if not p.exists():
        raise SystemExit(f"Falta {p}. Rode build.ps1, que prepara as capas.")
    return p.read_text(encoding="ascii").strip()


def ler_vendor(nome: str) -> str:
    p = RAIZ / "vendor" / nome
    if not p.exists():
        raise SystemExit(f"Falta {p}. Restaure as bibliotecas incorporadas da ficha.")
    return p.read_text(encoding="utf-8")


LIVROS = (
    ("livro-do-jogador.html", "I", "Livro do Jogador", "jogador"),
    ("bestiario.html", "II", "Bestiário", "bestiario"),
    ("grimorio.html", "III", "Grimório", "grimorio"),
    ("guia.html", "IV", "Guia do Mestre", "guia"),
    ("ficha.html", "V", "Ficha do Herói", "ficha"),
)


def miniestante(pagina_atual: str) -> str:
    """Tridente fixo que abre os outros livros, sem JavaScript."""
    links = []
    for href, tomo, nome, classe in LIVROS:
        if href == pagina_atual:
            continue
        links.append(
            f'<a href="{href}"><span class="mini-capa {classe}">{tomo}</span>'
            f'<span><b>{nome}</b><small>abrir livro</small></span></a>'
        )
    return (
        '<details class="biblioteca-flutuante">'
        '<summary aria-label="Abrir os outros livros" title="Outros livros">'
        '<span aria-hidden="true">♆</span></summary>'
        '<nav aria-label="Outros livros"><strong>Outros livros</strong>'
        + "".join(links)
        + '<a class="estante-completa" href="index.html">Ver a estante completa</a>'
        '</nav></details>'
    )


def aviso_independencia() -> str:
    """Aviso editorial comum a todos os livros publicados no site."""
    return (
        '<aside class="aviso-independencia" role="note">'
        '<strong>Projeto independente, não oficial e sem fins lucrativos.</strong> '
        '<span><em>Percy Jackson</em> e os elementos próprios dessa franquia '
        'pertencem aos seus respectivos autores e titulares, incluindo Rick '
        'Riordan e empresas licenciadas. Este projeto não é afiliado, aprovado '
        'ou patrocinado por eles.</span></aside>'
    )


def envelopar(corpo_e_cabeca: str, descricao: str, pagina_atual: str) -> str:
    """Fecha o livro num documento HTML de verdade.

    Os templates são fragmentos: começam no <title> e seguem no <style>. Sem
    doctype, charset e viewport, um celular renderiza a página a 980 px e o
    leitor recebe um livro ilegível. O corte é no fim do </style>: o que vem
    antes é cabeça, o que vem depois é corpo.
    """
    marca = "</style>"
    i = corpo_e_cabeca.rindex(marca) + len(marca)
    cabeca, corpo = corpo_e_cabeca[:i], corpo_e_cabeca[i:]
    return (
        "<!doctype html>\n"
        '<html lang="pt-BR">\n<head>\n'
        '<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
        f'<meta name="description" content="{html.escape(descricao, quote=True)}">\n'
        + cabeca
        + "\n</head>\n<body>\n"
        + miniestante(pagina_atual)
        + "\n"
        + corpo.strip()
        + "\n"
        + aviso_independencia()
        + "\n</body>\n</html>\n"
    )


def montar(template_nome: str, saida_nome: str, css: str,
           substituicoes: dict[str, str], descricao: str = "") -> None:
    s = (TEMPLATE / template_nome).read_text(encoding="utf-8")
    s = s.replace("{{CSS}}", css)
    for k, v in substituicoes.items():
        s = s.replace("{{" + k + "}}", v)
    faltando = re.findall(r"\{\{[A-Z_]+\}\}", s)
    if faltando:
        raise SystemExit(f"{saida_nome}: marcadores não substituídos: {set(faltando)}")
    s = envelopar(s, descricao, saida_nome)
    (RAIZ / saida_nome).write_text(s, encoding="utf-8")
    kb = round((RAIZ / saida_nome).stat().st_size / 1024)
    print(f"  {saida_nome:<26} {kb:>5} KB")


def main() -> None:
    css = (TEMPLATE / "livro.css").read_text(encoding="utf-8")
    print("montando:")

    # --- Livro do Jogador (escrito à mão no template)
    montar("livro-do-jogador.html", "livro-do-jogador.html", css, {
        "CAPA": ler_b64("capa"),
        "CONTRACAPA": ler_b64("contracapa"),
    }, descricao=(
        "Livro do Jogador: como jogar, criação de personagem em sete etapas, combate, equipamento, condições e o motor de criação de habilidades."
    ))

    # --- Bestiário (a partir dos markdown)
    partes = [
        "bestiario/01-a-escala-de-kleos.md",
        "bestiario/02-forja-de-monstros.md",
        "bestiario/03-criaturas-kleos-1-a-5.md",
        "bestiario/04-criaturas-kleos-6-a-11.md",
    ]
    corpo = []
    for n, arq in enumerate(partes, 1):
        md = (RAIZ / arq).read_text(encoding="utf-8")
        # tira o título "# Livro II — Bestiário" repetido em cada arquivo
        md = re.sub(r"^# Livro II — Bestiário\s*\n", "", md)
        corpo.append(f'<section class="capitulo" id="parte{n}">')
        corpo.append(converter(md))
        corpo.append("</section>")
    montar("bestiario.html", "bestiario.html", css, {
        "CAPA": ler_b64("capa-bestiario"),
        "CONTEUDO": "\n".join(corpo),
    }, descricao=(
        "Bestiário: a Escala de Kleos, o motor de criação de monstros e 38 criaturas, do sátiro errante a Tifão."
    ))

    # --- Grimório (a partir de regras/magia-da-nevoa.md)
    md = (RAIZ / "regras/magia-da-nevoa.md").read_text(encoding="utf-8")
    md = re.sub(r"^# Livro I.*?\n", "", md)
    md = re.sub(r"^## Parte V — Magia da Névoa\s*\n", "", md, flags=re.M)
    # --- Guia do Mestre (escrito à mão)
    montar("guia.html", "guia.html", css, {
        "CAPA": ler_b64("capa-guia"),
    })

    # --- Ficha do Herói (formulário, sem markdown)
    montar("ficha.html", "ficha.html", css, {
        "CAPA": ler_b64("capa-ficha"),
        "HTML2CANVAS": ler_vendor("html2canvas.min.js"),
        "JSPDF": ler_vendor("jspdf.umd.min.js"),
    }, descricao=(
        "Ficha do Herói preenchível: complete no navegador, adicione o retrato do personagem e baixe em PDF."
    ))

    montar("grimorio.html", "grimorio.html", css, {
        "CAPA": ler_b64("capa-grimorio"),
        "CONTEUDO": '<section class="capitulo" id="parte1">'
                    + converter(md) + "</section>",
    }, descricao=(
        "Grimório: a Magia da Névoa. Magia aprendida, Fórmulas, Repositório e a regra de Descrença."
    ))


if __name__ == "__main__":
    main()

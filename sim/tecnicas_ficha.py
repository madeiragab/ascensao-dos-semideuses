"""As 36 técnicas da ficha contra as 36 técnicas do livro.

A ficha passou a escolher técnicas em vez de aceitar texto livre, e a somar
sozinha o que elas mudam em número. Isso cria duas cópias da mesma lista: uma
no Livro do Jogador e outra na ficha. Cópia que ninguém compara vira divergência
— alguém corrige o livro, a ficha continua oferecendo a versão velha, e o
jogador monta um personagem que não existe.

Este arquivo lê as duas e compara nome por nome, tier por tier. Confere também
que toda técnica com efeito automático na ficha existe na lista, que as vagas
abrem nos níveis certos e que os Tiers 2 e 3 só aparecem a partir dos níveis 6
e 12.

Rodar de dentro da pasta sim/:
    python tecnicas_ficha.py
"""

import pathlib
import re
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

RAIZ = pathlib.Path(__file__).resolve().parent.parent
FICHA = RAIZ / "template" / "ficha.html"
LIVRO = RAIZ / "template" / "livro-do-jogador.html"

CHAVE = {"Guardião": "guardiao", "Furioso": "furioso", "Oráculo": "oraculo"}
NIVEIS_TECNICA = [1, 3, 6, 9, 12, 15, 18]
NIVEL_DO_TIER = {1: 1, 2: 6, 3: 12}


def limpar(texto: str) -> str:
    return re.sub(r"\s+", " ", re.sub(r"<[^>]*>", "", texto)).strip()


def tecnicas_do_livro() -> dict:
    """Tier 1 sai dos cartões de classe; Tiers 2 e 3 do capítulo das técnicas."""
    html = LIVRO.read_text(encoding="utf-8")
    achado = {}
    for bloco in re.finditer(r'<div class="classe">(.*?)\n  </div>', html, re.S):
        corpo = bloco.group(1)
        classe = re.search(r'<h3 style="margin:0;">(.*?)</h3>', corpo).group(1)
        corte = corpo.find("Escolha uma técnica")
        for cartao in re.finditer(r"<h5>(.*?)</h5><p>(.*?)</p>", corpo[corte:], re.S):
            achado.setdefault(CHAVE[classe], set()).add((1, limpar(cartao.group(1))))
    for bloco in re.finditer(
            r"<h4>(Guardião|Furioso|Oráculo) · Tier (\d)\b.*?</h4>(.*?)(?=<h4>|<h3|<h2)",
            html, re.S):
        classe, tier = CHAVE[bloco.group(1)], int(bloco.group(2))
        for cartao in re.finditer(r"<h5>(.*?)</h5><p>(.*?)</p>", bloco.group(3), re.S):
            achado.setdefault(classe, set()).add((tier, limpar(cartao.group(1))))
    return achado


def tecnicas_da_ficha() -> dict:
    html = FICHA.read_text(encoding="utf-8")
    corte = html.index("var TECNICAS = {")
    corpo = html[corte:html.index("var EFEITO_TECNICA", corte)]
    achado = {}
    classe = None
    for linha in corpo.split("\n"):
        cabeca = re.match(r"\s*(guardiao|furioso|oraculo):\s*\[", linha)
        if cabeca:
            classe = cabeca.group(1)
            achado[classe] = set()
            continue
        item = re.match(r'\s*\{ t: (\d), n: "(.*?)",', linha)
        if item and classe:
            achado[classe].add((int(item.group(1)), item.group(2)))
    return achado


def efeitos_da_ficha() -> set:
    html = FICHA.read_text(encoding="utf-8")
    corte = html.index("var EFEITO_TECNICA = {")
    corpo = html[corte:html.index("var NIVEL_DO_TIER", corte)]
    return set(re.findall(r'^  "(.+?)": \{', corpo, re.M))


def constantes_da_ficha() -> tuple:
    html = FICHA.read_text(encoding="utf-8")
    niveis = re.search(r"var NIVEIS_TECNICA\s*=\s*\[(.*?)\]", html).group(1)
    tiers = re.search(r"var NIVEL_DO_TIER = \{(.*?)\}", html).group(1)
    return ([int(n) for n in niveis.split(",")],
            {int(k): int(v) for k, v in re.findall(r"(\d):\s*(\d+)", tiers)})


def main() -> None:
    falhas = []
    livro, ficha = tecnicas_do_livro(), tecnicas_da_ficha()

    print("Técnicas por classe — livro × ficha:")
    for classe in ("guardiao", "furioso", "oraculo"):
        no_livro, na_ficha = livro.get(classe, set()), ficha.get(classe, set())
        print(f"  {classe:>9}: livro {len(no_livro):>2} · ficha {len(na_ficha):>2}")
        for tier, nome in sorted(no_livro - na_ficha):
            falhas.append(f"{classe}: o livro tem '{nome}' (Tier {tier}) e a ficha não oferece")
        for tier, nome in sorted(na_ficha - no_livro):
            falhas.append(f"{classe}: a ficha oferece '{nome}' (Tier {tier}) que não está no livro")

    total_livro = sum(len(v) for v in livro.values())
    if total_livro != 36:
        falhas.append(f"o livro tem {total_livro} técnicas; eram 36 quando isto foi escrito")

    # todo efeito automático precisa apontar para uma técnica que existe
    todas = {nome for conjunto in ficha.values() for _, nome in conjunto}
    print("\nEfeitos automáticos declarados:", len(efeitos_da_ficha()))
    for nome in sorted(efeitos_da_ficha()):
        if nome not in todas:
            falhas.append(f"a ficha calcula um efeito para '{nome}', que não está na lista de técnicas")

    niveis, tiers = constantes_da_ficha()
    print("Vagas nos níveis:", niveis, "· tiers abrem em:", tiers)
    if niveis != NIVEIS_TECNICA:
        falhas.append(f"as vagas da ficha abrem em {niveis}; a tabela do livro diz {NIVEIS_TECNICA}")
    if tiers != NIVEL_DO_TIER:
        falhas.append(f"os tiers da ficha abrem em {tiers}; o livro diz {NIVEL_DO_TIER}")

    # quantas opções cada nível oferece, que é o que o jogador vê
    print("\nOpções oferecidas ao Guardião por nível:")
    for nivel in (1, 5, 6, 11, 12, 20):
        disponiveis = [n for t, n in ficha["guardiao"] if nivel >= NIVEL_DO_TIER[t]]
        vagas = len([n for n in NIVEIS_TECNICA if n <= nivel])
        print(f"  nível {nivel:>2}: {len(disponiveis):>2} técnicas para {vagas} vaga(s)")
        if len(disponiveis) < vagas:
            falhas.append(f"nível {nivel}: {vagas} vagas para só {len(disponiveis)} técnicas")

    print()
    if falhas:
        for f in falhas:
            print("FALHOU:", f)
        raise SystemExit(1)
    print("As 36 técnicas da ficha são as 36 do livro, nos mesmos tiers,")
    print("e todo efeito somado automaticamente aponta para uma delas.")


if __name__ == "__main__":
    main()

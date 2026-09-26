"""Fases — o chefe que não cai num golpe só.

A queixa que saiu da mesa: "o sistema depende de status e cenas pras lutas
durarem mais". Nos logs da campanha, quase todo combate terminava num golpe —
"Rouge G2, 20", "Impacto Zero G5, 20" —, e o único chefe que aguentou foi o
Ouroboros, porque o Mestre inventou na hora que ele desfazia o dano. Regra
improvisada para segurar uma luta que a regra escrita não segurava.

Medido antes de mexer: uma habilidade no Teto tirava de 49% a 71% do PV do
monstro do encontro justo. E o simulador ainda subestimava o golpe: rolava o
golpe Físico dos marciais com o Atributo Divino, e não com Força. Corrigido, o
trio vencia o encontro justo em 96% a 98% das vezes, em 1,8 rodada.

A regra, que este arquivo segura:

  · o CHEFE do encontro tem Fases — a criatura que luta sozinha, ou a de Kleos
    mais alto num chefe com lacaios. Bando e lacaio não têm;
  · Kleos 2: duas Fases · 3 a 7: três · 8 ou mais: quatro. O PV se divide em
    partes iguais;
  · o golpe que quebra uma Fase para ali — o excesso se perde. Fase quebrada não
    volta com cura;
  · ao quebrar uma Fase, a criatura se livra de toda condição que a afete.

O grupo quebra mais ou menos uma Fase por rodada, então o número de Fases é o
que segura a DURAÇÃO da luta. O dano da Tábua, que não mudou, segura a VITÓRIA.

As regressões:
  1. com Fases, nenhum golpe tira mais que uma Fase do chefe;
  2. a luta do trio fica mais longa que sem Fases em toda faixa;
  3. o encontro justo do Livro II, de 1 a 4 jogadores, vence entre 50% e 97%
     das vezes na média de cada faixa;
  4. o Bestiário diz o mesmo número de Fases e a mesma tabela de Kleos do Grupo
     que o motor usa.

Rodar de dentro da pasta sim/:
    python fases.py
"""

import pathlib
import random
import re
import sys

import combate
import completo as C
from kleos import TABUA
from niveis import KLEOS_JUSTO, grau, kleos_do_grupo, teto_de_custo

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

N = 1500
FAIXAS = {1: (1, 3), 2: (5, 7), 3: (9, 11), 4: (13, 15), 5: (17, 20)}
BESTIARIO = pathlib.Path(__file__).resolve().parent.parent / "bestiario"


def mede(nivel: int, k: int, jogadores: int = 3, fases: bool = True, n: int = N):
    combate.FASES_ATIVAS = fases
    try:
        random.seed(20260926 + nivel + 31 * jogadores)
        return C.mede(nivel, k, recusas=2, n=n, jogadores=jogadores)
    finally:
        combate.FASES_ATIVAS = True


def golpe_no_teto(falhas: list) -> None:
    print("1. O GOLPE NO TETO CONTRA O CHEFE DO ENCONTRO JUSTO DO TRIO")
    print("   Dano médio de uma habilidade no Teto, em fração do PV do chefe.")
    print(f"{'nível':>6}{'Kleos':>7}{'PV':>6}{'Fases':>7}{'golpe':>8}"
          f"{'sem Fases':>11}{'com Fases':>11}")
    print("-" * 56)
    for nivel in (1, 5, 9, 13, 17, 20):
        k = kleos_do_grupo(nivel, 3)
        pv = TABUA[k][0]
        nf = combate.fases_do_kleos(k)
        golpe = teto_de_custo(nivel) * grau(nivel) * 4.5 + 4
        sem = min(1.0, golpe / pv)
        com = min(sem, 1 / nf)
        print(f"{nivel:>6}{k:>7}{pv:>6}{nf:>7}{golpe:>8.0f}{sem:>11.0%}{com:>11.0%}")
        # Prova no motor, não só na conta: um chefe fresco recebe o golpe.
        chefe = combate.Lutador.de_monstro(C.monstro_padrao(k))
        chefe.sofrer(int(golpe * 3))
        if nf > 1 and chefe.pv != pv * (nf - 1) // nf:
            falhas.append(f"nível {nivel}: um golpe passou de uma Fase no motor")
    print()


def duracao(falhas: list) -> None:
    print("2. O TRIO CONTRA O ENCONTRO JUSTO, SEM E COM FASES")
    print(f"{'faixa':>6}{'Kleos':>7}{'sem Fases':>18}{'com Fases':>18}")
    print("-" * 50)
    for g, niveis in FAIXAS.items():
        k = KLEOS_JUSTO[g][3]
        sem = [mede(nv, k, fases=False) for nv in niveis]
        com = [mede(nv, k) for nv in niveis]
        vs = sum(r["vitoria"] for r in sem) / 2
        rs = sum(r["rodadas"] for r in sem) / 2
        vc = sum(r["vitoria"] for r in com) / 2
        rc = sum(r["rodadas"] for r in com) / 2
        print(f"{'G' + str(g):>6}{k:>7}{vs:>10.0%} {rs:>4.1f} rod{vc:>10.0%} {rc:>4.1f} rod")
        if rc < rs + 0.5:
            falhas.append(f"Grau {g}: com Fases a luta dura {rc:.1f} rodadas, "
                          f"contra {rs:.1f} sem — as Fases não seguraram")
    print()


def tabela_do_grupo(falhas: list) -> None:
    print("3. O KLEOS DO GRUPO, DE UM A QUATRO JOGADORES")
    print("   Média das duas pontas de cada faixa. Com um jogador, o chefe solo.")
    print(f"{'faixa':>6}" + "".join(f"{f'{j} jog.':>18}" for j in (1, 2, 3, 4)))
    print("-" * 78)
    for g, niveis in FAIXAS.items():
        linha = f"{'G' + str(g):>6}"
        for jogadores in (1, 2, 3, 4):
            k = KLEOS_JUSTO[g][jogadores]
            res = [mede(nv, k, jogadores) for nv in niveis]
            v = sum(r["vitoria"] for r in res) / 2
            rod = sum(r["rodadas"] for r in res) / 2
            linha += f"{'K' + str(k):>6}{v:>6.0%}{rod:>5.1f}r "
            if not 0.50 <= v <= 0.97:
                falhas.append(f"Grau {g}, {jogadores} jogador(es): o encontro "
                              f"justo vence {v:.0%}, fora de 50% a 97%")
        print(linha)
    print()


def livro(falhas: list) -> None:
    print("4. O BESTIÁRIO CONTRA O MOTOR")
    forja = (BESTIARIO / "02-forja-de-monstros.md").read_text(encoding="utf-8")
    escala = (BESTIARIO / "01-a-escala-de-kleos.md").read_text(encoding="utf-8")

    m = re.search(r"\| Kleos \| Fases \|\n\|[-| ]+\|\n((?:\|.*\|\n)+)", forja)
    if not m:
        falhas.append("a tabela de Fases sumiu da Forja de Monstros")
    else:
        vistos = set()
        for linha in m.group(1).strip().splitlines():
            faixa, fases = [c.strip(" *") for c in linha.strip("|").split("|")][:2]
            ks = [int(x) for x in re.findall(r"\d+", faixa)]
            if "ou mais" in faixa:
                kleos = range(ks[0], 12)
            elif len(ks) == 2:
                kleos = range(ks[0], ks[1] + 1)
            else:
                kleos = ks
            no_livro = 1 if fases.lower().startswith("nenhuma") else int(fases)
            for k in kleos:
                vistos.add(k)
                if no_livro != combate.fases_do_kleos(k):
                    falhas.append(f"Kleos {k}: o Bestiário diz {no_livro} Fase(s), "
                                  f"o motor usa {combate.fases_do_kleos(k)}")
        if vistos != set(range(1, 12)):
            falhas.append("a tabela de Fases não cobre os onze degraus")
        print("  tabela de Fases: conferida contra fases_do_kleos()")

    m = re.search(r"\| Nível \| 1 herói[^\n]*\n\|[-| ]+\|\n((?:\|.*\|\n)+)", escala)
    if not m:
        falhas.append("a tabela de Kleos do Grupo sumiu da Escala de Kleos")
    else:
        for g, linha in enumerate(m.group(1).strip().splitlines(), start=1):
            celulas = [c.strip(" *") for c in linha.strip("|").split("|")][1:]
            valores = [int(c) for c in celulas]
            esperado = [KLEOS_JUSTO[g][j] for j in (1, 2, 3, 4, 5, 6)]
            if valores != esperado:
                falhas.append(f"Grau {g}: o Bestiário diz {valores}, "
                              f"o motor usa {esperado}")
        print("  tabela de Kleos do Grupo: conferida contra KLEOS_JUSTO")
    for frase in ("o excesso se perde", "Só o chefe tem Fases",
                  "Fase quebrada não volta"):
        if frase.lower() not in forja.lower():
            falhas.append(f"a Forja de Monstros não diz mais {frase!r}")
    print()


def main() -> None:
    falhas = []
    golpe_no_teto(falhas)
    duracao(falhas)
    tabela_do_grupo(falhas)
    livro(falhas)
    if falhas:
        for f in falhas:
            print("FALHOU:", f)
        raise SystemExit(1)
    print("Nenhum golpe tira mais que uma Fase do chefe, a luta do trio dura mais")
    print("em toda faixa, e o encontro justo de um a quatro jogadores continua")
    print("justo. O Bestiário diz o mesmo que o motor.")


if __name__ == "__main__":
    main()

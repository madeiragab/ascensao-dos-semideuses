"""Mede a linha Defesa do Capítulo Sete — a habilidade de +DEF que ninguém montava.

A queixa que saiu da mesa, dita assim: "criar uma técnica que aumenta DEF é
inútil, totalmente". Os logs da campanha confirmam — a primeira habilidade
defensiva do jogador nasceu como +1 DEF e foi trocada por PV temporários no
mesmo minuto, e a defesa que ele de fato usou o jogo inteiro foi uma reação que
impõe Desvantagem ao golpe.

Medido antes de mexer, com o Guardião pagando em SP — o mesmo SP do golpe
grande dele —, no encontro justo de cada tamanho de mesa:

    +1 DEF sustentada, com a ação (a regra até 0.17)   −9 a −31 pontos
    reação que impõe Desvantagem num ataque              +1 a +10 pontos

E o teto: +4 DEF DE GRAÇA no grupo inteiro, a luta toda, vale de +2 a +15.
A DEF vale pouco num combate de duas ou três rodadas em que o Sopro mira
Reflexos; e qualquer coisa que custe a ação perde para bater.

O conserto, que este arquivo segura:

  · um ponto de Defesa dá +2 DEF de uma vez (o máximo continua +2), para
    tantos alvos quanto o Grau;
  · instantânea, ela vale até o início do seu próximo turno;
  · o livro manda montá-la como reação — 2 pontos no Grau 1.

As regressões:
  1. a Defesa reativa soma vitória em média, sem virar obrigatória (≤ 10);
  2. ela fica perto da Desvantagem reativa (a régua que a mesa já aceitou);
  3. a mesma Defesa gastando a ação continua pior que atacar — se isso mudar,
     o aviso do livro ficou errado.

Rodar de dentro da pasta sim/:
    python defesa.py
"""

import pathlib
import random
import sys

import completo as C
from combate import Lutador, rola, rola_d20
from fichas import guardiao_ares
from kleos import TABUA, monstro_padrao
from niveis import grau, kleos_do_grupo, personagem

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

N = 2000
NIVEIS = (3, 5, 9, 13, 17)
MESAS = {
    1: ("guardiao",),
    2: ("guardiao", "furioso"),
    3: ("guardiao", "furioso", "oraculo"),
    4: ("guardiao", "furioso", "oraculo", "furioso"),
}

# nome: (pontos no Grau em que é paga, Grau pago, alvos, tipo)
#   "reacao"   +2 DEF até o próximo turno do Guardião, no primeiro ataque da rodada
#   "desv"     Desvantagem no primeiro ataque da rodada
#   "acao"     +2 DEF sustentada, conjurada com a ação, Concentração
VARIANTES = ("reacao", "desv", "acao")


def fortitude(nivel: int) -> int:
    f = personagem(guardiao_ares(), nivel)
    return 14 + f.mods["constituicao"] + f.prof


def encontro(nivel: int, jogadores: int) -> int:
    """O encontro justo do Livro II; numa mesa solo, o chefe dela."""
    return kleos_do_grupo(nivel, jogadores)


def luta(nivel: int, jogadores: int, variante: str) -> bool:
    k = encontro(nivel, jogadores)
    herois = [C.montar_heroi(c, nivel, True) for c in MESAS[jogadores]]
    g = herois[0]
    g.tecnicas = []          # sem Escudo Vínculo: mede só a habilidade
    for h in herois:
        h.aliados = herois
    m = Lutador.de_monstro(monstro_padrao(k))
    m.recusas, m.recusas_gastas, m.aliados = 2, 0, [m]
    fraca, sopro = C.DEFESAS[k][1], TABUA[k][3]
    arremetidas = 2 if k >= 8 else 1

    # Reação e Desvantagem pagas no Grau 1: 1 do efeito, 1 da reação.
    # A ação paga no Grau cheio, que é o que alcança o grupo.
    G = grau(nivel)
    reacao = {"livre": True, "alvos": []}
    sust = {"ativo": False, "alvos": []}
    fort = fortitude(nivel)
    custo_acao = 2 * G
    manter = max(1, custo_acao // 2)

    def soltar(estado):
        for a in estado["alvos"]:
            a.defesa -= 2
        estado["alvos"] = []
        estado["ativo"] = False

    if variante in ("reacao", "desv"):
        atacar = m.atacar

        def atacar_com_reacao(alvo, vantagem=False, desvantagem=False, **kw):
            if reacao["livre"] and g.vivo and g.sp >= 2:
                g.sp -= 2
                reacao["livre"] = False
                if variante == "desv":
                    desvantagem = True
                else:
                    reacao["alvos"] = [alvo]
                    alvo.defesa += 2
            return atacar(alvo, vantagem=vantagem, desvantagem=desvantagem, **kw)
        m.atacar = atacar_com_reacao

    if variante == "acao":
        sofrer = g.sofrer

        def sofrer_com_concentracao(dano):
            sofrer(dano)
            if sust["ativo"] and dano > 0 and rola_d20() + max(2, dano // 2 - 8) >= fort:
                soltar(sust)
            if not g.vivo and sust["ativo"]:
                soltar(sust)
        g.sofrer = sofrer_com_concentracao

    ordem = sorted(herois + [m], key=lambda c: rola_d20() + c.iniciativa_bonus,
                   reverse=True)
    sopro_pronto = True
    for _ in range(40):
        restantes = arremetidas
        for lut in ordem:
            if not lut.vivo:
                continue
            if lut is m:
                if m.perde_o_turno:
                    m.resolver_fim_de_turno()
                else:
                    if not sopro_pronto and rola(6) >= 5:
                        sopro_pronto = True
                    if sopro_pronto:
                        sopro_pronto = False
                        for h in herois:
                            if h.vivo:
                                passou = rola_d20() + h.prof >= 8 + m.bonus_ataque
                                h.receber(sopro // 2 if passou else sopro, m)
                    else:
                        m.turno([m], herois)
                for h in herois:
                    if (h.vivo and h.controle_ativo is m
                            and not C.rolagem_de_efeito(h, m, fraca)):
                        m.condicoes.pop("perde_turno", None)
                        h.controle_ativo = None
                if not any(h.vivo for h in herois):
                    break
                continue

            agiu = False
            if lut is g:
                for a in reacao["alvos"]:
                    a.defesa -= 2
                reacao["alvos"], reacao["livre"] = [], True
                if variante == "acao":
                    if sust["ativo"]:
                        if g.sp >= manter:
                            g.sp -= manter
                        else:
                            soltar(sust)
                    elif g.sp >= custo_acao and m.vivo:
                        g.sp -= custo_acao
                        outros = sorted((h for h in herois if h is not g and h.vivo),
                                        key=lambda h: h.pv_max)
                        sust["alvos"] = ([g] + outros)[:G]
                        for a in sust["alvos"]:
                            a.defesa += 2
                        sust["ativo"] = agiu = True
            if not agiu and lut.usa_habilidade and m.vivo:
                if (lut.papel == "controle" and C.recurso_de(lut) >= lut.custo_controle
                        and not m.perde_o_turno):
                    C.gastar(lut, lut.custo_controle)
                    if C.rolagem_de_efeito(lut, m, fraca):
                        m.aplicar_condicao("perde_turno", 1)
                        lut.controle_ativo = m
                    agiu = True
                elif lut.papel == "dano" and C.recurso_de(lut) >= lut.custo_dano:
                    C.gastar(lut, lut.custo_dano)
                    C.golpe_de_habilidade(lut, m)
                    agiu = True
            if not agiu:
                lut.turno(herois, [m])
            if (restantes > 0 and m.vivo and not m.perde_o_turno
                    and any(h.vivo for h in herois)):
                restantes -= 1
                m.atacar(max((h for h in herois if h.vivo), key=lambda h: h.pv))
            if not any(h.vivo for h in herois) or not m.vivo:
                break
        if not any(h.vivo for h in herois) or not m.vivo:
            return any(h.vivo for h in herois)
    return False


def vitoria(nivel: int, jogadores: int, variante: str, n: int = N) -> float:
    random.seed(20260926 + 97 * nivel + jogadores)
    return sum(luta(nivel, jogadores, variante) for _ in range(n)) / n


def main() -> None:
    falhas = []
    print("A linha Defesa, com o custo de verdade: o Guardião paga em SP")
    print("Diferença de vitória contra o mesmo grupo sem a habilidade.")
    print()
    print(f"{'mesa':>5}{'nível':>7}{'Kleos':>7}{'sem':>7}"
          f"{'Defesa reação':>15}{'Desvantagem':>13}{'Defesa com ação':>17}")
    print("-" * 71)
    for jogadores in MESAS:
        somas = {v: 0.0 for v in VARIANTES}
        for nivel in NIVEIS:
            base = vitoria(nivel, jogadores, "base")
            linha = (f"{jogadores:>5}{nivel:>7}{encontro(nivel, jogadores):>7}"
                     f"{base:>7.0%}")
            for v, largura in zip(VARIANTES, (15, 13, 17)):
                d = vitoria(nivel, jogadores, v) - base
                somas[v] += d
                linha += f"{d:>+{largura}.0%}"
            print(linha)
        media = {v: somas[v] / len(NIVEIS) for v in VARIANTES}
        print(f"{'':>5}{'média':>14}{'':>7}{media['reacao']:>+15.1%}"
              f"{media['desv']:>+13.1%}{media['acao']:>+17.1%}")
        print()

        if not -0.01 <= media["reacao"] <= 0.10:
            falhas.append(f"{jogadores} jogador(es): a Defesa reativa mede "
                          f"{media['reacao']:+.1%}, fora de −1 a +10 pontos")
        if abs(media["reacao"] - media["desv"]) > 0.04:
            falhas.append(f"{jogadores} jogador(es): Defesa reativa {media['reacao']:+.1%} "
                          f"longe da Desvantagem reativa {media['desv']:+.1%}")
        if media["acao"] >= 0:
            falhas.append(f"{jogadores} jogador(es): a Defesa com ação mede "
                          f"{media['acao']:+.1%} — o aviso do livro ficou errado")

    raiz = pathlib.Path(__file__).resolve().parent.parent
    livro = (raiz / "template" / "livro-do-jogador.html").read_text(encoding="utf-8")
    for frase in ("+2 DEF para 1 alvo", "Monte a Defesa como reação",
                  "até o início do seu próximo turno"):
        if frase not in livro:
            falhas.append(f"o livro não diz mais {frase!r}")

    if falhas:
        for f in falhas:
            print("FALHOU:", f)
        raise SystemExit(1)
    print("A Defesa reativa soma vitória sem virar obrigatória, fica no mesmo")
    print("lugar da Desvantagem, e a Defesa com a ação continua sendo a armadilha")
    print("que o livro avisa que é.")


if __name__ == "__main__":
    main()

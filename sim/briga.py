"""Briga — a luta sem arma, e o crítico que não tinha o que dobrar.

A cena que abriu este arquivo saiu do log da campanha: uma briga combinada na
arena do acampamento, "sem arma, sem poder", entre o David (Guardião, nível 10,
98 PV) e o Caleb, um valentão de Kleos 1. O David tira 20 natural num soco na
barriga — e a regra não tinha resposta:

    "soco desarmado causa 1 + FOR. Como David tem FOR +0, são 1 de dano; o
     crítico dobra dados, mas o soco não tem dado para dobrar."

O Mestre inventou na hora ("em combate desarmado, se sair crítico, o dano do
soco também dobra") e o crítico virou 2 de dano. Um semideus de nível 10
socando por 1 — o mesmo soco do nível 1, para sempre, enquanto a arma dele
ganhava dado pelo Grau do item.

A regra nova, que este arquivo segura:

  · o punho tem DADO: 1d4 + Força ou Destreza, e sobe como uma arma forjada —
    a linha do Grau do item que o seu nível alcança, com o d4 no lugar do dado
    da arma (2d4 +1 no nível 6, 2d4 +2 no 10, 3d4 +2 no 15);
  · crítico desarmado rola os dados duas vezes, como qualquer arma — e o golpe
    ENCAIXA: você escolhe Caído, Sem Ar (Desprevenido até o seu próximo turno)
    ou empurrado 1,5 m. A arma dobra mais; o punho encaixa;
  · o punho pode NOCAUTEAR: a 0 PV o alvo fica Inconsciente e estável, sem
    Agonia;
  · e, contra soco, existe guarda: BLOQUEAR é uma reação — 1d20 + o seu ataque
    desarmado contra o total do golpe; igualou, bloqueou. Crítico não se
    bloqueia.

Por que o Bloquear: sem ele a briga entre iguais é uma corrida. Os dois
acertam quase todo soco, o dano varia pouco, e quem começa chega primeiro —
dois Furiosos de nível 15 decidiam 90% das brigas na iniciativa. Com a guarda,
um golpe por rodada vira disputa, e a briga volta a ter vai e volta.

As regressões:
  1. o punho fica sempre abaixo da arma do mesmo nível (é o plano B, não o
     plano A), mas longe do 1 + FOR que ficava parado;
  2. uma briga combinada entre semideuses do mesmo nível, "até a metade dos
     PV", acaba em poucas rodadas em qualquer nível;
  3. começar a briga ajuda sem decidir: no espelho, até 75%, a mesma régua
     do duelo armado (duelo.py);
  4. a diferença de nível continua valendo, e o soco do semideus deixa de ser
     o do nível 1: o David, com Força +0, levava 8,7 rodadas para nocautear
     um valentão de Kleos 1, a 1 de dano por soco; agora, 1,4;
  5. o Livro do Jogador diz a mesma tabela do punho que o motor usa.

Rodar de dentro da pasta sim/:
    python briga.py
"""

import pathlib
import random
import re
import sys
from dataclasses import dataclass, field

from combate import rola, rola_d20
from fichas import furioso_ares, guardiao_ares, oraculo_atena
from fichas_v1 import def_com_armadura
from forja import DADO_DA_ARMA, item_do_nivel
from kleos import TABUA
from niveis import ataques_por_turno, personagem

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

N = 3000
NIVEIS = (1, 3, 6, 10, 15, 20)
BASE = {"guardiao": guardiao_ares, "furioso": furioso_ares, "oraculo": oraculo_atena}
TEMPLATE = pathlib.Path(__file__).resolve().parent.parent / "template"
LIVRO = TEMPLATE / "livro-do-jogador.html"
FICHA = TEMPLATE / "ficha.html"


# ---------------------------------------------------------------------------
# A regra
# ---------------------------------------------------------------------------

def punho(nivel: int) -> tuple[int, int]:
    """(quantos d4, bônus de ataque e dano) do punho naquele nível.

    É a linha do Grau do item que o nível alcança — a mesma tabela da forja —,
    com o d4 no lugar do dado da arma.
    """
    _, _, dados_extra, bonus, _ = item_do_nivel(nivel)
    return 1 + dados_extra, bonus


def media_por_acerto(dados: int, faces: int, fixo: int) -> float:
    return dados * (faces + 1) / 2 + fixo


# ---------------------------------------------------------------------------
# Os brigões
# ---------------------------------------------------------------------------

@dataclass
class Brigao:
    nome: str
    pv_max: int
    defesa: int
    ataque: int
    dados: int            # quantos d4 (0 = o soco antigo, sem dado)
    fixo: int
    ataques: int
    pv: int = 0
    sem_ar_ate: int = -1  # Desprevenido até a vez deste número de turno
    caido: bool = False
    bloqueia: bool = True
    reacao: bool = True   # volta no começo do próprio turno
    encaixes: dict = field(default_factory=dict)

    def __post_init__(self):
        self.pv = self.pv_max


def semideus(classe: str, nivel: int, regra: str = "nova",
             forca: int | None = None) -> Brigao:
    """Sem arma e sem escudo; a armadura que estiver vestindo continua.

    regra: "antiga" (1 + FOR, sem dado, sem guarda), "sem guarda" (o punho
    novo sem o Bloquear) ou "nova". forca troca o modificador de Força — o
    David do log tem Força +0.
    """
    f = personagem(BASE[classe](), nivel)
    m_for = f.mods["forca"] if forca is None else forca
    atributo = max(m_for, f.mods["destreza"])   # o punho tem Fineza
    armadura = ("peitoral" if nivel >= 5 else "escamas") if classe == "guardiao" else "couro_batido"
    defesa = def_com_armadura(f.mods["destreza"], armadura, False)
    if regra == "antiga":
        return Brigao(classe, f.pv_max, defesa, m_for + f.prof, 0,
                      max(1, 1 + m_for), ataques_por_turno(classe, nivel),
                      bloqueia=False)
    dados, bonus = punho(nivel)
    return Brigao(classe, f.pv_max, defesa, atributo + f.prof + bonus,
                  dados, atributo + bonus, ataques_por_turno(classe, nivel),
                  bloqueia=regra == "nova")


def valentao(k: int) -> Brigao:
    """Uma criatura da Tábua brigando de mão: o ataque e o dano dela."""
    pv, defesa, atk, dano, n = TABUA[k]
    return Brigao(f"Kleos {k}", pv, defesa, atk, 0, max(1, dano // n), n,
                  bloqueia=False)


# ---------------------------------------------------------------------------
# A briga
# ---------------------------------------------------------------------------

def soco(a: Brigao, alvo: Brigao, turno: int, termos: str) -> None:
    vantagem = alvo.sem_ar_ate >= turno or alvo.caido
    nat = rola_d20(vantagem=vantagem)
    if nat == 1:
        return
    critico = nat == 20
    total = nat + a.ataque
    if not critico and total < alvo.defesa:
        return
    # Bloquear: reação, contra soco que acertaria. Crítico não se bloqueia.
    if alvo.bloqueia and alvo.reacao and not critico and a.dados:
        alvo.reacao = False
        if rola_d20() + alvo.ataque >= total:
            return
    if a.dados:
        vezes = 2 if critico else 1
        dano = sum(rola(4) for _ in range(a.dados * vezes)) + a.fixo
    else:
        dano = a.fixo            # o soco antigo: nada a dobrar
    alvo.pv = max(0, alvo.pv - max(1, dano))
    if critico and a.dados:
        # O Encaixe. Numa briga "até a primeira queda", Caído encerra;
        # nas outras, Sem Ar é o que mais rende: Vantagem contra ele até a
        # próxima vez de quem socou.
        if termos == "queda":
            alvo.caido = True
            a.encaixes["Caído"] = a.encaixes.get("Caído", 0) + 1
        else:
            alvo.sem_ar_ate = turno + 1
            a.encaixes["Sem Ar"] = a.encaixes.get("Sem Ar", 0) + 1


def acabou(b: Brigao, termos: str) -> bool:
    if termos == "metade":
        return b.pv <= b.pv_max // 2
    if termos == "queda":
        return b.caido or b.pv == 0
    return b.pv == 0


def briga(a: Brigao, b: Brigao, termos: str = "metade", teto: int = 60) -> dict:
    ordem = [a, b] if rola_d20() >= rola_d20() else [b, a]
    turno = 0
    for rodada in range(1, teto + 1):
        for lut in ordem:
            turno += 1
            alvo = b if lut is a else a
            lut.reacao = True
            for _ in range(lut.ataques):
                soco(lut, alvo, turno, termos)
                if acabou(alvo, termos):
                    return {"vencedor": lut.nome, "rodadas": rodada,
                            "comecou": ordem[0].nome, "venceu_quem_comecou": lut is ordem[0]}
    return {"vencedor": None, "rodadas": teto, "comecou": ordem[0].nome,
            "venceu_quem_comecou": False}


def mede(fazer_a, fazer_b, termos="metade", n=N) -> dict:
    vit = rod = ini = teto = 0
    for _ in range(n):
        a, b = fazer_a(), fazer_b()
        a.nome, b.nome = "a", "b"
        r = briga(a, b, termos)
        vit += r["vencedor"] == "a"
        rod += r["rodadas"]
        ini += r["venceu_quem_comecou"]
        teto += r["vencedor"] is None
    return {"vitoria": vit / n, "rodadas": rod / n, "iniciativa": ini / n,
            "sem_fim": teto / n}


# ---------------------------------------------------------------------------
# As medições
# ---------------------------------------------------------------------------

def soco_contra_arma(falhas: list) -> None:
    print("1. O SOCO CONTRA A ARMA — dano médio por acerto")
    print("   Arma com o Grau do item do nível (d8 do Guardião, d10 do Furioso).")
    print(f"{'nível':>6}{'punho':>9}{'classe':>10}{'soco antigo':>13}"
          f"{'soco novo':>11}{'arma':>7}{'novo/arma':>11}")
    print("-" * 67)
    for nivel in NIVEIS:
        dados, bonus = punho(nivel)
        rotulo = f"{dados}d4" + (f"+{bonus}" if bonus else "")
        for classe in ("guardiao", "furioso"):
            f = personagem(BASE[classe](), nivel)
            m = max(f.mods["forca"], f.mods["destreza"])
            antigo = max(1, 1 + f.mods["forca"])
            novo = media_por_acerto(dados, 4, m + bonus)
            _, _, extra, b_item, _ = item_do_nivel(nivel)
            arma = media_por_acerto(1 + extra, DADO_DA_ARMA[classe], f.mods["forca"] + b_item)
            razao = novo / arma
            print(f"{nivel:>6}{rotulo:>9}{classe:>10}{antigo:>13.1f}{novo:>11.1f}"
                  f"{arma:>7.1f}{razao:>11.0%}")
            if not 0.50 <= razao <= 0.80:
                falhas.append(f"nível {nivel}, {classe}: o punho entrega {razao:.0%} "
                              f"da arma, fora de 50% a 80%")
            if novo <= antigo:
                falhas.append(f"nível {nivel}, {classe}: o punho novo não passa do antigo")
    print()


def briga_entre_semideuses(falhas: list) -> None:
    print("2. BRIGA COMBINADA ENTRE SEMIDEUSES DO MESMO NÍVEL")
    print("   Rodadas até o fim, e quanto vence quem começa. 'sem guarda' é o")
    print("   punho novo sem o Bloquear.")
    print(f"{'nível':>6}{'par':>22}{'termos':>9}{'antiga':>8}{'sem guarda':>17}"
          f"{'nova':>15}")
    print(f"{'':>45}{'rod.':>6}{'começa':>9}{'rod.':>6}{'começa':>9}")
    print("-" * 81)
    pares = (("guardiao", "furioso"), ("furioso", "furioso"), ("guardiao", "guardiao"))
    for nivel in NIVEIS:
        for c1, c2 in pares:
            # "Até o nocaute" é a briga longa por escolha: no nível 20 são
            # mais de 200 PV de cada lado.
            for termos, teto in (("metade", 6.0), ("nocaute", 12.0)):
                random.seed(20260926 + nivel)
                antes = mede(lambda: semideus(c1, nivel, "antiga"),
                             lambda: semideus(c2, nivel, "antiga"), termos, n=N // 3)
                sem = mede(lambda: semideus(c1, nivel, "sem guarda"),
                           lambda: semideus(c2, nivel, "sem guarda"), termos)
                nova = mede(lambda: semideus(c1, nivel), lambda: semideus(c2, nivel),
                            termos)
                print(f"{nivel:>6}{c1 + ' x ' + c2:>22}{termos:>9}{antes['rodadas']:>8.1f}"
                      f"{sem['rodadas']:>8.1f}{sem['iniciativa']:>9.0%}"
                      f"{nova['rodadas']:>6.1f}{nova['iniciativa']:>9.0%}")
                if not 1.5 <= nova["rodadas"] <= teto:
                    falhas.append(f"nível {nivel}, {c1} x {c2}, até {termos}: a briga "
                                  f"dura {nova['rodadas']:.1f} rodadas, fora de 1,5 a {teto:.0f}")
                if c1 == c2 and nova["iniciativa"] > 0.75:
                    falhas.append(f"nível {nivel}, {c1} x {c2}, até {termos}: quem "
                                  f"começa vence {nova['iniciativa']:.0%}")
                if c1 != c2 and not 0.20 <= nova["vitoria"] <= 0.80:
                    falhas.append(f"nível {nivel}, {c1} x {c2}, até {termos}: "
                                  f"{nova['vitoria']:.0%}, decidido antes de rolar")
    print()


def a_briga_do_caleb(falhas: list) -> None:
    print("3. A BRIGA DO LOG — Guardião de nível 10 contra um valentão de Kleos 1")
    print("   Até o nocaute do valentão. Com a Força da ficha de teste e com a do")
    print("   David, +0 — que socava por 1.")
    for rotulo, forca in (("ficha de teste", None), ("David, FOR +0", 0)):
        for regra in ("antiga", "nova"):
            random.seed(20260926)
            res = mede(lambda: semideus("guardiao", 10, regra, forca), lambda: valentao(1),
                       termos="nocaute")
            print(f"   {rotulo:<15} regra {regra:<7} vitória {res['vitoria']:.0%} · "
                  f"{res['rodadas']:.1f} rodada(s)")
            if res["vitoria"] < 0.95:
                falhas.append(f"{rotulo}, regra {regra}: o nível 10 perde a briga "
                              f"para um Kleos 1")
            if regra == "nova" and res["rodadas"] > 2.0:
                falhas.append(f"{rotulo}: o nível 10 leva {res['rodadas']:.1f} rodadas "
                              f"para nocautear um Kleos 1")
    print()


def o_critico(falhas: list) -> None:
    print("4. O CRÍTICO DESARMADO")
    print(f"{'nível':>6}{'acerto':>9}{'crítico':>10}{'antes':>8}")
    print("-" * 33)
    for nivel in NIVEIS:
        f = personagem(guardiao_ares(), nivel)
        m = max(f.mods["forca"], f.mods["destreza"])
        dados, bonus = punho(nivel)
        normal = media_por_acerto(dados, 4, m + bonus)
        critico = media_por_acerto(2 * dados, 4, m + bonus)
        antes = max(1, 1 + f.mods["forca"])
        print(f"{nivel:>6}{normal:>9.1f}{critico:>10.1f}{antes:>8.1f}")
        if critico <= normal:
            falhas.append(f"nível {nivel}: o crítico desarmado não soma nada")
    print("   Antes o crítico do soco era igual ao acerto: não havia dado.")
    print()


def livro(falhas: list) -> None:
    print("5. O LIVRO CONTRA O MOTOR")
    texto = LIVRO.read_text(encoding="utf-8")
    m = re.search(r'id="tabela-punho".*?<tbody>(.*?)</tbody>', texto, re.S)
    if not m:
        falhas.append("a tabela do punho sumiu do Livro do Jogador")
    else:
        linhas = re.findall(r"<tr><td[^>]*>(?:<strong>)?(\d+)(?:</strong>)?</td>"
                            r"<td[^>]*>(\d)d4</td><td[^>]*>([^<]+)</td>", m.group(1))
        if len(linhas) != 5:
            falhas.append(f"a tabela do punho tem {len(linhas)} linhas, e não 5")
        for nivel, dados, bonus in linhas:
            esperado = punho(int(nivel))
            no_livro = (int(dados), 0 if bonus.strip() in ("—", "-") else int(bonus.strip("+ ")))
            if no_livro != esperado:
                falhas.append(f"nível {nivel}: o livro diz {no_livro}, o motor usa {esperado}")
        print("  tabela do punho: conferida contra punho()")
    for frase in ("rola os dados duas vezes", "Encaixe", "Sem Ar", "Nocaute",
                  "Briga combinada", "<h4>Desprevenido</h4>", "Bloquear"):
        if frase not in texto:
            falhas.append(f"o Livro do Jogador não diz mais {frase!r}")

    ficha = FICHA.read_text(encoding="utf-8")
    m = re.search(r"var PUNHO = (\[\[.*?\]\]);", ficha)
    if not m:
        falhas.append("a ficha não calcula mais o punho")
    else:
        for nivel, dados, bonus in re.findall(r"\[(\d+), (\d+), (\d+)\]", m.group(1)):
            if (int(dados), int(bonus)) != punho(int(nivel)):
                falhas.append(f"nível {nivel}: a ficha diz {dados}d4 +{bonus}, "
                              f"o motor usa {punho(int(nivel))}")
        print("  punho da ficha: conferido contra punho()")
    print()


def main() -> None:
    falhas = []
    soco_contra_arma(falhas)
    briga_entre_semideuses(falhas)
    a_briga_do_caleb(falhas)
    o_critico(falhas)
    livro(falhas)
    if falhas:
        for f in falhas:
            print("FALHOU:", f)
        raise SystemExit(1)
    print("O punho cresce com o semideus sem alcançar a arma, a briga entre iguais")
    print("acaba em poucas rodadas, e o crítico desarmado tem o que dobrar.")


if __name__ == "__main__":
    main()

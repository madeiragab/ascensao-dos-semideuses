"""O jogo inteiro dentro do motor — a última dívida do simulador.

Até aqui o motor sabia metade do jogo: os heróis batiam com arma e as criaturas
batiam de volta. Faltava tudo que decide um combate de verdade — habilidade,
controle, e as peças de chefe que existem justamente para responder a controle.
Por isso as **Recusas** nunca puderam ser medidas: não havia Rolagem de Efeito
para recusar.

O que este arquivo acrescenta:

  HERÓIS
    · habilidade de dano no Teto de Custo, paga em MP (Oráculo) ou SP (marciais),
      com o crítico do livro: soma dados iguais ao Grau, não dobra;
    · habilidade de controle — condição forte, 4 pontos — resolvida por Rolagem
      de Efeito contra a defesa passiva mais fraca da criatura, com nova rolagem
      no fim do turno do alvo, como manda o Livro I;
    · equipamento no Grau do nível, pela tabela da Forja.

  CRIATURAS
    · Sopro de área com Recarga 5–6 e Arremetidas, já medidos em criaturas.py;
    · Recusas: a criatura transforma um acerto de Efeito em erro, N vezes.

As perguntas que ele responde:
  1. O arsenal dos heróis muda o resultado, ou gastar recurso é decoração?
  2. Quanto vale uma Recusa?
  3. Controle ainda compensa quando o chefe pode recusar?
  4. Com tudo ligado dos dois lados, o encontro justo continua justo?

Rodar de dentro da pasta sim/:
    python completo.py
"""

import random
import sys

from combate import Lutador, rola, rola_d20
from fichas import furioso_ares, guardiao_ares, oraculo_atena
from forja import heroi
from kleos import TABUA, monstro_padrao
from niveis import custo_em_recurso, grau, personagem, teto_de_custo

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

N = 1200
CENARIOS = [(5, 5), (9, 7), (13, 8), (17, 9), (20, 9)]

# Tábua de Kleos, seção 10 — defesa passiva forte e fraca de cada degrau.
DEFESAS = {
    1: (17, 14), 2: (18, 15), 3: (19, 15), 4: (20, 16), 5: (21, 16), 6: (22, 17),
    7: (23, 17), 8: (24, 18), 9: (25, 18), 10: (27, 19), 11: (29, 20),
}

BASE = {"guardiao": guardiao_ares, "furioso": furioso_ares, "oraculo": oraculo_atena}


# ---------------------------------------------------------------------------
# Os heróis, agora com arsenal
# ---------------------------------------------------------------------------

def montar_heroi(classe: str, nivel: int, com_habilidade: bool) -> Lutador:
    """O herói da Forja, mais a habilidade que a classe dele levaria."""
    lut = heroi(classe, nivel, True)
    f = personagem(BASE[classe](), nivel)
    lut.divino = f.mods["inteligencia" if classe == "oraculo" else "sabedoria"]
    lut.bonus_efeito = lut.divino + f.prof
    lut.grau_hab = grau(nivel)
    lut.teto = teto_de_custo(nivel)
    lut.usa_habilidade = com_habilidade
    # O Oráculo controla; os marciais gastam SP num golpe grande.
    lut.papel = "controle" if classe == "oraculo" else "dano"
    lut.custo_dano = custo_em_recurso(nivel, lut.teto)
    lut.custo_controle = custo_em_recurso(nivel, 4)
    lut.recurso = "mp" if classe == "oraculo" else "sp"
    lut.controle_ativo = None
    return lut


def recurso_de(lut) -> int:
    return lut.mp if lut.recurso == "mp" else lut.sp


def gastar(lut, quanto: int) -> None:
    if lut.recurso == "mp":
        lut.mp -= quanto
    else:
        lut.sp -= quanto


def golpe_de_habilidade(lut, alvo) -> int:
    """Ataque de Habilidade. No crítico soma dados iguais ao Grau, não dobra."""
    nat = rola_d20()
    if nat == 1:
        return 0
    critico = nat >= 20
    if not critico and nat + lut.bonus_efeito < alvo.defesa:
        return 0
    dados = lut.teto * lut.grau_hab + (lut.grau_hab if critico else 0)
    dano = sum(rola(8) for _ in range(dados)) + lut.divino
    alvo.receber(dano, lut)
    lut.dano_causado += dano
    return dano


def rolagem_de_efeito(lut, alvo, defesa_passiva: int) -> bool:
    """Efeito contra defesa passiva. Sem crítico: 1 e 20 usam o total.

    Um acerto pode ser anulado por uma Recusa da criatura.
    """
    if rola_d20() + lut.bonus_efeito < defesa_passiva:
        return False
    if getattr(alvo, "recusas", 0) > 0:
        alvo.recusas -= 1
        alvo.recusas_gastas += 1
        return False
    return True


# ---------------------------------------------------------------------------
# O combate com tudo ligado
# ---------------------------------------------------------------------------

def combate_total(herois, monstro, arremetidas=0, sopro=0, defesa_fraca=17):
    todos = herois + [monstro]
    for c in todos:
        c.aliados = herois if c.lado == "herois" else [monstro]
    ordem = sorted(todos, key=lambda c: rola_d20() + c.iniciativa_bonus, reverse=True)
    sopro_pronto = True

    for rodada in range(1, 41):
        restantes = arremetidas
        for lutador in ordem:
            if not lutador.vivo:
                continue

            # ---- o turno da criatura
            if lutador is monstro:
                if monstro.perde_o_turno:
                    monstro.resolver_fim_de_turno()
                else:
                    if sopro and not sopro_pronto and rola(6) >= 5:
                        sopro_pronto = True
                    if sopro and sopro_pronto:
                        sopro_pronto = False
                        for h in herois:
                            if h.vivo:
                                passou = rola_d20() + h.prof >= 8 + monstro.bonus_ataque
                                h.receber(sopro // 2 if passou else sopro, monstro)
                    else:
                        monstro.turno([monstro], herois)
                # fim do turno do alvo: a condição pede nova rolagem da fonte
                for h in herois:
                    if h.vivo and h.controle_ativo is monstro:
                        if not rolagem_de_efeito(h, monstro, defesa_fraca):
                            monstro.condicoes.pop("perde_turno", None)
                            h.controle_ativo = None
                if not any(h.vivo for h in herois):
                    break
                continue

            # ---- o turno de um herói
            agiu = False
            if lutador.usa_habilidade and monstro.vivo:
                if (lutador.papel == "controle"
                        and recurso_de(lutador) >= lutador.custo_controle
                        and not monstro.perde_o_turno):
                    gastar(lutador, lutador.custo_controle)
                    if rolagem_de_efeito(lutador, monstro, defesa_fraca):
                        monstro.aplicar_condicao("perde_turno", 1)
                        lutador.controle_ativo = monstro
                    agiu = True
                elif (lutador.papel == "dano"
                      and recurso_de(lutador) >= lutador.custo_dano):
                    gastar(lutador, lutador.custo_dano)
                    golpe_de_habilidade(lutador, monstro)
                    agiu = True
            if not agiu:
                lutador.turno(herois, [monstro])

            # ---- Arremetida ao fim do turno de outra criatura
            if (restantes > 0 and monstro.vivo and not monstro.perde_o_turno
                    and any(h.vivo for h in herois)):
                restantes -= 1
                monstro.atacar(max((h for h in herois if h.vivo), key=lambda h: h.pv))

            if not any(h.vivo for h in herois) or not monstro.vivo:
                break

        if not any(h.vivo for h in herois) or not monstro.vivo:
            return {"vencedor": "herois" if any(h.vivo for h in herois) else "monstros",
                    "rodadas": rodada,
                    "de_pe": sum(1 for h in herois if h.vivo),
                    "recusas_gastas": monstro.recusas_gastas}

    return {"vencedor": "tempo", "rodadas": 40,
            "de_pe": sum(1 for h in herois if h.vivo),
            "recusas_gastas": monstro.recusas_gastas}


def mede(nivel, k, recusas=0, com_habilidade=True, completo=True, n=N) -> dict:
    fraca = DEFESAS[k][1]
    arr = (2 if k >= 8 else 1) if completo else 0
    sopro = TABUA[k][3] if completo else 0
    v = r = pe = rec = 0
    for _ in range(n):
        herois = [montar_heroi(c, nivel, com_habilidade)
                  for c in ("guardiao", "furioso", "oraculo")]
        m = Lutador.de_monstro(monstro_padrao(k))
        m.recusas, m.recusas_gastas = recusas, 0
        res = combate_total(herois, m, arr, sopro, fraca)
        v += res["vencedor"] == "herois"
        r += res["rodadas"]
        pe += res["de_pe"]
        rec += res["recusas_gastas"]
    return {"vitoria": v / n, "rodadas": r / n, "de_pe": pe / n, "recusas": rec / n}


def main() -> None:
    random.seed(20260818)
    falhas = []

    print("1. O QUE O ARSENAL DOS HERÓIS MUDA")
    print("   criatura completa, com Sopro e Arremetidas, e sem Recusa")
    print(f"{'nível':>6}{'Kleos':>7}{'só arma':>10}{'com habilidade':>16}"
          f"{'rodadas':>9}{'de pé':>8}")
    print("-" * 58)
    for nivel, k in CENARIOS:
        so_arma = mede(nivel, k, com_habilidade=False)
        com = mede(nivel, k, com_habilidade=True)
        print(f"{nivel:>6}{k:>7}{so_arma['vitoria']:>10.0%}{com['vitoria']:>16.0%}"
              f"{com['rodadas']:>9.1f}{com['de_pe']:>8.1f}")
        if com["vitoria"] + 0.02 < so_arma["vitoria"]:
            falhas.append(f"nível {nivel}: gastar recurso piorou o grupo")

    print("\n2. QUANTO VALE UMA RECUSA")
    print(f"{'nível':>6}{'Kleos':>7}{'0 Recusas':>12}{'1':>8}{'2':>8}{'3':>8}"
          f"{'gastas com 3':>14}")
    print("-" * 66)
    for nivel, k in CENARIOS:
        taxas, tres = [], None
        for r in (0, 1, 2, 3):
            res = mede(nivel, k, recusas=r)
            taxas.append(res["vitoria"])
            if r == 3:
                tres = res
        print(f"{nivel:>6}{k:>7}{taxas[0]:>12.0%}{taxas[1]:>8.0%}"
              f"{taxas[2]:>8.0%}{taxas[3]:>8.0%}{tres['recusas']:>14.1f}")
        if taxas[3] > taxas[0] + 0.05:
            falhas.append(f"nível {nivel}: Recusa deixou a criatura mais fraca")

    print("\n3. CONTROLE COMPENSA CONTRA UM CHEFE QUE RECUSA?")
    print("   Oráculo gastando MP em condição forte, contra 2 Recusas")
    print(f"{'nível':>6}{'Kleos':>7}{'sem arsenal':>13}{'com arsenal':>13}{'ganho':>8}")
    print("-" * 47)
    for nivel, k in CENARIOS:
        sem = mede(nivel, k, recusas=2, com_habilidade=False)
        com = mede(nivel, k, recusas=2, com_habilidade=True)
        print(f"{nivel:>6}{k:>7}{sem['vitoria']:>13.0%}{com['vitoria']:>13.0%}"
              f"{com['vitoria'] - sem['vitoria']:>+8.0%}")

    print("\n4. O ENCONTRO JUSTO, COM TUDO LIGADO DOS DOIS LADOS")
    print("   criatura com Sopro, Arremetidas e 2 Recusas · heróis com item e habilidade")
    print(f"{'nível':>6}{'Kleos':>7}{'vitórias':>10}{'rodadas':>9}{'de pé de 3':>12}")
    print("-" * 46)
    for nivel, k in CENARIOS:
        res = mede(nivel, k, recusas=2)
        print(f"{nivel:>6}{k:>7}{res['vitoria']:>10.0%}{res['rodadas']:>9.1f}"
              f"{res['de_pe']:>12.1f}")
        if not 0.40 <= res["vitoria"] <= 0.95:
            falhas.append(f"nível {nivel}: encontro justo com tudo ligado deu "
                          f"{res['vitoria']:.0%} de vitória, fora de 40% a 95%")
        if res["rodadas"] > 6.5:
            falhas.append(f"nível {nivel}: {res['rodadas']:.1f} rodadas, longo demais")

    print()
    if falhas:
        for f in falhas:
            print("FALHOU:", f)
        raise SystemExit(1)
    print("O motor joga o jogo inteiro: habilidade, controle, Sopro, Arremetida")
    print("e Recusa. Nenhuma peça do sistema ficou sem medição.")


if __name__ == "__main__":
    main()

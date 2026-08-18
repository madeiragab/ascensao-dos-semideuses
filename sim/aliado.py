"""O Aliado que luta — quanto ele pode ser sem virar um jogador.

O Guia mandava construir todo NPC de combate pelo motor do Bestiário. Funciona
para inimigos e falha para companheiros: um aliado montado no Kleos que um herói
"vale" morre rápido demais para acompanhar a campanha, e o playtest de mesa
tropeçou exatamente nisso.

O alvo, dito pelo autor: **mais fraco que um personagem de jogador, mais forte
que o bloco de hoje.** Este arquivo mede três desenhos contra esse alvo.

  hoje       bloco do Kleos que um herói vale — Kleos 1 nos níveis 1–4, 2 nos
             5–8, e assim por diante. É o desenho que a mesa reprovou.
  couro      a linha do Kleos do GRUPO para PV e DEF: vira um tanque de 155 PV
             no nível 9, quase o dobro do Guardião. Reprovado por medição.
  parceiro   a linha do Kleos do GRUPO MENOS 2, inteira — a mesma trava da Fera
             Vinculada. É a regra que o Guia do Mestre passou a trazer.

Três medidas decidem: quanto o aliado sobrevive, quanto ele soma à vitória do
grupo, e que fatia do dano ele tira dos jogadores.

Rodar de dentro da pasta sim/:
    python aliado.py
"""

import random
import sys

from combate import Lutador, rola_d20
from completo import DEFESAS, combate_total, montar_heroi
from kleos import TABUA, monstro_padrao
from niveis import kleos_do_grupo, kleos_do_personagem

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

N = 1000
CENARIOS = [(5, 5), (9, 7), (13, 8), (17, 9)]


def bloco(pv_de: int, dano_de: int) -> Lutador:
    """Um aliado com o couro de um degrau e o soco de outro."""
    pv, defe = TABUA[pv_de][0], TABUA[pv_de][1]
    _, _, atk, dano, n_ataques = TABUA[dano_de]
    a = Lutador(
        nome="aliado", lado="herois", pv_max=pv, defesa=defe,
        bonus_ataque=atk, dados_dano=[8],
        dano_fixo=max(0, round(dano / max(1, n_ataques) - 4.5)),
        iniciativa_bonus=2, prof=2, regras="v1",
    )
    a.usa_habilidade = False
    a.papel = "dano"
    a.recurso = "sp"
    a.controle_ativo = None
    a.custo_dano = a.custo_controle = 10 ** 6
    return a


def desenho(nome: str, nivel: int, k_grupo: int):
    """Devolve a função que monta o aliado daquele desenho."""
    if nome == "hoje":
        k = max(1, round(kleos_do_personagem(nivel)))
        return lambda k=k: bloco(k, k)
    if nome == "couro":
        return lambda: bloco(k_grupo, max(1, k_grupo - 2))
    if nome == "parceiro":
        k = max(1, k_grupo - 2)
        return lambda k=k: bloco(k, k)
    raise ValueError(nome)


def mede(nivel, k, monta_aliado=None, n=N) -> dict:
    fraca = DEFESAS[k][1]
    arr = 2 if k >= 8 else 1
    sopro = TABUA[k][3]
    vit = de_pe = aliado_vivo = dano_aliado = dano_total = 0
    for _ in range(n):
        herois = [montar_heroi(c, nivel, True)
                  for c in ("guardiao", "furioso", "oraculo")]
        aliado = None
        if monta_aliado:
            aliado = monta_aliado()
            herois.append(aliado)
        m = Lutador.de_monstro(monstro_padrao(k))
        m.recusas, m.recusas_gastas = 2, 0
        res = combate_total(herois, m, arr, sopro, fraca)
        vit += res["vencedor"] == "herois"
        de_pe += sum(1 for h in herois[:3] if h.vivo)
        if aliado is not None:
            aliado_vivo += aliado.vivo
            dano_aliado += aliado.dano_causado
        dano_total += sum(h.dano_causado for h in herois)
    return {
        "vitoria": vit / n,
        "de_pe": de_pe / n,
        "aliado_vivo": aliado_vivo / n if monta_aliado else 0.0,
        "fatia": dano_aliado / dano_total if dano_total else 0.0,
    }


def main() -> None:
    random.seed(20260818)
    falhas = []

    print("O ALIADO CONTRA O ALVO: mais fraco que um jogador, mais forte que hoje")
    print("Trio com equipamento e habilidade, chefe completo com 2 Recusas.")
    print()
    print(f"{'nível':>6}{'Kleos':>7}{'desenho':>9}{'vitória':>9}"
          f"{'aliado sobrevive':>18}{'fatia do dano':>15}{'heróis de pé':>14}")
    print("-" * 78)
    for nivel, k in CENARIOS:
        base = mede(nivel, k)
        print(f"{nivel:>6}{k:>7}{'sem aliado':>9}{base['vitoria']:>9.0%}"
              f"{'—':>18}{'—':>15}{base['de_pe']:>14.1f}")
        for nome in ("hoje", "couro", "parceiro"):
            r = mede(nivel, k, desenho(nome, nivel, k))
            print(f"{'':>6}{'':>7}{nome:>9}{r['vitoria']:>9.0%}"
                  f"{r['aliado_vivo']:>18.0%}{r['fatia']:>15.0%}{r['de_pe']:>14.1f}")
            if nome == "parceiro":
                # O alvo, em três números: sobrevive como gente, bate como
                # coadjuvante, e não decide a luta.
                if r["aliado_vivo"] < 0.50:
                    falhas.append(f"nível {nivel}: o Aliado sobrevive só "
                                  f"{r['aliado_vivo']:.0%} — morre fácil demais")
                if r["fatia"] > 0.20:
                    falhas.append(f"nível {nivel}: o Aliado tira {r['fatia']:.0%} "
                                  f"do dano do grupo — está virando jogador")
                if r["vitoria"] - base["vitoria"] > 0.15:
                    falhas.append(f"nível {nivel}: o Aliado soma "
                                  f"{r['vitoria']-base['vitoria']:+.0%} de vitória")
        print()

    print("Leitura: 'hoje' morre em toda luta — 6% de sobrevivência no nível 9.")
    print("'couro' vira tanque de monstro. 'parceiro', a linha do Kleos do grupo")
    print("menos 2, sobrevive como gente e bate como coadjuvante: é a regra nova.")

    if falhas:
        print()
        for f in falhas:
            print("FALHOU:", f)
        raise SystemExit(1)


if __name__ == "__main__":
    main()

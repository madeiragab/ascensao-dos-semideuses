"""Auditoria de equilíbrio do sistema inteiro.

Cobre o que os outros arquivos não cobriam:

  1. A escala de Kleos, refeita depois do conserto do Ataque Extra
  2. Paridade entre as três classes, em quatro níveis
  3. As 27 armas: alguma domina?
  4. As armaduras: o degrau vale o preço?
  5. As técnicas de Tier 2 e 3: alguma é obrigatória ou morta?

Rodar de dentro da pasta sim/:
    python equilibrio.py
"""

import random
import sys

from combate import Lutador, combate
from dados import Ataque, chance_de_acertar
from fichas import Monstro
from fichas_v1 import ARMADURAS, def_com_armadura, furioso_v1, guardiao_v1, oraculo_v1
from kleos import TABUA
from niveis import ataques_por_turno, personagem, proficiencia, teto_de_custo
from calibrar_kleos import OraculoQueJoga, monstro

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

N = 4000
NIVEIS = (1, 5, 10, 20)


def titulo(n: str, t: str) -> None:
    print()
    print("=" * 78)
    print(f"{n}. {t}")
    print("=" * 78)


# ---------------------------------------------------------------------------
def montar_grupo(nivel: int, tecnicas_extra=None, classe_alvo=None):
    """O trio no nível pedido. tecnicas_extra entra só na classe_alvo."""
    def f():
        saida = []
        for base in (guardiao_v1(), furioso_v1(), oraculo_v1()):
            fic = personagem(base, nivel)
            extras = list(tecnicas_extra or []) if fic.classe == classe_alvo else []
            crit = 19 if "Coração de Ares" in extras else 20
            if fic.classe == "oraculo":
                lut = OraculoQueJoga(
                    nome=fic.nome, lado="herois", pv_max=fic.pv_max, defesa=fic.defesa,
                    bonus_ataque=fic.bonus_ataque, dados_dano=list(fic.dados_arma),
                    dano_fixo=fic.dano_fixo, iniciativa_bonus=fic.iniciativa_bonus,
                    prof=fic.prof, sp_max=fic.sp_max, mp_max=fic.mp_max,
                    classe="oraculo", mod_sabedoria=fic.mods["sabedoria"],
                    tecnicas=list(fic.tecnicas) + extras, regras="v1", nivel=nivel,
                    mod_divino=fic.mods["inteligencia"], teto=teto_de_custo(nivel),
                    critico_em=crit,
                )
            else:
                lut = Lutador.de_ficha(fic, regras="v1", critico_em=crit)
                lut.tecnicas = list(fic.tecnicas) + extras
            lut.ataques_por_turno = ataques_por_turno(fic.classe, nivel)
            saida.append(lut)
        return saida
    return f


def rodar(nivel: int, k: int, tecnicas=None, classe=None, n: int = N) -> dict:
    random.seed(777)
    v = rod = pe = 0
    dano = {}
    for _ in range(n):
        grupo = montar_grupo(nivel, tecnicas, classe)()
        r = combate(grupo, [Lutador.de_monstro(monstro(k))])
        v += r["vencedor"] == "herois"
        rod += r["rodadas"]
        pe += r["herois_vivos"]
        for nome, d in r["dano"].items():
            dano[nome] = dano.get(nome, 0) + d
    return {"vitoria": v / n, "rodadas": rod / n, "de_pe": pe / n,
            "dano": {kk: vv / n for kk, vv in dano.items()}}


# ===========================================================================
def t1_kleos_refeito() -> None:
    titulo(1, "A escala de Kleos, refeita com Ataque Extra funcionando")
    print("O motor ignorava ataques_por_turno no turno do Furioso: ele nunca usou")
    print("Ataque Extra em nenhuma calibragem anterior. Consertado, o grupo ficou")
    print("mais forte, e o Kleos justo tem que subir.\n")
    print(f"{'nível':>6} | " + "".join(f"{'K'+str(k):>7}" for k in range(1, 12))
          + "   justo")
    print("-" * 78)
    resultado = {}
    for nv in NIVEIS:
        linha, cruzou, ant = [], None, 1.0
        for k in range(1, 12):
            v = rodar(nv, k, n=1200)["vitoria"]
            linha.append(f"{v:>6.0%} ")
            if cruzou is None and v < 0.80:
                cruzou = (k - 1) + (ant - 0.80) / max(ant - v, 1e-9) if k > 1 else 1.0
            ant = v
        resultado[nv] = cruzou or 11.0
        print(f"{nv:>6} | " + "".join(linha) + f"  K{resultado[nv]:.1f}")

    print(f"\n{'nível':>6} {'justo agora':>12} {'no livro hoje':>14} {'por personagem':>15}")
    print("-" * 78)
    no_livro = {1: 3, 5: 5, 10: 7, 20: 9}
    for nv, k in resultado.items():
        print(f"{nv:>6} {k:>12.1f} {no_livro[nv]:>14} {k/3:>15.2f}")
    return resultado


# ===========================================================================
def t2_paridade_de_classe() -> None:
    titulo(2, "As três classes puxam o mesmo peso?")
    print("Fatia do dano do grupo, e quantas vezes cada uma termina de pé.\n")
    for nv in NIVEIS:
        k = {1: 3, 5: 6, 10: 8, 20: 10}[nv]
        r = rodar(nv, k)
        d = r["dano"]
        total = sum(v for kk, v in d.items() if kk in ("Guardião", "Furioso", "Oráculo"))
        print(f"  nível {nv:>2} contra Kleos {k}  ·  vitórias {r['vitoria']:.0%}")
        for nome in ("Guardião", "Furioso", "Oráculo"):
            fatia = d.get(nome, 0) / total if total else 0
            barra = "█" * round(fatia * 34)
            print(f"     {nome:<9} {d.get(nome,0):>7.0f} de dano  {fatia:>5.0%} {barra}")
        print()
    print("  Um sistema saudável não precisa de fatias iguais — o Furioso deve")
    print("  liderar. O sinal ruim seria alguém irrelevante, abaixo de ~10%.")


# ===========================================================================
def t3_armas() -> None:
    titulo(3, "Alguma arma domina a tabela?")
    print("Dano esperado por rodada contra DEF 14, com o atributo em +3 e")
    print("proficiência +2. Duas colunas: um ataque (nível 1) e dois (nível 5+).\n")

    # nome, dados, brutal, versatil_2m, duas_maos, obs
    armas = [
        ("Adaga",              [4],  False, None, "simples · Fineza, Leve, Arremesso"),
        ("Clava",              [6],  False, None, "simples"),
        ("Bastão",             [6],  False, [8],  "simples · Versátil"),
        ("Lança",              [6],  False, [8],  "simples · Arremesso, Versátil"),
        ("Porrete grande",     [8],  False, None, "simples · Duas Mãos"),
        ("Espada curta",       [6],  False, None, "marcial · Fineza, Leve"),
        ("Sabre defensivo",    [6],  False, None, "marcial · Fineza, +1 DEF"),
        ("Espada longa",       [8],  False, [10], "marcial · Versátil"),
        ("Machado de batalha", [8],  False, [10], "marcial · Versátil"),
        ("Rapieira",           [8],  False, None, "marcial · Fineza"),
        ("Maça pesada",        [8],  False, None, "marcial · Demolidora"),
        ("Tridente",           [8],  False, [10], "marcial · Arremesso, Versátil"),
        ("Lança longa",        [10], False, None, "marcial · Alcance, Duas Mãos"),
        ("Glaive",             [10], False, None, "marcial · Alcance, Pesada"),
        ("Machado grande",     [10], True,  None, "marcial · Pesada, BRUTAL"),
        ("Arco curto",         [6],  False, None, "simples · à distância"),
        ("Besta leve",         [8],  False, None, "simples · Recarga: 1 tiro por ação"),
        ("Arco longo",         [8],  False, None, "marcial · à distância"),
        ("Besta pesada",       [10], False, None, "marcial · Recarga: 1 tiro por ação"),
    ]
    print(f"{'arma':<19} {'1 ataque':>9} {'2 ataques':>10}  observação")
    print("-" * 78)
    linhas = []
    for nome, dados, brutal, duas, obs in armas:
        d = duas or dados
        um = Ataque(nome, 5, d, 3, brutal=brutal).dano_esperado(14)
        recarga = "Recarga" in obs
        dois = um if recarga else um * 2
        linhas.append((dois, um, nome, obs, recarga))
    for dois, um, nome, obs, recarga in sorted(linhas, reverse=True):
        marca = "  ← trava em 1 tiro" if recarga else ""
        print(f"{nome:<19} {um:>9.2f} {dois:>10.2f}  {obs}{marca}")

    print("\n  A coluna de dois ataques é a que importa a partir do nível 5. Repare")
    print("  onde a Besta pesada cai: de melhor arma do jogo para pior escolha")
    print("  marcial, exatamente como o Capítulo Quatro promete.")


# ===========================================================================
def t4_armaduras() -> None:
    titulo(4, "O degrau de armadura vale o preço?")
    print("Dano recebido por rodada de um atacante de Kleos 3 (+5, 2× 1d8+3),")
    print("com Destreza +1 e +3, e o preço em dracmas.\n")
    precos = {"0": 0, "acolchoada": 5, "couro_batido": 45, "escamas": 50, "peitoral": 400}
    nomes = {"0": "Sem armadura", "acolchoada": "Acolchoada",
             "couro_batido": "Couro batido", "escamas": "Cota de escamas",
             "peitoral": "Peitoral"}
    for escudo in (False, True):
        print(f"  {'com escudo (+2)' if escudo else 'sem escudo'}")
        print(f"     {'armadura':<16} {'DEF (DES+1)':>12} {'dano/rod':>9} "
              f"{'DEF (DES+3)':>12} {'dano/rod':>9} {'preço':>7}")
        anterior = None
        for chave in ("0", "acolchoada", "couro_batido", "escamas", "peitoral"):
            d1 = def_com_armadura(1, None if chave == "0" else chave, escudo)
            d3 = def_com_armadura(3, None if chave == "0" else chave, escudo)
            dano1 = 2 * Ataque("m", 5, [8], 3).dano_esperado(d1)
            dano3 = 2 * Ataque("m", 5, [8], 3).dano_esperado(d3)
            ganho = f"  −{anterior - dano1:.1f}" if anterior is not None else ""
            print(f"     {nomes[chave]:<16} {d1:>12} {dano1:>9.2f}{ganho:<7}"
                  f"{d3:>12} {dano3:>9.2f} {precos[chave]:>7}")
            anterior = dano1
        print()
    print("  O Peitoral custa 8× a Cota de escamas e compra 1 ponto de DEF. É caro")
    print("  de propósito, mas a diferença é pequena o bastante para a Cota ser a")
    print("  compra certa por muito tempo.")


# ===========================================================================
def t5_tecnicas() -> None:
    titulo(5, "As técnicas de Tier 2 e 3: alguma é obrigatória ou morta?")
    print("A/B no nível 12, onde os três tiers estão abertos. Cada linha é o")
    print(f"grupo com aquela técnica a mais, contra Kleos 8. {N} combates.\n")

    base = rodar(12, 8)
    print(f"  referência, sem técnica extra: {base['vitoria']:.1%} de vitórias\n")
    print(f"{'técnica':<22} {'classe':<10} {'vitórias':>9} {'delta':>8}  veredito")
    print("-" * 78)

    testes = [
        ("Coração de Ares",  "furioso",  "crítico em 19 e 20"),
        ("Massacre",         "furioso",  "ataque livre a cada abate"),
        ("Fúria Crescente",  "furioso",  "+1/rodada até +3, no 1º ataque do turno"),
        ("Golpe Duplo",      "furioso",  "1×/combate, sem modificador no dano"),
        ("Casca Grossa",     "furioso",  "+2 DEF abaixo de metade dos PV"),
        ("Bastião",          "guardiao", "−proficiência em cada golpe recebido"),
        ("Casca Grossa",     "guardiao", "+2 DEF abaixo de metade dos PV"),
    ]
    for tec, classe, obs in testes:
        r = rodar(12, 8, [tec], classe)
        delta = r["vitoria"] - base["vitoria"]
        if delta >= 0.10:
            v = "FORTE DEMAIS"
        elif delta <= 0.01:
            v = "sem efeito aqui"
        else:
            v = "ok"
        print(f"{tec:<22} {classe:<10} {r['vitoria']:>8.1%} {delta:>+8.1%}  {v}  · {obs}")

    print("\n  Uma técnica saudável muda a vitória em alguns pontos. Acima de dez")
    print("  ela vira escolha obrigatória; perto de zero, ninguém escolhe.")

    # Chefe solo não é o mundo inteiro: técnicas de encadear só aparecem
    # contra bando, e julgá-las só pelo chefe daria um veredito falso.
    print("\n  Contra CINCO inimigos de Kleos 4, em vez de um chefe:")
    random.seed(777)
    def contra_bando(tec):
        random.seed(777)
        v = 0
        for _ in range(N):
            g = montar_grupo(12, [tec] if tec else None, "furioso")()
            alvos = [Lutador.de_monstro(monstro(4), f" {i}") for i in range(1, 6)]
            v += combate(g, alvos)["vencedor"] == "herois"
        return v / N

    b = contra_bando(None)
    print(f"     {'referência':<22} {b:>8.1%}")
    for tec in ("Massacre", "Golpe Duplo", "Fúria Crescente"):
        r = contra_bando(tec)
        print(f"     {tec:<22} {r:>8.1%} {r - b:>+8.1%}")
    print("\n  Massacre não é fraca: é situacional. Zero contra um chefe, e das")
    print("  melhores contra um bando. Isso é desenho, não defeito.")


if __name__ == "__main__":
    t1_kleos_refeito()
    t2_paridade_de_classe()
    t3_armas()
    t4_armaduras()
    t5_tecnicas()
    print()

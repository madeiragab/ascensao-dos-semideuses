"""Mede TODAS as técnicas de classe, uma a uma.

Cada linha é o mesmo grupo com aquela técnica a mais. O que importa é o delta
de vitória, em dois cenários que medem coisas diferentes:

  CHEFE   um monstro forte sozinho  — mede dano por rodada e sobrevivência
  BANDO   cinco monstros médios     — mede encadeamento e efeitos em área

Uma técnica saudável muda a vitória em alguns pontos em pelo menos um dos dois.
Acima de dez pontos ela vira escolha obrigatória; perto de zero nos dois,
ninguém escolhe.

Rodar de dentro da pasta sim/:
    python tecnicas.py
"""

import random
import sys

from calibrar_kleos import monstro
from combate import Lutador, combate
from equilibrio import montar_grupo

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

N = 1500
NIVEL = 12

# nome, classe, o que o motor consegue medir (ou None se não consegue)
TECNICAS = [
    # ---- Guardião
    ("Postura Desafiadora", "guardiao", "marca: o inimigo ataca com Desvantagem"),
    ("Escudo Vínculo",      "guardiao", "reação, 2 SP, +proficiência na DEF"),
    ("Vigor do Sobrevivente","guardiao", "PV máximos +nível"),
    ("Interceptar",         "guardiao", "assume o golpe que derrubaria um aliado"),
    ("Pé Firme",            "guardiao", None),
    ("Muro de Escudos",     "guardiao", "+1 DEF nos aliados"),
    ("Represália",          "guardiao", "dano de volta ao interceptar"),
    ("Provocação Ampla",    "guardiao", "marca dois inimigos"),
    ("Fôlego de Ferro",     "guardiao", "recupera SP uma vez por combate"),
    ("Bastião",             "guardiao", "−proficiência no primeiro golpe da rodada"),
    ("Segunda Muralha",     "guardiao", "Interceptar de graça uma vez por rodada"),
    ("Juramento do Portão", "guardiao", "o jurado não cai por um golpe só"),
    # ---- Furioso
    ("Ataque Pesado",       "furioso",  "−2 e um dado a mais"),
    ("Investida Imprudente","furioso",  None),
    ("Grito de Batalha",    "furioso",  None),
    ("Sede de Sangue",      "furioso",  "SP ao abater"),
    ("Casca Grossa",        "furioso",  "+2 DEF abaixo da metade dos PV"),
    ("Fúria Crescente",     "furioso",  "+1/rodada até +3, no 1º ataque"),
    ("Golpe Duplo",         "furioso",  "1×/combate, sem modificador no dano"),
    ("Sem Recuo",           "furioso",  None),
    ("Rasgo",               "furioso",  "Sangrando 1 no Ataque Pesado"),
    ("Massacre",            "furioso",  "ataque livre a cada abate"),
    ("Fúria Cega",          "furioso",  "1×/combate, um ataque em cada inimigo"),
    ("Coração de Ares",     "furioso",  "crítico em 19 e 20"),
    # ---- Oráculo
    ("Palavra Curativa",    "oraculo",  "cura 1d6+SAB como ação bônus"),
    ("Bênção da Coragem",   "oraculo",  "+1d4 nos ataques de um aliado"),
    ("Visão do Infortúnio", "oraculo",  "Desvantagem no próximo ataque do inimigo"),
    ("Presságio",           "oraculo",  None),
    ("Mão Firme",           "oraculo",  None),
    ("Escudo do Destino",   "oraculo",  None),
    ("Cura em Cadeia",      "oraculo",  "Palavra Curativa pega dois alvos"),
    ("Voz Serena",          "oraculo",  None),
    ("Fio Cortado",         "oraculo",  None),
    ("Rede do Destino",     "oraculo",  "1×/combate, Vantagem para todo o grupo"),
    ("Fonte Profunda",      "oraculo",  None),
    ("Olho do Futuro",      "oraculo",  "1×/combate, um turno inteiro a mais"),
]


def cenario_chefe():
    return [Lutador.de_monstro(monstro(8))]


def cenario_bando():
    return [Lutador.de_monstro(monstro(4), f" {i}") for i in range(1, 6)]


# Técnicas que só funcionam junto de outra. Medidas como o par inteiro contra
# a base sozinha, senão o resultado é sempre zero e o veredito, mentira.
DEPENDE = {
    "Represália":      ["Interceptar"],
    "Segunda Muralha": ["Interceptar"],
    "Cura em Cadeia":  ["Palavra Curativa"],
}


def medir(tecnicas, classe, cenario, n=N):
    """tecnicas é a lista COMPLETA da classe — o baseline é lista vazia."""
    random.seed(4242)
    v = 0
    for _ in range(n):
        grupo = montar_grupo(NIVEL, tecnicas, classe, substituir=True)()
        if tecnicas and "Vigor do Sobrevivente" in tecnicas:
            for g in grupo:
                if g.classe == classe:
                    g.pv_max += NIVEL
                    g.pv = g.pv_max
        v += combate(grupo, cenario())["vencedor"] == "herois"
    return v / n


# Dívida conhecida. Quando este teste passou a falhar, quatro técnicas já
# estavam fora da faixa — não são regressão, são débito que ninguém tinha visto
# porque o arquivo só imprimia o aviso e saía com sucesso. Elas não bloqueiam a
# regressão, mas aparecem em todo run até serem ajustadas.
#
# Tirar nome daqui é o objetivo. Acrescentar exige decisão de design, não é
# jeito de fazer o teste passar.
DIVIDA_CONHECIDA = {
    "Escudo Vínculo",     # bando +12,1%
    "Interceptar",        # bando +11,2%
    "Rede do Destino",    # bando +13,0%
    "Olho do Futuro",     # chefe +11,3% · bando +12,8%
}


def veredito(dc, db):
    melhor = max(dc, db)
    if melhor >= 0.10:
        return "FORTE DEMAIS"
    if melhor <= 0.01:
        return "sem efeito medido"
    return "ok"


def main():
    print("=" * 78)
    print(f"TODAS AS TÉCNICAS — nível {NIVEL}, {N} combates por célula")
    print("=" * 78)

    bases = {}
    for cl in ("guardiao", "furioso", "oraculo"):
        bases[cl] = (medir([], cl, cenario_chefe), medir([], cl, cenario_bando))
    base_chefe, base_bando = bases["furioso"]
    print(f"\nreferência sem técnica extra:  chefe {base_chefe:.1%} · "
          f"bando {base_bando:.1%}\n")

    print(f"{'técnica':<22} {'classe':<9} {'chefe':>7} {'bando':>7}  veredito")
    print("-" * 78)

    nao_medidas = []
    fortes_demais = []
    for nome, classe, oquemede in TECNICAS:
        if oquemede is None:
            nao_medidas.append((nome, classe))
            continue
        pre = DEPENDE.get(nome, [])
        bc, bb = (bases[classe] if not pre
                  else (medir(pre, classe, cenario_chefe),
                        medir(pre, classe, cenario_bando)))
        conjunto = pre + [nome]
        dc = medir(conjunto, classe, cenario_chefe) - bc
        db = medir(conjunto, classe, cenario_bando) - bb
        v = veredito(dc, db)
        if v == "FORTE DEMAIS":
            fortes_demais.append((nome, classe, dc, db))
        print(f"{nome:<22} {classe:<9} {dc:>+7.1%} {db:>+7.1%}  "
              f"{v}  · {oquemede}")

    print("\n" + "-" * 78)
    print("NÃO MEDIDAS — o motor não representa o efeito, e dizer que são fracas")
    print("seria mentira. Precisam de mesa, não de simulador:")
    for nome, classe in nao_medidas:
        print(f"  {nome:<22} {classe}")

    # Ate 0.16.3 este arquivo imprimia "FORTE DEMAIS" e saia com sucesso, entao
    # a regressao ficava verde com tecnicas fora da faixa e ninguem lia o aviso.
    # Bastiao (+10,7%) e Provocacao Ampla (+25,1%) passaram meses assim.
    print()
    print("-" * 78)
    novas = [t for t in fortes_demais if t[0] not in DIVIDA_CONHECIDA]
    antigas = [t for t in fortes_demais if t[0] in DIVIDA_CONHECIDA]

    if antigas:
        print("DÍVIDA CONHECIDA — fora da faixa desde antes deste teste falhar:")
        for nome, classe, dc, db in antigas:
            print(f"  {nome:<22} {classe:<9} chefe {dc:+.1%} · bando {db:+.1%}")
        print("  (não bloqueiam a regressão; esperam decisão de design)")

    if novas:
        print()
        print("FORA DA FAIXA — acima de 10 pontos a técnica vira escolha obrigatória:")
        for nome, classe, dc, db in novas:
            print(f"  {nome:<22} {classe:<9} chefe {dc:+.1%} · bando {db:+.1%}")
        raise SystemExit(1)

    curadas = sorted(DIVIDA_CONHECIDA - {t[0] for t in fortes_demais})
    if curadas:
        print()
        print("Saíram da faixa e podem sair da DIVIDA_CONHECIDA: " + ", ".join(curadas))
    if not antigas and not novas:
        print("Nenhuma técnica passa de 10 pontos de vitória em nenhum dos dois cenários.")


if __name__ == "__main__":
    main()

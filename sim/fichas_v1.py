"""Fichas da PROPOSTA v1 — os números que estou sugerindo trocar.

Mudanças em relação ao livro v0:

1. Recursos de nível 1 redistribuídos, com total igual (32) para as três
   classes, e o Guardião finalmente sendo o mais resistente:
       Guardião  PV 14 + CON | SP 12 + CON | MP  6 + DIV
       Furioso   PV 12 + CON | SP 14 + CON | MP  6 + DIV
       Oráculo   PV 10 + CON | SP  8 + CON | MP 14 + DIV
2. MP usa o Atributo Divino (INT, SAB ou CAR, seção 4.2), não INT fixo.
   O mesmo vale para a Memória.
3. Armaduras passam a existir (tabela provisória abaixo), então a DEF
   diferencia as classes de verdade.
4. Ataque Pesado: −3 no ataque, +5 no dano, custa 1 SP, e NÃO pode ser
   combinado com Ataque Feroz.
5. Ataque Feroz: continua grátis, mas expõe o Furioso a apenas UM ataque
   com Vantagem, não a todos.
"""

from dataclasses import dataclass

from fichas import Ficha


@dataclass(frozen=True)
class Armadura:
    nome: str
    categoria: str
    base: int
    limite_destreza: int | None   # None = sem limite


ARMADURAS = {
    "acolchoada": Armadura("Acolchoada", "leve", 11, None),
    "couro_batido": Armadura("Couro batido", "leve", 12, None),
    "escamas": Armadura("Cota de escamas", "média", 13, 2),
    "peitoral": Armadura("Peitoral", "média", 14, 2),
}
BONUS_ESCUDO = 2


def def_com_armadura(mod_destreza: int, armadura: str | None, escudo: bool) -> int:
    """DEF total. Sem armadura continua sendo 10 + DES (regra 16)."""
    if armadura is None:
        total = 10 + mod_destreza
    else:
        a = ARMADURAS[armadura]
        des = mod_destreza if a.limite_destreza is None else min(mod_destreza, a.limite_destreza)
        total = a.base + des
    return total + (BONUS_ESCUDO if escudo else 0)


def _aplicar(f: Ficha, pv: int, sp: int, mp: int, atributo_divino: str,
             armadura: str | None, escudo: bool) -> Ficha:
    f.pv_max = pv + f.mods["constituicao"]
    f.sp_max = sp + f.mods["constituicao"]
    f.mp_max = mp + f.mods[atributo_divino]
    f.bonus_def = def_com_armadura(f.mods["destreza"], armadura, escudo) - (
        10 + f.mods["destreza"]
    )
    return f


def guardiao_v1() -> Ficha:
    f = Ficha(
        nome="Guardião", classe="guardiao",
        forca=17, destreza=13, constituicao=15,
        inteligencia=10, sabedoria=12, carisma=8,
        pv_max=0, sp_max=0, mp_max=0,
        arma="Espada longa", dados_arma=[8],
        tecnicas=["Escudo Vínculo"],
    )
    # Peitoral (média) + escudo: DEF 14 + min(DES,2) + 2 = 17
    return _aplicar(f, 14, 12, 6, "sabedoria", "peitoral", escudo=True)


def furioso_v1() -> Ficha:
    f = Ficha(
        nome="Furioso", classe="furioso",
        forca=17, destreza=13, constituicao=15,
        inteligencia=10, sabedoria=12, carisma=8,
        pv_max=0, sp_max=0, mp_max=0,
        arma="Machado grande", dados_arma=[10],
        tecnicas=["Ataque Pesado", "Sede de Sangue"],
    )
    # Couro batido (leve): DEF 12 + DES = 13. Machado grande ocupa as duas mãos.
    return _aplicar(f, 12, 14, 6, "sabedoria", "couro_batido", escudo=False)


def oraculo_v1() -> Ficha:
    f = Ficha(
        nome="Oráculo", classe="oraculo",
        forca=8, destreza=12, constituicao=13,
        inteligencia=17, sabedoria=15, carisma=10,
        pv_max=0, sp_max=0, mp_max=0,
        arma="Lança", dados_arma=[6], atributo_arma="destreza",
        tecnicas=["Palavra Curativa"],
    )
    # Couro batido (leve): DEF 12 + DES = 13.
    return _aplicar(f, 10, 8, 14, "inteligencia", "couro_batido", escudo=False)


TRIO_V1 = (guardiao_v1, furioso_v1, oraculo_v1)

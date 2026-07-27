"""Fichas de nível 1 conforme o livro v0, e monstros provisórios de teste.

IMPORTANTE: os monstros NÃO existem no livro. Foram criados aqui como réguas
de medição, calibrados para que um combate dure de 3 a 4 rodadas contra um
personagem de nível 1. Quando o livro tiver seu próprio bestiário, estes
valores devem ser substituídos.
"""

from dataclasses import dataclass, field

from dados import MOD

PROFICIENCIA_NIVEL_1 = 2


@dataclass
class Ficha:
    nome: str
    classe: str

    forca: int
    destreza: int
    constituicao: int
    inteligencia: int
    sabedoria: int
    carisma: int

    pv_max: int
    sp_max: int
    mp_max: int

    # Arma equipada
    arma: str
    dados_arma: list[int]
    atributo_arma: str = "forca"

    prof: int = PROFICIENCIA_NIVEL_1
    bonus_def: int = 0            # armadura/escudo — hoje sempre 0, não existem no livro
    tecnicas: list[str] = field(default_factory=list)

    # --- derivados ---
    @property
    def mods(self) -> dict[str, int]:
        return {
            "forca": MOD[self.forca],
            "destreza": MOD[self.destreza],
            "constituicao": MOD[self.constituicao],
            "inteligencia": MOD[self.inteligencia],
            "sabedoria": MOD[self.sabedoria],
            "carisma": MOD[self.carisma],
        }

    @property
    def defesa(self) -> int:
        return 10 + self.mods["destreza"] + self.bonus_def

    @property
    def bonus_ataque(self) -> int:
        return self.mods[self.atributo_arma] + self.prof

    @property
    def dano_fixo(self) -> int:
        return self.mods[self.atributo_arma]

    @property
    def iniciativa_bonus(self) -> int:
        return self.mods["destreza"]


# ---------------------------------------------------------------------------
# Personagens de nível 1 — distribuição padrão 15/14/13/12/10/8
# somada ao bônus do Parente Divino.
# ---------------------------------------------------------------------------

def guardiao_ares() -> Ficha:
    """Guardião, filho de Ares. FOR 15+2, CON 14+1. Espada longa + escudo.

    PV 6 + CON, SP 13 + CON, MP 8 + INT (livro v0, seção 6).
    """
    f = Ficha(
        nome="Guardião",
        classe="guardiao",
        forca=17, destreza=13, constituicao=15,
        inteligencia=10, sabedoria=12, carisma=8,
        pv_max=0, sp_max=0, mp_max=0,
        arma="Espada longa", dados_arma=[8],
        tecnicas=["Escudo Vínculo"],
    )
    f.pv_max = 6 + f.mods["constituicao"]
    f.sp_max = 13 + f.mods["constituicao"]
    f.mp_max = 8 + f.mods["inteligencia"]
    return f


def furioso_ares() -> Ficha:
    """Furioso, filho de Ares. Machado grande (1d10, Brutal, Pesada).

    PV 10 + CON, SP 10 + CON, MP 10 + INT (livro v0, seção 7).
    """
    f = Ficha(
        nome="Furioso",
        classe="furioso",
        forca=17, destreza=13, constituicao=15,
        inteligencia=10, sabedoria=12, carisma=8,
        pv_max=0, sp_max=0, mp_max=0,
        arma="Machado grande", dados_arma=[10],
        tecnicas=["Ataque Pesado", "Sede de Sangue"],
    )
    f.pv_max = 10 + f.mods["constituicao"]
    f.sp_max = 10 + f.mods["constituicao"]
    f.mp_max = 10 + f.mods["inteligencia"]
    return f


def oraculo_atena() -> Ficha:
    """Oráculo, filha de Atena. INT 15+2, SAB 14+1. Lança (1d6).

    PV 8 + CON, SP 10 + CON, MP 10 + INT (livro v0, seção 8).
    """
    f = Ficha(
        nome="Oráculo",
        classe="oraculo",
        forca=8, destreza=12, constituicao=13,
        inteligencia=17, sabedoria=15, carisma=10,
        pv_max=0, sp_max=0, mp_max=0,
        arma="Lança", dados_arma=[6], atributo_arma="destreza",
        tecnicas=["Palavra Curativa"],
    )
    f.pv_max = 8 + f.mods["constituicao"]
    f.sp_max = 10 + f.mods["constituicao"]
    f.mp_max = 10 + f.mods["inteligencia"]
    return f


TRIO_PADRAO = (guardiao_ares, furioso_ares, oraculo_atena)


# ---------------------------------------------------------------------------
# Monstros provisórios
# ---------------------------------------------------------------------------

@dataclass
class Monstro:
    nome: str
    pv_max: int
    defesa: int
    bonus_ataque: int
    dados_dano: list[int]
    dano_fixo: int
    iniciativa_bonus: int = 1
    ataques_por_turno: int = 1
    bonus_reflexos: int = 1


def bestiario() -> dict[str, Monstro]:
    return {
        # Capanga humano: a régua mais básica.
        "capanga": Monstro("Capanga", pv_max=11, defesa=12, bonus_ataque=3,
                           dados_dano=[6], dano_fixo=1),
        # Cão do inferno pequeno: rápido, morde forte.
        "cao": Monstro("Cão do Inferno", pv_max=15, defesa=13, bonus_ataque=4,
                       dados_dano=[6], dano_fixo=2, iniciativa_bonus=3),
        # Escorpião gigante: saco de pancada com dano alto.
        "escorpiao": Monstro("Escorpião Gigante", pv_max=22, defesa=14, bonus_ataque=4,
                             dados_dano=[8], dano_fixo=2),
        # Empusa: alvo difícil de acertar.
        "empusa": Monstro("Empusa", pv_max=18, defesa=15, bonus_ataque=5,
                          dados_dano=[6], dano_fixo=3, iniciativa_bonus=3),
        # Minotauro: chefe de teste, dois ataques.
        "minotauro": Monstro("Minotauro", pv_max=40, defesa=14, bonus_ataque=5,
                             dados_dano=[10], dano_fixo=3, ataques_por_turno=2),
    }

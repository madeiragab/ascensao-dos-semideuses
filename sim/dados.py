"""Matemática de dados do sistema Ascensão dos Semideuses.

Tudo aqui é analítico (probabilidade exata), não simulação. Serve para
responder perguntas de balanceamento sem depender de sorte de amostra.

Regras do sistema implementadas:
- Rolagem básica: 1d20 + modificador (+ proficiência quando aplicável).
- Acerto quando o resultado é >= DEF do alvo.
- 20 natural: Acerto Crítico (todos os dados de dano são rolados duas vezes,
  modificadores fixos entram uma vez só).
- 1 natural: erro automático.
- Vantagem: 2d20, usa o maior. Desvantagem: 2d20, usa o menor.
"""

from dataclasses import dataclass


def media_dado(faces: int) -> float:
    """Média de um dado de N faces."""
    return (faces + 1) / 2


def media_dado_brutal(faces: int) -> float:
    """Média de um dado com a propriedade Brutal.

    Ao rolar 1, rola de novo e usa o novo resultado (uma vez por ataque).
    """
    soma_2_ate_f = faces * (faces + 1) / 2 - 1
    return (media_dado(faces) + soma_2_ate_f) / faces


# ---------------------------------------------------------------------------
# Distribuição do d20
# ---------------------------------------------------------------------------

def dist_d20(vantagem: bool = False, desvantagem: bool = False) -> dict[int, float]:
    """Distribuição de probabilidade do resultado natural usado no teste.

    Vantagem e Desvantagem se anulam (regra 14 do livro).
    """
    if vantagem and desvantagem:
        vantagem = desvantagem = False

    if vantagem:
        return {k: (2 * k - 1) / 400 for k in range(1, 21)}
    if desvantagem:
        return {k: (2 * (21 - k) - 1) / 400 for k in range(1, 21)}
    return {k: 1 / 20 for k in range(1, 21)}


def chances_ataque(
    bonus: int,
    defesa: int,
    vantagem: bool = False,
    desvantagem: bool = False,
) -> tuple[float, float]:
    """Devolve (chance de acerto normal, chance de crítico).

    Acerto normal exclui o crítico — some os dois para a chance total de acertar.
    """
    dist = dist_d20(vantagem, desvantagem)
    p_crit = dist[20]
    p_normal = sum(
        p for nat, p in dist.items() if 2 <= nat <= 19 and nat + bonus >= defesa
    )
    return p_normal, p_crit


def chance_de_acertar(bonus: int, defesa: int, **kw) -> float:
    normal, crit = chances_ataque(bonus, defesa, **kw)
    return normal + crit


# ---------------------------------------------------------------------------
# Dano por ataque
# ---------------------------------------------------------------------------

@dataclass
class Ataque:
    """Um ataque único, para cálculo de dano esperado."""

    nome: str
    bonus: int
    dados: list[int]           # ex. [8] para 1d8, [6, 6] para 2d6
    fixo: float                # modificador de atributo e outros bônus fixos
    brutal: bool = False
    vantagem: bool = False
    desvantagem: bool = False

    def media_dos_dados(self) -> float:
        f = media_dado_brutal if self.brutal else media_dado
        return sum(f(d) for d in self.dados)

    def dano_esperado(self, defesa: int) -> float:
        """Dano médio por ataque contra uma DEF, já contando erro e crítico."""
        p_normal, p_crit = chances_ataque(
            self.bonus, defesa, vantagem=self.vantagem, desvantagem=self.desvantagem
        )
        d = self.media_dos_dados()
        return p_normal * (d + self.fixo) + p_crit * (2 * d + self.fixo)

    def chance_acerto(self, defesa: int) -> float:
        return chance_de_acertar(
            self.bonus, defesa, vantagem=self.vantagem, desvantagem=self.desvantagem
        )


def dano_area_esperado(
    dados: list[int],
    fixo: float,
    cd: int,
    bonus_reflexos: int,
    alvos: int = 1,
) -> float:
    """Dano esperado de habilidade em área.

    Falha no Teste de Reflexos = dano completo; sucesso = metade.
    O dano é rolado uma vez para todas as criaturas (regra 12.2).
    """
    p_passa = chance_de_acertar(bonus_reflexos, cd)  # alvo "acerta" o próprio teste
    total = sum(media_dado(d) for d in dados) + fixo
    por_alvo = p_passa * (total / 2) + (1 - p_passa) * total
    return por_alvo * alvos


MOD = {v: (v - 10) // 2 for v in range(1, 31)}
"""Modificador de atributo: (valor - 10) / 2 arredondado para baixo."""

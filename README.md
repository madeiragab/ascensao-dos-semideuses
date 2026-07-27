# Ascensão dos Semideuses

RPG de mesa autoral. Semideuses gregos no mundo moderno, base d20, com sistemas
próprios de criação de habilidades, de armas e de monstros.

Este repositório é a **oficina**: o livro sendo escrito e um simulador que testa
o balanceamento antes de qualquer número entrar no texto.

---

## O livro

**[`livro-do-jogador.html`](livro-do-jogador.html)** — o Livro do Jogador
diagramado. Abra no navegador. Ensina a jogar e a criar personagem do zero, com
capa e contracapa, sumário, capitulares e um d20 clicável no capítulo que explica
o teste. Imprime em PDF pelo Ctrl+P.

### Como ele é montado

O HTML publicado precisa ser autossuficiente — nenhum arquivo externo é
carregado —, então as capas entram codificadas dentro dele. Por isso existe uma
etapa de montagem:

```
livro-do-jogador.template.html  +  imagens/*.png  →  livro-do-jogador.html
```

```bash
powershell -ExecutionPolicy Bypass -File build-livro.ps1
```

> **Edite sempre o template.** O `livro-do-jogador.html` é gerado e será
> sobrescrito no próximo build.

---

## Os dois livros

| Livro | Onde | Conteúdo |
|---|---|---|
| **I — Livro do Jogador** | `livro-do-jogador.html` · rascunhos em `regras/` | personagem, combate, motor de habilidades, equipamento, interlúdio |
| **II — Bestiário** | [`bestiario/`](bestiario/README.md) | a Escala de Kleos, o motor de criação de monstros, 38 criaturas |

---

## Pastas

| Pasta | O que tem |
|---|---|
| `fonte/` | o Google Doc exportado, estado inicial do sistema. Quando um documento cita "seção 12.2", é aqui |
| `imagens/` | capa e contracapa originais, em PNG |
| `regras/` | os capítulos escritos e as propostas de mudança |
| `bestiario/` | o Livro II, completo |
| `sim/` | o simulador |

### Comece por [`regras/SUMARIO.md`](regras/SUMARIO.md)

É o mapa: cada capítulo do sistema, o que está pronto, o que tem buraco e o que
ainda não existe.

| Documento | Conteúdo |
|---|---|
| [SUMARIO.md](regras/SUMARIO.md) | mapa do livro inteiro e estado de cada capítulo |
| [v1-numeros.md](regras/v1-numeros.md) | correções de balanceamento, com o número que justifica cada uma |
| [combate.md](regras/combate.md) | ações, condições, cobertura, oportunidade, 0 PV e morte |
| [interludio.md](regras/interludio.md) | descanso, refeições, atividades de interlúdio, mecânica da Húbris |
| [magia-da-nevoa.md](regras/magia-da-nevoa.md) | **fora do Livro do Jogador.** Magia aprendida, Fórmulas, Descrença. Material para outro livro |

---

## O simulador

Python 3, nenhuma biblioteca externa. Rode de dentro de `sim/`.

```bash
cd sim
python experimentos.py      # diagnóstico do sistema original
python comparar.py          # original contra a proposta corrigida
python dia_de_aventura.py   # curva de desgaste ao longo de vários combates
python kleos.py             # valida a escala de perigo do Bestiário
python habilidades.py       # valida o motor de criação de habilidades
```

| Arquivo | O que faz |
|---|---|
| `dados.py` | Probabilidade exata do d20: acerto, crítico, Vantagem, dano esperado. Nada aqui é aleatório |
| `fichas.py` | Personagens de nível 1 conforme o sistema original, e os monstros de teste |
| `fichas_v1.py` | Os mesmos personagens com os números corrigidos, e a tabela de armaduras |
| `combate.py` | Motor de combate por turnos. Roda as duas versões de regra (`regras="v0"` ou `"v1"`) |
| `experimentos.py` | Bateria de diagnóstico do sistema original |
| `comparar.py` | Original contra proposta, nos mesmos combates |
| `dia_de_aventura.py` | Testa as regras de descanso: o desgaste acumula? |
| `kleos.py` | Valida a Escala de Kleos e as fórmulas de montagem de encontro |
| `habilidades.py` | Valida o motor de habilidades: custo por ponto, área, sustentar, orçamento do dia |

### Duas formas de medir, e por que as duas importam

**Analítica** (`dados.py`): probabilidade exata, sem sorte envolvida. Serve para
afirmações fechadas do tipo "esta técnica é sempre melhor que a outra".

**Simulação** (`combate.py`): milhares de combates completos com rolagens de
verdade. Alcança o que o cálculo isolado não vê — ordem de iniciativa, foco de
alvo, gasto de recursos ao longo do combate, quem cai primeiro.

Quando as duas discordam, a simulação está capturando algo real. Vale investigar
antes de decidir.

### Três vezes em que o teste me contrariou

Vale registrar, porque é o motivo de o simulador existir:

1. **Ataque Pesado.** Eu ia ajustar de −2/+5 para outro par de números. Nenhum
   par funciona enquanto o Ataque Feroz der Vantagem de graça no mesmo ataque —
   o conserto tinha de ser estrutural, não numérico.
2. **Bandos de monstros.** Escrevi que muitos inimigos fracos valem *mais* que a
   soma do Kleos. Valem **menos**: o grupo concentra fogo e cada morto para de
   causar dano para sempre. A regra foi reescrita segundo o dado.
3. **Orçamento do conjurador.** Escrevi que ele ganha o dia em dano acumulado.
   Não ganha — 80 contra 97 do Furioso, que não gasta nada. O que ele compra com
   MP é escolha, não dano bruto.

---

## Limites conhecidos do simulador

- **Condições não são modeladas.** Amedrontado, Preso, Atordoado e companhia não
  existem no motor de combate, então criaturas de controle são mais perigosas na
  mesa do que na simulação.
- **Arremetidas e Recusas não são modeladas**, então os degraus altos da Escala
  de Kleos (6 a 11) têm margem de erro maior que os baixos.
- **Sem posicionamento nem distância**: todos alcançam todos. Movimento, terreno,
  cobertura e alcance de arma não influenciam.
- **Ataques de oportunidade** já existem nas regras, mas não no simulador.
- **A escala foi calibrada no nível 1.** Enquanto não existir progressão de
  nível, tudo acima disso é extrapolação.

Cada item é uma lacuna a fechar, não uma limitação técnica.

## As dívidas do sistema

1. **Progressão de nível 2 a 20.** Hoje só existe o bônus de proficiência. É o
   que mais trava, e trava os dois livros.
2. **Armaduras e preços.** As armaduras em uso são provisórias.
3. **Economia.** Dracmas, quanto custa um Kit de Criação, quanto rende um bico.

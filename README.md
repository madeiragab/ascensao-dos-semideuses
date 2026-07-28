> 🇧🇷 **Português** · 🇬🇧 [English](README.en.md)

# Ascensão dos Semideuses — RPG de mesa

Sistema de RPG autoral. Semideuses gregos no mundo moderno, base d20, com
motores próprios de criação de habilidades, de armas e de monstros.

**No ar:** https://madeiragab.github.io/ascensao-dos-semideuses/

O que separa este projeto de um documento de regras é o **simulador**: nenhum
número entra no livro sem antes ser medido. Ele já me contrariou três vezes, e as
três correções estão documentadas mais abaixo.

---

## Os quatro livros

| | Livro | Conteúdo |
|---|---|---|
| **I** | [Livro do Jogador](https://madeiragab.github.io/ascensao-dos-semideuses/livro-do-jogador.html) | Como jogar, criação de personagem em sete etapas, combate, e o motor de criação de habilidades |
| **II** | [Bestiário](https://madeiragab.github.io/ascensao-dos-semideuses/bestiario.html) | A Escala de Kleos, o motor de criação de monstros e 38 criaturas |
| **III** | [Grimório](https://madeiragab.github.io/ascensao-dos-semideuses/grimorio.html) | A Magia da Névoa: magia aprendida, com regra de Descrença |
| **IV** | [Ficha do Herói](https://madeiragab.github.io/ascensao-dos-semideuses/ficha.html) | Preenchível no navegador, com retrato do personagem, e sai em PDF |

---

## Como o sistema funciona

**A rolagem** é `1d20 + modificador + proficiência` contra uma CD. Vantagem e
Desvantagem substituem modificadores pequenos: dois dados, usa o maior ou o menor.

**Três recursos**, cada um com um ritmo próprio de recuperação. Pontos de Vida
voltam devagar — um descanso longo devolve só metade. Pontos de Vigor voltam
inteiros em uma hora. Pontos de Mana só voltam dormindo. Isso faz o desgaste de
um dia de aventura acumular de verdade.

**A Húbris** é o defeito fatal do personagem, e tem regra. O Mestre oferece uma
*Provocação*; se o jogador aceita agir conforme o defeito, ganha *Ímpeto*, que
compra Vantagem e outras coisas. Uma vez por arco, o Mestre pode declarar uma
*Ruptura*, e aí a Húbris decide por você.

**Habilidades não vêm em lista.** O jogador constrói cada uma comprando efeitos
com pontos:

```
CUSTO = duração + efeitos adicionais + alcance
```

A duração já inclui o primeiro ponto de efeito: instantânea 1, sustentada 2, cena
4. Sustentar custa metade do custo final por rodada. Cada ponto compra 1d8 de
dano em alvo único, ou 1d6 em área, ou +1 DEF, ou uma condição fraca, e assim por
diante.

**Catorze perícias**, não dezesseis: *Arcanismo* foi absorvida por Mitologia, porque
num mundo em que toda magia é grega não existem dois corpos de conhecimento, e
*Lidar com Animais* entrou em Sobrevivência.

**Monstros são medidos em Kleos** — a glória que custa derrubá-los. Onze degraus
com nome: Rumor, Boato, Conto, Façanha, Feito, Canção, Lenda, Mito, Epopeia,
Teomaquia, Cataclisma. Uma criatura de Kleos N é um combate justo e perigoso para
N semideuses.

**Toda criatura tem uma Fraqueza Mítica** descobrível. A Hidra é impossível sem
fogo. O Leão de Neméia é imune a armas. Cérbero quer brincar de bola. Descobrir
isso é jogar.

---

## O simulador

Python 3, sem nenhuma biblioteca externa. Rode de dentro de `sim/`.

```bash
cd sim
python experimentos.py      # diagnóstico do sistema original
python comparar.py          # original contra a proposta corrigida
python dia_de_aventura.py   # curva de desgaste ao longo de vários combates
python kleos.py             # valida a escala de perigo do Bestiário
python habilidades.py       # valida o motor de criação de habilidades
```

Ele mede de duas formas, e as duas importam. A **analítica** calcula
probabilidade exata do d20, sem sorte envolvida — serve para afirmações fechadas
do tipo "esta técnica é sempre melhor que a outra". A **simulação** roda milhares
de combates completos com rolagens de verdade, e alcança o que o cálculo isolado
não vê: ordem de iniciativa, foco de alvo, gasto de recursos, quem cai primeiro.

### As três vezes em que o teste me contrariou

1. **O Ataque Pesado não tinha conserto numérico.** Eu ia trocar o −2/+5 por
   outro par de números. Varri sete variantes: nenhuma funciona enquanto o Ataque
   Feroz der Vantagem de graça no mesmo ataque, porque Vantagem paga qualquer
   penalidade de acerto. O conserto foi estrutural — proibir a combinação.
2. **Bandos de inimigos fracos valem menos, não mais.** Eu havia escrito que
   muitos inimigos somavam acima do Kleos total. É o contrário: três criaturas de
   Kleos 1 dão 96% de vitória contra 82% de uma única de Kleos 3, porque o grupo
   concentra fogo e cada morto para de causar dano para sempre. A regra virou
   `soma × 3/4`, com erro máximo de 0,3 numa escala de onze.
3. **Quem gasta mana não compra dano.** Eu havia concluído que o conjurador ganha
   o dia em dano acumulado. Não ganha: 80 contra 97 do Furioso, que não gasta
   nada. O que o MP compra é alcance, área, condição e escolha.

---

## Estrutura do repositório

```
livro-do-jogador.html   bestiario.html   grimorio.html   ficha.html
                                                        ← gerados, não edite
index.html              a estante do site

template/               as cascas dos livros e a folha de estilo única
  livro.css             CSS compartilhado pelos três livros
  livro-do-jogador.html escrito à mão
  bestiario.html        casca; o conteúdo vem dos markdown
  grimorio.html         casca, com paleta verde e ouro própria
  ficha.html            a ficha preenchível, paleta preta e ouro

regras/                 os capítulos em markdown, e o mapa do sistema
bestiario/              o Livro II em markdown
imagens/                capas originais e miniaturas geradas
sim/                    o simulador
fonte/                  o documento original, estado inicial do sistema
```

Comece por **[`regras/SUMARIO.md`](regras/SUMARIO.md)**: é o mapa de cada
capítulo, o que está pronto, o que tem buraco e o que ainda não existe.

### Como gerar os livros

Os HTML publicados são autossuficientes — nenhum arquivo externo é carregado, e
as capas entram codificadas dentro deles. Por isso existe uma etapa de montagem:

```bash
powershell -ExecutionPolicy Bypass -File build.ps1
```

O script redimensiona as capas, gera as miniaturas da estante e chama
`build_livros.py`, que converte os markdown e monta os três livros.

> **Edite sempre `template/` e os markdown.** Os arquivos `.html` na raiz são
> gerados e serão sobrescritos no próximo build.

---

## As dívidas do sistema

1. **Progressão de nível 2 a 20.** Hoje só existe o bônus de proficiência. É o
   que mais trava, e trava os três livros: a Escala de Kleos foi calibrada só no
   nível 1, então os degraus altos são extrapolação.
2. **Armaduras e preços.** As armaduras em uso são provisórias.
3. **Economia.** Dracmas, quanto custa um Kit de Criação, quanto rende um bico.

### Limites conhecidos do simulador

- Condições não são modeladas, então criaturas de controle são mais perigosas na
  mesa do que na simulação.
- Arremetidas e Recusas não são modeladas, o que aumenta a margem de erro nos
  degraus de Kleos 6 a 11.
- Sem posicionamento nem distância: todos alcançam todos.
- Ataques de oportunidade existem nas regras, mas não no simulador.

---

## Licença

Projeto pessoal, em desenvolvimento. As criaturas e divindades vêm da mitologia
greco-romana, que é domínio público; o sistema de regras, os textos e a Escala de
Kleos são autorais.

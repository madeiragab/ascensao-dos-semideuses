> 🇧🇷 **Português** · 🇬🇧 [English](README.en.md)

# Ascensão dos Semideuses — RPG de mesa

Sistema de RPG autoral. Semideuses gregos no mundo moderno, base d20, com
motores próprios de criação de habilidades, de armas e de monstros.

**No ar:** https://madeiragab.github.io/ascensao-dos-semideuses/

O que separa este projeto de um documento de regras é a combinação de
**simulação e playtest de mesa**: números são medidos, decisões improvisadas são
registradas, e a regra só fecha depois de sobreviver aos dois. As quatro vezes em
que os números contrariaram a intuição estão documentadas mais abaixo.

**Versão atual:** 0.11.1 · [Changelog](CHANGELOG.md)

---

## Os cinco livros

| | Livro | Conteúdo |
|---|---|---|
| **I** | [Livro do Jogador](https://madeiragab.github.io/ascensao-dos-semideuses/livro-do-jogador.html) | Como jogar, criação, combate, Fúria opcional, catálogo de itens, materiais divinos e motor de habilidades |
| **II** | [Bestiário](https://madeiragab.github.io/ascensao-dos-semideuses/bestiario.html) | A Escala de Kleos, o motor de criação de monstros e 38 criaturas |
| **III** | [Grimório](https://madeiragab.github.io/ascensao-dos-semideuses/grimorio.html) | A Magia da Névoa: magia aprendida, com regra de Descrença |
| **IV** | [Guia do Mestre](https://madeiragab.github.io/ascensao-dos-semideuses/guia.html) | Conduzir da one-shot à campanha, NPCs, investigação, quebrar objetos e perigos de ambiente |
| **V** | [Ficha do Herói](https://madeiragab.github.io/ascensao-dos-semideuses/ficha.html) | Preenchível, calcula linhagem e progressão, aceita retrato e baixa diretamente um PDF de três páginas A4 |

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
*Ruptura*, e aí a Húbris decide por você. Ímpeto entra no máximo uma vez por cena
e é gasto no máximo uma vez por turno.

Como módulo opcional, a **Fúria do Semideus** transforma a Ruptura em três
estágios de transbordamento divino, definidos pelos Vínculos, pela linhagem e
pelas emoções de cada personagem — com poder grande, agência combinada e preço real.

**Habilidades não vêm em lista.** O jogador constrói cada uma comprando efeitos
com pontos:

```
CUSTO FINAL = duração + efeitos adicionais + alcance + modificadores
```

A duração já inclui o primeiro ponto de efeito: instantânea 1, sustentada 2, cena
4. Sustentar custa metade do custo final por rodada. Cada ponto compra 1d8 de
dano em alvo único, ou 1d6 em área, ou +1 DEF, ou uma condição fraca, e assim por
diante.

**As regras universais** fecham as situações que costumavam depender do Mestre:
efeitos combinados, ativação, Manifestação Menor, fogo amigo, carregar aliados,
objetos e mãos, críticos de perícia, estabilização e Ímpeto. A consulta curta está
em [`regras/regras-universais.md`](regras/regras-universais.md).

**Itens têm nível.** Seis graus cobrem do equipamento Mortal à relíquia Divina;
Sintonização limita quantos poderes permanentes ficam ativos. Além das armas e
armaduras, o Livro do Jogador traz 21 utilitários, 12 curativos e 24 itens
mágicos com preço em dracmas.

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
python condicoes.py         # mede o preço do controle contra o do dano
python equilibrio.py        # auditoria: Kleos por nível, classes, armas, armaduras
python tecnicas.py          # mede as 36 técnicas de classe, uma a uma
python calibrar_kleos.py    # testa a escala de Kleos em todos os níveis
```

Ele mede de duas formas, e as duas importam. A **analítica** calcula
probabilidade exata do d20, sem sorte envolvida — serve para afirmações fechadas
do tipo "esta técnica é sempre melhor que a outra". A **simulação** roda milhares
de combates completos com rolagens de verdade, e alcança o que o cálculo isolado
não vê: ordem de iniciativa, foco de alvo, gasto de recursos, quem cai primeiro.

### As quatro vezes em que o teste me contrariou

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
4. **A Escala de Kleos estava errada fora do nível 1.** A regra dizia que um herói
   valia 1, 2, 3 ou 4 de Kleos conforme a faixa de nível. O medido é 1 · 1¾ · 2¼ ·
   2¾ · 3 — um personagem de nível 20 vale menos de *três* vezes um de nível 1, não
   quatro. Um grupo de nível 15 seguindo a regra antiga seria mandado contra algo
   três degraus acima do que aguenta.

---

## Estrutura do repositório

```
livro-do-jogador.html   bestiario.html   grimorio.html
guia.html               ficha.html
                                                        ← gerados, não edite
index.html              a estante do site

template/               as cascas dos livros e a folha de estilo única
  livro.css             CSS compartilhado pelos cinco livros
  livro-do-jogador.html escrito à mão
  bestiario.html        casca; o conteúdo vem dos markdown
  grimorio.html         casca, com paleta verde e ouro própria
  guia.html             o Guia do Mestre, paleta roxa e ouro
  ficha.html            a ficha preenchível, paleta preta e ouro

regras/                 os capítulos em markdown, e o mapa do sistema
  regras-universais.md  consulta rápida nascida do primeiro playtest completo
bestiario/              o Livro II em markdown
imagens/                capas originais e miniaturas geradas
sim/                    o simulador
fonte/                  o documento original, estado inicial do sistema
vendor/                 bibliotecas MIT incorporadas para gerar o PDF A4
CHANGELOG.md            histórico de versões e decisões de regra
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
`build_livros.py`, que converte os markdown e monta os cinco livros.

Para repetir toda a regressão numérica:

```bash
powershell -ExecutionPolicy Bypass -File test.ps1
```

> **Edite sempre `template/` e os markdown.** Os arquivos `.html` na raiz são
> gerados e serão sobrescritos no próximo build.

---

## As dívidas do sistema

O Livro do Jogador está completo para jogar do nível 1 ao 20. O que falta é
refinamento:

1. **Dez técnicas que o simulador não representa.** Das 36, 26 foram medidas; as
   outras dependem de posicionamento, deslocamento forçado, medo ou rerrolagem,
   que o motor não modela. Precisam de mesa, não de simulador.
2. **Economia de dracmas em campanha.** Os preços e recompensas iniciais funcionam,
   mas ainda falta medir inflação, manutenção e recompensas de arcos longos.

### Limites conhecidos do simulador

- **Arremetidas e Recusas** não são modeladas, o que aumenta a margem de erro nos
  degraus de Kleos 6 a 11 — as criaturas completas do Bestiário são mais perigosas
  que a versão testada.
- Condições **são** modeladas desde a calibragem do capítulo de Condições, mas só
  três famílias: perder o turno, atacar com Desvantagem e sangramento por rodada.
- Sem posicionamento nem distância: todos alcançam todos.
- Ataques de oportunidade existem nas regras, mas não no simulador.

---

## Licença

Projeto pessoal, em desenvolvimento. As criaturas e divindades vêm da mitologia
greco-romana, que é domínio público; o sistema de regras, os textos e a Escala de
Kleos são autorais.

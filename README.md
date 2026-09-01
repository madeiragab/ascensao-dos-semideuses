> 🇧🇷 **Português** · 🇬🇧 [English](README.en.md)

# Ascensão dos Semideuses — RPG de mesa

[![ci](https://github.com/madeiragab/ascensao-dos-semideuses/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/madeiragab/ascensao-dos-semideuses/actions/workflows/ci.yml)

Projeto independente e não oficial de RPG de mesa. Suas regras, seus textos e
seus motores de criação são autorais; a ambientação apresenta semideuses gregos
no mundo moderno em uma base d20.

**No ar:** https://madeiragab.github.io/ascensao-dos-semideuses/

> **Aviso de independência:** projeto não oficial e sem fins lucrativos.
> *Percy Jackson* e os elementos próprios dessa franquia pertencem aos seus
> respectivos autores e titulares, incluindo Rick Riordan e empresas licenciadas.
> Este projeto não é afiliado, aprovado ou patrocinado por eles.

O que separa este projeto de um documento de regras é a combinação de
**simulação e playtest de mesa**: números são medidos, decisões improvisadas são
registradas, e a regra só fecha depois de sobreviver aos dois. As quatro vezes em
que os números contrariaram a intuição estão documentadas mais abaixo.

**Versão atual:** 0.17.0 · 31/08/2026 · [Changelog](CHANGELOG.md)

---

## Os cinco livros

| | Livro | Conteúdo |
|---|---|---|
| **I** | [Livro do Jogador](https://madeiragab.github.io/ascensao-dos-semideuses/livro-do-jogador.html) | Como jogar, criação, combate, Fúria opcional, catálogo de itens, materiais divinos, encantamentos, a Forja e o motor de habilidades |
| **II** | [Bestiário](https://madeiragab.github.io/ascensao-dos-semideuses/bestiario.html) | A Escala de Kleos, o passo a passo de criação de criaturas, 38 delas prontas, o saque por Kleos e a Fera Vinculada |
| **III** | [Grimório](https://madeiragab.github.io/ascensao-dos-semideuses/grimorio.html) | A Magia da Névoa: magia aprendida, com regra de Descrença |
| **IV** | [Guia do Mestre](https://madeiragab.github.io/ascensao-dos-semideuses/guia.html) | Conduzir da one-shot à campanha, NPCs, o Aliado que luta, investigação, perigos, a Névoa e o mundo mortal |
| **V** | [Ficha do Herói](https://madeiragab.github.io/ascensao-dos-semideuses/ficha.html) | Preenchível, com abas para o herói e para a Fera Vinculada; calcula linhagem, progressão e Grau, aceita retrato e baixa ou importa um PDF editável em folhas A4 |

Os cinco livros têm sumários e referências clicáveis. Um pequeno tridente no
canto inferior abre os outros tomos sem tirar o leitor da página atual.

PDFs baixados pela Ficha a partir da versão 0.13.1 carregam os dados editáveis
dentro do próprio arquivo e podem ser importados depois. A leitura acontece
somente no navegador; PDFs anteriores eram imagens e não podem ser reconstruídos.
Desde a versão 0.13.2, o retrato original também é preservado sem recorte,
redimensionamento ou recompressão durante esse ciclo.

---

## Como o sistema funciona

**A rolagem** continua simples, mas agora cada oposição usa um alvo pronto. Testes
de perícia rolam `1d20 + modificador + proficiência` contra uma CD; ataques rolam
contra a DEF; efeitos rolam contra Fortitude, Reflexos ou Vontade passiva. Cada
defesa é `14 + atributo + proficiência`, se treinada. Quem causa o efeito é quem
rola. A base 14 preserva exatamente a chance do modelo anterior, inclusive ao
inverter Vantagem e Desvantagem.

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
com pontos, e só depois converte pontos em recurso:

```
PONTOS  = duração + efeitos adicionais + alcance + modificadores
CUSTO   = pontos × Grau do ponto
```

A duração já inclui o primeiro ponto de efeito: instantânea 1, sustentada 2, cena
4. Sustentar custa metade do custo final por rodada.

**A progressão é o Grau**, e ele é a faixa de nível — 1 nos níveis 1–4 até 5 nos
17–20. Cada tabela de efeito tem uma linha por Grau: um ponto de dano em alvo
único compra de `1d8` a `5d8`, um de área de `1d6` a `5d6`, um de movimento de
+3 m a +15 m. O ponto do Grau G custa G, de modo que o **dano por MP fica
constante**: o Grau muda quanto cabe numa ação, não quanto o recurso rende.
Condições e Vantagem não engordam com o Grau — alcançam mais criaturas. Defesa
não engorda nunca: +2 continua sendo o máximo, porque medido no nível 20 cada
ponto de DEF vale quase sete pontos de vitória.

Uma habilidade escrita no nível 1 não precisa ser reconstruída: ela continua na
ficha e passa a ser paga no Grau novo, entregando mais.

**As regras universais** fecham as situações que costumavam depender do Mestre:
defesas passivas, efeitos combinados, ativação, Manifestação Menor, fogo amigo, carregar aliados,
objetos e mãos, críticos de perícia, estabilização e Ímpeto. A consulta curta está
em [`regras/regras-universais.md`](regras/regras-universais.md).

**Itens têm Grau, e o Grau é a progressão do equipamento.** Seis degraus cobrem
do Mortal à relíquia Divina, e cada um dá **dados de arma** e DEF — uma espada
Heroica é `2d8`, um machado Lendário é `3d10`. Isso não é enfeite: medido em três
mil combates por nível, um trio de nível 20 sem item que cresça leva 11,5 rodadas
para derrubar o encontro justo e perde uma luta em cada três; com o Grau, o
combate volta a durar de 2 a 4 rodadas em toda a carreira.

**A Forja** é o motor do Capítulo Sete guardado dentro de um objeto: os mesmos
pontos, as mesmas tabelas, pagos em **Cargas** em vez de MP. Uma Ação de
Interlúdio é uma tentativa — Manufatura contra CD 10 + os pontos do item —, e a
falha marca a peça, não o ferreiro. Do Mítico para cima o projeto exige material
de criatura de Kleos 5 ou mais, o que amarra a forja ao Bestiário. Encantamentos
cuidam do resto: a arma que vira caneta, a que volta sozinha para a mão, o véu
que apaga quem o veste.

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
python graus.py             # calibra os Graus de habilidade e a progressão
python anteparo.py          # mede a habilidade de classe do Guardião
python defesas_passivas.py  # prova a equivalência exata das defesas de base 14
python forja.py             # prova que o Grau do item segura os 20 níveis
python criaturas.py         # mede Poderes de área e Arremetidas em Kleos
python completo.py          # o jogo inteiro: habilidade, controle e Recusa
python nevoa.py             # mede a Magia da Névoa: Fórmula, Descrença, Refluxo
python aliado.py            # quanto um Aliado pode ser sem virar um jogador
python duelo.py             # semideus contra semideus, e a armadilha do controle
python ficha.py             # confere a Ficha do Herói contra o simulador
```

Ele mede de duas formas, e as duas importam. A **analítica** calcula
probabilidade exata do d20, sem sorte envolvida — serve para afirmações fechadas
do tipo "esta técnica é sempre melhor que a outra". A **simulação** roda milhares
de combates completos com rolagens de verdade, e alcança o que o cálculo isolado
não vê: ordem de iniciativa, foco de alvo, gasto de recursos, quem cai primeiro.

**Desde a revisão de agosto de 2026, o motor joga o jogo inteiro.** Os heróis
entram com equipamento no Grau do nível, gastam MP e SP em habilidade de dano e
em controle por Rolagem de Efeito; as criaturas entram com Poder de área,
Arremetidas, Recusas, Vontade do Lugar e Presença. Com tudo ligado dos dois
lados, o encontro justo entrega de 68% a 93% de vitória, de 2,4 a 3,1 rodadas,
com 1,7 a 2,6 heróis de pé de três.

Cinco coisas que a medição mudou no livro, e que valem como aviso a quem for
mexer nos números:

- **o dano de arma não acompanhava o PV dos monstros** — o Grau do item passou a
  dar dados de arma, e o combate voltou a durar de 2 a 4 rodadas do nível 3 ao 20;
- **o crítico de habilidade apagava o encontro** — passou a somar dados iguais ao
  Grau em vez de dobrar tudo;
- **a Escala de Kleos tinha um platô de cinco níveis** — as faixas foram alinhadas
  às do Grau;
- **a conta de mesas grandes estava errada** — multiplicar heróis por Kleos mandava
  um grupo de quatro contra um encontro que ele vence 11% das vezes. Hoje é tabela
  medida: o quarto jogador quase não move o degrau, e o quinto vale +1;
- **um Aliado montado como monstro morria em toda sessão** — 6% de sobrevivência no
  nível 9. Hoje ele usa a linha do Kleos do Grupo menos 2.

### As sete vezes em que o teste me contrariou

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
5. **A conta de mesas grandes estava errada, e feio.** Kleos do Grupo era
   multiplicação: quatro heróis de nível 5 valiam Kleos 7. Medido, esse encontro é
   um massacre contra o grupo — **11% de vitória**; cinco heróis contra o Kleos 9
   que a conta mandava vencem **0%**. A escala sobe 35% por degrau e um jogador a
   mais soma bem menos que isso. Virou tabela medida: **o quarto jogador quase não
   move o degrau, o quinto vale +1, e o sexto não move nada**.
6. **O dano de arma não acompanhava o PV dos monstros.** Do nível 5 ao 20 o ataque
   com arma crescia 15% enquanto o PV do encontro justo crescia 250%: um trio de
   nível 20 levava **11,5 rodadas** e perdia uma luta em cada três. O conserto foi
   dar **dados de arma** ao Grau do item — e o combate voltou a durar de 2 a 4
   rodadas em toda a carreira.
7. **Um Aliado montado como monstro morria toda sessão.** Construir NPC de combate
   pelo Kleos que um herói "vale" dá **6% de sobrevivência no nível 9**. Ele agora
   usa a linha do Kleos do Grupo menos 2, e sobrevive de 64% a 78% sem roubar o
   dano dos jogadores.

E uma que o **playtest de mesa** contrariou, sem simulador nenhum: eu havia medido
a economia de MP dos marciais e descartado o problema com *"física paga SP"*. A
mesa mostrou o furo — um filho de Netuno constrói água, não músculo, e das quatro
habilidades que o jogador criou na ficção, três eram Elementais pagas em MP, com um
pool de 8.

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
  migracao-0.15.md      o que ajustar numa campanha começada antes de agosto/2026
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

Os cinco livros estão completos para jogar do nível 1 ao 20, e o mapa do sistema
não tem mais nenhuma linha vermelha. O que falta é de outra natureza:

1. **Playtest com mesa de verdade.** O único playtest completo foi solo, com dois
   NPCs — e mesmo assim achou três coisas que dezoito arquivos de simulação não
   tinham achado. Uma mesa com quatro pessoas discutindo tática vai achar outras.
2. **Dez técnicas que o simulador não representa.** Das 36, 26 foram medidas; as
   outras dependem de posicionamento, deslocamento forçado, medo ou rerrolagem.
   Precisam de mesa, não de simulador.
3. **Metade do Grimório é imensurável.** Porta Falsa, Cidade de Bruma e Outra Pele
   valem pelo que abrem de ficção, e nenhum motor de combate julga isso.
4. **Economia de dracmas em arco longo.** Preços e recompensas por Kleos existem e
   fecham a conta de um item por arco; falta medir inflação e manutenção.

### Limites conhecidos do simulador

- **Vontade do Lugar e Presença** entraram por aproximação: modeladas como
  Desvantagem, e não como raiz, escuridão e chão que treme, cada uma com sua
  defesa.
- A Tábua de Kleos foi calibrada com um **trio**. Mesas de quatro a seis foram
  medidas depois, mas fazem mais Rolagens de Efeito por rodada, o que empurra o
  valor da Recusa para cima.
- **Sem posicionamento nem distância**: todos alcançam todos. Ataques de
  oportunidade existem nas regras e não no motor.
- **O simulador joga sempre igual.** Ele não recua, não usa terreno, não negocia e
  não foge. Jogador faz as quatro.

---

## Licença

Projeto pessoal, em desenvolvimento. As criaturas e divindades vêm da mitologia
greco-romana, que é domínio público; o sistema de regras, os textos e a Escala de
Kleos são autorais.

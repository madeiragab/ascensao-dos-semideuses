# Livro II — Bestiário
## Parte I — A Escala de Kleos

---

## 1. O que é Kleos

**Κλέος** era, para os gregos, a glória que sobrevive a quem a conquistou. Não a
força de um herói: o tamanho da história que contam sobre ele depois.

Neste livro, o **Kleos** de uma criatura mede exatamente isso — **quanta glória
custa derrubá-la**. E, porque glória e perigo são a mesma moeda na boca de um
poeta, ele mede também quantos semideuses treinados são necessários para
sobreviver ao encontro.

> **A regra em uma frase:** uma criatura de **Kleos N** é um combate justo e
> perigoso para **N semideuses**.

Kleos 1 é uma criatura que um único semideus resolve. Kleos 10 é um deus
olímpico, e dez semideuses ainda vão sangrar por isso. Kleos 11 não é para ser
vencido por semideuses de jeito nenhum.

---

## 2. Os onze degraus

Cada degrau tem nome, porque "monstro de dificuldade 6" não é coisa que se diga
numa mesa.

| Kleos | Degrau | O que a morte dessa criatura significa |
|---|---|---|
| **1** | **Rumor** | Ninguém vai lembrar. Um sátiro bandoleiro, um mercenário mortal, um filhote. |
| **2** | **Boato** | Alguém comenta no acampamento. Uma harpia, uma dracena de guarda. |
| **3** | **Conto** | Você conta em volta da fogueira. Um cão do inferno adulto, um autômato. |
| **4** | **Façanha** | Você se gaba, e é justo. O Minotauro está aqui. |
| **5** | **Feito** | Ganha-se um apelido com isto. O Leão de Neméia, a Esfinge. |
| **6** | **Canção** | Um sátiro escreve uma música. A Quimera, a Hidra. |
| **7** | **Lenda** | Contada por gerações. Cérbero, Escila. |
| **8** | **Mito** | Entra no cânone. Ladão, Caríbdis, um titã menor. |
| **9** | **Epopeia** | Precisa de um poema inteiro. Um Gigante, Hiperião. |
| **10** | **Teomaquia** | Guerra contra um deus. Literalmente. |
| **11** | **Cataclisma** | O mundo quase acabou. Tifão, Cronos, Gaia. |

---

## 3. O Kleos de um grupo

Cada semideus vale um tanto de Kleos, e esse valor cresce com o nível — mas
**cresce bem mais devagar do que a escala de monstros**. Um herói de nível 20 não
vale vinte vezes um de nível 1; vale menos de três vezes.

| Nível do personagem | Kleos que ele vale |
|---|---|
| 1–4 | **1** |
| 5–8 | **1¾** |
| 9–12 | **2¼** |
| 13–16 | **2¾** |
| 17–20 | **3** |

As faixas são **as mesmas faixas de Grau** do Livro I, e isso não é coincidência:
o personagem muda de patamar quando o Grau dele muda.

O **Kleos do Grupo** é a soma. Para não fazer conta com frações na mesa, consulte
direto:

| Nível | 3 heróis | 4 heróis | 5 heróis | 6 heróis |
|---|---|---|---|---|
| 1–4 | 3 | 4 | 4 | 4 |
| 5–8 | 5 | 5 | 6 | 6 |
| 9–12 | 7 | 7 | 8 | 8 |
| 13–16 | 8 | 8 | 9 | 9 |
| 17–20 | 9 | 10 | 10 | 10 |

**Esta tabela não é a soma dos valores de cima, e é de propósito.** Somar
funcionava para um trio e quebrava para mesas maiores — ver logo abaixo.

**Aliados contam.** Um deus que luta ao seu lado soma o Kleos dele. É por isso que
existem alianças na mitologia — e é assim que um Cataclisma vira um problema
resolvível.

### O quarto jogador quase não muda o Kleos, e o quinto vale um degrau

A primeira versão desta tabela multiplicava: quatro heróis de nível 5 valiam
4 × 1¾ = 7. Medido com o motor jogando o jogo inteiro, esse encontro é um
**massacre contra o grupo**:

| Grupo | O que a conta linear mandava | Vitórias |
|---|---|---|
| 4 heróis de nível 5 | Kleos 7 | **11%** |
| 5 heróis de nível 5 | Kleos 9 | **0%** |
| 4 heróis de nível 9 | Kleos 9 | **6%** |
| 5 heróis de nível 13 | Kleos 11 | **4%** |

O motivo é a grossura da escala. A Tábua cresce cerca de **35% por degrau**,
e um jogador a mais soma bem menos que isso: ele traz um corpo e uma ação, mas
não traz PV de monstro nem dano de monstro junto. Multiplicar heróis por Kleos
supõe uma escala fina que a Tábua não tem.

A tabela acima é a medida: **o quarto jogador raramente move o degrau, o quinto
vale +1, e o sexto não move nada**. Um sexto herói entra como folga, não como
degrau: no nível 3 ele leva o grupo de 61% para 92% de vitória contra o mesmo
Kleos, e no 17 para 94%.

A única exceção está no topo: **seis heróis de nível 20 aguentam um Kleos 11**,
com 78% de vitória. Só que Kleos 11 é Cataclisma, e Cataclisma não cai por dano —
cai pelo Selo ([seção 7](#secao-7)). A conta permite; a ficção continua mandando.

Quando quiser apertar uma mesa grande sem subir um degrau inteiro, some criaturas
menores pelas fórmulas da [seção 5](#secao-5) — é para isso que elas existem.

Para reproduzir: `sim/completo.py`.

### Estes números foram medidos, e a primeira versão estava errada

A escala original dizia que um personagem valia 1, 2, 3 ou 4 de Kleos conforme a
faixa de nível. Isso estava certo no nível 1 e errado em todo o resto. Com a
progressão do Capítulo Nove implementada no simulador — e com a Oráculo usando o
MP dela, não cutucando com uma lança —, o Kleos justo para um trio ficou assim:

| Nível do trio | Kleos justo medido | A regra antiga dizia |
|---|---|---|
| 1 | 3,1 | 3 ✓ |
| 5 | 5,2 | 6 |
| 10 | 6,8 | **9** |
| 15 | 8,0 | **12** |
| 20 | 8,6 | **12** |

Um grupo de nível 15 seguindo a regra antiga seria mandado contra algo três
degraus acima do que aguenta. A tabela acima é a corrigida.

Para reproduzir: `sim/calibrar_kleos.py`.

### As faixas mudaram uma segunda vez, e pelo mesmo motivo

A primeira correção acertou os valores e errou os cortes: as faixas eram 1–4,
5–9, 10–14, 15–19 e 20, o que deixava **cinco níveis** presos no mesmo Kleos. O
grupo crescia cinco níveis e o encontro justo não mexia. Medido: no nível 9 o
monstro do encontro justo caía em **1,9 rodada**, contra 3 nos níveis vizinhos.

Alinhar os cortes às faixas de Grau resolve sem tocar em nenhum valor:

| Nível | Rodadas com os cortes antigos | Rodadas com os cortes de Grau |
|---|---|---|
| 9 | 1,9 | **3,4** |
| 13 | 2,8 | **3,9** |
| 17 | 2,9 | **3,9** |

Para reproduzir: `sim/forja.py`.

### Onde a escala fica grossa

Nos degraus altos, um passo de Kleos é um salto grande demais. Um trio de nível 5
vence um Kleos 5 em 95% das vezes e um Kleos 6 em 34% — não existe nada no meio.
Isso acontece porque a Tábua cresce cerca de 35% por degrau enquanto o grupo
cresce cerca de 10% por nível.

Quando precisar de um meio-termo, **não invente um Kleos quebrado**: monte o
encontro com criaturas menores somadas, usando as fórmulas da [seção 5](#secao-5). Um Kleos 5
mais um Kleos 2 dá um encontro entre 5 e 6 com muito mais precisão do que
qualquer ajuste na ficha de um monstro só.

### Acima de Kleos 9, a ficção manda

Se um grupo grande de nível alto chegar a somar Kleos 12 ou mais, a conta diz que
eles poderiam enfrentar um deus de igual para igual. Deixe. O que impede isso não
é a matemática, é a [seção 7](#secao-7): **deuses não morrem** — são derrotados, recuam e
guardam rancor. E um Cataclisma não cai por dano nenhum, só pelo Selo.

## 4. A Regra da Moira

Compare a **soma do Kleos de todos os inimigos** com o **Kleos do Grupo**.

| Kleos dos inimigos | O que acontece |
|---|---|
| **metade ou menos** | **Escaramuça.** Gasta recurso, não gasta sangue. |
| **igual** | **Combate justo.** Perigoso de verdade: alguém provavelmente vai a 0 PV. |
| **+1 acima** | **Brutal.** O grupo pode perder. Só use com uma rota de fuga. |
| **+2 ou mais** | **Derrota.** Não é um combate, é uma cena. Trate como tal. |

### Isso foi medido, não estimado

O trio de nível 1 do Livro I (Kleos 3), em 8.000 combates simulados por linha:

| Kleos do inimigo | Vitórias | Rodadas | Heróis de pé no fim |
|---|---|---|---|
| 1 | 100,0% | 1,30 | 2,97 de 3 |
| 2 | 99,5% | 2,08 | 2,59 |
| **3 (justo)** | **82,2%** | **3,54** | **1,58** |
| 4 (brutal) | 23,8% | 4,74 | 0,35 |
| 5 (derrota) | 0,4% | 3,65 | 0,01 |

E um semideus **sozinho** contra um Kleos 1: Guardião vence 95%, Furioso 90%,
Oráculo 64%.

> **Sobre o Oráculo:** um personagem de suporte sozinho vale menos Kleos do que a
> tabela diz. Kleos pressupõe um grupo com alguém que bate e alguém que aguenta.
> Um grupo só de suporte deve contar seu Kleos como um a menos.

Para reproduzir: `sim/kleos.py`.

---

## 5. Somando monstros

Vários inimigos **não** somam direto — e somam para **menos**, não para mais.

O motivo é a economia de ações: o grupo concentra fogo, derruba um inimigo por
vez, e cada inimigo morto para de causar dano para sempre. Um único monstro com o
mesmo total de PV mantém o dano inteiro até o último ponto de vida.

> Eu escrevi a regra oposta na primeira versão deste capítulo. A simulação me
> desmentiu, e o número manda.

### Bando — criaturas de Kleos parecido

> **Kleos do encontro = soma × 3/4**

Vale quando todas as criaturas estão dentro de **um degrau** umas das outras.

| Encontro | Soma | Kleos do encontro |
|---|---|---|
| 3 criaturas de Kleos 1 | 3 | **2** |
| 4 criaturas de Kleos 1 | 4 | **3** |
| 2 criaturas de Kleos 2 | 4 | **3** |
| 6 criaturas de Kleos 1 | 6 | **4,5** |
| 3 criaturas de Kleos 2 | 6 | **4,5** |

### Chefe com lacaios — uma criatura dois ou mais degraus acima

> **Kleos do encontro = Kleos do chefe + metade da soma dos lacaios**

| Encontro | Kleos do encontro |
|---|---|
| 1 de Kleos 3 + 2 de Kleos 1 | 3 + 1 = **4** |
| 1 de Kleos 2 + 3 de Kleos 1 | 2 + 1,5 = **3,5** |
| 1 de Kleos 3 + 4 de Kleos 1 | 3 + 2 = **5** |

**Diferença grande achata.** Ignore lacaios **4 ou mais degraus abaixo** do chefe:
morrem antes de agir e não mudam nada. São cenário.

### As duas fórmulas contra a simulação

8.000 combates por linha, trio de nível 1:

| Encontro | Previsto | Vitórias | Kleos efetivo medido |
|---|---|---|---|
| 3 × Kleos 1 | 2,2 | 96,2% | **2,2** |
| 4 × Kleos 1 | 3,0 | 78,0% | **3,1** |
| 2 × Kleos 2 | 3,0 | 79,8% | **3,0** |
| 2 × Kleos 3 | 4,5 | 4,8% | **4,8** |
| 1 × K2 + 3 × K1 | 3,5 | 47,4% | **3,6** |
| 1 × K3 + 2 × K1 | 4,0 | 25,3% | **4,0** |
| 1 × K3 + 4 × K1 | 5,0 | 1,5% | **5,0** |

Para reproduzir: `sim/kleos.py`.

### Quando o desconto some

O desconto de 3/4 existe porque o grupo consegue **concentrar fogo**. Ele
desaparece quando os inimigos não podem ser derrubados um a um:

- inimigos espalhados pelo mapa, longe demais para focar;
- inimigos que chegam em ondas, um substituindo o outro;
- inimigos que curam ou ressuscitam uns aos outros;
- terreno que impede o grupo de escolher alvos.

Nesses casos, use a **soma direta**. Um bando cercando o grupo num corredor
estreito não é o mesmo bando espalhado por um campo aberto — e essa diferença é
do mapa, não da ficha.

---

## 6. O que Kleos não mede

Kleos mede o combate. Não mede tudo, e três criaturas neste livro provam isso.

**Medusa** é Kleos 5, mas o olhar dela petrifica. Um grupo de nível 1 que não
saiba do espelho morre inteiro contra uma criatura que a tabela diz que eles
quase conseguiriam enfrentar. **Efeitos de derrota instantânea ignoram a escala.**

**A Esfinge** é Kleos 5 e pode nunca rolar iniciativa. O perigo dela é uma
pergunta.

**Um deus** é Kleos 10 e ainda assim é invencível, porque não se mata um deus —
ver a [seção 7](#secao-7).

Quando uma criatura tiver um efeito que possa acabar com um personagem sem
passar por PV, o Mestre deve avisar a mesa por dentro da ficção: a estátua no
jardim, o cheiro de enxofre, o silêncio dos pássaros. **Kleos é uma promessa
sobre dano, não sobre injustiça.**

---

## 7. O que morre e o que não morre

### Kleos 1–8 — Dissolução
Monstros não morrem de verdade. Ao chegar a 0 PV, o corpo se desfaz em **pó
dourado** e a essência escorre para o Tártaro, onde vai se remontando ao longo de
anos ou séculos. Matar um monstro é adiá-lo.

Um monstro que já foi morto pelo mesmo herói antes o reconhece, e volta com
rancor.

### Kleos 9–10 — Derrota, nunca morte
Deuses, titãs e divindades não podem ser mortos por dano. Ao chegar a 0 PV,
escolha o que a ficção pedir:

- o deus recua, ferido e humilhado;
- é forçado a conceder alguma coisa — uma resposta, uma passagem, um juramento;
- perde a forma física por uma temporada e some do tabuleiro;
- é aprisionado, se houver como.

Um deus derrotado **lembra**. Ganhar essa luta cria um inimigo que não morre.

### Kleos 11 — Selamento
Um Cataclisma não é derrotado por PV. Reduzi-lo a 0 apenas o deixa **exposto** —
e a partir daí ele só pode ser **selado**, através de uma condição de história
que o Mestre define desde o início e que os jogadores precisam descobrir.

Tifão foi enterrado sob o Etna. Cronos foi cortado em pedaços e espalhado. Gaia
foi devolvida ao sono. Nenhum deles morreu.

**A regra:** todo Cataclisma tem um **Selo** escrito na ficha. Sem cumprir o
Selo, o dano só o mantém ocupado.

---

## 8. Recompensa

O Kleos de um inimigo derrotado é a medida da recompensa: experiência, favores,
reputação, atenção divina.

| Kleos vencido | O que o mundo faz |
|---|---|
| 1–2 | nada muda |
| 3–4 | alguém no acampamento sabe o seu nome |
| 5–6 | um deus menor repara em você |
| 7–8 | um Olimpiano repara em você — e nem sempre com gratidão |
| 9–10 | seu nome entra numa profecia |
| 11 | o mundo continua existindo. É o suficiente. |

Nos Interlúdios (Livro I, Parte VIII), o Mestre pode conceder **uma Ação de
Interlúdio extra** ao grupo que tenha derrubado algo de Kleos igual ou superior
ao próprio Kleos do grupo.

### O que se leva do corpo

Monstro não carrega carteira. O que ele deixa é **matéria** — e é dela que sai a
economia do Livro I: dracmas para comprar, material para forjar.

| Kleos vencido | Dracmas para o grupo | Material |
|---|---|---|
| 1–2 | 1d6 | nada aproveitável |
| 3–4 | 3d6 | um componente comum: couro, presa, glândula |
| 5–6 | 5d10 | **material mítico** — serve para forjar item Mítico |
| 7–8 | 10d10 | material mítico, e um pedaço com nome próprio |
| 9–10 | 20d10 | **material lendário** — serve para forjar item Lendário |
| 11 | não se saqueia um Cataclisma | o que sobrar é relíquia, e tem dono |

**Isso é o total do grupo, não de cada um.** Divida como a mesa preferir.

Os valores foram tirados de trás para frente, a partir dos preços do Capítulo de
Itens: quatro encontros de Kleos 5 rendem cerca de **125 dracmas**, o bastante
para um item **Consagrado**, que custa de 80 a 250 — exatamente o Grau que um
grupo de nível 3 a 5 deveria estar comprando. Quatro encontros de Kleos 9 rendem
cerca de 440 dracmas, contra os 300 a 700 de um **Heroico**.

**Vender material mítico é possível e é burrice.** Um comprador paga metade do
preço do item que aquele material forjaria. Quem vende a pele do leão compra uma
espada; quem a guarda veste a pele.

**Um monstro só rende uma vez.** Um bando de seis capangas de Kleos 1 não rende
seis vezes 1d6 — rende o que a soma deles valia como encontro
([seção 5](#secao-5)). O saque acompanha o **Kleos do encontro**, não a contagem
de corpos.

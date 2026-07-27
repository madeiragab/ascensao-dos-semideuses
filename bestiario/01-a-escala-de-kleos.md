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

Cada semideus vale um tanto de Kleos, de acordo com o nível.

| Nível do personagem | Kleos que ele vale |
|---|---|
| 1–4 | **1** |
| 5–9 | **2** |
| 10–14 | **3** |
| 15–20 | **4** |

O **Kleos do Grupo** é a soma. Quatro personagens de nível 3 valem Kleos 4. Os
mesmos quatro no nível 17 valem Kleos 16.

**Aliados contam.** Um deus que luta ao seu lado soma o Kleos dele. É por isso
que existem alianças na mitologia — e é assim que um Cataclisma vira um problema
resolvível.

---

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
ver a seção 7.

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

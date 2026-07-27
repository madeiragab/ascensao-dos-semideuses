# Ascensão dos Semideuses — Livro II: Bestiário

Livro independente. Traz a escala de perigo do sistema, o motor de criação de
monstros e 38 criaturas prontas.

Pressupõe o Livro I (regras de combate, condições, Névoa, descanso), mas pode ser
lido sozinho por um Mestre que só queira as criaturas.

---

## Os quatro capítulos

| Arquivo | Conteúdo |
|---|---|
| [01-a-escala-de-kleos.md](01-a-escala-de-kleos.md) | O que é Kleos, os onze degraus, a Regra da Moira, como montar encontros, o que morre e o que não morre |
| [02-forja-de-monstros.md](02-forja-de-monstros.md) | Motor de criação: Tábua de Kleos, Arquétipos, Traços, Poderes, Arremetidas, Recusas, Fraqueza Mítica |
| [03-criaturas-kleos-1-a-5.md](03-criaturas-kleos-1-a-5.md) | 20 criaturas, do sátiro errante à Medusa |
| [04-criaturas-kleos-6-a-11.md](04-criaturas-kleos-6-a-11.md) | 18 criaturas, da Quimera a Gaia |

---

## A ideia em um parágrafo

**Kleos** (κλέος) era a glória que sobrevive ao herói. Aqui, o Kleos de uma
criatura mede quanta glória custa derrubá-la — e, porque glória e perigo são a
mesma moeda, quantos semideuses são necessários para sobreviver a ela.

> **Uma criatura de Kleos N é um combate justo e perigoso para N semideuses.**

Kleos 1 é um sátiro bandoleiro. Kleos 4 é o Minotauro. Kleos 10 é um deus
olímpico. Kleos 11 é Tifão, e não é para ser vencido por semideuses sozinhos.

Os onze degraus têm nome, porque ninguém deveria precisar dizer "monstro de
dificuldade 6" numa mesa:

**Rumor · Boato · Conto · Façanha · Feito · Canção · Lenda · Mito · Epopeia ·
Teomaquia · Cataclisma**

---

## O que este livro faz diferente

**Toda criatura tem uma Fraqueza Mítica.** Não é decoração: é o motivo de existir
uma cena de investigação antes da cena de luta. A Hidra é impossível sem fogo. O
Leão de Neméia é imune a armas. Cérbero quer brincar com uma bola. Descobrir isso
é jogar.

**O que morre e o que não morre.** Monstros de Kleos 1–8 viram pó dourado e se
remontam no Tártaro. Deuses (9–10) não podem ser mortos, só derrotados —
recuam, concedem, guardam rancor. Cataclismas (11) precisam de um **Selo**: uma
condição de história que o dano sozinho nunca cumpre.

**Kleos não mede tudo, e o livro admite isso.** Medusa é Kleos 5 e pode acabar
com um grupo inteiro pela petrificação. A Esfinge pode nunca rolar iniciativa. A
seção 6 trata disso de frente.

---

## Como montar um encontro

1. Some o **Kleos do Grupo**: cada personagem vale 1 (níveis 1–4), 2 (5–9),
   3 (10–14) ou 4 (15–20). Aliados contam.
2. Monte os inimigos e calcule o **Kleos do encontro**:
   - **Bando** (criaturas de Kleos parecido): soma × **3/4**
   - **Chefe com lacaios**: Kleos do chefe + **metade** da soma dos lacaios
3. Compare:

| Kleos do encontro | O que acontece |
|---|---|
| metade ou menos | escaramuça |
| igual | combate justo — alguém provavelmente cai |
| +1 | brutal — o grupo pode perder |
| +2 ou mais | derrota; trate como cena, não como luta |

---

## Isto foi medido

Nada aqui é chute. A escala inteira foi validada em `../sim/kleos.py`, contra o
trio de nível 1 do Livro I.

```bash
cd ../sim && python kleos.py
```

Trio de nível 1 (Kleos do Grupo = 3), 8.000 combates por linha:

| Kleos do inimigo | Vitórias | Heróis de pé |
|---|---|---|
| 1 · Rumor | 100,0% | 2,97 de 3 |
| 2 · Boato | 99,5% | 2,59 |
| **3 · Conto (justo)** | **82,2%** | **1,58** |
| 4 · Façanha (brutal) | 23,8% | 0,35 |
| 5 · Feito (derrota) | 0,4% | 0,01 |

E as fórmulas de encontro erram no máximo **0,3** numa escala de 11.

> A primeira versão da seção 5 dizia que muitos inimigos fracos valiam **mais**
> que a soma. A simulação mostrou o contrário — o grupo concentra fogo e cada
> morto para de causar dano para sempre. A regra foi reescrita segundo o dado.

---

## Limites conhecidos

- **O simulador não modela Arremetidas, Recusas nem Poderes.** Ele valida a Tábua
  de Kleos na sua forma crua: PV, DEF, ataque e dano. Uma criatura completa do
  bestiário é **mais perigosa** que a versão testada — o que significa que os
  degraus 6+ têm margem de erro maior que os degraus 1–5.
- **A escala foi calibrada no nível 1.** Kleos 6 a 11 são extrapolação da mesma
  curva. Quando o Livro I tiver progressão de nível, isso precisa ser refeito
  contra grupos de nível alto.
- **Condições não são simuladas**, então criaturas de controle (Esfinge, Basilisco,
  Medusa) são mais perigosas na mesa do que na simulação.

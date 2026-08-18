# Ascensão dos Semideuses — mapa do sistema

> Consulta rápida da revisão de mesa: [`regras-universais.md`](regras-universais.md).

Estado de tudo que existe, o que está pronto e o que falta. Este arquivo é o
índice de trabalho: quando um capítulo é escrito, ele muda de estado aqui.

**Legenda:** ✅ pronto · 🟡 existe mas tem buraco · 🔴 falta escrever · ⚙️ precisa de conserto numérico

---

## Onde o material está hoje

| Origem | Conteúdo | Situação |
|---|---|---|
| Google Doc | Seções 1–32 | é a fonte oficial |
| Conversa do ChatGPT | Seções 33–51 (Itens e Criação) | **só existe no link, precisa entrar no Doc** |
| `regras/v1-numeros.md` | Correções de balanceamento | proposta, aguardando sua decisão |
| `regras/combate.md` | Parte III completa | novo |
| `regras/magia-da-nevoa.md` | Parte V completa | novo |
| `regras/interludio.md` | Parte VIII completa | novo |

O primeiro trabalho de organização é **colar as seções 33–51 no Google Doc**.
Enquanto elas viverem só num link de conversa, o livro está incompleto e nada
garante que continuem existindo.

---

## Estrutura proposta

O livro hoje tem uma numeração corrida de 1 a 51, com um segundo bloco de
numeração interna dentro do capítulo de habilidades (1 a 24). Isso já está
difícil de navegar e vai piorar. A proposta é agrupar em Partes e renumerar uma
vez só, agora, enquanto o livro ainda é pequeno.

### Parte I — O Personagem

| # | Capítulo | Estado |
|---|---|---|
| 1 | Criação de personagem (ordem das etapas) | ✅ |
| 2 | Atributos e modificadores | ✅ |
| 3 | Conceito Mortal | ✅ |
| 4 | Húbris | ✅ Provocação, Ímpeto e Ruptura, no Capítulo Oito |
| 5 | Classes: Guardião, Furioso, Oráculo | ✅ recursos refeitos e medidos em `sim/equilibrio.py` |
| 6 | Perícias | ✅ |
| 7 | Defesas passivas | ✅ Fortitude, Reflexos e Vontade treinadas por classe |
| 8 | Parente Divino | ✅ |
| 9 | Atributo Divino | ✅ alimenta MP e Memória |
| 10 | Finalização | ✅ |
| 11 | Progressão de nível 1–20 | ✅ Capítulo Nove, do nível 1 ao 20 |

### Parte II — Regras Fundamentais

| # | Capítulo | Estado |
|---|---|---|
| 12 | A rolagem básica | ✅ |
| 13 | Classes de Dificuldade | ✅ tabela no Guia do Mestre, exemplos no Livro I |
| 14 | Vantagem e Desvantagem | ✅ |
| 15 | Recursos: PV, SP, MP | ✅ recuperação no Capítulo Oito |
| 16 | Defesa | ✅ armaduras e escudos no Capítulo Quatro |

### Parte III — Combate → `combate.md`

| # | Capítulo | Estado |
|---|---|---|
| 17 | Iniciativa e surpresa | ✅ novo |
| 18 | Estrutura do turno | ✅ |
| 19 | Movimento, terreno e queda | ✅ novo |
| 20 | Lista de ações | ✅ novo |
| 21 | Ataques, dano e crítico | ✅ |
| 22 | Cobertura e visibilidade | ✅ novo |
| 23 | Ataques de oportunidade | ✅ novo |
| 24 | Agarrar, empurrar e escalar criaturas | ✅ novo |
| 25 | Condições | ✅ novo — **eram citadas sem nunca serem definidas** |
| 26 | 0 PV, agonia e morte | ✅ novo — **não existia nenhuma regra** |

### Parte IV — Habilidades

| # | Capítulo | Estado |
|---|---|---|
| 27 | Afinidade e manifestação livre | ✅ |
| 28 | Memória | ✅ usa o Atributo Divino |
| 29 | Fontes: Elemental, Física, Híbrida, Médica | ✅ |
| 30 | Graus, custos e efeitos adicionais | ✅ ponto custa o Grau e entrega o Grau, medido em `sim/graus.py` |
| 31 | Dano, condições, buffs, movimento, defesa | ✅ |
| 32 | Passivas e Sacrifício de Atributo | ✅ −1 no atributo **e** −1 no recurso: o custo nunca é zero |
| 33 | Cura, Ressonância e PV temporários | ✅ |

### Parte V — Magia da Névoa → `magia-da-nevoa.md`

> ⚠️ **Fora do Livro do Jogador.** Em 27/07/2026 o usuário pediu para tirar toda
> menção à Névoa do Livro do Jogador. O sistema continua escrito e válido aqui,
> mas não é conteúdo de jogador — vai para outro livro, ou para um capítulo
> avançado. O lugar dele no Livro do Jogador foi ocupado pelo **motor completo de
> criação de habilidades** (pontos, alcance, duração, passivas), testado em
> `sim/habilidades.py`.
>
> O **Sacrifício de Atributo** do item 6 de `v1-numeros.md` está superado: a
> regra nova é −1 no valor de Inteligência ou Constituição **e** −1 no máximo do
> recurso que aquele atributo alimenta, o que garante que o custo nunca seja zero.

| # | Capítulo | Estado |
|---|---|---|
| 34 | O que é a Névoa | ✅ novo |
| 35 | Iniciação: como se torna conjurador | ✅ novo |
| 36 | Repositório e Fórmulas | ✅ novo |
| 37 | Conjuração: custo, componentes, Círculos | ✅ novo |
| 38 | Descrença | ✅ novo |
| 39 | Fórmulas iniciais | ✅ novo |
| 40 | Criando novas Fórmulas | ✅ novo |

### Parte VI — Equipamento

| # | Capítulo | Estado |
|---|---|---|
| 41 | Carga narrativa | ✅ |
| 42 | Armas e propriedades | ✅ |
| 43 | Criação de armas | ✅ |
| 44 | Armaduras e escudos | ✅ tabela completa, medida em `sim/equilibrio.py` |
| 45 | Materiais sobrenaturais | 🔴 citado como "será desenvolvido" |
| 46 | Dinheiro e preços | ✅ óbolo, dracma, mina e talento, com o que se ganha por dia |

### Parte VII — A Forja → `criacao-de-itens.md`

| # | Capítulo | Estado |
|---|---|---|
| 47 | O que o Grau do item dá | ✅ novo — dado de arma e DEF por Grau, medido em `sim/forja.py` |
| 48 | Cargas | ✅ novo — iguais à proficiência, como os Tratamentos |
| 49 | Forjar: Manufatura contra CD 10 + pontos | ✅ novo — a mesma fórmula de criar habilidade |
| 50 | Materiais míticos | ✅ novo — liga a forja ao Livro II |
| 51 | Aprimoramentos | ✅ novo — comprados com os pontos do Capítulo Sete |
| 52 | Melhorar, reparar, desmontar | ✅ novo |
| 53 | Integridade em jogo | ✅ novo — a falha da forja marca a peça, não o ferreiro |

### Parte VIII — Entre Aventuras → `interludio.md`

| # | Capítulo | Estado |
|---|---|---|
| 54 | Descanso e recuperação de recursos | ✅ novo — **era a lacuna mais urgente do livro** |
| 55 | Refeições | ✅ novo |
| 56 | O Interlúdio e as Ações de Interlúdio | ✅ novo |
| 57 | Atividades de Interlúdio | ✅ novo |
| 58 | Húbris: Provocação e Ruptura | ✅ novo — dá mecânica ao defeito fatal |

### Parte IX — O Mestre

| # | Capítulo | Estado |
|---|---|---|
| 59 | Bestiário | ✅ **virou o Livro II** — ver `bestiario/` |
| 60 | Montagem de encontros | ✅ Livro II, seções 4 e 5 |
| 61 | Recompensas | 🟡 Livro II, seção 8 — falta economia de dracmas |
| 62 | Tom, Névoa e o mundo mortal | 🔴 |
| 63 | Progressão de nível e ganho de experiência | 🔴 |

### A Fera Vinculada → **Livro II, Parte V** (`bestiario/05-a-fera-vinculada.md`)

Domar mora no Bestiário, e não aqui, porque a fera é um bloco deste livro com
três cortes — não uma peça nova do Livro I.

| # | Capítulo | Estado |
|---|---|---|
| 22 | Que criatura pode ser domada | ✅ novo |
| 23 | Poupar, Provar, Selar | ✅ novo |
| 24 | A ficha da fera | ✅ novo — deriva do bloco do Livro II |
| 25 | A fera em combate | ✅ novo — ela gasta o turno do dono |
| 26 | Quando ela cai | ✅ novo |

---

## Livro II — Bestiário

Livro separado, em `bestiario/`. Traz a **Escala de Kleos** (11 degraus, de Rumor
a Cataclisma), o motor de criação de monstros e 38 criaturas prontas. A escala foi
validada em `sim/kleos.py`.

O Livro I depende dele em dois pontos: a recompensa dos Interlúdios, e o fato de
que sem monstros não havia como calibrar nada.

---

## As dívidas que mais travam o livro

*(revisado em 16/08/2026, medindo o livro montado — as quatro dívidas antigas
foram todas pagas: Bestiário, progressão de nível, armaduras e economia.)*

1. ~~**O dano de arma não acompanha o PV dos monstros.**~~ ✅ Resolvido pelo
   **Grau do item** (Parte VII, seção 47): o item dá dados de arma e DEF por
   Grau, de graça. Sem ele, o trio de nível 20 levava 11,5 rodadas e perdia uma
   luta em cada três; com ele, o combate dura de 2 a 4 rodadas do nível 3 ao 20.
   Travado em `sim/forja.py`, que roda na regressão.
2. ~~**O crítico apaga o encontro em qualquer nível.**~~ ✅ Um Ataque de
   Habilidade crítico soma **dados iguais ao Grau** em vez de dobrar. Das quatro
   regras medidas, é a que menos deixa o crítico decidir a luta: pior caso de
   **83%** dos PV do monstro justo, contra 139% dobrando e 105% somando metade.
3. ~~**A DEF do personagem estagna.**~~ ✅ A coluna de DEF do Grau do item segura
   o monstro entre 45% e 60% de acerto nos 20 níveis, no lugar dos 70% do nível
   15 em diante.
4. ~~**O platô de Kleos entre os níveis 5 e 9.**~~ ✅ Os valores estavam certos e
   os **cortes** estavam errados: as faixas 1–4, 5–9, 10–14, 15–19 e 20 prendiam
   cinco níveis no mesmo Kleos, e no nível 9 o monstro caía em 1,9 rodada. As
   faixas passam a ser **as mesmas do Grau** — 1–4, 5–8, 9–12, 13–16, 17–20 —
   sem mexer em nenhum valor. Nível 9 vai de 1,9 para 3,4 rodadas; 13 de 2,8
   para 3,9; 17 de 2,9 para 3,9.

5. ~~**O simulador não modela Poderes nem Arremetidas.**~~ ✅ `sim/criaturas.py`
   ensina o motor a usar **Poder de área com Recarga** e **Arremetidas**, e mede
   o que elas valem: uma criatura completa dá o mesmo trabalho que uma crua **um
   degrau acima** — o Livro II agora manda contar o chefe como Kleos +1. O Sopro
   é o que derruba a vitória do grupo (100% → 76%); a Arremetida quase não muda
   quem vence, mas leva os heróis de pé de 2,1 para 1,2.

**A dívida que sobrou:** **Recusas** continuam fora da conta. Elas anulam uma
Rolagem de Efeito, e os heróis do simulador só atacam — não existe Efeito para
recusar. Medir Recusa exige antes ensinar o motor a usar controle do lado dos
jogadores, e esse é o próximo passo do `sim/`.

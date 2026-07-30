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
| 4 | Húbris | 🟡 sem mecânica — proposta em `interludio.md` |
| 5 | Classes: Guardião, Furioso, Oráculo | ⚙️ recursos quebrados, ver `v1-numeros.md` |
| 6 | Perícias | ✅ |
| 7 | Testes de Resistência | ⚙️ ninguém é proficiente em Reflexos |
| 8 | Parente Divino | ✅ |
| 9 | Atributo Divino | 🟡 existe em 4.2 mas não é usado por MP nem Memória |
| 10 | Finalização | ✅ |
| 11 | Progressão de nível 1–20 | 🔴 **só existe o bônus de proficiência** |

### Parte II — Regras Fundamentais

| # | Capítulo | Estado |
|---|---|---|
| 12 | A rolagem básica | ✅ |
| 13 | Classes de Dificuldade | 🔴 o livro diz "ainda não definidas" — proposta em `combate.md` |
| 14 | Vantagem e Desvantagem | ✅ |
| 15 | Recursos: PV, SP, MP | 🟡 sem regra de recuperação — resolvido em `interludio.md` |
| 16 | Defesa | 🟡 armaduras não existem — tabela provisória em `v1-numeros.md` |

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
| 28 | Memória | ⚙️ usa INT em vez do Atributo Divino |
| 29 | Fontes: Elemental, Física, Híbrida, Médica | ✅ |
| 30 | Níveis, custos e efeitos adicionais | ⚙️ nível 1 custa caro demais |
| 31 | Dano, condições, buffs, movimento, defesa | ✅ |
| 32 | Passivas e Sacrifício de Atributo | ⚙️ o sacrifício se auto-anula |
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
| 44 | Armaduras e escudos | 🔴 **três classes têm proficiência em algo que não existe** |
| 45 | Materiais sobrenaturais | 🔴 citado como "será desenvolvido" |
| 46 | Dinheiro e preços | 🔴 nada existe |

### Parte VII — Itens e Criação (seções 33–51 atuais)

| # | Capítulo | Estado |
|---|---|---|
| 47 | Categorias de itens | ✅ (fora do Doc) |
| 48 | Classe de Qualidade | ✅ (fora do Doc) |
| 49 | Kits de Criação | ✅ (fora do Doc) |
| 50 | Teste de criação, progresso e complicações | ✅ (fora do Doc) |
| 51 | Aprimoramentos | ✅ (fora do Doc) |
| 52 | Integridade, quebra e reparos | ✅ (fora do Doc) |
| 53 | Desmontar e aprender projetos | ✅ (fora do Doc) |

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

---

## Livro II — Bestiário

Livro separado, em `bestiario/`. Traz a **Escala de Kleos** (11 degraus, de Rumor
a Cataclisma), o motor de criação de monstros e 38 criaturas prontas. A escala foi
validada em `sim/kleos.py`.

O Livro I depende dele em dois pontos: a recompensa dos Interlúdios, e o fato de
que sem monstros não havia como calibrar nada.

---

## As dívidas que mais travam o livro

1. ~~**Bestiário.**~~ ✅ Resolvido pelo Livro II.
2. **Progressão de nível.** O livro tem personagens de nível 1 e uma tabela de
   proficiência até o 20, e nada no meio. Habilidades de Círculo 4 custam 9 MP
   com um pool inicial de 10, e exigem nível 15 — um nível que não existe.
   **Agora é a dívida número um**, e trava o Livro II também: a Escala de Kleos
   foi calibrada só no nível 1, e os degraus 6 a 11 são extrapolação.
3. **Armaduras.** Escritas como proficiência de classe, nunca escritas como
   equipamento. A tabela provisória está em `v1-numeros.md`, item 3.
4. **Economia.** Dracmas, preços, quanto custa um Kit de Criação. O sistema de
   itens pressupõe compras que não têm preço.

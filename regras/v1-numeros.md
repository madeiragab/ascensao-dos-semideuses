# Proposta v1 — correção dos números

Cada mudança abaixo foi testada em `sim/`. Rode `python comparar.py` de dentro
da pasta `sim/` para reproduzir todas as tabelas citadas.

---

## 1. Recursos das classes (nível 1)

**Problema.** O Guardião, classe defensiva, tem 6 + CON de PV — menos que o
Oráculo (8) e o Furioso (10). Somando os três recursos ele também tem o menor
total do jogo. A classe defensiva é a mais frágil.

**Proposta.** Total de 32 pontos de recurso para as três classes, distribuídos
segundo a identidade de cada uma:

| Classe | PV | SP | MP |
|---|---|---|---|
| Guardião | **14** + CON | **12** + CON | **6** + DIV |
| Furioso | **12** + CON | **14** + CON | **6** + DIV |
| Oráculo | **10** + CON | **8** + CON | **14** + DIV |

`DIV` = modificador do **Atributo Divino** (ver item 2).

Com a distribuição padrão isso dá: Guardião 16/14/7, Furioso 14/16/7,
Oráculo 11/9/17.

---

## 2. MP e Memória usam o Atributo Divino, não Inteligência

**Problema.** A seção 4.2 deixa o jogador escolher Inteligência, Sabedoria ou
Carisma como Atributo Divino — mas o MP máximo e a Memória (seção 2) são
calculados com Inteligência fixa. Quem escolhe Sabedoria ou Carisma acerta com
um atributo e tem combustível de outro, e é obrigado a investir nos dois.

**Proposta.** Trocar "modificador de Inteligência" por "modificador do Atributo
Divino" em:

- MP máximo das três classes;
- `Memória = 2 + modificador do Atributo Divino` (seção 2).

---

## 3. Armaduras (provisório, mas necessário agora)

**Problema.** As três classes têm proficiência em armaduras, e nenhuma armadura
existe no livro. Resultado: DEF = 10 + DES para todos, ou seja, DEF 11 para os
três personagens de teste. Sem isso o Guardião não tem como ser defensivo.

**Proposta provisória.**

| Armadura | Categoria | DEF | Limite de DES |
|---|---|---|---|
| Acolchoada | Leve | 11 + DES | — |
| Couro batido | Leve | 12 + DES | — |
| Cota de escamas | Média | 13 + DES | +2 |
| Peitoral | Média | 14 + DES | +2 |
| Escudo | — | +2 DEF | — |

Sem armadura continua sendo 10 + DES (seção 16).

Efeito nos personagens de teste: Guardião (peitoral + escudo) DEF **17**,
Furioso (couro batido) DEF **13**, Oráculo (couro batido) DEF **13**.

---

## 4. Ataque Feroz e Ataque Pesado

**Problema.** As seções 25 e 29 dizem explicitamente que as duas técnicas podem
ser combinadas. Isso quebra a matemática: a Vantagem grátis do Ataque Feroz
paga a penalidade do Ataque Pesado, e a combinação vira +43% de dano contra
DEF 11 e ainda +22% contra DEF 18. Não existe situação em que não usar os dois
seja correto — a decisão não existe.

A varredura em `experimentos.py` (item 9) mostra que **nenhum par −X/+Y
consegue gerar decisão enquanto a Vantagem estiver grátis no mesmo ataque**.
O conserto tem que ser estrutural, não de número.

**Proposta.**

> **Ataque Feroz.** Uma vez por turno, ao realizar seu primeiro ataque, o
> Furioso pode declarar um Ataque Feroz. O ataque é realizado com Vantagem, e
> **o próximo ataque feito contra o Furioso** antes do início do próximo turno
> dele também possui Vantagem. Não custa SP.
>
> **Ataque Pesado.** Antes de realizar um ataque corpo a corpo com uma arma na
> qual seja proficiente, o personagem pode gastar **1 SP** para declarar um
> Ataque Pesado. O ataque recebe **−2 na rolagem** e, se acertar, **soma um
> dado de dano extra da arma**.
>
> **Ataque Feroz e Ataque Pesado não podem ser usados no mesmo ataque.**

Duas mudanças além da proibição:

- A penalidade do Feroz passa a valer para **um** ataque, não para todos. Antes
  ela era quase gratuita em duelo e brutal contra quatro inimigos — escalava com
  algo que o jogador não controla.
- O bônus do Pesado deixa de ser +5 fixo e passa a ser **um dado da arma**.
  Assim ele escala com o peso da arma (machado grande +1d10, espada curta +1d6)
  em vez de premiar igualmente quem usa adaga.

**Resultado medido** (Furioso nível 1, machado grande, ataque +5):

| DEF do alvo | Feroz | Pesado | melhor |
|---|---|---|---|
| 11 | 8,97 | **10,28** | Pesado |
| 12 | 8,72 | **9,54** | Pesado |
| 13 | 8,43 | **8,79** | Pesado |
| 14 | **8,10** | 8,04 | Feroz |
| 15 | **7,72** | 7,30 | Feroz |
| 18 | **6,31** | 5,07 | Feroz |

Ataque Pesado contra alvo lento ou blindado, Ataque Feroz contra alvo ágil.
Agora existe uma decisão que depende de olhar o inimigo.

---

## 5. Custo das habilidades de nível 1

**Problema.** Uma habilidade de nível 1 custa 2 MP e causa 1d8 + modificador —
exatamente o dano de uma espada longa, que é grátis. Gastar recurso não compra
poder nenhum, só compra alcance e tipo elemental.

**Proposta.** Custo-base do nível 1 passa de 2 para **1 MP**. Os níveis 2, 3 e 4
continuam em 4, 6 e 9.

Efeito: o Oráculo de teste sai de 6 usos por dia para 17, e habilidade elemental
vira a ação padrão de quem investiu no Atributo Divino, como deveria ser.

*Alternativa, se preferir manter o custo:* subir o dano de nível 1 para 2d6 +
modificador. Prefiro mexer no custo — é um número só e não desalinha a tabela
de dano com a de PV temporários.

---

## 6. Sacrifício de Atributo (passivas, seção 17.1)

**Problema.** O sacrifício de −2 no valor de um atributo se anula contra o
próprio benefício da passiva:

| Passiva | Efeito | Sacrifício | Resultado real |
|---|---|---|---|
| Pele de Pedra | +1 DEF | −2 DES (13→11) | mod DES cai +1→+0, **DEF líquida 0**, e perde Reflexos, Iniciativa e Acrobacia |
| Passos Ligeiros | +1,5 m | −2 CON (15→13) | −1 PV máximo e −1 em Fortitude |
| Força das Profundezas | +1 Atletismo | −2 INT (12→10) | −1 de Memória, ou seja, o espaço da própria passiva |

Nenhuma das três passivas do exemplo é vantajosa. São armadilhas.

**Proposta.**

> **Sacrifício de Atributo.** Enquanto a habilidade passiva estiver preparada, o
> personagem sofre **−1 no modificador** de um atributo relacionado.
>
> O atributo sacrificado:
> - deve ter relação narrativa com a passiva;
> - **não pode ser o atributo que a passiva melhora**;
> - **não pode alimentar o mesmo valor derivado que a passiva melhora** (não
>   pague uma passiva de DEF com Destreza, nem uma de PV com Constituição);
> - não pode ser escolhido apenas por ser pouco utilizado.

Exemplos corrigidos: Pele de Pedra (+1 DEF) paga com −1 Carisma; Passos
Ligeiros (+1,5 m) paga com −1 Força.

---

## 7. Proficiências em Testes de Resistência

**Problema.** Guardião e Furioso são proficientes em Fortitude, Oráculo em
Vontade. **Ninguém é proficiente em Reflexos** — que é justamente a resistência
usada pelo dano em área, o padrão das habilidades ofensivas (seção 12.2).

**Proposta.** Duas resistências por classe, cobrindo as três:

| Classe | Resistências |
|---|---|
| Guardião | Fortitude e Vontade |
| Furioso | Fortitude e Reflexos |
| Oráculo | Vontade e Reflexos |

---

## 8. Investida Imprudente (técnica morta)

**Problema.** Custa 2 SP para dar Vantagem em um ataque corpo a corpo, depois de
mover 6 metros em linha reta. O Ataque Feroz dá Vantagem de graça, todo turno,
sem condição de movimento. Ninguém escolhe essa técnica.

**Proposta.** Trocar o efeito para algo que o Ataque Feroz não faz:

> **Investida Imprudente.** Após se mover pelo menos 6 metros em linha reta até
> um alvo, o personagem pode gastar 2 SP para atacar. Se acertar, o alvo é
> empurrado 3 metros e precisa passar em um Teste de Fortitude (CD 8 + mod de
> Força + proficiência) ou cai derrubado.

---

## 9. Contradição da arma dupla

**Problema.** A seção 32.12 exige que uma arma dupla use **duas mãos** e possua
a propriedade **Leve**. A seção 32.8 exige que Leve seja usada com **uma mão**.
É impossível construir uma arma dupla legal.

**Proposta.** Tirar a exigência de Leve e escrever a regra direto:

> **Armas duplas.** Uma arma dupla usa duas mãos, é Marcial e causa no máximo
> 1d6 em cada extremidade. Ela **não possui** a propriedade Leve, mas satisfaz
> os requisitos de Combate com Duas Armas por si só: o personagem pode usar sua
> Ação Bônus para atacar com a segunda extremidade, seguindo as regras da
> seção 28.

---

## 10. Bastão e Cajado

São a mesma arma duas vezes na tabela (1d6 Concussão, uma mão, Versátil 1d8).
Juntar em uma entrada só, ou dar ao Cajado uma função de foco de habilidade
quando o capítulo de itens divinos existir.

---

## 11. Besta leve vs Arco curto — não é bug, é dívida

A Besta leve (1d8) supera o Arco curto (1d6) em 16% de dano em toda faixa de
DEF, e as duas são armas simples. A limitação da Recarga só custa algo quando
existe um ataque extra para perder — o que no nível 1 não existe.

Não é preciso mexer na arma **se** a progressão der ataque extra em algum nível
(o padrão é o 5º). Se a decisão for nunca dar ataques extras, a Besta leve
precisa voltar para 1d6.

---

## O que a correção produziu nas simulações

20.000 combates por encontro, trio de nível 1, mesmos monstros nas duas versões:

| Encontro | Vitórias v0 → v1 | Rodadas v0 → v1 | Heróis de pé v0 → v1 |
|---|---|---|---|
| 3 capangas | 95,6% → 98,9% | 2,99 → 3,58 | 2,32 → 2,49 |
| 2 cães do inferno | 96,5% → 99,3% | 2,60 → 3,11 | 2,38 → 2,55 |
| 1 escorpião gigante | 99,5% → 100% | 1,86 → 2,03 | 2,65 → 2,88 |
| 2 empusas | 75,8% → 92,0% | 3,38 → 4,21 | 1,61 → 1,98 |
| 1 minotauro | 42,8% → 70,0% | 2,84 → 3,91 | 0,81 → 1,24 |

E a fatia de dano do Furioso caiu de **68–76%** do total do grupo para
**51–56%**, principalmente porque o Guardião passa a sobreviver o combate
inteiro em vez de cair na segunda rodada.

**Ressalva honesta:** os monstros usados nessas simulações foram inventados por
mim, porque o livro não tem bestiário. As conclusões que **não** dependem deles
são as dos itens 1, 2, 4, 5, 6, 7, 8, 9 e 11 — todas medidas com números que o
próprio livro fornece. As taxas de vitória acima servem para comparar v0 com v1,
não para afirmar qual é a dificuldade "certa" de um encontro.

---

## O que ainda não está resolvido

O Oráculo continua sendo o menor contribuinte de dano (11% do total do grupo).
Isso é aceitável para uma classe de suporte, mas as simulações não contam a cura
que ela distribui — e não contam porque **não existe regra de recuperação de
recursos no livro**, então não há como medir o valor de um PV recuperado contra
o custo de um MP.

O Guardião ainda não tem uma ferramenta ofensiva ou de controle própria:
Postura Desafiadora não tem duração definida, e Interceptar transfere dano sem
reduzi-lo. Isso é a próxima frente de trabalho.

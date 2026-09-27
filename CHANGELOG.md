# Changelog

Todas as mudanças relevantes de **Ascensão dos Semideuses** serão registradas
neste arquivo. O projeto está em beta e usa versionamento semântico a partir desta
revisão.

## [0.19.0] - 2026-09-26

### Briga — a luta sem arma

Saiu do mesmo log da 0.18.0. Na arena do acampamento, numa briga combinada "sem
arma, sem poder", o David (Guardião de nível 10, 98 PV) tirou **20 natural** num
soco — e a regra não tinha resposta. O soco era **1 + FOR**, sem dado; com Força +0,
1 de dano, e "o crítico dobra dados, mas o soco não tem dado para dobrar". O Mestre
inventou na hora que o dano dobrava, e o crítico virou 2. Um semideus de nível 10
socava igual a um de nível 1, para sempre.

- **O punho tem dado.** Ataque desarmado: **1d4 + FOR ou DES** (Fineza), dano de
  concussão, e todo mundo é proficiente. Ele cresce com o nível pela **mesma tabela
  do Grau do item**, com o d4 no lugar do dado da arma: 1d4 no nível 1, +1 no 3,
  **2d4 +1** no 6, **2d4 +2** no 10, **3d4 +2** no 15. Entrega de **62% a 76%** do
  dano de uma arma do mesmo nível — continua sendo o plano B.
- **O crítico desarmado rola os dados duas vezes**, como qualquer arma, **e
  encaixa**: escolha **Caído**, **Sem Ar** (Desprevenido até o início do seu
  próximo turno) ou **Empurrão** (1,5 m, e você ocupa o espaço). O Encaixe não é
  Rolagem de Efeito: não pede rolagem, e Recusa não anula. "A arma dobra mais; o
  punho encaixa."
- **Bloquear** (reação): contra um ataque desarmado que te acertaria, com uma mão
  livre, role 1d20 + o seu ataque desarmado; igualou ou passou o total, bloqueou.
  Crítico não se bloqueia. **Por quê:** sem guarda a briga entre iguais era uma
  corrida — os dois acertam quase todo soco, e quem começa chega primeiro. Medido,
  entre dois Furiosos do mesmo nível, quem vencia a iniciativa ganhava **até 90%**
  das brigas. Com o Bloquear, de **53% a 70%**.
- **Nocaute.** Um ataque desarmado que leva a 0 PV pode nocautear: Inconsciente e
  Estabilizado, sem Agonia, acorda com 1 PV em dez minutos. Com arma corpo a corpo,
  bata de lado ou com o cabo: rola o dano do punho, e pode nocautear.
- **Manobras de briga** num lugar só: Agarrar, Derrubar ou Empurrar, **Desarmar** e
  **Imobilizar**, todas em Atletismo contra Atletismo ou Acrobacia. Sem arma nas
  mãos, uma manobra pode tomar o lugar de um dos ataques da ação de Atacar.
- **Briga combinada**: os termos se combinam antes — **primeira queda**, **até a
  metade** (de 2 a 6 rodadas em qualquer nível) ou **até o nocaute** (de 4 a 11).
  "Sem arma, sem poder" tira habilidade, Poder e item com Carga; **técnica de
  classe vale**, mesmo a que gasta SP.
- A cena do log, refeita: o David de Força +0 levava **8,7 rodadas** para nocautear
  o valentão de Kleos 1; agora, **1,4**. O Livro do Jogador conta a cena num quadro
  de mesa.

### Desprevenido ganha definição

- A condição aparecia como exemplo de condição fraca e na Fúria Cega ("você fica
  Desprevenido"), mas nunca tinha sido definida. Agora está no Capítulo Seis e na
  tabela de consulta: **ataques contra você têm Vantagem**.

### Outras mudanças

- Arma improvisada passa a **1d6 + FOR**, sem proficiência: com o punho em 1d4 e
  proficiente, a garrafa não podia valer menos que a mão.
- O construtor da ficha escreve a linha do **Punho** sozinho — ataque, dano,
  crítico e o lembrete do Encaixe e do Bloquear — e a folha impressa traz o Punho
  como primeiro ataque.
- O Guia do Mestre ganhou "E quando é briga de mão", com os termos e três
  conselhos.

### Simulador

- `sim/briga.py` mede o punho contra a arma em cada nível, a briga combinada entre
  semideuses do mesmo nível (regra antiga, punho sem guarda e regra nova, até a
  metade e até o nocaute), a cena do log e o crítico desarmado, e confere a tabela
  do punho no Livro do Jogador e na ficha contra o motor. **Falha** se o punho sair
  de 50% a 80% da arma, se a briga até a metade passar de 6 rodadas, se quem
  começa vencer mais de 75% no espelho, ou se um nível 10 levar mais de duas
  rodadas para nocautear um Kleos 1.

## [0.18.0] - 2026-09-26

As três mudanças grandes saíram de uma campanha solo longa — David Davis, Guardião
de Hefesto com Afinidade Fogo, do nível 1 ao 17 em dois logs. As três queixas do
jogador foram medidas antes de virar regra, e o simulador confirmou as três. Uma
delas escondia um erro do próprio simulador.

E a versão fecha a conta que ficou aberta: **nenhuma dívida conhecida** sobra no
simulador. As seis técnicas que mediam acima de 10 pontos foram ajustadas, o duelo
Guardião x Oráculo voltou para a faixa, a Fonte Médica parou de divergir entre
livro e ficha, e o conversor do Bestiário parou de partir fichas de criatura ao
meio.

### O chefe tem Fases

- O **chefe** do encontro — a criatura que luta sozinha, ou a de Kleos mais alto
  num chefe com lacaios — tem o PV dividido em **Fases** iguais: duas no Kleos 2,
  três do 3 ao 7, quatro do 8 em diante. Bando e lacaio não têm.
- **O golpe que quebra uma Fase para no piso dela: o excesso se perde.** Nenhum
  golpe tira duas Fases. **Fase quebrada não volta** com cura nem Regeneração.
- Ao quebrar uma Fase, a criatura **se livra de toda condição** que a afete, e o
  Mestre mostra o que mudou. Os pisos de cada criatura do Bestiário vêm na ficha,
  ao lado do PV.
- **Num duelo entre semideuses, cada um tem duas Fases.**
- O **dano da Tábua de Kleos não mudou.** O número de Fases segura a duração da
  luta; a Tábua segura a vitória.
- **Por quê:** "o sistema depende de status e cenas pras lutas durarem mais". Nos
  logs, quase todo combate acabava num golpe — "Rouge G2, 20", "Impacto Zero G5,
  20" —, e o único chefe que aguentou foi o Ouroboros, porque o Mestre inventou na
  hora que ele desfazia o dano. Medido: uma habilidade no Teto tirava de **50% a
  74%** do PV do chefe do encontro justo, e o trio vencia de **80% a 97%** das vezes
  em **1,8 a 2,1 rodadas**. Com Fases, **56% a 79%** em **2,6 a 3,6 rodadas**.
- **Só o chefe, e isso foi medido.** Com Fase em toda criatura, cinco de Kleos 4
  derrubavam o grupo de nível 12 para **21%** de vitória, contra 69%. O golpe grande
  apagando lacaio é o prêmio de quem o montou.
- **Três Fases por duelista foi medido e piora**: a Oráculo, que depende de poucos
  golpes grandes por dia, fica sem como virar. Com duas, o espelho do Furioso cai
  de **77%** para quem começa para **63% a 71%**.

### A tabela de Kleos do Grupo, de um a seis jogadores

| Nível | 1 herói | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| 1–4 | 2 | 3 | 3 | 3 | 4 | 4 |
| 5–8 | 3 | 5 | 5 | 6 | 7 | 7 |
| 9–12 | 5 | 7 | 7 | 8 | 8 | 8 |
| 13–16 | 6 | 8 | 8 | 9 | 10 | 10 |
| 17–20 | 7 | 9 | 9 | 10 | 10 | 10 |

- O **trio não mudou**. A dupla aguenta o degrau do trio, o quarto jogador vale +1
  do nível 5 em diante. Sem o golpe que apagava o chefe, cada jogador a mais passou
  a contar.
- A coluna de **um herói** é o chefe de uma mesa solo. Substitui a regra da 0.17.1
  ("conte o herói como Kleos 2 no clímax"), que continua valendo no nível 1.
- Medido na média das duas pontas de cada faixa, de um a quatro jogadores: o
  encontro justo vence de **54% a 90%**. Mesas de quatro terminam mais cedo (2,1 a
  2,7 rodadas) — mais gente quebra Fase mais depressa. Uma Fase extra para mesa
  grande foi medida e rende só +0,4 rodada; ficou de fora.

### O simulador rolava o golpe dos marciais no atributo errado

- `sim/completo.py` rolava o golpe Físico do Guardião e do Furioso com o Atributo
  Divino (Sabedoria +1). O Livro I paga habilidade Física com **Força ou
  Destreza** (+5). Acertava 45% em vez de 70%.
- Corrigido, o encontro justo "de 2,4 a 3,1 rodadas" do README durava **1,8** —
  era o que a mesa dizia, e o simulador não via. Foi o erro que escondeu por meses
  que o chefe caía num golpe.
- Tudo que usa esses heróis foi medido de novo: `completo.py`, `defesa.py`,
  `aliado.py`, `nevoa.py`, `duelo.py`.

### O Grau fica gravado na habilidade

- Toda habilidade tem o **Grau dela**, escolhido quando ela nasce (qualquer um até
  o do personagem). Na hora de usar, cada ponto é pago **no Grau dela ou abaixo**,
  nunca acima. O Teto que vale é o do Grau da habilidade.
- Para subir, a habilidade é **aprimorada**: uma Ação de Interlúdio, o mesmo teste
  de desenvolver, contra a CD da versão nova. Pode ser remontada dentro do Teto
  novo.
- A **Habilidade Assinatura sobe sozinha**, sem Ação nem teste, a cada Grau novo.
  Habilidade que nasce na criação do personagem nasce no Grau dele, sem teste.
- A CD de desenvolver ou aprimorar passa a ser **10 + pontos + 1 por Grau acima do
  primeiro**. No Grau 1 é a mesma de antes.
- **Por quê:** a regra dizia "você pode comprar um ponto em qualquer Grau até o
  seu", sem dizer de quem era o Grau, e a habilidade do nível 1 passava a ser paga
  no Grau novo sozinha. Desenvolver no Grau 2 era exatamente o mesmo que
  desenvolver no Grau 1 e pagar no 2 — e mais difícil, porque a CD era "10 + o
  custo", e o custo no Grau 3 é o triplo. Nos logs, o Grau virou um botão girado
  na hora do golpe: "Rouge g1 no ifrit", "Rouge g2", "Impacto g3". O próprio jogador
  quis que cada Grau fosse uma técnica nova — o Rouge que vira Bleu, Blank e Noir —,
  e a regra não dava motivo mecânico nenhum para isso.
- A calibração não muda: o simulador sempre mediu cada herói com uma habilidade no
  Grau do nível, e é exatamente o que a Assinatura garante.
- O **Limiar de Grau** do Guia passa a ser respondido pela habilidade, paga naquele
  Grau — mais um motivo para o Grau da habilidade importar.

### A Defesa dá +2 por ponto, e se monta como reação

- Um ponto de Defesa dá **+2 DEF de uma vez**, para tantos alvos quanto o Grau.
  **+2 continua sendo o máximo** que habilidades dão, e duas fontes não somam.
- Instantânea, a Defesa vale **até o início do seu próximo turno**. O livro passa a
  mandar montá-la como **reação** — 2 pontos no Grau 1.
- A passiva de DEF continua +1: passiva entrega metade do ponto ativo, como o
  movimento (+3 m ativo, +1,5 m passivo).
- **Por quê:** o jogador trocou a primeira habilidade defensiva por PV temporários
  no minuto em que ela nasceu ("defesa é horrível"), e no nível 17 repetiu: "tem que
  ser de desvantagem, defesa é uma merda". Medido: a regra antiga (+1 DEF
  sustentada, com a ação) tirava de **9 a 31 pontos** de vitória do trio e da mesa
  solo. Com a regra nova e as Fases, de um a quatro jogadores, o Guardião pagando
  em SP:

  | | mesa solo | 2 | 3 | 4 |
  |---|---|---|---|---|
  | +2 DEF com ação (regra nova, mal usada) | −21,0 | −18,4 | −16,2 | −13,7 |
  | **+2 DEF como reação** | **+8,2** | **+3,8** | **+3,2** | **+0,6** |
  | Desvantagem como reação (a régua da mesa) | +10,4 | +3,9 | +4,7 | +2,4 |

  Médias em pontos de vitória, níveis 3 a 17. O teto também foi medido, antes das
  Fases: **+4 DEF de graça** no grupo inteiro, a luta toda, valia de +2 a +15. DEF
  vale pouco numa luta de duas rodadas, e qualquer coisa que custe a ação perde para
  bater. Por isso a Defesa nova é reativa — e as Fases, que alongam a luta, fazem
  ela render mais, sobretudo na mesa solo.

### Seis técnicas saem da dívida — e a Fúria Cega entra na linha

O limite do `tecnicas.py` é 10 pontos de vitória: acima disso a técnica vira
escolha obrigatória. Seis moravam acima dele, na lista de dívida conhecida — quatro
de antes, e duas que as Fases empurraram para lá, porque a luta mais longa faz
segurar um aliado de pé valer mais. Cada uma foi ajustada e medida (chefe / bando,
nível 12):

| Técnica | Era | Agora | Antes | Depois |
|---|---|---|---|---|
| **Escudo Vínculo** | + proficiência na DEF | **+2** na DEF | +10,8 / +12,1 | +7,1 / +6,0 |
| **Interceptar** | recebe o golpe inteiro | recebe **dois terços**; o aliado sofre o terço que sobra | +11,5 / +11,2 | +9,6 / +6,9 |
| **Represália** | Força + nível de dano | dano igual à **proficiência** | +12,4 / +6,8 | +1,5 / +2,7 |
| **Juramento do Portão** | o jurado fica em 1 PV | fica em 1 PV, e **quem jurou sofre o excesso** | +13,2 / +5,9 | +8,9 / +5,7 |
| **Rede do Destino** | Vantagem até o fim da próxima rodada | Vantagem **até o fim do próximo turno de cada um** | +11,7 / +13,0 | +4,9 / +7,5 |
| **Olho do Futuro** | um turno completo a mais | o turno é **emprestado**: você não age na próxima rodada, e nele nada passa de **metade do Teto** | +17,9 / +12,8 | +9,8 / +8,7 |

- A **Fúria Cega** não morava na dívida, mas passou da linha quando o Interceptar
  mudou o grupo de referência (bando **+12,7**). Ela passa a **gastar a ação**:
  um ataque em cada criatura ao alcance, **todos com Desvantagem** — antes vinha
  por cima da ação de Ataque. Agora **+7,6** contra o bando; contra um chefe
  sozinho, nada, como antes.
- Represália mede baixo (+1,5 / +2,7) e fica assim de propósito: ela é o
  complemento do Interceptar, não um segundo motor de dano.
- Textos trocados no Capítulo Três (Tier 1) e no Capítulo Nove (Tiers 2 e 3) do
  Livro do Jogador, e palavra por palavra na lista de técnicas do construtor. As
  notas automáticas da ficha acompanham: Represália mostra a proficiência, Escudo
  Vínculo mostra +2.

### A Fonte Médica paga SP e gasta Tratamento

- A tabela de Fontes do Livro I dizia que a Médica paga **SP**; a página de consulta
  rápida e o construtor diziam **MP**. Vale a tabela: **a Médica paga SP**.
- E, paga em SP, **cada uso que cura PV gasta um Tratamento**. Sem isso o SP, que
  volta inteiro num Descanso Curto, virava cura sem fim — a regra de Tratamentos
  existe justamente para limitar isso. A cura paga em MP (Palavra Curativa)
  continua fora do limite.
- O construtor oferece "Médica · paga SP e gasta Tratamento ao curar" e escreve
  "e 1 Tratamento" no custo de uma habilidade Médica que cura. `regras/interludio.md`
  diz o mesmo.

### O duelista paga o Grau que basta

- O duelo **Guardião contra Oráculo no nível 5** vencia **81%**, acima do limite de
  80% do `duelo.py`, e estava na dívida. A causa era o simulador jogando mal: com
  Fases, o excesso se perde, e o duelista pagava sempre o Grau cheio — dois golpes
  de Grau 2 numa Fase que o Grau 1 já quebrava.
- Com o Grau gravado desta versão, a habilidade pode ser paga no Grau dela **ou
  abaixo**. O duelista do simulador passou a pagar **o menor Grau cujo golpe médio
  quebra a Fase** do outro. O mesmo duelo cai para **73%**, e todo par fica entre
  **38% e 75%**.
- O Guia do Mestre ganhou o aviso ("o duelista paga o Grau que basta") e a tabela
  do duelo foi medida de novo. O Livro do Jogador já dizia que contra o chefe "às
  vezes vale pagar um Grau menor"; agora diz que no duelo isso pesa ainda mais.
- O grupo contra o chefe **continua** medido pagando o Grau cheio, de propósito: a
  calibração inteira da Tábua foi feita assim, e o grupo que economiza Grau só
  ganha folga.

### Correções

- **O Bestiário partia fichas de criatura ao meio.** O conversor de markdown
  (`build_livros.py`) lia só a primeira linha de cada item de lista; a
  continuação indentada virava parágrafo solto fora da lista. Isso cortava a
  maioria dos Traços e Ações das fichas publicadas. Agora a linha indentada é do
  item de cima, em lista com marcador e numerada.
- A nota do marcial elemental ainda dizia que uma Híbrida ligada ao golpe podia ser
  paga **inteiramente em SP**, contra a regra da 0.17.0. Agora diz "quase toda em SP,
  com o mínimo de 1 MP". O Mestre dos logs tropeçou nessa contradição duas vezes.
- O crítico de habilidade soma dados iguais ao Grau **em que a habilidade foi
  paga** — a palavra "comprada" passou a ser ambígua com o Grau gravado.

### A ficha acompanha

- O construtor chama o seletor de **Grau da habilidade**, mede o Teto por ele,
  impede que uma linha de efeito passe dele e escreve na saída o Grau, se ela sobe
  sozinha (Assinatura) e a **CD de desenvolver**.
- Subir o Grau da habilidade leva junto as linhas de efeito que estavam no teto
  dela.
- A Defesa sai como um ponto só, **+2 DEF**.

### Simulador

- `sim/fases.py` mede o golpe no Teto contra o chefe com e sem Fases, a duração da
  luta do trio em cada faixa e o encontro justo de um a quatro jogadores, e confere
  a tabela de Fases e a de Kleos do Grupo do Bestiário contra o motor.
- O motor (`combate.py`) ganhou Fases: `fases_do_kleos()`, os pisos, o excesso que se
  perde, a Fase que não volta e as condições que caem na quebra. `Lutador.de_monstro`
  só dá Fase ao chefe; bandos e lacaios são montados com `chefe=False`.
- Limites que mudaram, e por quê: `aliado.py` compara a sobrevivência do Aliado
  com a de um herói da mesma luta, em vez de um piso fixo de 50%; `graus.py` aceita
  +1 DEF permanente até 10 pontos (8,3 no nível 20, contra 5,8 antes das Fases);
  `completo.py` aceita 100% na mesa de cinco do nível 20, o topo conhecido da escala.
- **A dívida conhecida está vazia**: `DIVIDA_CONHECIDA` em `tecnicas.py` e
  `DIVIDA_DUELO` em `duelo.py` não têm mais nome. A lista e o mecanismo ficam, para
  a próxima que passar da linha ser anotada à vista e não escondida.
- `duelo.py` ganhou `grau_que_basta()`: com Fases, o duelista paga o menor Grau
  que quebra a Fase do outro.
- `sim/defesa.py` lê o livro a partir da própria pasta, e roda de qualquer
  diretório — o `test.ps1` da CI roda da raiz.
- `sim/defesa.py` mede a Defesa reativa, a Desvantagem reativa e a Defesa com ação,
  de 1 a 4 jogadores, e **falha** se a reativa sair de −1 a +10 pontos, se se
  afastar mais de 4 da Desvantagem, ou se a versão com ação deixar de ser pior que
  atacar — o aviso do livro dependeria disso.
- `sim/ficha.py` confere o Grau gravado, o Teto pelo Grau da habilidade, a CD nova,
  a Assinatura e a Defesa de +2, no livro e no construtor; e que a Fonte Médica
  paga o mesmo recurso na tabela, na consulta rápida e na ficha.

## [0.17.1] - 2026-09-07

As duas mudanças saíram do playtest da one-shot **Antes Que Eu Esqueça** —
Florence Widow, Guardiã de Afrodite no nível 1, mesa de um jogador só. O clímax
foi resolvido em duas rodadas, e só virou combate de verdade porque o Mestre
improvisou uma segunda criatura na hora. Nenhuma ficha de criatura, PV ou linha
da Tábua de Kleos mudou aqui.

### A mesa solo ganha um piso de Kleos

- O Guia mandava usar, contra um herói sozinho, uma criatura de Kleos **inferior
  ao Kleos do grupo**. Numa mesa de um jogador essa conta bate no chão: o Kleos
  do grupo é 1, e não existe degrau abaixo de 1.
- Agora, para o **clímax** de uma mesa solo, conte o herói como **Kleos 2**. As
  escaramuças do caminho continuam no Kleos 1.
- **Por quê:** um chefe de Kleos 1 tem **11 PV** na Tábua. Contra um Guardião de
  nível 1 que acerta com +4 e causa 1d10+2, isso é uma morte em dois golpes — e
  um crítico resolve antes de o monstro agir duas vezes. A instrução antiga não
  tinha para onde apontar, e o resultado na mesa foi um clímax que acabou antes
  de existir.
- O degrau extra vem com três ressalvas, porque não é de graça: o arquétipo
  importa mais aqui do que em qualquer outro lugar — o Kleos 2 causa 9 de dano
  por rodada contra um herói com menos de 20 PV, então um Bruto mata em duas
  rodadas e Conjurador, Sombra ou Veloz trocam esse dano por pressão; o degrau
  vai num chefe e não em dois inimigos somados, porque sozinho ninguém cobre a
  segunda frente; e a rota de fuga continua obrigatória.

### O Efeito mira a defesa fraca do alvo, não a da criatura

- A seção 10 da Forja de Monstros descrevia as duas defesas passivas fortes e a
  fraca **da criatura**. Faltava o outro lado da mesa: contra o que os Poderes
  dela devem rolar. O texto novo pede pelo menos um Poder contra a defesa
  passiva mais baixa de quem vai enfrentá-la.
- **Por quê:** uma Rolagem de Efeito vale o que valer a defesa que ela escolheu
  atacar. Um Efeito **+4 contra Vontade 18** acerta **35%** das vezes; o mesmo
  +4 contra **Reflexos 13** acerta **60%**. No playtest, os dois Poderes do
  monstro miravam justamente a defesa mais alta da personagem, e ele passou o
  combate errando. A mesa lê isso como monstro fraco, não como monstro mal
  apontado.
- O aviso é maior para o **Conjurador**, que gasta o turno inteiro em Rolagem de
  Efeito e não tem ataque contra DEF para compensar a rodada perdida. O
  arquétipo ganhou um item dizendo isso.

## [0.17.0] - 2026-08-31

Tudo nesta versão saiu de um playtest de campanha longa — Jessica Rondo,
Guardiã de Afrodite, dos níveis 2 ao 6 nos logs e projetada até o 12. As
mudanças de regra vêm dos furos que a mesa encontrou jogando.

### A Híbrida passa a pagar os dois recursos

- Uma habilidade Híbrida divide o custo como quiser, mas **pelo menos 1 de cada**
  — nunca mais "4 de um só". Habilidade de custo 1 não pode ser Híbrida.
- **Por quê:** o SP volta inteiro num Descanso Curto de uma hora, sem limite por
  dia, e o MP só volta dormindo. Uma Híbrida paga só em SP tirava toda habilidade
  cara do orçamento do dia. Medido na ficha do playtest — Guardiã 12, MP 21,
  SP 58, habilidade no Teto custando 18: **1 uso por dia** em MP contra **3 por
  hora de descanso** em SP. A Fonte Elemental pura tinha deixado de ter razão de
  existir para Guardião e Furioso.

### O Teto mede o tamanho; os −1 medem o preço

- O **tamanho** de uma habilidade é duração + efeitos + alcance + os
  modificadores que aumentam. É o tamanho que não pode passar do Teto de Custo.
- Os **−1** entram depois e reduzem só o que se paga em MP ou SP. E têm piso:
  **nunca tiram mais que metade do tamanho**.
- **Por quê:** os −1 entravam na mesma soma do Teto, então encolhiam a habilidade
  no papel. Dava para entregar onze pontos de efeito dentro de um Teto de seis, e
  cinco limitações compravam uma habilidade de teto por 1 de recurso.
- A **Tempestade Nebulosa** do playtest — 6 pontos de dano em área, três
  limitações reais — continua custando exatamente 9. A regra valida o que a mesa
  produziu e fecha só o passo seguinte.

### O recálculo retroativo tinha esquecido o SP

- Agora: "recalcule os **PV e o SP** como se ela sempre tivesse sido aquela". E o
  texto diz explicitamente que o Atributo Divino entra no MP **uma vez só**, na
  base da classe.
- **Por quê:** a frase antiga citava PV, Atributo Divino e MP, e nunca o SP — mas
  o SP também tem CON dentro. Nos logs dá para ver o erro nascer: no nível 4 a
  Constituição subiu, o PV foi recalculado e o SP não. O −1 atravessou oito
  níveis e chegou na ficha de nível 12.

### Duas técnicas de Tier 3 saíram da faixa

- **Bastião** reduz o **primeiro golpe de cada rodada**, não todos. Medido:
  +10,7% de vitória contra bando antes, **+4,7%** agora.
- **Provocação Ampla** mantém as duas marcas, mas a segunda **dura até o fim do
  próximo turno** e precisa ser renovada. Medido: +25,1% antes, **+6,9%** agora.
- O limite declarado em `sim/tecnicas.py` sempre foi 10 pontos. As duas passavam
  havia meses porque o teste imprimia o aviso e saía com sucesso.

### Quatro esclarecimentos que a mesa pediu

- **Crítico de habilidade** soma dados iguais ao **Grau em que a habilidade foi
  comprada**, não ao Grau do personagem. Sem isso, comprar barato dobrava o valor
  relativo do crítico.
- **"Zera seu movimento"** vale **até o início do seu próximo turno**.
- **Ferimento Grave não acumula** — o que a nova fonte faz é reiniciar a contagem.
- **Alvo adicional em condição não custa ponto**, e agora o livro diz isso com o
  número: a mesma condição custa 2 no Grau 1 para 1 alvo e 10 no Grau 5 para 5.
  Mesmo preço por alvo.

### Duas fronteiras declaradas

- **O motor não compra efeito de escala narrativa.** Expulsar uma entidade, selar
  uma passagem, virar uma multidão: resolve por teste de atributo contra CD do
  Mestre. É a mesma fronteira das condições de grau Destino.
- **Armadura sem proficiência** bloqueia habilidades de Fonte Física **e
  Híbrida** — a Híbrida tem corpo dentro dela. Elemental pura e Médica continuam
  funcionando. E a penalidade é **Desvantagem**, não desconto no número: o livro
  agora diz isso onde a dúvida aparece.

### O construtor escreve em bloco, não em linha corrida

- Cada habilidade e cada item saem agora como **título, régua e campos
  rotulados** — Custo, Dano, Resolução, Limitações, Tamanho, Memória —, um por
  linha e alinhados. Os campos de habilidades e itens ficaram monoespaçados,
  na tela e na folha impressa, que é o que faz o alinhamento existir.
- **Por quê:** a linha corrida separada por pontos cabia numa habilidade de dois
  campos e virava ilegível em qualquer coisa maior. "6 pontos, 9 dividido entre
  MP e SP" no meio de uma frase de sete segmentos não se lê na mesa, e impresso
  quebrava no meio de uma conta.
- As **limitações escolhidas aparecem pelo nome**, em vez de sumirem dentro do
  número — e a linha diz quando o piso segurou o custo.

### A ficha acompanha

- O construtor de habilidades aplica as regras novas: exige os dois recursos numa
  Híbrida, mede o Teto pelo tamanho e trava o piso dos −1, avisando quando ele
  segura o custo.
- `sim/tecnicas.py` passa a **falhar** quando uma técnica sai da faixa, com uma
  lista de dívida conhecida para as quatro que já estavam fora antes desta versão
  — Escudo Vínculo, Interceptar, Rede do Destino e Olho do Futuro.
- `sim/ficha.py` confere as seis correções contra o texto do livro e refaz as
  contas do piso.

## [0.16.3] - 2026-08-18

### A Ficha do Herói imprime no couro dela

- Desde a 0.15 os cinco livros imprimem com a paleta escura da tela, e a ficha
  era a única folha branca da mesa. Agora a folha impressa usa o **couro escuro
  e o ouro velho** da própria ficha: fundo `#16140F`, cabeçalhos em `#C9A94E`,
  blocos em `#1F1C14`.
- Vale para as duas abas — a do herói, com três páginas, e a da Fera Vinculada,
  com uma — e para os dois caminhos, `Ctrl+P` e o botão de baixar. O
  `html2canvas` recebeu a mesma cor de fundo, senão o PDF baixado sairia com
  falhas brancas onde o desenho não cobre.
- As cores da folha impressa são fixas, e não variáveis de tema: o `html2canvas`
  resolve variável em cascata do jeito dele e às vezes devolve preto.
- A folha impressa também passa a dizer **de que versão ela é**, no subtítulo da
  primeira página. O número vem do mesmo lugar dos livros: o topo do CHANGELOG.

## [0.16.2] - 2026-08-18

### Os livros passam a dizer de que versão são

- Quem baixava um PDF não tinha como saber se estava com a 0.14 ou a 0.16 na
  mão. Agora o colofão dos cinco livros termina com **Versão x.y.z · data**, e a
  estante mostra a mesma no rodapé.
- O número **sai do topo do CHANGELOG**, lido pelo `build_livros.py` a cada
  montagem. Não existe constante duplicada no código: quem publica uma versão
  mexe no CHANGELOG de qualquer jeito, e os livros passam a acompanhar sozinhos.
- O build também anuncia a versão que está montando, para o erro aparecer antes
  de virar arquivo publicado.

## [0.16.1] - 2026-08-18

### Dezoito parentes divinos

- Entram **Hermes** e **Dionísio**, que fecham os olimpianos com filhos, e sete
  **deuses menores** que no cânone têm chalé e descendência: **Hécate, Íris,
  Hipnos, Nêmesis, Nice, Hebe e Tique**.
- Todos no mesmo molde, e é regra explícita no livro: **+2 num atributo, +1 em
  outro, uma Afinidade e uma passiva pequena** — uma vantagem permanente miúda
  mais um efeito de uma vez por cena, combate ou dia. Nenhum ganha luta sozinho,
  e um filho de deus menor vale mecanicamente o mesmo que um filho de Zeus.
- **Hera, Ártemis e Héstia** ficam de fora, e o livro passa a dizer por quê: a
  deusa do casamento não tem filhos fora dele, e as outras duas fizeram voto de
  castidade. Elas entram na campanha como aliadas, patronas ou problemas.
- A nota abre a porta para parentes fora da lista, com a régua para montar um.
- A Ficha do Herói acompanha: os dezoito no seletor, com bônus, Afinidade e
  passiva automáticos.

### Layout

- **Estouro na tela, no Capítulo Onze.** O cartão "Montar uma habilidade" vazava
  400 px numa coluna de 270: `.dado` tem `white-space: nowrap`, o que é certo no
  corpo do texto — para `2d8` não virar "2d" numa linha e "8" na outra — e errado
  num cartão estreito. O cartão passa a usar bloco de fórmula, e o CSS ganha a
  regra de que dentro de cartão o dado quebra linha. Vale para todo cartão futuro.
- **Tabelas de Parente com largura fixa.** Sem isso o navegador dava 5% à coluna
  "Bônus" e quebrava o próprio cabeçalho no meio, "BÔN / US".
- Conferido: os quatro livros impressos ficam inteiros dentro da mancha do
  `@page`, e a página do Livro I não tem nenhum elemento vazando na tela.

## [0.16.0] - 2026-08-18

Quatro coisas que faltavam e não eram balanceamento: uma rede embaixo da ficha,
uma cena mostrando o jogo acontecer, a página que fica no meio da mesa, e uma
primeira sessão pronta para rodar.

### A ficha passa a ser conferida contra o simulador *(`sim/ficha.py`)*

- A Ficha do Herói calcula PV, SP, MP, proficiência, Grau e Teto em JavaScript; o
  `niveis.py` calcula tudo outra vez em Python, e é sobre o Python que todo o
  balanceamento foi medido. **Eram duas implementações da mesma regra e ninguém
  tinha comparado as duas.**
- O teste lê as constantes e as fórmulas direto do `template/ficha.html` e compara
  nos vinte níveis, nas três classes.
- **Achou na primeira execução:** os números batiam, mas a ficha explicava o Teto
  de Custo com a fórmula antiga — "4 + metade do nível" —, de antes da reforma do
  Grau. Valor certo, explicação errada ao lado. Corrigido, e o teste agora também
  confere os textos de ajuda.

### Livro do Jogador — Capítulo Onze: A mesa acontecendo

- **Um exemplo de jogo**: uma cena inteira, dado a dado, com iniciativa, Ataque
  Feroz, Efeito contra Reflexos, condição Preso, Anteparo, um crítico, e a Névoa
  explicando o combate para uma senhora com sacola. Termina com um problema novo
  em vez de um saque.
- **A página do meio da mesa**: oito cartões de consulta rápida do jogador — o
  turno, as ações, Vantagem e Desvantagem, as três rolagens, o que gasta o quê, o
  motor de habilidade em duas linhas, a Agonia e o Ímpeto.
- O bloco de diálogo `.mesa` saiu do Guia e foi para o CSS comum, usado pelos dois
  livros.

### Água de Ferrugem — aventura de estreia *(`regras/agua-de-ferrugem.md`)*

- Três a quatro horas, três a cinco semideuses de nível 1, seis cenas, com todos
  os blocos de criatura prontos.
- Ensina na ordem em que aparece: rolar contra uma CD, a Névoa explicando o mundo
  mortal, um combate simples, uma Fraqueza Mítica que evita a luta, um chefe com
  **Recusa acontecendo na frente da mesa**, e um final de quatro saídas em que
  nenhuma é limpa.
- O Guia do Mestre aponta para ela.

### Regressão

- 18 arquivos.

## [0.15.3] - 2026-08-18

Duas medições que faltavam: mesa de seis e semideus contra semideus.

### Mesa de seis jogadores

- A tabela de Kleos do Grupo agora vai até seis, medida. **O sexto jogador não
  move o degrau em nenhuma faixa**: ele entra como folga, não como dificuldade.
  No nível 3 leva o grupo de 61% para 92% de vitória contra o mesmo Kleos.
- Exceção no topo: seis heróis de nível 20 aguentam um **Kleos 11** a 78%. Mas
  Cataclisma não cai por dano, cai pelo Selo — a conta permite e a ficção manda.
- Acima de seis continua extrapolação, e o código diz isso.

### Semideus contra semideus *(`sim/duelo.py`)*

O duelo nunca tinha sido medido, e é o combate que mais foge das contas do resto
do livro: tudo que o sistema equilibra pressupõe grupo.

- **O Guardião ganha o duelo**, de 54% a 77%. DEF e PV valem mais quando não há
  ninguém dividindo os golpes. Fica registrado como aviso no Guia, não corrigido:
  quem montar arena ou torneio precisa saber antes de prometer justiça.
- **Controle em 1x1 é armadilha.** A mesma dupla, mudando só o que o Oráculo faz
  com a ação: controlando vence de 0% a 3%; gastando o mesmo MP em dano, de 44% a
  57%. É a terceira vez que a medição diz isso, agora em todos os níveis e com o
  arsenal completo.
- **Começar ajuda e não decide:** quem vence a iniciativa leva 56% a 58%. O duelo
  dura de 4 rodadas no nível 1 a 8 no nível 20.
- O Guia ganha o capítulo *Semideus contra semideus*, com a instrução de avisar a
  mesa sobre a armadilha do controle **antes** do duelo.

### Regressão

- 17 arquivos.

## [0.15.2] - 2026-08-18

Conserto vindo da mesa. Um playtest solo do Liam Davis — Furioso de Netuno,
Afinidade Água, do nível 1 ao 5 — apontou três coisas que nenhum simulador tinha
achado, e uma quarta virou regra nova.

### O marcial de afinidade elemental

- A economia de MP dos marciais tinha sido medida e descartada com "física paga
  SP". A mesa mostrou o furo: um filho de Netuno constrói água. Das quatro
  habilidades criadas na ficção, três eram Elementais pagas em MP — e o
  personagem tinha 8.
- Medido: quatro conjurações pequenas por dia no nível 1, e **duas** no nível 20,
  porque o preço do ponto cresce com o Grau e o MP do marcial não. No playtest o
  Mestre precisou recustar uma habilidade de 5 para 2 MP para a cena caber.
- O sistema já tinha as duas saídas e não as dizia para este caso: comprar o
  ponto num **Grau mais baixo**, que custa 1 MP para sempre, e construir
  **Híbridas**, que podem ser pagas inteiramente em SP.

### O Aliado que luta *(regra nova, no Guia do Mestre)*

- O Guia mandava construir todo NPC de combate pelo motor do Bestiário. Medido:
  um aliado montado no Kleos que um herói "vale" sobrevive a **6% dos combates**
  no nível 9. Ele não morre heroicamente, morre toda sessão.
- Regra nova: o Aliado recorrente usa a linha da Tábua do **Kleos do Grupo menos
  2**, inteira, e sobe junto quando o grupo muda de faixa. É a mesma trava da
  Fera Vinculada.
- Medido: sobrevive de 64% a 78% dos combates, responde por 6% a 9% do dano do
  grupo e soma de 3 a 5 pontos de vitória. Um jogador fica de pé em 65% e
  responde por um terço do dano — o Aliado aguenta como gente e bate como
  coadjuvante.
- Vem com passo a passo de cinco etapas e travado em `sim/aliado.py`.

### Itens que acordam

- Consciência vira um Aprimoramento de 2 pontos com Grau mínimo, e o **elo
  psíquico** ganha alcance por Grau: 18 m no Heroico, 100 m no Mítico, 1 km no
  Lendário, e qualquer distância no Divino. Fora do alcance sobra a sensação de
  que o item existe e está inteiro.
- Um item Consciente ocupa sintonia, e consciência não é obediência.

### Húbris personalizada e escudo sem proficiência

- A lista de Húbris vira explicitamente um cardápio: nome curto, uma frase do que
  ela faz e duas situações de Provocação.
- Escudo sem proficiência: você não soma o bônus de DEF e a mão continua ocupada.
  Nada além disso. O livro fechava o caso da armadura e deixava o do escudo em
  aberto.

### Regressão

- 16 arquivos, com `aliado.py` entrando.

## [0.15.1] - 2026-08-18

O simulador termina de aprender o jogo, e a medição derruba uma tabela.

### Mesas de quatro e cinco jogadores — a correção mais importante desta versão

- O Kleos do Grupo era **multiplicação**: quatro heróis de nível 5 valiam 4 × 1¾
  = Kleos 7. Medido, esse encontro é um massacre contra o grupo: **11% de
  vitória**. Cinco heróis contra o Kleos 9 que a conta mandava: **0%**.
- O motivo é a grossura da escala. A Tábua cresce 35% por degrau e um jogador a
  mais soma bem menos que isso.
- `kleos_do_grupo` deixa de multiplicar e passa a ser **tabela medida**. Regra
  nova, em uma frase: **o quarto jogador quase não move o degrau, e o quinto
  vale +1**.

### A Magia da Névoa, medida pela primeira vez

- `sim/nevoa.py`. O Grimório era o único sistema do projeto sem nenhum teste.
- Uma Fórmula entrega de **64% a 95%** do que a habilidade do mesmo MP entrega —
  nunca mais que isso. O que ela compra é ficção, não dano.
- A Descrença cobra o resto: criatura mítica descrê em **65%** das tentativas.
  Sobra 68% de uma criação Densa e 35% de uma Vestida. Contra mortal comum,
  sobra tudo.
- O Refluxo passa entre 40% e 50%: continua sendo desespero, não atalho.
- A Fera de Névoa mudou a vitória do grupo em −2% a +3%. Ela vale pelo corpo e
  pelo faro, não pelos 2d6.

### Vontade do Lugar, Presença e a Fera Vinculada entram no motor

- Vontade do Lugar tira de 1 a 4 pontos da vitória; Presença, de 0 a 4; as duas
  juntas, de 2 a 4. São temperos, não paredes — e por isso continuam fora da
  conta de Kleos.
- A Fera Vinculada soma de −1 a +3 pontos. Ela não é um quarto personagem, e é
  isso que a mantém honesta.

### Papelada

- O `SUMARIO.md` dizia que o Google Doc era a fonte oficial e que as seções
  33–51 só existiam num link de conversa. As duas coisas eram falsas: a fonte é
  o repositório.
- `regras/v1-numeros.md` ganha o aviso de que está **aplicado e superado**, e que
  onde ele diverge dos livros, os livros mandam.

### Regressão

- 15 arquivos, de `defesas_passivas.py` a `nevoa.py`.

## [0.15.0] - 2026-08-18

Uma revisão do sistema inteiro, medida do nível 1 ao 20, e o simulador finalmente
jogando o jogo completo. Cinco dívidas estruturais foram encontradas e pagas.

### O Grau do item vira a progressão do equipamento

- A revisão mostrou que o **dano de arma não acompanhava o PV dos monstros**: do
  nível 5 ao 20 o ataque com arma crescia 15% enquanto o PV do encontro justo
  crescia 250%. Um trio de nível 20 levava **11,5 rodadas** e perdia uma luta em
  cada três.
- O Grau do item passa a dar **dados de arma** e DEF, de graça: Heroico soma um
  dado, Lendário soma dois. Espada longa Heroica é `2d8`; machado grande
  Lendário, `3d10`. Com isso o combate volta a durar **2 a 4 rodadas** do nível 3
  ao 20, e o monstro acerta 45% a 60% em vez de 70%.
- Sai a regra de que bônus numérico custava ponto e parava no +3: ela tratava a
  escala do equipamento como inflação quando era o que segurava a carreira.

### O crítico de habilidade soma o Grau

- Dobrando os dados, uma habilidade no Teto de Custo apagava de 98% a 139% dos PV
  do monstro do encontro justo, em todos os níveis medidos.
- Quatro regras foram comparadas. Vence somar **dados iguais ao Grau**: pior caso
  de 83% dos PV, e o acréscimo no nível 20 ainda é maior que uma rodada inteira
  de machado. Arma continua dobrando.

### A Escala de Kleos perde o platô

- As faixas eram 1–4, 5–9, 10–14, 15–19 e 20 — cinco níveis presos no mesmo
  Kleos. No nível 9 o monstro caía em 1,9 rodada contra 3 nos vizinhos.
- As faixas passam a ser **as mesmas do Grau**: 1–4, 5–8, 9–12, 13–16, 17–20.
  Nenhum valor mudou. Nível 9 vai para 3,4 rodadas; 13 para 3,9; 17 para 3,9.

### A Forja (Parte VII)

- O Interlúdio mandava criar itens por uma Parte VII que não existia, e o Guia
  prometia Classe de Qualidade, Aprimoramentos e Integridade sem nenhuma escrita.
- A Forja é o motor do Capítulo Sete dentro de um objeto: **Manufatura contra
  CD 10 + os pontos do item**, Progresso por Ação de Interlúdio, e a falha
  cobrando Integridade da peça — não do ferreiro.
- **Cargas** iguais ao bônus de proficiência, pela mesma conta dos Tratamentos.
- Item Mítico exige material de criatura de **Kleos 5 ou mais**; Lendário, de
  Kleos 8 ou mais.
- **Encantamentos**: oito, com custo em pontos e preço em dracmas — Forma Oculta,
  Retorno Vinculado, Fome de Ícor, Passo Alado, Voz do Metal, Véu da Névoa,
  Mordida do Estige e Sopro do Portador. Nenhum soma ataque ou dano.

### Livro II — Bestiário

- **A Fera Vinculada** (Parte V): Poupar, Provar e Selar. A fera é um bloco deste
  livro com três cortes, ocupa um dos três Vínculos, gasta o turno do dono e
  morre de verdade.
- **A Forja de Monstros** vira um passo a passo de dez decisões. O Passo 4 é novo
  e preenchia um buraco que ninguém tinha notado: **tamanho, espaço, movimento,
  alcance natural e sentidos** não existiam em lugar nenhum do sistema.
- **O que se leva do corpo**: dracmas e material por Kleos vencido, calculados a
  partir dos preços do Capítulo de Itens.
- **Poderes e Arremetidas entram na conta**: uma criatura completa vale **+1
  Kleos** sobre a linha crua da Tábua. O Sopro é o que decide a luta; a
  Arremetida não mata o grupo, gasta o grupo.
- **Recusas**, medidas enfim: a primeira tira de 11 a 16 pontos da taxa de
  vitória, a segunda de 3 a 6, a terceira quase nada. Recomendação nova: 1 Recusa
  no Kleos 5 a 7, 2 a partir do 8.

### Guia do Mestre

- Capítulo novo: **A Névoa e o mundo mortal**, com o que o mortal vê, as três
  regras de mesa e o tom da campanha.
- Aviso medido: o mesmo grupo vence 58% a 62% batendo só com arma e 88% a 92%
  gastando recurso.

### Ficha do Herói

- **Duas abas**: o Herói e a Fera Vinculada, cada uma com folha própria no PDF. A
  folha da fera sai do documento quando não há fera.
- Campo de **Itens forjados**, com Grau, dado, pontos, Integridade e Cargas.

### Impressão

- Os cinco livros passam a imprimir em A4 com a paleta escura que aparece na
  tela, capa sangrando até a borda e tipografia de livro — a raiz encolhe para
  9,5pt na impressão, o que faltava para os títulos obedecerem.

### Simulador

- `sim/forja.py`, `sim/criaturas.py` e `sim/completo.py` entram na regressão, que
  passa a ter 14 arquivos.
- O motor agora joga o jogo inteiro: equipamento por Grau, habilidade de dano,
  controle por Rolagem de Efeito, Sopro, Arremetida e Recusa. Com tudo ligado dos
  dois lados, o encontro justo entrega de 68% a 93% de vitória, de 2,4 a 3,1
  rodadas, com 1,7 a 2,6 heróis de pé de três.
- Continuam sem modelo: **Vontade do Lugar** e **Presença**.

## [0.14.2] - 2026-08-01

### Ficha do Herói

- A ficha passa a imprimir a **habilidade de classe**, automática como já eram o
  poder do Conceito e a passiva do Parente Divino. Ela ficava de fora só porque o
  Guardião não tinha nenhuma; agora as três têm.
- **Anteparo** aparece com o número já resolvido pela proficiência — 1 nos níveis
  1–8, 2 nos 9–16, 3 nos 17–20 — em vez de mandar o jogador dividir na mesa.
- **Fonte de Mana** aparece com o modificador de Sabedoria somado no PDF.
- Aparece nas duas pontas: na linha de regras automáticas da tela e no bloco
  *Regras automáticas* do PDF.
- Corrigido de passagem: `num()` só entende hífen ASCII, mas os modificadores
  calculados saem com o menos Unicode de `sinal()`. Um Oráculo com Sabedoria
  negativa teria a Fonte de Mana lida com o sinal trocado.

## [0.14.1] - 2026-08-01

### Guardião ganha habilidade de classe

- O Guardião era a única das três classes sem habilidade de classe. Não era
  desenho: `regras/v1-numeros.md` registrava a falta como dívida desde a revisão
  v1, cujo conserto foi todo numérico — PV, armadura, defesas treinadas.
- Entra o **Anteparo**: uma vez por rodada, quando um aliado a até 3 metros sofre
  dano, ele sofre **metade da proficiência do Guardião a menos**, arredondada para
  baixo, mínimo 1. Sem ação, sem SP e **sem reação**.
- Não é reação de propósito. Interceptar, Escudo Vínculo e Represália já disputam
  a reação do Guardião; mais uma coisa naquela fila não seria escolha, seria fila.
- Reduz o dano em vez de transferi-lo, que era exatamente a falta anotada:
  "Interceptar transfere dano sem reduzi-lo".
- Não marca, não provoca e não dá DEF, então não pisa em Postura Desafiadora nem
  em Muro de Escudos — as duas continuam sendo escolhas de técnica.

### O que a medição decidiu

- A primeira versão descontava a **proficiência inteira**. Medida, dava **+14,3%**
  de vitória contra um bando no nível 20: com muitos inimigos batendo, o desconto
  entra toda rodada do combate inteiro. Isso é faixa de habilidade obrigatória.
- A metade da proficiência fica em **+1,3% a +4,8%**, dentro da faixa que o projeto
  usa para técnicas saudáveis.
- O cenário de bando precisou ser recalibrado antes de medir: com bandos fracos a
  coluna saturava em 100% e não dizia nada. Os bandos agora deixam o trio por volta
  de 80% de vitória sem a habilidade.
- Novo `sim/anteparo.py`, na suíte de regressão.
- A Escala de Kleos foi reconferida com o Anteparo ativo em todos os combates: o
  combate justo subiu de 1 a 3 pontos de vitória e continua na mesma curva.

## [0.14.0] - 2026-08-01

Mudança de motor: sai a Evolução por Potência, entra a progressão por **Grau**.
Uma habilidade escrita no nível 1 continua válida a campanha inteira e cresce
junto com o herói, sem ser reconstruída.

### O motor novo

- O **Grau** é a faixa de nível e não se compra: 1 nos níveis 1–4, 2 nos 5–8,
  3 nos 9–12, 4 nos 13–16, 5 nos 17–20.
- O custo é contado em **pontos**. O **Teto de Custo** passa a contar pontos e
  quase não cresce: 5 no Grau 1, 6 daí em diante.
- Um ponto comprado na linha do Grau G **custa G** de MP ou SP e **entrega o
  valor daquela linha**. Pode-se comprar ponto em qualquer Grau até o seu.
- Uma tabela por família de efeito, com uma linha por Grau: dano (alvo único,
  área, contínuo), vida e proteção, movimento e deslocamento, e Vantagem,
  Desvantagem e condições.
- Dano em alvo único vai de `1d8` a `5d8` por ponto; área e contínuo de `1d6` a
  `5d6`; movimento de +3 m a +15 m.
- Condições e Vantagem não ficam mais fortes com o Grau: passam a alcançar
  **mais criaturas**, de 1 a 5 alvos.
- O **Limiar de Potência** do Guia do Mestre virou **Limiar de Grau**, de 1 a 5.
  Em vez de comprar um número de 3 a 14 na hora, o herói tem o Grau ou não tem.

### O que a medição decidiu

- **O ponto não podia ficar melhor de graça.** A primeira versão manteve o ponto
  a 1 MP e só engordou o dado: medido, o conjurador chegava a **300% do dia do
  Furioso** no nível 20. O que precisa ficar constante é o dano por MP — por isso
  o ponto do Grau G custa G.
- **O teto antigo tinha de encolher.** Ele ia de 5 a 14 porque a única progressão
  possível era comprar mais pontos do mesmo tamanho. Mantê-lo junto com o dado
  maior somava duas progressões; reduzi-lo sem mexer no preço deixava cada uso
  barato demais e enchia o dia de usos.
- **Defesa é a única linha que não engorda.** Medido no nível 20, cada ponto de
  DEF vale quase **7 pontos de vitória** num combate justo, mais que qualquer
  outra linha por ponto gasto. O Grau alto espalha o bônus por mais aliados e o
  máximo continua sendo +2.
- Resultado: potência por uso sobe de **17 para 91** do nível 4 ao 20, com o dia
  de aventura parado onde o sistema publicado já estava — 112%, 57%, 80%, 103% e
  126% do Furioso, contra 110%, 64%, 90%, 106% e 121% do motor antigo.
- A Escala de Kleos foi reconferida com o Oráculo jogando pelo motor novo e
  continua de pé: o combate justo dá 84% a 99% de vitória, a mesma curva.

### Livros e ficha

- **Livro do Jogador:** capítulo Sete reescrito — nova seção *O Grau*, a conta do
  custo agora tem duas linhas (pontos, depois recurso), as seções de Evolução e
  Potência saíram, e o modelo de registro ganhou Grau e custo em recurso.
- Nota nova sobre rolar trinta dados: quem preferir pode usar valor médio.
- O capítulo Nove troca a fórmula do teto pela tabela de Graus.
- **Ficha do Herói:** os três campos de Evoluída saíram; entrou a caixa **Grau**,
  calculada do nível, com uma régua que diz o preço e o valor do ponto. O Teto de
  Custo passou a seguir o Grau.
- **Simulador:** novo `sim/graus.py` com a calibragem e a regressão do motor;
  `sim/evolucao_habilidades.py` foi aposentado junto com a regra que ele testava.

## [0.13.4] - 2026-08-01

### Ficha do Herói

- Corrigido o defeito que deixava o PDF ilegível: uma folha que crescia além de
  A4 era **reduzida inteira** para caber. Medido, uma ficha com história longa
  chegava a 887 mm e saía em escala 0,335 — o texto de 8 pt virava 2,7 pt, numa
  coluna de 70 mm no meio da página.
- A folha agora é **paginada**, não encolhida. O conteúdo é repartido em quantas
  páginas A4 forem necessárias, e o tamanho da letra nunca muda.
- A repartição respeita os blocos: primeiro devolve blocos inteiros para a folha
  seguinte; só reparte o texto de um bloco quando ele sozinho não cabe, e aí a
  continuação leva o mesmo título marcado como *(continuação)*.
- Tabelas longas de ataques ou perícias são repartidas por linha, sem cortar
  nenhuma ao meio.
- O rodapé passa a numerar o total real de folhas, e a mensagem de conclusão
  informa quantas páginas saíram.
- Medido depois da correção: de ficha vazia a 855 mil caracteres, **nenhuma
  página passa de 297 mm**. Uma ficha comum continua em três páginas e leva 8 ms
  para paginar. Baixar e reimportar um PDF paginado devolve os campos idênticos.

### Livros

- **Livro do Jogador:** a passagem de relíquias citava uma "CD de Habilidade" que
  não existe em nenhum outro lugar do sistema. Passou a usar o bônus de
  habilidade com Ataque de Habilidade ou Rolagem de Efeito, como o resto do livro.
- **Livro do Jogador:** a ficha de exemplo da Cássia não mencionava a habilidade
  Evoluída a que a Memória 3 dá direito. Quem copiava o capítulo perdia uma escolha.
- **Grimório:** a CD de Névoa convivia com a Rolagem de Efeito sem explicar por
  que uma usa base 8 e a outra base 14. Agora o livro diz qual número é rolado por
  quem — as duas bases são a mesma chance vista de pontas opostas.
- **Guia do Mestre:** Evoluída é a única escolha do sistema que não faz nada
  sozinha. O Guia passou a pedir ao Mestre pelo menos um Limiar de Potência por
  aventura, sem o qual a regra vira decoração.
- **Estante:** a página inicial ainda anunciava três correções vindas do
  simulador; são quatro desde a recalibragem da Escala de Kleos.

### Verificação

- A regressão numérica completa passa: dez arquivos, de `defesas_passivas.py` a
  `calibrar_kleos.py`.
- Os números da ficha de exemplo do Capítulo Dez foram conferidos contra o motor
  da Ficha do Herói, um a um: atributos, PV 16, SP 14, MP 7, DEF 17, Iniciativa
  +4, Memória 3, bônus de habilidade +3 e as três defesas passivas batem.
- Os cinco livros continuam sem rolagem horizontal.

## [0.13.3] - 2026-07-30

### Evolução de Habilidades

- Implementada a mecânica que estava registrada nos playtests, mas ausente dos
  livros: uma habilidade Evoluída pode elevar sua Potência e seu custo sem
  aumentar dano, alcance, área, duração ou qualquer outro efeito.
- O número máximo de habilidades Evoluídas agora é **metade da Memória,
  arredondada para baixo**: de 0 a 3 escolhas.
- Potência natural passou a ser o custo final de construção da habilidade; descontos
  recebidos depois não reduzem esse valor.
  Uma Evoluída pode alcançar qualquer Potência maior até o Teto de Custo.
- O Guia do Mestre recebeu Limiares de Potência para barreiras, imunidades,
  dissipações e rituais, com valores sugeridos de 3 a 14.

### Ficha do Herói

- A ficha calcula automaticamente o limite de Evoluídas e libera até três campos
  para registrar as habilidades escolhidas.
- Excesso causado por redução de Memória é sinalizado imediatamente.
- As escolhas aparecem no PDF e são preservadas ao importar a ficha.
- Adicionada regressão automática para o limite por Memória, Teto de Custo,
  descontos e preservação do perfil original da habilidade.

## [0.13.2] - 2026-07-30

### Ficha do Herói

- Corrigido o retrato do PDF editável: a imagem não é mais cortada para um
  quadrado de 520 × 520 nem recomprimida antes de ser incorporada ao arquivo.
- Baixar e importar agora preserva exatamente os dados da imagem original,
  inclusive proporção, transparência e resolução.
- A moldura da ficha e a moldura do PDF passaram a usar a mesma proporção e o
  mesmo ponto central, evitando mudança de enquadramento entre as duas versões.
- Retratos JPG, PNG, WEBP e GIF de até 15 MB são aceitos e continuam sendo
  processados apenas no navegador.

## [0.13.1] - 2026-07-30

### Ficha do Herói

- Adicionado **Importar PDF**: uma ficha baixada agora pode ser reaberta no site e
  restaura campos, seleções, marcações, ataques, recursos, textos, ajustes manuais
  e o retrato do personagem.
- O PDF continua com as mesmas três páginas A4, mas passa a carregar um pacote de
  dados versionado e invisível dentro do próprio arquivo.
- A importação valida assinatura, versão, tamanho e conteúdo antes de preencher a
  ficha. PDFs comuns e fichas de versões incompatíveis são recusados com uma
  mensagem clara.
- Todo o processo continua local: o PDF não é enviado, não existe conta e nenhum
  dado permanece no navegador depois que a aba é fechada.
- PDFs gerados antes desta versão continuam legíveis, mas eram somente imagens e
  não possuem informação suficiente para reconstruir os campos.

## [0.13.0] - 2026-07-30

### Defesas passivas

- Fortitude, Reflexos e Vontade agora são números prontos: **14 + atributo +
  proficiência**, quando a defesa é treinada. Guardião treina Fortitude e Vontade;
  Furioso, Fortitude e Reflexos; Oráculo, Vontade e Reflexos. No nível 10, todos
  treinam a terceira defesa.
- Ataques continuam contra DEF. Efeitos agora usam **1d20 + atributo +
  proficiência** contra uma defesa passiva; igualar o valor é acerto. Rolagens de
  Efeito não têm crítico e 1 ou 20 naturais usam o total normal.
- Áreas fazem uma Rolagem de Efeito separada contra cada alvo e rolam o dano uma
  vez. Efeitos combinados resolvem dano e condição com a mesma rolagem.
- Vantagem numa antiga resistência virou Desvantagem para a fonte do Efeito, e
  vice-versa. Perigos fixos usam bônus igual à antiga CD menos 8.
- A base **14** foi escolhida por equivalência, não por aproximação: a regressão
  exata verificou 3.888 combinações de rolagem normal, Vantagem e Desvantagem sem
  mudar nenhuma probabilidade do modelo anterior.

### Livros e ficha

- A Tábua de Kleos e os 38 perfis do Bestiário agora exibem bônus de Efeito e os
  totais de Fortitude, Reflexos e Vontade, sem somas durante a sessão.
- Todos os poderes dos monstros, Presenças, Recusas, condições, perigos de ambiente
  e venenos foram convertidos para a nova resolução.
- O Grimório ganhou Efeito de Fórmula. Descrença por Investigação ainda enfrenta a
  CD de Névoa; Descrença por força interior usa o Efeito da Fórmula contra Vontade
  passiva, com equivalência matemática.
- A Ficha do Herói calcula automaticamente as três defesas passivas, aplica os
  treinamentos da classe e do nível 10, aceita ajustes individuais e leva os
  valores prontos para o PDF.
- O Guia do Mestre recebeu uma escala de Efeito para perigos: +3 leve, +5 perigoso,
  +8 severo, +11 lendário e +14 divino.

### Qualidade

- Adicionado `sim/defesas_passivas.py`, uma prova exaustiva e sem dependências da
  equivalência entre a resolução antiga e a nova.
- Documentos auxiliares, sumário, READMEs bilíngues e gerador dos livros foram
  alinhados à versão 0.13.0.

## [0.12.0] - 2026-07-29

### Leitura e navegação

- Os cinco livros ganharam uma miniestante flutuante: um pequeno tridente acompanha
  a rolagem, abre os outros quatro tomos e oferece acesso à estante completa.
- Sumários e referências internas agora são hyperlinks. O Grimório recebeu sumário
  próprio; seções numeradas, degraus de Kleos e as 38 criaturas ganharam âncoras
  estáveis para links diretos.
- O índice rápido do Bestiário passou a levar diretamente a cada criatura, e as
  referências entre Livro do Jogador, Bestiário, Grimório, Guia e Ficha foram ligadas.
- A navegação flutuante funciona sem JavaScript, aceita teclado e desaparece na
  impressão para não alterar o PDF dos livros.

### Identidade do projeto

- A estante, os cinco livros e os READMEs agora identificam o RPG como projeto
  independente, não oficial e sem fins lucrativos, sem alegar afiliação, aprovação
  ou patrocínio dos titulares de *Percy Jackson*.
- A apresentação passou a distinguir explicitamente as regras e os textos autorais
  dos elementos próprios de franquias de terceiros.

## [0.11.1] - 2026-07-29

### Regras

- Bronze celestial, ferro estígio e ouro imperial foram fechados como materiais
  divinos mecanicamente equivalentes: preservam o perfil da arma e ferem criaturas
  míticas sem conceder bônus gratuito de ataque ou dano.
- Armas de ouro imperial receberam **Ruptura Áurea**: quando são realmente destruídas,
  explodem em 8 metros, atingem inclusive o portador, causam 4d6 de dano com Reflexos
  CD 13 para reduzir à metade e são perdidas definitivamente.
- O procedimento de 0 PV foi consolidado como **Teste de Morte**: três sucessos
  estabilizam, três falhas matam, 20 natural recupera 1 PV e 1 natural causa duas
  falhas. Dano, cura, estabilização e nova queda agora têm regras explícitas.
- A Ficha do Herói ganhou marcadores para três sucessos e três falhas de Agonia, que
  também aparecem no PDF.

## [0.11.0] - 2026-07-29

### Livro do Jogador

- Adicionada **Fúria do Semideus** como regra opcional de campanha. O módulo
  transforma a Ruptura da Húbris em três estágios: Despertar, Transbordamento e
  Ruptura, com gatilho emocional, testes de controle, Âncoras, manifestação
  pessoal, acordo de agência e consequências.
- A Fúria não pode ser acionada como técnica comum: depois de usada, exige
  Descanso Longo e a nova ação de Interlúdio **Assimilar a Fúria**.
- Criados seis graus de item — Mortal, Consagrado, Heroico, Mítico, Lendário e
  Divino — com requisito de nível e faixas de preço em dracmas.
- Itens mágicos permanentes passaram a usar **Sintonização**: um espaço nos
  níveis 1–5, dois nos níveis 6–11 e três a partir do nível 12.
- O catálogo ganhou 21 utilitários, 12 curativos e 24 relíquias mágicas, todos
  com nível, preço e efeito fechado.
- A tabela defensiva ganhou Broquel, Loriga de Hoplita e Escudo-torre, além de
  requisito de nível e preço em todos os equipamentos.
- A Ficha do Herói deixou de presumir uma lista fechada de armaduras: agora
  calcula DEF por Base da armadura + Destreza permitida + escudo/item + outros
  ajustes, e leva a fórmula completa para o PDF.
- Curativos divinos receberam Saturação para impedir consumo em sequência e
  preservar a função do Oráculo.
- “Uma vez por combate” foi formalizado para impedir que encerrar e reabrir a
  iniciativa recupere usos.

## [0.10.1] - 2026-07-29

### Ficha do Herói

- O botão **Baixar em PDF** não abre mais a janela de impressão: agora gera e
  baixa diretamente um PDF A4, sempre com três páginas.
- Corrigido o caso real em que uma configuração de papel 5×7 do navegador
  transformava as três folhas em seis, deixando uma página vazia após cada folha.
- A geração preserva retrato, cores, tabelas e textos longos e não envia os dados
  do personagem para nenhum servidor.
- `html2canvas` 1.4.1 e `jsPDF` 4.2.1 foram incorporados localmente com licença MIT;
  a ficha publicada continua autossuficiente.

## [0.10.0] - 2026-07-29

### Regras

- Consolidada a regra de **uma resolução por habilidade**: ataque ou resistência,
  nunca ambos. Efeitos secundários fracos acompanham o acerto; condições médias e
  fortes exigem resistência.
- **Ativação** virou campo obrigatório de toda habilidade. Ação bônus, reação e
  movimento acrescentam +1 ao custo. Passo das Trevas foi fechado em 2 MP, ação
  bônus e +3 m no turno.
- Adicionada **Manifestação Menor de Afinidade**: 1 MP e Interação Simples para
  improvisos narrativos sem dano, bônus, condição ou objeto funcional.
- Áreas agora têm origem e medida definidas, encontram paredes e atingem aliados
  por padrão. Área seletiva custa +1.
- Húbris concede Ímpeto no máximo uma vez por cena; a mesma Provocação não pode ser
  repetida antes de sua consequência se resolver.
- Gastar Ímpeto não exige ação, mas ficou limitado a um por turno. Resistir a uma
  Ruptura continua pagando dois pontos juntos.
- Definidos apoio, carga e arrasto de criaturas, mãos ocupadas e interações com
  objetos, algemas, duas armas Leves e objetos arremessados.
- Magia cosmética de itens não tem custo; retorno durante combate virou uma
  melhoria mecânica com Interação Simples.
- 20 natural em perícia concede benefício excepcional quando a tentativa é
  possível, sem realizar o impossível. Iniciativa não possui crítico.
- Estabilização usa ação e Intuição CD 10; Kit Médico dá Vantagem ou permite gastar
  1 Tratamento e 2 SP para sucesso automático sem cura em combate.
- Adicionados encontros solo e um Relógio de Ritual para rituais durante iniciativa.

### Ficha do Herói

- Refeita a impressão em **três páginas A4 próprias para PDF**, sem imprimir os
  controles da tela.
- Retrato passou de imagem de fundo para elemento de imagem real e agora aparece no PDF.
- História, Vínculos, habilidades e outros textos longos são convertidos em texto
  estático antes da impressão, sem corte por rolagem de textarea.
- Conceito, Parente Divino, Afinidade, bônus de linhagem, resistências da classe e
  perícias iniciais agora são seleções estruturadas e automáticas.
- Atributos separam Base, bônus Divino e pontos ganhos por nível; a ficha valida a
  distribuição padrão, o total disponível na progressão, o teto 20 e pontos
  adiantados por Treino de Interlúdio.
- Instinto de Briga soma Força automaticamente à Iniciativa. Caso de regressão:
  DES +1 e FOR +2 resultam em **Iniciativa +3**.
- Ferimento Grave, ajustes de DEF/Iniciativa/Movimento/recursos, CD, Memória,
  Tratamentos, resistências, Percepção passiva, ataque e dano foram automatizados.
- Ataques aceitam ajuste mágico, dado base e escolha de somar ou não o atributo ao
  dano, cobrindo corretamente combate com duas armas.
- A ficha continua sem persistência: fechar a aba apaga os dados.

### Documentação e qualidade

- Criada a consulta rápida [`regras/regras-universais.md`](regras/regras-universais.md).
- O Guia do Mestre ganhou exemplos de testes incomuns, orientação para herói solo
  e regras de rituais sob pressão.
- README em português e inglês atualizado para a revisão 0.10.0.
- O relatório de playtest **A Última Plataforma** virou teste de aceitação da ficha
  e das regras universais.
- Adicionado `test.ps1` para repetir a regressão numérica completa com um comando.

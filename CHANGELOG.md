# Changelog

Todas as mudanças relevantes de **Ascensão dos Semideuses** serão registradas
neste arquivo. O projeto está em beta e usa versionamento semântico a partir desta
revisão.

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

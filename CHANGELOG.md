# Changelog

Todas as mudanças relevantes de **Ascensão dos Semideuses** serão registradas
neste arquivo. O projeto está em beta e usa versionamento semântico a partir desta
revisão.

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

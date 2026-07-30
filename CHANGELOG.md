# Changelog

Todas as mudanças relevantes de **Ascensão dos Semideuses** serão registradas
neste arquivo. O projeto está em beta e usa versionamento semântico a partir desta
revisão.

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

# Convenções deste repositório

- Leia CONTRIBUTING.md antes de criar ou modificar uma skill.
- Cada skill fica em skills/<nome>/ e precisa apenas de SKILL.md. Crie recursos
  adicionais somente quando contribuírem para a execução.
- Preserve o escopo pedido pelo usuário, a portabilidade e o carregamento de
  referências conforme a necessidade. Não transforme exemplos em regras globais.
- Edite metadados na própria skill. Não mantenha uma segunda lista manual.
- A seção entre os marcadores skills-catalog do README é gerada por
  scripts/catalog.py; preserve o conteúdo fora dela.
- Antes de publicar mudanças na automação, execute os testes em tests/ e o
  validador. Para mudanças comportamentais, escolha avaliações pertinentes.
- Não altere os recursos visuais originais sem necessidade demonstrada. Não
  adicione saídas de execução, ambientes virtuais ou arquivos temporários ao Git.

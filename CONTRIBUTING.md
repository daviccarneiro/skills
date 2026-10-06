# Adicionar e manter skills

## Estrutura mínima

Crie `skills/<nome>/SKILL.md`, com uma capacidade bem delimitada:

```markdown
---
name: revisar-texto
description: Revise clareza e gramática de textos quando o usuário pedir revisão editorial.
---

# Revisar texto

Preserve a intenção e a voz do autor. Entregue o texto revisado e explique
somente alterações que mudem o sentido ou exijam uma decisão do usuário.
```

Use nomes em minúsculas, sem acentos, com números e hífens simples, de até 64
caracteres. O nome deve coincidir com a pasta. A descrição deve explicar a
capacidade e quando usá-la; o validador aceita até 1.024 caracteres, mas prefira
uma ou duas frases curtas. Nomes de apresentação podem ter acentos e maiúsculas:

```yaml
metadata:
  display_name: "Revisar texto"
```

## Conteúdo e portabilidade

- Escreva somente as instruções que mudam decisões ou melhoram o resultado.
- Separe regras constantes de entradas variáveis. Não dependa do histórico de
  uma conversa, caminhos pessoais ou arquivos que só existem em um projeto.
- Use links relativos para arquivos incluídos e diga quando devem ser lidos.
- Acrescente `references/`, `assets/`, `scripts/` ou `agents/` somente quando
  houver necessidade. Não exija que o agente carregue todos os recursos.
- Inclua poucos exemplos distintos que esclareçam decisões difíceis.
- Declare ferramentas necessárias e a alternativa quando estiverem ausentes.
  O formato portátil não garante que todo agente tenha as mesmas ferramentas.
- Mantenha instruções específicas de uma skill dentro dela; o README da raiz
  é um catálogo e guia de instalação da biblioteca.

## Imagens e arquivos grandes

Inclua arquivos que contribuam para a execução, não saídas temporárias, ZIPs
gerados, caches ou dependências instaladas. Prefira recursos menores quando
preservarem a qualidade necessária. Antes de reduzir referências visuais,
compare a legibilidade de traço, cor e textura; não descarte originais apenas
para reduzir tamanho. A skill de ilustração conserva suas cinco referências e
seleciona uma ou duas por tarefa. Não há exigência de imagens para outras skills.

## Verificação

Execute os comandos de validação descritos no README antes de enviar alterações.
O validador confere localização, campos obrigatórios, nomes, metadados YAML e
estrutura do catálogo. Isso não substitui a avaliação do comportamento da skill.

Para mudanças relevantes, teste pedidos representativos e registre o que foi
realmente observado. Em uma skill visual, por exemplo: mudar o assunto sem
herdar objetos da referência, mudar a paleta sem mudar o desenho e preservar
um personagem entre cenas. Não registre um exemplo como teste executado.

Não é necessário editar a tabela do README: após a mudança entrar na branch
padrão, a Action regenera o catálogo em ordem alfabética, incluindo remoções e
renomeações. É possível gerar a mesma atualização localmente com
`python scripts/catalog.py`.

## Dependências da manutenção

As versões das Actions são fixadas por commit e a dependência Python é fixada
em `requirements-dev.txt`. O Dependabot propõe atualizações; elas passam pela
mesma validação. Use commits focados e não reescreva o histórico para atualizar
uma skill. Preserve a origem dos recursos e não atribua a eles uma licença que
não tenha sido estabelecida.

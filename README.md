# Skills

Biblioteca pessoal de skills reutilizáveis para diferentes projetos e agentes
compatíveis com o formato `SKILL.md`. Cada skill pode ser instalada separadamente.
Recursos específicos de uma ferramenta são opcionais e ficam junto da skill.

## Catálogo

<!-- skills-catalog:start -->

| Skill | Descrição |
|---|---|
| [Gerar-ilustração-Notion](skills/gerar-ilustracao-notion/SKILL.md) | Ilustrações editoriais minimalistas com personagens simples, contornos escuros, cores foscas e textura de papel. Inclui cinco referências visuais, prompt-base, parâmetros, negativos e exemplos. |

<!-- skills-catalog:end -->

Esta seção é gerada a partir de `skills/*/SKILL.md`. Adicionar, renomear, alterar
ou remover uma skill na branch principal atualiza a listagem automaticamente.

## Instalação e uso

Clone este repositório:

```sh
git clone https://github.com/daviccarneiro/skills.git
cd skills
```

Copie a pasta inteira da skill desejada para o diretório de skills do seu agente.
No Codex, usando a configuração pessoal padrão, por exemplo:

```sh
mkdir -p ~/.codex/skills
cp -R skills/gerar-ilustracao-notion ~/.codex/skills/
```

Se você personalizou `CODEX_HOME`, use a pasta `skills` dentro desse diretório.
Preserve uma instalação existente antes de substituí-la. Não copie somente o
Markdown quando a skill incluir arquivos auxiliares. Em outros agentes, consulte
o mecanismo de instalação e as ferramentas disponíveis naquele ambiente.

Abra uma nova conversa e invoque a skill pelo identificador, por exemplo:

```text
Use $gerar-ilustracao-notion para criar uma horta comunitária em sálvia e terracota.
```

## Organização

```text
skills/<nome>/SKILL.md       Instruções e metadados obrigatórios
skills/<nome>/references/    Documentação e exemplos, quando necessários
skills/<nome>/assets/        Imagens, modelos e outros recursos reutilizáveis
skills/<nome>/scripts/       Código auxiliar, quando necessário
skills/<nome>/agents/        Metadados opcionais específicos de agentes
scripts/                    Manutenção do repositório e do catálogo
tests/                      Testes da automação do repositório
.github/workflows/          Validação e atualização automática
```

Skills simples precisam apenas de `SKILL.md`; não crie pastas vazias para seguir
o exemplo. Consulte [CONTRIBUTING.md](CONTRIBUTING.md) para adicionar skills e
[AGENTS.md](AGENTS.md) para as convenções de manutenção por agentes.

## Automação

A Action **Validar skills e atualizar catálogo** valida os metadados e executa
os testes em pushes e pull requests. Na branch padrão, atualiza somente o trecho
marcado do README e faz um commit se houver mudança. Também pode ser executada
manualmente pela aba **Actions**. Pull requests não recebem permissão de escrita.

O catálogo usa `name` e `description` do `SKILL.md`; para o título exibido,
prefere `metadata.display_name`, depois `interface.display_name` do arquivo
opcional `agents/openai.yaml`, e por último o identificador da skill.

Não é necessário configurar um token pessoal. O job de atualização usa o token
temporário do GitHub com `contents: write`. Se futuramente uma regra da branch
impedir commits do bot, a execução falhará explicitamente; adapte o fluxo para
pull requests em vez de desativar a proteção.

Para executar localmente (Python 3.11 ou superior):

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-dev.txt
.venv/bin/python -m unittest discover -s tests -v
.venv/bin/python scripts/catalog.py --validate-only
.venv/bin/python scripts/catalog.py
.venv/bin/python scripts/catalog.py --check
```

`--check` não modifica arquivos e falha se o catálogo estiver desatualizado.
As dependências de manutenção não são necessárias para usar as skills.

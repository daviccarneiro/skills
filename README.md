# Skills

Skills reutilizáveis para Codex.

## Disponíveis

| Skill | Descrição |
|---|---|
| [Gerar-ilustração-Notion](skills/gerar-ilustracao-notion/SKILL.md) | Ilustrações editoriais minimalistas com personagens simples, contornos escuros, cores foscas e textura de papel. Inclui cinco referências visuais, prompt-base, parâmetros, negativos e exemplos. |

## Instalação

Clone este repositório e copie a pasta da skill desejada para `~/.codex/skills/` (ou para `skills/` dentro de seu `CODEX_HOME` personalizado):

```sh
git clone https://github.com/daviccarneiro/skills.git
mkdir -p ~/.codex/skills
cp -R skills/skills/gerar-ilustracao-notion ~/.codex/skills/
```

Se já existir uma skill com o mesmo nome, preserve sua versão antes de substituí-la. Copie a pasta inteira, incluindo `assets`, `references` e `agents`, para manter as referências disponíveis.

Inicie uma nova conversa no Codex e invoque:

```text
Use $gerar-ilustracao-notion para criar três pessoas cuidando de uma horta
comunitária, com paleta sálvia e terracota e fundo claro, no formato 3:2.
```

## Gerar-ilustração-Notion

O nome exibido é **Gerar-ilustração-Notion**; o identificador técnico é `gerar-ilustracao-notion`.

A skill permite variar paleta, tema, cenário, objetos e contexto, preservando a linguagem visual das referências. Medicina, odontologia e tecnologia são apenas assuntos dos anexos e não limitam os novos pedidos. A menção ao Notion é uma aproximação estética, sem indicação de vínculo oficial.

- [Instruções e prompt-base](skills/gerar-ilustracao-notion/SKILL.md)
- [Análise visual dos cinco anexos](skills/gerar-ilustracao-notion/references/analise-visual.md)
- [Exemplos de uso](skills/gerar-ilustracao-notion/references/exemplos.md)
- [Imagens de referência](skills/gerar-ilustracao-notion/assets)

É necessário um gerador de imagens disponível para produzir imagens; sem ele, a skill prepara prompts e indica as referências a anexar. Os PNGs originais são mantidos sem alterações. A estrutura e os links foram verificados; a entrega inicial não incluiu geração de imagens de teste.

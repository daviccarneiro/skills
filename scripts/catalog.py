"""Validate skill metadata and replace only the generated README catalog."""

from __future__ import annotations

import argparse
from dataclasses import dataclass
import html
from pathlib import Path
import re
import sys

import yaml

START = "<!-- skills-catalog:start -->"
END = "<!-- skills-catalog:end -->"
NAME = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*\Z")


class CatalogError(ValueError):
    """Invalid input; leave README untouched."""


class UniqueSafeLoader(yaml.SafeLoader):
    """Reject duplicate keys instead of silently accepting the last value."""


def unique_mapping(loader, node, deep=False):
    result = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if not isinstance(key, str):
            raise CatalogError("As chaves YAML devem ser strings.")
        if key in result:
            raise CatalogError(f"Chave YAML duplicada: {key}")
        result[key] = loader.construct_object(value_node, deep=deep)
    return result


UniqueSafeLoader.add_constructor(
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, unique_mapping
)


def read_mapping(text: str, source: Path) -> dict:
    try:
        data = yaml.load(text, Loader=UniqueSafeLoader)
    except (yaml.YAMLError, CatalogError) as exc:
        raise CatalogError(f"{source}: YAML inválido: {exc}") from exc
    if not isinstance(data, dict):
        raise CatalogError(f"{source}: esperado um mapa YAML.")
    return data


def required_text(data: dict, key: str, source: Path) -> str:
    value = data.get(key)
    if not isinstance(value, str) or not value.strip():
        raise CatalogError(f"{source}: '{key}' deve ser texto não vazio.")
    return value.strip()


@dataclass(frozen=True)
class Skill:
    name: str
    title: str
    description: str


def load_skill(path: Path) -> Skill:
    text = path.read_text(encoding="utf-8")
    match = re.match(r"\A---\r?\n(.*?)\r?\n---(?:\r?\n|\Z)", text, re.S)
    if not match:
        raise CatalogError(f"{path}: frontmatter YAML ausente ou incompleto.")
    data = read_mapping(match.group(1), path)
    name = required_text(data, "name", path)
    description = required_text(data, "description", path)
    if not NAME.fullmatch(name) or len(name) > 64 or name != path.parent.name:
        raise CatalogError(f"{path}: nome inválido ou diferente da pasta.")
    if len(description) > 1024:
        raise CatalogError(f"{path}: descrição excede 1.024 caracteres.")
    if not text[match.end():].strip():
        raise CatalogError(f"{path}: corpo de instruções vazio.")
    metadata = data.get("metadata", {})
    if not isinstance(metadata, dict):
        raise CatalogError(f"{path}: metadata deve ser um mapa.")
    title = name
    agent_path = path.parent / "agents" / "openai.yaml"
    if agent_path.is_file():
        agent = read_mapping(agent_path.read_text(encoding="utf-8"), agent_path)
        interface = agent.get("interface", {})
        if not isinstance(interface, dict):
            raise CatalogError(f"{agent_path}: interface deve ser um mapa.")
        if "display_name" in interface:
            title = required_text(interface, "display_name", agent_path)
    if "display_name" in metadata:
        title = required_text(metadata, "display_name", path)
    return Skill(name, title, " ".join(description.split()))


def discover(root: Path) -> list[Skill]:
    directory = root / "skills"
    if not directory.exists():
        return []  # Git does not retain the empty directory after the last removal.
    if not directory.is_dir():
        raise CatalogError(f"Esperado um diretório: {directory}")
    for path in directory.rglob("*"):
        if path.is_symlink():
            raise CatalogError(f"Link simbólico não permitido nas skills: {path}")
        if path.is_file() and path.name.lower() == "skill.md":
            if path.name != "SKILL.md" or path.parent.parent != directory:
                raise CatalogError(f"Use skills/<nome>/SKILL.md: {path}")
    skills = []
    for folder in sorted(directory.iterdir()):
        if not folder.is_dir():
            continue
        entry = folder / "SKILL.md"
        if not entry.is_file():
            raise CatalogError(f"Pasta de skill sem SKILL.md: {folder}")
        skills.append(load_skill(entry))
    return sorted(skills, key=lambda skill: (skill.title.casefold(), skill.name))


def escape_cell(text: str) -> str:
    # Render metadata as text, never as injected HTML, Markdown links or rows.
    text = html.escape(" ".join(text.split()), quote=True)
    for character in "\\|[]`*_{}":
        text = text.replace(character, f"&#{ord(character)};")
    return text


def render(skills: list[Skill]) -> str:
    if not skills:
        return "Nenhuma skill cadastrada.\n"
    lines = ["| Skill | Identificador | Descrição |", "|---|---|---|"]
    for skill in skills:
        lines.append(
            f"| [{escape_cell(skill.title)}](skills/{skill.name}/SKILL.md) "
            f"| `{skill.name}` | {escape_cell(skill.description)} |"
        )
    return "\n".join(lines) + "\n"


def replace_catalog(readme: str, catalog: str) -> str:
    if readme.count(START) != 1 or readme.count(END) != 1:
        raise CatalogError("README deve conter exatamente um par de marcadores do catálogo.")
    start = readme.index(START) + len(START)
    end = readme.index(END)
    if end < start:
        raise CatalogError("Marcadores do catálogo estão invertidos.")
    return readme[:start] + "\n\n" + catalog + "\n" + readme[end:]


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--check", action="store_true")
    mode.add_argument("--validate-only", action="store_true")
    args = parser.parse_args(argv)
    try:
        skills = discover(args.root)
        path = args.root / "README.md"
        old = path.read_text(encoding="utf-8")
        new = replace_catalog(old, render(skills))
        if args.validate_only:
            print(f"{len(skills)} skill(s) válida(s).")
        elif args.check:
            if old != new:
                raise CatalogError("Catálogo desatualizado. Execute python scripts/catalog.py.")
            print("Catálogo atualizado.")
        elif old != new:
            path.write_text(new, encoding="utf-8")
            print(f"Catálogo atualizado: {len(skills)} skill(s).")
        else:
            print("Catálogo já está atualizado.")
        return 0
    except (CatalogError, OSError, UnicodeError) as exc:
        print(f"Erro: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())

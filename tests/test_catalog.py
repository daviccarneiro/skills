"""Observable behavior of catalog discovery, validation and README updates."""

import contextlib
import io
from pathlib import Path
import shutil
import tempfile
import unittest

from scripts.catalog import CatalogError, START, END, discover, main, render, replace_catalog


class CatalogTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        (self.root / "skills").mkdir()
        self.readme = self.root / "README.md"
        self.original = f"# Minha biblioteca\n\n{START}\nAntigo\n{END}\n\nInstalação manual.\n"
        self.readme.write_text(self.original)

    def skill(self, name="exemplo", description="Faça algo útil.", extra=""):
        path = self.root / "skills" / name / "SKILL.md"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(f"---\nname: {name}\ndescription: {description}\n{extra}---\n\nInstruções.\n")
        return path

    def run_cli(self, *args):
        with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
            return main(["--root", str(self.root), *args])

    def test_minimal_skill_needs_no_extra_directories(self):
        self.skill()
        self.assertEqual(discover(self.root)[0].title, "exemplo")
        self.assertEqual(self.run_cli(), 0)
        self.assertIn("skills/exemplo/SKILL.md", self.readme.read_text())

    def test_add_rename_remove_and_empty_catalog(self):
        first = self.skill("primeira")
        self.run_cli()
        second = self.skill("segunda")
        self.run_cli()
        self.assertIn("skills/segunda/", self.readme.read_text())
        first.parent.rename(first.parent.with_name("renomeada"))
        renamed = first.parent.with_name("renomeada") / "SKILL.md"
        renamed.write_text(renamed.read_text().replace("name: primeira", "name: renomeada"))
        shutil.rmtree(second.parent)
        self.assertEqual(self.run_cli(), 0)
        text = self.readme.read_text()
        self.assertIn("skills/renomeada/", text)
        self.assertNotIn("skills/primeira/", text)
        self.assertNotIn("skills/segunda/", text)
        shutil.rmtree(renamed.parent)
        self.assertEqual(self.run_cli(), 0)
        self.assertIn("Nenhuma skill cadastrada", self.readme.read_text())

    def test_multiline_yaml_titles_and_sorting(self):
        path = self.skill("zeta", ">-\n  Uma descrição\n  em duas linhas.")
        (path.parent / "agents").mkdir()
        (path.parent / "agents/openai.yaml").write_text('interface:\n  display_name: "Árvore"\n')
        self.skill("alfa", extra='metadata:\n  display_name: "A primeira"\n')
        skills = discover(self.root)
        self.assertEqual([s.name for s in skills], ["alfa", "zeta"])
        self.assertEqual(skills[1].description, "Uma descrição em duas linhas.")
        self.assertEqual(skills[1].title, "Árvore")

    def test_portable_title_takes_precedence(self):
        path = self.skill(extra='metadata:\n  display_name: "Portátil"\n')
        (path.parent / "agents").mkdir()
        (path.parent / "agents/openai.yaml").write_text('interface:\n  display_name: "Codex"\n')
        self.assertEqual(discover(self.root)[0].title, "Portátil")

    def test_check_is_read_only_and_update_is_idempotent(self):
        self.skill()
        self.assertEqual(self.run_cli("--check"), 1)
        self.assertEqual(self.readme.read_text(), self.original)
        self.assertEqual(self.run_cli("--validate-only"), 0)
        self.assertEqual(self.readme.read_text(), self.original)
        self.assertEqual(self.run_cli(), 0)
        once = self.readme.read_bytes()
        modified = self.readme.stat().st_mtime_ns
        self.assertEqual(self.run_cli(), 0)
        self.assertEqual(self.readme.read_bytes(), once)
        self.assertEqual(self.readme.stat().st_mtime_ns, modified)
        self.assertEqual(self.run_cli("--check"), 0)
        self.assertTrue(once.decode().startswith("# Minha biblioteca\n\n" + START))
        self.assertTrue(once.decode().endswith(END + "\n\nInstalação manual.\n"))

    def test_invalid_metadata_never_modifies_readme(self):
        path = self.skill()
        bad = [
            "Sem frontmatter",
            "---\nname: exemplo\n---\nTexto",
            "---\nname: outro\ndescription: Descrição\n---\nTexto",
            "---\nname: exemplo\ndescription: 123\n---\nTexto",
            "---\nname: exemplo\ndescription: A\ndescription: B\n---\nTexto",
            "---\nname: exemplo\ndescription: !unknown valor\n---\nTexto",
            "---\nname: exemplo\ndescription: [\n---\nTexto",
            "---\nname: exemplo\ndescription: Texto\n---\n",
            "---\nname: exemplo\ndescription: Texto\nmetadata: []\n---\nTexto",
        ]
        for text in bad:
            with self.subTest(text=text):
                path.write_text(text)
                self.assertEqual(self.run_cli(), 1)
                self.assertEqual(self.readme.read_text(), self.original)

    def test_invalid_names_and_long_description(self):
        for name in ["Maiuscula", "com--hifen", "com_acento", "a" * 65]:
            with self.subTest(name=name):
                path = self.skill(name)
                with self.assertRaises(CatalogError):
                    discover(self.root)
                shutil.rmtree(path.parent)
        self.skill(description="x" * 1025)
        self.assertEqual(self.run_cli(), 1)

    def test_markdown_and_html_cannot_break_table(self):
        self.skill(description="'Texto | [link](https://example.com) <script> **ênfase** `código`'")
        table = render(discover(self.root))
        self.assertEqual(len(table.splitlines()), 3)
        self.assertEqual(table.splitlines()[2].count("|"), 4)
        self.assertNotIn("<script>", table)
        self.assertNotIn("[link]", table)

    def test_invalid_markers_are_rejected(self):
        for text in ["Sem marcadores", START + END + END, END + START]:
            with self.subTest(text=text), self.assertRaises(CatalogError):
                replace_catalog(text, "Tabela\n")

    def test_nonstandard_locations_and_orphan_folders_fail(self):
        orphan = self.root / "skills/incompleta"
        orphan.mkdir()
        self.assertEqual(self.run_cli(), 1)
        orphan.rmdir()
        path = self.skill()
        path.rename(path.with_name("skill.md"))
        self.assertEqual(self.run_cli(), 1)
        path.with_name("skill.md").rename(path)
        nested = path.parent / "nested"
        nested.mkdir()
        (nested / "SKILL.md").write_text(path.read_text())
        self.assertEqual(self.run_cli(), 1)

    def test_symlink_is_rejected(self):
        self.skill()
        (self.root / "skills/externa").symlink_to(self.root, target_is_directory=True)
        self.assertEqual(self.run_cli(), 1)

    def test_crlf_frontmatter_is_supported(self):
        path = self.skill()
        path.write_bytes(path.read_bytes().replace(b"\n", b"\r\n"))
        self.assertEqual(self.run_cli(), 0)

    def test_last_skill_removal_with_no_directory(self):
        self.skill()
        self.run_cli()
        shutil.rmtree(self.root / "skills")
        self.assertEqual(self.run_cli(), 0)
        self.assertIn("Nenhuma skill cadastrada", self.readme.read_text())


if __name__ == "__main__":
    unittest.main()

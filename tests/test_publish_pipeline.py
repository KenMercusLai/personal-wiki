from __future__ import annotations

import hashlib
import os
from pathlib import Path
import subprocess
import struct
import tempfile
import unittest
from unittest import mock
import zlib

from tools.postprocess_publish import ProjectionError, project_wiki
from tools.validate_publish import ValidationError, _assert_casefold_unique, validate_publish
from scripts.verify_pages_output import dynamic_expected_artifacts


ROOT = Path(__file__).resolve().parents[1]


def png_1x1() -> bytes:
    def chunk(kind: bytes, payload: bytes) -> bytes:
        return struct.pack(">I", len(payload)) + kind + payload + struct.pack(">I", zlib.crc32(kind + payload) & 0xFFFFFFFF)
    return (b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR", struct.pack(">IIBBBBB", 1, 1, 8, 6, 0, 0, 0))
            + chunk(b"IDAT", zlib.compress(b"\x00\x00\x00\x00\x00")) + chunk(b"IEND", b""))


def digest_tree(root: Path) -> dict[str, str]:
    return {
        str(path.relative_to(root)): hashlib.sha256(path.read_bytes()).hexdigest()
        for path in sorted(root.rglob("*"))
        if path.is_file()
    }


def write_page(path: Path, front_matter: str, body: str = "正文\n") -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(f"---\n{front_matter}\n---\n\n{body}", encoding="utf-8")


class ProjectionTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.wiki = self.root / "wiki"
        write_page(self.wiki / "_index.md", 'title: "Wiki"')
        write_page(
            self.wiki / "sources" / "example" / "index.md",
            '\n'.join(
                (
                    'title: "Example"',
                    'description: "Example source"',
                    'type: "source"',
                    'author: "Author"',
                    'source_date: "2026-01-01"',
                    'updated: "2026-01-02"',
                    'source_url: "https://example.test/article"',
                    'source_key: "example"',
                    'image_status: "原文没有图片引用"',
                )
            ),
        )
        self.generated = self.root / ".generated" / "wiki"

    def test_projection_is_isolated_cleans_stale_output_and_preserves_canonical(self):
        self.generated.mkdir(parents=True)
        (self.generated / "stale.md").write_text("stale", encoding="utf-8")
        before = digest_tree(self.wiki)

        project_wiki(self.wiki, self.generated)

        self.assertEqual(digest_tree(self.wiki), before)
        self.assertEqual(
            digest_tree(self.generated),
            digest_tree(self.wiki),
        )
        self.assertFalse((self.generated / "stale.md").exists())
        self.assertNotEqual(self.generated.resolve(), self.wiki.resolve())

    def test_projection_rejects_symlinks_without_replacing_prior_output(self):
        self.generated.mkdir(parents=True)
        (self.generated / "prior.md").write_text("prior", encoding="utf-8")
        (self.wiki / "escape.md").symlink_to(self.root / "outside.md")

        with self.assertRaisesRegex(ProjectionError, "symlink is forbidden"):
            project_wiki(self.wiki, self.generated)

        self.assertEqual((self.generated / "prior.md").read_text(), "prior")

    def test_projection_rejects_symlinked_generated_ancestor(self):
        outside = self.root / "outside"
        outside.mkdir()
        generated_parent = self.root / ".generated"
        generated_parent.symlink_to(outside, target_is_directory=True)

        with self.assertRaisesRegex(ProjectionError, "generated path component is a symlink"):
            project_wiki(self.wiki, generated_parent / "wiki")

        self.assertEqual(list(outside.iterdir()), [])

    @unittest.skipUnless(hasattr(os, "mkfifo"), "FIFO is POSIX-specific")
    def test_projection_rejects_special_nodes(self):
        os.mkfifo(self.wiki / "pipe")

        with self.assertRaisesRegex(ProjectionError, "special node is forbidden"):
            project_wiki(self.wiki, self.generated)

    def test_projection_rejects_raw_private_artifacts(self):
        private = self.wiki / "sources" / "example" / "source.original.md"
        private.write_text("raw", encoding="utf-8")

        with self.assertRaisesRegex(ProjectionError, "forbidden canonical artifact"):
            project_wiki(self.wiki, self.generated)

    def test_projection_rejects_active_svg_content(self):
        asset = self.wiki / "sources" / "example" / "diagram.svg"
        asset.write_text('<svg xmlns="http://www.w3.org/2000/svg"><script>alert(1)</script></svg>', encoding="utf-8")

        with self.assertRaisesRegex(ProjectionError, "forbidden canonical artifact"):
            project_wiki(self.wiki, self.generated)

    def test_projection_rejects_private_local_paths_in_markdown(self):
        page = self.wiki / "sources" / "example" / "index.md"
        page.write_text(page.read_text() + "\n/Users/alice/private.md\n", encoding="utf-8")

        with self.assertRaisesRegex(ProjectionError, "private path"):
            project_wiki(self.wiki, self.generated)

    def test_projection_revalidates_the_same_inventory_it_publishes(self):
        page = self.wiki / "sources" / "example" / "index.md"
        page.write_text(
            page.read_text(encoding="utf-8").replace(
                'source_key: "example"', 'source_key: "example"\ndraft: true'
            ),
            encoding="utf-8",
        )
        with self.assertRaisesRegex(ProjectionError, "front matter key"):
            project_wiki(self.wiki, self.generated)
        self.assertFalse(self.generated.exists())

    def test_projection_uses_one_immutable_dirfd_inventory_across_ancestor_swap(self):
        import tools.postprocess_publish as postprocess
        nested = self.wiki / "sources" / "example"
        original = (nested / "index.md").read_bytes()
        real_inventory = __import__("tools.publish_policy", fromlist=["secure_inventory"]).secure_inventory

        def inventory_then_swap(root):
            inventory = real_inventory(root)
            saved = self.root / "saved-example"
            nested.rename(saved)
            outside = self.root / "outside-example"
            outside.mkdir()
            (outside / "index.md").write_bytes(b"attacker bytes")
            nested.symlink_to(outside, target_is_directory=True)
            return inventory

        with mock.patch.object(postprocess, "secure_inventory", side_effect=inventory_then_swap):
            project_wiki(self.wiki, self.generated)

        self.assertEqual((self.generated / "sources" / "example" / "index.md").read_bytes(), original)
        self.assertNotEqual((self.generated / "sources" / "example" / "index.md").read_bytes(), b"attacker bytes")

    def test_projection_detects_generated_ancestor_swap_without_writing_outside(self):
        import tools.postprocess_publish as postprocess
        generated_parent = self.root / ".generated"
        generated_parent.mkdir()
        outside = self.root / "outside-generated"
        outside.mkdir()
        real_write = postprocess._write_inventory

        def write_then_swap(directory_fd, payloads):
            real_write(directory_fd, payloads)
            generated_parent.rename(self.root / "saved-generated")
            generated_parent.symlink_to(outside, target_is_directory=True)

        with mock.patch.object(postprocess, "_write_inventory", side_effect=write_then_swap):
            with self.assertRaisesRegex(ProjectionError, "changed during projection"):
                project_wiki(self.wiki, self.generated)

        self.assertEqual(list(outside.iterdir()), [])


class ValidatorTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.wiki = self.root / "wiki"
        for section in (self.wiki, self.wiki / "sources", self.wiki / "concepts", self.wiki / "entities"):
            write_page(section / "_index.md", f'title: "{section.name}"')

    def add_source(self, key: str = "brand-new-source") -> None:
        write_page(
            self.wiki / "sources" / key / "index.md",
            '\n'.join(
                (
                    'title: "New source"',
                    'description: "A source introduced after this validator."',
                    'type: "source"',
                    'author: "Author"',
                    'source_date: "2026-08-31"',
                    'updated: "2026-08-31"',
                    'source_url: "https://example.test/new"',
                    f'source_key: "{key}"',
                    'image_status: "原文没有图片引用"',
                )
            ),
        )

    def test_validator_discovers_and_accepts_untracked_new_sources(self):
        self.add_source()
        write_page(
            self.wiki / "concepts" / "new-concept.md",
            '\n'.join(
                (
                    'title: "New concept"',
                    'description: "Derived dynamically."',
                    'type: "concept"',
                    'updated: "2026-08-31"',
                    'source_keys: ["brand-new-source"]',
                )
            ),
            '[来源]({{< relref "/wiki/sources/brand-new-source.md" >}})\n',
        )

        report = validate_publish(self.root)

        self.assertEqual(report.source_keys, ("brand-new-source",))
        self.assertEqual(report.pages, 2)

    def test_validator_rejects_remote_markdown_image_references(self):
        self.add_source()
        page = self.wiki / "sources" / "brand-new-source" / "index.md"
        page.write_text(
            page.read_text(encoding="utf-8") + "\n![tracking pixel](https://remote.example/pixel.png)\n",
            encoding="utf-8",
        )

        with self.assertRaisesRegex(ValidationError, "image references must be local validated assets"):
            validate_publish(self.root)

    def test_validator_rejects_reference_style_remote_markdown_image(self):
        self.add_source()
        page = self.wiki / "sources" / "brand-new-source" / "index.md"
        page.write_text(
            page.read_text(encoding="utf-8")
            + "\n![tracking pixel][remote]\n\n[remote]: https://tracker.example/pixel.png\n",
            encoding="utf-8",
        )
        with self.assertRaisesRegex(ValidationError, "unsupported Markdown image syntax"):
            validate_publish(self.root)

    def test_validator_rejects_raw_html_image_markup_case_insensitively(self):
        variants = (
            '<img src="https://tracker.example/pixel.png" alt="tracker">',
            "<IMG ALT='tracker' SRC='//tracker.example/pixel.png'>",
            '<picture><source srcset="https://tracker.example/pixel.webp"></picture>',
        )
        for markup in variants:
            with self.subTest(markup=markup):
                with tempfile.TemporaryDirectory() as temporary:
                    root = Path(temporary)
                    wiki = root / "wiki"
                    for section in (wiki, wiki / "sources", wiki / "concepts", wiki / "entities"):
                        write_page(section / "_index.md", f'title: "{section.name}"')
                    write_page(
                        wiki / "sources" / "example" / "index.md",
                        '\n'.join((
                            'title: "Example"', 'description: "Example"', 'type: "source"',
                            'updated: "2026-08-31"', 'source_key: "example"',
                            'image_status: "none"')),
                        markup,
                    )
                    with self.assertRaisesRegex(ValidationError, "raw image markup"):
                        validate_publish(root)

    def test_validator_rejects_remote_markdown_images_on_derived_pages(self):
        self.add_source()
        write_page(
            self.wiki / "concepts" / "remote-image.md",
            '\n'.join((
                'title: "Remote"', 'description: "Remote image"', 'type: "concept"',
                'updated: "2026-08-31"', 'source_keys: ["brand-new-source"]')),
            '[source]({{< relref "/wiki/sources/brand-new-source.md" >}})\n'
            '![tracker](https://remote.example/tracker.png)',
        )

        with self.assertRaisesRegex(ValidationError, "image references must be local validated assets"):
            validate_publish(self.root)

    def test_validator_rejects_unreferenced_source_assets(self):
        self.add_source()
        (self.wiki / "sources" / "brand-new-source" / "private-screenshot.png").write_bytes(png_1x1())

        with self.assertRaisesRegex(ValidationError, "selected asset is not referenced"):
            validate_publish(self.root)

    def test_validator_rejects_unknown_provenance(self):
        self.add_source()
        write_page(
            self.wiki / "concepts" / "orphan.md",
            '\n'.join(
                (
                    'title: "Orphan"',
                    'description: "Missing provenance."',
                    'type: "concept"',
                    'updated: "2026-08-31"',
                    'source_keys: ["missing-source"]',
                )
            ),
            '[来源]({{< relref "/wiki/sources/missing-source.md" >}})\n',
        )

        with self.assertRaisesRegex(ValidationError, "unknown source_key"):
            validate_publish(self.root)

    def test_validator_accepts_private_source_without_fabricated_public_metadata(self):
        write_page(
            self.wiki / "sources" / "private-note" / "index.md",
            '\n'.join(
                (
                    'title: "Private note"',
                    'description: "A privately supplied source."',
                    'type: "source"',
                    'updated: "2026-08-31"',
                    'source_key: "private-note"',
                    'image_status: "原文没有图片引用"',
                )
            ),
        )

        report = validate_publish(self.root)

        self.assertEqual(report.source_keys, ("private-note",))

    def test_validator_rejects_nonexistent_iso_calendar_date(self):
        self.add_source()
        page = self.wiki / "sources" / "brand-new-source" / "index.md"
        page.write_text(
            page.read_text(encoding="utf-8").replace(
                'updated: "2026-08-31"', 'updated: "2026-02-30"'
            ),
            encoding="utf-8",
        )

        with self.assertRaisesRegex(ValidationError, "invalid updated date"):
            validate_publish(self.root)

    def test_validator_rejects_nonexistent_source_date(self):
        self.add_source()
        page = self.wiki / "sources" / "brand-new-source" / "index.md"
        page.write_text(
            page.read_text(encoding="utf-8").replace(
                'source_date: "2026-08-31"', 'source_date: "2026-99-99"'
            ),
            encoding="utf-8",
        )
        with self.assertRaisesRegex(ValidationError, "invalid source_date"):
            validate_publish(self.root)

    def test_validator_rejects_malformed_quoted_front_matter(self):
        self.add_source()
        page = self.wiki / "sources" / "brand-new-source" / "index.md"
        page.write_text(
            page.read_text(encoding="utf-8").replace(
                'title: "New source"', 'title: "Valid title"junk"'
            ),
            encoding="utf-8",
        )
        with self.assertRaisesRegex(ValidationError, "front matter"):
            validate_publish(self.root)

    def test_validator_enforces_exact_front_matter_value_types(self):
        self.add_source()
        source = self.wiki / "sources" / "brand-new-source" / "index.md"
        original = source.read_text(encoding="utf-8")
        replacements = (
            ('title: "New source"', "title: true"),
            ('author: "Author"', 'author: ["Author"]'),
            ('image_status: "原文没有图片引用"', 'image_status: ["原文没有图片引用"]'),
        )
        for old, new in replacements:
            with self.subTest(field=old.split(":", 1)[0]):
                source.write_text(original.replace(old, new), encoding="utf-8")
                with self.assertRaisesRegex(ValidationError, "front matter schema"):
                    validate_publish(self.root)
        source.write_text(original, encoding="utf-8")

        index = self.wiki / "_index.md"
        index.write_text(index.read_text(encoding="utf-8").replace(
            'title: "wiki"', 'title: "wiki"\nweight: true'
        ), encoding="utf-8")
        with self.assertRaisesRegex(ValidationError, "front matter schema"):
            validate_publish(self.root)

    def test_validator_rejects_casefolded_route_collisions(self):
        with self.assertRaisesRegex(ValidationError, "case-folded path collision"):
            _assert_casefold_unique(
                ["sources/example/index.md", "sources/EXAMPLE/index.md"]
            )

    def test_validator_rejects_every_renderer_owned_front_matter_key(self):
        forbidden = ("url", "aliases", "draft", "outputs", "layout", "slug", "build")
        for key in forbidden:
            with self.subTest(key=key):
                with tempfile.TemporaryDirectory() as temporary:
                    root = Path(temporary)
                    wiki = root / "wiki"
                    for section in (wiki, wiki / "sources", wiki / "concepts", wiki / "entities"):
                        write_page(section / "_index.md", f'title: "{section.name}"')
                    write_page(wiki / "sources" / "example" / "index.md", '\n'.join((
                        'title: "Example"', 'description: "Example"', 'type: "source"',
                        'updated: "2026-08-31"', 'source_key: "example"',
                        'image_status: "none"', f'{key}: "attacker-controlled"')))
                    with self.assertRaisesRegex(ValidationError, "front matter key"):
                        validate_publish(root)

    def test_validator_rejects_index_outside_exact_section_roots(self):
        self.add_source()
        write_page(self.wiki / "sources" / "brand-new-source" / "_index.md", 'title: "Hijack"')
        with self.assertRaisesRegex(ValidationError, "_index.md is only allowed"):
            validate_publish(self.root)

    def test_validator_rejects_noncanonical_page_filenames(self):
        self.add_source()
        write_page(self.wiki / "concepts" / "Bad_Name.md", '\n'.join((
            'title: "Bad"', 'description: "Bad"', 'type: "concept"',
            'updated: "2026-08-31"', 'source_keys: ["brand-new-source"]')),
            '[source]({{< relref "/wiki/sources/brand-new-source.md" >}})')
        with self.assertRaisesRegex(ValidationError, "canonical filename"):
            validate_publish(self.root)

    def test_validator_requires_exact_visible_hugo_relref_provenance(self):
        self.add_source()
        bad_bodies = (
            '/wiki/sources/brand-new-source.md',
            '<!-- [source]({{< relref "/wiki/sources/brand-new-source.md" >}}) -->',
            '`[source]({{< relref "/wiki/sources/brand-new-source.md" >}})`',
            '[source](/wiki/sources/brand-new-source.md)',
        )
        for index, body in enumerate(bad_bodies):
            page = self.wiki / "concepts" / f"bad-{index}.md"
            write_page(page, '\n'.join((
                'title: "Bad"', 'description: "Bad"', 'type: "concept"',
                'updated: "2026-08-31"', 'source_keys: ["brand-new-source"]')), body)
            with self.subTest(body=body), self.assertRaisesRegex(ValidationError, "missing exact visible Hugo relref"):
                validate_publish(self.root)
            page.unlink()

    def test_validator_rejects_fake_image_references_and_invalid_image_bytes(self):
        fake_references = (
            '<!-- ![secret](secret.png) -->',
            '```md\n![secret](secret.png)\n```',
            '[ordinary link](secret.png)',
            'secret.png',
        )
        for body in fake_references:
            with self.subTest(body=body):
                with tempfile.TemporaryDirectory() as temporary:
                    root = Path(temporary)
                    wiki = root / "wiki"
                    for section in (wiki, wiki / "sources", wiki / "concepts", wiki / "entities"):
                        write_page(section / "_index.md", f'title: "{section.name}"')
                    write_page(wiki / "sources" / "example" / "index.md", '\n'.join((
                        'title: "Example"', 'description: "Example"', 'type: "source"',
                        'updated: "2026-08-31"', 'source_key: "example"', 'image_status: "one"')), body)
                    (wiki / "sources" / "example" / "secret.png").write_bytes(b"private text disguised as png")
                    with self.assertRaises(ValidationError):
                        validate_publish(root)

    def test_validator_rejects_mismatched_image_magic_even_when_visibly_referenced(self):
        self.add_source()
        page = self.wiki / "sources" / "brand-new-source" / "index.md"
        page.write_text(page.read_text() + "\n![secret](secret.png)\n", encoding="utf-8")
        (page.parent / "secret.png").write_bytes(b"GIF89a" + b"\x01\x00\x01\x00" + b"not png")
        with self.assertRaisesRegex(ValidationError, "image format does not match"):
            validate_publish(self.root)

    def test_validator_rejects_truncated_header_only_image(self):
        self.add_source()
        page = self.wiki / "sources" / "brand-new-source" / "index.md"
        page.write_text(page.read_text() + "\n![secret](secret.png)\n", encoding="utf-8")
        (page.parent / "secret.png").write_bytes(
            b"\x89PNG\r\n\x1a\n" + b"\x00\x00\x00\rIHDR" + b"\x00\x00\x00\x01\x00\x00\x00\x01"
        )
        with self.assertRaisesRegex(ValidationError, "invalid image encoding"):
            validate_publish(self.root)

    def test_validator_rejects_thirteen_byte_malformed_jpeg(self):
        self.add_source()
        page = self.wiki / "sources" / "brand-new-source" / "index.md"
        page.write_text(page.read_text() + "\n![broken](broken.jpg)\n", encoding="utf-8")
        malformed = b"\xff\xd8\xff\xc0\x00\x07\x08\x00\x01\x00\x01\xff\xd9"
        self.assertEqual(len(malformed), 13)
        (page.parent / "broken.jpg").write_bytes(malformed)

        with self.assertRaisesRegex(ValidationError, "invalid image encoding"):
            validate_publish(self.root)

    def test_repository_validator_accepts_current_live_worktree(self):
        report = validate_publish(ROOT)
        self.assertGreaterEqual(report.pages, 1)
        self.assertGreaterEqual(len(report.source_keys), 1)

    def test_dynamic_artifact_oracle_includes_every_current_route_and_asset(self):
        self.add_source("future-source")
        source = self.wiki / "sources" / "future-source" / "index.md"
        source.write_text(source.read_text() + "\n![one](one.png)\n", encoding="utf-8")
        (source.parent / "one.png").write_bytes(png_1x1())
        write_page(self.wiki / "concepts" / "future-concept.md", '\n'.join((
            'title: "Future"', 'description: "Future"', 'type: "concept"',
            'updated: "2026-08-31"', 'source_keys: ["future-source"]')),
            '[source]({{< relref "/wiki/sources/future-source.md" >}})')

        expected = dynamic_expected_artifacts(self.root)

        self.assertIn("wiki/sources/future-source/index.html", expected)
        self.assertIn("wiki/concepts/future-concept/index.html", expected)
        self.assertIn("wiki/sources/future-source/one.png", expected)
        self.assertIn("wiki/entities/index.html", expected)

    def test_baseline_mode_rejects_deletion_or_route_change_of_prior_page(self):
        self.add_source("conserved-source")
        subprocess.run(["git", "init", "-q"], cwd=self.root, check=True)
        subprocess.run(["git", "config", "user.email", "test@example.test"], cwd=self.root, check=True)
        subprocess.run(["git", "config", "user.name", "Test"], cwd=self.root, check=True)
        subprocess.run(["git", "add", "wiki"], cwd=self.root, check=True)
        subprocess.run(["git", "commit", "-qm", "baseline"], cwd=self.root, check=True)
        (self.wiki / "sources" / "conserved-source" / "index.md").unlink()

        with self.assertRaisesRegex(ValidationError, "canonical conservation violation"):
            validate_publish(self.root, baseline="HEAD")


class RepositoryIntegrationTest(unittest.TestCase):
    def test_build_projects_before_hugo_and_hugo_mounts_only_projection(self):
        build = (ROOT / "build.sh").read_text(encoding="utf-8")
        config = (ROOT / "hugo.toml").read_text(encoding="utf-8")
        projection = "python3 -m tools.postprocess_publish"
        validation = "python3 -m tools.validate_publish"
        hugo = '"${HUGO_BIN}" --gc'
        self.assertIn(validation, build)
        self.assertIn(projection, build)
        self.assertLess(build.index(validation), build.index(projection))
        self.assertLess(build.index(projection), build.index(hugo))
        self.assertIn("source = '.generated/wiki'", config)
        self.assertNotIn("source = 'wiki'", config)
        self.assertIn(".generated/", (ROOT / ".gitignore").read_text(encoding="utf-8"))

    def test_actions_keeps_test_build_verify_upload_deploy_order(self):
        workflow = (ROOT / ".github" / "workflows" / "pages.yml").read_text(encoding="utf-8")
        ordered = (
            "Install JPEG decoder",
            "Run content contract tests",
            "Build Hugo site once",
            "Validate generated site",
            "Upload Pages artifact",
            "Deploy the verified artifact",
        )
        positions = [workflow.index(item) for item in ordered]
        self.assertEqual(positions, sorted(positions))
        self.assertIn("libjpeg-turbo-progs", workflow)

    def test_ingest_protocol_defines_scriptbin_boundaries(self):
        protocol = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
        for requirement in (
            "llm_wiki_ingest",
            "immutable staged input",
            "wiki/**",
            "python3 -m tools.validate_publish",
            "wiki/sources/<slug>/index.md",
            "selected staged assets",
            "raw/private paths",
            "must not commit",
            "--baseline <observed-upstream-commit>",
            "exact visible Hugo `relref`",
            "Route/output controls are forbidden",
            "Do not require or fabricate `author`, `source_date`, or",
        ):
            self.assertIn(requirement, protocol)


if __name__ == "__main__":
    unittest.main()

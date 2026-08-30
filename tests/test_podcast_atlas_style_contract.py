from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parent.parent
CSS = ROOT / "assets" / "css" / "site.css"
BASE = ROOT / "layouts" / "_default" / "baseof.html"
HOME = ROOT / "layouts" / "index.html"
LIST = ROOT / "layouts" / "_default" / "list.html"
SINGLE = ROOT / "layouts" / "_default" / "single.html"


class PodcastAtlasStyleContractTest(unittest.TestCase):
    def test_global_design_tokens_match_podcast_atlas(self):
        css = CSS.read_text(encoding="utf-8")
        required = (
            "/* Source design: Podcast Atlas project layouts, ported 2026-08-30. */",
            "--bg: #fbfbf8;",
            "--fg: #1f2328;",
            "--muted: #666f7a;",
            "--line: #d8dee4;",
            "--link: #0b5cad;",
            "--panel: #ffffff;",
            "width: min(920px, calc(100% - 32px));",
            "font-size: 16px;",
            "font-size: clamp(2rem, 5vw, 3.25rem);",
            ".current-knowledge-grid",
            ".knowledge-collection-grid",
            ".wiki-landing-hero",
            ".wiki-recent-grid",
        )
        for token in required:
            self.assertIn(token, css)

    def test_shell_uses_podcast_atlas_header_and_footer_classes(self):
        base = BASE.read_text(encoding="utf-8")
        for token in (
            'class="site-nav"',
            'class="footer-brand"',
            'class="footer-links"',
            'aria-label="页脚"',
            '原始材料不随网站发布',
        ):
            self.assertIn(token, base)

    def test_page_templates_use_podcast_atlas_component_classes(self):
        home = HOME.read_text(encoding="utf-8")
        listing = LIST.read_text(encoding="utf-8")
        single = SINGLE.read_text(encoding="utf-8")

        for token in (
            'class="wiki-landing-hero"',
            'class="wiki-label"',
            'class="knowledge-collection-grid"',
            'class="knowledge-collection-card"',
        ):
            self.assertIn(token, home)

        for token in (
            'class="wiki-landing-hero"',
            'class="page-list"',
            'class="page-kind"',
        ):
            self.assertIn(token, listing)

        for token in (
            'class="wiki-label"',
            'class="wiki-meta page-meta"',
            'class="content"',
        ):
            self.assertIn(token, single)

        combined = "\n".join((home, listing, single))
        for retired in (
            'class="hero"',
            'class="stats"',
            'class="card-grid"',
            'class="card"',
            'class="prose"',
        ):
            self.assertNotIn(retired, combined)


if __name__ == "__main__":
    unittest.main()

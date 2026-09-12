from __future__ import annotations

from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]


class HugoRenderingConfigTest(unittest.TestCase):
    def test_typographer_is_disabled_to_preserve_canonical_visible_titles(self):
        config = (ROOT / "hugo.toml").read_text(encoding="utf-8")
        self.assertRegex(
            config,
            re.compile(
                r"(?ms)^\s*\[markup\.goldmark\.extensions\]\s*$.*?"
                r"^\s*typographer\s*=\s*false\s*$"
            ),
        )


if __name__ == "__main__":
    unittest.main()

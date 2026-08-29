from __future__ import annotations

import pathlib
import subprocess
import unittest

from scripts.verify_pages_output import (
    find_forbidden_public_files,
    find_private_path_leaks,
    find_private_path_leaks_in_bytes,
    is_generated_text_artifact,
)

ROOT = pathlib.Path(__file__).resolve().parents[1]


class OutputPrivacyTest(unittest.TestCase):
    def test_generated_text_artifact_classification_excludes_binary_images(self):
        self.assertTrue(is_generated_text_artifact(pathlib.Path("index.html")))
        self.assertTrue(is_generated_text_artifact(pathlib.Path("sitemap.xml")))
        self.assertTrue(is_generated_text_artifact(pathlib.Path("robots.txt")))
        self.assertFalse(is_generated_text_artifact(pathlib.Path("image.png")))
        self.assertFalse(is_generated_text_artifact(pathlib.Path("font.woff2")))

    def test_private_path_detector_rejects_cross_platform_and_encoded_paths(self):
        cases = {
            "/Users/alice/Documents/private.md",
            "file:///Users/bob/Library/Mobile%20Documents/source.md",
            "%2FUsers%2Fcarol%2FDocuments%2Fsecret.md",
            "/home/dave/private/source.md",
            r"C:\Users\erin\Documents\private.md",
            r"C:\\Users\\frank\\Documents\\private.md",
            "file:///C:/Users/grace/Documents/private.md",
            "%43%3A%5CUsers%5Chenry%5Cprivate.md",
            "%2525252FUsers%2525252Falice%2525252Fprivate.md",
            "https://example.com)/Users/alice/private.md",
            "https://example.com,/Users/alice/private.md",
            "https://example.com;/Users/alice/private.md",
            "https://example.com!/Users/alice/private.md",
            "https://example.com，/Users/alice/private.md",
            "https://example.com；/Users/alice/private.md",
            "https://example.com！/Users/alice/private.md",
            "~/Documents/private.md",
            "com~apple~CloudDocs/Documents/source.md",
        }
        for value in cases:
            with self.subTest(value=value):
                self.assertTrue(find_private_path_leaks(value), value)

    def test_private_path_detector_allows_public_site_paths(self):
        public_values = {
            "https://example.com/personal-wiki/wiki/source/",
            "https://example.com/users/alice/profile",
            "https://example.com/home/alice/dashboard",
            "https://example.com/%75sers/alice/profile",
            "https://example.com/%68ome/alice/dashboard",
            "/personal-wiki/css/site.css",
            "wiki/sources/example/index.html",
        }
        for value in public_values:
            with self.subTest(value=value):
                self.assertEqual(find_private_path_leaks(value), [], value)

    def test_valid_utf8_with_nul_cannot_bypass_private_path_detection(self):
        raw = b"generated text\x00/Users/alice/Documents/secret.md"
        self.assertTrue(find_private_path_leaks_in_bytes(raw))

    def test_invalid_utf8_cannot_hide_private_paths(self):
        cases = (
            b"\xff/Users/alice/Documents/secret.md",
            b"/Users/alice/Documents/secret.md\xff",
        )
        for raw in cases:
            with self.subTest(raw=raw):
                self.assertTrue(find_private_path_leaks_in_bytes(raw))

    def test_forbidden_public_file_detector_rejects_raw_assets_and_manifests(self):
        paths = [
            "wiki/sources/example/index.md",
            "wiki/sources/example/beec146_MD5.png",
            "wiki/sources/example/asset-manifest.json",
            "raw/source.md",
            "Archive/2026/08/source.md",
        ]
        self.assertEqual(
            find_forbidden_public_files(paths),
            [
                "wiki/sources/example/beec146_MD5.png",
                "wiki/sources/example/asset-manifest.json",
                "raw/source.md",
                "Archive/2026/08/source.md",
            ],
        )

    def test_tracked_tree_contains_no_forbidden_private_artifacts(self):
        output = subprocess.run(
            ["git", "ls-files", "-z"],
            cwd=ROOT,
            check=True,
            capture_output=True,
        ).stdout.decode("utf-8")
        tracked = [path for path in output.split("\0") if path]
        self.assertEqual(find_forbidden_public_files(tracked), [])


if __name__ == "__main__":
    unittest.main()

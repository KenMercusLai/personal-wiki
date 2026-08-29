from __future__ import annotations

import html
import json
import pathlib
import re
import sys
from html.parser import HTMLParser
from urllib.parse import unquote, urlsplit

EXPECTED = {
    "index.html",
    "wiki/index.html",
    "wiki/sources/index.html",
    "wiki/sources/wei-jie-pun-translation-woman-communication/index.html",
    "wiki/concepts/index.html",
    "wiki/concepts/semantic-retrieval-for-pun-translation/index.html",
    "wiki/concepts/functional-equivalence-in-pun-localization/index.html",
    "wiki/concepts/weak-guidance-in-game-localization/index.html",
    "wiki/entities/index.html",
    "wiki/entities/woman-communication/index.html",
    "wiki/entities/wei-jie/index.html",
    "sitemap.xml",
    "robots.txt",
}


class PageParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.canonical: list[str] = []
        self.links: list[str] = []
        self.jsonld: list[str] = []
        self._json = False
        self._buffer: list[str] = []

    def handle_starttag(self, tag, attrs):
        values = dict(attrs)
        rel = values.get("rel") or ""
        href = values.get("href") or ""
        if tag == "link" and "canonical" in rel.split():
            self.canonical.append(href)
        if tag == "a" and href:
            self.links.append(href)
        if tag == "script" and values.get("type") == "application/ld+json":
            self._json = True
            self._buffer = []

    def handle_data(self, data):
        if self._json:
            self._buffer.append(data)

    def handle_endtag(self, tag):
        if tag == "script" and self._json:
            self.jsonld.append("".join(self._buffer))
            self._json = False


def main() -> int:
    public = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "public").resolve()
    errors: list[str] = []
    for rel in EXPECTED:
        if not (public / rel).is_file():
            errors.append(f"missing artifact: {rel}")

    html_files = sorted(public.rglob("*.html"))
    if not html_files:
        errors.append("no HTML files generated")

    parsed_pages: dict[pathlib.Path, PageParser] = {}
    for path in html_files:
        text = path.read_text(encoding="utf-8")
        parser = PageParser()
        parser.feed(text)
        parsed_pages[path] = parser
        rel = path.relative_to(public)
        if len(parser.canonical) != 1:
            errors.append(f"{rel}: expected one canonical, found {len(parser.canonical)}")
        if len(parser.jsonld) != 1:
            errors.append(f"{rel}: expected one JSON-LD block, found {len(parser.jsonld)}")
        for payload in parser.jsonld:
            try:
                data = json.loads(payload)
            except json.JSONDecodeError as exc:
                errors.append(f"{rel}: invalid JSON-LD: {exc}")
                continue
            if parser.canonical and data.get("url") != parser.canonical[0]:
                errors.append(f"{rel}: JSON-LD URL differs from canonical")
        if "![[" in text:
            errors.append(f"{rel}: unresolved private image reference leaked into HTML")

    if parsed_pages:
        root = parsed_pages.get(public / "index.html")
        if root and root.canonical:
            base = root.canonical[0]
            base_parts = urlsplit(base)
            prefix = base_parts.path.rstrip("/") + "/"
            for path, parser in parsed_pages.items():
                rel = path.relative_to(public)
                if parser.canonical:
                    canonical = urlsplit(parser.canonical[0])
                    if (canonical.scheme, canonical.netloc) != (base_parts.scheme, base_parts.netloc):
                        errors.append(f"{rel}: canonical origin mismatch")
                    if not canonical.path.startswith(prefix):
                        errors.append(f"{rel}: canonical escapes project prefix {prefix}")
                for href in parser.links:
                    target = urlsplit(html.unescape(href))
                    if target.scheme or target.netloc or href.startswith("#") or href.startswith("mailto:"):
                        continue
                    decoded = unquote(target.path)
                    if not decoded.startswith(prefix):
                        errors.append(f"{rel}: internal link escapes project prefix: {href}")
                        continue
                    local = decoded[len(prefix):]
                    candidate = public / local
                    if local.endswith("/"):
                        candidate = candidate / "index.html"
                    if not candidate.exists():
                        errors.append(f"{rel}: broken internal link: {href}")

    source_html = public / "wiki/sources/wei-jie-pun-translation-woman-communication/index.html"
    if source_html.is_file():
        rendered = source_html.read_text(encoding="utf-8")
        for phrase in ("语义检索辅助谐音梗翻译", "功能对等与游戏本地化", "游戏文本中的弱引导", "15个图片引用均缺少对应资源"):
            if phrase not in rendered:
                errors.append(f"source page missing expected text: {phrase}")

    if errors:
        print("Generated-site verification failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"Verified {len(html_files)} HTML pages and {len(EXPECTED)} required artifacts.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

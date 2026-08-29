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
    "wiki/sources/wei-jie-pun-translation-woman-communication/semantic-search-candidates.png",
    "wiki/sources/wei-jie-pun-translation-woman-communication/localized-character-name.png",
    "wiki/sources/wei-jie-pun-translation-woman-communication/weak-guidance-japanese.png",
    "wiki/sources/wei-jie-pun-translation-woman-communication/weak-guidance-chinese.jpg",
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

PRIVATE_PATH_PATTERNS = (
    re.compile(r"(?i)(?:file:/+)?/Users/[^/\s<>\"']+/"),
    re.compile(r"(?i)(?:file:/+)?/home/[^/\s<>\"']+/"),
    re.compile(r"(?i)(?:file:/+)?[a-z]:[\\/]+Users[\\/]+[^\\/\s<>\"']+[\\/]"),
    re.compile(r"(?i)(?:^|[\s=\"'(:])~/"),
)
PRIVATE_PATH_MARKERS = (
    "com~apple~CloudDocs",
    "Mobile Documents/com~apple~CloudDocs",
    "98. static/img",
)
PRIVATE_DIRECTORY_NAMES = {"raw", "inbox", "archive", "metadata"}
RAW_IMAGE_SUFFIXES = {".gif", ".jpeg", ".jpg", ".png", ".svg", ".webp"}
GENERATED_TEXT_SUFFIXES = {
    ".css",
    ".csv",
    ".html",
    ".js",
    ".json",
    ".map",
    ".md",
    ".svg",
    ".txt",
    ".webmanifest",
    ".xml",
}
HTTP_URL_PATTERN = re.compile(r"(?i)https?://[^\s<>\"'\[\](){};,!，；！]+")
MAX_DECODE_PASSES = 16


def without_http_url_paths(text: str) -> str:
    query_and_fragment = []

    def replace(match: re.Match[str]) -> str:
        parsed = urlsplit(match.group(0))
        query_and_fragment.extend((parsed.query, parsed.fragment))
        return " "

    remaining = HTTP_URL_PATTERN.sub(replace, text)
    return " ".join((remaining, *query_and_fragment))


def find_private_path_leaks(text: str) -> list[str]:
    normalized = text
    decode_limit_reached = False
    for _ in range(MAX_DECODE_PASSES):
        decoded = unquote(html.unescape(normalized))
        if decoded == normalized:
            break
        normalized = decoded
    else:
        decode_limit_reached = True

    filesystem_text = without_http_url_paths(normalized)
    leaks = [
        match.group(0)
        for pattern in PRIVATE_PATH_PATTERNS
        for match in pattern.finditer(filesystem_text)
    ]
    leaks.extend(
        marker
        for marker in PRIVATE_PATH_MARKERS
        if marker.casefold() in filesystem_text.casefold()
    )
    if decode_limit_reached:
        leaks.append("excessive nested URL/HTML encoding")
    return sorted(set(leaks))


def find_private_path_leaks_in_bytes(raw: bytes) -> list[str]:
    text = raw.decode("utf-8", errors="replace")
    return find_private_path_leaks(text)


def is_generated_text_artifact(path: pathlib.Path) -> bool:
    return path.suffix.casefold() in GENERATED_TEXT_SUFFIXES


def find_forbidden_public_files(paths: list[str]) -> list[str]:
    forbidden = []
    for raw_path in paths:
        path = pathlib.PurePosixPath(raw_path)
        parts = {part.casefold() for part in path.parts}
        name = path.name.casefold()
        if parts & PRIVATE_DIRECTORY_NAMES:
            forbidden.append(raw_path)
        elif name in {"asset-manifest.json", "source.original.md", "source-registry.json"}:
            forbidden.append(raw_path)
        elif path.suffix.casefold() in RAW_IMAGE_SUFFIXES and "_md5" in name:
            forbidden.append(raw_path)
    return forbidden


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

    for path in sorted(
        item
        for item in public.rglob("*")
        if item.is_file() and is_generated_text_artifact(item)
    ):
        try:
            raw = path.read_bytes()
        except OSError:
            continue
        rel = path.relative_to(public)
        for leak in find_private_path_leaks_in_bytes(raw):
            errors.append(f"{rel}: private source path leaked into generated text: {leak}")

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
        for phrase in (
            "语义检索辅助谐音梗翻译",
            "功能对等与游戏本地化",
            "游戏文本中的弱引导",
            "本次图文Ingest已完整读取并检查15个原始图片引用",
            "精选4张公开嵌入",
            "另外11张不嵌入是编辑选择，不代表private分类",
        ):
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

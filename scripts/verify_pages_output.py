from __future__ import annotations

import html
import json
import pathlib
import re
import sys
from html.parser import HTMLParser
from urllib.parse import unquote, urlsplit

REPOSITORY_ROOT = pathlib.Path(__file__).resolve().parents[1]
if str(REPOSITORY_ROOT) not in sys.path:
    sys.path.insert(0, str(REPOSITORY_ROOT))

from tools.validate_publish import ValidationError, validate_publish

BASE_EXPECTED = {
    "index.html",
    "wiki/index.html",
    "wiki/sources/index.html",
    "wiki/concepts/index.html",
    "wiki/entities/index.html",
    "sitemap.xml",
    "robots.txt",
}

def dynamic_expected_artifacts(repository: pathlib.Path | str) -> set[str]:
    """Derive the complete public contract from the current validated canonical tree."""
    report = validate_publish(repository)
    route_artifacts = {f"{route.rstrip('/')}/index.html" for route in report.routes}
    return route_artifacts | set(report.assets)

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


def find_external_image_sources(images: list[tuple[str, str]]) -> list[str]:
    external: list[str] = []
    for src, _alt in images:
        parsed = urlsplit(html.unescape(src))
        if parsed.scheme or parsed.netloc:
            external.append(src)
    return external


class PageParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.canonical: list[str] = []
        self.links: list[str] = []
        self.images: list[tuple[str, str]] = []
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
        src = values.get("src")
        if tag == "img" and isinstance(src, str):
            self.images.append((src, values.get("alt") or ""))
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
    try:
        current_expected = dynamic_expected_artifacts(REPOSITORY_ROOT)
    except ValidationError as exc:
        print(f"Generated-site verification failed:\n- canonical contract invalid: {exc}")
        return 1
    required = BASE_EXPECTED | current_expected
    for rel in required:
        if not (public / rel).is_file():
            errors.append(f"missing artifact: {rel}")

    html_files = sorted(public.rglob("*.html"))
    if not html_files:
        errors.append("no HTML files generated")
    expected_wiki_html = {rel for rel in current_expected if rel.endswith(".html")}
    actual_wiki_html = {
        path.relative_to(public).as_posix()
        for path in html_files
        if path.relative_to(public).parts[:1] == ("wiki",)
    }
    for rel in sorted(actual_wiki_html - expected_wiki_html):
        errors.append(f"unexpected canonical wiki route artifact: {rel}")

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
        for src in find_external_image_sources(parser.images):
            errors.append(f"{rel}: external image source is forbidden: {src}")

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


    if errors:
        print("Generated-site verification failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"Verified {len(html_files)} HTML pages and {len(required)} required baseline + dynamic artifacts.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

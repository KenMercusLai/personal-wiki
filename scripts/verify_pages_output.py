#!/usr/bin/env python3
"""Independently verify the final Personal Wiki GitHub Pages artifact.

This verifier deliberately does not import the preparation scripts or the producer
validator.  It reconstructs the public route, identity, provenance, projection,
and image contracts directly from the checked-in canonical producer mirrors, then
compares those expectations with the final rendered files and DOM.
"""
from __future__ import annotations

import argparse
from collections import defaultdict
import datetime as dt
import hashlib
import html
import json
import pathlib
import re
import sys
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from html.parser import HTMLParser
from urllib.parse import unquote, urljoin, urlsplit

REPOSITORY_ROOT = pathlib.Path(__file__).resolve().parents[1]
SITE_TITLE = "Ken 的个人知识 Wiki"
PUBLIC_SECTIONS = ("concepts", "entities", "sources")
ALPHABETICAL_SECTIONS = ("concepts", "entities")
ALPHABETICAL_BUCKETS = ("0-9", *(chr(code) for code in range(ord("a"), ord("z") + 1)))
KEY_RE = re.compile(r"[A-Za-z0-9][A-Za-z0-9_-]*")
WIKILINK_RE = re.compile(r"\[\[([^\]\n]+)\]\]")

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
    ".css", ".csv", ".html", ".js", ".json", ".map", ".md", ".svg",
    ".txt", ".webmanifest", ".xml",
}
HTTP_URL_PATTERN = re.compile(r"(?i)https?://[^\s<>\"'\[\](){};,!，；！]+")
MAX_DECODE_PASSES = 16


@dataclass(frozen=True)
class CanonicalPage:
    key: str
    title: str
    section: str
    route: str
    metadata: dict[str, object]


@dataclass(frozen=True)
class CanonicalContract:
    pages: tuple[CanonicalPage, ...]
    expected_html: frozenset[str]
    expected_images: dict[str, tuple[bytes, str]]
    synthesis: dict[str, object]
    open_questions: str


@dataclass(frozen=True)
class VerificationReport:
    html_pages: int
    wiki_pages: int
    local_images: int
    file_count: int
    total_bytes: int


@dataclass
class Anchor:
    attrs: dict[str, str]
    text: str = ""
    section: str = ""


@dataclass
class SectionItem:
    section: str
    hrefs: list[str]
    text: str = ""


class PageParser(HTMLParser):
    """Collect the final DOM signals used by the independent verifier."""

    VOID_ELEMENTS = {
        "area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta",
        "param", "source", "track", "wbr",
    }
    TRACKED_SCOPES = {
        "wiki-knowledge-sources", "wiki-knowledge-signals", "current-synthesis",
        "current-synthesis-card",
    }

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.canonical: list[str] = []
        self.og_urls: list[str] = []
        self.og_titles: list[str] = []
        self.descriptions: list[str] = []
        self.links: list[str] = []
        self.anchors: list[Anchor] = []
        self.images: list[dict[str, str]] = []
        self.jsonld: list[str] = []
        self.h1: list[str] = []
        self.elements: list[tuple[str, dict[str, str]]] = []
        self.source_items: list[tuple[str, str, str]] = []
        self.section_items: list[SectionItem] = []
        self.source_sections = 0
        self.source_section_headings: list[str] = []
        self.times_by_scope: dict[str, list[str]] = defaultdict(list)
        self.visible_chunks: list[str] = []
        self.title = ""
        self._title_chunks: list[str] | None = None
        self._h1_chunks: list[str] | None = None
        self._h2_chunks: list[str] | None = None
        self._h2_in_source_scope = False
        self._current_section = ""
        self._anchor: Anchor | None = None
        self._list_items: list[SectionItem] = []
        self._json_chunks: list[str] | None = None
        self._source_key: str | None = None
        self._source_href = ""
        self._source_text: list[str] = []
        self._stack: list[tuple[str, set[str]]] = []
        self._scope_depth: dict[str, int] = defaultdict(int)

    @staticmethod
    def _attrs(attrs: list[tuple[str, str | None]]) -> dict[str, str]:
        return {name.casefold(): value or "" for name, value in attrs}

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        tag = tag.casefold()
        values = self._attrs(attrs)
        entered_scopes = set(values.get("class", "").split()) & self.TRACKED_SCOPES
        for scope in entered_scopes:
            self._scope_depth[scope] += 1
        if tag not in self.VOID_ELEMENTS:
            self._stack.append((tag, entered_scopes))
        if tag == "section" and "wiki-knowledge-sources" in entered_scopes:
            self.source_sections += 1
        self.elements.append((tag, values))
        if tag == "link" and "canonical" in values.get("rel", "").casefold().split():
            self.canonical.append(values.get("href", ""))
        if tag == "meta":
            if values.get("property", "").casefold() == "og:url":
                self.og_urls.append(values.get("content", ""))
            if values.get("property", "").casefold() == "og:title":
                self.og_titles.append(values.get("content", ""))
            if values.get("name", "").casefold() == "description":
                self.descriptions.append(values.get("content", ""))
        if tag == "a":
            anchor = Anchor(values, section=self._current_section)
            self.anchors.append(anchor)
            self._anchor = anchor
            href = values.get("href", "")
            if href:
                self.links.append(href)
                if self._list_items:
                    self._list_items[-1].hrefs.append(href)
            if self._source_key is not None and not self._source_href:
                self._source_href = href
        if tag == "img":
            self.images.append(values)
        if tag == "script" and values.get("type", "").casefold() == "application/ld+json":
            self._json_chunks = []
        if tag == "title":
            self._title_chunks = []
        if tag == "h1":
            self._h1_chunks = []
        if tag == "h2":
            self._h2_chunks = []
            self._h2_in_source_scope = self._scope_depth["wiki-knowledge-sources"] > 0
        if tag == "li":
            self._list_items.append(SectionItem(self._current_section, []))
        if (
            tag == "li"
            and values.get("data-source-key")
            and self._scope_depth["wiki-knowledge-sources"] > 0
        ):
            self._source_key = values["data-source-key"]
            self._source_href = ""
            self._source_text = []
        if tag == "time":
            for scope in self.TRACKED_SCOPES:
                if self._scope_depth[scope] > 0:
                    self.times_by_scope[scope].append(values.get("datetime", ""))

    def handle_startendtag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        self.handle_starttag(tag, attrs)
        self.handle_endtag(tag)

    def handle_data(self, data: str) -> None:
        if data.strip():
            self.visible_chunks.append(data)
        if self._title_chunks is not None:
            self._title_chunks.append(data)
        if self._h1_chunks is not None:
            self._h1_chunks.append(data)
        if self._h2_chunks is not None:
            self._h2_chunks.append(data)
        if self._anchor is not None:
            self._anchor.text += data
        if self._list_items:
            self._list_items[-1].text += data
        if self._json_chunks is not None:
            self._json_chunks.append(data)
        if self._source_key is not None:
            self._source_text.append(data)

    def handle_endtag(self, tag: str) -> None:
        tag = tag.casefold()
        if tag == "title" and self._title_chunks is not None:
            self.title = " ".join("".join(self._title_chunks).split())
            self._title_chunks = None
        if tag == "h1" and self._h1_chunks is not None:
            self.h1.append(" ".join("".join(self._h1_chunks).split()))
            self._h1_chunks = None
        if tag == "h2" and self._h2_chunks is not None:
            heading = " ".join("".join(self._h2_chunks).split())
            self._current_section = heading
            if self._h2_in_source_scope:
                self.source_section_headings.append(heading)
            self._h2_chunks = None
            self._h2_in_source_scope = False
        if tag == "a":
            self._anchor = None
        if tag == "script" and self._json_chunks is not None:
            self.jsonld.append("".join(self._json_chunks))
            self._json_chunks = None
        if tag == "li" and self._source_key is not None:
            self.source_items.append(
                (self._source_key, self._source_href, " ".join("".join(self._source_text).split()))
            )
            self._source_key = None
            self._source_href = ""
            self._source_text = []
        if tag == "li" and self._list_items:
            self.section_items.append(self._list_items.pop())
        for index in range(len(self._stack) - 1, -1, -1):
            if self._stack[index][0] != tag:
                continue
            closed = self._stack[index:]
            del self._stack[index:]
            for _closed_tag, scopes in closed:
                for scope in scopes:
                    self._scope_depth[scope] -= 1
            break

    def elements_with_class(self, class_name: str, tag: str | None = None) -> list[dict[str, str]]:
        return [
            attrs
            for element_tag, attrs in self.elements
            if (tag is None or element_tag == tag)
            and class_name in attrs.get("class", "").split()
        ]

    @property
    def visible_text(self) -> str:
        return " ".join(" ".join(self.visible_chunks).split())


def without_http_url_paths(text: str) -> str:
    query_and_fragment: list[str] = []

    def replace(match: re.Match[str]) -> str:
        try:
            parsed = urlsplit(match.group(0))
        except ValueError:
            return match.group(0)
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
    return find_private_path_leaks(raw.decode("utf-8", errors="replace"))


def is_generated_text_artifact(path: pathlib.Path) -> bool:
    return path.suffix.casefold() in GENERATED_TEXT_SUFFIXES


def find_forbidden_public_files(paths: list[str]) -> list[str]:
    forbidden: list[str] = []
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
        try:
            parsed = urlsplit(html.unescape(src))
        except ValueError:
            external.append(src)
            continue
        if parsed.scheme or parsed.netloc:
            external.append(src)
    return external


def _scalar(raw: str) -> object:
    value = raw.strip()
    if not value:
        return ""
    if value.startswith("[") and value.endswith("]"):
        inner = value[1:-1].strip()
        if not inner:
            return []
        return [_scalar(part) for part in inner.split(",")]
    if len(value) >= 2 and value[0] == value[-1] == '"':
        return json.loads(value)
    if len(value) >= 2 and value[0] == value[-1] == "'":
        return value[1:-1]
    if value in {"true", "false"}:
        return value == "true"
    if re.fullmatch(r"0|[1-9][0-9]*", value):
        return int(value)
    return value


def _front_matter(path: pathlib.Path) -> tuple[dict[str, object], str]:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    if not lines or lines[0] != "---":
        raise ValueError(f"canonical Markdown lacks front matter: {path}")
    try:
        end = lines.index("---", 1)
    except ValueError as exc:
        raise ValueError(f"canonical Markdown has unterminated front matter: {path}") from exc
    metadata: dict[str, object] = {}
    index = 1
    while index < end:
        line = lines[index]
        if not line or line.lstrip().startswith("#"):
            index += 1
            continue
        if line.startswith((" ", "\t")) or ":" not in line:
            raise ValueError(f"unsupported canonical front matter: {path}:{index + 1}")
        key, raw = line.split(":", 1)
        key = key.strip()
        if key in metadata:
            raise ValueError(f"duplicate canonical front-matter key: {path}: {key}")
        if raw.strip():
            metadata[key] = _scalar(raw)
            index += 1
            continue
        values: list[object] = []
        index += 1
        while index < end and lines[index].startswith("  - "):
            values.append(_scalar(lines[index][4:]))
            index += 1
        metadata[key] = values
    return metadata, "\n".join(lines[end + 1 :])


def _wikilink_target(raw: str) -> str:
    return raw.split("|", 1)[0].split("#", 1)[0].strip()


def _load_contract(repository: pathlib.Path) -> CanonicalContract:
    repository = repository.resolve()
    wiki = repository / "wiki"
    assets_root = repository / "wiki-assets"
    if wiki.is_symlink() or not wiki.is_dir() or assets_root.is_symlink() or not assets_root.is_dir():
        raise ValueError("canonical wiki and wiki-assets must be regular directories")
    for owned_root in (wiki, assets_root):
        for path in owned_root.rglob("*"):
            if path.is_symlink():
                raise ValueError(f"canonical producer mirror contains a symlink: {path}")

    pages: list[CanonicalPage] = []
    for section in PUBLIC_SECTIONS:
        directory = wiki / section
        if not directory.is_dir():
            raise ValueError(f"missing canonical section: wiki/{section}")
        for path in sorted(directory.glob("*.md")):
            if not KEY_RE.fullmatch(path.stem):
                raise ValueError(f"invalid canonical key: {path.stem}")
            metadata, _body = _front_matter(path)
            title = metadata.get("title")
            expected_type = {"concepts": "concept", "entities": "entity", "sources": "source"}[section]
            if not isinstance(title, str) or not title.strip() or metadata.get("type") != expected_type:
                raise ValueError(f"invalid canonical identity: {path}")
            pages.append(CanonicalPage(path.stem, title.strip(), section, f"wiki/{section}/{path.stem.casefold()}/", metadata))
    by_key = {page.key: page for page in pages}
    if len(by_key) != len(pages):
        raise ValueError("duplicate canonical Wiki key")
    folded_routes = {page.route.casefold() for page in pages}
    if len(folded_routes) != len(pages):
        raise ValueError("case-folded canonical Wiki route collision")

    for path in sorted(wiki.rglob("*.md")):
        if "_generated" in path.parts or path.name in {"index.md", "log.md", "overview.md"}:
            continue
        for raw in WIKILINK_RE.findall(path.read_text(encoding="utf-8")):
            target = _wikilink_target(raw)
            if target not in by_key:
                raise ValueError(f"canonical wikilink has no target: {path}: {target}")

    expected_images: dict[str, tuple[bytes, str]] = {}
    source_keys = {page.key for page in pages if page.section == "sources"}
    actual_asset_dirs = {path.name for path in assets_root.iterdir() if path.is_dir()}
    if actual_asset_dirs - source_keys:
        raise ValueError(f"orphan canonical image sidecar: {sorted(actual_asset_dirs - source_keys)[0]}")
    for source_key in sorted(actual_asset_dirs):
        directory = assets_root / source_key
        manifest_path = directory / "manifest.json"
        try:
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            raise ValueError(f"invalid canonical image manifest: {source_key}") from exc
        if (
            not isinstance(manifest, dict)
            or manifest.get("version") != 1
            or manifest.get("source_key") != source_key
            or not isinstance(manifest.get("images"), list)
        ):
            raise ValueError(f"invalid canonical image manifest: {source_key}")
        listed: set[str] = set()
        for record in manifest["images"]:
            if not isinstance(record, dict) or set(record) != {"file", "alt"}:
                raise ValueError(f"invalid canonical image record: {source_key}")
            name, alt = record["file"], record["alt"]
            if (
                not isinstance(name, str)
                or pathlib.PurePosixPath(name).name != name
                or not isinstance(alt, str)
                or not alt.strip()
                or name in listed
            ):
                raise ValueError(f"invalid canonical image record: {source_key}")
            image_path = directory / name
            if image_path.is_symlink() or not image_path.is_file():
                raise ValueError(f"missing canonical image: {source_key}/{name}")
            listed.add(name)
            expected_images[f"wiki/sources/{source_key}/{name}"] = (image_path.read_bytes(), alt.strip())
        extras = {path.name for path in directory.iterdir() if path.is_file() and path.name != "manifest.json"} - listed
        if extras:
            raise ValueError(f"unlisted canonical image: {source_key}/{sorted(extras)[0]}")

    expected_html = {"index.html", "wiki/index.html", "wiki/stats/index.html"}
    expected_html.update({
        "wiki/current-synthesis/index.html",
        "wiki/open-questions/index.html",
        "wiki/updates/index.html",
        "wiki/sources/index.html",
    })
    expected_html.update(f"{page.route}index.html" for page in pages)
    for section in ALPHABETICAL_SECTIONS:
        expected_html.add(f"wiki/{section}/index.html")
        expected_html.add(f"wiki/{section}/by-letter/index.html")
        expected_html.update(f"wiki/{section}/by-letter/{bucket}/index.html" for bucket in ALPHABETICAL_BUCKETS)

    overview_meta, overview_body = _front_matter(wiki / "overview.md")
    del overview_meta
    question_marker = "## Open Questions"
    if question_marker not in overview_body:
        raise ValueError("canonical Overview has no Open Questions section")
    open_questions = overview_body.split(question_marker, 1)[1].strip()

    synthesis_path = wiki / "_generated/synthesis/current.md"
    synthesis_meta, synthesis_body = _front_matter_after_marker(synthesis_path)
    manifest_path = wiki / "_generated/synthesis/manifest.json"
    try:
        synthesis_manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ValueError("invalid canonical compact synthesis manifest") from exc
    global_state = synthesis_manifest.get("global") if isinstance(synthesis_manifest, dict) else None
    if (
        not isinstance(global_state, dict)
        or global_state.get("output_digest") != hashlib.sha256(synthesis_path.read_bytes()).hexdigest()
        or synthesis_meta.get("synthesis_source") != "compact"
        or synthesis_meta.get("source_count") != global_state.get("corpus", {}).get("source_count")
    ):
        raise ValueError("canonical compact synthesis differs from its manifest")
    synthesis = {**synthesis_meta, "body": synthesis_body}
    return CanonicalContract(
        tuple(sorted(pages, key=lambda page: page.key)),
        frozenset(expected_html),
        expected_images,
        synthesis,
        open_questions,
    )


def _front_matter_after_marker(path: pathlib.Path) -> tuple[dict[str, object], str]:
    lines = path.read_text(encoding="utf-8").splitlines()
    try:
        start = lines.index("---")
        end = lines.index("---", start + 1)
    except ValueError as exc:
        raise ValueError(f"generated canonical Markdown has invalid front matter: {path}") from exc
    temporary_text = "\n".join(["---", *lines[start + 1 : end], "---", *lines[end + 1 :]]) + "\n"
    # Parse from bytes without sharing the producer or preparation parser.
    metadata: dict[str, object] = {}
    index = 1
    while index < end - start:
        line = temporary_text.splitlines()[index]
        if ":" not in line:
            index += 1
            continue
        key, value = line.split(":", 1)
        metadata[key.strip()] = _scalar(value)
        index += 1
    return metadata, "\n".join(lines[end + 1 :]).strip()


def _expected_url(root_url: str, relative_artifact: str) -> str:
    if relative_artifact == "index.html":
        return root_url
    route = relative_artifact.removesuffix("index.html")
    return urljoin(root_url, route)


def _artifact_for_href(
    href: str,
    *,
    page_url: str,
    root_url: str,
    public: pathlib.Path,
) -> pathlib.Path | None:
    normalized = html.unescape(href)
    if not normalized or normalized.startswith("#"):
        return None
    try:
        absolute = urlsplit(urljoin(page_url, normalized))
        root = urlsplit(root_url)
    except ValueError as exc:
        raise ValueError(f"malformed internal URL {href!r}: {exc}") from exc
    if absolute.scheme not in {"http", "https"}:
        return None
    if (absolute.scheme, absolute.netloc) != (root.scheme, root.netloc):
        return None
    prefix = root.path
    if not prefix.endswith("/"):
        prefix += "/"
    path = unquote(absolute.path)
    if not path.startswith(prefix):
        raise ValueError(f"internal URL escapes deployment prefix: {href}")
    local = path[len(prefix) :]
    candidate = public / local
    if not local or local.endswith("/"):
        candidate /= "index.html"
    try:
        candidate.resolve().relative_to(public.resolve())
    except ValueError as exc:
        raise ValueError(f"internal URL escapes artifact: {href}") from exc
    return candidate


def _parse_page(path: pathlib.Path) -> PageParser:
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError as exc:
        raise ValueError(f"HTML is not UTF-8: {path}") from exc
    parser = PageParser()
    parser.feed(text)
    parser.close()
    return parser


def _require_one(values: list[str], label: str, relative: str) -> str:
    if len(values) != 1 or not values[0]:
        raise ValueError(f"{relative}: expected exactly one {label}, found {len(values)}")
    return values[0]


def _verify_identity_page(
    page: CanonicalPage,
    parser: PageParser,
    root_url: str,
    relative: str,
) -> None:
    expected_title = f"{page.title} · {SITE_TITLE}"
    if parser.title != expected_title:
        raise ValueError(f"{relative}: document title does not preserve canonical identity")
    if parser.h1 != [page.title]:
        raise ValueError(f"{relative}: H1 does not preserve canonical identity")
    if _require_one(parser.og_titles, "Open Graph title", relative) != expected_title:
        raise ValueError(f"{relative}: Open Graph title does not preserve canonical identity")
    try:
        schema = json.loads(_require_one(parser.jsonld, "JSON-LD block", relative))
    except json.JSONDecodeError as exc:
        raise ValueError(f"{relative}: invalid JSON-LD: {exc}") from exc
    if not isinstance(schema, dict) or schema.get("name") != expected_title:
        raise ValueError(f"{relative}: JSON-LD name does not preserve canonical identity")

    if page.section in {"concepts", "entities"} and page.metadata.get("knowledge_schema") == "synthesis-v1":
        sources = page.metadata.get("sources")
        if not isinstance(sources, list) or not sources or not all(isinstance(key, str) for key in sources):
            raise ValueError(f"invalid canonical synthesis source inventory: {page.key}")
        signals = parser.elements_with_class("wiki-knowledge-signals", "p")
        if len(signals) != 1:
            raise ValueError(f"{relative}: missing synthesis-v1 knowledge signal")
        signal = signals[0]
        if signal.get("data-knowledge-schema") != "synthesis-v1" or signal.get("data-source-count") != str(len(dict.fromkeys(sources))):
            raise ValueError(f"{relative}: source-derived knowledge signal mismatch")
        expected_items = []
        for key in sources:
            route = f"wiki/sources/{key.casefold()}/"
            expected_items.append((key, urljoin(root_url, route), key))
        if parser.source_sections != 1 or parser.source_section_headings != ["Sources"]:
            raise ValueError(f"{relative}: source inventory is not scoped to exactly one Sources section")
        if len(parser.source_items) != len(expected_items):
            raise ValueError(f"{relative}: source inventory is incomplete")
        for (actual_key, href, visible), (key, expected_href, _label) in zip(parser.source_items, expected_items):
            if actual_key != key or urljoin(_require_one(parser.canonical, "canonical", relative), href) != expected_href:
                raise ValueError(f"{relative}: source inventory link mismatch: {key}")
            if not visible:
                raise ValueError(f"{relative}: source inventory has an empty visible label")
        updated = page.metadata.get("last_updated")
        if (
            not isinstance(updated, str)
            or parser.times_by_scope["wiki-knowledge-signals"] != [updated]
        ):
            raise ValueError(f"{relative}: source-derived update date mismatch")

        canonical = _require_one(parser.canonical, "canonical", relative)
        evidence_items = [item for item in parser.section_items if item.section == "Evidence"]
        expected_source_urls = {item[1] for item in expected_items}
        if not evidence_items or any(
            not item.hrefs
            or not any(urljoin(canonical, href) in expected_source_urls for href in item.hrefs)
            for item in evidence_items
        ):
            raise ValueError(f"{relative}: each Evidence item must contain a canonical source anchor")
        relationship = "Related Concepts" if page.section == "concepts" else "Relationships"
        relationship_items = [item for item in parser.section_items if item.section == relationship]
        if not relationship_items or any(not item.hrefs for item in relationship_items):
            raise ValueError(f"{relative}: each {relationship} item must contain a relationship anchor")


def _verify_images(
    contract: CanonicalContract,
    parsers: dict[str, PageParser],
    public: pathlib.Path,
    root_url: str,
) -> None:
    actual_image_files = {
        path.relative_to(public).as_posix()
        for path in public.rglob("*")
        if path.is_file()
        and path.suffix.casefold() in RAW_IMAGE_SUFFIXES
        and path.relative_to(public).parts[:2] == ("wiki", "sources")
    }
    if actual_image_files != set(contract.expected_images):
        raise ValueError(
            "public source image inventory mismatch: "
            f"missing={sorted(set(contract.expected_images) - actual_image_files)}, "
            f"unexpected={sorted(actual_image_files - set(contract.expected_images))}"
        )
    by_source: dict[str, list[tuple[str, str]]] = {}
    for relative, (expected_bytes, expected_alt) in contract.expected_images.items():
        path = public / relative
        if path.read_bytes() != expected_bytes:
            raise ValueError(f"public image bytes differ from canonical sidecar: {relative}")
        source_key = pathlib.PurePosixPath(relative).parts[2]
        by_source.setdefault(source_key, []).append((path.name, expected_alt))
    for source_key, expected in sorted(by_source.items()):
        page_relative = f"wiki/sources/{source_key}/index.html"
        parser = parsers[page_relative]
        actual = []
        page_url = _require_one(parser.canonical, "canonical", page_relative)
        for image in parser.images:
            src = image.get("src", "")
            if find_external_image_sources([(src, image.get("alt", ""))]):
                raise ValueError(f"{page_relative}: external image source is forbidden: {src}")
            target = _artifact_for_href(src, page_url=page_url, root_url=root_url, public=public)
            if target is None:
                raise ValueError(f"{page_relative}: invalid local image source: {src}")
            actual.append((target.name, image.get("alt", "")))
        if actual != expected:
            raise ValueError(f"{page_relative}: rendered image order or alt text differs from canonical manifest")


def _verify_projection(contract: CanonicalContract, parsers: dict[str, PageParser], root_url: str) -> None:
    detail_rel = "wiki/current-synthesis/index.html"
    landing_rel = "wiki/index.html"
    detail = parsers[detail_rel]
    landing = parsers[landing_rel]
    detail_markers = detail.elements_with_class("current-synthesis", "article")
    card_markers = landing.elements_with_class("current-synthesis-card", "article")
    if len(detail_markers) != 1 or len(card_markers) != 1:
        raise ValueError("Current Synthesis detail/card artifact markers are missing")
    summary = str(contract.synthesis.get("summary", ""))
    source_count = str(contract.synthesis.get("source_count", ""))
    for label, marker in (("detail", detail_markers[0]), ("card", card_markers[0])):
        if marker.get("data-synthesis-source") != "compact":
            raise ValueError(f"Current Synthesis {label} source marker mismatch")
        if marker.get("data-summary") != summary or marker.get("data-source-count") != source_count:
            raise ValueError(f"Current Synthesis {label} derived metadata mismatch")
    updated = str(contract.synthesis.get("last_updated", ""))
    try:
        parsed_updated = dt.date.fromisoformat(updated)
    except ValueError as exc:
        raise ValueError("canonical Current Synthesis date is invalid") from exc
    del parsed_updated
    if detail.times_by_scope["current-synthesis"] != [updated]:
        raise ValueError("Current Synthesis detail date mismatch")
    if landing.times_by_scope["current-synthesis-card"] != [updated]:
        raise ValueError("Current Synthesis card date mismatch")
    for required_heading in ("Executive Summary", "Synthesis by Domain"):
        if required_heading not in detail.visible_text:
            raise ValueError(f"Current Synthesis detail is missing {required_heading}")
    open_page = parsers["wiki/open-questions/index.html"]
    for line in contract.open_questions.splitlines():
        visible = line.removeprefix("-").strip()
        if visible and visible not in open_page.visible_text:
            raise ValueError(f"Open Questions projection omitted canonical text: {visible}")
    expected_projection_links = {
        urljoin(root_url, "wiki/current-synthesis/"),
        urljoin(root_url, "wiki/open-questions/"),
        urljoin(root_url, "wiki/updates/"),
    }
    landing_url = _require_one(landing.canonical, "canonical", landing_rel)
    actual_links = {urljoin(landing_url, anchor.attrs.get("href", "")) for anchor in landing.anchors}
    if not expected_projection_links.issubset(actual_links):
        raise ValueError("Wiki landing is missing a projected knowledge route")


def _verify_directory_identity(contract: CanonicalContract, parsers: dict[str, PageParser], root_url: str) -> None:
    for page in contract.pages:
        if page.section in ALPHABETICAL_SECTIONS:
            bucket = next(
                (char.casefold() for char in page.key if char.isascii() and char.isalpha()),
                "0-9",
            )
            directories = [
                f"wiki/{page.section}/index.html",
                f"wiki/{page.section}/by-letter/{bucket}/index.html",
            ]
        else:
            directories = ["wiki/sources/index.html"]
        expected_url = urljoin(root_url, page.route)
        for relative in directories:
            parser = parsers[relative]
            found = [
                anchor
                for anchor in parser.anchors
                if urljoin(_require_one(parser.canonical, "canonical", relative), anchor.attrs.get("href", "")) == expected_url
            ]
            if len(found) != 1 or " ".join(found[0].text.split()) != page.title:
                raise ValueError(f"{relative}: directory label/link does not preserve {page.key}")


def verify_site(public: pathlib.Path | str, repository: pathlib.Path | str = REPOSITORY_ROOT) -> VerificationReport:
    public = pathlib.Path(public).resolve()
    repository = pathlib.Path(repository).resolve()
    if public.is_symlink() or not public.is_dir():
        raise ValueError(f"not a regular public directory: {public}")
    contract = _load_contract(repository)

    all_paths = sorted(public.rglob("*"))
    for path in all_paths:
        if path.is_symlink():
            raise ValueError(f"symbolic link not allowed in public artifact: {path.relative_to(public)}")
    files = [path for path in all_paths if path.is_file()]
    relative_files = [path.relative_to(public).as_posix() for path in files]
    forbidden = find_forbidden_public_files(relative_files)
    if forbidden:
        raise ValueError(f"forbidden public file: {forbidden[0]}")

    actual_html = {
        path.relative_to(public).as_posix()
        for path in files
        if path.suffix.casefold() == ".html"
    }
    if actual_html != set(contract.expected_html):
        raise ValueError(
            "HTML route artifact mismatch: "
            f"missing={sorted(set(contract.expected_html) - actual_html)}, "
            f"unexpected={sorted(actual_html - set(contract.expected_html))}"
        )
    for hidden in (
        "wiki/index/index.html",
        "wiki/log/index.html",
        "wiki/overview/index.html",
        "wiki/_generated/index.html",
        "wiki-projections/index.html",
    ):
        if (public / hidden).exists():
            raise ValueError(f"private or namespace route was rendered: {hidden}")

    parsers = {relative: _parse_page(public / relative) for relative in sorted(actual_html)}
    root = parsers["index.html"]
    root_url = _require_one(root.canonical, "canonical", "index.html")
    try:
        root_parts = urlsplit(root_url)
    except ValueError as exc:
        raise ValueError(f"invalid site-root canonical: {exc}") from exc
    if root_parts.scheme not in {"http", "https"} or not root_parts.netloc or not root_parts.path.endswith("/"):
        raise ValueError(f"invalid site-root canonical: {root_url}")

    pages_by_relative = {f"{page.route}index.html": page for page in contract.pages}
    for relative, parser in parsers.items():
        expected_url = _expected_url(root_url, relative)
        canonical = _require_one(parser.canonical, "canonical", relative)
        og_url = _require_one(parser.og_urls, "Open Graph URL", relative)
        description = _require_one(parser.descriptions, "meta description", relative)
        if canonical != expected_url or og_url != expected_url:
            raise ValueError(f"{relative}: canonical/Open Graph URL mismatch for deployment prefix")
        try:
            schema = json.loads(_require_one(parser.jsonld, "JSON-LD block", relative))
        except json.JSONDecodeError as exc:
            raise ValueError(f"{relative}: invalid JSON-LD: {exc}") from exc
        if (
            not isinstance(schema, dict)
            or schema.get("@context") != "https://schema.org"
            or schema.get("url") != expected_url
            or schema.get("description") != description
        ):
            raise ValueError(f"{relative}: JSON-LD metadata differs from rendered metadata")
        if schema.get("name") != parser.title:
            raise ValueError(f"{relative}: JSON-LD name differs from the document title")
        raw = (public / relative).read_bytes()
        if b"[[" in raw or b"![[" in raw:
            raise ValueError(f"{relative}: unresolved canonical syntax leaked into HTML")
        for image in parser.images:
            src = image.get("src", "")
            external = find_external_image_sources([(src, image.get("alt", ""))])
            if external:
                raise ValueError(f"{relative}: external image source is forbidden: {external[0]}")
        for href in parser.links:
            target = _artifact_for_href(href, page_url=canonical, root_url=root_url, public=public)
            if target is not None and not target.exists():
                raise ValueError(f"{relative}: unresolved internal URL: {href}")
        page = pages_by_relative.get(relative)
        if page is not None:
            _verify_identity_page(page, parser, root_url, relative)

    _verify_images(contract, parsers, public, root_url)
    _verify_projection(contract, parsers, root_url)
    _verify_directory_identity(contract, parsers, root_url)

    sitemap_path = public / "sitemap.xml"
    if not sitemap_path.is_file():
        raise ValueError("missing artifact: sitemap.xml")
    try:
        sitemap = ET.parse(sitemap_path)
    except ET.ParseError as exc:
        raise ValueError(f"invalid sitemap XML: {exc}") from exc
    sitemap_urls = {
        element.text.strip()
        for element in sitemap.getroot().iter()
        if element.tag.rsplit("}", 1)[-1] == "loc" and element.text
    }
    expected_urls = {_expected_url(root_url, relative) for relative in contract.expected_html}
    if sitemap_urls != expected_urls:
        raise ValueError(
            "sitemap route coverage mismatch: "
            f"missing={sorted(expected_urls - sitemap_urls)}, unexpected={sorted(sitemap_urls - expected_urls)}"
        )

    for path in files:
        if not is_generated_text_artifact(path):
            continue
        raw = path.read_bytes()
        decoded = raw.decode("utf-8")
        for _ in range(16):
            unescaped = html.unescape(decoded)
            if unescaped == decoded:
                break
            decoded = unescaped
        else:
            raise ValueError(
                f"{path.relative_to(public)}: excessive entity encoding in generated text"
            )
        if "[[" in decoded:
            raise ValueError(
                f"{path.relative_to(public)}: unresolved canonical syntax leaked into generated text"
            )
        for leak in find_private_path_leaks_in_bytes(raw):
            raise ValueError(
                f"{path.relative_to(public)}: private source path leaked into generated text: {leak}"
            )

    total_bytes = sum(path.stat().st_size for path in files)
    if total_bytes > 1024 ** 3:
        raise ValueError("artifact exceeds the GitHub Pages 1 GiB supported limit")
    wiki_pages = sum(relative.startswith("wiki/") for relative in actual_html)
    return VerificationReport(
        html_pages=len(actual_html),
        wiki_pages=wiki_pages,
        local_images=len(contract.expected_images),
        file_count=len(files),
        total_bytes=total_bytes,
    )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("public_dir", nargs="?", type=pathlib.Path, default=pathlib.Path("public"))
    parser.add_argument("--repository", type=pathlib.Path, default=REPOSITORY_ROOT)
    args = parser.parse_args(argv)
    try:
        report = verify_site(args.public_dir, args.repository)
    except (OSError, UnicodeError, ValueError) as exc:
        print(f"Generated-site verification failed:\n- {exc}", file=sys.stderr)
        return 1
    print(
        "Verified independent final artifact: "
        f"html_pages={report.html_pages}, wiki_pages={report.wiki_pages}, "
        f"local_images={report.local_images}, files={report.file_count}, bytes={report.total_bytes}."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

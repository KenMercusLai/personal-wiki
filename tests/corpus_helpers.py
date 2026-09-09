from __future__ import annotations

import json
from pathlib import Path
import re
import shutil
import subprocess

PUBLIC_SECTIONS = ("concepts", "entities", "sources")
LETTER_BUCKETS = ("0-9", *tuple("abcdefghijklmnopqrstuvwxyz"))
SYNTHESIS_H2 = {
    "concepts": (
        "Definition",
        "Current Synthesis",
        "Key Claims",
        "Evidence",
        "Counterevidence & Qualifications",
        "What Changed",
        "Related Concepts",
    ),
    "entities": (
        "Overview",
        "Current Profile",
        "Key Characteristics",
        "Evidence",
        "Qualifications",
        "What Changed",
        "Relationships",
    ),
}
TEST_CONCEPT_KEY = "ConsumerContractConcept"
TEST_ENTITY_KEY = "ConsumerContractEntity"


def front_matter(path: Path) -> tuple[dict[str, object], str]:
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0] != "---":
        raise AssertionError(f"missing front matter: {path}")
    end = lines.index("---", 1)
    metadata: dict[str, object] = {}
    index = 1
    while index < end:
        line = lines[index]
        if not line or line.lstrip().startswith("#"):
            index += 1
            continue
        key, raw = line.split(":", 1)
        key = key.strip()
        raw = raw.strip()
        if raw:
            if len(raw) >= 2 and raw[0] == raw[-1] == '"':
                metadata[key] = json.loads(raw)
            elif raw in {"true", "false"}:
                metadata[key] = raw == "true"
            elif re.fullmatch(r"[0-9]+", raw):
                metadata[key] = int(raw)
            else:
                metadata[key] = raw
            index += 1
            continue
        values: list[str] = []
        index += 1
        while index < end and lines[index].startswith("  - "):
            values.append(lines[index][4:].strip().strip('"'))
            index += 1
        metadata[key] = values
    return metadata, "\n".join(lines[end + 1 :])


def canonical_pages(root: Path, section: str | None = None) -> list[tuple[str, str, str, dict[str, object]]]:
    sections = (section,) if section else PUBLIC_SECTIONS
    pages: list[tuple[str, str, str, dict[str, object]]] = []
    for current in sections:
        for path in sorted((root / "wiki" / current).glob("*.md")):
            metadata, _ = front_matter(path)
            pages.append((path.stem, str(metadata["title"]), current, metadata))
    return pages


def synthesis_pages(root: Path, section: str | None = None) -> list[tuple[str, str, str, dict[str, object]]]:
    return [
        page
        for page in canonical_pages(root, section)
        if page[2] in SYNTHESIS_H2 and page[3].get("knowledge_schema") == "synthesis-v1"
    ]


def synthesis_topic_ids(root: Path) -> list[str]:
    manifest = json.loads(
        (root / "wiki/_generated/synthesis/manifest.json").read_text(encoding="utf-8")
    )
    topics = manifest["topics"]
    if not isinstance(topics, dict) or not topics:
        raise AssertionError("canonical synthesis manifest has no topics")
    return sorted(topics)


def expected_html_routes(root: Path) -> set[str]:
    """Derive the complete public HTML route inventory from canonical inputs."""
    routes = {
        "/",
        "/wiki/",
        "/wiki/current-synthesis/",
        "/wiki/open-questions/",
        "/wiki/stats/",
        "/wiki/updates/",
        "/wiki/sources/",
    }
    for section in ("concepts", "entities"):
        routes.add(f"/wiki/{section}/")
        routes.add(f"/wiki/{section}/by-letter/")
        routes.update(f"/wiki/{section}/by-letter/{bucket}/" for bucket in LETTER_BUCKETS)
    for key, _title, section, metadata in canonical_pages(root):
        if section == "sources":
            source_key = metadata.get("source_key")
            if not isinstance(source_key, str) or not source_key:
                raise AssertionError(f"canonical source {key} has no source_key")
            routes.add(f"/wiki/sources/{source_key}/")
        else:
            routes.add(f"/wiki/{section}/{key.casefold()}/")
    return routes


def image_records(root: Path) -> list[tuple[str, str, str]]:
    records: list[tuple[str, str, str]] = []
    for manifest_path in sorted((root / "wiki-assets").glob("*/manifest.json")):
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        for image in manifest["images"]:
            records.append((manifest_path.parent.name, image["file"], image["alt"]))
    return records


def ensure_image_record(root: Path) -> tuple[str, str, str]:
    records = image_records(root)
    if records:
        return records[0]
    sources = canonical_pages(root, "sources")
    if not sources:
        raise AssertionError("image fixture requires one canonical source")
    source_key = sources[0][0]
    directory = root / "wiki-assets" / source_key
    directory.mkdir(parents=True, exist_ok=True)
    filename = "0000-consumer-contract.gif"
    alt = "Synthetic one-pixel image used only by consumer contract tests"
    # Complete, valid 1x1 GIF89a. The temporary fixture never enters managed inputs.
    (directory / filename).write_bytes(bytes.fromhex(
        "47494638396101000100800000000000ffffff21f90401000000002c00000000010001000002024401003b"
    ))
    (directory / "manifest.json").write_text(
        json.dumps(
            {"version": 1, "source_key": source_key, "images": [{"file": filename, "alt": alt}]},
            ensure_ascii=False,
            indent=2,
            sort_keys=True,
        )
        + "\n",
        encoding="utf-8",
    )
    return source_key, filename, alt


def duplicate_scalar_key(text: str, *, nested: bool) -> str:
    indentation = r" {4,}" if nested else r" {2}"
    pattern = re.compile(
        rf'(?m)^(?P<indent>{indentation})(?P<field>"(?:[^"\\]|\\.)+": '
        r'(?:"(?:[^"\\]|\\.)*"|true|false|null|-?[0-9]+(?:\.[0-9]+)?))(?P<comma>,?)$'
    )
    match = pattern.search(text)
    if match is None:
        raise AssertionError("JSON fixture has no duplicate-key mutation target")
    indent, field, comma = match.group("indent", "field", "comma")
    replacement = f"{indent}{field},\n{indent}{field}{comma}"
    return text[: match.start()] + replacement + text[match.end() :]


def replace_scalar_with_constant(text: str, constant: str, *, nested: bool = False) -> str:
    indentation = r" {4,}" if nested else r" {2}"
    pattern = re.compile(
        rf'(?m)^(?P<indent>{indentation})(?P<key>"(?:[^"\\]|\\.)+": )'
        r'(?P<value>"(?:[^"\\]|\\.)*"|true|false|null|-?[0-9]+(?:\.[0-9]+)?)(?P<comma>,?)$'
    )
    match = pattern.search(text)
    if match is None:
        raise AssertionError("JSON fixture has no constant mutation target")
    return text[: match.start("value")] + constant + text[match.end("value") :]


def _test_page(title: str, page_type: str, source_key: str, relation_key: str) -> str:
    section = "concepts" if page_type == "concept" else "entities"
    relationship = "Related Concepts" if page_type == "concept" else "Relationships"
    headings = SYNTHESIS_H2[section]
    blocks = {
        headings[0]: f"A deterministic synthetic {page_type} used only by consumer contract tests.",
        headings[1]: "The fixture exercises rendered schema validation independently of the canonical corpus.",
        headings[2]: "- The consumer must preserve canonical identity and provenance.",
        "Evidence": f"- Fixture evidence - [[{source_key}]] is the canonical source for this test page.",
        headings[4]: "This fixture makes no semantic claim about the canonical corpus.",
        "What Changed": "- Added an isolated consumer-test schema fixture.",
        relationship: f"- [[{relation_key}]] - deterministic relationship target.",
    }
    body = "\n\n".join(f"## {heading}\n\n{blocks[heading]}" for heading in headings)
    return (
        "---\n"
        f'title: {json.dumps(title)}\n'
        f"type: {page_type}\n"
        "tags: [consumer-contract-test]\n"
        "sources:\n"
        f"  - {source_key}\n"
        "last_updated: 2000-01-01\n"
        "knowledge_schema: synthesis-v1\n"
        "---\n\n"
        f"{body}\n"
    )


def build_schema_fixture(source_root: Path, destination: Path) -> tuple[Path, Path, str, str, str, str]:
    ignore = shutil.ignore_patterns(".git", ".generated", "public", "resources", ".cache", "__pycache__")
    shutil.copytree(source_root, destination, ignore=ignore)
    cache = source_root / ".cache"
    if cache.exists():
        (destination / ".cache").symlink_to(cache, target_is_directory=True)
    sources = canonical_pages(destination, "sources")
    if not sources:
        raise AssertionError("schema fixture requires one canonical source")
    source_key, source_title, _, _ = sources[0]
    existing = {page[0] for page in canonical_pages(destination)}
    concept_key = TEST_CONCEPT_KEY
    while concept_key in existing:
        concept_key += "Fixture"
    existing.add(concept_key)
    entity_key = TEST_ENTITY_KEY
    while entity_key in existing:
        entity_key += "Fixture"
    (destination / "wiki/concepts" / f"{concept_key}.md").write_text(
        _test_page("Consumer Contract Concept", "concept", source_key, entity_key),
        encoding="utf-8",
    )
    entity_dir = destination / "wiki/entities"
    entity_dir.mkdir(parents=True, exist_ok=True)
    (entity_dir / f"{entity_key}.md").write_text(
        _test_page("Consumer Contract Entity", "entity", source_key, concept_key),
        encoding="utf-8",
    )
    ensure_image_record(destination)
    subprocess.run(
        ["./build.sh"],
        cwd=destination,
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
    )
    return destination, destination / "public", source_key, source_title, concept_key, entity_key

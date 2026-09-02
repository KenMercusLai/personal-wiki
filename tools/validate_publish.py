from __future__ import annotations

import argparse
from dataclasses import dataclass
from datetime import date
import json
import re
import subprocess
import sys
from pathlib import Path, PurePosixPath
from urllib.parse import urlsplit

from .publish_policy import markdown_image_targets, secure_inventory, validate_canonical_file, visible_markdown

KEY_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
SOURCE_DATE_PREFIX_RE = re.compile(r"^(\d{4})(?:-(\d{2})(?:-(\d{2}))?)?")
SCALAR_RE = re.compile(r'^([A-Za-z_][A-Za-z0-9_]*):\s*(.*)$')
ALLOWED_INDEXES = {PurePosixPath("_index.md"), PurePosixPath("sources/_index.md"), PurePosixPath("concepts/_index.md"), PurePosixPath("entities/_index.md")}
INDEX_KEYS = {"title", "description", "weight"}
SOURCE_KEYS = {"title", "description", "type", "updated", "source_key", "author", "translator", "source_date", "source_url", "featured"}
CONCEPT_KEYS = {"title", "description", "type", "updated", "source_keys", "featured"}
ENTITY_KEYS = CONCEPT_KEYS | {"entity_kind"}
STRING_FIELDS = {
    "title", "description", "type", "updated", "source_key",
    "author", "translator", "source_date", "source_url", "entity_kind",
}


class ValidationError(ValueError):
    """The live canonical wiki violates its publication contract."""


@dataclass(frozen=True)
class ValidationReport:
    pages: int
    source_keys: tuple[str, ...]
    routes: tuple[str, ...]
    assets: tuple[str, ...]
    canonical_pages: tuple[str, ...]


def _front_matter(path: PurePosixPath, data: bytes) -> tuple[dict[str, object], str]:
    try:
        text = data.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise ValidationError(f"canonical Markdown is not UTF-8: {path}") from exc
    if not text.startswith("---\n") or "\n---\n" not in text[4:]:
        raise ValidationError(f"missing YAML front matter: {path}")
    raw, body = text[4:].split("\n---\n", 1)
    values: dict[str, object] = {}
    for line in raw.splitlines():
        match = SCALAR_RE.fullmatch(line)
        if match is None:
            raise ValidationError(f"unsupported front matter syntax in {path}: {line}")
        key, value = match.groups()
        if key in values:
            raise ValidationError(f"duplicate front matter key in {path}: {key}")
        if value.startswith('"') or value.startswith("["):
            try:
                parsed = json.loads(value)
            except json.JSONDecodeError as exc:
                raise ValidationError(f"invalid front matter value in {path}: {key}") from exc
            if type(parsed) not in {str, list} or (
                type(parsed) is list and not all(type(item) is str for item in parsed)
            ):
                raise ValidationError(f"invalid front matter value in {path}: {key}")
            values[key] = parsed
        elif value in {"true", "false"}:
            values[key] = value == "true"
        elif value.isdigit():
            values[key] = int(value)
        else:
            raise ValidationError(f"front matter values must be quoted, lists, booleans, or integers in {path}: {key}")
    return values, body


def _require(meta: dict[str, object], keys: tuple[str, ...], path: PurePosixPath) -> None:
    missing = [key for key in keys if not meta.get(key)]
    if missing:
        raise ValidationError(f"missing front matter in {path}: {', '.join(missing)}")


def _allow_only(meta: dict[str, object], allowed: set[str], path: PurePosixPath) -> None:
    unexpected = sorted(set(meta) - allowed)
    if unexpected:
        raise ValidationError(f"unsupported front matter key in {path}: {', '.join(unexpected)}")


def _validate_front_matter_schema(meta: dict[str, object], path: PurePosixPath) -> None:
    for key, value in meta.items():
        valid = True
        if key in STRING_FIELDS:
            valid = type(value) is str and bool(value.strip())
        elif key == "featured":
            valid = type(value) is bool
        elif key == "weight":
            valid = type(value) is int
        elif key == "source_keys":
            valid = type(value) is list and all(
                type(item) is str and bool(item.strip()) for item in value
            )
        if not valid:
            raise ValidationError(f"invalid front matter schema in {path}: {key}")



def _valid_source_date(value: object) -> bool:
    if type(value) is not str or not value.strip():
        return False
    match = SOURCE_DATE_PREFIX_RE.match(value)
    if match is None:
        return True
    year, month, day = match.groups()
    remainder = value[match.end():]
    if remainder.startswith("-"):
        return False
    try:
        if month is None:
            date(int(year), 1, 1)
        elif day is None:
            date(int(year), int(month), 1)
        else:
            date(int(year), int(month), int(day))
    except ValueError:
        return False
    return not remainder or not remainder[0].isalnum()


def _assert_casefold_unique(values: list[str], *, label: str = "path") -> None:
    folded: dict[str, str] = {}
    for value in values:
        key = value.casefold()
        previous = folded.get(key)
        if previous is not None and previous != value:
            raise ValidationError(f"case-folded {label} collision: {previous} vs {value}")
        folded[key] = value


def _exact_relref(body: str, source_key: str) -> bool:
    target = re.escape(f'/wiki/sources/{source_key}.md')
    pattern = re.compile(r'\[[^\]\n]+\]\(\s*\{\{<\s+relref\s+"' + target + r'"\s+>\}\}\s*\)')
    return pattern.search(visible_markdown(body)) is not None


def _image_targets(body: str, page: PurePosixPath) -> set[str]:
    try:
        return markdown_image_targets(body)
    except ValueError as exc:
        raise ValidationError(f"{exc} in {page}") from exc
def validate_publish(
    repository: Path | str = ".", *, baseline: str | None = None,
    inventory: dict[PurePosixPath, bytes] | None = None,
) -> ValidationReport:
    root = Path(repository).resolve()
    wiki = root / "wiki"
    try:
        inventory = secure_inventory(wiki) if inventory is None else inventory
    except ValueError as exc:
        raise ValidationError(str(exc)) from exc
    relative_paths = [path.as_posix() for path in inventory]
    _assert_casefold_unique(relative_paths)
    payloads: dict[PurePosixPath, bytes] = {}
    for relative, data in inventory.items():
        try:
            payloads[relative] = validate_canonical_file(wiki, wiki / relative, data=data)
        except (OSError, UnicodeError, ValueError) as exc:
            raise ValidationError(str(exc)) from exc

    markdown = sorted(path for path in inventory if path.suffix == ".md")
    source_meta: dict[str, tuple[PurePosixPath, dict[str, object], str]] = {}
    derived: list[tuple[PurePosixPath, dict[str, object], str]] = []
    page_bodies: dict[PurePosixPath, str] = {}
    routes: list[str] = []
    canonical_pages: list[str] = []

    for relative in markdown:
        meta, body = _front_matter(relative, payloads[relative])
        page_bodies[relative] = body
        if relative.name == "_index.md":
            if relative not in ALLOWED_INDEXES:
                raise ValidationError(f"_index.md is only allowed at exact section roots: {relative}")
            _allow_only(meta, INDEX_KEYS, relative)
            _validate_front_matter_schema(meta, relative)
            _require(meta, ("title",), relative)
            route = "wiki/" if len(relative.parts) == 1 else f"wiki/{relative.parts[0]}/"
            routes.append(route)
            canonical_pages.append(f"wiki/{relative.as_posix()}")
            continue

        parts = relative.parts
        _require(meta, ("title", "description", "type", "updated"), relative)
        updated = meta["updated"]
        try:
            valid_updated = (
                isinstance(updated, str)
                and DATE_RE.fullmatch(updated) is not None
                and date.fromisoformat(updated).isoformat() == updated
            )
        except ValueError:
            valid_updated = False
        if not valid_updated:
            raise ValidationError(f"invalid updated date in {relative}")

        if len(parts) == 3 and parts[0] == "sources" and parts[2] == "index.md":
            key = parts[1]
            if not KEY_RE.fullmatch(key):
                raise ValidationError(f"invalid source bundle key: {key}")
            _allow_only(meta, SOURCE_KEYS, relative)
            _validate_front_matter_schema(meta, relative)
            _require(meta, ("source_key",), relative)
            if meta["type"] != "source" or meta["source_key"] != key:
                raise ValidationError(f"source_key/type does not match bundle: {relative}")
            if "source_date" in meta:
                source_date = meta["source_date"]
                if not _valid_source_date(source_date):
                    raise ValidationError(f"invalid source_date in {relative}")
            if "source_url" in meta:
                parsed = urlsplit(str(meta["source_url"]))
                if parsed.scheme not in {"http", "https"} or not parsed.netloc or parsed.username or parsed.password:
                    raise ValidationError(f"invalid source_url in {relative}")
            if key in source_meta:
                raise ValidationError(f"duplicate source_key: {key}")
            source_meta[key] = (relative, meta, body)
            routes.append(f"wiki/sources/{key}/")
        elif len(parts) == 2 and parts[0] in {"concepts", "entities"}:
            slug = relative.stem
            if not KEY_RE.fullmatch(slug) or relative.name != f"{slug}.md":
                raise ValidationError(f"invalid lowercase ASCII canonical filename: {relative}")
            expected_type = {"concepts": "concept", "entities": "entity"}[parts[0]]
            _allow_only(meta, CONCEPT_KEYS if expected_type == "concept" else ENTITY_KEYS, relative)
            _validate_front_matter_schema(meta, relative)
            if meta["type"] != expected_type:
                raise ValidationError(f"type does not match section: {relative}")
            _require(meta, ("source_keys",), relative)
            if expected_type == "entity":
                _require(meta, ("entity_kind",), relative)
            derived.append((relative, meta, body))
            routes.append(f"wiki/{parts[0]}/{slug}/")
        else:
            raise ValidationError(f"Markdown outside Hugo wiki schema: {relative}")
        canonical_pages.append(f"wiki/{relative.as_posix()}")

    _assert_casefold_unique(routes, label="route")

    source_pages = {page for page, _meta, _body in source_meta.values()}
    for page, body in page_bodies.items():
        if page not in source_pages and _image_targets(body, page):
            raise ValidationError(
                f"image references must be local validated assets in {page}"
            )

    source_image_targets: dict[str, set[str]] = {}
    for key, (page, _meta, body) in source_meta.items():
        targets = _image_targets(body, page)
        source_image_targets[key] = targets
        for target in targets:
            relative_target = PurePosixPath(target)
            asset_path = PurePosixPath("sources") / key / target
            if (
                not target
                or relative_target.name != target
                or target in {".", ".."}
                or asset_path not in inventory
                or asset_path.suffix.casefold() not in {".png", ".gif", ".jpg", ".jpeg", ".webp"}
            ):
                raise ValidationError(
                    f"image references must be local validated assets in {page}: {target}"
                )


    assets: list[str] = []
    for relative in sorted(path for path in inventory if path.suffix != ".md"):
        parts = relative.parts
        if len(parts) != 3 or parts[0] != "sources" or parts[1] not in source_meta:
            raise ValidationError(f"asset outside a registered source bundle: {relative}")
        targets = source_image_targets[parts[1]]
        if parts[2] not in targets:
            raise ValidationError(f"bundle image asset is not referenced by a real visible Markdown image: {relative}")
        assets.append(f"wiki/{relative.as_posix()}")

    known = set(source_meta)
    for path, meta, body in derived:
        keys = meta["source_keys"]
        if not isinstance(keys, list) or not keys or len(keys) != len(set(keys)) or not all(isinstance(key, str) for key in keys):
            raise ValidationError(f"source_keys must be a non-empty unique list: {path}")
        for key in keys:
            if key not in known:
                raise ValidationError(f"unknown source_key {key!r} in {path}")
            if not _exact_relref(body, key):
                raise ValidationError(f"missing exact visible Hugo relref for {key!r} in {path}")

    report = ValidationReport(
        pages=len(canonical_pages) - len(ALLOWED_INDEXES),
        source_keys=tuple(sorted(known)), routes=tuple(sorted(routes)), assets=tuple(sorted(assets)),
        canonical_pages=tuple(sorted(canonical_pages)),
    )
    if baseline is not None:
        _validate_baseline(root, baseline, report)
    return report


def _validate_baseline(root: Path, commit: str, report: ValidationReport) -> None:
    try:
        result = subprocess.run(
            ["git", "ls-tree", "-r", "--name-only", commit, "--", "wiki"], cwd=root,
            check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True,
        )
    except subprocess.CalledProcessError as exc:
        raise ValidationError(f"cannot inspect baseline commit {commit!r}: {exc.stderr.strip()}") from exc
    baseline_pages = {
        line for line in result.stdout.splitlines()
        if line == "wiki/_index.md" or line in {"wiki/sources/_index.md", "wiki/concepts/_index.md", "wiki/entities/_index.md"}
        or re.fullmatch(r"wiki/sources/[a-z0-9]+(?:-[a-z0-9]+)*/index\.md", line)
        or re.fullmatch(r"wiki/(?:concepts|entities)/[a-z0-9]+(?:-[a-z0-9]+)*\.md", line)
    }
    missing = sorted(baseline_pages - set(report.canonical_pages))
    if missing:
        raise ValidationError("canonical conservation violation; baseline pages deleted or routes changed: " + ", ".join(missing))


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate the adversarial canonical wiki publication contract.")
    parser.add_argument("--baseline", metavar="GIT_COMMIT", help="reject deletion/route changes of canonical pages present in this commit")
    args = parser.parse_args(argv)
    try:
        report = validate_publish(Path.cwd(), baseline=args.baseline)
    except ValidationError as exc:
        print(f"Publish validation failed: {exc}", file=sys.stderr)
        return 1
    print(f"Validated {report.pages} canonical pages, {len(report.routes)} routes, and {len(report.assets)} assets across {len(report.source_keys)} dynamically discovered sources.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

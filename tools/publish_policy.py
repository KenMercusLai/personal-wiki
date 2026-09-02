from __future__ import annotations

import html
import os
from pathlib import Path, PurePosixPath
import re
import shutil
import stat
import struct
import subprocess
import zlib
from urllib.parse import unquote

FORBIDDEN_DIRECTORIES = {"archive", "inbox", "metadata", "private", "raw"}
FORBIDDEN_NAMES = {"asset-manifest.json", "source.original.md", "source-registry.json"}
PUBLIC_SUFFIXES = {".gif", ".jpeg", ".jpg", ".md", ".png", ".webp"}
PRIVATE_PATHS = (
    re.compile(r"(?i)(?:file:/+)?/Users/[^/\s<>\"']+/"),
    re.compile(r"(?i)(?:file:/+)?/home/[^/\s<>\"']+/"),
    re.compile(r"(?i)(?:file:/+)?[a-z]:[\\/]+Users[\\/]+"),
    re.compile(r"(?i)(?:^|[\s=\"'(:])~/"),
)
IMAGE_RE = re.compile(r"!\[[^\]\n]*\]\(\s*<?([^\s)>]+)>?(?:\s+(?:\"[^\"]*\"|'[^']*'|\([^)]*\)))?\s*\)")
RAW_IMAGE_MARKUP_RE = re.compile(
    r"<\s*(?:img|picture|source|object|embed|svg|image)\b"
    r"|<\s*input\b(?=[^>]*\btype\s*=\s*(?:[\"']\s*)?image(?:\s*[\"'])?(?:\s|/?>))",
    flags=re.IGNORECASE,
)
IMAGE_SHORTCODE_RE = re.compile(
    r"\{\{[<%]\s*/?\s*(?:figure|img|image|picture|source)\b",
    flags=re.IGNORECASE,
)


def _decoded(text: str) -> str:
    for _ in range(16):
        value = unquote(html.unescape(text))
        if value == text:
            return text
        text = value
    raise ValueError("forbidden canonical artifact: excessive nested encoding")


def _read_regular_at(parent_fd: int, name: str, relative: PurePosixPath) -> bytes:
    flags = os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK | getattr(os, "O_CLOEXEC", 0)
    try:
        fd = os.open(name, flags, dir_fd=parent_fd)
    except OSError as exc:
        raise ValueError(f"cannot securely open canonical artifact: {relative}") from exc
    try:
        info = os.fstat(fd)
        if not stat.S_ISREG(info.st_mode):
            raise ValueError(f"canonical artifact is not a regular file: {relative}")
        chunks: list[bytes] = []
        while chunk := os.read(fd, 1024 * 1024):
            chunks.append(chunk)
        return b"".join(chunks)
    finally:
        os.close(fd)


def secure_inventory(root: Path) -> dict[PurePosixPath, bytes]:
    """Inventory and read a tree only through anchored, no-follow directory FDs."""
    if not hasattr(os, "O_NOFOLLOW") or not hasattr(os, "O_DIRECTORY"):
        raise ValueError("secure canonical reads require O_NOFOLLOW and O_DIRECTORY")
    flags = os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW | getattr(os, "O_CLOEXEC", 0)
    try:
        root_fd = os.open(root, flags)
    except OSError as exc:
        raise ValueError(f"canonical wiki is not a regular directory: {root}") from exc
    inventory: dict[PurePosixPath, bytes] = {}

    def visit(directory_fd: int, prefix: PurePosixPath) -> None:
        for name in sorted(os.listdir(directory_fd)):
            if name in {".", ".."} or "/" in name or "\x00" in name:
                raise ValueError(f"invalid canonical entry name: {name!r}")
            relative = prefix / name
            info = os.stat(name, dir_fd=directory_fd, follow_symlinks=False)
            if stat.S_ISLNK(info.st_mode):
                raise ValueError(f"symlink is forbidden: {relative}")
            if stat.S_ISDIR(info.st_mode):
                try:
                    child_fd = os.open(name, flags, dir_fd=directory_fd)
                except OSError as exc:
                    raise ValueError(f"cannot securely open canonical directory: {relative}") from exc
                try:
                    if not stat.S_ISDIR(os.fstat(child_fd).st_mode):
                        raise ValueError(f"canonical entry is not a directory: {relative}")
                    visit(child_fd, relative)
                finally:
                    os.close(child_fd)
            elif stat.S_ISREG(info.st_mode):
                inventory[relative] = _read_regular_at(directory_fd, name, relative)
            else:
                raise ValueError(f"special node is forbidden: {relative}")

    try:
        visit(root_fd, PurePosixPath())
    finally:
        os.close(root_fd)
    return inventory


def secure_read_canonical(root: Path, path: Path) -> bytes:
    relative = PurePosixPath(path.relative_to(root).as_posix())
    inventory = secure_inventory(root)
    try:
        return inventory[relative]
    except KeyError as exc:
        raise ValueError(f"canonical artifact not found: {relative}") from exc


def visible_markdown(text: str) -> str:
    """Return a same-length view with comments and code masked."""
    chars = list(text)
    spans: list[tuple[int, int]] = []
    spans.extend((m.start(), m.end()) for m in re.finditer(r"<!--[\s\S]*?-->", text))
    spans.extend((m.start(), m.end()) for m in re.finditer(r"(?m)^(?: {0,3})(`{3,}|~{3,})[^\n]*\n[\s\S]*?^ {0,3}\1\s*$", text))
    spans.extend((m.start(), m.end()) for m in re.finditer(r"(?<!`)`[^`\n]+`(?!`)", text))
    spans.extend((m.start(), m.end()) for m in re.finditer(r"(?m)^(?: {4}|\t).*$", text))
    for start, end in spans:
        for index in range(start, end):
            if chars[index] not in "\r\n":
                chars[index] = " "
    return "".join(chars)


def markdown_image_targets(body: str) -> set[str]:
    # Hugo expands shortcodes before Markdown code spans/blocks are rendered.
    if IMAGE_SHORTCODE_RE.search(body):
        raise ValueError("raw image markup is forbidden")
    visible = visible_markdown(body)
    if RAW_IMAGE_MARKUP_RE.search(visible):
        raise ValueError("raw image markup is forbidden")
    matches = list(IMAGE_RE.finditer(visible))
    inline_starts = {match.start() for match in matches}
    if any(match.start() not in inline_starts for match in re.finditer(r"!\[", visible)):
        raise ValueError("unsupported Markdown image syntax")
    return {unquote(match.group(1)) for match in matches}


def _jpeg_dimensions(data: bytes) -> tuple[int, int] | None:
    if not data.startswith(b"\xff\xd8"):
        return None
    pos = 2
    while pos + 4 <= len(data):
        if data[pos] != 0xFF:
            pos += 1
            continue
        marker = data[pos + 1]
        pos += 2
        if marker in {0xD8, 0xD9} or 0xD0 <= marker <= 0xD7:
            continue
        if pos + 2 > len(data):
            return None
        length = int.from_bytes(data[pos:pos + 2], "big")
        if length < 2 or pos + length > len(data):
            return None
        if marker in {0xC0, 0xC1, 0xC2, 0xC3, 0xC5, 0xC6, 0xC7, 0xC9, 0xCA, 0xCB, 0xCD, 0xCE, 0xCF}:
            if length < 7:
                return None
            return int.from_bytes(data[pos + 5:pos + 7], "big"), int.from_bytes(data[pos + 3:pos + 5], "big")
        pos += length
    return None


def _jpeg_decodable(data: bytes) -> bool:
    """Decode one frame with a trusted system codec, failing closed if unavailable."""
    djpeg = shutil.which("djpeg")
    ffmpeg = shutil.which("ffmpeg")
    if djpeg:
        command = [djpeg, "-fast", "-onepass", "-outfile", os.devnull]
    elif ffmpeg:
        command = [
            ffmpeg, "-v", "error", "-f", "image2pipe", "-c:v", "mjpeg",
            "-i", "pipe:0", "-frames:v", "1", "-f", "null", "-",
        ]
    else:
        return False
    try:
        result = subprocess.run(
            command, input=data, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE,
            timeout=10, check=False,
        )
    except (OSError, subprocess.TimeoutExpired):
        return False
    return result.returncode == 0


def image_format_and_dimensions(data: bytes) -> tuple[str, int, int] | None:
    if data.startswith(b"\x89PNG\r\n\x1a\n") and len(data) >= 24 and data[12:16] == b"IHDR":
        width, height = struct.unpack(">II", data[16:24])
        return "png", width, height
    if data[:6] in {b"GIF87a", b"GIF89a"} and len(data) >= 10:
        width, height = struct.unpack("<HH", data[6:10])
        return "gif", width, height
    jpeg = _jpeg_dimensions(data)
    if jpeg:
        return "jpeg", *jpeg
    if data.startswith(b"RIFF") and data[8:12] == b"WEBP" and len(data) >= 30:
        kind = data[12:16]
        if kind == b"VP8X":
            width = 1 + int.from_bytes(data[24:27], "little")
            height = 1 + int.from_bytes(data[27:30], "little")
            return "webp", width, height
        if kind == b"VP8L" and data[20] == 0x2F:
            bits = int.from_bytes(data[21:25], "little")
            return "webp", (bits & 0x3FFF) + 1, ((bits >> 14) & 0x3FFF) + 1
        if kind == b"VP8 " and data[23:26] == b"\x9d\x01\x2a":
            return "webp", int.from_bytes(data[26:28], "little") & 0x3FFF, int.from_bytes(data[28:30], "little") & 0x3FFF
    return None


def validate_image(relative: PurePosixPath, data: bytes) -> None:
    parsed = image_format_and_dimensions(data)
    expected = {".png": "png", ".gif": "gif", ".jpg": "jpeg", ".jpeg": "jpeg", ".webp": "webp"}[relative.suffix.casefold()]
    if parsed is None or parsed[0] != expected:
        raise ValueError(f"image format does not match extension: {relative}")
    valid_encoding = False
    if expected == "png":
        position = 8
        chunks: list[tuple[bytes, bytes]] = []
        try:
            while position + 12 <= len(data):
                length = int.from_bytes(data[position:position + 4], "big")
                kind = data[position + 4:position + 8]
                end = position + 12 + length
                if end > len(data):
                    break
                payload = data[position + 8:position + 8 + length]
                checksum = int.from_bytes(data[position + 8 + length:end], "big")
                if zlib.crc32(kind + payload) & 0xFFFFFFFF != checksum:
                    break
                chunks.append((kind, payload))
                position = end
                if kind == b"IEND":
                    break
            idat = b"".join(payload for kind, payload in chunks if kind == b"IDAT")
            valid_encoding = (
                position == len(data)
                and len(chunks) >= 3
                and chunks[0][0] == b"IHDR"
                and chunks[-1][0] == b"IEND"
                and bool(zlib.decompress(idat))
            )
        except (ValueError, zlib.error):
            valid_encoding = False
    elif expected == "jpeg":
        valid_encoding = data.endswith(b"\xff\xd9") and parsed is not None and _jpeg_decodable(data)
    elif expected == "gif":
        valid_encoding = data.endswith(b"\x3b") and b"\x2c" in data[10:]
    elif expected == "webp":
        valid_encoding = len(data) >= 20 and int.from_bytes(data[4:8], "little") + 8 == len(data)
    if not valid_encoding:
        raise ValueError(f"invalid image encoding: {relative}")
    _, width, height = parsed
    if not (1 <= width <= 20000 and 1 <= height <= 20000) or len(data) > 50 * 1024 * 1024:
        raise ValueError(f"unreasonable image shape: {relative}")


def validate_canonical_file(root: Path, path: Path, *, data: bytes | None = None) -> bytes:
    relative = PurePosixPath(path.relative_to(root).as_posix())
    folded_parts = {part.casefold() for part in relative.parts}
    name = relative.name.casefold()
    if folded_parts & FORBIDDEN_DIRECTORIES:
        raise ValueError(f"forbidden canonical artifact: {relative}")
    if name in FORBIDDEN_NAMES or "_md5" in name or relative.suffix.casefold() not in PUBLIC_SUFFIXES:
        raise ValueError(f"forbidden canonical artifact: {relative}")
    if data is None:
        data = secure_read_canonical(root, path)
    if relative.suffix.casefold() != ".md":
        validate_image(relative, data)
        return data
    try:
        text = _decoded(data.decode("utf-8"))
    except UnicodeDecodeError as exc:
        raise ValueError(f"canonical Markdown is not UTF-8: {relative}") from exc
    if "![[" in text:
        raise ValueError(f"forbidden canonical artifact: raw Obsidian embed in {relative}")
    if any(pattern.search(text) for pattern in PRIVATE_PATHS):
        raise ValueError(f"private path in canonical Markdown: {relative}")
    if "com~apple~clouddocs" in text.casefold() or "mobile documents/" in text.casefold():
        raise ValueError(f"private path in canonical Markdown: {relative}")
    return data

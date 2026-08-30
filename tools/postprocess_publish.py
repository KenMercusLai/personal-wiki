from __future__ import annotations

import os
from pathlib import Path, PurePosixPath
import secrets
import stat
import sys

from .publish_policy import secure_inventory


class ProjectionError(ValueError):
    """Canonical wiki cannot be projected safely."""


def _directory_flags() -> int:
    return os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW | getattr(os, "O_CLOEXEC", 0)


def _open_or_create_directory(parent_fd: int, name: str, display: PurePosixPath) -> int:
    try:
        info = os.stat(name, dir_fd=parent_fd, follow_symlinks=False)
    except FileNotFoundError:
        os.mkdir(name, mode=0o755, dir_fd=parent_fd)
        info = os.stat(name, dir_fd=parent_fd, follow_symlinks=False)
    if stat.S_ISLNK(info.st_mode):
        raise ProjectionError(f"generated path component is a symlink: {display}")
    if not stat.S_ISDIR(info.st_mode):
        raise ProjectionError(f"generated path component is not a directory: {display}")
    try:
        fd = os.open(name, _directory_flags(), dir_fd=parent_fd)
    except OSError as exc:
        raise ProjectionError(f"cannot securely open generated directory: {display}") from exc
    if not stat.S_ISDIR(os.fstat(fd).st_mode):
        os.close(fd)
        raise ProjectionError(f"generated path component is not a directory: {display}")
    return fd


def _remove_tree_at(parent_fd: int, name: str, display: PurePosixPath) -> None:
    info = os.stat(name, dir_fd=parent_fd, follow_symlinks=False)
    if stat.S_ISLNK(info.st_mode):
        raise ProjectionError(f"generated destination is a symlink: {display}")
    if not stat.S_ISDIR(info.st_mode):
        raise ProjectionError(f"generated destination is not a directory: {display}")
    child_fd = os.open(name, _directory_flags(), dir_fd=parent_fd)
    try:
        for child in os.listdir(child_fd):
            child_info = os.stat(child, dir_fd=child_fd, follow_symlinks=False)
            child_display = display / child
            if stat.S_ISLNK(child_info.st_mode):
                raise ProjectionError(f"symlink in generated destination: {child_display}")
            if stat.S_ISDIR(child_info.st_mode):
                _remove_tree_at(child_fd, child, child_display)
            elif stat.S_ISREG(child_info.st_mode):
                os.unlink(child, dir_fd=child_fd)
            else:
                raise ProjectionError(f"special node in generated destination: {child_display}")
    finally:
        os.close(child_fd)
    os.rmdir(name, dir_fd=parent_fd)


def _write_inventory(directory_fd: int, payloads: dict[PurePosixPath, bytes]) -> None:
    directory_fds: dict[PurePosixPath, int] = {PurePosixPath(): os.dup(directory_fd)}
    try:
        for relative, data in sorted(payloads.items(), key=lambda item: item[0].as_posix()):
            parent = PurePosixPath()
            for part in relative.parts[:-1]:
                next_parent = parent / part
                if next_parent not in directory_fds:
                    directory_fds[next_parent] = _open_or_create_directory(directory_fds[parent], part, next_parent)
                parent = next_parent
            flags = os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW | getattr(os, "O_CLOEXEC", 0)
            fd = os.open(relative.name, flags, 0o644, dir_fd=directory_fds[parent])
            try:
                view = memoryview(data)
                while view:
                    written = os.write(fd, view)
                    if written <= 0:
                        raise ProjectionError(f"short write projecting {relative}")
                    view = view[written:]
            finally:
                os.close(fd)
    finally:
        for fd in directory_fds.values():
            os.close(fd)


def _verify_open_chain(repository_fd: int, parts: tuple[str, ...], opened: list[int]) -> None:
    """Require repository path names to still identify the anchored directory FDs."""
    current_fd = os.dup(repository_fd)
    try:
        for part, expected_fd in zip(parts, opened):
            info = os.stat(part, dir_fd=current_fd, follow_symlinks=False)
            expected = os.fstat(expected_fd)
            if not stat.S_ISDIR(info.st_mode) or (info.st_dev, info.st_ino) != (expected.st_dev, expected.st_ino):
                raise ProjectionError(f"generated ancestor changed during projection: {part}")
            next_fd = os.open(part, _directory_flags(), dir_fd=current_fd)
            os.close(current_fd)
            current_fd = next_fd
    except (FileNotFoundError, OSError) as exc:
        raise ProjectionError("generated ancestor changed during projection") from exc
    finally:
        os.close(current_fd)


def project_wiki(source: Path, destination: Path) -> None:
    """Atomically replace destination from one immutable no-follow source inventory."""
    source = source.absolute()
    destination = destination.absolute()
    repository = source.parent
    try:
        relative_destination = PurePosixPath(destination.relative_to(repository).as_posix())
    except ValueError as exc:
        raise ProjectionError("generated destination must stay inside the repository") from exc
    if source == destination or source in destination.parents or destination in source.parents:
        raise ProjectionError("canonical and generated trees must be disjoint")
    if not relative_destination.parts:
        raise ProjectionError("generated destination must not be the repository root")

    try:
        inventory = secure_inventory(source)
        from .validate_publish import ValidationError, validate_publish
        try:
            validate_publish(repository, inventory=inventory)
        except ValidationError as exc:
            raise ProjectionError(str(exc)) from exc
        payloads = dict(inventory)
    except ValueError as exc:
        raise ProjectionError(str(exc)) from exc

    try:
        repository_fd = os.open(repository, _directory_flags())
    except OSError as exc:
        raise ProjectionError(f"repository is not a secure directory: {repository}") from exc
    parent_fd = repository_fd
    opened: list[int] = []
    temporary_name = f".{relative_destination.name}-{secrets.token_hex(12)}"
    temporary_created = False
    try:
        display = PurePosixPath()
        for part in relative_destination.parts[:-1]:
            display /= part
            child_fd = _open_or_create_directory(parent_fd, part, display)
            opened.append(child_fd)
            parent_fd = child_fd
        final_name = relative_destination.name
        try:
            final_info = os.stat(final_name, dir_fd=parent_fd, follow_symlinks=False)
        except FileNotFoundError:
            final_info = None
        if final_info is not None and stat.S_ISLNK(final_info.st_mode):
            raise ProjectionError(f"generated destination is a symlink: {relative_destination}")

        os.mkdir(temporary_name, mode=0o755, dir_fd=parent_fd)
        temporary_created = True
        temporary_fd = os.open(temporary_name, _directory_flags(), dir_fd=parent_fd)
        try:
            _write_inventory(temporary_fd, payloads)
        finally:
            os.close(temporary_fd)

        _verify_open_chain(repository_fd, relative_destination.parts[:-1], opened)

        if final_info is not None:
            _remove_tree_at(parent_fd, final_name, relative_destination)
        os.rename(temporary_name, final_name, src_dir_fd=parent_fd, dst_dir_fd=parent_fd)
        temporary_created = False
        _verify_open_chain(repository_fd, relative_destination.parts[:-1], opened)
    except ProjectionError:
        raise
    except OSError as exc:
        raise ProjectionError(f"secure generated destination operation failed: {exc}") from exc
    finally:
        if temporary_created:
            try:
                _remove_tree_at(parent_fd, temporary_name, PurePosixPath(temporary_name))
            except (OSError, ProjectionError):
                pass
        for fd in reversed(opened):
            os.close(fd)
        os.close(repository_fd)


def main() -> int:
    root = Path.cwd()
    try:
        project_wiki(root / "wiki", root / ".generated" / "wiki")
    except ProjectionError as exc:
        print(f"Publication projection failed: {exc}", file=sys.stderr)
        return 1
    print("Projected canonical wiki into ignored .generated/wiki without source mutation.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

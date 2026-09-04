# Personal Wiki

A deterministic Hugo consumer for Ken's canonical Personal LLM Wiki.

## Architecture

```text
parent-selected text
-> separate personal-wiki-agent producer (LLM Wiki ingest/lint/synthesis/validation)
-> exact Git-blob mirror: wiki/ + wiki-assets/
-> deterministic ignored .generated projections
-> pinned Hugo build
-> independent final HTML verifier
```

This repository never runs a model and never performs semantic synthesis. Its checked-in `wiki/` and `wiki-assets/` are exact producer mirrors. Canonical `index.md`, `log.md`, `overview.md`, and synthesis internals are retained for the producer contract but are not mounted as direct public pages.

## Local verification

```bash
python3 -m unittest discover -s tests -v
python3 -m compileall -q scripts tests
python3 scripts/prepare-overview-projections.py
python3 scripts/prepare-wiki-content.py
python3 scripts/prepare-overview-projections.py --check
python3 scripts/prepare-wiki-content.py --check
./build.sh
PUBLIC_DIR=public-root ./build.sh --baseURL https://example.test/
git diff --check
```

`build.sh` downloads and checksum-verifies Hugo 0.163.3, cleans the destination, and runs the artifact verifier. Override `PUBLIC_DIR` to keep root and project-subpath artifacts side by side.

# Personal Wiki consumer contract

This repository is the public Hugo consumer for the canonical Personal LLM Wiki producer. It must never run a coding agent or perform semantic synthesis.

## Repository boundary

The publication orchestrator owns the two-repository transaction:

1. Run the production LLM Wiki workflow in the separate producer.
2. Validate and publish the producer commit.
3. Mirror exactly the producer commit's `wiki/` and `wiki-assets/` Git blobs here.
4. Run deterministic preparation, Hugo, and the independent final artifact verifier.
5. Publish this consumer only after every gate succeeds.

The checked-in `wiki/` and `wiki-assets/` trees are producer-owned inputs. They are exact mirrors and must never be edited by consumer scripts. The consumer owns only ignored `.generated/` output, Hugo's ignored `public/` and `resources/`, templates, tests, and deterministic build tooling.

## Deterministic consumer workflow

Run only:

```text
scripts/prepare-overview-projections.py
scripts/prepare-wiki-content.py
scripts/prepare-overview-projections.py --check
scripts/prepare-wiki-content.py --check
pinned Hugo --cleanDestinationDir
scripts/verify_pages_output.py
```

Preparation validates identities, canonical wikilinks, source provenance, image sidecars, image bytes, route collisions, and output ownership before writing. `--check` compares exact expected bytes and stale inventory without writing. Repeated generation must be idempotent and preserve every byte under `wiki/` and `wiki-assets/`.

Canonical `wiki/index.md`, `wiki/log.md`, and `wiki/overview.md` are not public pages. The canonical compact synthesis and overview are visible only through the intended Current Synthesis, Open Questions, and Update History projections. Source notes remain renderer-independent flat Markdown; source bundles, local image references, public routes, and Hugo metadata are derived only in `.generated/`.

Do not add ingest, lint, model, prompt, semantic-refresh, commit, push, archive, or deployment entrypoints here. Do not commit `.generated/` or `public/`. Do not commit, push, or deploy as part of local reconstruction or verification.

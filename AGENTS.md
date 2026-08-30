# LLM Wiki ingest protocol

This repository is the canonical public Personal Wiki. ScriptBin's existing
`llm_wiki_ingest` runs with this repository as its current working directory.
The orchestrator, not the model, supplies immutable staged input and enforces
write ownership at the process boundary.

## Trust and ownership boundary

- Read the task's immutable staged input; never read the live inbox, archive,
  home-directory source paths, or unrelated files.
- Write ownership is restricted to canonical `wiki/**`. Do not modify tooling,
  tests, workflows, layouts, configuration, `.git`, or generated output.
- Never include raw/private paths, Obsidian embeds, source manifests, original
  documents, `_MD5` assets, private metadata, or unselected staged files.
- The ingest process must not commit, push, build, deploy, archive, or move the
  staged input. The unrestricted ScriptBin parent validates, audits the exact
  changed paths, commits and pushes canonical output, then archives locally.
- GitHub Actions alone performs publication-only Post Process, Hugo build,
  artifact validation, upload, and Pages deployment.

## Canonical Hugo schema

Create or update only these forms:

- Source page bundle: `wiki/sources/<slug>/index.md`
- Concept: `wiki/concepts/<slug>.md`
- Entity: `wiki/entities/<slug>.md`
- Public media: selected staged assets beside their source bundle's `index.md`

Slugs, canonical concept/entity filenames, and `source_key` values use lowercase
ASCII words separated by single hyphens. `_index.md` is reserved to exactly
`wiki/_index.md`, `wiki/sources/_index.md`, `wiki/concepts/_index.md`, and
`wiki/entities/_index.md`.

Front matter uses the exact per-type allowlists below; no other key is accepted:

- section index: `title`, optional `description`, optional `weight`;
- source: `title`, `description`, `type`, `updated`, `source_key`, `image_status`,
  and only the optional provenance/presentation keys `author`, `translator`,
  `source_date`, `source_url`, `featured`;
- concept: `title`, `description`, `type`, `updated`, `source_keys`, optional
  `featured`;
- entity: concept keys plus required `entity_kind`.

Quoted text fields must be non-empty strings, `updated` must be a real
`YYYY-MM-DD` calendar date, `featured` is boolean, `weight` is an integer, and
`source_keys` is a non-empty list of non-empty strings. Booleans, integers, or
lists cannot substitute for text fields.
When present, `source_date` preserves the source's non-empty display text. If it
starts with `YYYY`, `YYYY-MM`, or `YYYY-MM-DD`, that leading calendar value must
be real; a source-supplied annotation may follow it.

Route/output controls are forbidden, including `url`, `aliases`, `slug`,
`draft`, `outputs`, `layout`, `build`, and framework equivalents. A source has
`type: "source"`, `updated` (`YYYY-MM-DD`), a matching `source_key`, and
`image_status`. Do not require or fabricate `author`, `source_date`, or
`source_url` for private notes. Include optional provenance only when the staged
source actually supplies it; any supplied `source_url` must be absolute HTTP(S).
The deterministic repository validator authenticates provenance structure and
URL safety, not semantic truth extraction from arbitrary prose. ScriptBin binds
the resulting source bundle and pushed commit to the immutable staged source's
SHA-256 and byte length in its private receipt and Archive metadata; do not add
private source identity metadata to public canonical front matter.

Every concept/entity must preserve provenance for every `source_keys` entry with
an exact visible Hugo `relref` Markdown link of the form
`[label]({{< relref "/wiki/sources/<source_key>.md" >}})`. Plain text,
ordinary links, comments, and code do not count. Preserve useful existing
synthesis when adding evidence; do not silently delete another source's
contribution. Each selected staged asset must be a non-SVG image whose bytes
match its filename format and whose dimensions are reasonable. It must have a
real visible Markdown image reference using only its relative filename;
comments, code, ordinary links, and filename substrings do not select an asset.
Only inline local Markdown image syntax is accepted. Reference-style images,
absolute/protocol-relative/data URLs, remote resources, and raw image markup are
forbidden. JPEG selection additionally requires a working `djpeg` or `ffmpeg`
decoder so malformed marker-only files fail closed.

## Required handoff

Leave the worktree uncommitted. Report the canonical paths changed and whether
new sources, concepts, entities, or selected assets were created. The parent
must run from repository root:

```sh
python3 -m tools.validate_publish --baseline <observed-upstream-commit>
```

The ScriptBin parent must pass the immutable Git commit it inspected before
starting ingest. Baseline mode rejects deletion or route-changing rename of any
source, concept, entity, or allowed section page that existed in that commit.
The parent should still audit the complete Git diff and exact writable paths.
For a clean local publication check where conservation is not an ingest concern,
`python3 -m tools.validate_publish` validates the current corpus alone.

This validator intentionally scans the live filesystem, including untracked
new files, and discovers the source registry dynamically. A nonzero result is
a hard failure: do not commit or push.

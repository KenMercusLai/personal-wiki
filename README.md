# Personal Wiki

A Hugo-powered public projection of Ken's personal LLM Wiki.

## Architecture

```text
private source inbox (outside Git)
-> text-first ingest
-> canonical derived Markdown in wiki/
-> deterministic ignored publication projection in .generated/wiki/
-> Hugo build
-> GitHub Pages artifact deployment
```

The server-side ingest owns only `wiki/**`: it validates, commits, and pushes
canonical knowledge, then the local source lifecycle may Archive the input.
GitHub Actions independently runs `tools.validate_publish`, rebuilds
`.generated/wiki/` from scratch with `tools.postprocess_publish`, builds Hugo,
verifies the artifact, and deploys Pages. Generated projection files are never
committed, and an Actions failure does not requeue a successfully pushed source.

Raw articles, PDFs, screenshots, Web Archives, and missing image assets are not committed to this public repository.

## Local build

Publication validation requires `djpeg` or `ffmpeg` to decode selected JPEGs;
validation fails closed when neither trusted decoder is available.

```bash
./build.sh
python3 scripts/verify_pages_output.py public
```

The production workflow overrides Hugo's `baseURL` with the GitHub Pages project URL.

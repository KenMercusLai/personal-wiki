# Personal Wiki

A Hugo-powered public projection of Ken's personal LLM Wiki.

## Architecture

```text
private source inbox (outside Git)
-> text-first ingest
-> canonical derived Markdown in wiki/
-> Hugo build
-> GitHub Pages artifact deployment
```

Raw articles, PDFs, screenshots, Web Archives, and missing image assets are not committed to this public repository.

## Local build

```bash
./build.sh
python3 scripts/verify_pages_output.py public
```

The production workflow overrides Hugo's `baseURL` with the GitHub Pages project URL.

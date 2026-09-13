# Wiki Lint Report — 2026-09-13

Scanned 1016 pages.

## Structural Issues

No structural issues found.

## Graph-Aware Issues

### Hub Pages with Insufficient Content (0 pages)
No hub stubs detected — all high-degree nodes have sufficient content.

### Fragile Bridges (5 community pairs)
These community connections rely on a single edge — one broken link isolates them:
- Community 1 ↔ Community 7 via `concepts/ConversionRateOptimization` → `concepts/BehavioralData`
- Community 2 ↔ Community 5 via `concepts/BootstrappedSaaS` → `concepts/CloudCostOptimization`
- Community 8 ↔ Community 15 via `concepts/PlatformAbuseResponse` → `concepts/SemanticIsolation`
- Community 11 ↔ Community 12 via `sources/a-look-at-auth0-cloud-architecture-5-years-in` → `entities/Mozilla`
- Community 12 ↔ Community 13 via `concepts/MobileProductivity` → `concepts/PersonalProductivity`

### Isolated Communities (0 communities)
No isolated communities — all clusters have external connections.

---

## Semantic Checks Unavailable

Semantic lint did not complete because the LLM API call failed.

- Error: `BadRequestError: litellm.BadRequestError: LLM Provider NOT provided. Pass in the LLM provider you are trying to call. You passed model=claude-3-5-sonnet-latest Pass model as E.g. For 'Huggingface' inference endpoints pass in `completion(model='huggingface/starcoder',..)` Learn more: https://docs.litellm.ai/docs/providers`
- Deterministic and graph-aware checks above still completed.
- Configure `LLM_MODEL` with a provider-qualified LiteLLM model and required API key, then rerun `python tools/lint.py` for contradiction, stale-content, and data-gap analysis.
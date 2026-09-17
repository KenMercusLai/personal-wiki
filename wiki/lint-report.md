# Wiki Lint Report — 2026-09-17

Scanned 1817 pages.

## Structural Issues

No structural issues found.

## Graph-Aware Issues

### Hub Pages with Insufficient Content (0 pages)
No hub stubs detected — all high-degree nodes have sufficient content.

### Fragile Bridges (11 community pairs)
These community connections rely on a single edge — one broken link isolates them:
- Community 1 ↔ Community 7 via `concepts/BehavioralData` → `concepts/SemanticSearch`
- Community 1 ↔ Community 8 via `concepts/EconomicGraph` → `concepts/MOOCLearningAnalytics`
- Community 1 ↔ Community 13 via `concepts/ExitAsGovernance` → `concepts/PrivacyPovertyDivide`
- Community 3 ↔ Community 4 via `concepts/LivestreamCommerce` → `concepts/ConversionRateOptimization`
- Community 3 ↔ Community 18 via `concepts/DigitalGifting` → `concepts/Gamification`
- Community 6 ↔ Community 13 via `concepts/SecurityTokens` → `concepts/ComplianceArchitecture`
- Community 7 ↔ Community 17 via `concepts/IndieGameDevelopment` → `concepts/GameLocalization`
- Community 11 ↔ Community 12 via `concepts/DigitalProductTimelessness` → `concepts/BrandDistinctiveness`
- Community 11 ↔ Community 18 via `concepts/EntropyReductionManagement` → `concepts/OrganizationalDataSharing`
- Community 12 ↔ Community 13 via `concepts/CryptoWalletSecurity` → `concepts/ProductEvolution`
- Community 13 ↔ Community 18 via `sources/building-for-trust-airbnb-engineering-data-science-medium` → `concepts/SupportLoadScaling`

### Isolated Communities (0 communities)
No isolated communities — all clusters have external connections.

---

## Semantic Checks Unavailable

Semantic lint did not complete because the LLM API call failed.

- Error: `BadRequestError: litellm.BadRequestError: LLM Provider NOT provided. Pass in the LLM provider you are trying to call. You passed model=claude-3-5-sonnet-latest Pass model as E.g. For 'Huggingface' inference endpoints pass in `completion(model='huggingface/starcoder',..)` Learn more: https://docs.litellm.ai/docs/providers`
- Deterministic and graph-aware checks above still completed.
- Configure `LLM_MODEL` with a provider-qualified LiteLLM model and required API key, then rerun `python tools/lint.py` for contradiction, stale-content, and data-gap analysis.
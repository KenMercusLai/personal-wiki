# Wiki Lint Report — 2026-09-14

Scanned 1469 pages.

## Structural Issues

No structural issues found.

## Graph-Aware Issues

### Hub Pages with Insufficient Content (0 pages)
No hub stubs detected — all high-degree nodes have sufficient content.

### Fragile Bridges (11 community pairs)
These community connections rely on a single edge — one broken link isolates them:
- Community 0 ↔ Community 13 via `concepts/StructuredCLIOutput` → `concepts/DataGeneratingProcess`
- Community 0 ↔ Community 19 via `concepts/SelfHostedSurveillanceStorage` → `concepts/InternetOfThingsData`
- Community 1 ↔ Community 16 via `concepts/EntropyReductionManagement` → `concepts/OrganizationalDataSharing`
- Community 3 ↔ Community 7 via `concepts/CorporateSatire` → `concepts/CreatorFeedbackLoop`
- Community 5 ↔ Community 19 via `concepts/DatabaseServiceExposure` → `concepts/PrivateDataChatbot`
- Community 6 ↔ Community 8 via `concepts/AIInvestmentTheme` → `concepts/AIFirstEngineering`
- Community 8 ↔ Community 18 via `concepts/UTXOModel` → `concepts/DoubleEntryAccounting`
- Community 9 ↔ Community 18 via `concepts/BitcoinScript` → `concepts/SmartContracts`
- Community 12 ↔ Community 16 via `concepts/ProductLedRetention` → `concepts/DifferentiationStrategy`
- Community 13 ↔ Community 16 via `concepts/AppleAdvertisingPatterns` → `concepts/ProductEvolution`
- Community 13 ↔ Community 18 via `concepts/CryptoWalletSecurity` → `concepts/ProductEvolution`

### Isolated Communities (0 communities)
No isolated communities — all clusters have external connections.

---

## Semantic Checks Unavailable

Semantic lint did not complete because the LLM API call failed.

- Error: `BadRequestError: litellm.BadRequestError: LLM Provider NOT provided. Pass in the LLM provider you are trying to call. You passed model=claude-3-5-sonnet-latest Pass model as E.g. For 'Huggingface' inference endpoints pass in `completion(model='huggingface/starcoder',..)` Learn more: https://docs.litellm.ai/docs/providers`
- Deterministic and graph-aware checks above still completed.
- Configure `LLM_MODEL` with a provider-qualified LiteLLM model and required API key, then rerun `python tools/lint.py` for contradiction, stale-content, and data-gap analysis.
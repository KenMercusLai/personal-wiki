---
title: "Causal Encoder-Decoder Architecture"
type: concept
tags: [ai, transformer, prefill, long-context, inference]
sources:
  - ba-kv-cache-ya-suo-tui-dao-ji-zhi-zartbot
  - deepseek-v41-tech-report
last_updated: 2026-10-24
knowledge_schema: synthesis-v1
---

## Definition
[[CausalEncoderDecoderArchitecture]] is a Transformer organization in which a lower causal stack produces reusable global context representations and an upper decoder reads those representations with new queries, allowing most prompt positions to stop before traversing the full network.

## Current Synthesis
In [[DeepSeekV41Flash]], the first 20 of 40 backbone layers form a causal encoder. Its final hidden state supplies decoder global KV through layer-specific projections, so long prompt positions traverse the encoder but not the complete decoder. Generated tokens still execute all decoder layers, and every decoder layer retains its own local sliding-window state and query behavior.

That split moves cost rather than eliminating every decoder dependency. Historical prompt positions have no decoder-local SWA state because they exited early. Exact reconstruction would replay a depth-expanded history, so the system instead processes only the most recent 128 tokens under a truncated local-attention interval. Global sparse KV remains available throughout, but local state near the replay boundary is approximate. The architecture therefore combines a strong asymptotic prefill saving with an explicitly tested—not mathematically exact—recovery path.

## Key Claims
- Separating global-memory production from decoder consumption can approximately halve backbone work for prompts much longer than the replay window.
- The encoder is causal; its name describes a memory-producing role rather than bidirectional access.
- Decoder global KV is projected from the encoder boundary with layer-specific weights, while decoder queries and local SWA state remain layer-specific.
- Exact recovery of stacked sliding-window state can require a history proportional to depth times window size.
- Bounded replay caps recovery at one recent window and is especially valuable after short tool-call increments or persistent-cache hits.
- The saving is workload-dependent because short prompts, warm local state, projection, MoE, communication, and replay overhead remain.

## Evidence
Memory boundary and compute:
- [[deepseek-v41-tech-report]] gives the projection from the 20th-layer hidden state to each decoder layer's global KV and reduces long-sequence complexity from full 40-layer prompt execution toward 20 layers plus bounded replay.
- [[ba-kv-cache-ya-suo-tui-dao-ji-zhi-zartbot]] reconstructs the same midpoint early-exit path and distinguishes prompt-side from generated-token execution.

Local-state reconstruction:
- [[deepseek-v41-tech-report]] explains encoder and decoder SWA Bounded Replay, the 128-token replay interval, cached-global-KV reuse, and the deliberate difference from full decoder execution.
- [[ba-kv-cache-ya-suo-tui-dao-ji-zhi-zartbot]] explains why local dependencies expand across decoder depth and why the bounded suffix is an approximation.

Deployment consequence:
- [[deepseek-v41-tech-report]] uses bounded replay to remove SWA KV from long-lived persistent storage and to make local-cache misses a fixed-size recomputation rather than a full depth-expanded replay.

## Counterevidence & Qualifications
The near-half prefill claim is asymptotic and does not imply a universal latency or FLOP ratio. The report says bounded replay causes negligible quality loss in its tests and simulates the decoder path during post-training, but it provides no independent replication or exhaustive cache-resumption stress test. Because replayed local states differ by cache-hit position, untested boundaries can still degrade behavior; the authors identify this as future robustness work. The evidence is one primary vendor report plus a secondary technical reconstruction derived from it.

## What Changed
- Added the primary projection and complexity account behind causal prompt early exit.
- Connected bounded replay to persistent-cache removal and both encoder- and decoder-local state recovery.
- Reframed negligible observed degradation as tested approximation rather than exact equivalence.

## Related Concepts
- [[TransformerArchitecture]] - broader family whose depth is partitioned into causal context production and consumption.
- [[CompressedSparseAttention2]] - supplies shared global memory and layer-local sparse readout within the split architecture.
- [[KVCacheCompression]] - benefits from fewer independently retained global caches and a shorter-lived local state lifecycle.
- [[AttentionMechanism]] - provides layer-specific queries over encoder-derived global memory and local SWA state.
- [[PromptCaching]] - avoids some prefills entirely, while causal early exit and replay reduce work when a prefix must be resumed or extended.

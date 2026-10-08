---
title: "Causal Encoder-Decoder Architecture"
type: concept
tags: [ai, transformer, prefill, long-context, inference]
sources:
  - ba-kv-cache-ya-suo-tui-dao-ji-zhi-zartbot
last_updated: 2026-10-08
knowledge_schema: synthesis-v1
---

## Definition
[[CausalEncoderDecoderArchitecture]] is a Transformer organization in which a lower causal stack produces reusable global context representations and an upper decoder stack reads those representations with new queries, allowing most prompt positions to stop before traversing the full network.

## Current Synthesis
In the described DeepSeek design, the first 20 of 40 backbone layers form a causal encoder. Its boundary representation supplies the decoder's global KV through layer-specific projections, so bulk prompt positions need not execute the upper 20 layers. The decoder still builds fresh local sliding-window state at every layer and processes generated positions normally.

This creates a recovery problem after a cold or resumed prefill: decoder-local KV for historical positions does not exist because those positions exited early. Bounded replay recomputes only a recent suffix instead of recursively reconstructing the entire theoretical sliding-window receptive field. The approximation preserves access to long history through global sparse KV while accepting that the local state near the replay boundary differs from full execution.

## Key Claims
- Separating global-memory production from repeated consumption can approximately halve long-prompt backbone work.
- The architecture's encoder remains causal; the name describes its role as a reusable context producer, not bidirectional access.
- Decoder layers retain distinct queries and local SWA state even when they share global content from the encoder boundary.
- Exact reconstruction of deep local-window state can require a history much longer than one window because dependencies expand across layers.
- Bounded replay caps that recovery work at a fixed suffix length and is therefore most consequential in tool-heavy sessions with short new increments.
- Global sparse memory remains available during replay, so the approximation truncates local reconstruction rather than the whole historical context.

## Evidence
Early exit:
- [[ba-kv-cache-ya-suo-tui-dao-ji-zhi-zartbot]] contrasts full 40-layer prompt execution with 20-layer encoder execution plus a bounded decoder suffix.

Memory boundary:
- [[ba-kv-cache-ya-suo-tui-dao-ji-zhi-zartbot]] says decoder global KV is projected from the final causal-encoder representation while decoder queries remain layer-specific.

Replay tradeoff:
- [[ba-kv-cache-ya-suo-tui-dao-ji-zhi-zartbot]] explains why local dependencies expand across decoder depth and why replay is deliberately approximate.

## Counterevidence & Qualifications
The near-half compute claim applies when prompt length greatly exceeds the bounded replay suffix and should not be read as a universal latency or FLOP ratio. Short prompts, warm-cache behavior, projection work, MoE execution, communication, and implementation overhead change realized savings. The source reports prior evidence that SWA influence decays with distance but does not reproduce a task-level ablation of the chosen replay bound.

## What Changed
- Defined causal encoder-decoder as a prefill early-exit and shared-memory architecture.
- Added bounded replay as the explicit cost-versus-local-state approximation.

## Related Concepts
- [[TransformerArchitecture]] - broader family whose depth is partitioned into causal context production and consumption.
- [[CompressedSparseAttention2]] - implements the shared global-memory and fresh local-window readout.
- [[KVCacheCompression]] - benefits from the reduced number of independently retained global caches.
- [[AttentionMechanism]] - supplies layer-specific queries over shared encoder-derived memory.
- [[PromptCaching]] - application-level prefix reuse can avoid prefill, while this architecture reduces the cost when prefill remains necessary.

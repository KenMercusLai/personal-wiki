---
title: "KV-Cache Compression"
type: concept
tags: [ai, inference, kv-cache, long-context, compression]
sources:
  - ba-kv-cache-ya-suo-tui-dao-ji-zhi-zartbot
last_updated: 2026-10-08
knowledge_schema: synthesis-v1
---

## Definition
[[KVCacheCompression]] reduces the stored, transferred, or recomputed key-value state used by autoregressive attention while preserving enough content and addressing information for useful later-token readout.

## Current Synthesis
The source organizes compression into three multiplicative dimensions. Channel compression shares a smaller latent representation across attention heads; sequence compression merges neighboring positions into fewer entries; layer compression lets several layers consume one published content cache or one sparse selection rather than retaining their own copies. Precision reduction applies after those structural choices and can further shrink the surviving entries.

Compression is not only a memory-capacity optimization. Long agent sessions persist and move cache state across HBM, host memory, SSD, and interconnects, while cache misses trigger repeated prefill after tool calls. A useful design therefore coordinates storage layout, prefill execution, sparse address selection, cache sharing, quantization, and deployment locality rather than optimizing bytes in isolation.

## Key Claims
- Channel, sequence, layer, and numerical-precision reductions compound rather than substitute for one another.
- Cross-layer sharing can remove far more duplicate cache state than sequence compression alone, but it reduces which content and addresses later layers may change.
- Prefill early exit and KV compression solve related but distinct problems: one reduces computation over prompt positions, while the other reduces stored and transferred state.
- Main global KV can tolerate a different precision and lifecycle from fresh local sliding-window KV.
- Cache size should include indexer keys, scale metadata, local-state requirements, persistent copies, and transfer costs rather than only nominal K/V payloads.
- Deployment routing and model architecture are complementary: smaller caches lower movement cost, while locality-aware routing raises reuse probability.

## Evidence
Compression dimensions:
- [[ba-kv-cache-ya-suo-tui-dao-ji-zhi-zartbot]] attributes DeepSeek-V4.1-Flash's reduction to a 512-channel latent, 2:1 encoder position compression, four cross-layer cache sources, and FP4 storage.

Accounting and lifecycle:
- [[ba-kv-cache-ya-suo-tui-dao-ji-zhi-zartbot]] derives 288 bytes for one 512-channel FP4 main-KV entry and 890 bytes per token across the reported global cache sources.
- [[ba-kv-cache-ya-suo-tui-dao-ji-zhi-zartbot]] distinguishes HBM runtime state, persisted host/SSD state, and cache-transfer bandwidth as separate service constraints.

Compute interaction:
- [[ba-kv-cache-ya-suo-tui-dao-ji-zhi-zartbot]] uses causal early exit for bulk prompt positions and bounded replay for decoder-local SWA state rather than treating compression alone as a prefill solution.

## Counterevidence & Qualifications
Compression ratios are architecture- and accounting-dependent: changing sequence granularity, scale metadata, local windows, persistence policy, or precision changes the comparison. Shared content and addresses create recall and expressivity limits, and low-precision caches require training adaptation. The source reports quality retention but does not independently ablate each compression dimension or reproduce the serving-cost result.

## What Changed
- Established a four-part model spanning channel, sequence, layer, and precision compression.
- Separated cache-capacity reduction from prefill-compute reduction and cache-locality routing.

## Related Concepts
- [[CompressedSparseAttention2]] - concrete mechanism combining the first three compression dimensions.
- [[CausalEncoderDecoderArchitecture]] - reduces the computation needed to produce decoder-visible global cache.
- [[BlockQuantization]] - supplies local shared scales for low-precision cache entries.
- [[QuantizationAwareTraining]] - adapts attention to FP4 main-KV distortion.
- [[KVCacheAwareRouting]] - raises the chance that compressed prefix state is reused on the selected worker.
- [[LLMContextManagement]] - determines which long-context material should remain available to the model.

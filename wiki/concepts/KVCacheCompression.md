---
title: "KV-Cache Compression"
type: concept
tags: [ai, inference, kv-cache, long-context, compression]
sources:
  - ba-kv-cache-ya-suo-tui-dao-ji-zhi-zartbot
  - 2604.19528
  - ds4-ascend
last_updated: 2026-10-24
knowledge_schema: synthesis-v1
---

## Definition
[[KVCacheCompression]] reduces the stored, transferred, or recomputed key-value state used by autoregressive attention while preserving enough content and addressing information for useful later-token readout.

## Current Synthesis
The source organizes compression into three multiplicative dimensions. Channel compression shares a smaller latent representation across attention heads; sequence compression merges neighboring positions into fewer entries; layer compression lets several layers consume one published content cache or one sparse selection rather than retaining their own copies. Precision reduction applies after those structural choices and can further shrink the surviving entries.

Compression is not only a memory-capacity optimization. Long agent sessions persist and move cache state across HBM, host memory, SSD, and interconnects, while cache misses trigger repeated prefill after tool calls. A useful design therefore coordinates storage layout, prefill execution, sparse address selection, cache sharing, quantization, and deployment locality rather than optimizing bytes in isolation.

The RaBitQ–TurboQuant comparison supplies a direct task-quality example for key-cache quantization. With identical outlier-channel allocation and cache machinery, a lower-error code matters more at 2.5 bits and long contexts: RaBitQ remains near full precision on Needle-In-A-Haystack while TurboQuant's reconstruction-oriented variant degrades broadly after 32k tokens. At 3.5 bits the difference largely closes, so quantizer choice interacts with bit width rather than defining a fixed ranking.

A simpler latent-attention pattern joins compression to persistence. [[DwarfStar]] compresses K and V into a shared latent before storage and expands it for attention in its reported [[DeepSeekV4Flash]] path, while a custom on-disk format couples tensors to the exact rendered prefix used for reuse. Representation size is therefore tied to identity and lifecycle: compact state is useful only if the runtime can match, load, and replay the same prefix without invalidating it.

## Key Claims
- Channel, sequence, layer, and numerical-precision reductions compound rather than substitute for one another.
- Cross-layer sharing can remove far more duplicate cache state than sequence compression alone, but it reduces which content and addresses later layers may change.
- Prefill early exit and KV compression solve related but distinct problems: one reduces computation over prompt positions, while the other reduces stored and transferred state.
- Main global KV can tolerate a different precision and lifecycle from fresh local sliding-window KV.
- Cache size should include indexer keys, scale metadata, local-state requirements, rendered-prefix identity, persistent copies, and transfer costs rather than only nominal K/V payloads.
- Deployment routing and model architecture are complementary: smaller caches lower movement cost, while locality-aware routing raises reuse probability.
- Equal nominal cache bit widths can yield different long-context attention quality, especially near the lower-precision failure boundary.

## Evidence
Compression dimensions:
- [[ba-kv-cache-ya-suo-tui-dao-ji-zhi-zartbot]] attributes DeepSeek-V4.1-Flash's reduction to a 512-channel latent, 2:1 encoder position compression, four cross-layer cache sources, and FP4 storage.

Accounting and lifecycle:
- [[ba-kv-cache-ya-suo-tui-dao-ji-zhi-zartbot]] derives 288 bytes for one 512-channel FP4 main-KV entry and 890 bytes per token across the reported global cache sources.
- [[ba-kv-cache-ya-suo-tui-dao-ji-zhi-zartbot]] distinguishes HBM runtime state, persisted host/SSD state, and cache-transfer bandwidth as separate service constraints.

Compute interaction:
- [[ba-kv-cache-ya-suo-tui-dao-ji-zhi-zartbot]] uses causal early exit for bulk prompt positions and bounded replay for decoder-local SWA state rather than treating compression alone as a prefill solution.

Task-quality boundary:
- [[2604.19528]] reports Needle-In-A-Haystack scores of 0.987 for full precision, 0.951/0.977 for RaBitQ at 2.5/3.5 bits, and 0.709/0.962 for TurboQuant; its heatmap localizes most TurboQuant 2.5-bit failures to longer contexts and many needle depths.
- [[2604.19528]] reports modest RaBitQ LongBench-E advantages at 2.5 bits on two models and essentially tied averages at 3.5 bits on Llama-3.1-8B.

Latent storage and persistence:
- [[ds4-ascend]] describes shared compressed K/V latent vectors, reports an approximate 8:1–10:1 reduction, and attributes about 26 GB of memory to a million-token context on an M3 Max.
- [[ds4-ascend]] stores a 48-byte header, rendered prefix text, and compressed tensors on disk and preserves exact DSML tool-call text so a re-render does not invalidate prefix matching.

## Counterevidence & Qualifications
Compression ratios are architecture- and accounting-dependent: changing sequence granularity, scale metadata, local windows, prefix representation, persistence policy, or precision changes the comparison. Shared content and addresses create recall and expressivity limits, and low-precision caches may require training adaptation. The DeepSeek-V4.1 analysis does not independently ablate each compression dimension. The DwarfStar port report does not derive its ratio or million-token accounting and provides no cache-load benchmark or failure tests. The RaBitQ-authored experiment repairs TurboQuant's released code, selects its MSE variant, and uses a unified custom cache framework; this makes the comparison more controlled but not a direct or independent reproduction of TurboQuant's original setup.

## What Changed
- Added DwarfStar's compressed-latent and on-disk prefix-reuse case.
- Extended cache accounting from tensor bytes to rendered-prefix identity and persistent lifecycle.

## Related Concepts
- [[CompressedSparseAttention2]] - concrete mechanism combining the first three compression dimensions.
- [[CausalEncoderDecoderArchitecture]] - reduces the computation needed to produce decoder-visible global cache.
- [[BlockQuantization]] - supplies local shared scales for low-precision cache entries.
- [[QuantizationAwareTraining]] - adapts attention to FP4 main-KV distortion.
- [[KVCacheAwareRouting]] - raises the chance that compressed prefix state is reused on the selected worker.
- [[LLMContextManagement]] - determines which long-context material should remain available to the model.
- [[VectorQuantization]] - supplies alternative low-bit representations for cached key vectors.
- [[RaBitQ]] - retained stronger 2.5-bit retrieval quality in the comparison.
- [[TurboQuant]] - reconstruction-oriented cache quantizer whose 3.5-bit results approached RaBitQ.
- [[DwarfStar]] - runtime persisting compressed latent attention state for exact prefix reuse.

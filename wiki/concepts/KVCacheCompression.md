---
title: "KV-Cache Compression"
type: concept
tags: [ai, inference, kv-cache, long-context, compression]
sources:
  - ba-kv-cache-ya-suo-tui-dao-ji-zhi-zartbot
  - 2604.19528
  - ds4-ascend
  - deepseek-v41-tech-report
last_updated: 2026-10-24
knowledge_schema: synthesis-v1
---

## Definition
[[KVCacheCompression]] reduces the stored, transferred, or recomputed key-value state used by autoregressive attention while preserving enough content and addressing information for useful later-token readout.

## Current Synthesis
Cache reduction spans four multiplicative dimensions. Channel compression shares a smaller latent representation across heads; sequence compression merges positions into fewer entries; layer compression lets several layers consume one published content cache or sparse selection; and lower precision shrinks the entries that remain. These mechanisms affect model expressivity differently, so a useful design decides separately which content, addresses, local state, and metadata can be shared or quantized.

Deployment adds a lifecycle dimension. Global KV can exhibit long-tail prefix reuse and justify retention in HBM, host memory, or SSD, while local sliding-window state may be useful only during an active session. [[DeepSeekV41Flash]] exploits this difference: it reports 890 bytes of HBM-resident global KV per token through [[CompressedSparseAttention2]] plus FP4, keeps short-lived SWA KV in a minute-scale DRAM pool, and reconstructs one recent window after a miss rather than persisting local state for days. The resulting persistent footprint is reported at one eighth of its predecessor's under the compared workload.

Compression quality cannot be inferred from nominal bit width alone. The RaBitQ–TurboQuant comparison shows that quantizer error becomes more consequential at 2.5 bits and long contexts, while results converge near 3.5 bits. A simpler DwarfStar path shows another systems boundary: compressed latent state helps only if exact prefix identity, load paths, device placement, and expansion kernels preserve the intended reuse and performance.

## Key Claims
- Channel, sequence, layer, and numerical-precision reductions compound but impose different accuracy and flexibility constraints.
- Prefill early exit reduces prompt computation, whereas cache compression reduces stored and transferred state; robust systems coordinate both.
- Global and local attention state can warrant different precision, retention, and recovery policies.
- Approximate replay can trade bounded recomputation and local-state error for a much smaller long-lived cache.
- Complete accounting includes indexer keys, scales, sparse addresses, local state, rendered-prefix identity, persistent copies, transfers, and miss recovery.
- Equal nominal bit widths can produce different long-context quality, especially near a low-precision failure boundary.
- Smaller cache objects and locality-aware routing are complementary because one lowers movement cost and the other raises reuse probability.

## Evidence
Structural and precision compression:
- [[deepseek-v41-tech-report]] reports cross-layer main-KV and index reuse, 2:1 encoder position compression, FP4 main KV, and a global footprint of 890 bytes per token.
- [[ba-kv-cache-ya-suo-tui-dao-ji-zhi-zartbot]] independently derives 288 bytes per 512-channel FP4 entry and the four-source 890-byte accounting.

Lifecycle and recovery:
- [[deepseek-v41-tech-report]] distinguishes long-tail global KV from minute-scale SWA reuse, moves local state to 10% of host DRAM, retains global prefixes for at least 72 hours, and uses bounded replay after SWA misses.
- [[ds4-ascend]] persists compressed latent tensors with rendered prefix text and preserves exact tool-call serialization for prefix matching.

Task-quality boundary:
- [[2604.19528]] reports Needle-In-A-Haystack scores of 0.987 at full precision, 0.951/0.977 for RaBitQ at 2.5/3.5 bits, and 0.709/0.962 for TurboQuant, with the largest failures at low precision and long contexts.

Compute and implementation interaction:
- [[deepseek-v41-tech-report]] combines causal early exit, hierarchical indexing, fused kernels, and bounded replay rather than treating fewer bytes as a complete serving solution.
- [[ds4-ascend]] shows that CPU dequantization, repeated transfers, and single-device placement can overwhelm a compressed representation's nominal advantage.

## Counterevidence & Qualifications
Compression ratios depend on architecture, scale metadata, local windows, persistence policy, prefix representation, and comparison baseline. Shared content and addresses create recall limits, FP4 main KV requires training adaptation, and bounded replay produces cache-hit-position-dependent local states. The DeepSeek report evaluates a combined system and does not independently ablate every reduction or reproduce it outside its stack. The DwarfStar port does not derive its reported ratio or million-token memory figure. The RaBitQ-authored comparison repairs TurboQuant code and remains an interested-party study despite its controlled setup.

## What Changed
- Added persistent-cache lifecycle as a distinct compression dimension alongside tensor representation.
- Added bounded local-state replay as a storage-versus-recomputation trade-off with explicit approximation risk.
- Replaced secondary-only DeepSeek cache figures with direct report evidence while preserving independent-replication limits.

## Related Concepts
- [[CompressedSparseAttention2]] - combines channel, sequence, layer, and precision reduction in one attention design.
- [[CausalEncoderDecoderArchitecture]] - reduces computation needed to produce decoder-visible global memory.
- [[BlockQuantization]] - supplies local shared scales for low-precision cache entries.
- [[QuantizationAwareTraining]] - adapts attention to FP4 main-KV distortion.
- [[KVCacheAwareRouting]] - increases the probability that reusable prefix state is already local.
- [[LLMContextManagement]] - determines which long-context material should remain available.
- [[VectorQuantization]] - supplies alternative low-bit representations for cached key vectors.

---
title: "DeepSeek-V4.1-Flash"
type: entity
tags: [ai, multimodal-model, mixture-of-experts, long-context, inference]
sources:
  - ba-kv-cache-ya-suo-tui-dao-ji-zhi-zartbot
last_updated: 2026-10-08
knowledge_schema: synthesis-v1
---

## Overview
[[DeepSeekV41Flash]] is a reported 552-billion-parameter multimodal mixture-of-experts model designed for contexts up to one million tokens, with aggressive KV-cache compression and reduced prefill work for input-heavy agent workloads.

## Current Profile
The architecture uses 40 language-backbone layers split evenly between a causal encoder and decoder. CED allows most prompt positions to stop after the encoder; CSA2 supplies local SWA plus sparse global attention while sharing global content and selected addresses across groups of layers. The article reports roughly 8 billion activated parameters per prefill token and 16 billion per decode token, four global KV sources, 890 bytes of global cache growth per token, FP4 main KV, and bounded hierarchical reindexing in the decoder.

The wider model joins four-stream single-pass mHC residual mixing, Top-6-of-384 routed experts, two Engram modules, three DSpark draft blocks, and a 32-layer vision encoder whose 3-by-3 spatial rearrangement reduces visual-token count before projection into the language backbone.

## Key Characteristics
- Splits its backbone into 20 causal-encoder and 20 decoder layers to reduce bulk-prompt computation.
- Uses CSA2 Full, Reindex, and Reuse modes to decouple content refresh, sparse-address refresh, and per-layer queries.
- Maintains three compressed encoder global caches and one per-token decoder global cache rather than one long-lived cache per attention layer.
- Stores main KV and indexer K in FP4 while retaining more sensitive sliding-window KV in FP8.
- Uses a decoder candidate pool to make later reindex work bounded with respect to total context length.
- Combines sparse global attention with a fresh 128-token local sliding window in every applicable layer.
- Adds multimodal input, Engram conditional memory, mHC residual mixing, and DSpark speculative decoding around the cache-focused core.

## Evidence
- End-to-end structure: [[ba-kv-cache-ya-suo-tui-dao-ji-zhi-zartbot]] reproduces the causal-encoder, decoder, vision, Engram, CSA2, and DSpark architecture.
- Cache accounting: [[ba-kv-cache-ya-suo-tui-dao-ji-zhi-zartbot]] derives 890 bytes per token from four FP4 main-KV and indexer-K sources.
- Prefill path: [[ba-kv-cache-ya-suo-tui-dao-ji-zhi-zartbot]] explains midpoint early exit plus bounded decoder SWA replay.
- Decoder indexing: [[ba-kv-cache-ya-suo-tui-dao-ji-zhi-zartbot]] identifies one full scan at layer 20 and pool-limited reindexing at layers 24, 28, 32, and 36.
- Reported performance: [[ba-kv-cache-ya-suo-tui-dao-ji-zhi-zartbot]] reproduces benchmark and context-length compute charts alongside the cache-reduction claim.

## Qualifications
All specifications and outcomes are mediated by one secondary analysis of the model's technical report. The supplied Markdown loses numerous equation symbols and table values, the benchmark and throughput claims lack independent replication, HSI post-training details are undisclosed, and the causal contribution of any one component is not isolated. The model's “encoder” is causal and should not be conflated with the bidirectional encoder in the original Transformer.

## What Changed
- Created a profile centered on the model's prefill, cache, indexing, precision, and multimodal architecture.

## Relationships
- [[CausalEncoderDecoderArchitecture]] - halves the backbone into memory-producing and memory-consuming regions.
- [[CompressedSparseAttention2]] - supplies the model's sparse global attention and cross-layer cache reuse.
- [[HierarchicalSparseIndexer]] - bounds repeated decoder address selection.
- [[BlockQuantization]] - describes the shared-scale layout used for FP4 main KV.
- [[QuantizationAwareTraining]] - adapts the cache representation to low precision.
- [[AttentionMechanism]] - base mechanism whose content, address, and query degrees of freedom are selectively refreshed.
- [[DeepSeekR1]] - separate DeepSeek reasoning-model family already represented in the wiki.

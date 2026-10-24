---
title: "Compressed Sparse Attention 2"
type: concept
tags: [ai, attention, sparse-attention, kv-cache, long-context]
sources:
  - ba-kv-cache-ya-suo-tui-dao-ji-zhi-zartbot
  - deepseek-v41-tech-report
last_updated: 2026-10-24
knowledge_schema: synthesis-v1
---

## Definition
[[CompressedSparseAttention2]] (CSA2) is a sparse-attention design that joins fresh local sliding-window KV with selected global KV while sharing global content, indexer keys, and sometimes Top-K addresses across layers.

## Current Synthesis
CSA2 separates an attention read into content, address, and query. Full layers publish main KV, derive indexer K, compute indexer Q, and select new Top-K addresses. Reindex layers reuse main KV and indexer K but compute a fresh indexer query and address set. Reuse layers share both content and the latest compatible addresses, computing only a new main query and local SWA state. This lets expensive state change more slowly without forcing every layer to use an identical readout.

The design compounds channel, sequence, layer, and precision reductions. The encoder compresses adjacent positions two to one and publishes global content from three Full layers; the decoder keeps per-token content from one Full layer, refreshes addresses in four Reindex layers, and otherwise uses Reuse. A hierarchical decoder indexer performs one full-history scan, creates a candidate pool of up to 16,384 positions, and limits later Reindex searches to that pool. FP4 main KV further reduces the surviving cache representation.

This reuse has a hard semantic boundary. A Reuse layer can reweight the selected content through its query, but it cannot retrieve omitted positions or repair an upstream selection error. Periodic Full and Reindex layers restore content or address flexibility, while the local 128-token SWA branch supplies fresh nearby state.

## Key Claims
- Full, Reindex, and Reuse make cache sharing and sparse-address reuse independent scheduling decisions.
- Main KV and indexer K are shared content state; Top-K indices are address state; main queries and local SWA KV remain layer-local operands.
- Non-overlapping sequence compression and deriving indexer K from main KV simplify the predecessor's compressor paths.
- Cross-layer sharing removes duplicated storage, while address reuse removes repeated indexer work.
- Hierarchical indexing makes later decoder reindex cost bounded by candidate-pool size, although the first Full layer still scans all visible history.
- Query-only reuse cannot recover content excluded by the shared address set, so periodic refresh layers remain necessary.
- Joint use of selected global content and local SWA balances stable long-range memory against fresh nearby information.

## Evidence
Mode contract and schedules:
- [[deepseek-v41-tech-report]] specifies the three execution modes and the encoder schedule of Full plus five Reuse layers versus the decoder schedule of Full or Reindex plus three Reuse layers.
- [[ba-kv-cache-ya-suo-tui-dao-ji-zhi-zartbot]] reconstructs the same contract as different refresh rates for content, address, and query.

Compression and implementation:
- [[deepseek-v41-tech-report]] documents non-overlapping compression groups, removal of compressor absolute positions, projected indexer K, FP4 main KV, cross-pipeline shadow indexers, and fused Reuse paths of 15 prefill or 11 decode kernels.
- [[ba-kv-cache-ya-suo-tui-dao-ji-zhi-zartbot]] derives the cache accounting and explains the 2:1 encoder versus per-token decoder entries.

Indexer and expressivity boundary:
- [[deepseek-v41-tech-report]] defines the first full-range decoder scan, 2,048 eight-position blocks, 16,384-position candidate pool, and later Top-512 selections.
- [[ba-kv-cache-ya-suo-tui-dao-ji-zhi-zartbot]] analyzes Reuse as query-dependent reweighting over a fixed selected dictionary and identifies its inability to recover omitted content.

## Counterevidence & Qualifications
The report evaluates the complete system rather than isolating the quality contribution of every sharing mode, compression ratio, precision choice, or candidate-pool size. Reuse inherits upstream selection errors, and Reindex cannot search outside the shared decoder pool. The vendor reports no systematic degradation in its test suite but explicitly leaves extreme sparse-retrieval failures and robustness boundaries unresolved. The secondary geometric analysis gives an expressivity limit, not proof that learned queries attain every allowable weighting. Performance and kernel counts also depend on the disclosed implementation stack rather than the abstract attention design alone.

## What Changed
- Added primary-source mode, layer-schedule, compressor, and distributed-training details.
- Connected hierarchical candidate restriction and fused kernel counts to CSA2's compute savings.
- Elevated selection error from an inferred limit to an explicit robustness boundary acknowledged by the report.

## Related Concepts
- [[AttentionMechanism]] - provides the query-weighted readout that CSA2 sparsifies and shares.
- [[KVCacheCompression]] - CSA2 combines channel, sequence, layer, and precision reduction.
- [[CausalEncoderDecoderArchitecture]] - schedules global content production differently across encoder and decoder halves.
- [[HierarchicalSparseIndexer]] - restricts later decoder Reindex searches to a shared candidate pool.
- [[BlockQuantization]] - supplies local scaling for FP4 main-KV entries.
- [[TransformerArchitecture]] - places CSA2 beside MoE, residual mixing, and local attention in repeated layers.

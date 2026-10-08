---
title: "Compressed Sparse Attention 2"
type: concept
tags: [ai, attention, sparse-attention, kv-cache, long-context]
sources:
  - ba-kv-cache-ya-suo-tui-dao-ji-zhi-zartbot
last_updated: 2026-10-08
knowledge_schema: synthesis-v1
---

## Definition
[[CompressedSparseAttention2]] (CSA2) is a sparse-attention design that joins local sliding-window KV with selected global latent KV while sharing global content, indexer keys, and sometimes Top-K addresses across layers.

## Current Synthesis
CSA2 separates an attention read into content, address, and query. Content is the compressed global dictionary and is expensive to rebuild; the address is the discrete Top-K subset chosen by an indexer; the query is a cheap, continuous per-layer projection that reweights selected content. Full layers refresh all three, Reindex layers keep content but choose new addresses, and Reuse layers keep content and addresses while changing only the query. Every mode also computes fresh local sliding-window KV.

The design compresses across channel, sequence, and layer dimensions. Encoder Full layers publish 2:1 position-compressed content, while the decoder Full layer preserves per-token entries. Unlike the predecessor described in the source, CSA2 removes overlapping compression groups and absolute positions from the compressor, then projects indexer K from the main-KV latent rather than running a separate hidden-state compression path.

## Key Claims
- Full, Reindex, and Reuse make cache sharing and sparse-address reuse independent decisions.
- Main KV and indexer K are shared content state; Top-K indices are address state; queries and local SWA KV remain fresh layer operands.
- Content changes slowest, addresses change at a middle rate, and queries change every layer because their recomputation costs and semantic roles differ.
- Reuse can still produce layer-specific outputs by exponentially tilting weights over one fixed selected dictionary.
- Reuse cannot retrieve an omitted item, move the dictionary vectors, or escape the selected vectors' convex hull.
- Periodic Full and Reindex layers restore content and address flexibility that query-only layers lack.
- Joint softmax over global selected content and local SWA lets each layer allocate attention between stable long-range memory and fresh nearby state.

## Evidence
Mode contract:
- [[ba-kv-cache-ya-suo-tui-dao-ji-zhi-zartbot]] diagrams which of main KV, indexer K, Top-K indices, main Q, and SWA KV each mode computes or reuses.

Layer schedule:
- [[ba-kv-cache-ya-suo-tui-dao-ji-zhi-zartbot]] groups encoder layers into one Full plus five Reuse layers and decoder layers into one Full or Reindex plus three Reuse layers.

Query-only geometry:
- [[ba-kv-cache-ya-suo-tui-dao-ji-zhi-zartbot]] derives Reuse output as a convex combination over fixed selected vectors and query perturbation as an exponential tilt of a baseline distribution.

Simplified compression:
- [[ba-kv-cache-ya-suo-tui-dao-ji-zhi-zartbot]] contrasts non-overlapping CSA2 groups and projected indexer K with the predecessor's overlapping support and separate indexer compressor.

## Counterevidence & Qualifications
The fixed-dictionary analysis is an expressivity upper bound, not proof that learned queries can reach every distribution allowed by the geometry. Reuse inherits upstream selection errors and cannot repair missing content. Reindex remains limited by the decoder candidate pool, and the source does not disclose full training losses or isolate quality effects by mode. Many formulas were lost in the supplied Markdown, so the retained diagrams and prose support the qualitative contract more strongly than every numerical derivation.

## What Changed
- Established content, address, and query as distinct refreshable attention state.
- Defined the Full/Reindex/Reuse contract and its expressivity boundary.

## Related Concepts
- [[AttentionMechanism]] - provides the query-weighted readout that CSA2 sparsifies and shares.
- [[KVCacheCompression]] - CSA2 implements channel, sequence, and layer compression together.
- [[CausalEncoderDecoderArchitecture]] - schedules CSA2 differently across its memory-producing and memory-consuming halves.
- [[HierarchicalSparseIndexer]] - restricts decoder Reindex searches to a shared candidate pool.
- [[BlockQuantization]] - further reduces the stored main-KV and indexer-K entries.
- [[TransformerArchitecture]] - organizes CSA2 with MoE blocks and residual paths into repeated layers.

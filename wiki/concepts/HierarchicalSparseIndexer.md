---
title: "Hierarchical Sparse Indexer"
type: concept
tags: [ai, sparse-attention, indexing, long-context, inference]
sources:
  - ba-kv-cache-ya-suo-tui-dao-ji-zhi-zartbot
last_updated: 2026-10-08
knowledge_schema: synthesis-v1
---

## Definition
[[HierarchicalSparseIndexer]] (HSI) is a decoder sparse-attention index that performs one full-history position scan, converts those scores into a fixed-size block candidate pool, and limits later index layers to re-ranking positions inside that pool.

## Current Synthesis
The described HSI uses decoder layer 20 as the sole full-range scanner. The same position scores produce that layer's Top-512 addresses and a separate candidate pool: positions are grouped into blocks of eight, each block receives its maximum position score, up to 2,048 blocks are retained, and the block containing the newest visible position is forced into the pool. This yields at most 16,384 candidate positions.

Decoder layers 24, 28, 32, and 36 compute their own queries and select their own Top-512 addresses, but only inside the layer-20 pool. The pool therefore bounds deeper search cost without forcing all index layers to use the same final selection. Reuse layers skip indexing and inherit the latest selection.

## Key Claims
- Separating a broad candidate pool from each layer's final Top-K preserves more layer-specific routing than sharing one Top-K globally.
- Block maxima retain sharp high-scoring positions that mean pooling could dilute.
- A fixed candidate count makes later reindex work independent of total context length, although the first full scan remains linear in visible history.
- The source layer's own Top-K and the shared candidate pool are sibling outputs of one score tensor rather than one being derived from the other.
- Forcing the newest block into the pool protects the causal frontier at the cost of one block budget slot.
- Training must expose deeper indexers to the same restricted pool they will see at inference to avoid a train-serving search-domain mismatch.
- A shared pool can exclude a position that a deeper layer would have ranked highly, so bounded cost creates a recall ceiling.

## Evidence
Pool construction:
- [[ba-kv-cache-ya-suo-tui-dao-ji-zhi-zartbot]] describes eight-position blocks, block-maximum scoring, 2,048 selected blocks, forced retention of the latest block, and a 16,384-position maximum pool.

Layer schedule:
- [[ba-kv-cache-ya-suo-tui-dao-ji-zhi-zartbot]] assigns full scanning to layer 20 and pool-limited independent reindexing to layers 24, 28, 32, and 36.

Cost and recall:
- [[ba-kv-cache-ya-suo-tui-dao-ji-zhi-zartbot]] estimates a substantial reduction in decoder index scoring while explicitly illustrating how a deeper layer's best out-of-pool position becomes unreachable.

## Counterevidence & Qualifications
HSI does not make all sparse indexing constant-cost: the first decoder Full layer still scans visible history. Pool quality depends on whether shallow-layer block maxima cover the positions later layers need, and forced latest-block retention consumes capacity. The report reportedly introduces HSI during post-training but does not disclose the exact training objective, so the article's suggested distillation-style loss is speculative.

## What Changed
- Defined HSI as one full scan followed by shared block-level gating and independent in-pool re-ranking.
- Preserved both the bounded-cost benefit and out-of-pool recall failure mode.

## Related Concepts
- [[CompressedSparseAttention2]] - supplies the Full, Reindex, and Reuse modes that consume the pool.
- [[KVCacheCompression]] - complements smaller stored state by reducing repeated address-generation work.
- [[CausalEncoderDecoderArchitecture]] - places HSI only in the decoder half of the model.
- [[AttentionMechanism]] - consumes the Top-K positions chosen by the indexer.
- [[InferenceLoadBalancing]] - addresses system-level request placement rather than within-model sparse address selection.

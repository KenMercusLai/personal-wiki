---
title: "FlashAttention"
type: concept
tags: [ai, attention, gpu, performance]
sources:
  - flashattention-1
  - foundation-model-kernel-optimization
last_updated: 2026-10-18
knowledge_schema: synthesis-v1
---

## Definition
[[FlashAttention]] is a family of exact attention implementations that tiles queries, keys, values, and online-softmax state so the quadratic score and probability matrices need not be materialized in HBM.

## Current Synthesis
The foundational optimization is algorithmic dataflow rather than fewer attention FLOPs. Conventional composition writes `[S,S]` scores to HBM, reloads them for softmax, writes probabilities, reloads them, and then multiplies by values. A bounded on-chip working set can instead stream or tile keys and values, maintain numerically stable row statistics and output accumulators, and write only the final output plus limited backward state.

The earlier tutorial isolates that intuition with one query per program and scalar-by-scalar accumulation of `exp(q·kᵢ)vᵢ` plus its denominator. It is deliberately not a production algorithm: direct exponentials can overflow, one-element work misses accelerator matrix tiles, and the derivation omits masks, batching, backward, and hardware scheduling.

The field guide adds the production lineage as a sequence of changing bottlenecks. FA1 addressed quadratic HBM I/O; FA2 reduced non-matmul work and improved work partitioning; FA3 used Hopper TMA, WGMMA, and warp specialization to overlap movement, matrix multiplication, and softmax; FA4 rescheduled around Blackwell's different Tensor Core, SFU, shared-memory, TMEM, and two-CTA ratios. The stable principle is bounded intermediate state, while the best tile, partition, and pipeline remain hardware- and shape-specific.

## Key Claims
- Exact attention can avoid quadratic score and probability materialization by combining tiled Q/K/V movement with online normalization.
- HBM traffic, not only arithmetic count, explains why changing evaluation order can improve attention.
- Production implementations require stable softmax, matrix-shaped tiles, masks, tail handling, backward recomputation, and device-specific scheduling beyond the pedagogical loop.
- FA1 through FA4 preserve the broad I/O-aware idea while changing work partition and hardware pipeline as the binding resource moves.
- A forward-only or one-shape result does not establish the best training, prefill, decode, backward, mask, head-dimension, or hardware implementation.

## Evidence
Memory bottleneck and algebraic intuition:
- [[flashattention-1]] contrasts `[S,S]` score and probability matrices with `[S,D]` inputs and outputs and derives a fused loop accumulating an unnormalized weighted sum and denominator.

Scope of the simplified derivation:
- [[flashattention-1]] explicitly says its result is not the real FlashAttention algorithm and provides no stable online recurrence, tiled kernel, backward path, or benchmark.

Hardware-generation progression:
- [[foundation-model-kernel-optimization]] maps FA1 to I/O-aware tiling, FA2 to improved partitioning and reduced non-matmul work, FA3 to Hopper TMA/WGMMA and warp specialization, and FA4 to Blackwell TMEM, asynchronous MMA, software exponentiation choices, and two-CTA scheduling.

Workload boundary:
- [[foundation-model-kernel-optimization]] distinguishes prefill attention from bandwidth-bound paged or split-KV decode attention and warns that the fastest forward schedule may not minimize forward-plus-backward time.

## Counterevidence & Qualifications
The tutorial is conceptual and the field guide is a secondary synthesis of cited primary papers and author notes rather than an independent cross-generation reproduction. Reported utilization figures are configuration-specific, and implementation choice depends on sequence length, head dimension, dtype, mask, dropout, determinism, batch raggedness, backward requirements, accelerator generation, and surrounding layout. Decode with query length near one is a different bandwidth and scheduling regime, so replacing a prefill FlashAttention kernel alone may not improve end-to-end serving.

## What Changed
- Extended the concept from a pedagogical streaming loop to the FA1-through-FA4 production lineage.
- Made stable softmax, tiling, backward, masks, shapes, and hardware scheduling explicit implementation requirements.
- Distinguished large-tile prefill attention from paged, split-KV, bandwidth-bound decode attention.
- Reframed generation changes as responses to moving HBM, partitioning, asynchronous-pipeline, and SFU or on-chip-memory bottlenecks.

## Related Concepts
- [[AttentionMechanism]] - supplies the exact query-key softmax and weighted-value computation being preserved.
- [[OperatorFusion]] - keeps attention stages and bounded intermediates within one coordinated dataflow.
- [[GPUMemoryHierarchy]] - makes HBM traffic and on-chip capacity central constraints.
- [[FoundationModelKernelOptimization]] - places FlashAttention inside a wider workload, communication, and model co-design loop.
- [[KVCacheCompression]] - reduces the cache bytes that dominate long-context decode outside the prefill regime.
- [[ParallelProgramming]] - determines how rows, heads, sequence tiles, warps, and CTAs share the work.

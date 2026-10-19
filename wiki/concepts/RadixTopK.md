---
title: "Radix Top-K"
type: concept
tags: [radix-selection, top-k, integer-algorithms, order-statistics]
sources:
  - radix-top-k
last_updated: 2026-10-19
knowledge_schema: synthesis-v1
---

## Definition
[[RadixTopK]] is a top-k selection algorithm for fixed-width values that processes radix digits from most significant to least significant, certifying complete buckets below the desired rank while recursively refining only the bucket that contains the cutoff.

## Current Synthesis
For unsigned integers divided into fixed-width bit chunks, each round extracts the next chunk from every remaining candidate, counts candidates per digit bucket, and computes an inclusive prefix sum. If `K_remaining` is the number of still-open result slots, the first bucket whose cumulative count reaches it contains the selection boundary. Every smaller bucket is now certainly in the result, the boundary bucket alone advances to the next digit, and every larger bucket is discarded.

The state invariant is more important than the presentation order of the partial result: certified values plus the required number of values from the current boundary bucket still make up the final top-k. `K_remaining` therefore falls by the number newly certified at each round. When all digits are exhausted, candidates can remain tied at the same value; only enough to fill the open slots are retained. Reversing bucket order gives the analogous largest-k procedure.

The available implementation is explanatory, not performance evidence. It uses PyTorch operations on a CUDA device but does not fuse rounds, measure candidate shrinkage, state work or memory complexity, handle signed or floating-point encodings, discuss incomplete final bit chunks, or compare with full sorting, heap selection, quickselect, or optimized library top-k routines.

## Key Claims
- Most-significant-digit partitioning can identify top-k membership without ordering the whole input.
- An inclusive bucket-count scan identifies the unique bucket containing the remaining rank boundary.
- Buckets below the boundary are certified, the boundary bucket is refined, and buckets above it are eliminated.
- Correctness across rounds depends on subtracting newly certified values from the remaining rank.
- Equal values at the final boundary require truncation by slots rather than further value discrimination.
- Reversing the bucket traversal yields largest-k selection.

## Evidence
Selection invariant:
- [[radix-top-k]] states the five-step digit extraction, histogram, inclusive-scan, boundary selection, and remaining-rank update procedure.

Worked example:
- [[radix-top-k]] visually traces two two-bit rounds over nine four-bit values, including bucket counts, cumulative counts, candidate indices, and the final four values.

Reference implementation:
- [[radix-top-k]] supplies a minimal PyTorch/CUDA script that preserves original indices, accumulates certified values, carries forward the boundary candidates, and truncates the final tie set.

## Counterevidence & Qualifications
The sole source is a short tutorial note with one toy input. It assumes unsigned values with a fixed `NUM_BITS` divisible by `BITS_PER_ITER`; extensions to signed integers, floating-point order encodings, other widths, and invalid parameter combinations are asserted only generally or left unspecified. The script uses high-level PyTorch operations and repeated concatenation, so it does not establish an efficient fused GPU implementation. No asymptotic analysis, benchmark, stability guarantee, tie-index policy, adversarial distribution, or comparison against production top-k alternatives is supplied.

## What Changed
- Established the wiki's first dedicated synthesis of Radix Top-K selection.
- Recorded the boundary-bucket invariant and remaining-rank update.
- Added the worked two-round example and explicit implementation limits.

## Related Concepts
- [[ParallelProgramming]] - can execute per-candidate digit extraction and aggregation stages concurrently, subject to implementation-specific synchronization and reduction costs.
- [[GPUMemoryHierarchy]] - constrains efficient GPU placement and movement for candidates, histograms, scans, and compaction, none of which the source measures.

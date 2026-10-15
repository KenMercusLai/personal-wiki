---
title: "FlashAttention"
type: concept
tags: [ai, attention, gpu, performance]
sources:
  - flashattention-1
last_updated: 2026-10-15
knowledge_schema: synthesis-v1
---

## Definition
[[FlashAttention]] is a family of attention implementations that reorganizes exact attention around the GPU memory hierarchy so large score and probability intermediates need not be materialized in HBM.

## Current Synthesis
The tutorial motivates FlashAttention from data movement rather than from fewer mathematical operations. A conventional composition computes `QKᵀ`, writes the `[SL, SL]` scores to HBM, reloads them for softmax, writes the equally large probability matrix, reloads it, and finally multiplies by `V`. When sequence length is much larger than head width, traffic for those quadratic intermediates can dominate the `[SL, D]` inputs and outputs.

Its pedagogical rewrite assigns an independent query output to each GPU program and streams across keys and values. For each pair it computes an exponential score, adds that scalar to a denominator, and adds the score-weighted value to an output vector; after the loop it divides the vector by the denominator. This algebraically defers normalization and reduces the live state to one query, one key/value pair, a scalar denominator, and an output accumulator.

That derivation captures the memory-avoidance intuition but not the published production algorithm. The source does not implement block tiling or numerically stable online softmax, does not cover backward recomputation or masks, and supplies no kernel or benchmark. It should therefore be read as a conceptual bridge into memory-efficient attention, not as an executable FlashAttention specification.

## Key Claims
- The main optimization target is HBM traffic for quadratic score and probability intermediates, not a change to the mathematical attention result.
- Independent query outputs provide a natural parallel partition, subject to each program's limited SRAM.
- Fusing query-key scoring, exponentiation, denominator accumulation, and value aggregation avoids storing length-`SL` intermediate vectors in the simplified forward pass.
- Softmax normalization can be deferred until after the unnormalized weighted-value sum and denominator are complete.
- A pedagogical streaming loop is insufficient to specify production FlashAttention without stability, tiling, masking, backward, and hardware details.

## Evidence
- Memory bottleneck: [[flashattention-1]] contrasts `[SL, SL]` score and probability matrices with `[SL, D]` inputs and outputs and diagrams their repeated HBM store/load path.
- Parallel decomposition: [[flashattention-1]] assigns one query row and output row to each program ID, then streams keys and values that do not fit in SRAM.
- Fused recurrence: [[flashattention-1]] derives a single loop accumulating `exp(q·kᵢ)vᵢ` and `exp(q·kᵢ)`, followed by one division.
- Scope boundary: [[flashattention-1]] explicitly says its result is not the real FlashAttention algorithm and presents no measured implementation.

## Counterevidence & Qualifications
The source's direct exponential accumulation can overflow and is not the stable online-softmax recurrence used by practical implementations. Processing one key/value at a time also omits the tiled matrix operations required for efficient accelerator use. The derivation ignores score scaling, masks, batches, multiple heads, non-divisible shapes, backward propagation, recomputation, layout, synchronization, and device-specific scheduling. It establishes a conceptual mechanism, not speed, bandwidth, or memory measurements.

## What Changed
- Created the concept around HBM-traffic avoidance and deferred softmax normalization.
- Explicitly separated the tutorial's simplified streaming loop from production FlashAttention.

## Related Concepts
- [[AttentionMechanism]] - provides the exact query-key softmax and weighted-value computation being preserved.
- [[OperatorFusion]] - combines attention stages so intermediates remain on chip.
- [[GPUMemoryHierarchy]] - makes SRAM capacity and HBM traffic determine the dataflow.
- [[ParallelProgramming]] - distributes independent query outputs across GPU programs.
- [[TransformerArchitecture]] - repeatedly invokes attention and therefore inherits its memory cost.

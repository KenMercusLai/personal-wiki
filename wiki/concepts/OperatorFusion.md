---
title: "Operator Fusion"
type: concept
tags: [gpu, performance, kernels, memory]
sources:
  - flashattention-1
last_updated: 2026-10-15
knowledge_schema: synthesis-v1
---

## Definition
[[OperatorFusion]] combines adjacent operations into one lower-level kernel so shared inputs can be loaded once and intermediate results can remain in fast local memory instead of being materialized in slower memory.

## Current Synthesis
The tutorial presents fusion as a data-movement optimization. A literal compiler translation of several high-level operations may reload the same value for each operation or store an intermediate to HBM only for the next operation to load it immediately. A fused kernel instead loads the shared working set once, performs the dependent arithmetic in SRAM, and stores only the required outputs.

For attention, fusion alone is not merely concatenating matrix multiplication, softmax, and another matrix multiplication. The `[SL, SL]` intermediates exceed local capacity, so the algorithm must also change evaluation order: compute each exponential score as its key arrives, add it to both the denominator and weighted-value accumulator, and normalize after streaming finishes. Fusion and algebraic reordering therefore work together.

## Key Claims
- Reusing an input across adjacent operations can remove redundant loads.
- Keeping short-lived intermediates in SRAM can remove paired HBM stores and loads.
- Fusion is constrained by the local memory needed for the combined live working set.
- Effective fusion may require algebraic reordering rather than mechanical kernel concatenation.
- In the tutorial's attention derivation, fusion removes large score and probability materializations from HBM.

## Evidence
- Shared-input reuse: [[flashattention-1]] rewrites three additions so the common input is loaded once rather than three times.
- Intermediate retention: [[flashattention-1]] keeps the result of one addition in SRAM for the next addition instead of round-tripping it through HBM.
- Attention dataflow: [[flashattention-1]] diagrams separate score, softmax, and value stages storing and reloading `[SL, SL]` intermediates.
- Algebraic fusion: [[flashattention-1]] folds exponentiation, denominator accumulation, and value weighting into one streaming loop.

## Counterevidence & Qualifications
The source uses a simplified logical GPU model and pseudocode, not compiler output, a real kernel, or measurements. Fusion can increase register or SRAM pressure, reduce occupancy, complicate synchronization, or duplicate computation; these costs are outside the tutorial. The attention example also omits numerical-stability machinery and block-level matrix operations.

## What Changed
- Created the concept from the tutorial's shared-load, intermediate-retention, and attention-reordering examples.

## Related Concepts
- [[GPUMemoryHierarchy]] - determines why avoiding HBM round trips can matter.
- [[FlashAttention]] - applies fusion and reordered softmax evaluation to attention.
- [[AttentionMechanism]] - supplies the operator chain being fused.
- [[ParallelProgramming]] - determines how fused work is partitioned across programs.
- [[HighThroughputIOOptimization]] - shares the broader discipline of optimizing measured data movement rather than arithmetic alone.

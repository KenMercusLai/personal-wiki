---
title: "Operator Fusion"
type: concept
tags: [gpu, performance, kernels, memory]
sources:
  - flashattention-1
  - foundation-model-kernel-optimization
last_updated: 2026-10-18
knowledge_schema: synthesis-v1
---

## Definition
[[OperatorFusion]] combines compatible operations or communication stages so shared inputs and short-lived intermediates can stay in fast local storage or a common pipeline instead of crossing HBM, launch, or synchronization boundaries.

## Current Synthesis
Fusion is fundamentally a dataflow tradeoff. Adjacent pointwise operations can reuse loaded inputs and avoid intermediate stores with little structural risk. A GEMM epilogue can apply scale, bias, activation, gating, residual addition, conversion, or quantization while the accumulator tile is still on chip, making this a common high-return boundary.

More ambitious fusion is conditional. GEMM-to-GEMM or GEMM-to-attention fusion needs compatible tiles, layouts, and pipelines; compute-to-communication fusion needs tile- or chunk-complete dependencies rather than a whole operator barrier. Benefits disappear when the combined live state causes register or shared-memory pressure, spills, occupancy loss, cross-CTA synchronization, duplicated fan-out work, or excessive dynamic-shape variants.

[[FlashAttention]] illustrates why fusion can require algorithmic reordering rather than mechanical kernel concatenation. The quadratic score and probability arrays do not fit local storage, so the implementation tiles inputs and carries online normalization state instead of merely placing matrix multiplication, softmax, and value multiplication in one oversized kernel.

## Key Claims
- Pointwise chains can remove launches and HBM round trips by retaining a small compatible working set.
- GEMM epilogue or prologue fusion is often the safest high-return boundary because the producer tile is already on chip.
- Fusion may require changing evaluation order, tiling, or normalization state rather than concatenating source operators.
- GEMM-to-GEMM and compute-to-communication fusion pay only when layouts, dependencies, and resource use align.
- Register pressure, shared-memory demand, spills, synchronization, duplicated work, and variant explosion can make larger fused kernels slower.
- End-to-end profiling must include layout conversions, graph breaks, workspace, backward recomputation, and communication contention around the fused region.

## Evidence
Shared-input and intermediate reuse:
- [[flashattention-1]] rewrites repeated additions to load a common input once and retain an intermediate locally rather than round-tripping through HBM.

Algebraic dataflow:
- [[flashattention-1]] folds score exponentiation, denominator accumulation, and value weighting into one streaming attention loop because sequence-length intermediates exceed local capacity.

Fusion levels:
- [[foundation-model-kernel-optimization]] distinguishes pointwise chains, GEMM epilogues or prologues, GEMM-to-GEMM or attention pipelines, and compute-to-communication fusion, with increasing resource and scheduling constraints.

Failure conditions:
- [[foundation-model-kernel-optimization]] identifies spills, incompatible tiles, cross-CTA reductions, producer fan-out, JIT variant growth, and backward recomputation as reasons not to fuse blindly.

## Counterevidence & Qualifications
The available evidence is explanatory rather than a controlled benchmark of one fusion compiler or kernel suite. Fusion profitability depends on shapes, dtype, device generation, local-memory capacity, compiler quality, launch cost, consumer fan-out, backward requirements, and surrounding graph structure. A fused kernel can show fewer launches yet lose end-to-end time through lower occupancy, extra recomputation, layout conversion, or competition with communication for SM, cache, and HBM resources.

## What Changed
- Expanded fusion from shared-load and intermediate retention into a four-level dataflow hierarchy.
- Identified GEMM epilogues as a common high-return boundary while making larger fusion conditional.
- Added explicit resource, synchronization, fan-out, dynamic-shape, and backward failure modes.
- Connected compute-to-communication fusion with fine-grained tile or chunk dependencies.

## Related Concepts
- [[GPUMemoryHierarchy]] - determines the cost saved by retaining values locally and the capacity limit of a fused working set.
- [[FlashAttention]] - combines tiling, online normalization, and fusion to avoid quadratic attention intermediates.
- [[FoundationModelKernelOptimization]] - locates fusion within operator-graph and distributed-system optimization.
- [[AttentionMechanism]] - supplies one operator chain whose evaluation order can be fused.
- [[DistributedNeuralNetworkTraining]] - supplies collectives and dependencies for compute-to-communication fusion.
- [[ParallelProgramming]] - determines the thread, warp, CTA, and tile ownership inside a fused schedule.

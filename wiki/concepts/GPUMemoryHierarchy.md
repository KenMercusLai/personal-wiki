---
title: "GPU Memory Hierarchy"
type: concept
tags: [gpu, memory, performance, hardware]
sources:
  - flashattention-1
last_updated: 2026-10-15
knowledge_schema: synthesis-v1
---

## Definition
[[GPUMemoryHierarchy]] is the layered storage model in which host DRAM, device HBM, and smaller on-chip SRAM-like storage trade increasing capacity for decreasing access speed and determine where GPU operands and intermediates can live.

## Current Synthesis
The tutorial uses a deliberately abstract three-level model: CPU DRAM holds host data, GPU HBM holds device-visible tensors, and GPU SRAM represents the much smaller local storage used during arithmetic. Computation therefore includes explicit data movement: operands load from HBM into SRAM, arithmetic creates or updates local state, and required results store back to HBM.

Capacity makes this an algorithmic constraint rather than a vocabulary detail. Large tensors that fit in HBM may not fit in a program's local storage, so work must be tiled or streamed. Repeatedly materializing large intermediates in HBM can dominate execution even when the arithmetic is unchanged, which is why [[OperatorFusion]] and [[FlashAttention]] organize their dataflow around keeping a bounded working set on chip.

## Key Claims
- Host DRAM, GPU HBM, and on-chip local storage form a capacity-versus-speed hierarchy in the tutorial's logical model.
- Arithmetic operates on data after it has been loaded into local GPU storage.
- Limited local capacity forces large arrays to be partitioned, tiled, or streamed.
- HBM loads, stores, and intermediate allocation are performance costs distinct from arithmetic.
- Algorithm design can reduce traffic by reusing loaded values and retaining bounded intermediates locally.

## Evidence
- Hierarchy diagram: [[flashattention-1]] places GPU SRAM above GPU HBM and CPU DRAM, with capacity increasing and speed decreasing down the hierarchy.
- Explicit movement: [[flashattention-1]] rewrites a simple addition with HBM allocation, two loads, local arithmetic, and one store.
- Capacity constraint: [[flashattention-1]] assumes a program can hold order-`D` state but not order-`SL` state, motivating streaming attention.
- Traffic consequence: [[flashattention-1]] identifies score and probability matrices as large HBM intermediates that fusion should avoid.

## Counterevidence & Qualifications
The hierarchy is pedagogical. The source explicitly groups hardware registers and caches under the logical label “SRAM,” while real devices expose multiple register, shared-memory, cache, HBM, interconnect, and host-memory behaviors. It supplies no capacities, bandwidths, latencies, occupancy model, or device comparison, so the qualitative ordering should not be used as a quantitative hardware specification.

## What Changed
- Created the concept from the tutorial's logical storage hierarchy and explicit load/store model.

## Related Concepts
- [[OperatorFusion]] - reduces transfers between HBM and local storage.
- [[FlashAttention]] - reorganizes attention around bounded on-chip state.
- [[ParallelProgramming]] - partitions data so each program's working set fits local capacity.
- [[AttentionMechanism]] - produces the large intermediates whose placement motivates the optimization.
- [[LatencyHierarchy]] - generalizes the idea that movement across storage levels has unequal cost.

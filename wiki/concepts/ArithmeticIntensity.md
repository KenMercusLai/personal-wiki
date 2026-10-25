---
title: "Arithmetic Intensity"
type: concept
tags: [systems-performance, roofline-model, memory-hierarchy]
sources:
  - ann-v3
  - how-to-llm-inference
last_updated: 2026-10-25
knowledge_schema: synthesis-v1
---

## Definition
[[ArithmeticIntensity]] is the ratio of arithmetic work to data movement, used to predict whether a workload is more likely to be limited by compute throughput or memory bandwidth.

## Current Synthesis
A low-intensity kernel performs little work per fetched byte, so memory movement tends to dominate; a high-intensity kernel reuses or expands each fetched unit into enough work that instruction throughput becomes limiting. The distinction is hardware- and implementation-relative rather than an immutable label for an application.

[[ANNv3]] demonstrates that representation can change the regime. Full-precision vector distance uses each fetched coordinate once and is bandwidth-bound. One-bit quantization reduces bytes per logical coordinate and RaBitQ reuses each bit in several estimation terms, raising the source's stated arithmetic intensity by 64×. The resulting production bottleneck shifts to CPU execution, making an AVX-512 popcount optimization visible end to end.

Local LLM inference shows that shape can change the regime without changing the underlying linear algebra. Decode multiplies a single activation row by each weight matrix, so each streamed weight is used once and GEMV tends to be bandwidth-bound. Prefill multiplies many prompt rows at once, allowing a weight tile to remain in registers or cache across several output columns; once reuse raises intensity above the machine's compute-to-bandwidth ratio, GEMM becomes compute-bound. Quantizing weights reduces bytes on the decode critical path only if the kernel computes directly on the compact representation.

## Key Claims
- Arithmetic intensity relates work performed to bytes moved rather than measuring either resource alone.
- Low-intensity vector dot products commonly expose memory-hierarchy bandwidth limits.
- Compression can increase intensity by packing more logical operations into each fetched byte.
- Moving data into faster, smaller tiers and reducing its size can change the active bottleneck.
- A microbenchmark improvement supports a bottleneck diagnosis only when the affected kernel matters to end-to-end performance.
- Tensor shape and batch width can move the same logical operation between bandwidth- and compute-limited regimes.

## Evidence
Bandwidth-bound phase:
- [[ann-v3]] models full-precision vector distance as one use per fetched element and derives per-level scan bandwidth for its clustered index.

Compute-bound transition:
- [[ann-v3]] attributes 64× higher arithmetic intensity to one-bit RaBitQ estimation and reports a 30% kernel improvement translating to about 5% production throughput after adopting AVX-512 popcount.

Shape-dependent transition:
- [[how-to-llm-inference]] contrasts one-row decode GEMV with multi-row prefill GEMM and attributes the latter's compute pressure to weight-tile reuse.
- [[how-to-llm-inference]] reports approximately 50 GB/s effective bandwidth for its largest decode kernels on a machine rated near 55 GB/s usable bandwidth.

## Counterevidence & Qualifications
The sources' ceilings and regime labels are hardware- and implementation-relative rather than universal. Real systems also face latency, concurrency, cache conflicts, branching, instruction mix, I/O granularity, scheduling, network fan-out, and workload skew. Compression has encoding, metadata, quality, and refinement costs, so increased arithmetic intensity is not automatically an end-to-end win. The LLM result covers one model and CPU setup without a named processor, thread count, comparison runtime, or independent reproduction.

## What Changed
- Added activation shape and weight reuse as a second route across the bandwidth-compute boundary.
- Added direct compact-format execution as a condition for quantization to reduce critical-path traffic.

## Related Concepts
- [[ANNv3]] - concrete system whose bottleneck changes after binary quantization.
- [[VectorQuantization]] - representation change that reduces bytes while adding estimation work.
- [[ApproximateNearestNeighborSearch]] - workload used in the source's roofline analysis.
- [[GPUMemoryHierarchy]] - related tier and bandwidth model for accelerator workloads.
- [[LLMInferenceSystems]] - applies the regime distinction separately to prompt prefill and token decode.

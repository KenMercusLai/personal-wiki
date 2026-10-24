---
title: "Arithmetic Intensity"
type: concept
tags: [systems-performance, roofline-model, memory-hierarchy]
sources:
  - ann-v3
last_updated: 2026-10-24
knowledge_schema: synthesis-v1
---

## Definition
[[ArithmeticIntensity]] is the ratio of arithmetic work to data movement, used to predict whether a workload is more likely to be limited by compute throughput or memory bandwidth.

## Current Synthesis
A low-intensity kernel performs little work per fetched byte, so memory movement tends to dominate; a high-intensity kernel reuses or expands each fetched unit into enough work that instruction throughput becomes limiting. The distinction is hardware- and implementation-relative rather than an immutable label for an application.

[[ANNv3]] demonstrates that representation can change the regime. Full-precision vector distance uses each fetched coordinate once and is bandwidth-bound. One-bit quantization reduces bytes per logical coordinate and RaBitQ reuses each bit in several estimation terms, raising the source's stated arithmetic intensity by 64×. The resulting production bottleneck shifts to CPU execution, making an AVX-512 popcount optimization visible end to end.

## Key Claims
- Arithmetic intensity relates work performed to bytes moved rather than measuring either resource alone.
- Low-intensity vector dot products commonly expose memory-hierarchy bandwidth limits.
- Compression can increase intensity by packing more logical operations into each fetched byte.
- Moving data into faster, smaller tiers and reducing its size can change the active bottleneck.
- A microbenchmark improvement supports a bottleneck diagnosis only when the affected kernel matters to end-to-end performance.

## Evidence
Bandwidth-bound phase:
- [[ann-v3]] models full-precision vector distance as one use per fetched element and derives per-level scan bandwidth for its clustered index.

Compute-bound transition:
- [[ann-v3]] attributes 64× higher arithmetic intensity to one-bit RaBitQ estimation and reports a 30% kernel improvement translating to about 5% production throughput after adopting AVX-512 popcount.

## Counterevidence & Qualifications
The source's QPS ceilings are simplified roofline calculations, not measured universal limits. Real systems also face latency, concurrency, cache conflicts, branching, instruction mix, I/O granularity, scheduling, network fan-out, and workload skew. Compression has encoding, metadata, quality, and refinement costs, so increased arithmetic intensity is not automatically an end-to-end win.

## What Changed
- Created the concept from a vector-search case that crosses from bandwidth-bound to compute-bound after quantization.
- Added end-to-end translation as a check on kernel-level bottleneck claims.

## Related Concepts
- [[ANNv3]] - concrete system whose bottleneck changes after binary quantization.
- [[VectorQuantization]] - representation change that reduces bytes while adding estimation work.
- [[ApproximateNearestNeighborSearch]] - workload used in the source's roofline analysis.
- [[GPUMemoryHierarchy]] - related tier and bandwidth model for accelerator workloads.

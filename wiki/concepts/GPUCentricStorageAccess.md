---
title: "GPU-Centric Storage Access"
type: concept
tags: [gpu, storage, nvme, io, machine-learning-systems]
sources:
  - geminifs
last_updated: 2026-10-17
knowledge_schema: synthesis-v1
---

## Definition
[[GPUCentricStorageAccess]] is an I/O architecture in which GPU threads initiate storage requests and operate device-visible queues directly, avoiding per-request CPU orchestration between GPU memory and NVMe storage.

## Current Synthesis
GPU-centric access separates data-plane directness from control-plane directness. A CPU-centric system can use DMA between NVMe and HBM yet still require host threads, system calls, or page-fault handling to initiate each transfer. Moving NVMe submission and completion queues into GPU memory lets the GPU generate fine-grained requests at its own concurrency, shortening the path and avoiding CPU-core contention.

Raw-device directness creates a management problem: private block ownership and isolated user-space metadata make files harder to protect, share, recover, or access from both processors. [[GeminiFS]] demonstrates a middle design. The CPU keeps namespace and allocation authority, embeds a stable per-file block map, and establishes GPU queue pairs; the GPU then performs offset translation and data I/O without returning to the CPU for each request. This gains file-based direct access by deliberately limiting mutation and POSIX semantics.

## Key Claims
- Direct GPU-to-storage DMA does not by itself remove CPU orchestration; the request control path must also move off the host.
- GPU-resident NVMe queues can exploit accelerator parallelism for many small requests that saturate CPU-mediated paths.
- Giving each process raw block-device control sacrifices useful file abstraction, sharing, isolation, consistency, and durability boundaries.
- A companion file system can retain CPU-owned namespace and allocation while delegating stable per-file translation and I/O to the GPU.
- The practicality of this split depends on workload predictability, pre-allocation, restricted mutation, explicit synchronization, and device-driver support.
- Performance claims must separate uncached storage access from GPU-memory page-cache throughput and application-level effects.

## Evidence
- Control-path distinction: [[geminifs]] contrasts GPUfs and GDS with BaM, showing that direct DMA can remain CPU-initiated while BaM places control and data paths on the GPU.
- CPU scaling limit: [[geminifs]] reports rising GPUfs latency after GPU threads exceed CPU service capacity and persistent GDS software overhead despite batching.
- File-abstraction gap: [[geminifs]] argues that raw-device GPU access inherits user-space metadata, integrity, sharing, crash-consistency, and durability burdens.
- Companion split: [[geminifs]] embeds a two-level block map per file and registers GPU I/O queues through SNVMe while leaving file management on the host.
- Performance boundary: [[geminifs]] reports GeminiFS within about 4.6% of BaM bandwidth and 4.8% of its latency in the selected uncached 4 KiB tests, but measures cache mechanics separately through memory replication.

## Counterevidence & Qualifications
The concept is grounded here in one prototype on Nvidia GPU APIs, one Optane NVMe device, EXT4, and selected ML patterns. CPU orchestration can be competitive at low concurrency: the paper reports lower GDS latency for one to eight threads. Predictable, pre-allocated, mostly immutable data is materially easier than general files with arbitrary growth, rename, truncation, permissions, journaling, recovery, and concurrent CPU/GPU mutation. Direct queue access also shifts validation, isolation, lifecycle, and failure-recovery responsibilities into drivers and libraries; the source does not establish production security or crash behavior.

## What Changed
- Created the concept by distinguishing a direct data plane from a GPU-owned control plane.
- Added companion file systems as a qualified middle ground between CPU-orchestrated files and GPU-owned raw devices.

## Related Concepts
- [[GPUMemoryHierarchy]] - locates NVMe below HBM and on-chip storage as a larger, slower capacity tier.
- [[HighThroughputIOOptimization]] - examines queueing, memory registration, translation, concurrency, and topology across the complete I/O path.
- [[StoragePerformanceBenchmarking]] - controls cache state, request size, parallelism, and device activity when evaluating direct storage.
- [[DatabaseBypass]] - shares the pattern of shortening a managed storage path while inheriting format, consistency, and validation obligations.

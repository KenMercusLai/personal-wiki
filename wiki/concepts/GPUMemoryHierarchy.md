---
title: "GPU Memory Hierarchy"
type: concept
tags: [gpu, memory, performance, hardware]
sources:
  - flashattention-1
  - geminifs
  - outperforming-cublas-nvfp4
last_updated: 2026-10-18
knowledge_schema: synthesis-v1
---

## Definition
[[GPUMemoryHierarchy]] is the layered storage model in which NVMe storage, host DRAM, device HBM, and smaller on-chip SRAM-like storage trade increasing capacity for decreasing access speed and determine where GPU data, operands, and intermediates can live.

## Current Synthesis
The FlashAttention tutorial uses a deliberately abstract three-level compute model: CPU DRAM holds host data, GPU HBM holds device-visible tensors, and GPU SRAM represents the much smaller local storage used during arithmetic. Computation therefore includes explicit data movement: operands load from HBM into SRAM, arithmetic creates or updates local state, and required results store back to HBM.

Capacity makes this an algorithmic constraint rather than a vocabulary detail. Large tensors that fit in HBM may not fit in a program's local storage, so work must be tiled or streamed. Repeatedly materializing large intermediates in HBM can dominate execution even when the arithmetic is unchanged, which is why [[OperatorFusion]] and [[FlashAttention]] organize their dataflow around keeping a bounded working set on chip.

[[geminifs]] extends the hierarchy below DRAM and HBM to persistent NVMe when model inputs, weights, activations, graph data, checkpoints, or KV cache exceed device memory or require sharing and durability. That tier is not transparent GPU memory: request initiation, logical-to-physical translation, queue placement, file semantics, page-cache policy, PCIe transfer, and synchronization become part of the data path. [[GPUCentricStorageAccess]] can remove per-request CPU orchestration, while a GPU-resident page cache exploits HBM bandwidth for locality, but neither makes storage equivalent to HBM.

[[outperforming-cublas-nvfp4]] resolves the on-chip side of the abstraction for GB300. TMA moves packed operands and scale bytes from HBM into separate shared-memory rings; scale factors then move into TMEM, tensor cores accumulate FP32 output there, and epilogue warps drain TMEM through registers to FP16 global stores. Capacity and timing couple these levels: six operand stages and seven scale stages consume 99.1% of available shared memory, while two output buffers fit into TMEM only by overlapping 36 columns and draining the collision region first.

The same source treats GB300's 128 MB L2 behaviorally as two halves associated with two SM requester populations. Physical addresses select a home side in 4 KiB granules, while each cluster has a near side; these can differ, so first-touch placement and later reuse are separate questions. Assigning repeated A-row requests to one requester population does not move all of that row into one physical half, but it avoids building duplicate useful residency across both populations.

## Key Claims
- NVMe storage, host DRAM, GPU HBM, and on-chip local storage form a broad capacity-versus-speed hierarchy, although each tier has distinct access semantics.
- Arithmetic operates on data after it has been loaded into local GPU storage.
- Limited local capacity forces large arrays to be partitioned, tiled, or streamed.
- HBM loads, stores, and intermediate allocation are performance costs distinct from arithmetic.
- Algorithm design can reduce traffic by reusing loaded values and retaining bounded intermediates locally.
- Extending capacity to storage adds file metadata, address translation, request queues, PCIe movement, caching, and persistence policy to the optimization problem.
- Real accelerator tiers include distinct shared memory, tensor memory, registers, and partitioned caches whose capacity, ownership, and synchronization semantics can shape the kernel schedule.

## Evidence
- Hierarchy diagram: [[flashattention-1]] places GPU SRAM above GPU HBM and CPU DRAM, with capacity increasing and speed decreasing down the hierarchy.
- Explicit movement: [[flashattention-1]] rewrites a simple addition with HBM allocation, two loads, local arithmetic, and one store.
- Capacity constraint: [[flashattention-1]] assumes a program can hold order-`D` state but not order-`SL` state, motivating streaming attention.
- Traffic consequence: [[flashattention-1]] identifies score and probability matrices as large HBM intermediates that fusion should avoid.
- Storage tier: [[geminifs]] catalogs training inputs, graph structures, model state, activations, checkpoints, and KV cache whose scale or retention can motivate NVMe-backed GPU access.
- Access path: [[geminifs]] shows that a storage-backed tier requires per-file block translation, GPU-visible NVMe queues, explicit read/write calls, and an optional HBM page cache.
- Quantitative separation: [[geminifs]] measures roughly 6 GB/s on the tested NVMe path, hundreds of GB/s inside GPU page-cache microbenchmarks, and a 1,935 GB/s nominal HBM peak, illustrating that placement and cache hits change the governing bandwidth by orders of magnitude.
- Blackwell on-chip path: [[outperforming-cublas-nvfp4]] diagrams HBM-to-TMA-to-SMEM operand movement, SMEM-to-TMEM scale copies, tensor-core output into TMEM, and register-mediated FP16 stores.
- Capacity-driven synchronization: [[outperforming-cublas-nvfp4]] accounts for 230,400 of 232,448 shared-memory bytes and overlaps two 256-column accumulators by 36 columns so scale storage still fits in 512-column TMEM.
- Cache topology: [[outperforming-cublas-nvfp4]] reports near/far dependent atomic latency of 148/344 ns, variable SM-side census, 4 KiB home granules, and a scheduler that couples row ownership with local tile order.

## Counterevidence & Qualifications
The hierarchy remains an abstraction. [[flashattention-1]] explicitly groups hardware registers and caches under the logical label “SRAM,” while real devices expose multiple register, shared-memory, tensor-memory, cache, HBM, interconnect, host-memory, and storage behaviors. [[geminifs]] adds quantitative results, but only for one host, A100-class GPU, PCIe link, Optane NVMe device, EXT4 configuration, and selected workloads. Its software-managed storage interface is not ordinary load/store memory, cache results do not equal device throughput, and larger pages or more prefetching can trade bandwidth against amplification, capacity, contention, and workload mismatch. The GB300 topology is a reverse-engineered behavioral model from one author's microbenchmarks and cited clues, not vendor-confirmed physical documentation; dependent latency does not itself establish GEMM benefit, SM-side splits vary, and the owned-side schedule is shape-specific.

## What Changed
- Resolved the abstract on-chip tier into Blackwell shared memory, TMEM, registers, and tensor-core dataflow.
- Added capacity-driven buffer overlap and synchronization as part of memory placement.
- Added the behavioral split-L2 distinction between an address's home side and an SM's near side.

## Related Concepts
- [[OperatorFusion]] - reduces transfers between HBM and local storage.
- [[FlashAttention]] - reorganizes attention around bounded on-chip state.
- [[ParallelProgramming]] - partitions data so each program's working set fits local capacity.
- [[AttentionMechanism]] - produces the large intermediates whose placement motivates the optimization.
- [[LatencyHierarchy]] - generalizes the idea that movement across storage levels has unequal cost.
- [[GPUCentricStorageAccess]] - moves storage request initiation and NVMe queue handling into GPU execution.
- [[GeminiFS]] - implements a file-based NVMe tier plus an HBM-resident software page cache.

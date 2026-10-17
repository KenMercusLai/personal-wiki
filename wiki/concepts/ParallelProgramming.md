---
title: "Parallel Programming"
type: concept
tags: [parallel-programming, concurrency, software-development]
sources:
  - blog-wulc-python-bing-xing-bian-cheng-gai-shu
  - flashattention-1
  - lemire-parsing-json
  - scaling-elections
last_updated: 2026-10-18
knowledge_schema: synthesis-v1
---

## Definition
[[ParallelProgramming]] is a programming model where multiple processes, accelerator programs, or other work units execute at the same time by partitioning a larger computation across independent compute resources.

## Current Synthesis
Wulc distinguishes parallel programming from concurrency by grounding parallelism in a multi-core environment. The inspected parallel-programming diagram shows one parallel program dispatching processes to CPU01 through CPU04, making the defining feature simultaneous execution rather than scheduler-created pseudo-parallel progress on one CPU.

The source treats parallel programming as one member of a broader family that also includes concurrent and distributed programming. Because parallelized processes still work on the same task, communication remains necessary, and shared state, message passing, deadlock, starvation, and race conditions remain part of the design surface.

The GPU tutorial adds data-parallel decomposition rather than process coordination. A generic program receives an ID, maps that ID to an equally sized slice, and performs the same operation on its slice. Good partitions keep work balanced, fit each program's local storage, and exploit independent dimensions. For attention, separate queries can run independently, while each query's reduction across keys remains an internal loop in the simplified design.

Lemire adds record-parallel CPU threads under free-threaded Python 3.14. Independent NDJSON records are mapped to callbacks, each worker updates private counters, and the main thread merges only compact summaries after all events complete. This makes partition independence and reduction shape as important as core count: the lazy fastsimdjson path reportedly scales from 2.13 GB/s on one core to 65.7 GB/s on 64 cores, about 31-fold rather than linearly.

The blocked [[SchulzeMethod]] case adds partially parallel dynamic programming. Its outer pivot order remains sequential, but each pivot tile creates three phases: update the diagonal dependency, update the pivot row and column, then update all remaining tiles in parallel. This shows that useful parallelism does not require the whole algorithm to be independent; it can come from identifying the exact dependency frontier and choosing tiles that reuse local data. CPU SIMD and GPU kernels then exploit different levels of the same decomposition.

## Key Claims
- Parallel programming is true simultaneous execution in the source's model.
- Parallelism is distinct from scheduler-mediated [[ConcurrentProgramming]].
- Parallelized processes need communication because they cooperate on one task.
- Parallel programming inherits coordination hazards such as [[Deadlock]] and [[RaceCondition]].
- GPU data-parallel programs use an ID to select balanced, independent partitions whose working sets fit local capacity.
- Record-parallel CPU work scales more cleanly when hot-path state is thread-local and only compact results require a final merge.
- A sequential outer dependency can still permit broad tile-level parallelism when dependent, partially dependent, and independent phases are explicit.

## Evidence
- Multi-core definition: [[blog-wulc-python-bing-xing-bian-cheng-gai-shu]] says each core can run a process at the same time in a multi-core environment.
- Diagram evidence: [[blog-wulc-python-bing-xing-bian-cheng-gai-shu]] includes an inspected diagram with four processes mapped to four CPUs.
- Communication requirement: [[blog-wulc-python-bing-xing-bian-cheng-gai-shu]] says communication is necessary because parallelized processes complete the same task.
- Failure scope: [[blog-wulc-python-bing-xing-bian-cheng-gai-shu]] groups deadlock, starvation, and race conditions under problems encountered in parallelized programming.
- GPU partitioning: [[flashattention-1]] maps program IDs to equal vector slices and then uses independent queries as the partitioning dimension for attention.
- CPU record partitioning: [[lemire-parsing-json]] maps 2.2 million NDJSON events across 64 free-threaded Python workers.
- Local reduction: [[lemire-parsing-json]] uses one counter pair per worker and merges the small summaries only after event processing completes.
- Measured scaling: [[lemire-parsing-json]] reports 65.7 GB/s on 64 cores versus 2.13 GB/s on one core for the same lazy strategy.
- Dependency-aware tiling: [[scaling-elections]] orders one diagonal tile, its row and column, and then all remaining tiles for each strongest-path pivot.
- Cross-architecture execution: [[scaling-elections]] reports one Mojo formulation across CPU SIMD and Nvidia and AMD GPUs, alongside Numba and CUDA variants.

## Counterevidence & Qualifications
The two introductory articles simplify their execution models. Wulc does not distinguish threads from processes in depth or discuss Python's GIL, while the GPU tutorial uses an abstract “compute unit” and program-ID model without warps, thread blocks, synchronization, occupancy, memory coalescing, or real hardware measurements. Its one-query-per-program attention partition is pedagogical rather than a claim about an optimal production kernel. Lemire supplies a concrete CPU measurement, but it is a maintainer-authored best-of-seven result for one in-memory selective-parsing workload on one server. Vardanian's results are likewise author-run and compare heterogeneous hardware and unevenly tuned implementations; blocking preserves the Schulze recurrence's cubic work and sequential pivot order. Free-threaded availability, native-library work, memory bandwidth, allocation, compiler maturity, tuning effort, power, cost, and workload balance all limit generalization.

## What Changed
- Added a measured free-threaded Python case based on independent records, thread-local state, and final reduction.
- Qualified the roughly 31-fold 64-core gain by its parser, hardware, data-residency, and benchmark boundaries.
- Created the concept page from Wulc's multi-core parallel-programming overview.
- Expanded the concept from process-level CPU parallelism to ID-based GPU data partitioning.
- Added dependency-aware blocked execution in which a sequential pivot surrounds parallel row, column, and remaining-tile phases.

## Related Concepts
- [[ConcurrentProgramming]] - concurrency is contrasted as pseudo-parallel scheduling.
- [[DistributedProgramming]] - distributed programming spreads work across physically separate machines.
- [[InterprocessCommunication]] - parallelized processes need shared state or message passing.
- [[PythonConcurrencyLibraries]] - Python modules provide practical routes into concurrent, parallel, and distributed work.
- [[ConcurrencyFailureModes]] - parallel work can expose resource and synchronization hazards.
- [[GPUMemoryHierarchy]] - bounds how much data each accelerator program can process locally.
- [[FlashAttention]] - uses query independence as one axis for parallel attention work.
- [[SelectiveJSONParsing]] - combines record partitioning with avoided materialization of unused values.
- [[Fastsimdjson]] - supplies the measured multi-threaded mapping interface.
- [[SchulzeMethod]] - demonstrates tiled parallelism around a sequential dynamic-programming dependency.
- [[Mojo]] - expresses the source's CPU SIMD and cross-vendor GPU variants.

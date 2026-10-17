---
title: "Parallel Programming"
type: concept
tags: [parallel-programming, concurrency, software-development]
sources:
  - blog-wulc-python-bing-xing-bian-cheng-gai-shu
  - flashattention-1
  - lemire-parsing-json
last_updated: 2026-10-17
knowledge_schema: synthesis-v1
---

## Definition
[[ParallelProgramming]] is a programming model where multiple processes, accelerator programs, or other work units execute at the same time by partitioning a larger computation across independent compute resources.

## Current Synthesis
Wulc distinguishes parallel programming from concurrency by grounding parallelism in a multi-core environment. The inspected parallel-programming diagram shows one parallel program dispatching processes to CPU01 through CPU04, making the defining feature simultaneous execution rather than scheduler-created pseudo-parallel progress on one CPU.

The source treats parallel programming as one member of a broader family that also includes concurrent and distributed programming. Because parallelized processes still work on the same task, communication remains necessary, and shared state, message passing, deadlock, starvation, and race conditions remain part of the design surface.

The GPU tutorial adds data-parallel decomposition rather than process coordination. A generic program receives an ID, maps that ID to an equally sized slice, and performs the same operation on its slice. Good partitions keep work balanced, fit each program's local storage, and exploit independent dimensions. For attention, separate queries can run independently, while each query's reduction across keys remains an internal loop in the simplified design.

Lemire adds record-parallel CPU threads under free-threaded Python 3.14. Independent NDJSON records are mapped to callbacks, each worker updates private counters, and the main thread merges only compact summaries after all events complete. This makes partition independence and reduction shape as important as core count: the lazy fastsimdjson path reportedly scales from 2.13 GB/s on one core to 65.7 GB/s on 64 cores, about 31-fold rather than linearly.

## Key Claims
- Parallel programming is true simultaneous execution in the source's model.
- Multi-core CPUs and many-unit accelerators are hardware bases for simultaneous work.
- Parallelism is distinct from scheduler-mediated [[ConcurrentProgramming]].
- Parallelized processes need communication because they cooperate on one task.
- Parallel programming inherits coordination hazards such as [[Deadlock]] and [[RaceCondition]].
- GPU data-parallel programs use an ID to select balanced, independent partitions whose working sets fit local capacity.
- Record-parallel CPU work scales more cleanly when hot-path state is thread-local and only compact results require a final merge.

## Evidence
- Multi-core definition: [[blog-wulc-python-bing-xing-bian-cheng-gai-shu]] says each core can run a process at the same time in a multi-core environment.
- Diagram evidence: [[blog-wulc-python-bing-xing-bian-cheng-gai-shu]] includes an inspected diagram with four processes mapped to four CPUs.
- Communication requirement: [[blog-wulc-python-bing-xing-bian-cheng-gai-shu]] says communication is necessary because parallelized processes complete the same task.
- Failure scope: [[blog-wulc-python-bing-xing-bian-cheng-gai-shu]] groups deadlock, starvation, and race conditions under problems encountered in parallelized programming.
- GPU partitioning: [[flashattention-1]] maps program IDs to equal vector slices and then uses independent queries as the partitioning dimension for attention.
- CPU record partitioning: [[lemire-parsing-json]] maps 2.2 million NDJSON events across 64 free-threaded Python workers.
- Local reduction: [[lemire-parsing-json]] uses one counter pair per worker and merges the small summaries only after event processing completes.
- Measured scaling: [[lemire-parsing-json]] reports 65.7 GB/s on 64 cores versus 2.13 GB/s on one core for the same lazy strategy.

## Counterevidence & Qualifications
The two introductory articles simplify their execution models. Wulc does not distinguish threads from processes in depth or discuss Python's GIL, while the GPU source uses an abstract “compute unit” and program-ID model without warps, thread blocks, synchronization, occupancy, memory coalescing, or real hardware measurements. Its one-query-per-program attention partition is pedagogical rather than a claim about an optimal production kernel. Lemire supplies a concrete CPU measurement, but it is a maintainer-authored best-of-seven result for one in-memory, selective parsing workload on one 64-core server; free-threaded availability, native-library work, memory bandwidth, allocation, callback cost, and workload balance limit generalization.

## What Changed
- Added a measured free-threaded Python case based on independent records, thread-local state, and final reduction.
- Qualified the roughly 31-fold 64-core gain by its parser, hardware, data-residency, and benchmark boundaries.
- Created the concept page from Wulc's multi-core parallel-programming overview.
- Expanded the concept from process-level CPU parallelism to ID-based GPU data partitioning.

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

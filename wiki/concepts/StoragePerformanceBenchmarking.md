---
title: "Storage Performance Benchmarking"
type: concept
tags: [storage, performance, benchmarking, nvme, observability]
sources:
  - the-quest-for-one-million-iops-benchmarking-storage-at-lancedb
  - task-failed-successfully-saturating-nic-and-disk-bandwidth
  - linker-io-tricks-and-their-downsides
  - slatedb-benchmark
last_updated: 2026-10-17
knowledge_schema: synthesis-v1
---

## Definition
[[StoragePerformanceBenchmarking]] is the design and measurement of tests that connect storage behavior to a representative application workload, cache state, concurrency level, data distribution, and physical-device result.

## Current Synthesis
A storage benchmark is decision-useful when it preserves the important structure of production work. For selective search, that means more than timing one random read: the test may need an index stage, batches of selected rows and columns, concurrent requests, decoding, post-processing, hot metadata, and both page-cached and uncached row data. Latency and throughput answer different questions because synchronization, CPU-cache contention, task scheduling, and queue depth emerge only under concurrency.

Measurement should also separate logical work from physical I/O. Repeated random selections can hit the same row, turning an assumed device operation into a kernel-page-cache hit. Larger datasets, explicit cache control, queue instrumentation, system counters, and device statistics help verify whether the intended bottleneck was actually exercised. End-to-end tests guide defaults and architecture, while microbenchmarks remain useful for regression and local profiling.

The LanceDB case adds an interaction lesson: replacing blocking calls with `io_uring` did not improve the old task-heavy scheduler, and simplifying that scheduler alone delivered only part of the eventual gain. The NVMe-to-RDMA case sharpens causal attribution: a wide flamegraph frame or real overhead is not necessarily the throughput wall. Registered files removed `fget` without changing throughput, more request splitting left throughput unchanged, and a computation-free buffer scan reproduced the CRC-enabled limit. Hugepages then changed both throughput and the directly implicated dTLB counters.

Together, the cases show that performance features compose through runtime, memory, kernel, and topology structure. A useful benchmark varies one suspected mechanism, includes negative controls, observes both output and internal state, and preserves distinctions between logical requests, physical device work, CPU computation, cache behavior, and virtual-address translation.

The linker case extends this discipline to filesystem identity and process lifetime. Repeatedly rewriting the same output selects a warm page-cache best case, while evicting the output reveals that in-place reuse may read every old block before overwriting it. A linker whose parent exits before its worker child finishes also changes the measurement boundary: ordinary wall time, CPU time, and RSS may describe the signaling parent rather than the work, while cgroup memory persists and the build admits another job. Benchmark configuration must therefore include publication semantics, cache residency, page size, memory fragmentation, process-tree tracking, and the point at which downstream resource use is considered complete.

The SlateDB case carries the method into cloud object storage. The measured system includes machine type, region, provider routing, object-store API pricing, cache fraction and fetch granularity, compaction policy, and whether one task couples reads with writes. A public results site improves inspectability, but comparability still depends on declaring that roughly 10%-cached remote SlateDB and fully local RocksDB are different systems. Diagnostic value can also justify holding back an optimization: disabling trivial moves preserves a baseline that continues to reveal general ingestion cost.

Performance evidence should close a loop into design. SlateDB's suite exposed routing instability, an avoidable persisted-polling bill, and large-partition tail latency; those observations led respectively to provider work, local in-memory coordination, and a redesigned cache boundary. This is stronger than publishing a leaderboard, though controlled before-and-after runs are still needed to attribute each improvement.

## Key Claims
- Benchmark workloads should represent the application operation and its full critical path, not only an isolated storage primitive.
- Cache state and granularity, working-set size, row duplication, batching, selected-data fraction, topology, and API cost can materially change what a test measures.
- Throughput under realistic concurrency can reveal synchronization, scheduling, queue-depth, and CPU-cache effects hidden by single-operation latency.
- Pipeline queues and system/device counters can localize bottlenecks and verify that reported logical operations reached physical storage.
- Runtime and kernel-I/O optimizations can be complementary rather than independently beneficial.
- Flamegraph prominence identifies candidates, but causal attribution requires a controlled intervention that changes throughput and a direct measurement tied to the proposed mechanism.
- A benchmark must preserve completion and identity semantics: warm inode reuse or an early-exiting parent can improve reported wall time by changing what is cached or counted.

## Evidence
- Workload fidelity: [[the-quest-for-one-million-iops-benchmarking-storage-at-lancedb]] turns vector search into 2,000 concurrent queries per second with 500 fetched rows per query rather than timing a single row read.
- Cache discipline: [[the-quest-for-one-million-iops-benchmarking-storage-at-lancedb]] tests cached and uncached row data while keeping normally hot metadata resident.
- Logical-versus-physical validation: [[the-quest-for-one-million-iops-benchmarking-storage-at-lancedb]] finds that repeated row IDs reduce an inferred million IOPS to about 600,000 measured IOPS on a one-million-row dataset.
- Bottleneck localization: [[the-quest-for-one-million-iops-benchmarking-storage-at-lancedb]] combines flame graphs with queue-size instrumentation to narrow the limiting stage to I/O scheduling.
- Optimization interaction: [[the-quest-for-one-million-iops-benchmarking-storage-at-lancedb]] reports 600 queries per second for the old scheduler with per-thread `io_uring` versus 3,800 for the new scheduler with the same I/O API.
- Negative controls: [[task-failed-successfully-saturating-nic-and-disk-bandwidth]] removes most `fget` overhead and separately increases each logical read from three to five block requests without materially changing aggregate throughput.
- Operation isolation: [[task-failed-successfully-saturating-nic-and-disk-bandwidth]] replaces CRC with a 64-byte-stride touch that reproduces the same throughput wall, separating memory traversal from checksum arithmetic.
- Direct counter evidence: [[task-failed-successfully-saturating-nic-and-disk-bandwidth]] reports more than 80 dTLB misses per GET for the slow scanning cases and about five with hugepages, while high L1D miss counts do not track low throughput.
- Scale and topology: [[task-failed-successfully-saturating-nic-and-disk-bandwidth]] compares a controlled single-NIC, single-worker setup with an eight-NIC, eight-NUMA-shard deployment before generalizing the bottleneck.
- Cache-state reversal: [[linker-io-tricks-and-their-downsides]] reports a warm 2 GiB in-place link faster than new-inode output, then a cold in-place link at 3.89 seconds versus 0.38 seconds because it reads the old file before overwriting it.
- Completion-boundary control: [[linker-io-tricks-and-their-downsides]] shows `wait4`-based time and RSS observing only an early-exiting parent while cgroup memory tracks the orphaned linking child, and uses `--no-fork` to restore comparable accounting.
- Memory-policy counterfactual: [[linker-io-tricks-and-their-downsides]] intercepts `MADV_HUGEPAGE` and compares VM counters, finding similar hugepage allocation but about 550 extra compaction stalls with the hint under `enabled=always`.
- Economic measurement: [[slatedb-benchmark]] adds object-store API cost and reports that replacing remote-style local polling reduced estimated idle cost from roughly US$40 to below US$5 per month.
- Tail diagnosis: [[slatedb-benchmark]] links repeated p99.9 spikes to small reads fetching 4 MiB object-cache partitions and distinguishes whole-database mirroring from smaller-unit partial caching.
- Baseline transparency: [[slatedb-benchmark]] states that SlateDB keeps roughly 10% of data cached over object storage while the RocksDB run keeps all data on local disk, and disables trivial moves to retain baseline ingestion behavior.

## Counterevidence & Qualifications
One benchmark cannot define a universal protocol. Cold startup, scans, writes, compaction, cloud object storage, network storage, tail latency, mixed tenants, failures, durability, cost, power, and recall may require different methods and metrics. All four cases are first-party and configuration-specific. LanceDB deliberately reduces vector-search recall; the NVMe-to-RDMA case uses a controlled direct-I/O read workload, fixed request sizes, NUMA-local devices, IOMMU passthrough, and one hardware/kernel configuration. The linker study uses one Linux 6.18 host, ext4 on SATA, selected synthetic and Chromium workloads, and an in-development mold port. SlateDB's comparison mixes remote object storage and 10% cache residency with fully local RocksDB, while its charts do not themselves provide controlled before-and-after evidence. These sources support diagnostic methods and interaction findings within their experiments, not broad product rankings.

## What Changed
- Added cloud topology, object-store API cost, cache-fetch granularity, and background coordination to benchmark controls.
- Distinguished a public diagnostic baseline from a benchmark configured to maximize the strongest headline number.
- Connected benchmark observations to compaction, coordination, and cache-design changes while retaining the need for controlled attribution.

## Related Concepts
- [[DatabaseEngineeringTradeoffs]] - storage measurements are meaningful only in the context of workload and system tradeoffs.
- [[LatencyHierarchy]] - client latency combines CPU, runtime, kernel, device, and sometimes network costs.
- [[ServiceObservability]] - profiles, queues, counters, and device statistics reveal the limiting stage.
- [[VectorDatabase]] - selective vector-search retrieval supplies the benchmark workload in the LanceDB case.
- [[ApproximateNearestNeighborSearch]] - recall and index-search work must be reported alongside storage throughput.
- [[HighThroughputIOOptimization]] - applies the benchmark's evidence to buffer registration, page size, and end-to-end device saturation.
- [[LinkerOptimizationTradeoffs]] - applies the method to output publication, asynchronous teardown, and hugepage requests.
- [[ObjectStorageNativeDatabase]] - makes remote latency, request pricing, caching, and maintenance placement part of the measured system.

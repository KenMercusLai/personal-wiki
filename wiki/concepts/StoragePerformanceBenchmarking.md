---
title: "Storage Performance Benchmarking"
type: concept
tags: [storage, performance, benchmarking, nvme, observability]
sources:
  - the-quest-for-one-million-iops-benchmarking-storage-at-lancedb
last_updated: 2026-10-02
knowledge_schema: synthesis-v1
---

## Definition
[[StoragePerformanceBenchmarking]] is the design and measurement of tests that connect storage behavior to a representative application workload, cache state, concurrency level, data distribution, and physical-device result.

## Current Synthesis
A storage benchmark is decision-useful when it preserves the important structure of production work. For selective search, that means more than timing one random read: the test may need an index stage, batches of selected rows and columns, concurrent requests, decoding, post-processing, hot metadata, and both page-cached and uncached row data. Latency and throughput answer different questions because synchronization, CPU-cache contention, task scheduling, and queue depth emerge only under concurrency.

Measurement should also separate logical work from physical I/O. Repeated random selections can hit the same row, turning an assumed device operation into a kernel-page-cache hit. Larger datasets, explicit cache control, queue instrumentation, system counters, and device statistics help verify whether the intended bottleneck was actually exercised. End-to-end tests guide defaults and architecture, while microbenchmarks remain useful for regression and local profiling.

The LanceDB case adds an interaction lesson: replacing blocking calls with `io_uring` did not improve the old task-heavy scheduler, and simplifying that scheduler alone delivered only part of the eventual gain. Performance features compose through runtime structure, so individual optimizations cannot be assumed additive.

## Key Claims
- Benchmark workloads should represent the application operation and its full critical path, not only an isolated storage primitive.
- Cache state, working-set size, row duplication, batching, and selected-data fraction can materially change what a test measures.
- Throughput under realistic concurrency can reveal synchronization, scheduling, queue-depth, and CPU-cache effects hidden by single-operation latency.
- Pipeline queues and system/device counters can localize bottlenecks and verify that reported logical operations reached physical storage.
- Runtime and kernel-I/O optimizations can be complementary rather than independently beneficial.

## Evidence
- Workload fidelity: [[the-quest-for-one-million-iops-benchmarking-storage-at-lancedb]] turns vector search into 2,000 concurrent queries per second with 500 fetched rows per query rather than timing a single row read.
- Cache discipline: [[the-quest-for-one-million-iops-benchmarking-storage-at-lancedb]] tests cached and uncached row data while keeping normally hot metadata resident.
- Logical-versus-physical validation: [[the-quest-for-one-million-iops-benchmarking-storage-at-lancedb]] finds that repeated row IDs reduce an inferred million IOPS to about 600,000 measured IOPS on a one-million-row dataset.
- Bottleneck localization: [[the-quest-for-one-million-iops-benchmarking-storage-at-lancedb]] combines flame graphs with queue-size instrumentation to narrow the limiting stage to I/O scheduling.
- Optimization interaction: [[the-quest-for-one-million-iops-benchmarking-storage-at-lancedb]] reports 600 queries per second for the old scheduler with per-thread `io_uring` versus 3,800 for the new scheduler with the same I/O API.

## Counterevidence & Qualifications
One benchmark cannot define a universal protocol. Cold startup, scans, writes, compaction, cloud object storage, network storage, tail latency, mixed tenants, failures, durability, cost, power, and recall may require different methods and metrics. The LanceDB evidence is first-party, configuration-specific, and deliberately reduces vector-search recall; it supports the methodology and interaction finding within that experiment, not a broad product ranking.

## What Changed
- Created the concept from LanceDB's end-to-end random-access and NVMe-saturation experiment.

## Related Concepts
- [[DatabaseEngineeringTradeoffs]] - storage measurements are meaningful only in the context of workload and system tradeoffs.
- [[LatencyHierarchy]] - client latency combines CPU, runtime, kernel, device, and sometimes network costs.
- [[ServiceObservability]] - profiles, queues, counters, and device statistics reveal the limiting stage.
- [[VectorDatabase]] - selective vector-search retrieval supplies the benchmark workload in the LanceDB case.
- [[ApproximateNearestNeighborSearch]] - recall and index-search work must be reported alongside storage throughput.

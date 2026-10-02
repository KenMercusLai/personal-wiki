---
title: "LanceDB"
type: entity
tags: [database, vector-search, storage, open-source]
sources:
  - the-quest-for-one-million-iops-benchmarking-storage-at-lancedb
last_updated: 2026-10-02
knowledge_schema: synthesis-v1
---

## Overview
[[LanceDB]] is represented as a vector database and storage project built around the Lance columnar format, with both embedded open-source and separated compute-storage deployment models.

## Current Profile
The source centers LanceDB's storage design on fast random row access after an index has selected candidate row identifiers. Lance caches index, table, and file metadata but leaves row caching to the operating system, while still supporting scan-oriented access when a query selects a material fraction of a table.

Its benchmark path divides work into CPU-bound search and scheduling, disk-bound reads, and CPU-bound decode and reranking. Profiling attributed poor scaling to small task boundaries and synchronization around blocking reads rather than to NVMe capacity alone. A lighter scheduler plus a per-thread `io_uring` runtime reportedly saturated three AWS local NVMe drives at roughly 1.5 million read operations per second.

This result is an engineering milestone rather than a general product-performance claim. The experiment intentionally lowered ANN search effort and recall, used three datasets and drives, and tested unmerged changes on one machine and workload. The enterprise architecture separately places index search on CPU-and-RAM-heavy compute nodes and row fetches on NVMe-heavy storage nodes so the two resources can scale independently.

## Key Characteristics
- Uses the Lance columnar format while targeting both selective row access and scan workloads.
- Treats index-selected row fetching and decoding as the storage half of vector search.
- Caches metadata in process memory while relying on the kernel page cache for row data.
- Uses pipeline, scheduler, and asynchronous-I/O design to drive high NVMe concurrency.
- Supports embedded operation and a separated compute-storage enterprise architecture.

## Evidence
- Workload role: [[the-quest-for-one-million-iops-benchmarking-storage-at-lancedb]] maps search from index-produced row identifiers through fetch, decode, and post-processing.
- Cache and scan policy: [[the-quest-for-one-million-iops-benchmarking-storage-at-lancedb]] distinguishes hot metadata, kernel-cached row data, uncached row data, and scan-and-discard above a source-reported roughly 1% selection threshold.
- Scheduler design: [[the-quest-for-one-million-iops-benchmarking-storage-at-lancedb]] traces blocking reads through Tokio task and queue boundaries and reports a large-server gain after reducing them.
- Measured result: [[the-quest-for-one-million-iops-benchmarking-storage-at-lancedb]] reports about 1.5 million IOPS and 3,800 queries per second with the revised scheduler and per-thread `io_uring` path.
- Deployment shape: [[the-quest-for-one-million-iops-benchmarking-storage-at-lancedb]] diagrams separate compute servers for index search and storage servers for row fetching.

## Qualifications
The evidence is one first-party benchmark without independent reproduction, released code-state verification, repeated-run variance, energy or cost analysis, or a matched database comparison. Its final vector-search configuration sacrifices recall by reducing `nprobes`, spreads requests across three datasets, and depends on local NVMe, a specific AWS instance, ten million 3-KiB vectors, and high concurrency. The source therefore supports a narrow storage-path capability, not a universal LanceDB performance ranking.

## What Changed
- Created the initial profile from LanceDB's million-IOPS engineering benchmark.

## Relationships
- [[VectorDatabase]] - LanceDB uses vector search as the end-to-end workload around selective row retrieval.
- [[StoragePerformanceBenchmarking]] - LanceDB's result depends on representative workload and physical-I/O measurement.
- [[DatabaseEngineeringTradeoffs]] - LanceDB balances random access, scans, caching, concurrency, CPU work, and recall.
- [[ApproximateNearestNeighborSearch]] - the benchmark lowers ANN search effort to isolate the storage path.
- [[AWS]] - an i8g.12xlarge supplies the cores and three local NVMe drives used in the final run.

---
title: "PostgreSQL Asynchronous I/O"
type: concept
tags: [postgresql, asynchronous-io, io-uring, sequential-scan, read-ahead]
sources:
  - pgsql08-05
last_updated: 2026-10-19
knowledge_schema: synthesis-v1
---

## Definition
[[PostgreSQLAsynchronousIO]] is PostgreSQL's read-side mechanism for submitting storage requests before they are immediately needed, combining contiguous blocks, tracking their target buffers, and overlapping I/O with executor work.

## Current Synthesis
PostgreSQL 18 applies asynchronous reads to page sequences used by sequential scans, bitmap heap scans, and vacuum, but not to index scans or writes in the described implementation. Linux can use `io_uring` submission and completion rings; other supported systems can use PostgreSQL `io_worker` processes that execute synchronous reads concurrently behind shared-memory queues. Both paths ultimately load requested pages into allocated buffer-pool slots and report completion to the backend.

For sequential scans, `ReadStream` joins buffer allocation, pinning, read-ahead, vectored I/O, and ordered consumption. Contiguous relation blocks can be one vectored request even when their destination slots are scattered through the buffer pool. The backend submits a future batch before finishing tuple processing on the current page, waits only when the next required buffer is still in progress, and then consumes completed pages in order.

The request shape follows cache state. The first cache hit ends the current accumulation of misses so one request never spans a noncontiguous hole. `combine_distance` starts at one, doubles on storage-reading rounds up to the configured and queue-size cap, holds during an initial warm run, and then decays one at a time after sufficiently many consecutive hits. Once it reaches one, sustained hits enter Fast Path and bypass stream-queue management; a miss immediately restores normal read-ahead.

The durable performance judgment is therefore conditional. AIO can expose NVMe parallelism, reduce syscall and completion overhead through vectored reads, and overlap storage work with tuple execution, but it has less to contribute as the buffer pool warms. Evaluation must distinguish cold from warm cache, supported scan types from index access, and submission mechanics from end-to-end query throughput.

## Key Claims
- PostgreSQL offers kernel-backed `io_uring` and process-backed `io_worker` implementations whose concurrency and coordination costs differ.
- `ReadStream` makes asynchronous reads usable by connecting future block numbers, pinned buffer slots, outstanding operations, and ordered consumption.
- Vectored I/O combines contiguous relation blocks into fewer requests and completion events while allowing scattered buffer-pool destinations.
- Sequential scans can overlap tuple processing on one page with storage reads for the next batch, unlike a page-by-page synchronous cycle.
- Cache hits terminate a combined request boundary; adaptive growth, slow decay, and Fast Path reduce unnecessary read-ahead and bookkeeping as residency changes.
- Performance claims are cache- and workload-sensitive: the source expects the largest gain for cold sequential reads and no direct gain for index scans or writes.

## Evidence
- Implementation alternatives: [[pgsql08-05]] diagrams kernel `io_uring` queues beside shared-memory queues and background `io_worker` processes.
- Request combining: [[pgsql08-05]] shows blocks zero through three loaded by one vectored request into four noncontiguous buffer slots.
- Pipeline overlap: [[pgsql08-05]] contrasts an asynchronous batch whose next read overlaps tuple work with the earlier serialized allocation-read-process cycle.
- Cache-aware boundaries: [[pgsql08-05]] shows a hit ending a two-block vectored request and consecutive hits producing one-block stream rounds.
- Adaptive control: [[pgsql08-05]] diagrams exponential growth to the configured cap, gradual decay after a queue-length warm run, and immediate renewed growth after a miss.
- Warm-cache bypass: [[pgsql08-05]] shows entry to Fast Path at a one-block window and return to normal mode on a miss.

## Counterevidence & Qualifications
The source is a technical explanation rather than an empirical evaluation. It does not quantify throughput, latency, CPU cost, fairness, device utilization, or the relative overhead of `io_uring`, `io_worker`, and synchronous mode. Its strongest architectural diagrams intentionally simplify page-cache, descriptor-locking, pin, error, cancellation, and partial-completion details. Version-specific configuration and implementation can change, and the chapter's PostgreSQL 19 worker controls extend beyond its PostgreSQL 18 baseline. AIO also cannot eliminate a wait when the next requested page has not completed; it creates opportunity for overlap rather than guaranteed acceleration.

## What Changed
- Established the two implementation paths and their distinct kernel-versus-worker coordination boundaries.
- Connected vectored reads and `ReadStream` to concrete buffer-pool placement and ordered scan consumption.
- Added the cache-hit, adaptive-window, and Fast Path mechanisms that bound overhead under warm-cache conditions.
- Narrowed the performance claim to supported read paths and cache-sensitive end-to-end measurements.

## Related Concepts
- [[PostgreSQLBufferManagement]] - provides the buffers, pins, cache hits, and replacement context used by asynchronous reads.
- [[PostgreSQLPageArchitecture]] - defines the page-sized relation blocks submitted and combined by the read path.
- [[StoragePerformanceBenchmarking]] - requires cache-state, physical-I/O, concurrency, and end-to-end measurements before attributing gains to AIO.
- [[DatabaseEngineeringTradeoffs]] - frames portability, worker overhead, kernel dependence, and workload fit as engineering choices.
- [[HighThroughputIOOptimization]] - shares the principle that an asynchronous API matters only within the complete scheduling, memory, and device pipeline.

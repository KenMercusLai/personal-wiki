---
title: "8.5. Asynchronous I/O in PostgreSQL"
type: source
tags: [postgresql, asynchronous-io, io-uring, buffer-management, sequential-scan]
date: 2026-10-19
source_file: /mnt/ken_personal_wiki/Articles/pgsql08-05.md
---

## Summary
[[HironobuSuzuki]] explains PostgreSQL 18's read-side asynchronous I/O through its `io_uring` and `io_worker` implementations, then traces how `ReadStream` combines read-ahead, vectored I/O, completion waits, and tuple processing during sequential scans. The chapter shows that [[PostgreSQLAsynchronousIO]] is adaptive rather than a fixed prefetch loop: cache hits bound contiguous requests, the combine window grows on misses and decays through warm runs, and a Fast Path bypasses stream bookkeeping for sustained hits. Its performance claim is deliberately narrow—benefits are strongest for cold, sequentially read workloads and diminish as buffer-cache hit rates rise.

## Key Claims
- Synchronous reads serialize application waiting and storage work, whereas asynchronous submission lets PostgreSQL overlap other backend work with several outstanding reads.

![Sequence comparison showing synchronous reads blocking an application one request at a time while asynchronous reads let it submit multiple requests, run other work, and later collect completions](../../wiki-assets/pgsql08-05/synchronous-versus-asynchronous-read.png)

- PostgreSQL 18 offers Linux `io_uring`, whose kernel-shared submission and completion rings can place data directly into buffer slots, and portable `io_worker` processes, which coordinate conventional reads through PostgreSQL shared-memory queues.

![PostgreSQL asynchronous I/O architectures comparing kernel io_uring submission and completion queues with shared-memory queues served by io_worker processes](../../wiki-assets/pgsql08-05/io-uring-versus-io-worker.png)

- Vectored I/O combines contiguous relation blocks into one request while scattering their results into distinct buffer-pool slots, reducing calls and completion events.

![One vectored read request loading contiguous relation blocks zero through three into noncontiguous PostgreSQL buffer-pool slots before a single completion event](../../wiki-assets/pgsql08-05/vectored-read-buffer-placement.png)

- `ReadStream` tracks pinned buffer identifiers in a circular FIFO array whose active window is abstracted as `stream_buffers`; enqueue and dequeue operations connect relation blocks, descriptors, and buffer-pool slots.

![ReadStream circular buffer array with queue size, oldest buffer index, and combine distance alongside its simplified stream_buffers representation](../../wiki-assets/pgsql08-05/readstream-buffer-array.png)

![ReadStream enqueue example mapping relation block two through buffer descriptor and buffer pool slot five into the circular buffers array and simplified stream_buffers queue](../../wiki-assets/pgsql08-05/readstream-enqueue.png)

![ReadStream dequeue example advancing oldest_buffer_index and reducing pinned_buffers as the leftmost element leaves the simplified stream_buffers queue](../../wiki-assets/pgsql08-05/readstream-dequeue.png)

- In a cold sequential scan, PostgreSQL submits the next contiguous batch before finishing tuple work on the current batch; it waits when the next dequeued page is still in progress, then consumes the completed pages without another wait.

![Asynchronous sequential-scan sequence showing read-ahead batches, completion waits, FIFO buffer consumption, and tuple processing overlapping the next storage read](../../wiki-assets/pgsql08-05/asynchronous-sequential-scan.png)

- Earlier synchronous sequential scans instead repeat allocation, blocking read, I/O termination, and tuple processing for every page, leaving no equivalent overlap.

![Traditional synchronous sequential-scan sequence in which each BufferAlloc and read completes before tuple processing and the next block begins](../../wiki-assets/pgsql08-05/synchronous-sequential-scan.png)

- A cache hit terminates the current read-ahead search so accumulated misses remain physically contiguous for one vectored request; later misses refill a batch, while consecutive hits are initially handled one at a time.

![Read-ahead stopping at an already cached block so only the preceding contiguous cache misses are submitted as one vectored read](../../wiki-assets/pgsql08-05/cache-hit-read-ahead.png)

![ReadStream behavior after a cache hit comparing refill with a contiguous storage batch against repeated one-block handling of consecutive cache hits](../../wiki-assets/pgsql08-05/post-cache-hit-stream-refill.png)

- `combine_distance` begins at one and doubles toward `min(io_combine_limit / BLCKSZ, queue_size - 1)` on storage reads; after more than `queue_size - 1` consecutive hits it decays one block at a time, and a miss resumes growth.

![Adaptive combine distance doubling from one to sixteen blocks across sequential-read rounds until reaching the configured maximum](../../wiki-assets/pgsql08-05/adaptive-combine-distance-growth.png)

![Adaptive combine distance remaining stable and then decaying during a long cached run before a cache miss switches it back to growth](../../wiki-assets/pgsql08-05/adaptive-combine-distance-decay.png)

- When the window reaches one during sustained cache hits, Fast Path reads buffer slots without `stream_buffers`; any cache miss returns the scan to normal read-ahead.

![ReadStream entering Fast Path after consecutive cache hits, returning to normal read-ahead on a miss, and staying in Fast Path for a fully cached relation](../../wiki-assets/pgsql08-05/fast-path-transitions.png)

- The implementation targets read-heavy sequential access such as sequential scans, bitmap heap scans, and vacuum; it does not provide asynchronous writes or accelerate index scans in the described release.

## Key Quotes
> "Its benefit is greatest when the buffer pool is cold." - the chapter's benchmark boundary.

> "A cache miss immediately triggers the increment mode." - on adaptive read-ahead recovery.

## Connections
- [[HironobuSuzuki]] - author of the PostgreSQL internals chapter.
- [[PostgreSQL]] - database whose version 18 buffer manager gains read-side asynchronous I/O.
- [[PostgreSQLAsynchronousIO]] - synthesis of the implementations, sequential-scan pipeline, and adaptive behavior.
- [[PostgreSQLBufferManagement]] - supplies the page residency, pinning, cache-hit, and buffer-slot substrate used by `ReadStream`.
- [[PostgreSQLPageArchitecture]] - supplies the default 8KB blocks combined into vectored reads.
- [[StoragePerformanceBenchmarking]] - provides the cache-state and workload discipline needed to evaluate the source's performance claims.

## Contradictions
- No direct contradiction was found. The source narrows generic AIO performance claims by excluding index scans and asynchronous writes and by warning that cold-cache-only benchmarks can overstate real-world benefit.
- The chapter is an implementation explanation, not a comparative benchmark. It supplies no throughput, latency, CPU, device, queue-depth, workload, or repeated-run measurements for `io_uring`, `io_worker`, or synchronous mode.
- Details are version-sensitive: PostgreSQL 18 is the implementation baseline, while the dynamic `io_worker` controls described for version 19 are prospective relative to that baseline.

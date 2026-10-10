---
title: "Introduction to Buffers in PostgreSQL"
type: source
tags: [postgresql, buffers, caching, wal, performance]
date: 2026-01-24
source_file: "/mnt/ken_personal_wiki/Articles/Introduction to Buffers in PostgreSQL.md"
---

## Summary
This article explains how [[PostgreSQL]] moves its default 8KB pages through shared buffers, chooses eviction candidates with pin and usage counts, and coordinates dirty-page writes with WAL, checkpoints, and the background writer. It connects [[PostgreSQLPageArchitecture]] to observable behavior in `pg_buffercache`, bulk-operation ring strategies, per-session temporary-table buffers, and the operating-system page cache. The walkthrough is a useful mental model, but several phrases blur implementation boundaries or turn rules of thumb into general rules.

## Key Claims
- [[PostgreSQLBufferManagement]] uses a shared-memory pool whose slots contain 8KB pages plus descriptors and a mapping table that locates a page without scanning the whole pool.
- Pin counts prevent active pages from being evicted, while bounded usage counts feed a clock-sweep policy that gives repeatedly accessed pages more chances to survive.
- Dirty pages can be flushed by checkpoints, the background writer, or an allocating backend; WAL durability ordering must prevent a data page from reaching durable storage before the WAL needed to recover it.
- `pg_buffercache` can reveal page identity, usage count, and dirty state, including pages dirtied by hint-bit updates during an otherwise read-only query.
- Large sequential scans, bulk writes, and VACUUM use bounded buffer-access rings to limit cache pollution, while temporary tables use per-backend local buffers controlled by `temp_buffers`.
- PostgreSQL shared buffers coexist with the operating-system page cache, whose retained clean pages and read-ahead can make a PostgreSQL buffer miss cheaper than physical storage I/O.
- `shared_buffers`, `temp_buffers`, and `effective_cache_size` have different semantics and memory scopes, so fixed percentages are starting heuristics rather than workload-independent settings.

## Key Quotes
> "The page remains the atomic unit of I/O." - the physical boundary underlying buffer operations.

> "The goal is keeping enough clean buffers available so backends never stall on synchronous writes during eviction." - the operational purpose assigned to background flushing.

## Connections
- [[PostgreSQL]] - database whose buffer, WAL, temporary-table, and OS-cache interactions the article explains.
- [[PostgreSQLBufferManagement]] - synthesis of shared-buffer lookup, eviction, dirty-page handling, bulk-access strategies, and cache tiers.
- [[PostgreSQLPageArchitecture]] - the 8KB page is both the slotted storage container and the unit moved through the buffer system.
- [[DatabaseEngineeringTradeoffs]] - cache sizing, double buffering, bulk isolation, and backend memory require workload-specific choices.
- [[BackupAndRecovery]] - WAL-before-data durability ordering and checkpoints make buffered writes recoverable.
- [[SelfHostedDatabaseOperations]] - buffer and per-connection memory settings belong to an operator-owned tuning and capacity model.
- [[StoragePerformanceBenchmarking]] - `pg_buffercache` and `EXPLAIN (ANALYZE, BUFFERS)` expose different parts of page residency and query I/O behavior.

## Contradictions
- The article calls sequential-scan and bulk-operation rings "small, private buffer pools" whose pages never touch the main cache. PostgreSQL buffer-access strategies instead restrict reuse to a small ring of slots within shared buffers; they protect most of the pool without bypassing it.
- `Buffers: shared read=...` means blocks were read into PostgreSQL shared buffers. It does not distinguish physical disk reads from pages served by the operating-system cache, so `EXPLAIN (ANALYZE, BUFFERS)` alone does not report exact disk-versus-OS-cache counts.
- The sentence "This parameter allocates no memory" follows a `shared_buffers` example but describes `effective_cache_size`. `shared_buffers` reserves the database shared-buffer pool at server start; `effective_cache_size` is the non-allocating planner estimate.
- WAL must be flushed before a corresponding dirty data page is written to durable storage, but the claim that every modification is WAL-logged before the in-memory page is dirtied is an oversimplified description of the internal critical-section sequence.
- The mapping hash table offers expected constant-time lookup, not a strict worst-case guarantee independent of collision and concurrency behavior. Similarly, a 25%-of-RAM `shared_buffers` value is a common starting heuristic, not a universal optimum.

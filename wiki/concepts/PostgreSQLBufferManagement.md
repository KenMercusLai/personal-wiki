---
title: "PostgreSQL Buffer Management"
type: concept
tags: [postgresql, buffers, caching, wal, performance]
sources:
  - introduction-to-buffers-in-postgresql
last_updated: 2026-10-10
knowledge_schema: synthesis-v1
---

## Definition
[[PostgreSQLBufferManagement]] is the system that maps PostgreSQL's disk-backed pages into shared or local memory, protects pages in active use, chooses reusable slots, and coordinates dirty-page persistence with WAL and the operating system.

## Current Synthesis
PostgreSQL normally performs storage I/O in page-sized units. For ordinary tables and indexes, backends share a pool sized by `shared_buffers`; each slot combines page bytes with descriptor state, while a mapping hash table locates the slot for a relation, fork, and block. A hit avoids loading the page into the PostgreSQL cache again, whereas a miss may still be served from the operating-system page cache rather than physical storage.

Replacement separates immediate safety from longer-term value. A pin prevents eviction while a backend actively uses a buffer. A bounded usage count records repeated access, and the clock sweep skips pinned buffers, ages positive counts, and reuses an unpinned zero-count slot. Bulk-access strategies constrain scans, bulk writes, and VACUUM to repeatedly reuse a small ring of shared-buffer slots so one pass does not displace most hot data. Temporary tables are different: their pages use per-backend local buffers because cross-process coordination is unnecessary.

Writes add a durability constraint. Modified buffers can remain dirty in memory and absorb repeated changes, but WAL required for recovery must become durable before the corresponding data page. Checkpoints, the background writer, and allocating backends provide different write paths; the performance objective is to maintain reusable clean buffers without violating recovery ordering. Because PostgreSQL and the kernel both cache pages, tuning must consider shared buffers, OS cache, per-backend memory, workload concurrency, storage behavior, and planner estimates together.

## Key Claims
- Shared buffers cache ordinary table and index pages across backends, with descriptors and a mapping structure separating page content, state, and lookup.
- Pin counts protect actively referenced buffers, while bounded usage counts and a clock sweep approximate recency without maintaining a lock-heavy exact LRU list.
- Dirty-buffer throughput depends on coordinated checkpoint, background-writer, and backend writes under WAL-before-data durability ordering.
- Bulk-access rings limit destructive cache churn by reusing a bounded subset of shared-buffer slots; they are strategies within the shared pool, not independent private caches.
- Local buffers isolate temporary-table pages per backend, while the OS page cache forms a second cache tier beneath PostgreSQL.
- Buffer observations require careful semantics: a PostgreSQL cache miss or `shared read` does not by itself prove physical disk I/O.

## Evidence
- Shared-pool structure: [[introduction-to-buffers-in-postgresql]] describes 8KB buffer blocks, per-slot descriptors, buffer tags and state, and a mapping hash table from page identity to slot.
- Replacement state: [[introduction-to-buffers-in-postgresql]] explains pins, usage counts capped at five, and the clock sweep's skip, decrement, and reuse decisions.
- Dirty-page paths: [[introduction-to-buffers-in-postgresql]] distinguishes checkpoint writes, background-writer cleaning, and synchronous backend writes when allocation selects a dirty victim.
- Observable lifecycle: [[introduction-to-buffers-in-postgresql]] uses `pg_buffercache` to show dirty inserted pages, clean cached pages after `CHECKPOINT`, hint-bit dirties after a `SELECT`, eviction under pressure, and clean reloads at usage count one.
- Specialized access: [[introduction-to-buffers-in-postgresql]] describes bounded strategies for large sequential scans, bulk writes, and VACUUM, plus per-session local buffers for temporary tables.
- Cache hierarchy: [[introduction-to-buffers-in-postgresql]] explains double buffering, kernel retention of clean evictions, read-ahead, and the planner-only role of `effective_cache_size`.

## Counterevidence & Qualifications
The article is a practitioner explanation and demonstration rather than a version-spanning implementation specification or comparative benchmark. Several details are version- and configuration-sensitive, including access-strategy thresholds and sizes, WAL segment size, defaults, and VACUUM controls. Hash lookup is expected rather than guaranteed constant time, the background writer's behavior is more selective than a general dirty-buffer scanner, and absence of WAL for temporary relations reduces logging work without guaranteeing low physical I/O. Its 25%-of-RAM guidance is a starting heuristic; large-memory systems, workload concurrency, operating-system behavior, huge pages, and per-backend allocations can change the balance. Most importantly, ring strategies still operate on shared-buffer slots, and PostgreSQL buffer counters cannot alone separate kernel-cache hits from storage reads.

## What Changed
- Established buffer management as the link between 8KB page storage, shared-memory residency, replacement, and durability.
- Distinguished pins from usage counts and bounded bulk-access rings from separate caches.
- Added the OS page cache and local temporary buffers as separate memory scopes.
- Preserved observability limits and version-sensitive tuning boundaries.

## Related Concepts
- [[PostgreSQLPageArchitecture]] - supplies the page-sized storage unit moved through the buffer system.
- [[BackupAndRecovery]] - depends on WAL durability ordering and checkpoint progress before dirty pages become recoverable on disk.
- [[DatabaseEngineeringTradeoffs]] - frames memory allocation, cache duplication, concurrency, and I/O as workload-dependent choices.
- [[SelfHostedDatabaseOperations]] - owns buffer sizing, per-connection memory, monitoring, and recovery configuration in self-managed deployments.
- [[StoragePerformanceBenchmarking]] - provides the measurement context needed to interpret buffer hits, reads, dirties, and writes.
- [[DatabaseOverloadProtection]] - reduces query, connection, and retry pressure that can otherwise amplify buffer churn and backend stalls.

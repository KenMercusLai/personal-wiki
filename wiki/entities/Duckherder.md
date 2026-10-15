---
title: "Duckherder"
type: entity
tags: [duckdb, distributed-query, analytics, arrow-flight]
sources:
  - duckdb-on-object-storage
last_updated: 2026-10-15
knowledge_schema: synthesis-v1
---

## Overview
[[Duckherder]] is a distributed DuckDB execution extension that uses one driver and multiple read-only workers over a shared [[DuckDBObjectStorage]] database.

## Current Profile
The driver plans queries, partitions work into row-group tasks, sends those tasks to workers over Arrow Flight, and merges partial results. It is the only writer; workers attach the same bucket-backed database read-only, removing data-copying and shard-rebalancing steps when capacity changes. The article demonstrates a four-worker partial `GROUP BY` whose local plan is reduced to a `DISTRIBUTED_SCAN` followed by final ordering.

The storage layer gives each worker committed-state reads, but the article says query-level snapshot pinning is still next work. Without it, readers do not observe half-written states, yet independently refreshing workers are not guaranteed to use exactly the same committed version for a distributed query.

## Key Characteristics
- Separates a planning and merge driver from read-only execution workers.
- Uses Arrow Flight to dispatch partitioned tasks and return partial results.
- Shares one object-backed DuckDB database rather than copying or sharding data per worker.
- Keeps the driver as the only writer and workers as non-fencing readers.
- Can distribute row-group partial aggregation and merge results at the driver.
- Has not yet guaranteed one pinned committed snapshot across every worker in a query.

## Evidence
Execution topology:
- [[duckdb-on-object-storage]] diagrams a client, a single-writer driver, multiple read-only workers, and one shared bucket.

Demonstrated query:
- [[duckdb-on-object-storage]] shows four registered workers, a distributed `GROUP BY`, a `DISTRIBUTED_SCAN` plan, and execution statistics reporting four generated tasks across four workers.

Consistency boundary:
- [[duckdb-on-object-storage]] states that per-query snapshot pinning across workers is future work, alongside an optional strong refresh mode.

## Qualifications
The source provides an illustrative query and architecture rather than comparative distributed-query benchmarks. It does not quantify scheduling overhead, skew, shuffle behavior, fault recovery, retries, partial-result correctness, network cost, elasticity time, concurrent queries, security, or scale beyond four workers. Committed-state reads prevent torn versions but do not yet prove all workers use one identical snapshot.

## What Changed
- Established Duckherder's driver, worker, Arrow Flight, and shared-storage execution model.
- Added the demonstrated four-worker row-group aggregation path.
- Recorded cross-worker snapshot pinning as an unresolved correctness boundary.

## Relationships
- [[DuckDBObjectStorage]] - shared storage prerequisite for worker access without copying or rebalancing data.
- [[DuckDB]] - query engine and database semantics distributed by the extension.
- [[SlateDB]] - provides committed manifest states to the driver and readers through the storage extension.
- [[ObjectStorageNativeDatabase]] - shared native database enables disposable read-only compute workers.
- [[DatabaseEngineeringTradeoffs]] - distributed speed, consistency, coordination, failure handling, and operations remain coupled.

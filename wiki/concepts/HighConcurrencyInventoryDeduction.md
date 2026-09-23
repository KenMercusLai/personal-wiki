---
title: "High-Concurrency Inventory Deduction"
type: concept
tags: [ecommerce, inventory, distributed-systems, consistency]
sources:
  - kikcat-dian-shang-xi-tong-de-gao-bing-fa-ku-cun-kou-jian
last_updated: 2026-09-23
knowledge_schema: synthesis-v1
---

## Definition
[[HighConcurrencyInventoryDeduction]] is the problem of accepting many simultaneous purchase attempts while preventing or bounding stock from being sold above or below the durable available quantity across order, inventory, cache, and database boundaries.

## Current Synthesis
The source compares four design families. A conditional database update is atomic and strongly grounded in durable state, but a hot SKU turns the exclusive row lock into a serial queue whose waiters consume latency and connections. Redis distributed locks move admission control away from the database, but global locks suppress unrelated work, SKU locks still serialize the hottest item, and multi-SKU orders enlarge deadlock and atomic-commit complexity.

The proposed high-throughput alternative makes Redis the synchronous stock snapshot and converts replenishments and order items into replayable stock events. This removes the relational database from the latency-critical deduction path, but correctness then depends on idempotent consumers, snapshot freshness gates, durable failure reporting, coordinator-led recovery, and reconciliation. A single Redis node can fail closed more strictly at the cost of availability; Sentinel improves failover but permits split-brain windows that epoch checks, majority observation, replica-health requirements, freshness deadlines, and delayed recovery can only reduce.

AliSQL Inventory Hint represents a fourth path: shorten the database transaction inside a specialized engine. It preserves stronger database-centered consistency for a narrow update, but immediate commit or rollback complicates multi-SKU transactions and introduces cloud-vendor dependence.

## Key Claims
- Conditional database updates can preserve stock non-negativity, but hot-row serialization makes the transaction's lock-hold time the throughput ceiling.
- Redis locks protect the database from a request surge without removing hot-SKU serialization or multi-SKU coordination complexity.
- Event-driven in-memory deduction trades immediate cross-service atomicity for low latency plus delayed, replayable reconciliation.
- A Redis snapshot is safe to use only while its freshness and failover generation are trusted; otherwise the business path must reject writes.
- Sentinel split brain, long process pauses, and clock anomalies leave residual overselling risk even with epoch and timeout fencing.
- Underselling and lost updates require durable local reporting when possible and heavier periodic reconciliation when that reporting itself is lost.
- No approach maximizes consistency, availability, throughput, simplicity, and portability simultaneously.

## Evidence
- Database and lock contention: [[kikcat-dian-shang-xi-tong-de-gao-bing-fa-ku-cun-kou-jian]] traces exclusive-row locking, connection exhaustion, lock granularity, and multi-SKU deadlock risk.
- Event path: [[kikcat-dian-shang-xi-tong-de-gao-bing-fa-ku-cun-kou-jian]] shows replenishment and order events feeding stock consumers, the goods database, and the Redis snapshot.
- Fail-closed controls: [[kikcat-dian-shang-xi-tong-de-gao-bing-fa-ku-cun-kou-jian]] uses `is_stale`, Sentinel configuration epochs, majority Sentinel queries, replica-health limits, and Lua rejection checks.
- Residual failure windows: [[kikcat-dian-shang-xi-tong-de-gao-bing-fa-ku-cun-kou-jian]] describes network partitions, long GC pauses, swapping, container throttling, short timeout windows, and clock rollback.
- Recovery and underselling: [[kikcat-dian-shang-xi-tong-de-gao-bing-fa-ku-cun-kou-jian]] requires draining unsynced order items and stock events before rebuilding Redis, plus local-ledger or periodic reconciliation for failed orders.
- Database-engine alternative: [[kikcat-dian-shang-xi-tong-de-gao-bing-fa-ku-cun-kou-jian]] describes AliSQL Inventory Hint's immediate commit or rollback and its multi-statement and portability limits.

## Counterevidence & Qualifications
This is one practitioner's architecture proposal rather than an independent benchmark or formal safety proof. The claim of roughly ten thousand to tens of thousands of TPS is not reproduced, the AliSQL mechanism is partly inferred from limited public detail, and the proposed Sentinel design explicitly leaves overselling windows. The best design depends on workload shape: a single-item flash sale, ordinary multi-item checkout, strict no-oversell requirement, and high-availability requirement do not justify the same tradeoff.

## What Changed
- Created a cross-approach synthesis of database, Redis-lock, event-driven memory, and AliSQL inventory deduction.
- Made fail-closed recovery and residual split-brain risk part of the concept rather than implementation footnotes.

## Related Concepts
- [[EventDrivenConsistency]] - reconciles Redis-side deductions with durable goods state through replayable stock events.
- [[TwoPhaseCommit]] - offers stronger cross-resource atomicity with latency and coordination costs the source avoids.
- [[SystemReliability]] - supplies circuit breaking, recovery, reconciliation, and capacity-protection concerns.
- [[DatabaseTransactionIsolation]] - row locking and transaction duration shape contention in the database-centered approach.
- [[DistributedSystemRestraint]] - the source demonstrates the operational complexity incurred when throughput and availability force distribution.

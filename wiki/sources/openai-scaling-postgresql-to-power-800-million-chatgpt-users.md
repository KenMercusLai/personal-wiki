---
title: "Scaling PostgreSQL to power 800 million ChatGPT users"
type: source
tags: [postgresql, databases, scaling, reliability, openai]
date: 2026-01-23
source_file: "/mnt/ken_personal_wiki/Articles/OpenAI - Scaling PostgreSQL to power 800 million ChatGPT users.md"
---

## Summary
[[OpenAI]] describes keeping a single unsharded [[PostgreSQL]] primary for ChatGPT and API workloads while scaling read traffic across nearly 50 geographically distributed replicas. The case combines workload separation, query and write reduction, connection pooling, cache-miss coalescing, tier isolation, rate limiting, load shedding, high availability, and cautious schema operations; it also draws a firm boundary around write-heavy work, which is being moved to sharded systems rather than forced through one PostgreSQL writer.

## Key Claims
- PostgreSQL can support millions of queries per second for a read-heavy global workload when most reads leave the primary, replicas remain close to clients, and the writer retains capacity for unavoidable transactions and spikes.
- A single-primary design does not scale writes horizontally: PostgreSQL MVCC can amplify heavy updates through new row versions, dead-tuple scans, index maintenance, bloat, and autovacuum work, so shardable write-heavy workloads belong in sharded systems.
- [[DatabaseOverloadProtection]] requires layered controls: efficient SQL, workload isolation, connection pooling, cache-miss coalescing, rate limits, sane retry intervals, query-digest blocking, and deliberate load shedding.
- PgBouncer transaction or statement pooling reduced the reported average connection setup time from 50 ms to 5 ms and helped stay within Azure PostgreSQL's 5,000-connection instance limit.
- Cache locking and leasing make one requester refill a missing key while concurrent requesters wait, preventing a cache failure from multiplying identical database reads.
- High availability reduces but does not remove the single-writer risk: a hot standby can take over, read replicas preserve read-only service during writer failure, and multiple replicas per region retain headroom for a replica loss.
- Direct WAL streaming from one primary to nearly 50 replicas creates a fan-out ceiling; cascading replication could support more replicas but adds failover complexity and was still under test.
- Operational constraints are part of the architecture: avoid pathological ORM-generated joins, terminate idle transactions, enforce a five-second schema-change timeout, use concurrent index operations, and rate-limit backfills even when they take more than a week.

## Key Quotes
> "PostgreSQL can be scaled to reliably support much larger read-heavy workloads than many previously thought possible." - the article's central workload-qualified conclusion.

> "We also no longer allow adding new tables to the current PostgreSQL deployment." - the boundary that directs new workloads toward sharded systems.

## Connections
- [[OpenAI]] - operator reporting the production architecture and its incident-driven evolution.
- [[PostgreSQL]] - unsharded relational system whose primary serves all remaining writes.
- [[PostgreSQLReadScaling]] - architecture combining one writer, regional read replicas, locality, headroom, and prospective cascading replication.
- [[DatabaseOverloadProtection]] - layered protection against expensive queries, connection storms, cache misses, retries, and traffic spikes.
- [[SystemReliability]] - the case treats capacity, failure isolation, failover, overload behavior, and safe change as one system.
- [[DynamicContentCaching]] - cache locking prevents concurrent misses for one key from becoming redundant database reads.
- [[DatabaseEngineeringTradeoffs]] - read scaling, MVCC write costs, sharding complexity, replica lag, and failover are workload-specific tradeoffs.
- [[ChatGPT]] - major product whose read-heavy workload is served by the PostgreSQL deployment.

## Contradictions
- No direct contradiction was found. The case qualifies PostgreSQL-first consolidation: one mature database can have substantial read-scaling runway, but OpenAI deliberately moves shardable write-heavy workloads elsewhere and forbids new tables in the legacy deployment.
- The performance, availability, user-count, incident, and latency figures are first-party production claims without workload traces or independent audit. The saved date is used as the source-note date because the supplied Markdown does not state a separate publication date.
- Cascading replication is a planned, tested direction in the source rather than a deployed result, and read availability during primary failure does not preserve write operations or guarantee every request can complete.

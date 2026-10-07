---
title: "Aurora DSQL"
type: entity
tags: [aws, database, postgresql, serverless, microvm]
sources:
  - seven-years-of-firecracker-marcs-blog
last_updated: 2026-10-07
knowledge_schema: synthesis-v1
---

## Overview
[[AuroraDSQL]] is an [[AWS]] serverless relational database with PostgreSQL compatibility, represented here through its isolated query-processor and bounded-lifetime architecture.

## Current Profile
Each active transaction runs in a PostgreSQL-derived query processor inside its own [[Firecracker]] environment. A query processor can be reused for the same database but serves only one transaction at a time. Database-specific prepared snapshots make processors fast to create, clean memory pages can be shared across clones, and fixed VM and transaction lifetimes allow the surrounding system to simplify memory reclamation and MVCC garbage collection because connection handling, caching, and concurrency control live outside the processor.

## Key Characteristics
- Routes active transactions to isolated PostgreSQL-derived query processors.
- Restricts each query processor to one transaction at a time.
- Reuses processors only within the same DSQL database.
- Restores prepared VM snapshots rather than booting and initializing every processor from scratch.
- Shares unchanged clean pages across clones while preserving private dirty pages.
- Uses bounded processor and transaction lifetimes to simplify reclamation.

## Evidence
- Processing topology: [[seven-years-of-firecracker-marcs-blog]] describes and diagrams a transaction/session router distributing work to multiple query processors in separate Firecracker instances.
- One-transaction boundary: [[seven-years-of-firecracker-marcs-blog]] says query processors may be reused for one database but handle only one transaction at a time.
- Clone startup: [[seven-years-of-firecracker-marcs-blog]] describes booting Linux and PostgreSQL, customizing the database, snapshotting the result, and restoring clones for new processors.
- Memory density: [[seven-years-of-firecracker-marcs-blog]] separates per-VM dirty pages from shared clean memory- and disk-backed pages.
- Lifetime simplification: [[seven-years-of-firecracker-marcs-blog]] says DSQL retires VMs on a timer and limits transactions to five minutes, enabling age-based cleanup.

## Qualifications
The page reflects one first-party architectural essay rather than complete service documentation or measured evaluation. The source does not quantify startup time beyond an order-of-magnitude claim, memory and cache savings, service cost, transaction throughput, compatibility gaps, clone failure modes, or security properties. Snapshot restoration also needs extra mechanisms to re-establish unique state such as randomness.

## What Changed
- Created the entity page for Aurora DSQL's microVM-backed query-processing model.

## Relationships
- [[AWS]] - provider of Aurora DSQL.
- [[Firecracker]] - isolates and rapidly instantiates query processors.
- [[VMSnapshotCloning]] - restores initialized database processors and shares clean pages.
- [[BoundedLifetimeSimplification]] - uses maximum lifetimes to simplify page and version reclamation.
- [[DatabaseTransactionIsolation]] - related database correctness concern, distinct from the per-processor execution boundary described here.
- [[ServerlessComputing]] - Aurora DSQL creates and retires managed compute behind a database interface.

---
title: "Bigtable"
type: entity
tags: [database, distributed-systems, wide-column, google]
sources:
  - bigtable-er-shi-nian-jia-gou-de-bu-bian-yu-bian
last_updated: 2026-10-08
knowledge_schema: synthesis-v1
---

## Overview
[[Bigtable]] is Google's distributed non-relational database, presented here as a twenty-year production system whose durable tablet, metadata, and storage separation survived large growth while its replication, computation, maintenance, integrity, and resource-management layers evolved around that skeleton.

## Current Profile
Bigtable stores tablet data in Colossus rather than on tablet-server local disks, so scheduling can move responsibility without copying durable state. Metadata lives in Bigtable itself, with Chubby retaining only bootstrap location information. The source credits these early choices with making tablets movable and later work independently scalable.

New capabilities mostly avoid coordinating the foreground write path. Pull-based eventual replication, CRDT changelogs, materialized-view pipelines, full-file validation, file garbage collection, compaction, offline reads, and bulk import reuse logical clocks, watermarks, LSM compaction, metadata tables, and external jobs. Operational evolution adds domain-aware autosizing, adaptive caches and Bloom filters, black-box probes, and centralized SRE ownership. The retained boundary is equally important: transactions remain single-row, so applications must colocate atomic state or redesign their logic.

## Key Characteristics
- Separates Colossus-resident durable data from movable tablet-serving compute.
- Uses asynchronous pull replication without cross-replica mutation admission coordination.
- Extends an LSM-based core with SQL, change streams, CRDT counters, and materialized views.
- Offloads parallelizable stateless work while retaining metadata ownership in the stateful service.
- Applies checksums and full SSTable rereads as layered integrity defenses.
- Treats workload-aware elasticity, cache efficiency, probes, and SRE ownership as architecture.
- Preserves single-row transactional semantics despite two decades of feature growth.

## Evidence
- Stable state boundary: [[bigtable-er-shi-nian-jia-gou-de-bu-bian-yu-bian]] describes Colossus-backed tablets, self-hosted metadata, and Chubby bootstrap state.
- Replication and convergence: [[bigtable-er-shi-nian-jia-gou-de-bu-bian-yu-bian]] reports destination-pulled eventual replication, progress watermarks, dummy mutations, replication-aware version GC, and CRDT compaction handling.
- Computation and offload: [[bigtable-er-shi-nian-jia-gou-de-bu-bian-yu-bian]] connects row-key-aware SQL, CDC, counters, materialized views, external compaction, offline reads, and bulk SSTable construction to existing extension points.
- Integrity and operations: [[bigtable-er-shi-nian-jia-gou-de-bu-bian-yu-bian]] reports layered CRC checks, full SSTable validation, two-level autoscaling, adaptive cache and Bloom-filter decisions, metadata and latency probes, and centralized SRE operation.
- Persistent constraint: [[bigtable-er-shi-nian-jia-gou-de-bu-bian-yu-bian]] says atomic transactions remain limited to one row and that oversized rows can become a performance problem.

## Qualifications
This profile is grounded in one Chinese practitioner summary of Google's 2026 retrospective rather than a complete protocol specification or independent production audit. Reported scale, near-elimination of observed SSTable inconsistency, common replication lag, and resource-efficiency outcomes are source claims without reproduced measurements here. Eventual replication is explicitly best effort, and the source does not define full failure, conflict, security, or availability guarantees for every feature.

## What Changed
- Established Bigtable as a stable-core architecture that evolved through asynchronous attachment points and offloaded work.
- Added the interaction risks among replication, garbage collection, CRDT deletion, compaction, and watermarks.
- Added workload-aware resource control, integrity validation, and specialized SRE operation to the product profile.
- Preserved the single-row transaction boundary as a long-lived application-level cost.

## Relationships
- [[Google]] - develops and operates Bigtable as an internal and cloud database service.
- [[StorageArchitectureEvolvability]] - Bigtable supplies the principal long-lived architecture case.
- [[DatabaseEngineeringTradeoffs]] - Bigtable couples consistency, latency, throughput, operability, resource cost, and data modeling.
- [[ReplicatedLog]] - provides a contrasting coordinated-order model to Bigtable's asynchronous replica convergence.
- [[GreptimeDB]] - compared by the source on separated storage, replicas, compaction, and derived computation.

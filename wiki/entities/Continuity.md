---
title: "Continuity"
type: entity
tags: [git, storage, distributed-systems, cursor]
sources:
  - ren-yi-gui-mo-de-git
last_updated: 2026-10-09
knowledge_schema: synthesis-v1
---

## Overview
[[Continuity]] is Cursor's Git storage system, built around an object-store write-ahead log as durable authority and ordinary local Git repositories as disposable high-performance caches.

## Current Profile
Continuity accepts a push by writing its packfile as a WAL entry to S3-compatible object storage, preparing the local Git reference transaction, and publishing an index pointer with atomic compare-and-swap. The source says this ordering makes acknowledged pushes durable and concurrent updates linearizable without coordinating a quorum of local repository replicas.

Each server can restore a repository from the WAL, so placement is an efficiency decision rather than durable state. Rendezvous hashing gives clients a stable preferred-node order; UDP gossip lets replicas catch up optimistically; and a conditional read against the WAL index verifies freshness before a replica serves fetch or clone. Repacking runs only on the primary and its output is propagated through the WAL.

This makes replication elastic: hot repositories may have many local copies, cold repositories one or none, while the object-store log remains authoritative. Cursor reports synthetic linear read scaling through 100 replicas and high push rates, but has not supplied a public implementation or reproducible evaluation in this source.

## Key Characteristics
- Treats an S3-compatible write-ahead log, not local repository disks, as the durable source of truth.
- Stores acknowledged pushes durably before exposing their reference updates.
- Uses atomic compare-and-swap on the WAL index to serialize concurrent repository updates.
- Keeps ordinary Git repositories on local NVMe as rebuildable caches for native Git performance.
- Combines rendezvous hashing, opportunistic gossip, and mandatory read-time freshness validation.
- Propagates primary-produced repacks through the WAL so follower replicas spend bandwidth instead of repeating compression CPU work.
- Allows replica count to range from zero for idle repositories to many copies for read-heavy repositories.

## Evidence
- Durable and visible push ordering: [[ren-yi-gui-mo-de-git]] describes uploading a WAL entry, preparing the local reference transaction, and then publishing its index pointer.
- Coordination model: [[ren-yi-gui-mo-de-git]] says S3 compare-and-swap makes any server safe to use as primary while rendezvous hashing reduces avoidable conflicts.
- Replica correctness: [[ren-yi-gui-mo-de-git]] describes gossip-assisted catch-up followed by an ETag-based conditional S3 read before fetch or clone.
- Cache model: [[ren-yi-gui-mo-de-git]] says absent repositories can be restored from the WAL and idle local copies garbage-collected.
- Compaction: [[ren-yi-gui-mo-de-git]] says only the primary repacks and followers download the resulting compressed pack through the WAL.
- Scale claims: [[ren-yi-gui-mo-de-git]] reports synthetic tests with 100 replicas and claimed push rates of 120 per second on standard S3 and more than 300 on S3 Express One Zone.

## Qualifications
Continuity is documented here only through Cursor's product-launch engineering article. The source gives no reproducible workload, code, cost model, complete protocol, formal proof, latency distribution, multi-region behavior, object-store outage analysis, or independent comparison. “No consensus” means no consensus protocol among local Git replicas in the described design; the system instead relies on the consistency, durability, conditional operations, and availability of its external object store. A locally stale replica may also need to catch up before serving a read, so local copies are not synchronously identical at all moments.

## What Changed
- Created the entity profile for Cursor's WAL-backed Git storage system.

## Relationships
- [[Cursor]] - company that developed and operates Continuity.
- [[Origin]] - Git platform whose storage layer is Continuity.
- [[GitHostingArchitecture]] - Continuity is the source's WAL-first alternative to replicated local repositories.
- [[ReplicatedLog]] - related durable-history pattern with a different authority and coordination model.
- [[GitHub]] - Spokes provides the principal architecture against which Continuity is compared.
- [[DistributedConsensus]] - Continuity replaces quorum coordination among repository copies with atomic updates to shared durable storage.

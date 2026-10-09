---
title: "任意规模的 Git"
type: source
tags: [git, distributed-systems, storage, replication, consistency]
date: 2026-08-18
source_file: "/mnt/ken_personal_wiki/Articles/任意规模的 Git.md"
---

## Summary
This Cursor engineering article explains why Git's local-first packfile and object-graph design makes large-scale centralized hosting difficult, then compares object-level storage, distributed filesystems, GitHub's Spokes architecture, and Cursor's [[Continuity]] system. It presents [[GitHostingArchitecture]] as a tradeoff among native-Git performance, strict consistency, durable authority, replica elasticity, and operational complexity, culminating in an S3-backed write-ahead log whose local Git repositories are disposable NVMe caches. The design and performance figures are first-party claims rather than independent benchmarks.

## Key Claims
- Git stores and transports objects through packfiles whose compression, delta chains, and layout suit local disks and efficient clones but create random-access and network-round-trip problems when repositories are distributed at object, file, or block level.
- GitHub's Spokes keeps ordinary Git repositories on local NVMe, replicates packfiles, and uses three-phase commit on reference transactions so a push becomes visible consistently across replicas; reads can then use any replica.
- Spokes' fixed replicated-repository model becomes expensive at both extremes: more replicas worsen push tail latency, while three always-current replicas are wasteful for millions of cold or ephemeral repositories.
- [[Continuity]] records each push in an S3-compatible write-ahead log, publishes it through an atomically updated index only after the local reference transaction is prepared, and uses compare-and-swap to linearize concurrent updates.
- Local repositories are derived caches rather than the source of truth: rendezvous hashing suggests placement, missing repositories are restored from the log, UDP gossip accelerates catch-up, and a conditional S3 read verifies freshness before every replica serves a read.
- Only the primary performs Git repacking; the compressed result enters the log so followers trade network bandwidth for repeated CPU work, while idle repositories can lose every local replica without losing durable state.
- Cursor reports linear read scaling in synthetic tests up to 100 replicas, sustained push throughput up to 120 pushes per second on standard S3 and above 300 on S3 Express One Zone, but supplies no independent benchmark, workload specification, failure test, cost analysis, or public implementation.

## Key Quotes
> "在推送完全持久化之前，我们绝不会确认该推送。" - on the durability boundary for accepting a push.

> "该系统旨在降级时始终保持正确，在健康时始终保持快速。" - on the design priority joining correctness with optimistic acceleration.

## Connections
- [[GitHostingArchitecture]] - compares the storage and coordination strategies available to centralized Git hosts.
- [[Continuity]] - Cursor's WAL-first Git storage system described in the article.
- [[Origin]] - Cursor platform built on Continuity for Git protocol, web, API, and agent access.
- [[Cursor]] - company presenting the new architecture and its internal operational motivation.
- [[GitHub]] - source of the Rails-plus-file-server history and the Spokes replication architecture used as the main comparison.
- [[ReplicatedLog]] - related ordered-log pattern, though Continuity places durable authority in an object-store WAL and uses CAS rather than consensus among repository replicas.
- [[DistributedConsensus]] - the source contrasts Spokes' coordinated replica commit with Continuity's shared durable authority and atomic object-store updates.

## Contradictions
- The article calls Spokes' three-phase commit a consensus algorithm and describes Continuity as having “no consensus.” More precisely, the account contrasts per-repository replica coordination with synchronization through a strongly consistent external object store and atomic compare-and-swap; correctness still depends on S3's stated semantics and availability.
- The claim that every replica is “completely consistent” includes a read-time freshness check and possible catch-up. It does not mean every local disk is synchronously current at every instant.
- The performance, simplicity, and operational claims come from Cursor, which is introducing [[Origin]]. The article does not publish reproducible methods, latency distributions, repository shapes, costs, correlated-failure results, recovery-time measurements, or an independent comparison with Spokes or Azure DevOps.
- No effective image reference exists in the supplied Markdown. Interactive-demo remnants such as voting labels, playback speed, replica count, latency, and dropped-datagram text do not provide inspectable visual evidence, so no assets were retained.

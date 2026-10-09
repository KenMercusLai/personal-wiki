---
title: "Git Hosting Architecture"
type: concept
tags: [git, distributed-systems, storage, consistency]
sources:
  - ren-yi-gui-mo-de-git
last_updated: 2026-10-09
knowledge_schema: synthesis-v1
---

## Definition
[[GitHostingArchitecture]] is the storage, coordination, replication, routing, and recovery design used to serve centralized Git operations while preserving Git's packfile protocol and repository semantics.

## Current Synthesis
Git's distributed client model does not make centralized hosting operationally simple. Git objects form a content-addressed DAG, but traversals discover the next key only after reading the current object. Storing each object independently in a remote key-value service can therefore turn graph walks into serial network round trips. Packfiles reduce transfer and disk size through compression and delta chains, but their logical object order and physical layout diverge, making Git's random access hostile to distributed file or block storage.

The durable pattern in the source is to preserve ordinary Git repositories on local NVMe for execution and packfile production while moving coordination or authority above them. GitHub's Spokes makes several local repositories jointly authoritative: it distributes packfiles, prepares reference transactions, and commits reference updates across a quorum so any replica can serve a current read. This gives native performance and strict visibility but makes replica placement, health, repair, and quorum membership operationally important; increasing replica count also increases coordinated-write tail latency.

Cursor's [[Continuity]] instead makes an object-store WAL authoritative and treats local repositories as derived caches. Atomic index updates serialize pushes; rendezvous hashing optimizes placement without making it correctness-critical; gossip speeds replication; and read-time object-store validation closes gaps left by missed gossip. This separates durability from active replica count, allowing hot repositories to fan out and cold repositories to have no local copy, at the cost of depending on object-store semantics and sometimes restoring or catching up before reads.

## Key Claims
- Git's content-addressed DAG permits direct lookup but still imposes sequential pointer discovery during history and tree traversal.
- Packfile compression and delta layout create random physical reads that make naive distributed filesystems and block replication poor fits for active Git workloads.
- Keeping native repositories on local NVMe preserves upstream Git compatibility, fast graph traversal, and efficient client-facing packfile generation.
- Synchronously coordinated repository replicas provide current reads but bind write latency and availability to replica health and quorum behavior.
- A durable shared WAL can make local repositories replaceable caches and decouple availability from a fixed replica floor.
- Correctness can combine authoritative atomic updates, optimistic replication, and mandatory read-time freshness checks rather than requiring every acceleration path to be reliable.
- Replication and repacking must be designed together because each push creates packfiles whose accumulation eventually harms lookup performance.

## Evidence
- Object and file-distribution limits: [[ren-yi-gui-mo-de-git]] connects DAG pointer chasing, packfile delta chains, and random reads to failures of DHT, NFS, GFS, and DRBD approaches.
- Native-repository advantage: [[ren-yi-gui-mo-de-git]] says both Spokes and Continuity retain ordinary Git repositories on local NVMe to reuse Git behavior and optimizations.
- Coordinated-replica model: [[ren-yi-gui-mo-de-git]] describes Spokes fan-out of packfiles followed by three-phase commit of reference transactions.
- WAL-authority model: [[ren-yi-gui-mo-de-git]] describes Continuity's durable push objects, CAS-updated index, rebuildable caches, and read freshness checks.
- Elasticity and maintenance: [[ren-yi-gui-mo-de-git]] says replica count can vary with demand and that repacking results flow through the WAL instead of consuming CPU independently on every replica.

## Counterevidence & Qualifications
The comparison is written by Cursor while launching [[Origin]], so its account of Spokes' limits and Continuity's advantages is interested and incomplete. The source does not supply reproducible benchmarks, full protocol details, costs, security boundaries, object-store failure behavior, multi-region semantics, or independent operational evidence. Its rejection of object-level Git storage rests partly on an older JGit DHT attempt and should not prove that every future disaggregated design must fail. The phrase “no consensus” also does not remove coordination assumptions; it relocates serialization and durable authority into an external store with atomic conditional operations.

## What Changed
- Created the concept to compare native-repository replication with object-store-WAL authority for hosted Git.

## Related Concepts
- [[ReplicatedLog]] - ordered durable history can coordinate derived replicas, although authority and consensus placement vary.
- [[DistributedConsensus]] - Spokes coordinates visibility across repository copies while Continuity delegates serialization to object-store CAS.
- [[DataDurability]] - acknowledged pushes must survive loss or replacement of local repository caches.
- [[SystemReliability]] - hosting design must preserve reads, writes, repair, and recovery through machine and storage failures.
- [[StorageArchitectureEvolvability]] - separating durable authority from serving caches changes how storage can scale and be replaced.
- [[DistributedSystemRestraint]] - Git hosting shows why distribution should follow concrete traversal, consistency, capacity, and recovery needs.

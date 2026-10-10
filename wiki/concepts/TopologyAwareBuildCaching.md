---
title: "Topology-Aware Build Caching"
type: concept
tags: [continuous-integration, caching, scheduling, storage]
sources:
  - so-you-want-to-build-your-own-datacenter
last_updated: 2026-10-10
knowledge_schema: synthesis-v1
---

## Definition
[[TopologyAwareBuildCaching]] is a CI scheduling and storage pattern that tracks where cache revisions already exist, places ephemeral work near a suitable copy, and attaches snapshot state just in time instead of transferring a full cache archive for every job.

## Current Synthesis
Traditional remote CI caching wraps useful work in a five-stage data path: download an archive, expand it, run the job, repack the result, and upload it. Namespace's Cache Volumes collapse the illustrated job path to snapshot-backed environment creation, job execution, and completion. The scheduler chooses a node holding the relevant revision, while the storage layer makes that local state attachable to an isolated ephemeral job.

The gain comes from co-design rather than caching alone. Scheduler metadata, snapshot semantics, node-local storage, image management, and [[DataCenterNetworkFabric|network topology]] must agree about location and availability. The source does not describe the consistency or recovery protocol, so locality should be treated as an optimization under explicit durability and cold-miss behavior, not as proof that network transfer disappears from every job.

## Key Claims
- Archive-based remote caching can add download, extraction, compression, and upload latency around the actual build.
- Tracking cache revision location lets a scheduler prefer a node that already holds reusable state.
- Just-in-time snapshots can preserve ephemeral job isolation while avoiding a full archive materialization path.
- Cache locality requires coordination across scheduling, storage, images, and the network rather than a standalone cache client.
- Cold misses, invalidation, replication, eviction, durability, isolation, and scheduler failure remain necessary design boundaries.

## Evidence
- Traditional path: [[so-you-want-to-build-your-own-datacenter]] and its retained diagram show environment creation followed by cache download, expansion, work, packing, upload, and completion.
- Local snapshot path: [[so-you-want-to-build-your-own-datacenter]] and its second diagram show snapshot-backed environment creation feeding a shorter start, work, and finish loop.
- Placement mechanism: [[so-you-want-to-build-your-own-datacenter]] says the scheduler records which nodes hold each cache revision and routes arriving jobs accordingly.
- Integration requirement: [[so-you-want-to-build-your-own-datacenter]] attributes the design to ownership of the scheduler, storage layer, and image-management layer.

## Counterevidence & Qualifications
The source gives no cache-hit rate, latency distribution, data volume, benchmark, comparison baseline, or correctness model. It does not specify snapshot granularity, copy-on-write behavior, invalidation, concurrent writers, revision selection, replication, eviction, encryption, tenant isolation, durability, cold placement, or recovery when a node or scheduler fails. The diagrams compare conceptual steps rather than measured elapsed time, and cache-aware placement can conflict with queue time, CPU availability, affinity, fault-domain spread, or fairness. The pattern therefore needs workload-specific evidence and a defined miss and failure path.

## What Changed
- Established node-local snapshot placement as an alternative to per-job cache archive transfer.
- Made scheduler, storage, image, and network co-design part of the caching boundary.
- Preserved consistency, cold-miss, durability, and scheduling-conflict questions as unresolved.

## Related Concepts
- [[BuildOptimizedInfrastructure]] - provides the local NVMe, fast compute, and vertically integrated control plane that make the pattern useful.
- [[DataCenterNetworkFabric]] - exposes path capacity and topology when cached state or images must still move.
- [[DynamicContentCaching]] - shares locality and reuse goals but applies to serving dynamic application responses rather than ephemeral builds.
- [[GitHostingArchitecture]] - likewise uses local NVMe copies for fast work while separating placement and durable authority concerns.
- [[SystemReliability]] - requires explicit miss, degradation, recovery, and observability behavior for the cache path.

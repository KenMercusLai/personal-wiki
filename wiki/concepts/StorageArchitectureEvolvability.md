---
title: "Storage Architecture Evolvability"
type: concept
tags: [databases, distributed-systems, architecture, operability]
sources:
  - bigtable-er-shi-nian-jia-gou-de-bu-bian-yu-bian
last_updated: 2026-10-08
knowledge_schema: synthesis-v1
---

## Definition
[[StorageArchitectureEvolvability]] is a storage system's ability to add capabilities, scale work, and strengthen correctness through stable state boundaries and reusable extension mechanisms without repeatedly redesigning its critical foreground paths.

## Current Synthesis
The Bigtable retrospective suggests three mutually reinforcing properties. First, durable state should be movable independently of serving compute, making the scheduling unit cheap to reassign. Second, asynchronous work needs explicit homes—replication pullers, compaction, logical clocks, watermarks, metadata tables, and external jobs—so new computation and validation can attach without lengthening foreground writes. Third, work that need not own core state should be parallelized or offloaded so its resources and failures can be governed separately.

This is not a claim that background processing removes complexity. It relocates coordination and creates composition risks: replication changes garbage-collection safety, deletion breaks the commutativity of counters, delayed work needs watermarks and recovery state, and best-effort tasks need priorities and limits. Nor does a stable skeleton guarantee flexible semantics. Bigtable's single-row transaction boundary illustrates how an early invariant can remain operationally valuable while transferring lasting costs to applications.

## Key Claims
- Separating durable state from serving compute makes partitions movable and enables later scheduling and offload choices.
- Reusable asynchronous mechanisms let new features avoid destabilizing latency-sensitive foreground writes.
- Stateless, independently scalable work should move out of state-owning services when ownership boundaries remain explicit.
- Cross-feature composition must be checked because individually valid background mechanisms can violate one another's assumptions.
- Workload-aware resource control, integrity validation, probing, and specialized operations are part of evolvability rather than afterthoughts.
- Stable architectural constraints can preserve reliability while imposing durable limitations on users.

## Evidence
- Movable state: [[bigtable-er-shi-nian-jia-gou-de-bu-bian-yu-bian]] links Colossus-backed tablets to balancing, autoscaling, external compaction, and offline access.
- Reusable background paths: [[bigtable-er-shi-nian-jia-gou-de-bu-bian-yu-bian]] shows replication, CRDT counters, materialized views, validation, and GC attaching to pullers, compaction, clocks, watermarks, and metadata.
- Composition risk: [[bigtable-er-shi-nian-jia-gou-de-bu-bian-yu-bian]] shows asynchronous replication interacting with version GC and deletion interacting with counter operation order.
- Operability: [[bigtable-er-shi-nian-jia-gou-de-bu-bian-yu-bian]] connects autosizing, cache control, hotspot movement, adaptive Bloom filters, probes, and SRE ownership to long-run operation.
- Persistent boundary: [[bigtable-er-shi-nian-jia-gou-de-bu-bian-yu-bian]] presents single-row transactions as both an unchanged design choice and an application burden.

## Counterevidence & Qualifications
The concept is induced from one unusually long-lived system described by its operator and a secondary commentator. It does not establish that all storage engines should use remote durable storage, eventual replication, LSM compaction, one control-plane shape, or the same offload boundary. Network cost, workload locality, stronger transaction requirements, compliance, staffing, and failure models can justify different designs. Architectural continuity may also conceal accumulated user workarounds or deferred semantic limitations.

## What Changed
- Established movable durable state, reusable asynchronous mechanisms, and explicit offload boundaries as the concept's core.
- Added cross-feature composition and recovery state as the principal cost of moving work off foreground paths.
- Added operational ownership and persistent semantic constraints to the evolvability test.

## Related Concepts
- [[DatabaseEngineeringTradeoffs]] - evolvability couples correctness, latency, coordination, cost, and application burden over time.
- [[SystemReliability]] - extension points must preserve recovery and integrity across failures and feature interactions.
- [[ReplicatedLog]] - offers a contrasting coordination mechanism based on one agreed order.
- [[ServiceObservability]] - probes and domain signals make evolved behavior measurable and operable.
- [[Bigtable]] - supplies the motivating twenty-year architecture case.

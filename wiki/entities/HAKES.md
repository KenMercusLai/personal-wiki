---
title: "HAKES"
type: entity
tags: [vector-database, distributed-systems, vector-search]
sources:
  - p3049-ooi
last_updated: 2026-10-15
knowledge_schema: synthesis-v1
---

## Overview
[[HAKES]] is a distributed [[VectorDatabase]] that separates compressed candidate filtering from full-vector refinement to scale high-recall search and online updates independently.

## Current Profile
HAKES serves [[HAKESIndex]] through replicated IndexWorkers that hold a compressed global filter index and RefineWorkers that shard the original vectors. A client sends a query to one IndexWorker, dispatches returned candidates to the relevant RefineWorkers, and merges their exact-score results. Inserts write the full vector to its refine shard, compute one compressed representation, and broadcast that lightweight index update; deletions use tombstones until compaction.

This architecture targets high-dimensional, concurrent read-write workloads where graph-index construction, neighborhood locking, and fan-out across many independently indexed shards become expensive. Filter compute and full-vector memory can be provisioned separately, but the evaluated system does not provide strong consistency.

## Key Characteristics
- Replicates a compact global filter-stage index while sharding full-precision vectors.
- Scales compute-heavy IndexWorkers independently from memory-heavy RefineWorkers.
- Uses [[HAKESIndex]] to make inserts append-oriented rather than graph-rewiring operations.
- Supports ID-based or IVF-assignment-based full-vector sharding.
- Uses checkpointing plus post-checkpoint reinsertion for recovery and offers session rather than strong consistency.
- Reports near-linear one-to-eight-node read scaling and leading concurrent-workload throughput in the paper's setup.

## Evidence
Architecture and workflow:
- [[p3049-ooi]] describes query fan-out from one IndexWorker to relevant RefineWorkers, independent worker scaling, update broadcast, tombstone deletion, and checkpoint recovery.

Performance:
- [[p3049-ooi]] reports near-linear read scaling on DPR-768-10m and E5-1024-10m and up to 16× higher throughput than three distributed vector database baselines.
- [[p3049-ooi]] reports HAKES ahead of HAKES-Base, isolating benefit from learned compression and search optimizations within the same architecture.

## Qualifications
The evidence is a first-party research prototype comparison rather than an independent production study. Systems differ in implementation language, maturity, feature surface, shard behavior, and deployment stack; HAKES omits strong consistency and does not evaluate multi-tenancy, authorization, encrypted transport, long-duration drift, or operational total cost. A compressed global index still grows with the dataset and must itself be sharded once it exceeds one server.

## What Changed
- Created the entity profile from the HAKES paper.
- Recorded the filter/refine worker boundary, write path, scaling result, and consistency limit.

## Relationships
- [[HAKESIndex]] - supplies HAKES's compressed filter and full-vector refine search path.
- [[VectorDatabase]] - is the system category HAKES implements.
- [[ApproximateNearestNeighborSearch]] - is the retrieval workload HAKES serves.
- [[HNSWIndex]] - is the graph-index architecture HAKES contrasts with partitioned and replicated filtering.
- [[RetrievalAugmentedGeneration]] - is a motivating application for mutable vector retrieval.

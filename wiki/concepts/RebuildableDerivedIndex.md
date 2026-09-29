---
title: "Rebuildable Derived Index"
type: concept
tags: [databases, search, indexing, data-architecture]
sources:
  - image-stacks-and-iphone-racks-building-an-internet-scale-meme-search-engine
last_updated: 2026-09-29
knowledge_schema: synthesis-v1
---

## Definition
[[RebuildableDerivedIndex]] is a data architecture in which an optimized retrieval store is treated as a reproducible projection of canonical records, so the index may be deleted and regenerated without becoming a second authoritative database.

## Current Synthesis
In the [[FindThatMeme]] architecture, [[PostgreSQL]] owns meme text and structured context while PGSync mirrors selected columns through Redis into a single-node Elasticsearch cluster. Search requests benefit from Elasticsearch's full-text capabilities, but corrections and durable state remain in PostgreSQL. If the search node loses data, the operator can discard it and repopulate it rather than reconcile two independent truths.

This separation changes the reliability decision. A single search node still causes query downtime during failure and rebuild, yet canonical data loss is bounded by PostgreSQL's durability rather than Elasticsearch replication. The pattern works only if projection rules, deletion behavior, ordering, replay, monitoring, schema changes, and rebuild duration are controlled; “rebuildable” is an operational property that must be demonstrated, not merely an architectural label.

## Key Claims
- Canonical data and retrieval-optimized data can have different stores without becoming equal sources of truth.
- Automated change projection reduces manual drift between the transactional record and search index.
- Disposable indexes make lower-redundancy search infrastructure more tolerable when temporary search downtime is acceptable.
- Rebuild safety depends on reproducible projection logic and a canonical store that retains every field needed by the index.
- Index loss and index staleness are different failure modes and require monitoring, reconciliation, and tested recovery.
- Rebuild time, load on the canonical database, and schema compatibility determine whether the recovery promise is practical.

## Evidence
- Canonical boundary: [[image-stacks-and-iphone-racks-building-an-internet-scale-meme-search-engine]] identifies PostgreSQL as the source of truth for meme text and structured metadata.
- Automated projection: [[image-stacks-and-iphone-racks-building-an-internet-scale-meme-search-engine]] uses PGSync with Redis to synchronize selected PostgreSQL columns into Elasticsearch.
- Replaceability: [[image-stacks-and-iphone-racks-building-an-internet-scale-meme-search-engine]] says Elasticsearch could be removed and rebuilt from PostgreSQL after data loss.
- Cost and reliability tradeoff: [[image-stacks-and-iphone-racks-building-an-internet-scale-meme-search-engine]] runs Elasticsearch as a one-node cluster to save resources while explicitly accepting reduced failure resilience.
- Workload fit: [[image-stacks-and-iphone-racks-building-an-internet-scale-meme-search-engine]] reports about 17 million meme records searchable on a shared six-core, 16 GB RAM instance.

## Counterevidence & Qualifications
The source does not report rebuild duration, write lag, reconciliation checks, delete propagation, backfill load, schema migration behavior, Redis durability requirements, or failure drills. A rebuildable index can still serve stale, missing, duplicated, or unauthorized results before a failure is noticed, and reconstruction can overload the canonical database or exceed an acceptable recovery window. A single node remains inappropriate where search continuity is critical. The pattern also does not justify storing search-only facts outside the canonical model if those facts cannot be deterministically reproduced.

## What Changed
- Created the concept from FindThatMeme's PostgreSQL, PGSync, Redis, and Elasticsearch boundary.
- Separated canonical durability from search availability and made rebuild validation part of the concept.

## Related Concepts
- [[DatabaseConsolidation]] - the canonical database retains authority even when a specialized search store is added.
- [[MicroserviceDataBoundaries]] - ownership remains explicit across systems with different query responsibilities.
- [[SystemReliability]] - reconstruction is a recovery path, while availability during reconstruction remains a separate requirement.
- [[DataBackupAndRecovery]] - canonical backup protects source records; index rebuild restores a derived serving surface.
- [[CostConstrainedInfrastructure]] - reconstructable state can justify a cheaper single-node deployment.
- [[ServiceObservability]] - lag, projection failures, stale documents, and rebuild progress must be visible.

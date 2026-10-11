---
title: "USearch"
type: entity
tags: [vector-search, database, hnsw, open-source]
sources:
  - combinatorial-stable-marriages-for-dbms-semantic-joins
last_updated: 2026-10-11
knowledge_schema: synthesis-v1
---

## Overview
[[USearch]] is an open-source vector-search library represented in the source as an HNSW-based engine with a stable-matching-inspired join operation.

## Current Profile
The article extends USearch from nearest-neighbor lookup to pairing records across two vector indexes. Rather than storing complete preferences, the implementation queries candidates as proposals are needed, tracks availability with a fixed-capacity ring, and uses concurrent bitsets for synchronization. A `max_proposals` parameter bounds work; zero asks the library to estimate a stopping point, while the reported experiments fix it at 100 to reduce variance.

The source reports more than 500,000 queries per second for small cache-resident collections and roughly 1,000 per second at billion-entry scale, but supplies no full benchmark method for those headline rates. It also reports that int8 text embeddings preserve join accuracy while improving construction and search/join speed threefold in the tested workload.

## Key Characteristics
- Implements [[HNSWIndex|HNSW]] approximate nearest-neighbor search.
- Adds a two-index join that dynamically retrieves preferences for a bounded proposal process.
- Exposes exactness and maximum-proposal controls that affect cost and completeness.
- Targets compact vector representations and multiple JIT distance-function paths.

## Evidence
- Join API: [[combinatorial-stable-marriages-for-dbms-semantic-joins]] shows `men.join(women, max_proposals=0, exact=False)` and describes automatic stopping estimation.
- Concurrency design: [[combinatorial-stable-marriages-for-dbms-semantic-joins]] mentions a fixed-capacity availability ring and multiple concurrent bitsets.
- Scaling profile: [[combinatorial-stable-marriages-for-dbms-semantic-joins]] contrasts cache-resident throughput with billion-entry throughput.
- Quantized workload: [[combinatorial-stable-marriages-for-dbms-semantic-joins]] reports nearly unchanged text-join metrics and a threefold speed improvement after downcasting E5 embeddings from float32 to int8.

## Qualifications
All implementation and performance evidence comes from the project's author. The article does not provide sufficient hardware, index-parameter, recall, build-cost, concurrency, or measurement detail to reproduce the broad throughput figures, and bounded approximate proposals do not imply the same guarantee as exact stable matching over complete preference lists.

## What Changed
- Established USearch's semantic-join interface, bounded proposal mechanism, and reported scaling limits.

## Relationships
- [[Unum]] - organizational context for the library.
- [[AshVardanian]] - author and implementer describing the library.
- [[HNSWIndex]] - approximate graph index used by USearch.
- [[ApproximateNearestNeighborSearch]] - retrieval method used to generate join candidates.
- [[SemanticJoin]] - join operation implemented over two indexes.
- [[StableMatching]] - algorithmic model generalized by the join.

---
title: "psql_bm25s"
type: entity
tags: [postgresql, search, bm25, open-source]
sources:
  - psql-bm25s
last_updated: 2026-10-22
knowledge_schema: synthesis-v1
---

## Overview
[[PsqlBm25s]] is an open-source PostgreSQL index access method from Intelligent Internet for exact BM25-family lexical retrieval over mutable tables.

## Current Profile
The extension is positioned as a small retrieval primitive rather than an agent runtime, reranker, or memory-policy engine. It offers id- and token-based SQL APIs, multi-field evidence, ordinary SQL composition, mutable maintenance, WAL recovery, and physical-replication compatibility so application data, agent artifacts, and imported corpora can share one retrieval surface.

Its base-plus-delta design directs foreground changes to a small append-only delta and periodically folds them into an optimized base. Realtime reads combine or wait for pending maintenance to return committed results; eventual reads favor latency while accepting brief ranking staleness.

The authors report roughly four times the Python bm25s median query throughput across 15 BEIR datasets and much larger advantages over two PostgreSQL alternatives. Those figures describe one first-party benchmark configuration, not independently verified relevance, operational safety, or total cost.

## Key Characteristics
- Implements exact BM25-family retrieval as a PostgreSQL access method.
- Exposes lexical candidates through SQL so filters, joins, permissions, recency, and vector search can compose in-database.
- Maintains mutable indexes through an optimized base plus a write-oriented delta.
- Offers realtime and eventual read modes with different freshness and latency behavior.
- Targets WAL, crash-recovery, and physical-replication compatibility.
- Uses precomputed sparse scores to trade additional construction work for repeated query throughput.

## Evidence
Architecture and composition:
- [[psql-bm25s]] describes id- and token-based query APIs, field-aware evidence, PostgreSQL access-method integration, and SQL-native hybrid composition.

Mutable operation:
- [[psql-bm25s]] shows writes, updates, and tombstones entering a delta that background maintenance folds into a replacement base.

Performance:
- [[psql-bm25s]] reports 3.97x and 3.93x suite-median QPS versus Python bm25s for the ids and text-array paths across 15 BEIR datasets.

Operational intent:
- [[psql-bm25s]] states that the index participates in WAL, recovery, and physical replication and that each optimization had to preserve those constraints.

## Qualifications
The available evidence is a first-party product article. It does not provide relevance metrics, statistical uncertainty, tail latency, storage or memory use, update throughput, delta-fold cost, concurrency behavior, resource-normalized comparisons, failure-injection results, or independent reproduction. Its benchmark therefore supports a configuration-specific query-throughput claim, not universal superiority or production correctness.

## What Changed
- Established psql_bm25s as a PostgreSQL-native mutable BM25 access method.
- Recorded its base-plus-delta maintenance and selectable freshness modes.
- Bounded its reported speedups to the authors' PG18 BEIR benchmark.

## Relationships
- [[PostgreSQL]] - host database, SQL composition layer, recovery system, and replication substrate.
- [[BM25]] - lexical ranking family implemented by the access method.
- [[BaseDeltaIndexMaintenance]] - update and background-fold architecture used by the extension.
- [[HybridSearch]] - vector and lexical candidates can be combined through SQL.
- [[RetrievalBudgeting]] - lower query cost is the motivating agent-system effect.
- [[HarnessEngineering]] - validation-heavy optimization loop used during development.

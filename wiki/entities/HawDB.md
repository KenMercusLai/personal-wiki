---
title: "HawDB"
type: entity
tags: [embedded-database, graph-database, vector-search, multimodal-data]
sources:
  - vane-data-hawdb-video-comparison
last_updated: 2026-10-24
knowledge_schema: synthesis-v1
---

## Overview
[[HawDB]] is a Rust-written embedded multimodal database presented as combining Cypher graph queries, transactional reads and writes, and optional text/vector search without a separately deployed database service.

## Current Profile
In the multi-video comparison proof of concept, HawDB stores authors, videos, processing runs, transcript evidence, frame-recognition records, timestamps, content hashes, and provenance relationships. The application selects completed `Run` versions and reads all relevant evidence in one transaction, allowing a saved comparison to recover the source snapshot used when the result was generated even after later reprocessing.

When semantic search is enabled, application-generated FastEmbed vectors, text blocks, and source metadata are written to a HawDB index. HawDB executes vector similarity and metadata filtering, while the application handles chunking, index lifecycle, keyword/vector score combination, candidate grouping, and evidence reconstruction.

## Key Characteristics
- Embeds locally rather than requiring a separate database service in the described proof of concept.
- Represents author-to-video-to-processing-run provenance with graph relationships queried through Cypher.
- Provides transactional reads so paginated evidence and its source relationships come from one consistent database view.
- Stores original evidence separately from version-specific search documents, allowing search indexes to be rebuilt.
- Supports optional vector similarity with metadata filters alongside graph and property queries.
- Leaves processing-version policy, chunking, ranking fusion, cache rules, and application validation outside the database.

## Evidence
- Provenance graph: [[vane-data-hawdb-video-comparison]] queries `Author`–`PUBLISHED`–`Video`–`PROCESSED`–`Run` relationships before reading evidence by `run_id`.
- Consistent reconstruction: [[vane-data-hawdb-video-comparison]] reads selected-run evidence in one transaction and saves the source versions with each comparison result.
- Optional retrieval: [[vane-data-hawdb-video-comparison]] stores text, FastEmbed vectors, and evidence/video/run metadata and demonstrates vector search filtered by `video_id`.
- Responsibility boundary: [[vane-data-hawdb-video-comparison]] assigns chunk formation, hybrid ranking, input-budget selection, index rebuilding, and citation binding to the application.

## Qualifications
The source is a project-authored proof of concept, not an independent database evaluation. It supplies no durability, crash-recovery, concurrency, scaling, latency, index-quality, storage-cost, or comparative benchmark results. The displayed code omits import, deployment, error, retention, and operational details; optional vector-search code is illustrative and was not necessarily enabled for the reported comparison. Transactional consistency does not by itself define how long runs are retained or whether model-derived fields are accurate.

## What Changed
- Created a source-bounded profile of HawDB's graph, versioned-evidence, transactional-read, and optional vector-search roles.

## Relationships
- [[VaneData]] - supplies frame reading and structured multimodal model calls in the joint proof of concept.
- [[TraceableMultiSourceComparison]] - HawDB preserves the versioned evidence and relationships required for replayable comparisons.
- [[RetrievalAugmentedGeneration]] - optional vector, metadata, and raw-evidence access form the retrieval layer used before model analysis.
- [[GraphModeling]] - author, video, processing run, and evidence provenance are represented as related records.
- [[MultimodalDataPipelines]] - HawDB persists transcript, frame-derived, vector, and provenance records produced by the pipeline.

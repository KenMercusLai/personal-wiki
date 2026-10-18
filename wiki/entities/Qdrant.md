---
title: "Qdrant"
type: entity
tags: [database, vector-search, ai, retrieval]
sources:
  - custom-llm-memory-layer
last_updated: 2026-10-18
knowledge_schema: synthesis-v1
---

## Overview
[[Qdrant]] is a vector database used in the tutorial as persistent per-user storage and similarity retrieval for atomic memories.

## Current Profile
The implementation creates a `memories` collection with 64-dimensional dot-product vectors, stores text, date, and `user_id` as payload, and creates an index over `user_id`. Search embeds model-generated query text, applies the trusted user's identifier as a payload filter, sets a score threshold, and returns a bounded number of nearest memories.

## Key Characteristics
- Stores embeddings beside memory text and metadata payloads.
- Supports dot-product similarity search over a configured vector dimension.
- Applies indexed payload filters such as `user_id` during retrieval.
- Exposes asynchronous upsert, query, and deletion operations in the tutorial.

## Evidence
- Collection design: [[custom-llm-memory-layer]] configures a 64-dimensional dot-product collection and an integer payload index on `user_id`.
- Record lifecycle: [[custom-llm-memory-layer]] demonstrates point upsert and deletion with UUID-like point identifiers.
- Retrieval: [[custom-llm-memory-layer]] combines a query vector, per-user filter, score threshold, and top-k limit.

## Qualifications
The source does not benchmark Qdrant, compare it with other stores, test concurrent tenants, or evaluate backup, recovery, authorization, and production failure handling. The 64 dimensions, score threshold, and top-k value are tutorial choices, not general recommendations.

## What Changed
- Established Qdrant as the tutorial's filtered vector-storage and similarity-retrieval component.

## Relationships
- [[VectorDatabase]] - is the system category Qdrant represents.
- [[Embeddings]] - supply the vectors stored and queried in Qdrant.
- [[AgentMemory]] - uses Qdrant as one retrieval component rather than the complete memory semantics.
- [[DSPy]] - controls tools that generate queries and call the Qdrant-backed search helper.

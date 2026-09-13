---
title: "pgvector"
type: entity
tags: [postgresql, vector-search, open-source, database-extension]
sources:
  - aws-blog-optimize-generative-ai-applications-with-pgvector-indexing
last_updated: 2026-09-13
knowledge_schema: synthesis-v1
---

## Overview
[[Pgvector]] is an open-source [[PostgreSQL]] extension for storing and searching vector embeddings inside PostgreSQL.

## Current Profile
The AWS source presents pgvector as the bridge between relational PostgreSQL deployments and vector retrieval workloads for generative AI. It supports vector columns, distance operators, and approximate nearest-neighbor indexes so teams can keep embeddings near application data in Amazon RDS for PostgreSQL or Amazon Aurora PostgreSQL.

The article focuses less on pgvector as a project history and more on operational index choice. pgvector supplies L2, cosine, and inner-product operator classes, plus [[IVFFlatIndex]] and [[HNSWIndex]] options that trade build time, recall, memory, and query latency differently.

## Key Characteristics
- Extends [[PostgreSQL]] with vector storage and similarity search.
- Supports L2, cosine, and inner-product distance operations through operator classes.
- Provides IVFFlat and HNSW approximate nearest-neighbor indexes.
- Can support RAG-style enterprise context retrieval without a separate specialized vector database.
- Requires index and operator choices to match the query's distance metric.

## Evidence
- PostgreSQL extension role: [[aws-blog-optimize-generative-ai-applications-with-pgvector-indexing]] says pgvector stores and retrieves vector embeddings as high-dimensional points in PostgreSQL.
- Distance operations: [[aws-blog-optimize-generative-ai-applications-with-pgvector-indexing]] lists `vector_l2_ops`, `vector_cosine_ops`, and `vector_ip_ops`.
- Index options: [[aws-blog-optimize-generative-ai-applications-with-pgvector-indexing]] explains IVFFlat and HNSW index creation for L2, cosine, and inner-product search.
- RAG implementation: [[aws-blog-optimize-generative-ai-applications-with-pgvector-indexing]] stores 58,634 embedded document chunks in a PostgreSQL table and searches them by cosine distance.

## Qualifications
The source is an AWS technical blog post with one benchmark setup, not a neutral survey of all vector stores or pgvector versions. Its performance numbers depend on dataset size, dimensionality, hardware, PostgreSQL version, pgvector version, query shape, and recall requirements.

## What Changed
- Created the pgvector entity page from the AWS vector-indexing article.

## Relationships
- [[PostgreSQL]] - pgvector extends PostgreSQL with vector capabilities.
- [[VectorDatabase]] - pgvector lets PostgreSQL act as a vector retrieval store.
- [[Embeddings]] - pgvector stores and searches embedding vectors.
- [[RetrievalAugmentedGeneration]] - pgvector-backed retrieval can supply enterprise context to LLMs.
- [[IVFFlatIndex]] - one pgvector ANN index type.
- [[HNSWIndex]] - one pgvector ANN index type.

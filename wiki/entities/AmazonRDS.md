---
title: "Amazon RDS"
type: entity
tags: [aws, database, postgresql]
sources:
  - aws-blog-optimize-generative-ai-applications-with-pgvector-indexing
last_updated: 2026-09-13
knowledge_schema: synthesis-v1
---

## Overview
[[AmazonRDS]] is presented as the managed PostgreSQL environment used for testing pgvector index behavior.

## Current Profile
The AWS article uses Amazon RDS for PostgreSQL as the concrete deployment target for a pgvector-backed product-catalog search. The benchmark environment stores LangChain-generated document chunks and embeddings in an RDS PostgreSQL table, then compares sequential scan, IVFFlat, and HNSW query plans.

## Key Characteristics
- Hosts PostgreSQL with pgvector in the article's test setup.
- Supports a LangChain embedding table with metadata and vector columns.
- Provides the managed database context for comparing vector index query plans.

## Evidence
- Test setup: [[aws-blog-optimize-generative-ai-applications-with-pgvector-indexing]] says the initial tests used an RDS db.r5.large instance with PostgreSQL 15.4 and pgvector 0.5.0.
- RAG table: [[aws-blog-optimize-generative-ai-applications-with-pgvector-indexing]] stores 58,634 document chunks in `langchain_pg_embedding`.
- Query-plan comparison: [[aws-blog-optimize-generative-ai-applications-with-pgvector-indexing]] compares sequential scan, IVFFlat, and HNSW plans on the RDS PostgreSQL workload.

## Qualifications
The source is a single AWS-authored benchmark and does not compare RDS with self-managed PostgreSQL or non-AWS managed PostgreSQL services.

## What Changed
- Created the Amazon RDS entity page for the pgvector benchmark environment.

## Relationships
- [[AWS]] - Amazon RDS is the managed database service in the AWS source.
- [[PostgreSQL]] - the source uses RDS for PostgreSQL.
- [[Pgvector]] - pgvector runs inside the RDS PostgreSQL test database.
- [[HNSWIndex]] - HNSW is benchmarked on the RDS PostgreSQL workload.
- [[IVFFlatIndex]] - IVFFlat is benchmarked on the RDS PostgreSQL workload.

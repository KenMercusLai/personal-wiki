---
title: "Amazon Aurora"
type: entity
tags: [aws, database, postgresql]
sources:
  - aws-blog-optimize-generative-ai-applications-with-pgvector-indexing
last_updated: 2026-09-13
knowledge_schema: synthesis-v1
---

## Overview
[[AmazonAurora]] is presented as an AWS PostgreSQL-compatible database option for pgvector-backed generative AI applications.

## Current Profile
The source mainly benchmarks Amazon RDS for PostgreSQL, but it also frames the guidance as applicable to Amazon Aurora PostgreSQL. Aurora appears as a managed PostgreSQL-compatible deployment target where pgvector can store and search embeddings for RAG applications.

## Key Characteristics
- Offers a PostgreSQL-compatible target for pgvector use.
- Is named alongside Amazon RDS for PostgreSQL as a deployment option.
- Supports the broader AWS story of keeping vector retrieval in a managed relational database.

## Evidence
- Deployment option: [[aws-blog-optimize-generative-ai-applications-with-pgvector-indexing]] says the post discusses indexes for Amazon RDS for PostgreSQL and Amazon Aurora PostgreSQL.
- RAG storage: [[aws-blog-optimize-generative-ai-applications-with-pgvector-indexing]] says knowledge bases can split documents, create embeddings, and store them in Amazon Aurora PostgreSQL.
- Conclusion framing: [[aws-blog-optimize-generative-ai-applications-with-pgvector-indexing]] presents pgvector index choice as useful for generative AI applications on Aurora PostgreSQL.

## Qualifications
The source's detailed performance test is on RDS PostgreSQL and a later r7g.large rerun for HNSW build time, so Aurora-specific performance is not independently established here.

## What Changed
- Created the Amazon Aurora entity page for the source's Aurora PostgreSQL references.

## Relationships
- [[AWS]] - Amazon Aurora is an AWS managed database service.
- [[PostgreSQL]] - the relevant Aurora variant is PostgreSQL-compatible.
- [[Pgvector]] - pgvector-backed vector search is the article's use case.
- [[RetrievalAugmentedGeneration]] - Aurora PostgreSQL is named as a storage option for RAG embeddings.

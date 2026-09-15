---
title: "Amazon Aurora"
type: entity
tags: [aws, database, postgresql]
sources:
  - aws-blog-optimize-generative-ai-applications-with-pgvector-indexing
  - cnbc-amazon-plans-to-move-off-oracle-software-by-early-2020
last_updated: 2026-09-15
knowledge_schema: synthesis-v1
---

## Overview
[[AmazonAurora]] is presented as an AWS relational database service that appears both as a PostgreSQL-compatible option for pgvector-backed generative AI applications and as part of AWS's competitive challenge to Oracle's core database market.

## Current Profile
AWS's pgvector guidance mainly benchmarks Amazon RDS for PostgreSQL, but it also frames the guidance as applicable to Amazon Aurora PostgreSQL. Aurora appears as a managed PostgreSQL-compatible deployment target where pgvector can store and search embeddings for RAG applications.

Aurora also has an earlier strategic role in the Amazon-Oracle rivalry. AWS introduced Aurora in 2014, taking aim at Oracle's core market, so Aurora is not only a managed PostgreSQL-compatible database option in the wiki; it is also evidence that AWS used database services to compete directly with incumbent enterprise database vendors.

## Key Characteristics
- Offers a PostgreSQL-compatible target for pgvector use.
- Is named alongside Amazon RDS for PostgreSQL as a deployment option.
- Supports the broader AWS story of keeping vector retrieval in a managed relational database.
- Was introduced by AWS in 2014 as a direct challenge to Oracle's core database market.
- Had named customers such as Capital One, Expedia, GE, and Verizon listed on the AWS website in the CNBC source.

## Evidence
- Deployment option: [[aws-blog-optimize-generative-ai-applications-with-pgvector-indexing]] says the post discusses indexes for Amazon RDS for PostgreSQL and Amazon Aurora PostgreSQL.
- RAG storage: [[aws-blog-optimize-generative-ai-applications-with-pgvector-indexing]] says knowledge bases can split documents, create embeddings, and store them in Amazon Aurora PostgreSQL.
- Conclusion framing: [[aws-blog-optimize-generative-ai-applications-with-pgvector-indexing]] presents pgvector index choice as useful for generative AI applications on Aurora PostgreSQL.
- Competitive launch: [[cnbc-amazon-plans-to-move-off-oracle-software-by-early-2020]] says AWS introduced Aurora in 2014, taking aim at Oracle's core market.
- Customer examples: [[cnbc-amazon-plans-to-move-off-oracle-software-by-early-2020]] says Capital One, Expedia, GE, and Verizon were among Aurora customers according to the AWS website.

## Qualifications
The pgvector source's detailed performance test is on RDS PostgreSQL and a later r7g.large rerun for HNSW build time, so Aurora-specific performance is not independently established there. The CNBC source reports AWS's competitive positioning and customer claims rather than independently benchmarking Aurora against Oracle Database.

## What Changed
- Created the Amazon Aurora entity page for the source's Aurora PostgreSQL references.
- Added CNBC's 2018 framing of Aurora as an AWS challenge to Oracle's core database market.

## Relationships
- [[AWS]] - Amazon Aurora is an AWS managed database service.
- [[Oracle]] - Aurora is framed as targeting Oracle's core database market.
- [[EnterpriseCloudMigration]] - Aurora is part of AWS's database migration and incumbent-displacement story.
- [[PostgreSQL]] - the relevant Aurora variant is PostgreSQL-compatible.
- [[Pgvector]] - pgvector-backed vector search is the article's use case.
- [[RetrievalAugmentedGeneration]] - Aurora PostgreSQL is named as a storage option for RAG embeddings.

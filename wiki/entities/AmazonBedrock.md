---
title: "Amazon Bedrock"
type: entity
tags: [aws, ai, embeddings]
sources:
  - aws-blog-optimize-generative-ai-applications-with-pgvector-indexing
last_updated: 2026-09-13
knowledge_schema: synthesis-v1
---

## Overview
[[AmazonBedrock]] is presented as the AWS service that supplies the Titan Embeddings model used in the article's RAG indexing test.

## Current Profile
In this source, Amazon Bedrock appears as an embedding-model provider rather than as the main system under study. The test uses Titan Embeddings G1 - Text to convert product-catalog chunks and user prompts into 1,536-dimensional vectors that are then stored in PostgreSQL through pgvector.

## Key Characteristics
- Provides the Titan Embeddings model used in the benchmark.
- Converts both documents and prompts into comparable vectors.
- Fits into a RAG pipeline alongside LangChain, PostgreSQL, and pgvector.

## Evidence
- Embedding model: [[aws-blog-optimize-generative-ai-applications-with-pgvector-indexing]] identifies Titan Embeddings G1 - Text on Amazon Bedrock as the model used for document vectors.
- Vector dimensionality: [[aws-blog-optimize-generative-ai-applications-with-pgvector-indexing]] says the model outputs 1,536-dimensional embeddings.
- Prompt parity: [[aws-blog-optimize-generative-ai-applications-with-pgvector-indexing]] says search prompts must be converted with the same embedding model used for documents.

## Qualifications
The source does not compare Amazon Bedrock with other embedding providers, evaluate model quality, or discuss Bedrock's broader service surface.

## What Changed
- Created the Amazon Bedrock entity page for the embedding role in the pgvector benchmark.

## Relationships
- [[AWS]] - Amazon Bedrock is part of the AWS context in the source.
- [[Embeddings]] - Bedrock supplies the embedding model used to produce vectors.
- [[RetrievalAugmentedGeneration]] - Bedrock-generated embeddings support the retrieval pipeline.
- [[Pgvector]] - pgvector stores and searches the vectors produced from Bedrock embeddings.

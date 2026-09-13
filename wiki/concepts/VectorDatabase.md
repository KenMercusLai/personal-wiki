---
title: "Vector Database"
type: concept
tags: [ai, retrieval, database]
sources:
  - ling-ji-chu-da-jian-ji-yu-si-yu-shu-ju-de-chatgpt
  - aws-blog-optimize-generative-ai-applications-with-pgvector-indexing
last_updated: 2026-09-13
knowledge_schema: synthesis-v1
---

## Definition
[[VectorDatabase]] is a retrieval store for vectorized data that supports similarity search over embedded document chunks or other representations.

## Current Synthesis
Vector databases are the storage and retrieval layer in applications that need semantic access to external data. Document chunks or other records are embedded, saved into FAISS, Pinecone, PostgreSQL with pgvector, or a similar system, and retrieved when an embedded user question is semantically close to stored passages.

A vector store can be a specialized system or a general database extended for vector search. [[PostgreSQL]] with [[Pgvector]] shows the latter path: exact k-NN search preserves full recall, while approximate indexes such as [[IVFFlatIndex]] and [[HNSWIndex]] trade some recall and tuning complexity for lower latency.

## Key Claims
- Vector databases store embedded document chunks or other vectorized records for later semantic search.
- Similarity retrieval over vectors selects passages likely to answer a user question.
- FAISS is used in the private-chatbot tutorial as the local vector store, while Pinecone is named as another category example.
- PostgreSQL can serve as a vector database when extended with pgvector.
- Exact vector search maximizes recall but compares the query vector with every stored vector.
- Approximate vector indexes such as IVFFlat and HNSW reduce search latency by trading against recall, build time, memory, or tuning complexity.
- Vector stores are often accessed through higher-level frameworks such as LangChain.

## Evidence
- Storage role: [[ling-ji-chu-da-jian-ji-yu-si-yu-shu-ju-de-chatgpt]] says embedded chunks are saved to FAISS after processing.
- Retrieval role: [[ling-ji-chu-da-jian-ji-yu-si-yu-shu-ju-de-chatgpt]] says an embedded user question is used to find corresponding passages in the FAISS library.
- Category examples: [[ling-ji-chu-da-jian-ji-yu-si-yu-shu-ju-de-chatgpt]] names FAISS and Pinecone as vector-database options.
- Framework integration: [[ling-ji-chu-da-jian-ji-yu-si-yu-shu-ju-de-chatgpt]] identifies LangChain VectorStores as the abstraction used in the sample.
- PostgreSQL-backed vector store: [[aws-blog-optimize-generative-ai-applications-with-pgvector-indexing]] describes using PostgreSQL with pgvector to store and retrieve embeddings.
- Exact versus approximate search: [[aws-blog-optimize-generative-ai-applications-with-pgvector-indexing]] contrasts full-scan k-NN with IVFFlat and HNSW approximate nearest-neighbor indexes.
- Benchmark evidence: [[aws-blog-optimize-generative-ai-applications-with-pgvector-indexing]] reports query-plan screenshots where sequential scan is much slower than IVFFlat and HNSW index scans on the tested dataset.

## Counterevidence & Qualifications
The sources do not provide a broad comparison of vector databases, hybrid search, metadata filtering, access control, or production evaluation methods. The AWS benchmark is source-scoped: its results depend on one dataset, embedding model, PostgreSQL and pgvector versions, hardware, query pattern, and unstated recall target.

## What Changed
- Created the initial concept page for vector databases in private-data chatbot architecture.
- Added PostgreSQL-plus-pgvector as a vector database path and distinguished exact search from ANN indexing.

## Related Concepts
- [[Embeddings]] - vector databases store embeddings generated from source text.
- [[RetrievalAugmentedGeneration]] - vector retrieval supplies external context for generation.
- [[PrivateDataChatbot]] - vector databases let chatbots search uploaded private corpora.
- [[AIApplicationFramework]] - application frameworks often wrap vector-store access.
- [[PostgreSQL]] - PostgreSQL can serve as the vector store when extended with pgvector.
- [[Pgvector]] - pgvector supplies vector storage, distance operations, and ANN indexes inside PostgreSQL.
- [[ApproximateNearestNeighborSearch]] - ANN indexes accelerate vector retrieval when full recall is not required.

---
title: "Vector Database"
type: concept
tags: [ai, retrieval, database]
sources:
  - ling-ji-chu-da-jian-ji-yu-si-yu-shu-ju-de-chatgpt
  - aws-blog-optimize-generative-ai-applications-with-pgvector-indexing
  - ai-memory-de-zhen-zheng-nan-dian-wei-shen-me-vector-store-embedding-yuan-yuan-bu-gou
  - the-quest-for-one-million-iops-benchmarking-storage-at-lancedb
  - lancedb-xuan-xing-zhi-nan-ta-wei-shen-me-zhe-me-huo-yi-ji-ni-de-xiang-mu-shi-fou-gai-yong-ta
last_updated: 2026-10-11
knowledge_schema: synthesis-v1
---

## Definition
[[VectorDatabase]] is a retrieval store for vectorized data that supports similarity search over embedded document chunks or other representations.

## Current Synthesis
Vector databases are the storage and retrieval layer in applications that need semantic access to external data. Document chunks or other records are embedded, saved into FAISS, Pinecone, PostgreSQL with pgvector, or a similar system, and retrieved when an embedded user question is semantically close to stored passages.

A vector store can be a specialized system or a general database extended for vector search. [[PostgreSQL]] with [[Pgvector]] shows the latter path: exact k-NN search preserves full recall, while approximate indexes such as [[IVFFlatIndex]] and [[HNSWIndex]] trade some recall and tuning complexity for lower latency.

That retrieval role should not be confused with a complete memory model. A vector database can surface similar prior records, but similarity alone does not compact duplicates, identify which fact is current, preserve validity windows, weigh provenance, or reconcile contradictions. In [[AgentMemory]], it is therefore one possible retrieval component alongside structured graph, document, or relational state.

The [[LanceDB]] benchmark adds the storage path beneath approximate search. After an index produces candidate row identifiers, the system must fetch selected rows, decode them, and often rerank a larger candidate set. That path is sensitive to batching, cache state, data duplication, queue depth, scheduler structure, and physical I/O concurrency. Index parameters also bind retrieval quality to systems performance: lowering `nprobes` reduced CPU work enough to isolate storage, but deliberately damaged recall, so a high IOPS result cannot stand alone as a vector-search result.

The selection guide adds a deployment taxonomy. An embedded vector database can minimize setup and fit local or single-machine applications, but centralized concurrency, strict online latency, replication, and multi-node fault tolerance favor a service architecture. A relational extension such as [[Pgvector]] can minimize operational systems when vector search is secondary to existing PostgreSQL data. A lower-level algorithm library supplies indexes without a complete persistence or serving layer. These are different architectural positions, so selection should compare workload, ownership, and failure boundaries before product features.

## Key Claims
- Vector databases store embedded chunks or other vectorized records and retrieve semantically similar material for a query.
- PostgreSQL can serve as a vector database when extended with pgvector.
- Exact vector search maximizes recall but compares the query vector with every stored vector.
- Approximate vector indexes such as IVFFlat and HNSW reduce search latency by trading against recall, build time, memory, or tuning complexity.
- Vector-store deployment can be embedded, service-based, an extension to an incumbent database, or a lower-level index library with application-built infrastructure.
- Similarity search does not by itself maintain temporal, authoritative, or conflict-resolved memory state.
- Storage throughput and infrastructure simplicity must be interpreted alongside recall, concurrency, failure handling, and transferred application responsibility.

## Evidence
- Storage role: [[ling-ji-chu-da-jian-ji-yu-si-yu-shu-ju-de-chatgpt]] says embedded chunks are saved to FAISS after processing.
- Retrieval role: [[ling-ji-chu-da-jian-ji-yu-si-yu-shu-ju-de-chatgpt]] says an embedded user question is used to find corresponding passages in the FAISS library.
- Category examples: [[ling-ji-chu-da-jian-ji-yu-si-yu-shu-ju-de-chatgpt]] names FAISS and Pinecone as vector-database options.
- Framework integration: [[ling-ji-chu-da-jian-ji-yu-si-yu-shu-ju-de-chatgpt]] identifies LangChain VectorStores as the abstraction used in the sample.
- PostgreSQL-backed vector store: [[aws-blog-optimize-generative-ai-applications-with-pgvector-indexing]] describes using PostgreSQL with pgvector to store and retrieve embeddings.
- Exact versus approximate search: [[aws-blog-optimize-generative-ai-applications-with-pgvector-indexing]] contrasts full-scan k-NN with IVFFlat and HNSW approximate nearest-neighbor indexes.
- Benchmark evidence: [[aws-blog-optimize-generative-ai-applications-with-pgvector-indexing]] reports query-plan screenshots where sequential scan is much slower than IVFFlat and HNSW index scans on the tested dataset.
- Memory boundary: [[ai-memory-de-zhen-zheng-nan-dian-wei-shen-me-vector-store-embedding-yuan-yuan-bu-gou]] characterizes vector-store-plus-embedding memory as a searchable log until compaction, evolution, and conflict handling are added.
- Retrieval storage path: [[the-quest-for-one-million-iops-benchmarking-storage-at-lancedb]] follows index-selected row IDs through fetch, decode, and reranking, then shows how batching, page-cache hits, scheduler overhead, and NVMe concurrency affect throughput.
- Recall qualification: [[the-quest-for-one-million-iops-benchmarking-storage-at-lancedb]] reduces `nprobes` from 20 to 1 to isolate I/O and explicitly states that the change harms recall.
- Deployment taxonomy: [[lancedb-xuan-xing-zhi-nan-ta-wei-shen-me-zhe-me-huo-yi-ji-ni-de-xiang-mu-shi-fou-gai-yong-ta]] separates embedded libraries, client-server services, PostgreSQL extensions, and algorithm libraries by workload and ownership model.
- Embedded responsibility: [[lancedb-xuan-xing-zhi-nan-ta-wei-shen-me-zhe-me-huo-yi-ji-ni-de-xiang-mu-shi-fou-gai-yong-ta]] says removing a server tier moves cleanup, concurrency, remote-storage validation, and upgrade testing into the application.

## Counterevidence & Qualifications
The sources do not provide a controlled broad comparison of vector databases, hybrid search, metadata filtering, access control, durability, backup, recovery, or end-to-end production economics. The AWS benchmark is source-scoped: its results depend on one dataset, embedding model, PostgreSQL and pgvector versions, hardware, query pattern, and unstated recall target. The LanceDB benchmark is likewise first-party and workload-specific; its final IOPS result uses local NVMe, three datasets, high concurrency, unmerged changes, and an intentionally low-recall search setting. The selection guide is secondary and its product maturity, default behavior, feature coverage, and competitive claims are time-sensitive. The memory critique is conceptual and does not show that every application needs a graph or relational store; its narrower claim is that retrieval infrastructure cannot silently supply missing state semantics.

## What Changed
- Added embedded library, client-server service, incumbent-database extension, and algorithm-library positions.
- Made concurrency, fault tolerance, existing-stack fit, and transferred operating responsibility part of selection.

## Related Concepts
- [[Embeddings]] - vector databases store embeddings generated from source text.
- [[RetrievalAugmentedGeneration]] - vector retrieval supplies external context for generation.
- [[PrivateDataChatbot]] - vector databases let chatbots search uploaded private corpora.
- [[AIApplicationFramework]] - application frameworks often wrap vector-store access.
- [[PostgreSQL]] - PostgreSQL can serve as the vector store when extended with pgvector.
- [[Pgvector]] - pgvector supplies vector storage, distance operations, and ANN indexes inside PostgreSQL.
- [[ApproximateNearestNeighborSearch]] - ANN indexes accelerate vector retrieval when full recall is not required.
- [[AgentMemory]] - may use a vector database for recall but requires additional state-maintenance semantics.
- [[MemoryConflictResolution]] - resolves related but incompatible records that similarity search can only retrieve.
- [[StoragePerformanceBenchmarking]] - tests the row-fetch and decode path under representative cache and concurrency conditions.
- [[LanceDB]] - supplies the source's end-to-end vector-search storage case.
- [[VectorDatabaseSelection]] - turns deployment, workload, and ownership differences into a selection framework.

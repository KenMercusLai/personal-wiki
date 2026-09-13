---
title: "Approximate Nearest Neighbor Search"
type: concept
tags: [vector-search, algorithms, retrieval]
sources:
  - aws-blog-optimize-generative-ai-applications-with-pgvector-indexing
last_updated: 2026-09-13
knowledge_schema: synthesis-v1
---

## Definition
[[ApproximateNearestNeighborSearch]] is a similarity-search approach that trades perfect recall for faster retrieval over vector data.

## Current Synthesis
The AWS source introduces ANN as the practical alternative to exact k-NN when full recall is unnecessary or too expensive. Instead of comparing the query vector with every stored vector, ANN structures the search space with an index so only promising regions or graph neighborhoods are visited.

In pgvector, the source's two ANN examples are [[IVFFlatIndex]] and [[HNSWIndex]]. IVFFlat clusters vectors around centroids, while HNSW builds a multi-layer graph. Both need workload-specific tuning because the same choices that improve recall can increase latency, build time, or memory use.

## Key Claims
- Exact k-NN gives full recall by comparing a query vector against every stored vector.
- ANN improves search performance when applications can tolerate a small recall loss.
- ANN index behavior depends on distance operator, dataset shape, and workload requirements.
- IVFFlat and HNSW are pgvector-supported ANN strategies with different mechanics and tuning parameters.
- Recall and latency must be balanced rather than optimized independently.

## Evidence
- Exact-search baseline: [[aws-blog-optimize-generative-ai-applications-with-pgvector-indexing]] says exact search can be acceptable for small datasets or use cases needing full accuracy.
- Performance motivation: [[aws-blog-optimize-generative-ai-applications-with-pgvector-indexing]] says ANN offers major performance improvements at some accuracy cost.
- pgvector implementations: [[aws-blog-optimize-generative-ai-applications-with-pgvector-indexing]] explains IVFFlat and HNSW as two ANN implementations.
- Benchmark contrast: [[aws-blog-optimize-generative-ai-applications-with-pgvector-indexing]] reports sequential scan around 650 ms, IVFFlat around 2.4 ms, and HNSW around 1.5 ms for the tested query.

## Counterevidence & Qualifications
The source's benchmark is small relative to many production vector-search systems and does not publish recall measurements for the tested prompts. Its advice is therefore strongest as a mechanics-and-tuning guide, not as a universal performance ranking.

## What Changed
- Created the concept page from the AWS pgvector indexing article.

## Related Concepts
- [[VectorDatabase]] - ANN indexes accelerate vector database retrieval.
- [[Embeddings]] - ANN searches over embedding vectors.
- [[IVFFlatIndex]] - one centroid-based ANN implementation.
- [[HNSWIndex]] - one graph-based ANN implementation.
- [[RetrievalAugmentedGeneration]] - RAG systems use ANN to retrieve context quickly.

---
title: "Approximate Nearest Neighbor Search"
type: concept
tags: [vector-search, algorithms, retrieval]
sources:
  - aws-blog-optimize-generative-ai-applications-with-pgvector-indexing
  - 2604.19528
  - p3049-ooi
last_updated: 2026-10-15
knowledge_schema: synthesis-v1
---

## Definition
[[ApproximateNearestNeighborSearch]] is a similarity-search approach that trades perfect recall for faster retrieval over vector data.

## Current Synthesis
The AWS source introduces ANN as the practical alternative to exact k-NN when full recall is unnecessary or too expensive. Instead of comparing the query vector with every stored vector, ANN structures the search space with an index so only promising regions or graph neighborhoods are visited.

In pgvector, the source's two ANN examples are [[IVFFlatIndex]] and [[HNSWIndex]]. IVFFlat clusters vectors around centroids, while HNSW builds a multi-layer graph. Both need workload-specific tuning because the same choices that improve recall can increase latency, build time, or memory use.

The RaBitQ–TurboQuant comparison adds a second approximation layer: even after a search procedure chooses candidates, compressed vector codes can change the estimated inner-product order. Recall therefore depends on the quantizer, bit width, estimator objective, and random rotation as well as the index. Repeated runs and a full recall curve are more informative than one seed or one cutoff when comparing randomized compressed search.

[[HAKESIndex]] makes the candidate boundary explicit. Its compressed filter stage only needs to keep true neighbors in a larger candidate set; a full-precision refine stage can then recover their order. That changes the useful compression objective from globally reconstructing vectors or exact scores to preserving local similarity distributions well enough for candidate inclusion. Index choice also depends on update and scaling behavior: in the paper's workloads, append-oriented IVF/PQ updates avoid the graph-neighborhood locking and shard fan-out that weaken HNSW under writes and scale-out.

## Key Claims
- Exact k-NN gives full recall by comparing a query vector against every stored vector.
- ANN improves search performance when applications can tolerate a small recall loss.
- ANN index behavior depends on distance operator, dimensionality, dataset shape, update mix, shard layout, and workload requirements.
- IVFFlat and HNSW are pgvector-supported ANN strategies with different mechanics and tuning parameters.
- Recall and latency must be balanced rather than optimized independently.
- Quantization quality can change ANN candidate inclusion and ranking even when the final scoring protocol is otherwise identical.
- A filter-and-refine index can trade aggressive approximate filtering for exact reranking when true neighbors survive into the candidate set.

## Evidence
- Exact-search baseline: [[aws-blog-optimize-generative-ai-applications-with-pgvector-indexing]] says exact search can be acceptable for small datasets or use cases needing full accuracy.
- Performance motivation: [[aws-blog-optimize-generative-ai-applications-with-pgvector-indexing]] says ANN offers major performance improvements at some accuracy cost.
- pgvector implementations: [[aws-blog-optimize-generative-ai-applications-with-pgvector-indexing]] explains IVFFlat and HNSW as two ANN implementations.
- Benchmark contrast: [[aws-blog-optimize-generative-ai-applications-with-pgvector-indexing]] reports sequential scan around 650 ms, IVFFlat around 2.4 ms, and HNSW around 1.5 ms for the tested query.
- Quantized ranking: [[2604.19528]] reports ten-run Recall@1@k curves across GloVe-200 and two OpenAI3 datasets, with RaBitQ above both TurboQuant variants at two and four bits and the largest differences at small `k`.
- Filter-and-refine evidence: [[p3049-ooi]] reports that learned local-distribution-preserving compression improves candidate recall across every displayed ten-million-vector configuration, enabling smaller probe and candidate budgets.
- Update and scaling evidence: [[p3049-ooi]] reports partitioning-based indexes retaining more throughput than HNSW as writes rise and HAKES scaling nearly linearly while sharded graph baselines flatten in its one-to-eight-node tests.

## Counterevidence & Qualifications
The AWS benchmark is small relative to many production vector-search systems and does not publish recall measurements for the tested prompts. The quantizer comparison is authored by RaBitQ researchers, evaluates exhaustive ranking over quantized base vectors rather than a full optimized ANN index, and reports no independent reproduction. The HAKES comparison is likewise first-party and implementation-sensitive, covers selected in-memory high-dimensional datasets, and trades away strong consistency. None of the sources establishes a universal performance ranking.

## What Changed
- Added candidate inclusion as distinct from final candidate ordering.
- Added filter-and-refine as a route to aggressive compression with exact reranking.
- Added update contention and shard layout to ANN system selection.

## Related Concepts
- [[VectorDatabase]] - ANN indexes accelerate vector database retrieval.
- [[Embeddings]] - ANN searches over embedding vectors.
- [[IVFFlatIndex]] - one centroid-based ANN implementation.
- [[HNSWIndex]] - one graph-based ANN implementation.
- [[RetrievalAugmentedGeneration]] - RAG systems use ANN to retrieve context quickly.
- [[VectorQuantization]] - compressed codes can change candidate similarity estimates and recall.
- [[RaBitQ]] - quantizer reporting stronger recall in the source's tested settings.
- [[TurboQuant]] - comparison quantizer with separate reconstruction and unbiased variants.
- [[HAKESIndex]] - learned filter-and-refine ANN design with decoupled search and insert parameters.
- [[HAKES]] - distributed system showing how ANN index structure affects scale-out and mixed workloads.

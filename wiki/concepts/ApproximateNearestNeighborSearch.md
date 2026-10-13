---
title: "Approximate Nearest Neighbor Search"
type: concept
tags: [vector-search, algorithms, retrieval]
sources:
  - aws-blog-optimize-generative-ai-applications-with-pgvector-indexing
  - 2604.19528
last_updated: 2026-10-13
knowledge_schema: synthesis-v1
---

## Definition
[[ApproximateNearestNeighborSearch]] is a similarity-search approach that trades perfect recall for faster retrieval over vector data.

## Current Synthesis
The AWS source introduces ANN as the practical alternative to exact k-NN when full recall is unnecessary or too expensive. Instead of comparing the query vector with every stored vector, ANN structures the search space with an index so only promising regions or graph neighborhoods are visited.

In pgvector, the source's two ANN examples are [[IVFFlatIndex]] and [[HNSWIndex]]. IVFFlat clusters vectors around centroids, while HNSW builds a multi-layer graph. Both need workload-specific tuning because the same choices that improve recall can increase latency, build time, or memory use.

The RaBitQ–TurboQuant comparison adds a second approximation layer: even after a search procedure chooses candidates, compressed vector codes can change the estimated inner-product order. Recall therefore depends on the quantizer, bit width, estimator objective, and random rotation as well as the index. Repeated runs and a full recall curve are more informative than one seed or one cutoff when comparing randomized compressed search.

## Key Claims
- Exact k-NN gives full recall by comparing a query vector against every stored vector.
- ANN improves search performance when applications can tolerate a small recall loss.
- ANN index behavior depends on distance operator, dataset shape, and workload requirements.
- IVFFlat and HNSW are pgvector-supported ANN strategies with different mechanics and tuning parameters.
- Recall and latency must be balanced rather than optimized independently.
- Quantization quality can change ANN ranking even when the candidate-scoring protocol is otherwise identical.

## Evidence
- Exact-search baseline: [[aws-blog-optimize-generative-ai-applications-with-pgvector-indexing]] says exact search can be acceptable for small datasets or use cases needing full accuracy.
- Performance motivation: [[aws-blog-optimize-generative-ai-applications-with-pgvector-indexing]] says ANN offers major performance improvements at some accuracy cost.
- pgvector implementations: [[aws-blog-optimize-generative-ai-applications-with-pgvector-indexing]] explains IVFFlat and HNSW as two ANN implementations.
- Benchmark contrast: [[aws-blog-optimize-generative-ai-applications-with-pgvector-indexing]] reports sequential scan around 650 ms, IVFFlat around 2.4 ms, and HNSW around 1.5 ms for the tested query.
- Quantized ranking: [[2604.19528]] reports ten-run Recall@1@k curves across GloVe-200 and two OpenAI3 datasets, with RaBitQ above both TurboQuant variants at two and four bits and the largest differences at small `k`.

## Counterevidence & Qualifications
The AWS benchmark is small relative to many production vector-search systems and does not publish recall measurements for the tested prompts. The quantizer comparison is authored by RaBitQ researchers, evaluates exhaustive ranking over quantized base vectors rather than a full optimized ANN index, and reports no independent reproduction. Neither source establishes a universal performance ranking.

## What Changed
- Added quantized similarity estimation as a second source of approximate ranking error.
- Added repeated-run Recall@1@k evidence and the interested-party qualification.

## Related Concepts
- [[VectorDatabase]] - ANN indexes accelerate vector database retrieval.
- [[Embeddings]] - ANN searches over embedding vectors.
- [[IVFFlatIndex]] - one centroid-based ANN implementation.
- [[HNSWIndex]] - one graph-based ANN implementation.
- [[RetrievalAugmentedGeneration]] - RAG systems use ANN to retrieve context quickly.
- [[VectorQuantization]] - compressed codes can change candidate similarity estimates and recall.
- [[RaBitQ]] - quantizer reporting stronger recall in the source's tested settings.
- [[TurboQuant]] - comparison quantizer with separate reconstruction and unbiased variants.

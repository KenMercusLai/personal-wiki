---
title: "HNSW Index"
type: concept
tags: [vector-search, pgvector, indexing, graph-algorithms]
sources:
  - aws-blog-optimize-generative-ai-applications-with-pgvector-indexing
last_updated: 2026-09-13
knowledge_schema: synthesis-v1
---

## Definition
[[HNSWIndex]] is a graph-based approximate vector index that searches through layered neighborhoods to find near vectors quickly.

## Current Synthesis
The AWS source frames HNSW as a combination of skip-list intuition and navigable small-world graph search. The inspected diagrams show why the layered structure matters: sparse upper layers make long jumps from an entry point, then denser lower layers refine the nearest-neighbor search around the query.

HNSW is tuned differently from IVFFlat. Build-time parameters such as `m` and `ef_construction` affect graph connectivity, memory, and build latency, while `hnsw.ef_search` expands the query-time candidate set to improve recall at a latency cost. In the article's benchmark, HNSW had the fastest query time, and pgvector 0.6.0 reduced HNSW build time substantially compared with 0.5.0.

## Key Claims
- HNSW represents vectors as a multi-layer graph with sparse upper layers and denser lower layers.
- Search starts from a high-level entry point and greedily descends toward nearer candidates.
- Multiple candidate entry points can improve search quality.
- `m` and `ef_construction` affect build-time graph quality, memory, and latency.
- `hnsw.ef_search` affects query-time candidate breadth, recall, and latency.
- In the source's test, HNSW queries were faster than IVFFlat, while HNSW index builds were slower than IVFFlat builds.

## Evidence
- Skip-list analogy: [[aws-blog-optimize-generative-ai-applications-with-pgvector-indexing]] uses an inspected skip-list figure to explain faster navigation through layered links.
- NSW qualification: [[aws-blog-optimize-generative-ai-applications-with-pgvector-indexing]] shows greedy routing and an early-stopping case where graph navigability can fail.
- Layered HNSW mechanics: [[aws-blog-optimize-generative-ai-applications-with-pgvector-indexing]] includes an inspected HNSW figure where search descends layer by layer from an entry point to the nearest lower-layer neighbor.
- Parameter guidance: [[aws-blog-optimize-generative-ai-applications-with-pgvector-indexing]] describes `m`, `ef_construction`, and `hnsw.ef_search`.
- Performance evidence: [[aws-blog-optimize-generative-ai-applications-with-pgvector-indexing]] reports HNSW query execution around 1.5 ms and HNSW build time improving from about 81 seconds in pgvector 0.5.0 to about 30 seconds in 0.6.0.

## Counterevidence & Qualifications
The source notes that vector storage and retrieval recommendations are changing quickly. Its HNSW performance claim is limited to one dataset, hardware setup, PostgreSQL version, pgvector version, query style, and unstated recall target.

## What Changed
- Created the HNSW index concept page from the AWS pgvector article.

## Related Concepts
- [[ApproximateNearestNeighborSearch]] - HNSW is one ANN index strategy.
- [[Pgvector]] - pgvector implements HNSW indexes for vector columns.
- [[IVFFlatIndex]] - IVFFlat is the contrasting centroid-based pgvector ANN index.
- [[VectorDatabase]] - HNSW accelerates vector database similarity retrieval.

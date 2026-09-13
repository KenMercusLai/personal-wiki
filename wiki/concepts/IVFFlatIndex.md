---
title: "IVFFlat Index"
type: concept
tags: [vector-search, pgvector, indexing]
sources:
  - aws-blog-optimize-generative-ai-applications-with-pgvector-indexing
last_updated: 2026-09-13
knowledge_schema: synthesis-v1
---

## Definition
[[IVFFlatIndex]] is an approximate vector index that clusters vectors into centroid-defined regions and searches selected regions instead of scanning the full vector space.

## Current Synthesis
The AWS source explains IVFFlat as a performance-oriented pgvector index built from K-means-like partitioning. The inspected figures show two regions with centroids: when the query is near a centroid, local search can find close neighbors efficiently, but a query near a region boundary may miss a closer vector in a neighboring region.

The index's main tuning knobs are `lists`, which controls how many clusters exist at build time, and `ivfflat.probes`, which controls how many nearby regions are searched at query time. More lists can make each searched region smaller but increase boundary-related recall risk, while more probes can recover recall by visiting more regions at a latency cost.

## Key Claims
- IVFFlat partitions vector space into regions around centroids.
- Query-time search begins with the region whose centroid is closest to the query vector.
- Boundary cases can lose recall when the nearest actual vector sits in a neighboring region.
- `lists` controls the number of index regions created at build time.
- `ivfflat.probes` controls how many regions are searched at query time.
- IVFFlat must be built after data is loaded because it needs vectors to identify centroids.

## Evidence
- Region mechanics: [[aws-blog-optimize-generative-ai-applications-with-pgvector-indexing]] describes centroids, regions, and local search within a selected region.
- Diagram evidence: [[aws-blog-optimize-generative-ai-applications-with-pgvector-indexing]] includes inspected figures showing a successful Region 1 local search and a boundary case where Region 1 contains a closer vector than the chosen Region 2 search area.
- Tuning parameters: [[aws-blog-optimize-generative-ai-applications-with-pgvector-indexing]] explains `lists` and `ivfflat.probes` as the main recall/performance controls.
- Query-plan evidence: [[aws-blog-optimize-generative-ai-applications-with-pgvector-indexing]] shows an IVFFlat cosine index with `lists='100'` and an index-scan execution time around 2.5 ms.

## Counterevidence & Qualifications
The source does not give recall curves across `lists` and `probes`, nor does it evaluate insert/update churn beyond warning that rebuilding may be needed after adding or modifying vectors.

## What Changed
- Created the IVFFlat index concept page from the AWS pgvector article.

## Related Concepts
- [[ApproximateNearestNeighborSearch]] - IVFFlat is one ANN index strategy.
- [[Pgvector]] - pgvector implements IVFFlat indexes for vector columns.
- [[HNSWIndex]] - HNSW is the contrasting graph-based pgvector ANN index.
- [[VectorDatabase]] - IVFFlat accelerates vector database similarity retrieval.

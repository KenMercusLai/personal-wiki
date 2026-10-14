---
title: "Hybrid Search"
type: concept
tags: [search, information-retrieval, ranking]
sources:
  - bm25-the-search-algorithm-behind-elasticsearch
last_updated: 2026-10-14
knowledge_schema: synthesis-v1
---

## Definition
[[HybridSearch]] combines lexical retrieval with semantic retrieval or neural reranking so exact-term evidence and meaning-based evidence can contribute to one result set.

## Current Synthesis
The source describes two common compositions. A serial pipeline uses [[BM25]] to retrieve a bounded candidate pool and a cross-encoder to rerank it, avoiding neural scoring over the whole collection. A parallel pipeline runs BM25 and a dense retriever independently, then combines their ordered results with reciprocal-rank fusion so incompatible raw score scales do not need direct calibration.

The rationale is complementary error coverage: BM25 is fast, interpretable, training-free, and strong on rare exact terms, but it cannot bridge synonyms or disambiguate meaning; dense and neural methods add semantic matching at higher computational and operational cost. Hybridization is an architecture pattern rather than proof of better relevance, so candidate depth, fusion, latency, and evaluation remain collection-specific decisions.

## Key Claims
- Lexical and dense retrieval expose complementary evidence rather than interchangeable scores.
- First-stage BM25 followed by neural reranking bounds expensive model inference to a candidate set.
- Parallel retrieval plus reciprocal-rank fusion combines rank positions without assuming comparable score scales.
- Hybrid effectiveness depends on candidate recall, reranker quality, fusion settings, latency budgets, and relevance judgments.

## Evidence
Serial candidate and reranking pipeline:
- [[bm25-the-search-algorithm-behind-elasticsearch]] describes retrieving roughly 100 to 1,000 BM25 candidates before a cross-encoder selects the final results.

Parallel rank fusion:
- [[bm25-the-search-algorithm-behind-elasticsearch]] presents reciprocal-rank fusion as a way to merge BM25 and dense rankings without calibrating BM25 scores against cosine similarity.

Complementary strengths:
- [[bm25-the-search-algorithm-behind-elasticsearch]] contrasts BM25's speed, interpretability, rare-term matching, and zero-training setup with its semantic and vocabulary limitations.

## Counterevidence & Qualifications
The source gives no hybrid-search experiment, dataset, latency profile, cost analysis, ablation, or relevance metric. Candidate counts are examples rather than validated settings, and the article does not compare serial reranking with parallel fusion. Hybrid search can still lose relevant material during first-stage retrieval, add serving complexity, or produce unstable rankings when its components and fusion rule are poorly evaluated.

## What Changed
- Established the serial-reranking and parallel-fusion forms of hybrid lexical-semantic retrieval.

## Related Concepts
- [[BM25]] - supplies the exact-match lexical signal or first-stage candidate set.
- [[SemanticSearch]] - supplies meaning-based candidates that can bridge vocabulary mismatch.
- [[SearchRelevance]] - supplies the evaluation target for choosing candidate depth and fusion behavior.
- [[RetrievalAugmentedGeneration]] - often consumes candidate sets produced by lexical, semantic, or hybrid retrieval.

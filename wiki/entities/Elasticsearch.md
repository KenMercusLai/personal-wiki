---
title: "Elasticsearch"
type: entity
tags: [search, information-retrieval, software]
sources:
  - bm25-the-search-algorithm-behind-elasticsearch
last_updated: 2026-10-14
knowledge_schema: synthesis-v1
---

## Overview
[[Elasticsearch]] is a production search system represented in this source through its use and configuration of [[BM25]] lexical ranking.

## Current Profile
The article says Elasticsearch uses BM25 as its default scoring algorithm and exposes `k1` and `b` per field through index mappings. It also describes phrase queries, multi-field scoring, and hybrid retrieval as ways to extend pure bag-of-words ranking, but does not independently test Elasticsearch's implementation or operational behavior.

## Key Characteristics
- Uses BM25 as the default lexical scoring model according to the source.
- Permits per-field adjustment of term-frequency saturation and document-length normalization.
- Supports phrase matching as a partial response to BM25's loss of word order.
- Is described as supporting hybrid retrieval with lexical and dense signals.

## Evidence
Default scoring and tuning:
- [[bm25-the-search-algorithm-behind-elasticsearch]] states that Elasticsearch uses BM25 by default and shows `k1` and `b` configured in an index mapping.

Lexical extensions:
- [[bm25-the-search-algorithm-behind-elasticsearch]] identifies field-aware ranking and phrase queries as mechanisms for structured importance and exact order.

Hybrid role:
- [[bm25-the-search-algorithm-behind-elasticsearch]] names Elasticsearch among systems supporting BM25 plus dense-vector retrieval.

## Qualifications
This profile rests on one secondary tutorial and does not establish version-specific defaults, distributed architecture, index internals, benchmark performance, or the exact semantics of every feature it attributes to Elasticsearch. Configuration and product capabilities can change across releases.

## What Changed
- Created a bounded profile of Elasticsearch's BM25 configuration and hybrid-search role.

## Relationships
- [[BM25]] - default lexical ranker attributed to Elasticsearch by the source.
- [[HybridSearch]] - combines Elasticsearch lexical and dense retrieval signals.
- [[InvertedIndex]] - underlying sparse retrieval structure described by the tutorial.
- [[SearchRelevance]] - application objective used to evaluate and tune ranking behavior.

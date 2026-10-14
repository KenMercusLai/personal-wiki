---
title: "Inverted Index"
type: concept
tags: [search, information-retrieval, data-structures]
sources:
  - blog-aakash-japi-implementing-a-search-engine-with-ranking-in-python
  - bm25-the-search-algorithm-behind-elasticsearch
last_updated: 2026-10-14
knowledge_schema: synthesis-v1
---

## Definition
[[InvertedIndex]] is a search data structure that maps each token to the documents where it appears; in a position-aware form, it also stores the token positions inside each document.

## Current Synthesis
The sources present an inverted index as the central bridge between raw text and fast query answering. A position-aware educational index shaped as `{word: {documentID: [positions]}}` supports free-text and phrase matching. A ranking-oriented production design also stores term frequencies and combines postings with collection-wide document frequencies, individual document lengths, and average document length so [[BM25]] can score only documents containing at least one query term.

## Key Claims
- An inverted index reverses the document-to-words relationship into a word-to-documents lookup.
- Position lists extend the index from ordinary word lookup to ordered phrase matching.
- Building the index requires tokenization and normalization before aggregation.
- Nested dictionaries are enough to demonstrate the core retrieval structure for local files.
- Ranking-oriented postings can carry per-document term frequency while collection metadata supplies IDF and length-normalization statistics.
- Candidate lookup changes query work from scanning all documents to scoring the postings reached by query terms.

## Evidence
Word-to-document lookup:
- [[blog-aakash-japi-implementing-a-search-engine-with-ranking-in-python]] defines the inverted index as mapping tokens to the documents in which they appear.

Position-aware phrase support:
- [[blog-aakash-japi-implementing-a-search-engine-with-ranking-in-python]] stores each word's token positions per document so phrase queries can later test adjacency and order.

Index construction pipeline:
- [[blog-aakash-japi-implementing-a-search-engine-with-ranking-in-python]] builds from sanitized file token lists to per-document indices and then to the final nested dictionary.

Demonstration-scale implementation:
- [[blog-aakash-japi-implementing-a-search-engine-with-ranking-in-python]] uses Python dictionaries and lists rather than specialized search infrastructure.

Ranking statistics and candidate narrowing:
- [[bm25-the-search-algorithm-behind-elasticsearch]] stores `(document, term-frequency)` postings plus document frequency and length statistics, then scores only the union of documents reached by query terms.

## Counterevidence & Qualifications
Both sources are educational implementations rather than production index evaluations. The BM25 article names compressed indexes, skip lists, block-max skipping, and caching as production optimizations but neither source implements or measures them. Neither covers incremental indexing, distributed shards, concurrency, durability, Unicode edge cases, or index-maintenance costs.

## What Changed
- Created the concept to capture exact-match search indexing.
- Added the collection statistics and postings data needed for BM25, plus the candidate-narrowing complexity boundary.

## Related Concepts
- [[PhraseQuery]] - phrase search depends on a position-aware inverted index.
- [[TFIDFRanking]] - ranking uses indexed term statistics after candidate retrieval.
- [[BM25]] - consumes postings, term frequencies, document frequencies, and length statistics from the index.
- [[NaturalLanguageProcessing]] - tokenization and normalization are NLP preprocessing steps.
- [[SemanticSearch]] - semantic search contrasts with exact token lookup by using meaning-based similarity.

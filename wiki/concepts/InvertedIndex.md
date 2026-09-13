---
title: "Inverted Index"
type: concept
tags: [search, information-retrieval, data-structures]
sources:
  - blog-aakash-japi-implementing-a-search-engine-with-ranking-in-python
last_updated: 2026-09-14
knowledge_schema: synthesis-v1
---

## Definition
[[InvertedIndex]] is a search data structure that maps each token to the documents where it appears; in a position-aware form, it also stores the token positions inside each document.

## Current Synthesis
The source presents an inverted index as the central bridge between raw text files and fast query answering. A simple index can map a word to matching documents, while a richer index shaped as `{word: {documentID: [positions]}}` can support both free-text retrieval and phrase matching. The tutorial's construction path moves from files to token lists, then to per-file word-position maps, and finally to a corpus-level inverted index.

## Key Claims
- An inverted index reverses the document-to-words relationship into a word-to-documents lookup.
- Position lists extend the index from ordinary word lookup to ordered phrase matching.
- Building the index requires tokenization and normalization before aggregation.
- Nested dictionaries are enough to demonstrate the core retrieval structure for local files.

## Evidence
Word-to-document lookup:
- [[blog-aakash-japi-implementing-a-search-engine-with-ranking-in-python]] defines the inverted index as mapping tokens to the documents in which they appear.

Position-aware phrase support:
- [[blog-aakash-japi-implementing-a-search-engine-with-ranking-in-python]] stores each word's token positions per document so phrase queries can later test adjacency and order.

Index construction pipeline:
- [[blog-aakash-japi-implementing-a-search-engine-with-ranking-in-python]] builds from sanitized file token lists to per-document indices and then to the final nested dictionary.

Demonstration-scale implementation:
- [[blog-aakash-japi-implementing-a-search-engine-with-ranking-in-python]] uses Python dictionaries and lists rather than specialized search infrastructure.

## Counterevidence & Qualifications
The source explains a local-file educational implementation, not a production search index. It does not cover compression, postings-list skipping, incremental indexing, distributed shards, ranking-feature storage, Unicode/tokenization edge cases, or modern hybrid search.

## What Changed
- Created the concept to capture exact-match search indexing.

## Related Concepts
- [[PhraseQuery]] - phrase search depends on a position-aware inverted index.
- [[TFIDFRanking]] - ranking uses indexed term statistics after candidate retrieval.
- [[NaturalLanguageProcessing]] - tokenization and normalization are NLP preprocessing steps.
- [[SemanticSearch]] - semantic search contrasts with exact token lookup by using meaning-based similarity.

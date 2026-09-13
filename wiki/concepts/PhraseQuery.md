---
title: "Phrase Query"
type: concept
tags: [search, information-retrieval, querying]
sources:
  - blog-aakash-japi-implementing-a-search-engine-with-ranking-in-python
last_updated: 2026-09-14
knowledge_schema: synthesis-v1
---

## Definition
[[PhraseQuery]] is a search query that requires all query terms to appear in a document in the same adjacent order as the requested phrase.

## Current Synthesis
The article treats phrase search as the ordered counterpart to ordinary free-text search. A free-text query can union documents that contain any query word, while a phrase query first intersects documents containing every word and then uses position lists to test whether the terms occur as a sequence. The implementation subtracts each word's query offset from its document positions; a shared adjusted position indicates the whole phrase occurs in order.

## Key Claims
- Phrase search requires more information than document membership; it needs term positions.
- Candidate documents can be narrowed by intersecting the document lists for every query term.
- Ordering can be tested by normalizing each term's position list by its offset in the phrase.
- Phrase logic complements free-text query logic rather than replacing it.

## Evidence
Need for positions:
- [[blog-aakash-japi-implementing-a-search-engine-with-ranking-in-python]] adds token positions to the inverted index specifically to support phrases.

Candidate intersection:
- [[blog-aakash-japi-implementing-a-search-engine-with-ranking-in-python]] first intersects all one-word query result lists before testing order.

Offset-normalized position test:
- [[blog-aakash-japi-implementing-a-search-engine-with-ranking-in-python]] demonstrates that subtracting 0, 1, 2, and onward from successive position lists leaves a common value only when the phrase appears.

Combination with standard queries:
- [[blog-aakash-japi-implementing-a-search-engine-with-ranking-in-python]] suggests parsing quoted phrase fragments alongside ordinary query terms and intersecting their result sets.

## Counterevidence & Qualifications
The source covers exact adjacent phrase matching only. It does not handle proximity queries, slop, stemming-aware phrases, stopword-sensitive phrase indexing, tokenization complications, or ranked phrase features beyond returning matches into the ranking stage.

## What Changed
- Created the concept to represent ordered exact-match search over token positions.

## Related Concepts
- [[InvertedIndex]] - phrase queries use its per-document position lists.
- [[TFIDFRanking]] - phrase-query matches can be ranked after candidate retrieval.
- [[NaturalLanguageProcessing]] - query sanitization and tokenization shape phrase boundaries.
- [[SemanticSearch]] - semantic retrieval may find related meaning without exact phrase order.

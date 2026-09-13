---
title: "Bag-of-Words Model"
type: concept
tags: [information-retrieval, natural-language-processing, vectors]
sources:
  - blog-aakash-japi-implementing-a-search-engine-with-ranking-in-python
last_updated: 2026-09-14
knowledge_schema: synthesis-v1
---

## Definition
[[BagOfWordsModel]] represents a document as an unordered collection of token counts, usually as a vector whose dimensions correspond to vocabulary terms.

## Current Synthesis
The source presents bag-of-words as the document representation behind term-frequency and tf-idf ranking. A document becomes a vector of term counts, and in a multi-document corpus each vector can share the same vocabulary dimensions so documents and queries can be compared. This representation is useful for simple ranking, but it discards word order, which is why the tutorial separately stores token positions for phrase search.

## Key Claims
- Bag-of-words treats term counts as the representation of a document.
- Shared vocabulary dimensions let multiple documents and queries be compared as vectors.
- Vector normalization can prevent repeated copies of the same text from dominating by magnitude alone.
- The model ignores order, so it cannot by itself answer phrase queries.

## Evidence
Token-count representation:
- [[blog-aakash-japi-implementing-a-search-engine-with-ranking-in-python]] describes term frequency as counting each token in a document.

Shared vector dimensions:
- [[blog-aakash-japi-implementing-a-search-engine-with-ranking-in-python]] represents every document in an N-dimensional vector space where N is the number of unique terms in the collection.

Normalization:
- [[blog-aakash-japi-implementing-a-search-engine-with-ranking-in-python]] normalizes vectors so repeated text does not automatically create a different representation.

Order limitation:
- [[blog-aakash-japi-implementing-a-search-engine-with-ranking-in-python]] explicitly uses position-aware indexing for phrase queries because bag-of-words term frequency does not account for order.

## Counterevidence & Qualifications
The source presents bag-of-words as useful and widely used, but also notes that it is not fully accurate because order is ignored. It does not cover n-grams, syntax, semantics, embeddings, transformer representations, or domain-specific feature engineering.

## What Changed
- Created the concept to capture count-vector document representation in classic search ranking.

## Related Concepts
- [[TFIDFRanking]] - tf-idf weights bag-of-words vector entries.
- [[PhraseQuery]] - phrase queries compensate for bag-of-words order loss.
- [[NaturalLanguageProcessing]] - bag-of-words is a basic NLP text representation.
- [[Embeddings]] - embeddings are a later vector representation that can encode meaning beyond raw counts.

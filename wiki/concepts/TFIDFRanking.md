---
title: "TF-IDF Ranking"
type: concept
tags: [search, information-retrieval, ranking]
sources:
  - blog-aakash-japi-implementing-a-search-engine-with-ranking-in-python
last_updated: 2026-09-14
knowledge_schema: synthesis-v1
---

## Definition
[[TFIDFRanking]] ranks documents by weighting terms according to how often they appear in a document and how uncommon they are across the corpus.

## Current Synthesis
The source uses tf-idf as the ranking layer after an inverted index has found candidate documents. Term frequency captures how strongly a term appears in a document, but by itself it overvalues common words and document length. Inverse document frequency reduces the weight of terms that appear broadly across the collection, and cosine similarity then compares the query vector to document vectors while reducing the effect of vector magnitude.

## Key Claims
- Ranking is a separate layer from matching; the index can find candidates before scoring them.
- Term frequency alone is weak because common words can create false similarity.
- Inverse document frequency downweights corpus-common terms, especially after log scaling.
- Document and query vectors can be compared with cosine similarity to rank results.
- TF and IDF values can be precomputed because they do not depend on a specific query.

## Evidence
Separate ranking layer:
- [[blog-aakash-japi-implementing-a-search-engine-with-ranking-in-python]] describes indexing and querying first, then adds ranking as the final step.

Term-frequency limitation:
- [[blog-aakash-japi-implementing-a-search-engine-with-ranking-in-python]] argues that treating every term as equally important makes common words misleading.

IDF correction:
- [[blog-aakash-japi-implementing-a-search-engine-with-ranking-in-python]] defines inverse document frequency as a corpus-level correction and adds a natural log to soften the penalty.

Cosine similarity comparison:
- [[blog-aakash-japi-implementing-a-search-engine-with-ranking-in-python]] ranks candidate documents by computing similarity between the query vector and each document vector.

Precomputation:
- [[blog-aakash-japi-implementing-a-search-engine-with-ranking-in-python]] notes that term and inverse-document-frequency quantities should be computed in advance.

## Counterevidence & Qualifications
The source gives theory rather than ranking code in the article body, and its definitions are simplified for didactic use. It does not address BM25, link analysis, learning-to-rank, embeddings, click feedback, field weighting, freshness, spam, personalization, or evaluation metrics.

## What Changed
- Created the concept to represent classic term-statistic search ranking.

## Related Concepts
- [[BagOfWordsModel]] - tf-idf uses bag-of-words document and query vectors.
- [[InvertedIndex]] - tf-idf ranking scores candidates retrieved from the index.
- [[PhraseQuery]] - phrase matches can be passed into the same ranking stage.
- [[SemanticSearch]] - semantic search often replaces or complements tf-idf with embedding similarity.

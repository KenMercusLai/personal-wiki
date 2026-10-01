---
title: "TF-IDF Ranking"
type: concept
tags: [search, information-retrieval, ranking]
sources:
  - blog-aakash-japi-implementing-a-search-engine-with-ranking-in-python
  - per-harald-borgen-boosting-sales-with-machine-learning
last_updated: 2026-10-01
knowledge_schema: synthesis-v1
---

## Definition
[[TFIDFRanking]] ranks documents by weighting terms according to how often they appear in a document and how uncommon they are across the corpus.

## Current Synthesis
The sources use tf-idf as a general weighting transform over count vectors. In search, it follows candidate retrieval and emphasizes terms that are frequent within a document but uncommon across the collection before cosine-similarity ranking. In Xeneta's classification experiment, the same transform supplies weighted company-description features to a Random Forest, showing that tf-idf can support prediction as well as document ranking.

## Key Claims
- Ranking is a separate layer from matching; the index can find candidates before scoring them.
- Term frequency alone is weak because common words can create false similarity.
- Inverse document frequency downweights corpus-common terms, especially after log scaling.
- Document and query vectors can be compared with cosine similarity to rank results.
- TF and IDF values can be precomputed because they do not depend on a specific query.
- TF-idf vectors can also be inputs to a supervised classifier rather than a final ranking score.

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

Classification features:
- [[per-harald-borgen-boosting-sales-with-machine-learning]] applies an L1-normalized TfidfTransformer to company-description count vectors before training its lead classifier.

## Counterevidence & Qualifications
The search source gives simplified theory rather than ranking code in the article body and does not address BM25, link analysis, learning-to-rank, embeddings, click feedback, field weighting, freshness, spam, personalization, or evaluation metrics. The Xeneta source does not isolate tf-idf's contribution, compare it with raw counts, or test alternative normalizations, so it supports the existence of the feature pipeline rather than a causal claim that tf-idf produced the reported accuracy.

## What Changed
- Created the concept to represent classic term-statistic search ranking.
- Added tf-idf's use as a supervised classification feature transform and bounded the evidence for its effect.

## Related Concepts
- [[BagOfWordsModel]] - tf-idf uses bag-of-words document and query vectors.
- [[InvertedIndex]] - tf-idf ranking scores candidates retrieved from the index.
- [[PhraseQuery]] - phrase matches can be passed into the same ranking stage.
- [[SemanticSearch]] - semantic search often replaces or complements tf-idf with embedding similarity.
- [[TextClassification]] - uses tf-idf-weighted document vectors as classifier inputs in the Xeneta case.

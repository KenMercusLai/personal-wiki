---
title: "Bag-of-Words Model"
type: concept
tags: [information-retrieval, natural-language-processing, vectors]
sources:
  - blog-aakash-japi-implementing-a-search-engine-with-ranking-in-python
  - per-harald-borgen-boosting-sales-with-machine-learning
last_updated: 2026-10-01
knowledge_schema: synthesis-v1
---

## Definition
[[BagOfWordsModel]] represents a document as an unordered collection of token counts, usually as a vector whose dimensions correspond to vocabulary terms.

## Current Synthesis
The sources use bag-of-words for both retrieval ranking and supervised classification. A document becomes a vector of token counts over shared vocabulary dimensions; tf-idf can then reweight those dimensions before comparing queries or training a classifier. The search tutorial exposes the loss of word order by adding positional storage for phrase queries, while the Xeneta experiment partly restores short-range order through one-to-three-word n-grams and limits the vocabulary to frequent features.

## Key Claims
- Bag-of-words treats term counts as the representation of a document.
- Shared vocabulary dimensions let multiple documents and queries be compared as vectors.
- Vector normalization can prevent repeated copies of the same text from dominating by magnitude alone.
- The model ignores order, so it cannot by itself answer phrase queries.
- Vocabulary limits and n-gram ranges change which lexical patterns the representation can expose to a classifier.

## Evidence
Token-count representation:
- [[blog-aakash-japi-implementing-a-search-engine-with-ranking-in-python]] describes term frequency as counting each token in a document.

Shared vector dimensions:
- [[blog-aakash-japi-implementing-a-search-engine-with-ranking-in-python]] represents every document in an N-dimensional vector space where N is the number of unique terms in the collection.

Normalization:
- [[blog-aakash-japi-implementing-a-search-engine-with-ranking-in-python]] normalizes vectors so repeated text does not automatically create a different representation.

Order limitation:
- [[blog-aakash-japi-implementing-a-search-engine-with-ranking-in-python]] explicitly uses position-aware indexing for phrase queries because bag-of-words term frequency does not account for order.

Classification use:
- [[per-harald-borgen-boosting-sales-with-machine-learning]] uses CountVectorizer, a capped vocabulary, and tuned one-to-three-word grams before Random Forest lead classification.

## Counterevidence & Qualifications
The search source presents bag-of-words as useful but incomplete because order is ignored. The Xeneta source adds n-grams and stemming but does not inspect learned features, compare preprocessing choices systematically, or show whether lexical associations transfer beyond its dataset. Neither source covers syntax-aware representations or a controlled comparison with embeddings and transformer features.

## What Changed
- Created the concept to capture count-vector document representation in classic search ranking.
- Extended the synthesis from retrieval to supervised classification and added vocabulary and n-gram choices as representation controls.

## Related Concepts
- [[TFIDFRanking]] - tf-idf weights bag-of-words vector entries.
- [[PhraseQuery]] - phrase queries compensate for bag-of-words order loss.
- [[NaturalLanguageProcessing]] - bag-of-words is a basic NLP text representation.
- [[Embeddings]] - embeddings are a later vector representation that can encode meaning beyond raw counts.
- [[TextClassification]] - second use case in which bag-of-words vectors become predictive features.

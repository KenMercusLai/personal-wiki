---
title: "N-Gram Language Model"
type: concept
tags: [nlp, probability, python]
sources:
  - a-comprehensive-guide-to-build-your-own-language-model-in-python
last_updated: 2026-09-13
knowledge_schema: synthesis-v1
---

## Definition
[[NGramLanguageModel]] is a statistical language model that predicts a token from a fixed-size local history of the previous `n-1` tokens.

## Current Synthesis
The source introduces unigrams, bigrams, and trigrams as increasingly long token sequences, then uses the Markov assumption to make language probability computable from local context. Its Reuters example builds a trigram model: count each `(w1, w2) -> w3` occurrence, normalize counts into probabilities, and repeatedly sample a next word to generate text. The model produces plausible but slightly odd news-style lines, making both the power and brittleness of N-gram modeling visible.

## Key Claims
- N-grams represent language as fixed-length token sequences.
- The Markov assumption approximates full history with a short recent context.
- A trigram model can estimate the next word from the previous two words.
- Count normalization turns corpus co-occurrences into conditional probabilities.
- Iterative next-word sampling can generate coherent local text even without deep language understanding.
- N-gram models become expensive and sparse as N increases.

## Evidence
- Sequence definitions: [[a-comprehensive-guide-to-build-your-own-language-model-in-python]] defines unigrams, bigrams, and trigrams using a data-science sentence example.
- Markov simplification: [[a-comprehensive-guide-to-build-your-own-language-model-in-python]] replaces full history with the immediately preceding word in the bigram explanation and notes larger fixed histories are possible.
- Reuters implementation: [[a-comprehensive-guide-to-build-your-own-language-model-in-python]] uses NLTK trigrams over Reuters sentences, counts third-word frequencies, and normalizes by total counts for each two-word history.
- Screenshot evidence: [[a-comprehensive-guide-to-build-your-own-language-model-in-python]] shows probability dictionaries for "today the" and "the price" plus generated Reuters-like lines beginning with "today".
- Limitations: [[a-comprehensive-guide-to-build-your-own-language-model-in-python]] says higher N raises RAM/computation needs and unseen words receive zero probability.

## Counterevidence & Qualifications
The tutorial's N-gram model is intentionally basic. It omits smoothing, unknown-token treatment, train/test evaluation, perplexity, and modern tokenizer issues, so it should be read as a teaching implementation rather than a competitive NLP system.

## What Changed
- Created an N-gram language-model concept page from the Reuters trigram example.

## Related Concepts
- [[StatisticalLanguageModel]] - N-grams are a statistical language-model family.
- [[LanguageModeling]] - N-grams estimate sequence probabilities for language modeling.
- [[NaturalLanguageGeneration]] - repeated next-token sampling can generate text.

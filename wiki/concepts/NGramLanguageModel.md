---
title: "N-Gram Language Model"
type: concept
tags: [nlp, probability, python]
sources:
  - a-comprehensive-guide-to-build-your-own-language-model-in-python
  - what-is-chatgpt-doing-and-why-does-it-work
last_updated: 2026-09-17
knowledge_schema: synthesis-v1
---

## Definition
[[NGramLanguageModel]] is a statistical language model that predicts a token from a fixed-size local history of the previous `n-1` tokens.

## Current Synthesis
Both sources use n-grams as the honest baseline for language modeling, and the ChatGPT essay uses them as the ladder that shows why counting is not enough. The tutorial introduces unigrams, bigrams, and trigrams, applies the Markov assumption to make probability computable from local context, and implements a trigram model over the Reuters corpus by counting `(w1, w2) -> w3` occurrences, normalising into conditional probabilities, and sampling repeated next words to generate news-like lines.

The essay runs the same argument in both directions. Downwards, it starts from letters: counting letters in a Wikipedia article gives a frequency distribution, sampling those frequencies produces pseudo-words, adding spaces and then matching English word-length distributions improves them, and moving to 2-gram letter probabilities makes combinations like "q" followed by "u" visible in a heat map. Upwards, it moves to whole words, sampling from unigram frequencies to produce nonsense and then from word bigrams to produce five samples that start from "cat" and look slightly more sensible. The essay's punchline is combinatorial: with about 40,000 common English words there are already 1.6 billion possible 2-grams and 60 trillion 3-grams, so even the observed web and book corpora cannot estimate their probabilities, and by the time sequences reach twenty words the count of possibilities exceeds the number of particles in the universe. The conclusion is not that n-grams are wrong but that they demonstrate the need for a model that estimates unseen sequences.

## Key Claims
- N-grams represent language as fixed-length token sequences.
- The Markov assumption approximates full history with a short recent context.
- A trigram model can estimate the next word from the previous two words.
- Count normalization turns corpus co-occurrences into conditional probabilities.
- Iterative next-word sampling can generate locally coherent text even without deep language understanding.
- N-gram models become expensive and sparse as N increases, and the sparsity of long n-grams is a counting problem rather than a data-collection problem, because the number of possible sequences grows faster than any corpus can.
- The same ladder works at character level: letter frequencies, then letter 2-grams, then longer sequences produce progressively more realistic pseudo-words.

## Evidence
- Sequence definitions: [[a-comprehensive-guide-to-build-your-own-language-model-in-python]] defines unigrams, bigrams, and trigrams using a data-science sentence example.
- Markov simplification: [[a-comprehensive-guide-to-build-your-own-language-model-in-python]] replaces full history with the immediately preceding word in the bigram explanation and notes larger fixed histories are possible.
- Reuters implementation: [[a-comprehensive-guide-to-build-your-own-language-model-in-python]] uses NLTK trigrams over Reuters sentences, counts third-word frequencies, and normalizes by total counts for each two-word history.
- Screenshot evidence: [[a-comprehensive-guide-to-build-your-own-language-model-in-python]] shows probability dictionaries for "today the" and "the price" plus generated Reuters-like lines beginning with "today".
- Limitations: [[a-comprehensive-guide-to-build-your-own-language-model-in-python]] says higher N raises RAM/computation needs and unseen words receive zero probability.
- Letter-level ladder: [[what-is-chatgpt-doing-and-why-does-it-work]] shows letter counts for Wikipedia's "cats" and "dogs" articles, English letter frequencies from e at 12.7% down to z at 0.074%, and pseudo-words generated at increasing realism.
- Letter 2-grams: [[what-is-chatgpt-doing-and-why-does-it-work]] shows a letter-pair probability heat map in which the "q" column is blank except on the "u" row.
- Word-level samples: [[what-is-chatgpt-doing-and-why-does-it-work]] shows nonsense generated from word frequencies and five bigram continuations from "cat".
- Combinatorial limit: [[what-is-chatgpt-doing-and-why-does-it-work]] states that 40,000 common English words give 1.6 billion possible 2-grams and 60 trillion 3-grams, so their probabilities cannot be estimated from available text.
- Conclusion: [[what-is-chatgpt-doing-and-why-does-it-work]] says the answer is a model that estimates the probability of sequences never explicitly seen, which is what a large language model is for.

## Counterevidence & Qualifications
The tutorial's N-gram model is intentionally basic. It omits smoothing, unknown-token treatment, train/test evaluation, perplexity, and modern tokenizer issues, so it should be read as a teaching implementation rather than a competitive NLP system. The essay's n-gram arguments are illustrative and use rounded counts rather than corpus measurements, and its sparsity argument applies to exact sequence counting rather than to smoothed or interpolated statistical models, which the source does not discuss.

## What Changed
- Created an N-gram language-model concept page from the Reuters trigram example.
- Added the character-level ladder and the combinatorial sparsity argument from the ChatGPT explanation.

## Related Concepts
- [[StatisticalLanguageModel]] - n-grams are a statistical language-model family.
- [[LanguageModeling]] - n-grams estimate sequence probabilities for language modeling.
- [[NaturalLanguageGeneration]] - repeated next-token sampling can generate text.
- [[NeuralLanguageModel]] - neural models estimate probabilities for sequences n-grams cannot count.
- [[AttentionMechanism]] - attention generalises the fixed local context that n-grams use.

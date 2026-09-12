---
title: "Reuters Corpus"
type: entity
tags: [dataset, nlp, corpus]
sources:
  - a-comprehensive-guide-to-build-your-own-language-model-in-python
last_updated: 2026-09-13
knowledge_schema: synthesis-v1
---

## Overview
[[ReutersCorpus]] is the news-text dataset used in the tutorial's basic trigram language model.

## Current Profile
The source describes the Reuters corpus as 10,788 news documents totaling about 1.3 million words. It is used as a compact corpus for demonstrating how trigram counts can become next-word probabilities and generated text.

## Key Characteristics
- Provides sentence-level news text for NLTK-based examples.
- Supplies enough repeated phrase patterns for a small trigram model.
- Produces generated output that feels news-like but slightly awkward.
- Functions as a teaching dataset rather than a benchmark in the article.

## Evidence
- Dataset description: [[a-comprehensive-guide-to-build-your-own-language-model-in-python]] describes Reuters as 10,788 news documents with 1.3 million words.
- Training role: [[a-comprehensive-guide-to-build-your-own-language-model-in-python]] iterates through Reuters sentences to count trigrams.
- Output evidence: [[a-comprehensive-guide-to-build-your-own-language-model-in-python]] shows generated lines beginning with "today" and comments that they are coherent but slightly off because Reuters is mostly news.
- Scope: [[a-comprehensive-guide-to-build-your-own-language-model-in-python]] uses Reuters only for the statistical model section.

## Qualifications
The source does not discuss Reuters corpus licensing, train/test splits, categories, preprocessing conventions, or evaluation metrics.

## What Changed
- Created an entity profile for the Reuters corpus as a tutorial dataset.

## Relationships
- [[NLTK]] - toolkit used to access Reuters sentences.
- [[NGramLanguageModel]] - statistical model trained on Reuters trigrams.
- [[StatisticalLanguageModel]] - Reuters supplies corpus counts for the statistical example.

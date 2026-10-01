---
title: "Text Classification"
type: concept
tags: [machine-learning, natural-language-processing, classification]
sources:
  - per-harald-borgen-boosting-sales-with-machine-learning
last_updated: 2026-10-01
knowledge_schema: synthesis-v1
---

## Definition
[[TextClassification]] assigns one or more predefined labels to a text using rules or a learned model; in this source, the labels are qualified and disqualified sales prospects.

## Current Synthesis
The Xeneta case frames classification as an end-to-end decision-support system rather than an isolated algorithm. Company names must first be resolved to likely websites and descriptions, humans must supply task-specific labels, text must be cleaned and transformed into numeric features, and the classifier must then be evaluated against the intended sales workflow. The reported accuracy suggests that simple count-based features can expose domain vocabulary, but it does not reveal which prospects are missed, which false positives consume sales time, or whether performance transfers beyond the balanced historical dataset.

## Key Claims
- Useful text classification depends on obtaining representative text and task-relevant labels before model selection.
- Cleaning, stemming, stop-word removal, count vectorization, and tf-idf can form a simple feature pipeline for prose.
- Model comparisons require held-out data, but a single accuracy score does not describe operational error costs.
- Balanced experimental classes can simplify testing while differing from the prevalence encountered in real prospect lists.
- Classification can triage human review without proving that autonomous decisions are appropriate.

## Evidence
- Label construction: [[per-harald-borgen-boosting-sales-with-machine-learning]] builds the dataset from 1,000 customers and 1,000 manually disqualified companies.
- Feature pipeline: [[per-harald-borgen-boosting-sales-with-machine-learning]] applies regex cleaning, stemming, stop-word removal, bag-of-words vectorization, and tf-idf.
- Model comparison: [[per-harald-borgen-boosting-sales-with-machine-learning]] reports stronger test accuracy for Random Forest than K-nearest neighbors on a 70/30 split.
- Workflow role: [[per-harald-borgen-boosting-sales-with-machine-learning]] proposes rough sorting before sales representatives perform qualification.

## Counterevidence & Qualifications
The source reports one 2016 experiment with 2,000 labeled examples, one split, and accuracy as the primary metric. It provides no cross-validation, temporal holdout, confusion matrix, calibration, precision, recall, class-prevalence analysis, baseline, ablation, feature inspection, or production outcome. URL resolution and third-party descriptions can introduce upstream errors, while historical customers and one person's rejected prospects may encode selection and labeling bias.

## What Changed
- Created the concept around a bounded lead-triage case and made the data, evaluation, and human-review limits explicit.

## Related Concepts
- [[NaturalLanguageProcessing]] - supplies preprocessing and representation methods for the input text.
- [[BagOfWordsModel]] - converts descriptions into count-based feature vectors.
- [[TFIDFRanking]] - reweights count features by corpus frequency before classification.
- [[SQLFirstBusinessAutomation]] - offers a transparent rules-first alternative when simple business conditions are sufficient.

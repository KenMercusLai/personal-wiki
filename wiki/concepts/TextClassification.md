---
title: "Text Classification"
type: concept
tags: [machine-learning, natural-language-processing, classification]
sources:
  - per-harald-borgen-boosting-sales-with-machine-learning
  - vane-data-jev-building-an-end-to-end-voice-analytics-pipeline
last_updated: 2026-10-07
knowledge_schema: synthesis-v1
---

## Definition
[[TextClassification]] assigns one or more predefined labels to text using rules or a learned model, with useful operation depending on category boundaries, representative inputs, evaluation, and treatment of uncertain or failed cases.

## Current Synthesis
The sources frame classification as an end-to-end decision-support system rather than an isolated algorithm. The Xeneta case acquires company descriptions, constructs human labels, engineers count-based features, and trains a supervised binary model; the banking case transcribes audio, checks transcript quality, defines 14 intent boundaries, compares keywords with an external semantic judge, and maps predicted intents to queues. Together they show that the classifier's operational meaning comes from the input pipeline, label definitions, error handling, downstream action, and evaluation denominator. Neither case establishes production value: Xeneta reports only a limited held-out accuracy result, while the voice example ships no measured scores at all.

## Key Claims
- Useful text classification depends on representative text, explicit task boundaries, and labels or evaluation targets before model selection.
- Rules and learned or semantic models can operate on the same text, but fair comparison requires common upstream inputs and denominators.
- Upstream acquisition, transcription, and quality failures are part of classification performance rather than removable preprocessing noise.
- Metrics should reflect the workflow: class-level measures expose uneven errors, while coarser outcomes such as queue accuracy may remain correct despite label error.
- Confidence thresholds and typed outputs can support triage, but they require calibration and do not by themselves justify autonomous action.
- Classification can prioritize human work while preserving a distinct review decision for the prediction itself.

## Evidence
- Task construction: [[per-harald-borgen-boosting-sales-with-machine-learning]] derives binary labels from customers and manually rejected prospects; [[vane-data-jev-building-an-end-to-end-voice-analytics-pipeline]] defines 14 banking intents with explicit exclusions and queue mappings.
- Input pipeline: [[per-harald-borgen-boosting-sales-with-machine-learning]] resolves companies to descriptions and builds count/tf-idf features; [[vane-data-jev-building-an-end-to-end-voice-analytics-pipeline]] decodes audio, transcribes it, and gates suspicious text before classification.
- Comparison discipline: [[per-harald-borgen-boosting-sales-with-machine-learning]] compares two learned models on one split; [[vane-data-jev-building-an-end-to-end-voice-analytics-pipeline]] compares keywords and Jev on identical Whisper transcripts while retaining failed records.
- Workflow metrics: [[vane-data-jev-building-an-end-to-end-voice-analytics-pipeline]] separates intent accuracy, macro-F1, and queue accuracy because business routing can survive some fine-label errors.
- Human boundary: both [[per-harald-borgen-boosting-sales-with-machine-learning]] and [[vane-data-jev-building-an-end-to-end-voice-analytics-pipeline]] position classification as reviewed decision support rather than a demonstrated autonomous action system.

## Counterevidence & Qualifications
The Xeneta source reports one 2016 experiment with 2,000 labeled examples, one split, and accuracy as the primary metric. It provides no cross-validation, temporal holdout, confusion matrix, calibration, class-prevalence analysis, or production outcome; upstream URL resolution and historical labels may be biased. The voice source publishes no results, uses a fixed development subset that may overlap model training data, and lacks labels for most judgment fields. Its single-utterance recordings cannot validate full-call state or speaker separation, and its `0.5` follow-up threshold is uncalibrated. These cases illustrate architectures and evaluation questions, not a general performance comparison between classical models, keywords, and external semantic services.

## What Changed
- Expanded the concept from one supervised lead-triage case to include semantic intent routing, common-input comparisons, failure-inclusive denominators, workflow-specific metrics, and calibration limits.

## Related Concepts
- [[NaturalLanguageProcessing]] - supplies preprocessing and representation methods for the input text.
- [[BagOfWordsModel]] - converts descriptions into count-based feature vectors.
- [[TFIDFRanking]] - reweights count features by corpus frequency before classification.
- [[SQLFirstBusinessAutomation]] - offers a transparent rules-first alternative when simple business conditions are sufficient.
- [[VoiceAnalyticsPipeline]] - embeds intent classification inside audio processing, quality control, SQL shaping, evaluation, and review.

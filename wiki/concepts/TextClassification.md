---
title: "Text Classification"
type: concept
tags: [machine-learning, natural-language-processing, classification]
sources:
  - per-harald-borgen-boosting-sales-with-machine-learning
  - vane-data-jev-building-an-end-to-end-voice-analytics-pipeline
  - jev-kuhung
last_updated: 2026-10-25
knowledge_schema: synthesis-v1
---

## Definition
[[TextClassification]] assigns one or more predefined labels or bounded scores to text using rules or a learned model, with useful operation depending on category boundaries, representative inputs, evaluation, uncertainty handling, and downstream action.

## Current Synthesis
The sources frame classification as an end-to-end decision system rather than an isolated algorithm. The Xeneta case acquires company descriptions, constructs human labels, engineers count-based features, and trains a fixed binary model. The banking case transcribes audio, checks text quality, defines 14 intent boundaries, compares keywords with [[Jev]], maps predictions to queues, and preserves human review. The Jev survey adds a runtime-flexible [[SingleStepDecisionModel]] that accepts candidate choices, scores, and binary questions without autoregressive output. Together they show a continuum from fixed-label classical models through rules to dynamic semantic classifiers, but the durable requirements stay the same: define the task, include upstream failures, test representative labeled data, measure the workflow outcome, calibrate uncertainty, and constrain the authority granted to a prediction.

## Key Claims
- Representative text, explicit class boundaries, and labels or evaluation targets matter before model selection.
- Rules, fixed-label learned models, and runtime-candidate semantic models can operate on the same task, but fair comparison requires common upstream inputs, denominators, and downstream objectives.
- Upstream acquisition, transcription, and quality failures are part of classification performance rather than removable preprocessing noise.
- Metrics should reflect class-level error and workflow consequences; agreement with another model and syntactically valid output are not accuracy.
- Candidate wording, ordering, irrelevant alternatives, and large flat taxonomies can affect dynamic semantic classification and should be tested as part of the input contract.
- Confidence thresholds can support triage only after representative calibration and drift checks, and they do not by themselves justify autonomous action.
- Classification can prioritize or route work while deterministic policy and human or stronger-model review preserve a distinct authority boundary.

## Evidence
- Task construction: [[per-harald-borgen-boosting-sales-with-machine-learning]] derives binary labels from customers and manually rejected prospects; [[vane-data-jev-building-an-end-to-end-voice-analytics-pipeline]] defines 14 intents with explicit exclusions and queue mappings; [[jev-kuhung]] describes runtime candidate sets and hierarchical pruning for large taxonomies.
- Input pipeline: [[per-harald-borgen-boosting-sales-with-machine-learning]] resolves companies to descriptions and builds count/tf-idf features; [[vane-data-jev-building-an-end-to-end-voice-analytics-pipeline]] decodes audio, transcribes it, and gates suspicious text before classification.
- Comparison discipline: [[per-harald-borgen-boosting-sales-with-machine-learning]] compares two learned models on one split; [[vane-data-jev-building-an-end-to-end-voice-analytics-pipeline]] proposes comparing keywords and Jev on identical Whisper transcripts while retaining failures; [[jev-kuhung]] exposes why replayed cross-model timing and model-agreement figures are not accuracy benchmarks.
- Uncertainty and perturbation: [[jev-kuhung]] reports overconfidence from raw open-model logits, candidate-order sensitivity, and irrelevant-option interference; [[vane-data-jev-building-an-end-to-end-voice-analytics-pipeline]] uses an explicitly uncalibrated follow-up threshold and therefore keeps every record under review.
- Workflow boundary: [[per-harald-borgen-boosting-sales-with-machine-learning]], [[vane-data-jev-building-an-end-to-end-voice-analytics-pipeline]], and [[jev-kuhung]] position classification as prioritization, routing, or gating embedded in a larger process; none demonstrates safe autonomous high-consequence action in production.

## Counterevidence & Qualifications
The Xeneta source reports one 2016 experiment with 2,000 labeled examples, one split, and accuracy as the primary metric, without cross-validation, calibration, class-prevalence analysis, drift, or production outcomes. The voice source publishes no results, uses a fixed development subset that may overlap model training data, lacks labels for most judgment fields, and cannot validate full-call state or speaker separation. The Jev survey combines vendor statements, pre-recorded comparisons, community reproductions, selected third-party tests, and hypothetical economics; Jev's implementation and calibration data are undisclosed. A conventional classifier can be faster and easier to validate when labels are stable, while a generative model may be necessary for open-ended output or multi-step reasoning. None of the sources establishes a universal model choice or threshold.

## What Changed
- Added runtime-candidate single-step classifiers, candidate-set perturbation, shared-prefix fan-out, and explicit prediction-versus-authority separation.
- Narrowed performance claims by distinguishing model agreement, replay latency, probability calibration, and task accuracy.

## Related Concepts
- [[NaturalLanguageProcessing]] - supplies preprocessing and representation methods for input text.
- [[BagOfWordsModel]] - converts descriptions into fixed count-based feature vectors.
- [[TFIDFRanking]] - reweights count features by corpus frequency before classical classification.
- [[SingleStepDecisionModel]] - provides bounded runtime-defined judgments without autoregressive text generation.
- [[OracleRouting]] - escalates uncertain or high-risk classifications to a stronger evaluator.
- [[VoiceAnalyticsPipeline]] - embeds intent classification inside audio processing, quality control, SQL shaping, evaluation, and review.

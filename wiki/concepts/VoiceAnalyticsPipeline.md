---
title: "Voice Analytics Pipeline"
type: concept
tags: [voice, data-pipelines, classification, human-in-the-loop]
sources:
  - vane-data-jev-building-an-end-to-end-voice-analytics-pipeline
last_updated: 2026-10-07
knowledge_schema: synthesis-v1
---

## Definition
A [[VoiceAnalyticsPipeline]] turns recordings into traceable, structured decision-support fields through audio preparation, speech recognition, quality control, semantic judgment, deterministic shaping, evaluation, and review.

## Current Synthesis
The banking example shows why voice analytics is more than transcription. Useful routing requires preserving record identity, checking the waveform and transcript, interpreting paraphrased intent and unresolved state, converting judgments into stable business columns, and retaining failures for review and evaluation. The strongest design principle is to treat semantic judgment as one bounded stage inside a data system: deterministic checks control admission, explicit questions constrain outputs, SQL applies transparent mappings and thresholds, and human review remains separate from whether customer work is still pending.

## Key Claims
- End-to-end quality depends on audio decoding, transcription, semantic judgment, field shaping, and review rather than any single model call.
- Stable record identity and error-preserving rows make failures auditable and prevent success-only evaluation.
- Transcript quality checks should gate semantic inference without removing problematic records from downstream accounting.
- Explicit intent boundaries and typed questions produce more operationally usable fields than free-form summaries or keyword matches alone.
- Human follow-up status and model-output review are different decisions and should be represented separately.
- Evaluation must share the same upstream transcript, retain every selected record, and distinguish fine-grained intent accuracy from queue accuracy.

## Evidence
- Stage architecture: [[vane-data-jev-building-an-end-to-end-voice-analytics-pipeline]] carries audio through CPU decode, GPU Whisper, checks, [[Jev]], SQL, Parquet output, and a review CSV.
- Traceability and gating: [[vane-data-jev-building-an-end-to-end-voice-analytics-pipeline]] derives a stable record ID, propagates errors, and skips semantic calls only for failed or suspicious transcripts.
- Operational schema: [[vane-data-jev-building-an-end-to-end-voice-analytics-pipeline]] emits intent, queue, urgency, dissatisfaction, follow-up, and review fields from explicit questions and SQL rules.
- Evaluation discipline: [[vane-data-jev-building-an-end-to-end-voice-analytics-pipeline]] compares methods on common Whisper text, preserves the selected ID set, and reports intent and queue metrics separately.

## Counterevidence & Qualifications
The source does not establish that the pipeline improves routing. It ships no measured scores, throughput, cost, calibration, or production outcome, and the fixed development subset may overlap model training data. Its short single-utterance recordings cannot validate multi-turn state, speaker roles, resolved requests, or complete-call urgency and dissatisfaction; all segments are labeled caller, every result requires review, and no banking action is automated.

## What Changed
- Created the concept around a traceable audio-to-decision-support architecture with explicit failure, evaluation, privacy, and human-review boundaries.

## Related Concepts
- [[TextClassification]] - intent assignment is the bounded label-selection stage within the pipeline.
- [[OracleRouting]] - review routing should distinguish automation uncertainty from the customer's unresolved work.
- [[SQLFirstBusinessAutomation]] - deterministic SQL converts model outputs into queues, thresholds, and review reasons.
- [[NaturalLanguageProcessing]] - transcription and semantic interpretation supply the language-processing core.

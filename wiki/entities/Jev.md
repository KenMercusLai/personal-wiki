---
title: "Jev"
type: entity
tags: [ai, classification, decision-support]
sources:
  - vane-data-jev-building-an-end-to-end-voice-analytics-pipeline
last_updated: 2026-10-07
knowledge_schema: synthesis-v1
---

## Overview
[[Jev]] is an external TypeSafe AI service presented as returning typed semantic judgments and confidence probabilities for explicit questions over unstructured state.

## Current Profile
The voice-routing example uses Jev as a non-generative decision operator. Each eligible transcript row sends all five questions in one request, using Choice for intent, Score for bounded ordinal ratings, and Noul for probability-like yes/no judgments. Vane Data executors reuse clients across batches, validate each response against its request, and write it back to the row before SQL extracts business fields.

## Key Characteristics
- Accepts question definitions and unstructured state rather than generating free-form text.
- Exposes Choice, Score, and Noul as the three question primitives described by the source.
- Returns all requested answers in one per-row call with typed values and confidence probabilities.
- Runs as an external service; local executors manage request concurrency and response alignment rather than hosting the model.
- Is positioned for high-frequency classification and rating, but the banking example keeps every result under human review.

## Evidence
- Typed interface: [[vane-data-jev-building-an-end-to-end-voice-analytics-pipeline]] defines intent, urgency, dissatisfaction, follow-up, and input-sufficiency questions with three primitives.
- Execution lifecycle: [[vane-data-jev-building-an-end-to-end-voice-analytics-pipeline]] separates plan registration from per-row execution and validated response-column writes.
- Concurrency: [[vane-data-jev-building-an-end-to-end-voice-analytics-pipeline]] configures four actors with eight in-flight requests each while warning that configuration is not measured throughput.
- Workflow boundary: [[vane-data-jev-building-an-end-to-end-voice-analytics-pipeline]] skips failed transcripts and sends outputs to review rather than triggering banking operations.

## Qualifications
Latency, relative speed, and price figures in the article are vendor claims, not measurements from the demonstrated pipeline. The example publishes no Jev result scores, calibration analysis, independent test set, throughput, cost, or production outcomes. Transcript text leaves the local environment and may contain personal information even when raw audio and ground-truth labels are excluded.

## What Changed
- Created the initial profile around Jev's typed question primitives, per-row execution, response validation, and decision-support boundary.

## Relationships
- [[VaneData]] - provides the Relation operator and executor layer used to call Jev and align responses.
- [[VoiceAnalyticsPipeline]] - uses Jev to turn checked transcripts into structured routing and review fields.
- [[TextClassification]] - Jev performs bounded intent selection as one part of a larger classification pipeline.
- [[OracleRouting]] - confidence and input-sufficiency outputs can inform escalation, although this example requires review for every row.

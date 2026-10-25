---
title: "Single-Step Decision Model"
type: concept
tags: [ai, classification, inference, routing]
sources:
  - jev-kuhung
last_updated: 2026-10-25
knowledge_schema: synthesis-v1
---

## Definition
A [[SingleStepDecisionModel]] maps supplied context and a bounded decision schema directly to discrete choices, ordinal scores, or binary probabilities in one forward evaluation, without autoregressively generating an explanation.

## Current Synthesis
The source presents single-step decision models as a middle ground between fixed-label classical classifiers and free-form generative models. They can inherit a modern transformer's broad representation and long context while accepting runtime candidate sets, yet avoid iterative token decoding by reading candidate logits or a classification head. Their value is architectural rather than universal: they can make frequent bounded decisions cheap enough to place before a generative model, but safe automation still depends on label design, representative evaluation, probability calibration, deterministic policy, observability, and escalation.

## Key Claims
- Eliminating autoregressive output removes token-by-token decode latency and format parsing, but does not remove context-prefill cost.
- Shared-prefix KV caching can amortize long-context prefill across independent questions or candidates; dependent decisions still require sequential evaluation.
- Choice, ordinal score, and binary judgment cover many routing and gating tasks, while generation, explanation, and multi-step causal reasoning remain outside the architecture's natural scope.
- Candidate wording, order, and irrelevant alternatives can change scores, so a dynamic candidate set is part of the evaluated input rather than a neutral output schema.
- Confidence is operationally meaningful only after calibration on representative data and continued drift checks; raw Softmax magnitude is insufficient.
- Production use should separate prediction from authority through thresholds, deterministic rules, shadow comparison, logging, and fallback to a human or stronger model.

## Evidence
- Architecture and interface: [[jev-kuhung]] describes final-position logit projection and NLI heads as community reconstruction paths, alongside Jev's Choice, Score, and Noul primitives.
- Amortized inference: [[jev-kuhung]] reports latency scaling consistent with one long-context prefill shared across many questions, while also showing queueing at very large fan-out.
- Behavioral limits: [[jev-kuhung]] reports order sensitivity, irrelevant-option interference, weak multi-layer phishing performance, and overconfidence from uncalibrated open-model logits.
- Deployment controls: [[jev-kuhung]] recommends confidence tiers, deterministic composite scoring, hierarchical classification, shadow traffic, and generative or human escalation.

## Counterevidence & Qualifications
The evidence comes from one secondary technical article combining vendor statements, pre-recorded comparisons, community reverse engineering, selected third-party tests, and hypothetical production economics. Jev's implementation is not fully open, and community reproductions do not establish its architecture or calibration procedure. Reported latency varies with model, hardware, provider queueing, network path, input length, and candidate count; agreement with another model is not accuracy; and a calibrated aggregate probability may still fail by class, subgroup, language, attack type, or under drift. A conventional classifier can be faster when labels are stable, while a generative model is better suited to open-ended output or multi-step reasoning.

## What Changed
- Established the concept as a bounded-output transformer architecture distinct from both fixed-label classical classifiers and autoregressive generation.
- Added candidate-set sensitivity, confidence calibration, shared-prefix fan-out, and authority-gating as first-class design constraints.

## Related Concepts
- [[TextClassification]] - provides a common task family for bounded labels over text.
- [[KVCacheAwareRouting]] - shares prefix computation to reduce marginal work across related inference requests.
- [[OracleRouting]] - escalates uncertain cases to a stronger evaluator or human.
- [[Jev]] - exemplifies the commercial typed-decision interface described by the source.

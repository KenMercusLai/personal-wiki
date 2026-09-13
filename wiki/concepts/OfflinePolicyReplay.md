---
title: "Offline Policy Replay"
type: concept
tags: [machine-learning, experimentation, evaluation, recommendations]
sources:
  - artwork-personalization-at-netflix-netflix-techblog-medium
last_updated: 2026-09-14
knowledge_schema: synthesis-v1
---

## Definition
[[OfflinePolicyReplay]] is a counterfactual evaluation method that uses logged randomized interactions to estimate how a different decision policy would have performed.

## Current Synthesis
The Netflix source uses replay to evaluate artwork-selection algorithms before exposing the whole member base to them. Historical exploration logs record which image was randomly assigned, whether the member played the title, and enough randomization information to correct selection bias. A candidate model is then scored on the subset of logged cases where its chosen image matches the historical assignment, producing metrics such as take fraction. The inspected chart shows random image selection lowest, a non-contextual bandit higher, and contextual-bandit approaches highest on average image take fraction, supporting the move from global artwork winners to member-contextual choices.

## Key Claims
- Replay answers counterfactual policy questions from randomized historical logs.
- The method can compare candidate algorithms before online deployment.
- Replay metrics can include take fraction, but the label should reflect quality engagement rather than clickbait starts.
- Replay depends on logged exploration data; without randomized exposure, offline comparisons can be biased.
- Offline gains should be checked online because replay is useful but not a substitute for live experiments.

## Evidence
- Counterfactual setup: [[artwork-personalization-at-netflix-netflix-techblog-medium]] says replay asks what would have happened in historical sessions under different algorithms.
- Matching rule: [[artwork-personalization-at-netflix-netflix-techblog-medium]] describes calculating a replay metric where the random assignment and model assignment are the same.
- Metric focus: [[artwork-personalization-at-netflix-netflix-techblog-medium]] says image evaluation particularly uses take fraction.
- Chart evidence: [[artwork-personalization-at-netflix-netflix-techblog-medium]] shows contextual-bandit bars above random and simple bandit bars on average image take fraction.
- Online check: [[artwork-personalization-at-netflix-netflix-techblog-medium]] reports that promising replay results were followed by A/B testing and showed reasonable offline-online correlation.

## Counterevidence & Qualifications
Replay only estimates outcomes under the logged exploration distribution and the source does not publish confidence intervals, sample sizes, or exact model details for the shown comparison. The source also reports online lift qualitatively, so replay should be treated as a pre-deployment filter rather than proof of full causal impact by itself.

## What Changed
- Created the concept to capture counterfactual offline evaluation of logged recommendation policies.

## Related Concepts
- [[DataExploration]] - supplies the randomized logs that replay needs.
- [[ContextualBandits]] - are candidate policies evaluated through replay in the Netflix source.
- [[ArtworkPersonalization]] - provides the source's replay use case.
- [[BehavioralData]] - provides logged impressions, plays, and quality-engagement outcomes.
- [[ProductMetricLadder]] - replay metrics connect fast evaluation to broader member-experience goals.

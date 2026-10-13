---
title: "ID Balancing"
type: concept
tags: [mixture-of-experts, load-balancing, sparse-routing, pid-control]
sources:
  - 2609.39137
last_updated: 2026-10-13
knowledge_schema: synthesis-v1
---

## Definition
[[IDBalancing]] is an auxiliary-loss-free [[MixtureOfExpertsLoadBalancing]] method that accumulates magnitude-scaled expert-load errors and worsening-gated error changes in non-trainable routing biases.

## Current Synthesis
For expert `i`, the method normalizes the difference between uniform target load and observed token count, adds `Ki` times that error to the expert bias, and adds `Kd` times the error change only when the previous error and its change have the same sign. The gate therefore reacts to an existing imbalance moving farther from zero, while remaining closed when the error shrinks, crosses zero, or has no history.

The resulting bias affects Top-K selection but not expert combination weights. After every update, the method subtracts the mean bias; this removes a routing-irrelevant common component introduced by gated derivative corrections while preserving relative scores. The design is best understood as a generalized integral-derivative controller rather than a literal classical PID implementation because its derivative correction is both gated and accumulated.

Within the paper's MoE family, ID Balancing improves the most as routing becomes extremely sparse, stays stable in a larger configuration, and can remain active during continued pretraining if gains are reduced substantially. It does not uniformly dominate Quantile Balancing, and the causal contribution of model scale is not isolated.

## Key Claims
- Magnitude-aware integral correction responds strongly to severe load errors and weakly near balance.
- A worsening-only derivative gate concentrates extra correction on growing imbalance instead of every fluctuation.
- Zero-mean re-centering removes common bias drift without changing Top-K routing decisions.
- The method needs O(E) token-count feedback per layer and no balancing gradient in the LM objective.
- Smaller continued-pretraining gains trade some load correction for language-model loss close to frozen-bias training.
- Reported advantages grow as the active expert fraction falls, but remain architecture- and experiment-specific.

## Evidence
Mechanism and ablation:
- [[2609.39137]] defines the normalized error, accumulated integral update, worsening gate, derivative correction, and zero-mean centering, then reports lower early violations than integral-only control.

Sparsity and scale:
- [[2609.39137]] reports a Top-3-of-768 worst backbone MaxVio of 15.33 and average MinVio of 0.55, and near-constant worst MaxVio when moving between its 18.9B and 69.9B Top-10 configurations.

Training and inference behavior:
- [[2609.39137]] reports competitive LM and downstream results, lower or comparable violations across 20 backbone layers, and fewer inactive experts on nine evaluation benchmarks.

## Counterevidence & Qualifications
Quantile Balancing achieves tighter backbone balance in the constant high-learning-rate stress test. Larger derivative gains improve early backbone overload while worsening MTP overload, and full gains during continued pretraining worsen LM loss relative to reduced or frozen updates. The scaling configurations change depth, width, active parameters, total parameters, and duration together. All results come from one first-party family of decoder-only, fixed-Top-K MoE models, with no independent replication or formal closed-loop stability proof.

## What Changed
- Established a generalized integral-derivative controller for sparse-MoE expert-bias updates.
- Added worsening-gated error change and zero-mean bias centering as explicit load-control mechanisms.
- Preserved the tradeoffs with Quantile Balancing, MTP load, continued-pretraining loss, and configuration-coupled scaling.

## Related Concepts
- [[MixtureOfExpertsLoadBalancing]] - is the broader routing-capacity problem ID Balancing addresses.
- [[InferenceLoadBalancing]] - shares a load-distribution goal but routes requests across serving workers rather than tokens across experts.
- [[NetworkLoadBalancing]] - provides a system-level analogy while operating at packet and connection scope.
- [[DeepSeekV41Flash]] - is an existing sparse-MoE model profile whose routing would face expert-utilization constraints.

---
title: "Layer Normalization"
type: concept
tags: [machine-learning, neural-networks, normalization, transformers]
sources:
  - transformer-jia-gou-bian-hua-rmsnorm-zhi-nan
last_updated: 2026-10-11
knowledge_schema: synthesis-v1
---

## Definition
[[LayerNormalization]] normalizes a sample across a specified feature shape by subtracting the feature mean and dividing by the square root of the feature variance plus a small stability term, then optionally applying learned elementwise scale and bias.

## Current Synthesis
Layer normalization combines re-centering and re-scaling. Mean subtraction makes the normalized coordinates insensitive to a uniform additive shift, while division by standard deviation makes them insensitive to a uniform positive rescaling, apart from the numerical-stability term. Learned scale and bias then let training restore useful featurewise magnitudes and offsets. In the original [[TransformerArchitecture]], this operation appears around residual attention and feed-forward sublayers; the newer source uses it chiefly as the baseline that [[RMSNorm]] simplifies.

## Key Claims
- The normalized feature vector has approximately zero mean and unit variance before the learned affine transformation.
- Re-centering removes a shared additive offset across the normalized coordinates.
- Re-scaling removes a shared positive multiplicative change in activation magnitude.
- The affine form learns both an elementwise scale and an elementwise bias.

## Evidence
- Formula and interpretation: [[transformer-jia-gou-bian-hua-rmsnorm-zhi-nan]] gives the mean-subtraction, variance-division, scale, and bias formula and interprets its standardized intermediate vector.
- Shift behavior: [[transformer-jia-gou-bian-hua-rmsnorm-zhi-nan]] demonstrates mean subtraction after adding a large constant to all input coordinates.
- Scale behavior: [[transformer-jia-gou-bian-hua-rmsnorm-zhi-nan]] demonstrates standard-deviation division after multiplying the input coordinates by a large constant.
- Affine parameters: [[transformer-jia-gou-bian-hua-rmsnorm-zhi-nan]] contrasts LayerNorm's learned scale and bias with RMSNorm's scale-only form.

## Counterevidence & Qualifications
The source is a compact practitioner tutorial rather than a controlled study. Exact statistics depend on which axes are normalized and on variance conventions and epsilon, while the learned affine output need not itself retain zero mean or unit variance. Shift invariance applies to an offset shared across the normalized coordinates, not arbitrary featurewise perturbations; scale invariance is also only approximate in the presence of epsilon. The guide explains why the transformation has these algebraic properties but does not isolate their causal effect on optimization or downstream quality.

## What Changed
- Created the concept by separating LayerNorm's re-centering and re-scaling roles.
- Added RMSNorm as a qualified simplification that preserves scaling control but not shift removal.

## Related Concepts
- [[RMSNorm]] - removes LayerNorm's mean subtraction and learned bias while retaining magnitude normalization and scale.
- [[TransformerArchitecture]] - originally uses normalization around residual attention and feed-forward sublayers.
- [[NeuralNetworkTraining]] - learns the affine parameters and the surrounding network under normalized activations.

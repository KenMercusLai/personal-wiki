---
title: "RMSNorm"
type: concept
tags: [machine-learning, neural-networks, normalization, transformers]
sources:
  - transformer-jia-gou-bian-hua-rmsnorm-zhi-nan
last_updated: 2026-10-11
knowledge_schema: synthesis-v1
---

## Definition
[[RMSNorm]] normalizes a vector by dividing each coordinate by the square root of the mean squared coordinates plus a small stability term, then optionally applying a learned elementwise scale, without subtracting the vector mean or adding a learned bias.

## Current Synthesis
RMSNorm treats magnitude control as the useful core of [[LayerNormalization]]. Replacing variance around the mean with the raw second moment removes the mean calculation, and omitting the learned bias leaves only a scale vector. This makes the operation algebraically simpler and cheaper while preserving approximate invariance to a shared positive rescaling. It does not preserve LayerNorm's invariance to a uniform additive shift, so the two operations encode different assumptions even when their observed task quality is close.

The guide maps this definition to PyTorch through `normalized_shape`, `eps`, and an optional affine scale. Its handwritten implementation clearly shows `x * rsqrt(eps + mean(x²))`, but correctly represents only single-axis normalization because it always reduces over the final dimension.

## Key Claims
- RMSNorm divides by root mean square rather than standard deviation around a subtracted mean.
- It omits re-centering and therefore does not remove a uniform additive shift.
- Its affine form needs a learned scale but no learned bias.
- Avoiding mean and variance-around-mean calculations reduces arithmetic relative to LayerNorm.
- Comparable quality is an empirical claim whose scope depends on model and task evidence.

## Evidence
- Core operation: [[transformer-jia-gou-bian-hua-rmsnorm-zhi-nan]] provides the root-mean-square formula and a PyTorch implementation using squared activations, a mean, and reciprocal square root.
- Structural simplification: [[transformer-jia-gou-bian-hua-rmsnorm-zhi-nan]] explicitly identifies removal of mean subtraction, replacement of variance by mean square, and deletion of the learned bias.
- Interface: [[transformer-jia-gou-bian-hua-rmsnorm-zhi-nan]] lists PyTorch's normalized trailing shape, epsilon, and affine-scale switch.
- Empirical motivation: [[transformer-jia-gou-bian-hua-rmsnorm-zhi-nan]] says results are close to LayerNorm and directs the reader to the original 2019 paper for experiments.

## Counterevidence & Qualifications
The source does not reproduce or quantify the cited paper's accuracy or efficiency results and does not survey adoption across current models. RMSNorm's scale invariance is approximate when epsilon is material, and it does not provide LayerNorm's shift invariance. Parameter savings remove the bias vector but retain the scale vector; total model savings may therefore be small. The handwritten example's final-axis reduction conflicts with its multi-axis `normalized_shape` annotation, so it should not be treated as a full replacement for `nn.RMSNorm` in the general case.

## What Changed
- Created the concept with a mechanism-first comparison against LayerNorm.
- Preserved the missing re-centering behavior and unquantified empirical claim as explicit qualifications.
- Recorded the handwritten implementation's multi-axis mismatch.

## Related Concepts
- [[LayerNormalization]] - baseline that also subtracts the feature mean and learns an affine bias.
- [[TransformerArchitecture]] - model family in which RMSNorm is used as a normalization variant.
- [[NeuralNetworkTraining]] - supplies the learned scale and determines whether the simpler normalization is effective for a task.

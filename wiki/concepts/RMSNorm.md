---
title: "RMSNorm"
type: concept
tags: [machine-learning, neural-networks, normalization, transformers]
sources:
  - transformer-jia-gou-bian-hua-rmsnorm-zhi-nan
  - transformer-architectures
last_updated: 2026-10-24
knowledge_schema: synthesis-v1
---

## Definition
[[RMSNorm]] normalizes a vector by dividing each coordinate by the square root of the mean squared coordinates plus a small stability term, then optionally applying a learned elementwise scale, without subtracting the vector mean or adding a learned bias.

## Current Synthesis
RMSNorm treats magnitude control as the useful core of [[LayerNormalization]]. Replacing variance around the mean with the raw second moment removes the mean calculation, and omitting the learned bias leaves only a scale vector. This makes the operation algebraically simpler and cheaper while preserving approximate invariance to a shared positive rescaling. It does not preserve LayerNorm's invariance to a uniform additive shift, so the two operations encode different assumptions even when their observed task quality is close.

The guide maps this definition to PyTorch through `normalized_shape`, `eps`, and an optional affine scale. Its handwritten implementation clearly shows `x * rsqrt(eps + mean(x²))`, but correctly represents only single-axis normalization because it always reduces over the final dimension. A later survey supplies the missing adoption evidence within a selected sample: 41 of 53 Transformer LLMs use RMSNorm, with increasing share after its use in Gopher and Chinchilla and its inclusion in the LLaMA recipe. That frequency supports RMSNorm as a modern default but does not isolate normalization from model-family inheritance or other bundled choices.

## Key Claims
- RMSNorm divides by root mean square rather than standard deviation around a subtracted mean.
- It omits re-centering and therefore does not remove a uniform additive shift.
- Its affine form needs a learned scale but no learned bias.
- Avoiding mean and variance-around-mean calculations reduces arithmetic relative to LayerNorm.
- Comparable quality is an empirical claim whose scope depends on model and task evidence.
- Broad modern adoption reflects training, efficiency, implementation, and ecosystem forces rather than proving universal superiority.

## Evidence
- Core operation: [[transformer-jia-gou-bian-hua-rmsnorm-zhi-nan]] provides the root-mean-square formula and a PyTorch implementation using squared activations, a mean, and reciprocal square root.
- Structural simplification: [[transformer-jia-gou-bian-hua-rmsnorm-zhi-nan]] explicitly identifies removal of mean subtraction, replacement of variance by mean square, and deletion of the learned bias.
- Interface: [[transformer-jia-gou-bian-hua-rmsnorm-zhi-nan]] lists PyTorch's normalized trailing shape, epsilon, and affine-scale switch.
- Empirical motivation: [[transformer-jia-gou-bian-hua-rmsnorm-zhi-nan]] says results are close to LayerNorm and directs the reader to the original 2019 paper for experiments.
- Adoption: [[transformer-architectures]] reports RMSNorm in 41 of 53 selected models and shows its cumulative share rising across later releases.

## Counterevidence & Qualifications
The implementation guide does not reproduce or quantify the cited paper's accuracy or efficiency results. RMSNorm's scale invariance is approximate when epsilon is material, and it does not provide LayerNorm's shift invariance. Parameter savings remove the bias vector but retain the scale vector; total model savings may therefore be small. The handwritten example's final-axis reduction conflicts with its multi-axis `normalized_shape` annotation, so it should not be treated as a full replacement for `nn.RMSNorm` in the general case. The survey is descriptive, favors public and influential families, counts related releases separately, and cannot establish that RMSNorm caused their quality or stability.

## What Changed
- Added selected-sample adoption evidence across 53 Transformer LLMs.
- Qualified adoption as bundled and family-correlated rather than causal proof.

## Related Concepts
- [[LayerNormalization]] - baseline that also subtracts the feature mean and learns an affine bias.
- [[TransformerArchitecture]] - model family in which RMSNorm is used as a normalization variant.
- [[NeuralNetworkTraining]] - supplies the learned scale and determines whether the simpler normalization is effective for a task.
- [[TransformerArchitecturalConvergence]] - places RMSNorm in the current dense decoder-only default stack.
- [[QueryKeyNormalization]] - may reuse RMS-style normalization specifically on attention queries and keys.

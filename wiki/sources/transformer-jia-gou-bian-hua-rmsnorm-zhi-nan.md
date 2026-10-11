---
title: "Transformer 架构变化：RMSNorm 指南"
type: source
tags: [transformer, normalization, rmsnorm, layernorm, pytorch]
date: 2025-05-11
source_file: "/mnt/ken_personal_wiki/Articles/Transformer 架构变化：RMSNorm 指南.md"
---

## Summary
This Chinese-language technical guide contrasts [[LayerNormalization]] with [[RMSNorm]], presenting RMSNorm as a re-scaling-only simplification that removes mean subtraction and the learned bias while replacing variance with the mean of squared activations. It explains the formulas, expected parameter and computation savings, PyTorch's `nn.RMSNorm` interface, and a short handwritten implementation, while referring readers to the original paper rather than reproducing its experiments.

## Key Claims
- [[LayerNormalization]] transforms each sample's feature vector by subtracting its mean and dividing by its standard deviation, then applying learned scale and bias parameters.
- Layer normalization is commonly explained through two invariances: re-centering resists a uniform additive shift, while re-scaling resists proportional changes in magnitude.
- [[RMSNorm]] keeps the re-scaling mechanism but omits re-centering: it divides each activation by the root mean square of the normalized coordinates and applies a learned scale.
- Removing the mean calculation and learned bias reduces arithmetic and affine parameters relative to layer normalization.
- The guide says RMSNorm performs comparably to layer normalization, but delegates the supporting experiments and details to Zhang and Sennrich's 2019 paper.
- PyTorch exposes the normalized trailing shape, numerical-stability epsilon, and optional learnable affine scale; the supplied custom implementation demonstrates the core calculation with `rsqrt`.

## Key Quotes
> “RMSNorm 的效果还真就挺好的，跟 LayerNorm 也差不了多少” — the guide's qualitative empirical conclusion.

> “只需要维护 γ 参数，不需要维护 β” — on the smaller affine parameter set.

## Connections
- [[RMSNorm]] — the normalization method introduced and implemented by the guide.
- [[LayerNormalization]] — the baseline decomposed into re-centering and re-scaling.
- [[TransformerArchitecture]] — the model family in which the guide says RMSNorm increasingly replaces layer normalization.
- [[NeuralNetworkTraining]] — normalization changes activation scaling and the parameters learned during training.

## Contradictions
- The article's empirical comparison is a summary of the cited RMSNorm paper, not an experiment reproduced in the guide; it gives no model, task, metric, speedup, memory, or quality measurements of its own.
- RMSNorm is invariant to positive rescaling but does not remove a uniform additive shift because it deliberately omits mean subtraction; it is therefore a different inductive choice, not an algebraically equivalent cheaper LayerNorm.
- The handwritten class accepts a list or tuple for `normalized_shape`, but its `mean(dim=-1)` normalizes only the final axis. It does not reproduce PyTorch's multi-axis behavior when more than one trailing dimension is requested.
- The introductory claim that more contemporary large models use RMSNorm is plausible but unquantified and supplies no adoption survey.

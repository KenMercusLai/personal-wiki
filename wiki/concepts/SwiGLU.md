---
title: "SwiGLU"
type: concept
tags: [transformers, activation-functions, gated-linear-units, mlp]
sources:
  - transformer-architectures
last_updated: 2026-10-24
knowledge_schema: synthesis-v1
---

## Definition
[[SwiGLU]] is a gated Transformer feed-forward layer that multiplies a SiLU-activated projection by a separate linear projection before applying an output projection.

## Current Synthesis
A conventional Transformer FFN applies one nonlinear hidden projection and one output projection. SwiGLU adds a third matrix so one input-dependent path gates another: `SiLU(xW1) ⊙ xW3`, followed by `W2`. The multiplicative interaction can selectively amplify or suppress features instead of applying only a fixed elementwise nonlinearity.

The added projection changes fair width comparisons. A two-matrix FFN with hidden width `4d` and a three-matrix SwiGLU layer have similar parameter counts when the gated hidden width is near `8d/3`; the familiar expansion is therefore a parameter-matching convention, not a proven optimum. The surveyed sample reports GLU-family activations in 38 of 53 models and near-universal use after LLaMA, but those adoption counts do not isolate gating from the rest of the model recipe.

## Key Claims
- SwiGLU combines SiLU nonlinearity with an input-dependent multiplicative gate.
- Its third projection increases expressivity and parameter cost relative to a two-matrix FFN at equal width.
- An expansion near `8/3` matches the parameter count of a conventional four-times-wide FFN.
- The gated path can suppress or amplify features conditionally on the input.
- Broad adoption and cited controlled results support SwiGLU as a strong default, not a universal optimum.

## Evidence
Mechanism and parameter matching:
- [[transformer-architectures]] gives the three-projection equation and equates its parameter count with a `4d` standard FFN to obtain the `8d/3` width.

Adoption and motivation:
- [[transformer-architectures]] reports 38 of 53 sampled models using SwiGLU or GeGLU and attributes the family to better quality at similar parameter or FLOP budgets.

## Counterevidence & Qualifications
The article is a survey, not a reproduced ablation, and its sample groups SwiGLU with GeGLU in the summary count. The claim that gating is worth more than width depends on cited prior comparisons and may vary with scale, optimizer, data, kernels, and total compute. Smooth nonzero SiLU gradients are a plausible mechanism, not by themselves a causal explanation of end quality. The `8/3` ratio follows parameter equality and remains an open tuning question.

## What Changed
- Created the concept with mechanism, parameter-matching, and adoption evidence.

## Related Concepts
- [[TransformerArchitecture]] - places SwiGLU in the positionwise feed-forward sublayer.
- [[TransformerArchitecturalConvergence]] - treats SwiGLU as part of the modern dense default stack.
- [[MixtureOfExpertsLoadBalancing]] - often routes among expert FFNs built from related gated MLPs.
- [[NeuralNetworkTraining]] - determines whether the extra gated interaction improves a particular model.

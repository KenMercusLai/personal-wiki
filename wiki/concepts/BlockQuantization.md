---
title: "Block Quantization"
type: concept
tags: [machine-learning, quantization, numerical-computing, neural-networks]
sources:
  - scar-of-quantization
last_updated: 2026-10-07
knowledge_schema: synthesis-v1
---

## Definition
[[BlockQuantization]] represents a group of tensor values with a shared low-precision scale, trading compact and efficient arithmetic against error caused when the group's values have very different magnitudes.

## Current Synthesis
The source makes block shape a semantic choice. A 32 by 32 activation tile shares one INT8 scale across 32 tokens and 32 channels, so one large magnitude fixes the range for 1,024 values. Smaller nonzero values can then fall below the representable step and round to zero across both dimensions. A 1 by 32 scale keeps the same channel width but stops the outlier from setting the scale for neighboring tokens.

On one selected 10,000-step tile, the source reports underflow falling from 92.3% with 32 by 32 scaling to 9.1% with 1 by 32 scaling, while SQNR rises from 27.2 to 43.4 dB. Applying a Hadamard transform offline before 1 by 32 quantization spreads the outlier and yields 0.7% underflow and 54.0 dB after inverse rotation. The narrower block also restores validation convergence in the reported retraining, whereas the transform has no end-to-end training evidence here.

## Key Claims
- Shared scales couple every value in a block, so block dimensions determine an outlier's error blast radius.
- Large within-block dynamic range can systematically map small nonzero values to zero and bias the represented tensor.
- Narrower scaling can preserve more signal at the cost of managing more scales or changing kernel and hardware tradeoffs not measured by this source.
- Orthogonal rotation can redistribute an outlier before quantization, but local SQNR improvement does not guarantee training or deployment benefit.
- In causal attention, a scale computed across multiple token positions can itself carry future information even when later attention weights are masked.

## Evidence
- Coupling mechanism: [[scar-of-quantization]] compares one scale over 32 tokens by 32 channels with separate 1 by 32 token-row scales around the same marked outlier.
- Underflow and signal quality: [[scar-of-quantization]] reports 92.3%/27.2 dB for 32 by 32, 9.1%/43.4 dB for 1 by 32, and 0.7%/54.0 dB for Hadamard plus 1 by 32 on the selected tile.
- Training consequence: [[scar-of-quantization]] shows 1 by 32 W8A8 validation tracking BF16 while 32 by 32 validation turns upward despite similar falling training losses.
- Token boundary: [[scar-of-quantization]] cites MatX for future leakage when an attention quantization scale is shared across causally separated tokens.

## Counterevidence & Qualifications
The measurements cover one selected tensor tile and one reported training comparison. The source does not quantify scale-storage overhead, kernel performance, memory traffic, accelerator support, calibration choices, saturation, per-channel alternatives, stochastic variation, or whether the same block shape works across layers and model sizes. The Hadamard result is offline and inverted before measurement. The causal-attention warning is attributed to external work rather than reproduced in this experiment.

## What Changed
- Created the concept around scale-sharing boundaries and outlier blast radius.
- Added measured underflow and SQNR comparisons for 32 by 32, 1 by 32, and rotated 1 by 32 scaling.
- Separated local numerical improvement from demonstrated end-to-end convergence.

## Related Concepts
- [[QuantizationAwareTraining]] - trains a model under the distortions introduced by the chosen block scheme.
- [[NeuralNetwork]] - weights and transient activations are candidate tensors for shared-scale representation.
- [[AttentionMechanism]] - causal token order constrains which positions may safely contribute to scale calculation.
- [[DeepLearningScaling]] - larger models may develop outlier structure that changes the required granularity or transform.

---
title: "Block Quantization"
type: concept
tags: [machine-learning, quantization, numerical-computing, neural-networks]
sources:
  - scar-of-quantization
  - outperforming-cublas-nvfp4
last_updated: 2026-10-18
knowledge_schema: synthesis-v1
---

## Definition
[[BlockQuantization]] represents a group of tensor values with a shared low-precision scale, trading compact and efficient arithmetic against error caused when the group's values have very different magnitudes.

## Current Synthesis
The source makes block shape a semantic choice. A 32 by 32 activation tile shares one INT8 scale across 32 tokens and 32 channels, so one large magnitude fixes the range for 1,024 values. Smaller nonzero values can then fall below the representable step and round to zero across both dimensions. A 1 by 32 scale keeps the same channel width but stops the outlier from setting the scale for neighboring tokens.

On one selected 10,000-step tile, the source reports underflow falling from 92.3% with 32 by 32 scaling to 9.1% with 1 by 32 scaling, while SQNR rises from 27.2 to 43.4 dB. Applying a Hadamard transform offline before 1 by 32 quantization spreads the outlier and yields 0.7% underflow and 54.0 dB after inverse rotation. The narrower block also restores validation convergence in the reported retraining, whereas the transform has no end-to-end training evidence here.

NVFP4 supplies a hardware-consumed example with a different precision and boundary. Sixteen consecutive E2M1 values along K share one unsigned UE4M3 scale, for 9 bytes per block or 4.5 bits per value. A simple conversion chooses the block's maximum absolute magnitude divided by E2M1's largest magnitude, six, then normalizes values into the representable set. On Blackwell, `tcgen05.mma` reads packed values and scale factors through different staging paths, applies the scale internally, and accumulates in FP32, so numerical grouping also determines scale traffic, TMEM use, and pipeline geometry.

## Key Claims
- Shared scales couple every value in a block, so block dimensions determine an outlier's error blast radius.
- Large within-block dynamic range can systematically map small nonzero values to zero and bias the represented tensor.
- Narrower scaling can preserve more signal at the cost of managing more scales or changing kernel and hardware tradeoffs not measured by this source.
- Orthogonal rotation can redistribute an outlier before quantization, but local SQNR improvement does not guarantee training or deployment benefit.
- In causal attention, a scale computed across multiple token positions can itself carry future information even when later attention weights are masked.
- Hardware-native block formats couple numerical granularity to scale storage, layout, movement, and tensor-core instruction shapes.

## Evidence
- Coupling mechanism: [[scar-of-quantization]] compares one scale over 32 tokens by 32 channels with separate 1 by 32 token-row scales around the same marked outlier.
- Underflow and signal quality: [[scar-of-quantization]] reports 92.3%/27.2 dB for 32 by 32, 9.1%/43.4 dB for 1 by 32, and 0.7%/54.0 dB for Hadamard plus 1 by 32 on the selected tile.
- Training consequence: [[scar-of-quantization]] shows 1 by 32 W8A8 validation tracking BF16 while 32 by 32 validation turns upward despite similar falling training losses.
- Token boundary: [[scar-of-quantization]] cites MatX for future leakage when an attention quantization scale is shared across causally separated tokens.
- NVFP4 representation: [[outperforming-cublas-nvfp4]] records E2M1's representable magnitudes, one UE4M3 scale per 16 K-adjacent values, and the resulting 4.5-bit effective storage.
- Hardware dataflow: [[outperforming-cublas-nvfp4]] shows scale bytes taking a separate TMA-to-SMEM-to-TMEM path before `tcgen05.mma` applies them and accumulates FP32 output.

## Counterevidence & Qualifications
The INT8 measurements cover one selected tensor tile and one reported training comparison. That source does not quantify scale-storage overhead, kernel performance, memory traffic, accelerator support, calibration choices, saturation, per-channel alternatives, stochastic variation, or whether the same block shape works across layers and model sizes. The Hadamard result is offline and inverted before measurement, and the causal-attention warning is attributed to external work. The NVFP4 source evaluates kernel throughput rather than model quality: it supplies no quantization-error distribution, accuracy comparison, calibration study, training result, or evidence that maximum-absolute scaling is optimal. Its 4.5-bit accounting excludes broader metadata and layout costs.

## What Changed
- Added hardware-native NVFP4 as a 16-value E2M1 block with one UE4M3 scale and 4.5-bit effective payload cost.
- Connected scale granularity to Blackwell's separate scale movement, TMEM footprint, and tensor-core consumption.
- Preserved the distinction between a throughput demonstration and evidence of model-level quantization quality.

## Related Concepts
- [[QuantizationAwareTraining]] - trains a model under the distortions introduced by the chosen block scheme.
- [[NeuralNetwork]] - weights and transient activations are candidate tensors for shared-scale representation.
- [[AttentionMechanism]] - causal token order constrains which positions may safely contribute to scale calculation.
- [[DeepLearningScaling]] - larger models may develop outlier structure that changes the required granularity or transform.

---
title: "Block Quantization"
type: concept
tags: [machine-learning, quantization, numerical-computing, neural-networks]
sources:
  - scar-of-quantization
  - outperforming-cublas-nvfp4
  - how-to-llm-inference
last_updated: 2026-10-25
knowledge_schema: synthesis-v1
---

## Definition
[[BlockQuantization]] represents a group of tensor values with a shared low-precision scale, trading compact and efficient arithmetic against error caused when the group's values have very different magnitudes.

## Current Synthesis
The source makes block shape a semantic choice. A 32 by 32 activation tile shares one INT8 scale across 32 tokens and 32 channels, so one large magnitude fixes the range for 1,024 values. Smaller nonzero values can then fall below the representable step and round to zero across both dimensions. A 1 by 32 scale keeps the same channel width but stops the outlier from setting the scale for neighboring tokens.

On one selected 10,000-step tile, the source reports underflow falling from 92.3% with 32 by 32 scaling to 9.1% with 1 by 32 scaling, while SQNR rises from 27.2 to 43.4 dB. Applying a Hadamard transform offline before 1 by 32 quantization spreads the outlier and yields 0.7% underflow and 54.0 dB after inverse rotation. The narrower block also restores validation convergence in the reported retraining, whereas the transform has no end-to-end training evidence here.

NVFP4 supplies a hardware-consumed example with a different precision and boundary. Sixteen consecutive E2M1 values along K share one unsigned UE4M3 scale, for 9 bytes per block or 4.5 bits per value. A simple conversion chooses the block's maximum absolute magnitude divided by E2M1's largest magnitude, six, then normalizes values into the representable set. On Blackwell, `tcgen05.mma` reads packed values and scale factors through different staging paths, applies the scale internally, and accumulates in FP32, so numerical grouping also determines scale traffic, TMEM use, and pipeline geometry.

The CPU-inference source supplies two GGUF formats at another hardware boundary. Q8_0 uses one fp16 scale for 32 signed eight-bit values, totaling 34 bytes or 8.5 bits per weight. Q4_K groups 256 four-bit values into eight 32-value sub-blocks with local scale and minimum, then quantizes those sixteen parameters to six bits under one fp16 scale and one fp16 minimum, totaling 144 bytes or 4.5 bits per weight. Runtime bf16 activations are quantized to Q8_K so unpacked Q4_K weights can use CPU `u8 × i8` dot products without an intervening fp32 weight tensor.

## Key Claims
- Shared scales couple every value in a block, so block dimensions determine an outlier's error blast radius.
- Large within-block dynamic range can systematically map small nonzero values to zero and bias the represented tensor.
- Narrower scaling can preserve more signal at the cost of managing more scales or changing kernel and hardware tradeoffs not measured by this source.
- Orthogonal rotation can redistribute an outlier before quantization, but local SQNR improvement does not guarantee training or deployment benefit.
- In causal attention, a scale computed across multiple token positions can itself carry future information even when later attention weights are masked.
- Hardware-native block formats couple numerical granularity to scale storage, layout, movement, and tensor-core instruction shapes.
- A deployment format should be evaluated with its matching compute path: dequantizing a compact block into a wide temporary can erase its bandwidth advantage.

## Evidence
- Coupling mechanism: [[scar-of-quantization]] compares one scale over 32 tokens by 32 channels with separate 1 by 32 token-row scales around the same marked outlier.
- Underflow and signal quality: [[scar-of-quantization]] reports 92.3%/27.2 dB for 32 by 32, 9.1%/43.4 dB for 1 by 32, and 0.7%/54.0 dB for Hadamard plus 1 by 32 on the selected tile.
- Training consequence: [[scar-of-quantization]] shows 1 by 32 W8A8 validation tracking BF16 while 32 by 32 validation turns upward despite similar falling training losses.
- Token boundary: [[scar-of-quantization]] cites MatX for future leakage when an attention quantization scale is shared across causally separated tokens.
- NVFP4 representation: [[outperforming-cublas-nvfp4]] records E2M1's representable magnitudes, one UE4M3 scale per 16 K-adjacent values, and the resulting 4.5-bit effective storage.
- Hardware dataflow: [[outperforming-cublas-nvfp4]] shows scale bytes taking a separate TMA-to-SMEM-to-TMEM path before `tcgen05.mma` applies them and accumulates FP32 output.
- GGUF CPU formats: [[how-to-llm-inference]] diagrams Q8_0's 32-value shared-scale block and Q4_K's 256-value hierarchy of local and super-block parameters.
- Direct quantized execution: [[how-to-llm-inference]] aligns Q4_K weights with Q8_K activations and CPU integer-dot instructions, retaining fp32 only for scaled accumulation around the integer reduction.

## Counterevidence & Qualifications
The INT8 measurements cover one selected tensor tile and one reported training comparison. That source does not quantify scale-storage overhead, kernel performance, memory traffic, accelerator support, calibration choices, saturation, per-channel alternatives, stochastic variation, or whether the same block shape works across layers and model sizes. The Hadamard result is offline and inverted before measurement, and the causal-attention warning is attributed to external work. The NVFP4 source evaluates kernel throughput rather than model quality: it supplies no quantization-error distribution, accuracy comparison, calibration study, training result, or evidence that maximum-absolute scaling is optimal. Its 4.5-bit accounting excludes broader metadata and layout costs. The GGUF inference source likewise does not measure perplexity or output quality against an unquantized model, compare its kernel with a mature runtime, or establish that its selected per-tensor formats are optimal.

## What Changed
- Added Q8_0 and hierarchical Q4_K as concrete GGUF block layouts for CPU inference.
- Connected stored block structure to Q8_K activation conversion and native integer dot products.
- Preserved the distinction between runtime throughput and model-quality evidence.

## Related Concepts
- [[QuantizationAwareTraining]] - trains a model under the distortions introduced by the chosen block scheme.
- [[NeuralNetwork]] - weights and transient activations are candidate tensors for shared-scale representation.
- [[AttentionMechanism]] - causal token order constrains which positions may safely contribute to scale calculation.
- [[DeepLearningScaling]] - larger models may develop outlier structure that changes the required granularity or transform.

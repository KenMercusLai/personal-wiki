---
title: "Quantization-Aware Training"
type: concept
tags: [machine-learning, neural-network-training, quantization, low-precision]
sources:
  - scar-of-quantization
last_updated: 2026-10-07
knowledge_schema: synthesis-v1
---

## Definition
[[QuantizationAwareTraining]] trains a neural network while exposing its forward computation to approximated low-precision rounding and scaling effects so that learned parameters can adapt to the numerical behavior expected from quantized execution.

## Current Synthesis
The source shows that adaptation is not guaranteed to succeed merely because optimization continues. In one W8A8 pretraining run, 32-token by 32-channel activation blocks shared an INT8 scale. A large outlier could therefore enlarge the step size for all 1,024 values, round many smaller nonzero activations to zero, and form structured bands in `mlp.down_proj`. Some bands changed across checkpoints while one remained visible through 50,000 steps.

Aggregate training loss concealed the failure: BF16, 32 by 32 W8A8, and 1 by 32 W8A8 training curves all declined, yet BF16 validation with quantization disabled diverged only for the 32 by 32 run. Holding weight quantization fixed and narrowing activation scales to 1 by 32 made the rerun nearly track the BF16 validation curve. This makes scale granularity part of the training objective's effective information path, not only an inference-format detail.

## Key Claims
- A decreasing training loss does not establish that a quantization-aware run is learning a model that generalizes when quantization is disabled.
- Outlier-driven rounding can create structured, persistent activation underflow rather than unbiased random noise.
- Quantization granularity changes the number and kinds of values coupled through one scale, and can therefore determine whether training converges.
- Activation-level inspection across fixed inputs and checkpoints can reveal failure modes hidden by aggregate loss curves.
- Offline numerical improvement from an outlier-spreading transform is a candidate intervention, not evidence of end-to-end training benefit.

## Evidence
- Hidden failure: [[scar-of-quantization]] shows all three training losses falling while the 32 by 32 W8A8 run's BF16 validation loss bottoms out and rises.
- Structured underflow: [[scar-of-quantization]] visualizes pale zeroed activation bands for the same sequence across checkpoints, with at least one band persisting through 50,000 steps.
- Granularity intervention: [[scar-of-quantization]] reports validation convergence after changing activations from 32 by 32 to 1 by 32 scales while keeping weight quantization unchanged.
- Candidate transform: [[scar-of-quantization]] reports a one-tile offline SQNR increase from 43.4 to 54.0 dB with Hadamard rotation plus 1 by 32 scaling, without a corresponding training run.

## Counterevidence & Qualifications
The evidence is one practitioner experiment without a fully specified model, dataset, optimizer, seed set, confidence interval, throughput comparison, or full-tensor summary. The source selects one problematic activation and one tile, so the visible scar and reported underflow rates do not establish prevalence across layers, inputs, or checkpoints. Validation deliberately disables quantization, which usefully tests learned model quality but does not by itself report deployed quantized accuracy. Hadamard rotation and larger-model behavior remain untrained or externally motivated hypotheses in this source.

## What Changed
- Created the concept around the distinction between successful loss minimization and successful adaptation to quantization noise.
- Added activation-scar inspection and validation-with-quantization-disabled as complementary diagnostics.
- Identified activation scale granularity as a convergence-relevant training design choice.

## Related Concepts
- [[BlockQuantization]] - shared-scale block shape determines the outlier coupling that the training process must absorb.
- [[NeuralNetworkTraining]] - supplies the loss-minimization and validation framework within which adaptation can fail.
- [[NeuralNetwork]] - transient activations are the low-precision values distorted in the reported run.
- [[DeepLearningScaling]] - increasing model size may change outlier structure and invalidate a granularity that worked at smaller scale.
- [[AttentionMechanism]] - token-shared scales can introduce a separate causal-information risk during quantized attention.

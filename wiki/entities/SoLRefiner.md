---
title: "SoL-Refiner"
type: entity
tags: [video-generation, video-refinement, diffusion-models, nvidia]
sources:
  - 2609.37969
last_updated: 2026-10-13
knowledge_schema: synthesis-v1
---

## Overview
[[SoLRefiner]] is a [[Nvidia]] one-step generated-video refiner that can improve detail, repair some local synthesis artifacts, and optionally upscale outputs from multiple base generators.

## Current Profile
The model starts from LTX-2.3 and follows paired high-resolution continual training, frame-reward RL post-training, and staged DMD-GAN distillation. At inference, a tiny autoencoder handles video coding, the low-quality latent is upsampled and noised, Sol-Engine executes one refiner evaluation, and the result is decoded. The paper positions it as a replaceable second stage rather than a modification of the base generator.

## Key Characteristics
- Uses one target-resolution denoising network evaluation.
- Supports artifact mitigation with or without spatial enlargement.
- Is trained through continual flow matching, perceptual reward feedback, and staged distribution/adversarial distillation.
- Transfers across several evaluated base video generators without base-model retraining.
- Combines model compression with TAE and Sol-Engine system acceleration.
- Preserves base content and motion more readily than it corrects large upstream semantic or geometric errors.

## Evidence
Architecture:
- [[2609.37969]] diagrams the three training stages and the TAE → latent upsampling/noise → one-NFE Sol-Engine → TAE inference path.

Quality:
- [[2609.37969]] reports leading VBench and UniPercept averages among evaluated external refiners at roughly 2K and gains over LTX-2.3 from 720p to 4K.

Latency and transfer:
- [[2609.37969]] reports 6.447-second 2K refinement after the full stack and lower end-to-end latency across WAN, Cosmos-Nano, MiniMax H3, and DGX Spark settings.

## Qualifications
All results are first-party. The one-step model trails the 23-step variant on aggregate quality, the benchmark uses automated metrics and selected examples, and hardware-specific speedups use different resolutions, frame counts, and baselines. Frame rewards do not directly optimize long-range consistency, and major content, geometry, and motion repair is outside the stated objective.

## What Changed
- Created the model profile and recorded its training, inference, benchmark, and scope boundaries.

## Relationships
- [[Nvidia]] - organization that developed and evaluated the model.
- [[VideoRefinement]] - task the model performs.
- [[OneStepDiffusionDistillation]] - method used to compress its multi-step teacher.
- [[RefinerBench]] - benchmark introduced to evaluate the model against other refiners.
- [[DiffusionModelSampling]] - computational process reduced to one target-resolution evaluation.

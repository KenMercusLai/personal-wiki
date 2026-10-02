---
title: "Stable Diffusion"
type: entity
tags: [ai, diffusion-models, image-generation]
sources:
  - stable-diffusion-samplers-a-comprehensive-guide-stable-diffusion-art
last_updated: 2026-10-02
knowledge_schema: synthesis-v1
---

## Overview
[[StableDiffusion]] is represented in the available source as a latent diffusion image-generation model whose inference begins with a random latent and repeatedly applies a learned noise estimate until a clean image is produced.

## Current Profile
The guide focuses on Stable Diffusion's inference mechanics rather than training, ownership, release history, or current product status. Its key operational boundary is between the learned noise predictor and [[DiffusionModelSampling]]: the model estimates what should be removed, while the selected solver and schedule determine how that estimate changes the latent at each step. The article uses SDXL samples for PCA trajectory illustrations and evaluates a historical menu of methods exposed by [[AUTOMATIC1111]].

## Key Characteristics
- Generates images by iteratively transforming a random latent through learned denoising predictions.
- Exposes sampler and step-count choices that trade runtime, repeatability, variation, and measured output quality.
- Operates in a high-dimensional latent space; the source describes an SDXL sample as 65,536-dimensional before PCA projection.
- Can be driven by deterministic, stochastic, multistep, predictor-corrector, and model-specific sampling methods.

## Evidence
- Generation loop: [[stable-diffusion-samplers-a-comprehensive-guide-stable-diffusion-art]] diagrams successive noise predictions and latent updates from noise to a cat image.
- Latent trajectory: [[stable-diffusion-samplers-a-comprehensive-guide-stable-diffusion-art]] presents PCA projections for one SDXL path and for seed and prompt changes.
- Sampler surface: [[stable-diffusion-samplers-a-comprehensive-guide-stable-diffusion-art]] compares multiple solver families available through AUTOMATIC1111 and explains their update and scheduling differences.
- Output trade-offs: [[stable-diffusion-samplers-a-comprehensive-guide-stable-diffusion-art]] presents convergence, relative-time, and BRISQUE plots across a selected sampler set.

## Qualifications
This profile comes from one practitioner guide centered on sampler behavior. The model-family description is simplified, the PCA projections are lossy explanatory views, and the benchmark does not establish current or universal sampler rankings. The source does not provide a broader institutional, licensing, training-data, safety, or release-history profile of Stable Diffusion.

## What Changed
- Created a source-bounded profile of Stable Diffusion's sampler-facing inference behavior.
- Separated the learned noise predictor from the numerical method that applies its predictions.

## Relationships
- [[DiffusionModelSampling]] - numerical inference process that turns Stable Diffusion's predictions into iterative latent updates.
- [[AUTOMATIC1111]] - interface through which the source selects and compares Stable Diffusion samplers.
- [[DeepLearning]] - broader learned-model field containing the noise-prediction component described here.
- [[PrincipalComponentAnalysis]] - method used to visualize compressed SDXL latent trajectories.

---
title: "AUTOMATIC1111"
type: entity
tags: [stable-diffusion, software, image-generation]
sources:
  - stable-diffusion-samplers-a-comprehensive-guide-stable-diffusion-art
last_updated: 2026-10-02
knowledge_schema: synthesis-v1
---

## Overview
[[AUTOMATIC1111]] is represented in the source as a graphical interface for [[StableDiffusion]] that exposes a menu of sampling methods and step controls for image generation.

## Current Profile
The 2023 guide uses AUTOMATIC1111 as the practical setting for comparing Euler, Heun, LMS, DDIM, PLMS, DPM and DPM++ variants, UniPC, Karras-labelled schedule variants, and later LCM sampling. The interface makes technical implementation choices user-visible through compact names, but those names combine several dimensions: numerical solver, stochastic behavior, schedule, and sometimes intended model family. The article also attributes most of its then-current samplers, apart from DDIM, PLMS, and UniPC, to Katherine Crowson's k-diffusion implementation.

## Key Characteristics
- Provides user-facing selection of sampling method and sampling-step count.
- Uses labels such as `a` and `Karras` to signal ancestral behavior or an alternate noise schedule in some sampler names.
- Integrates sampler implementations from several research and software lineages, including k-diffusion.
- Serves as the historical benchmark environment for the article's convergence, speed, and quality comparisons.

## Evidence
- Interface inventory: [[stable-diffusion-samplers-a-comprehensive-guide-stable-diffusion-art]] shows and enumerates the sampler menu available at the time of writing.
- Naming semantics: [[stable-diffusion-samplers-a-comprehensive-guide-stable-diffusion-art]] explains ancestral `a` variants and Karras schedule variants while warning that not every stochastic method carries the `a` label.
- Implementation lineage: [[stable-diffusion-samplers-a-comprehensive-guide-stable-diffusion-art]] connects most listed methods to k-diffusion and identifies exceptions.
- Evaluation setting: [[stable-diffusion-samplers-a-comprehensive-guide-stable-diffusion-art]] presents relative rendering time, convergence, and BRISQUE comparisons for methods exposed through the interface.

## Qualifications
The profile is a narrow historical snapshot from one tutorial, not a current feature inventory or an independently verified software history. The source says the sampler count was growing, and later updates added LCM, so names, defaults, implementations, and available methods should be checked against the software version in use. The benchmark also does not document enough environment detail to attribute every observed difference specifically to the interface or sampler implementation.

## What Changed
- Created a source-bounded profile of AUTOMATIC1111 as the article's sampler-selection and evaluation environment.
- Preserved the historical and version-sensitive nature of its sampler inventory.

## Relationships
- [[StableDiffusion]] - model family the interface operates in the source.
- [[DiffusionModelSampling]] - technical process exposed through the interface's sampler controls.
- [[DeepLearning]] - broader model family whose inference the interface orchestrates.

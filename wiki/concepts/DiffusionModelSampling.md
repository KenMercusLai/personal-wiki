---
title: "Diffusion Model Sampling"
type: concept
tags: [diffusion-models, image-generation, numerical-methods, sampling]
sources:
  - stable-diffusion-samplers-a-comprehensive-guide-stable-diffusion-art
last_updated: 2026-10-02
knowledge_schema: synthesis-v1
---

## Definition
[[DiffusionModelSampling]] is the inference-time process that converts an initial noisy latent into a generated result by repeatedly applying a learned noise or denoised-state prediction according to a numerical solver and noise schedule.

## Current Synthesis
The available guide separates four choices that sampler names often compress together: the numerical update rule, whether fresh noise is introduced, the schedule of noise levels, and compatibility with the trained model. The learned [[DeepLearning]] model predicts noise or a cleaner state; the sampler then decides how to traverse that prediction field. Euler is a simple deterministic first-order update, Heun trades a second model evaluation per step for a more accurate correction, multistep methods reuse prior evaluations, ancestral and SDE methods introduce stochasticity, and Karras-labelled variants alter the noise schedule rather than replacing the underlying solver.

These choices optimize different outcomes. Smaller scheduled changes can reduce discretization error, but more steps do not guarantee convergence when a method deliberately injects noise. Deterministic convergence supports repeatable refinement, while stochastic paths can yield useful variations. Runtime depends heavily on noise-model evaluations per step, and perceptual quality is distinct from convergence: an image can look good without approaching a fixed high-step result. Specialized LCM sampling adds a further constraint because it is intended for latent consistency models rather than as a drop-in universal solver.

## Key Claims
- Sampler behavior is jointly determined by solver, stochasticity, noise schedule, step count, and the model it is designed to use.
- Early high-noise steps influence broad composition, while later low-noise steps make smaller refinements in the article's PCA-based interpretation.
- Deterministic convergence and visually appealing output are separate goals; stochastic methods may vary indefinitely with step count yet still produce good images.
- Higher-order correction can reduce numerical error per step but usually costs additional learned-model evaluations and therefore more runtime.
- Karras scheduling allocates smaller changes near the low-noise end, but its practical benefit is sampler- and step-dependent rather than automatic.
- Benchmark-derived sampler rankings are conditional on prompts, seeds, model version, implementation, hardware, reference choice, and quality metric.

## Evidence
- Denoising mechanism and trajectory: [[stable-diffusion-samplers-a-comprehensive-guide-stable-diffusion-art]] depicts predicted noise being subtracted repeatedly, plots large early and small late schedule changes, and projects an SDXL trajectory into two PCA dimensions.
- Stochasticity and convergence: [[stable-diffusion-samplers-a-comprehensive-guide-stable-diffusion-art]] compares Euler with Euler ancestral animations and reports nonconvergent ancestral and DPM++ SDE curves against deterministic families.
- Cost and accuracy: [[stable-diffusion-samplers-a-comprehensive-guide-stable-diffusion-art]] reports that two-evaluation methods form a roughly 2x runtime tier, while DPM Adaptive is slower still because it selects its own steps.
- Schedule and method families: [[stable-diffusion-samplers-a-comprehensive-guide-stable-diffusion-art]] distinguishes Euler, Heun, LMS, DDIM, DPM/DPM++, UniPC, Karras schedules, and LCM-specific sampling.
- Quality versus convergence: [[stable-diffusion-samplers-a-comprehensive-guide-stable-diffusion-art]] shows low BRISQUE scores for DDIM and DPM++ SDE variants even where convergence results favor other methods.

## Counterevidence & Qualifications
The evidence is a practitioner tutorial and a single presented benchmark rather than a controlled multi-model evaluation. It does not state enough configuration detail to reproduce the rankings, and it uses a 40-step output as a convergence reference even for stochastic methods that are not expected to approach one fixed output. BRISQUE is a no-reference natural-image metric, so its scores do not establish prompt adherence, aesthetics, semantic correctness, diversity, or human preference. Sampler availability, names, defaults, and implementations can also change after the article's 2023 publication and 2026 archive update.

## What Changed
- Created a sampler model that separates solver, stochasticity, schedule, step count, and model compatibility.
- Distinguished convergence, runtime, and perceptual score as different selection criteria.
- Added explicit benchmark and historical-version limits to the article's practical recommendations.

## Related Concepts
- [[DeepLearning]] - provides the learned predictor evaluated during each sampling update.
- [[PrincipalComponentAnalysis]] - supplies the article's lossy two-dimensional view of high-dimensional sampling trajectories.
- [[TextGenerationSampling]] - shares the term sampling but selects tokens from a probability distribution rather than numerically reversing an image diffusion process.
- [[DimensionalityReduction]] - frames what is lost when latent trajectories are projected for visualization.

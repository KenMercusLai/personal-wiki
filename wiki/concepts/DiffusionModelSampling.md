---
title: "Diffusion Model Sampling"
type: concept
tags: [diffusion-models, image-generation, numerical-methods, sampling]
sources:
  - stable-diffusion-samplers-a-comprehensive-guide-stable-diffusion-art
  - 2605.18736
  - 2609.37969
last_updated: 2026-10-13
knowledge_schema: synthesis-v1
---

## Definition
[[DiffusionModelSampling]] is the inference-time process that converts an initial noisy state into a generated result by repeatedly applying a learned noise, denoised-state, or velocity prediction according to a numerical solver, noise or flow schedule, and computational representation schedule.

## Current Synthesis
The available evidence separates choices that sampler names often compress together: the numerical update rule, whether fresh noise is introduced, the schedule of noise or flow time, step count, the resolution and token representation used at each stage, and compatibility with the trained model. A learned [[DeepLearning]] model predicts noise, a cleaner state, or a velocity field; the sampler decides how to traverse that field. Euler is a simple deterministic first-order update, Heun trades a second model evaluation per step for a more accurate correction, multistep methods reuse prior evaluations, ancestral and SDE methods introduce stochasticity, and Karras-labelled variants alter the noise schedule rather than replacing the underlying solver.

These choices optimize different outcomes. Smaller scheduled changes can reduce discretization error, but more steps do not guarantee convergence when a method deliberately injects noise. Deterministic convergence supports repeatable refinement, while stochastic paths can yield useful variations. Runtime depends on the number, order, and token count of model evaluations, and perceptual quality is distinct from convergence: an image can look good without approaching a fixed high-step result. Specialized LCM sampling adds a model constraint because it is not a universal drop-in solver.

Resolution scheduling supplies a second efficiency axis through [[SpectralProgressiveDiffusion]]. Because low spatial frequencies carry more signal and emerge earlier than high-frequency detail, early evaluations can run on smaller grids; power-spectrum-derived transitions then inject the newly representable high-frequency noise and align the enlarged state before sampling continues. This can complement step reduction, but it introduces cross-resolution generalization assumptions and a separate quality-efficiency tolerance.

A cascaded alternative for generated video moves content and motion generation to a cheaper low-resolution grid, after which a separate [[SoLRefiner]] processes target-resolution tokens. Staged [[OneStepDiffusionDistillation]] compresses that refiner from a multi-step teacher to one model evaluation, while a tiny autoencoder and optimized attention and kernels address the now-visible encode, decode, and runtime overhead. This makes evaluation count, token count, pipeline boundaries, and non-model overhead jointly important: one NFE does not mean one cheap end-to-end operation, and the distilled result may remain below its multi-step teacher.

## Key Claims
- Sampler behavior is jointly determined by solver, stochasticity, noise schedule, step count, and the model it is designed to use.
- Early high-noise steps influence broad composition, while later low-noise steps make smaller refinements in the article's PCA-based interpretation.
- Deterministic convergence and visually appealing output are separate goals; stochastic methods may vary indefinitely with step count yet still produce good images.
- Higher-order correction can reduce numerical error per step but usually costs additional learned-model evaluations and therefore more runtime.
- Model-evaluation cost depends on token count as well as evaluation count; progressive resolution can avoid full-grid work while high frequencies remain noise-dominated.
- Frequency-derived resolution transitions are principled under simplified spectral assumptions, but aggressive tolerances can introduce ghosting, halos, and metric degradation.
- Cascaded video generation can move most sampling to a low-resolution base stage and reserve one target-resolution evaluation for refinement, trading some teacher quality for lower latency whose benchmark ranking remains conditional on prompts, models, implementation, hardware, baselines, and metrics.

## Evidence
- Denoising mechanism and trajectory: [[stable-diffusion-samplers-a-comprehensive-guide-stable-diffusion-art]] depicts predicted noise being subtracted repeatedly, plots large early and small late schedule changes, and projects an SDXL trajectory into two PCA dimensions.
- Stochasticity and convergence: [[stable-diffusion-samplers-a-comprehensive-guide-stable-diffusion-art]] compares Euler with Euler ancestral animations and reports nonconvergent ancestral and DPM++ SDE curves against deterministic families.
- Cost and accuracy: [[stable-diffusion-samplers-a-comprehensive-guide-stable-diffusion-art]] reports that two-evaluation methods form a roughly 2x runtime tier, while DPM Adaptive is slower still because it selects its own steps.
- Schedule and method families: [[stable-diffusion-samplers-a-comprehensive-guide-stable-diffusion-art]] distinguishes Euler, Heun, LMS, DDIM, DPM/DPM++, UniPC, Karras schedules, and LCM-specific sampling.
- Quality versus convergence: [[stable-diffusion-samplers-a-comprehensive-guide-stable-diffusion-art]] shows low BRISQUE scores for DDIM and DPM++ SDE variants even where convergence results favor other methods.
- Resolution and spectral scheduling: [[2605.18736]] derives a power-spectrum-based progressive-resolution schedule, preserves existing low-frequency state during expansion, and reports image and video acceleration with model- and regime-dependent quality changes.
- Training-free versus adapted sampling: [[2605.18736]] applies its schedule directly to pretrained models, then shows that trajectory-matched LoRA fine-tuning can recover part of the resulting quality gap.
- Cascaded one-step refinement: [[2609.37969]] reports that a distilled one-step refiner plus TAE and Sol-Engine reduces measured 2K refinement latency from 57.461 to 6.447 seconds, while its 23-step variant retains higher aggregate quality.

## Counterevidence & Qualifications
The solver evidence is a practitioner tutorial and a single presented benchmark rather than a controlled multi-model evaluation. It does not state enough configuration detail to reproduce the rankings, and it uses a 40-step output as a convergence reference even for stochastic methods that are not expected to approach one fixed output. BRISQUE is a no-reference natural-image metric, so its scores do not establish prompt adherence, aesthetics, semantic correctness, diversity, or human preference. Sampler availability, names, defaults, and implementations can also change after the article's 2023 publication and 2026 archive update.

The progressive-resolution evidence is a first-party paper covering four backbones and selected automated metrics. Its activation derivation simplifies spectral coefficients as Gaussian and monotonically power-ordered, while training-free use assumes the model generalizes across chosen resolutions. Reported wall-clock gains are hardware- and implementation-dependent, some quality metrics decline, aggressive tolerances create visible artifacts, and the video experiments do not schedule temporal frequencies.

One-step refinement is supported by first-party evidence coupling distillation with a new benchmark, TAE, sparse attention, kernel fusion, and hardware-specific measurements. Its frame rewards do not directly assess long-range consistency, the 23-step teacher remains better on VBench and UniPercept averages, and large semantic, geometric, or motion errors are outside the stated objective. The reported 8.91x refinement and 27.03x end-to-end gains use different pipelines and baselines and should not be treated as universal sampler ratios.

## What Changed
- Expanded the sampling model to include resolution, token count, and velocity prediction alongside solver, stochasticity, time schedule, and step count.
- Added frequency-guided progressive resolution as a complementary acceleration axis rather than treating fewer steps as the only route to lower cost.
- Qualified analytic transition schedules by their distributional assumptions, cross-resolution model compatibility, and measured quality tradeoffs.
- Added cascaded one-step video refinement as a distinct way to reduce target-resolution model evaluations.
- Separated model-evaluation reduction from encoding, decoding, attention, kernel, hardware, and teacher-quality effects.

## Related Concepts
- [[DeepLearning]] - provides the learned predictor evaluated during each sampling update.
- [[PrincipalComponentAnalysis]] - supplies the article's lossy two-dimensional view of high-dimensional sampling trajectories.
- [[TextGenerationSampling]] - shares the term sampling but selects tokens from a probability distribution rather than numerically reversing an image diffusion process.
- [[DimensionalityReduction]] - frames what is lost when latent trajectories are projected for visualization.
- [[SpectralProgressiveDiffusion]] - changes the spatial representation and token count along the denoising trajectory.
- [[VideoRefinement]] - moves high-resolution detail recovery into a separate post-generation stage.
- [[OneStepDiffusionDistillation]] - compresses a multi-step refiner into one learned-model evaluation.
- [[CompressedSparseAttention2]] - exemplifies reducing attention work within fixed token sequences rather than changing spatial resolution over time.

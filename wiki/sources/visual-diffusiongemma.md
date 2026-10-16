---
title: "A Visual Guide to DiffusionGemma"
type: source
tags: [ai, language-models, diffusion, inference, visual-explainer]
date: 2026-06-10
source_file: "/mnt/ken_personal_wiki/Articles/visual-diffusiongemma.md"
---

## Summary
[[MaartenGrootendorst]] explains [[DiffusionGemma]] from the hardware motivation through discrete text diffusion, its shared Gemma 4 encoder-denoiser architecture, and its inference scheduler and sampler. The model spends otherwise idle batch-one compute on parallel 256-token canvas refinement, uses uniform random tokens rather than masks so any position can be revised, and combines causal prompt encoding with bidirectional denoising, self-conditioning, blockwise generation, temperature scheduling, adaptive stopping, and entropy-bounded token acceptance. The article is an illustrated conceptual guide rather than a benchmark or primary model report, so its performance and quality characterizations remain qualitative.

## Key Claims
- Autoregressive decoding loads model weights for every emitted token and can amortize that memory traffic across users, whereas text diffusion spends more arithmetic per pass to update many positions for one user; this can reduce single-request sequential latency while sacrificing multi-user throughput.

![Autoregressive decoding emits one token per forward pass and repeatedly manages model weights](../../wiki-assets/visual-diffusiongemma/autoregressive-token-decoding.png)

- DiffusionGemma repeatedly improves a 256-token canvas, allowing high-confidence context to anchor later revisions, so it can generate a block with fewer forward passes than its token count.

![DiffusionGemma iteratively revises every position until a noisy canvas becomes coherent text](../../wiki-assets/visual-diffusiongemma/parallel-canvas-refinement.png)

- Masked diffusion replaces selected tokens with `[MASK]` during forward diffusion and accepts confident replacements during reverse diffusion, but accepted tokens become fixed and cannot later self-correct.

![Masked text diffusion replaces a selected fraction of tokens with mask tokens](../../wiki-assets/visual-diffusiongemma/masked-diffusion-noising.png)

- Uniform-state diffusion instead corrupts text with random vocabulary tokens, predicts every position at every step, retains sufficiently confident candidates, and re-noises uncertain positions; previously accepted positions can still change when later context lowers their confidence.

![Uniform-state diffusion revises any canvas position across successive denoising steps](../../wiki-assets/visual-diffusiongemma/uniform-state-token-revision.png)

- Compared with autoregression, the guide characterizes text diffusion as parallel within a canvas, revisable at every position, compute-bound rather than memory-bound, and optimized for low per-user latency rather than high concurrent-user throughput.

![Table comparing autoregressive and diffusion text generation across order, revision, bottleneck, and latency](../../wiki-assets/visual-diffusiongemma/autoregression-vs-text-diffusion.png)

- One Gemma 4 26B A4B checkpoint serves two roles: causal attention encodes the query into a reusable KV cache, while bidirectional attention denoises the random canvas and applies the LM head at every position. Soft self-conditioning converts the prior step's full probability distributions to weighted embeddings, passes them through a small feedforward network, and adds them to the next step's token embeddings.

![Full DiffusionGemma architecture with causal encoder KV cache, bidirectional denoiser, and self-conditioning](../../wiki-assets/visual-diffusiongemma/diffusiongemma-architecture.png)

- Outputs longer than 256 tokens use block diffusion: a completed canvas is appended to the causal prefix, its KV state is extended, and a new 256-token canvas is denoised until a stop token ends generation.

![Sequential 256-token canvases combine diffusion within blocks with autoregression between blocks](../../wiki-assets/visual-diffusiongemma/block-diffusion-generation.png)

- The scheduler controls maximum step count, samples from temperature-adjusted logits, lowers temperature from 0.8 toward 0.4 over 48 illustrated steps, and can stop early when argmax predictions are stable and mean entropy is sufficiently low.

![Worked temperature schedule decreasing from exploration early in denoising to sharper later predictions](../../wiki-assets/visual-diffusiongemma/temperature-schedule.png)

![Early denoising steps emphasize exploration while later steps emphasize exploitation](../../wiki-assets/visual-diffusiongemma/exploration-to-exploitation.png)

- The default entropy-bounded sampler sorts positions from lowest to highest entropy and accepts a growing confident set while cumulative entropy minus its maximum stays within a configured bound; rejected positions are replaced by fresh uniform noise.

![Worked entropy-budget example accepting two low-entropy tokens and rejecting the next](../../wiki-assets/visual-diffusiongemma/entropy-bounded-acceptance.png)

![Entropy-bounded sampler accepts confident predictions and re-noises rejected positions for the next step](../../wiki-assets/visual-diffusiongemma/entropy-bounded-renoising-loop.png)

## Key Quotes
> "This is where iterative refinement comes in." - on turning an initially poor parallel prediction into coherent text through repeated passes.

> "As such, the canvases are generated using diffusion but are stitched together sequentially." - on combining within-block diffusion with between-block autoregression.

## Connections
- [[DiffusionGemma]] - the Gemma 4-based model whose architecture and inference loop the guide explains.
- [[DiffusionLanguageModels]] - the broader family of iterative discrete-token denoisers contrasted with autoregressive generation.
- [[MaartenGrootendorst]] - author and visual explainer.
- [[AttentionMechanism]] - switches between causal query encoding and bidirectional canvas denoising.
- [[TextGenerationSampling]] - encompasses temperature, multinomial choice, entropy, acceptance, re-noising, and stopping decisions.
- [[DiffusionModelSampling]] - supplies the forward-noising and reverse-denoising analogy from image generation.

## Contradictions
- No direct contradiction with the existing wiki was found. The guide complements [[diffusion-gemma]] with a more granular conceptual account of masked versus uniform-state diffusion, temperature scheduling, and entropy-budget acceptance.
- The article calls the single-user result "much much faster" and says the output converges to quality similar to regular Transformers, but supplies no measured latency, quality, throughput, energy, or hardware table. Those statements should not override the qualified first-party benchmark limits already recorded in [[DiffusionGemma]].
- The text gives an adaptive-stopping confidence threshold of 0.005 and stability threshold of 1, while the entropy-acceptance illustration uses a default bound of 0.1; these govern different decisions and must not be conflated.
- Some diagrams use abbreviated toy sequences, and the article's 12-16 or 48 illustrated forward-pass counts are explanatory configurations rather than a demonstrated universal convergence requirement.

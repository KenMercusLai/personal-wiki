---
title: "Diffusion Language Models"
type: concept
tags: [ai, language-models, diffusion, inference]
sources:
  - diffusion-gemma
last_updated: 2026-10-16
knowledge_schema: synthesis-v1
---

## Definition
[[DiffusionLanguageModels]] generate text by repeatedly refining a noisy discrete-token canvas, potentially updating many positions per model evaluation, rather than irrevocably emitting one next token at a time.

## Current Synthesis
[[DiffusionGemma]] realizes block diffusion with a fixed 256-token canvas. Prompt and completed blocks form a causal committed prefix, while positions within the active canvas attend bidirectionally and are refined in parallel. The design therefore relaxes autoregression within a block but not across blocks.

Each step proposes a token distribution at every position. An entropy budget retains the most confident samples and renoises the rest; the previous full distributions are also fed back through soft self-conditioning. A block commits the stable low-entropy argmax prediction, not the noisy working canvas. This converts extra parallel compute into fewer sequential model passes, a favorable exchange when batch size is low and memory bandwidth rather than arithmetic is limiting.

Serving requires phase-aware state rather than only a different model forward. The implementation tracks canvas, phase, self-conditioning probabilities, and convergence history; changes masks between causal and bidirectional modes; and prevents intermediate denoise passes from advancing the committed KV position.

## Key Claims
- Parallel canvas refinement exchanges additional computation per forward pass for fewer sequential decoding passes.
- Bidirectional attention applies only within the active block, while committed blocks preserve left-to-right dependence.
- Entropy-bounded acceptance turns confident positions into anchors and resamples uncertain positions.
- Soft self-conditioning carries the prior prediction forward even when working tokens are replaced by random noise.
- Correct serving must distinguish denoise state from committed sequence state and advance KV only on commit.
- Performance depends on block size, convergence steps, batch load, memory bandwidth, attention kernels, and stopping criteria.

## Evidence
- Generation structure: [[diffusion-gemma]] contrasts one-token autoregression with repeated denoising and whole-block commit.
- Denoising mechanism: [[diffusion-gemma]] shows progressive retention under a cumulative entropy budget and convergence on a clean argmax canvas.
- State feedback: [[diffusion-gemma]] diagrams probability-weighted previous-step embeddings entering a gated residual.
- Serving semantics: [[diffusion-gemma]] documents phase-aware ModelState hooks, zero logical advance during denoising, and causal KV writes during commit.
- Performance boundary: [[diffusion-gemma]] reports large batch-one generation-rate gains on H100 and H200 under one FP8 configuration.

## Counterevidence & Qualifications
The source covers one model, one 256-token block design, and one serving implementation. It does not show that diffusion language models generally match autoregressive quality, dominate at higher batch sizes, converge in a predictable number of steps, or use less total compute or energy. Reported speed excludes prefill and may depend on always producing a large block; output truncation, early end-of-sequence, difficult prompts, and conservative entropy thresholds can reduce the practical advantage. "Diffusion" here refers to discrete iterative token denoising and should not be assumed to share every mechanism or guarantee of continuous visual diffusion models.

## What Changed
- Created a language-specific diffusion concept centered on block causality, confidence-based denoising, self-conditioning, and serving state.
- Separated parallelism within a canvas from the causal ordering between committed blocks.

## Related Concepts
- [[LanguageModeling]] - supplies the token distributions that the denoising loop repeatedly refines.
- [[TextGenerationSampling]] - controls candidate drawing, temperature, confidence, and final token selection.
- [[AttentionMechanism]] - provides bidirectional within-block context and causal committed-prefix processing.
- [[SpeculativeDecoding]] - offers a reusable scheduling protocol, though no separate target verifies DiffusionGemma's canvas.
- [[DiffusionModelSampling]] - related iterative denoising family in continuous visual-generation settings.

---
title: "DiffusionGemma"
type: entity
tags: [ai, language-models, diffusion, inference]
sources:
  - diffusion-gemma
last_updated: 2026-10-16
knowledge_schema: synthesis-v1
---

## Overview
[[DiffusionGemma]] is a 26B-parameter discrete diffusion language model built on a Gemma4 backbone and served in [[VLLM]] through alternating causal encode and bidirectional denoise phases.

## Current Profile
DiffusionGemma generates 256-token blocks rather than committing one token after each forward pass. It prefills a prompt causally into the KV cache, initializes a random canvas, repeatedly denoises every canvas position with bidirectional attention, and commits a converged clean argmax block through a final causal pass. Later blocks remain left-to-right because they condition on the committed prefix.

The model combines entropy-bounded token retention, convergence checks, and soft self-conditioning. vLLM hosts this behavior in per-request state and a custom sampler while reusing its scheduler, runner, prefix cache, and speculative-decoding accounting.

## Key Characteristics
- Uses one Gemma4 weight set in causal encoder and bidirectional decoder modes.
- Refines and commits fixed 256-token canvases block by block.
- Retains low-entropy candidate tokens while renoising less confident positions.
- Feeds previous-step token distributions back through a gated self-conditioning residual.
- Commits only after stable argmax predictions and low mean entropy, or a hard step limit.
- Supports FP8 and NVFP4 quantized checkpoints in compressed-tensors format.

## Evidence
- Architecture and generation: [[diffusion-gemma]] diagrams prompt prefill, full-canvas denoising, block commit, and cross-block causal dependence.
- Sampling and conditioning: [[diffusion-gemma]] documents entropy-bound acceptance, random renoising, convergence tests, and probability-distribution self-conditioning.
- Serving integration: [[diffusion-gemma]] maps model state and sampling into vLLM's existing speculative-decoding control path.
- Performance: [[diffusion-gemma]] reports 1,008 and 1,288 generation tokens/s at batch size one on H100 and H200 respectively for its FP8 checkpoint.

## Qualifications
The available evidence is a joint first-party launch article rather than an independent evaluation. Its throughput comparison excludes prefill, fixes 16 denoising steps, and uses a synthetic acceptance assumption for one baseline. The article does not show full quality tables, quality-latency curves, convergence distributions, high-concurrency results, energy, cost, long-output behavior, or how fixed block size interacts with early stopping.

## What Changed
- Created a model profile separating within-block parallel denoising from left-to-right block dependence.
- Recorded the shared-weight dual attention modes, entropy rule, self-conditioning, and vLLM execution contract.

## Relationships
- [[DiffusionLanguageModels]] - model family to which DiffusionGemma belongs.
- [[VLLM]] - serving engine providing the execution, cache, and scheduling substrate.
- [[DeepMind]] - co-developer named by the launch article.
- [[SpeculativeDecoding]] - infrastructure path reused for canvas accounting without a separate draft verifier.
- [[AttentionMechanism]] - alternates causal and bidirectional masks across generation phases.

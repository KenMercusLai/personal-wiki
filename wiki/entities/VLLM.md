---
title: "vLLM"
type: entity
tags: [ai, inference, serving, open-source]
sources:
  - diffusion-gemma
last_updated: 2026-10-16
knowledge_schema: synthesis-v1
---

## Overview
[[VLLM]] is an open-source language-model inference and serving engine represented here through its native integration of [[DiffusionGemma]].

## Current Profile
The integration presents vLLM as a reusable serving stack whose scheduler, GPU model runner, KV cache, prefix cache, and speculative-decoding data path can host a non-autoregressive model without being forked. Model-specific behavior lives in a ModelState with input, attention, sampler, and request-lifecycle hooks plus a custom diffusion sampler.

Supporting mixed prefill, denoise, and commit phases required attention-kernel changes: causality became a per-sequence property in Triton Attention and FlashAttention 4, and sliding-window bounds became symmetric for bidirectional canvases. The generic runner and scheduler remain shared.

## Key Characteristics
- Exposes ModelState hooks for model-specific input preparation, attention metadata, sampling, and request state.
- Reuses speculative-decoding scheduling and accounting for iterative diffusion steps.
- Preserves ordinary causal KV writes, enabling automatic prefix caching without a diffusion-specific cache design.
- Supports mixed causal and bidirectional requests inside one batch through per-sequence mask metadata.
- Implements the required dynamic masking in Triton Attention and FlashAttention 4.
- Keeps model-specific canvas and self-conditioning state in preallocated GPU tensors.

## Evidence
- Extension boundary: [[diffusion-gemma]] shows DiffusionGemmaModelState and DiffusionSampler as the principal new components around an unchanged scheduler, runner, and Gemma4 backbone.
- Accounting reuse: [[diffusion-gemma]] explains zero sampled tokens and full rejection during denoising, followed by a 256-token commit.
- Cache behavior: [[diffusion-gemma]] states that ordinary causal prompt and commit writes make prefix caching reusable without diffusion-specific changes.
- Kernel behavior: [[diffusion-gemma]] diagrams per-request causal and bidirectional masks and the corresponding asymmetric or symmetric sliding windows.

## Qualifications
This profile is source-bounded to one jointly authored integration article and is not a general audit of vLLM's architecture, model coverage, reliability, APIs, or comparative serving performance. The claim that future block-diffusion models need only a ModelState and registration assumes their execution and sampling requirements fit the exposed hooks and attention backends.

## What Changed
- Created a profile centered on the ModelState extension boundary and reuse of serving infrastructure.
- Recorded dynamic per-sequence causal and sliding-window attention as the main shared-kernel change.

## Relationships
- [[DiffusionGemma]] - first diffusion language model described as natively supported by the engine.
- [[DiffusionLanguageModels]] - model family whose iterative state motivates the ModelState extension.
- [[SpeculativeDecoding]] - data path reused to keep denoising stationary and advance only on commit.
- [[AttentionMechanism]] - kernel layer extended from batch-wide to per-sequence causality.
- [[KVCacheCompression]] - adjacent serving concern; this source instead preserves and reuses ordinary causal cache semantics.

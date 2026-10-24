---
title: "DeepSeek V4 Flash"
type: entity
tags: [ai, language-model, mixture-of-experts, long-context, inference]
sources:
  - ds4-ascend
last_updated: 2026-10-24
knowledge_schema: synthesis-v1
---

## Overview
[[DeepSeekV4Flash]] is the model artifact targeted by [[DwarfStar]], described in the source as a 284-billion-parameter sparse mixture-of-experts model with multi-head latent attention and low-bit routed experts.

## Current Profile
The source reports about 37 billion active parameters per token, an approximately 81 GB package, and IQ2_XXS or Q2_K routed experts alongside higher-precision shared experts, projections, and routing. Its attention path stores compressed K/V latent vectors, while DwarfStar separates parallel prompt prefill from one-token decode and can persist compressed prefix state to disk.

## Key Characteristics
- Uses multi-head latent attention to compress stored key-value state before attention-time expansion.
- Activates a sparse subset of routed experts plus shared-expert work for each token.
- Applies the most aggressive two-bit quantization to routed experts rather than uniformly across the model.
- Is served by a deliberately specialized engine and packaged GGUF artifact rather than a generic runtime path.
- Supports persistent compressed KV state and exact rendered-prefix reuse in the described engine.

## Evidence
- Scale and activation: [[ds4-ascend]] reports 284B total parameters and about 37B active per token.
- Quantization layout: [[ds4-ascend]] places IQ2_XXS or Q2_K on routed experts while retaining higher precision elsewhere.
- Attention and cache: [[ds4-ascend]] describes compressed K/V latents, an approximate 8:1–10:1 reduction, and persistent prefix state.
- Runtime scope: [[ds4-ascend]] says DwarfStar targets this model and one specially packaged GGUF format rather than general model loading.

## Qualifications
All specifications come from one implementation report rather than a primary model technical report or independently reproduced artifact. The article does not derive the counts or compression ratio, and its model name must not be conflated with the separate [[DeepSeekV41Flash]] profile, whose reported size, active parameters, cache design, and wider multimodal architecture differ materially.

## What Changed
- Created a distinct model profile to prevent DeepSeek V4 Flash claims from being merged into DeepSeek-V4.1-Flash.

## Relationships
- [[DwarfStar]] - specialized local inference engine built for this model.
- [[KVCacheCompression]] - compressed latent attention state reduces long-context storage and transfer.
- [[MixtureOfExpertsLoadBalancing]] - adjacent execution problem for the model's sparse routed experts.
- [[BlockQuantization]] - related low-precision design space, although the source does not fully specify IQ2_XXS internals.
- [[DeepSeekV41Flash]] - later, separately represented model profile with materially different reported specifications.

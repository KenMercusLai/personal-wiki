---
title: "把 Redis 作者的 ds4 移植到昇腾 Atlas 300i Duo 上"
type: source
tags: [ai, inference, ascend, mixture-of-experts, kv-cache, kernel-porting]
date: 2026-05-20
source_file: /mnt/ken_personal_wiki/Articles/ds4-ascend.md
---

## Summary
[[Donge]] reports a functionally aligned but very slow port of [[DwarfStar]] from its Metal and CUDA backends to Huawei's Ascend platform on an Atlas 300i Duo. The article uses the port to explain [[DeepSeekV4Flash]] inference through multi-head latent attention, sparse MoE execution, persistent compressed KV state, and separate prefill and decode paths. Its strongest engineering result is negative but useful: falling back to CPU-side IQ2_XXS dequantization, repeated Host-to-Device transfers, and one of the card's two 48 GB devices produces a reported 0.1–0.3 token/s, making native low-bit kernels and cross-device weight placement prerequisites for practical performance.

## Key Claims
- [[DwarfStar]] is a model-specific C inference engine for [[DeepSeekV4Flash]], not a general GGUF runtime; hard-coding one model and packaging format keeps its execution path small and direct.
- The article describes multi-head latent attention as storing a shared compressed K/V latent and expanding it for attention work, reporting an approximate 8:1–10:1 cache reduction and about 26 GB for a million-token context on an M3 Max.
- The described 284B-parameter MoE activates about 37B parameters per token and quantizes routed experts to IQ2_XXS or Q2_K while keeping shared experts, projections, and routing at higher precision, yielding an approximately 81 GB package.
- Inference proceeds through embedding lookup, repeated RMSNorm, latent attention, routed MoE feed-forward work, final normalization, vocabulary projection, and sampling; prefill processes prompt tokens in parallel while decode advances one token at a time.
- DwarfStar persists compressed KV state in a custom binary file containing a 48-byte header, rendered prefix text, and tensors; exact DSML tool-call replay preserves byte-identical prefix matching for cache reuse.
- The Ascend backend implements the interface in `ds4_gpu.h` through AscendCL and needs GEMM, RMSNorm, RoPE, softmax, and low-bit matrix multiplication support.
- The current port dequantizes IQ2_XXS weights to FP16 on the CPU and transfers them to the NPU for ordinary GEMM. Repeating that transfer and streaming layers through one 48 GB device is identified as the principal cause of the reported 0.1–0.3 token/s result.
- The author reports output alignment with the CPU path and proposes native NPU dequantization, two-die weight partitioning, and batched prefill attention as the next steps.

## Key Quotes
> “非常慢，但流程跑通了。” — the article's concise distinction between functional completion and practical performance.

> “量化 kernel 是核心瓶颈” — the author's diagnosis after moving low-bit expert weights through a CPU dequantization path.

## Connections
- [[Donge]] - author and implementer of the Ascend port.
- [[DwarfStar]] - specialized inference engine whose backend interface is ported.
- [[DeepSeekV4Flash]] - model whose latent-attention and sparse-expert execution path the engine targets.
- [[Huawei]] - vendor of the Ascend 310P platform and CANN software stack used by the port.
- [[KVCacheCompression]] - compressed latent state and persistent prefix reuse reduce long-context storage and repeated prefill.
- [[FoundationModelKernelOptimization]] - explains why native dequantization, data placement, and end-to-end profiling matter more than nominal NPU GEMM capability.
- [[AcceleratorBackendPorting]] - broader practice of preserving model semantics while replacing device APIs, kernels, memory movement, and placement.
- [[Antirez]] - Redis creator and original DwarfStar author.

## Contradictions
- The article's [[DeepSeekV4Flash]] specification—284B total parameters, about 37B active, and an approximately 81 GB package—must not be merged with the wiki's later [[DeepSeekV41Flash]] profile, which reports 552B total parameters and 8B/16B active during prefill/decode. The names denote different reported model versions or artifacts.
- Output alignment with the CPU path is asserted without prompts, tolerances, token-by-token traces, sampling controls, or a released validation report, so it supports a first-party correctness claim rather than independent verification.
- The 0.1–0.3 token/s Ascend result and “tens of tokens per second” Mac comparison omit exact model artifact, context length, CANN version, kernel mix, power state, and benchmark protocol. They diagnose this implementation but do not establish a general Ascend-versus-Metal performance ranking.
- The reported cache ratio, million-token memory use, parameter counts, precision mix, and package size are not derived or independently reproduced in the article. Cache accounting may also vary with layers, metadata, local state, and precision.
- No effective image references appear in the supplied Markdown, so no visual assets or manifest were required.

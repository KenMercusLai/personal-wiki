---
title: "LLM Inference Systems"
type: concept
tags: [llm, inference, systems-programming, performance]
sources:
  - how-to-llm-inference
last_updated: 2026-10-25
knowledge_schema: synthesis-v1
---

## Definition
[[LLMInferenceSystems]] are runtimes that turn a model artifact and token sequence into generated tokens by coordinating representation, tensor execution, reusable state, hardware instructions, and request-level performance constraints.

## Current Synthesis
The source presents local inference as a chain whose constraints must agree. GGUF metadata defines tensor shapes and per-tensor formats; the tokenizer defines integer inputs; embedding and layer blocks preserve a model-width activation; vocabulary projection produces logits; and sampling closes the autoregressive loop. Static Rust types can encode tensor dimensions and quantization formats so many invalid combinations fail before runtime.

Performance divides sharply by activation shape. Prompt prefill uses a multi-row activation and can reuse weight tiles, raising arithmetic intensity toward a compute limit. Decode uses one row, streams each weight with little reuse, and tends toward the memory-bandwidth ceiling. Quantization is therefore an execution format as well as a storage format: direct Q4_K-by-Q8_K integer dot products avoid expanding weights to fp32, while scales reconstruct the numerical result around hardware-supported reductions.

State reuse adds a second axis. Attention KV grows with context, DeltaNet keeps fixed per-layer state, and exact shared prefixes can reuse already computed rows. The complete runtime must therefore optimize model bytes, transient activation formats, state growth, prefix identity, SIMD kernels, fusion, and thread ownership together rather than treating matrix multiplication as an isolated primitive.

## Key Claims
- Artifact metadata, tokenizer behavior, tensor shapes, quantization formats, sampling, and state reuse form one correctness boundary.
- Prefill GEMM and decode GEMV require different schedules because weight reuse changes arithmetic intensity and the active hardware bottleneck.
- Direct quantized computation can preserve compression's bandwidth benefit; eager fp32 expansion can erase it before multiplication begins.
- Available instructions constrain useful operand formats, so efficient kernels often adapt stored weights and runtime activations to a supported dot-product path.
- Attention and recurrent-style layers impose different context-state growth, changing long-context capacity and cache policy.
- Kernel bandwidth near a hardware ceiling is meaningful only when connected to end-to-end token throughput and output correctness.

## Evidence
Execution boundary:
- [[how-to-llm-inference]] walks one GGUF artifact through model-specific tokenization, typed tensor layers, logits, sampling, and autoregressive state.

Shape-dependent bottlenecks:
- [[how-to-llm-inference]] distinguishes `[n, 2048]` prefill GEMM from `[1, 2048]` decode GEMV and reports 117.7 versus 15.1 tokens/s in the selected workload.

Representation-instruction alignment:
- [[how-to-llm-inference]] converts bf16 activations to Q8_K and combines them with unpacked Q4_K weights through CPU integer dot products rather than materializing fp32 weights.

State and reuse:
- [[how-to-llm-inference]] reports 2 KB per token per attention layer, fixed 2 MB state per DeltaNet layer, and exact-prefix slicing of cached K/V rows.

## Counterevidence & Qualifications
The available evidence is one dependency-free educational runtime specialized to one model and CPU. It omits GPU execution, speculative decoding, general model compatibility, production batching, scheduling, fault handling, and comparative quality validation. The source supplies end-to-end and kernel timings but not the CPU model, thread count, raw benchmark harness, accuracy checks, energy, or comparison runtime. Its tensor-shape figure also conflicts with the prose on vocabulary width. These measurements support the architectural relationships, not a universal performance ranking.

## What Changed
- Created a systems-level synthesis connecting artifact layout, tensor shape, quantized execution, autoregressive state, and hardware bottlenecks.
- Distinguished prefill's reuse-driven compute regime from decode's streaming bandwidth regime.

## Related Concepts
- [[BlockQuantization]] - supplies compact weight and activation representations consumed by inference kernels.
- [[ArithmeticIntensity]] - predicts when reuse shifts execution between bandwidth and compute limits.
- [[FoundationModelKernelOptimization]] - broadens the local CPU case into accelerator, graph, and distributed co-design.
- [[OperatorFusion]] - removes compatible intermediate traffic and instruction boundaries inside the runtime.
- [[PromptCaching]] - reuses stable-prefix computation across autoregressive requests.
- [[InferenceTokenization]] - maps text and chat structure into the model-specific integer sequence.
- [[KVCacheCompression]] - reduces one growing component of autoregressive serving state.

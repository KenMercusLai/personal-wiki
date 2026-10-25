---
title: "Qwen3.6-35B-A3B"
type: entity
tags: [llm, qwen, mixture-of-experts, deltanet, gguf]
sources:
  - how-to-llm-inference
last_updated: 2026-10-25
knowledge_schema: synthesis-v1
---

## Overview
[[Qwen36_35BA3B]] is the sparse mixture-of-experts language model used by the available source to demonstrate a model-specific CPU inference engine over a quantized GGUF artifact.

## Current Profile
The represented artifact contains about 34.66B parameters in 20.60 GiB and routes approximately 3.3B parameters for each token. Forty layers repeat a three-DeltaNet plus one-attention pattern ten times, with an MoE block after each sequence layer. The 256-expert MoE routes each token to eight experts, causing expert weights to dominate stored size without making every parameter active on every step.

The artifact mixes six tensor formats and is dominated by Q4_K storage. Its attention layers accumulate linearly growing K/V state, while its DeltaNet layers hold fixed-size recurrent state. The implementation is deliberately scoped to this one artifact rather than presented as a general Qwen runtime.

## Key Characteristics
- Contains about 34.66B total parameters with roughly 3B active per token under the source's approximate accounting.
- Uses 40 layers arranged as ten repetitions of three DeltaNet blocks and one attention block, each paired with an MoE block.
- Routes eight of 256 experts per token, while MoE weights account for 89.4% of the reported stored model size.
- Uses a 2,048-wide activation and two 256-dimensional KV heads in each attention layer.
- Is represented as a roughly 21.6 GB mixed-precision GGUF artifact dominated by Q4_K weights.

## Evidence
Architecture and parameter distribution:
- [[how-to-llm-inference]] diagrams the repeated hybrid stack and reports component parameter counts, stored bytes, expert routing, and approximate active-parameter arithmetic.

Runtime representation:
- [[how-to-llm-inference]] enumerates 753 tensors across BF16, F32, Q4_K, Q5_K, Q6_K, and Q8_0 and explains per-tensor dtype selection.

State behavior:
- [[how-to-llm-inference]] reports 20 KB of additional KV memory per token across ten attention layers and fixed 2 MB state for each DeltaNet layer.

## Qualifications
This profile comes from one practitioner article and one Unsloth-quantized artifact, not an official architecture audit. The source says its approximate 3.3B active calculation differs from the official convention. Its prose gives a 151,936-token vocabulary, while the retained tensor-life figure labels 248,320. No output-quality, perplexity, architecture-ablation, or comparison-runtime evidence is provided, and the engine omits the model's MTP path.

## What Changed
- Created a source-bounded profile of the model's hybrid DeltaNet-attention-MoE structure, mixed quantization, and per-layer state.

## Relationships
- [[QwenTeam]] - research organization associated with the model family.
- [[LLMInferenceSystems]] - runtime layer demonstrated by implementing this specific model.
- [[BlockQuantization]] - representation family used across the GGUF artifact.
- [[KVCacheCompression]] - adjacent concern for the model's linearly growing attention state.
- [[MixtureOfExpertsLoadBalancing]] - related routing concern for its 256-expert MoE blocks.

---
title: "Speculative Decoding"
type: concept
tags: [ai, llm, inference, decoding]
sources:
  - wechat-rrhg9uccinsc-zecigjnbq
  - diffusion-gemma
last_updated: 2026-10-16
knowledge_schema: synthesis-v1
---

## Definition
[[SpeculativeDecoding]] accelerates autoregressive generation by letting a cheaper draft process propose several future tokens and letting the target model verify those proposals in parallel, accepting a contiguous prefix and supplying a correction when the first proposal fails.

## Current Synthesis
Speculative decoding is useful when one target-model verification pass can evaluate several positions for less wall time than generating those positions one by one. Its value is therefore not determined by draft accuracy alone. Expected accepted tokens per cycle must be weighed against draft latency, verification latency, proposal length, batch size, and the opportunity cost of verification slots under concurrency.

Exact speculative sampling preserves the target distribution through rejection sampling: a proposed token is accepted with probability bounded by the target-to-draft probability ratio, and rejection draws from the target distribution's positive residual over the draft distribution. Greedy implementations can instead compare proposed and target argmax tokens, but alternative sample-and-compare schemes do not automatically retain distributional exactness at nonzero temperature.

Draft architectures move along a causality-efficiency frontier. Autoregressive drafts condition well on the sampled prefix but pay serial cost per proposed token. Parallel heads or diffusion blocks draft many positions at once but can combine individually plausible tokens into an incoherent suffix. Token trees increase candidate coverage at additional verification cost. [[DSpark]] occupies a hybrid point: one parallel backbone supplies high-capacity base logits while a small sequential head restores local prefix dependence, and a load-aware scheduler verifies only prefixes with sufficient expected system return.

The [[DiffusionGemma]] integration shows that the same serving data path can also act as an execution protocol rather than a target-versus-draft algorithm. Its active 256-token canvas is exposed as draft tokens, but every denoise step reports zero sampled tokens and rejects the whole query length so the scheduler resubmits the same logical position; only the final causal commit advances the KV cache and emits tokens. This reuse does not make diffusion denoising distribution-exact speculative verification because no separate target model accepts or corrects a draft prefix.

## Key Claims
- Correct rejection-and-residual sampling can make speculative generation distribution-equivalent to direct target-model sampling.
- Accepted output is prefix-structured: rejection at one position invalidates every later proposal that depended on it.
- Speed is governed jointly by expected accepted length, draft cost, target verification cost, proposal length, and calibrated estimates that allocate verification under current load.
- Autoregressive, parallel, multi-head, and tree drafts trade serial dependence, capacity, candidate breadth, and verification work differently.
- The first draft position has disproportionate value because an early rejection destroys the entire remaining prefix.
- At high concurrency, additional verification tokens have nonzero opportunity cost even when they are cheap for a single memory-bound request.
- The speculative-decoding data path can support non-verification workflows when its sampled/rejected counts correctly represent whether committed sequence state advances.

## Evidence
- Correctness and performance model: [[wechat-rrhg9uccinsc-zecigjnbq]] derives prefix acceptance, residual correction, expected accepted length, and the acceptance-cost-length speedup relation.
- Architecture history: [[wechat-rrhg9uccinsc-zecigjnbq]] compares small autoregressive models, self-speculation, SpecInfer, Medusa, EAGLE, MTP, DFlash, DDTree, JetSpec, and DSpark.
- Parallel-versus-causal tradeoff: [[wechat-rrhg9uccinsc-zecigjnbq]] shows DFlash beginning with stronger acceptance than EAGLE-3 but decaying over later positions, while DSpark retains the stronger start and flatter suffix.
- Serving economics: [[wechat-rrhg9uccinsc-zecigjnbq]] models system throughput as expected accepted tokens times profiled steps per second at the chosen verification batch size.
- Production evidence: [[wechat-rrhg9uccinsc-zecigjnbq]] reproduces preview-system telemetry showing verification budgets contract as concurrency grows.
- Infrastructure reuse: [[diffusion-gemma]] maps iterative denoising onto vLLM's draft-token accounting, holding logical position fixed until a whole block commits.

## Counterevidence & Qualifications
The speedup equations rely on simplified timing and, in some forms, position-independent acceptance assumptions; real kernels, caches, batch shapes, and conditional acceptance vary by position and workload. High single-request speedup need not improve aggregate throughput. A confidence ranking is insufficient when the scheduler needs absolute expected returns, so miscalibration can route capacity poorly. The DSpark source's algorithm history mixes published results with author interpretation and code reading, and its outcomes have not been independently reproduced in this wiki. Distribution-exact rejection sampling must be distinguished from greedy equality checks, non-exact sample-and-compare verification, and DiffusionGemma's use of the same bookkeeping without a separate verifier.

## What Changed
- Created a unified account joining sampling correctness, draft architecture, expected accepted length, and concurrent-serving economics.
- Expanded the concept from draft verification to a serving protocol that can keep iterative model state stationary until commit.

## Related Concepts
- [[TextGenerationSampling]] - provides the probability distributions and temperature-dependent sampling behavior being accelerated.
- [[AttentionMechanism]] - enables parallel sequence verification, tree masks, and draft conditioning.
- [[DSpark]] - hybrid draft and scheduling system that addresses suffix decay and verification opportunity cost.
- [[InferenceHostOverhead]] - shows why accelerator progress can still be limited by the surrounding request-control path.
- [[KVCacheAwareRouting]] - complementary serving optimization that reduces prompt work rather than decode steps.
- [[VLLM]] - inference engine that reuses speculative accounting for DiffusionGemma's denoise-and-commit loop.

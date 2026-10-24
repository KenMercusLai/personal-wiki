---
title: "DeepSeek-V4.1-Flash"
type: entity
tags: [ai, multimodal-model, mixture-of-experts, long-context, inference]
sources:
  - ba-kv-cache-ya-suo-tui-dao-ji-zhi-zartbot
  - deepseek-v41-tech-report
last_updated: 2026-10-24
knowledge_schema: synthesis-v1
---

## Overview
[[DeepSeekV41Flash]] is DeepSeek-AI's reported 552B-backbone-parameter multimodal mixture-of-experts model for contexts up to one million tokens, designed to lower long-horizon agent serving cost through reduced prefill work, compressed KV state, and a 16B-parameter decode activation footprint.

## Current Profile
The 40-layer language backbone is divided into a 20-layer causal encoder and 20-layer decoder. [[CausalEncoderDecoderArchitecture]] projects decoder global KV from the final encoder state, while [[CompressedSparseAttention2]] shares global content and selected addresses across groups of layers. The model activates about 8B backbone parameters per prompt token and 16B per generated token, retains fresh 128-token sliding-window state, and uses a decoder candidate pool to bound most repeated indexing work.

The report attributes a global-cache footprint of 890 bytes per token—roughly one quarter of DeepSeek-V4-Flash—to cross-layer reuse and FP4 main KV. Short-lived SWA KV stays in host DRAM when available and can be approximately rebuilt from one recent window, allowing long-lived persistent cache to retain only global KV and reportedly fall to one eighth of the predecessor's footprint.

Around this cache-focused core, the model adds a 32-layer vision encoder, two 98B-parameter Engram modules, Single-Pass mHC, and [[DSpark]]. Pre-training uses a reported 45T-token multimodal corpus. Post-training uses conventional SFT, RL, and on-policy distillation but scales synthesized environments, asynchronous rollouts, over 40 teachers, effort-conditioned behavior, and preliminary multi-agent training.

## Key Characteristics
- Splits 40 backbone layers evenly between causal context production and autoregressive decoding, reducing long-prompt work.
- Uses CSA2 Full, Reindex, and Reuse modes to refresh global content, sparse addresses, and layer-specific queries at different rates.
- Combines cross-layer sharing and FP4 main KV for a reported 890-byte-per-token HBM-resident global cache.
- Separates long-lived global KV from short-lived local SWA state and uses approximate bounded replay on local-cache misses.
- Integrates native multimodal pre-training, conditional Engram memory, Single-Pass mHC residual mixing, and DSpark drafting.
- Learns a scalar reasoning-effort control and is evaluated across multiple agent scaffolds and multi-agent configurations.
- Derives its claimed post-training gains primarily from data, environment, and rollout scaling rather than a new RL algorithm.

## Evidence
Architecture and cache layout:
- [[deepseek-v41-tech-report]] specifies the 20/20 CED split, CSA2 layer schedules, 128-token local window, FP4 main KV, candidate pool, and 8B/16B activation counts; [[ba-kv-cache-ya-suo-tui-dao-ji-zhi-zartbot]] independently reconstructs the same component relationships from the report.

Runtime and persistent-cache behavior:
- [[deepseek-v41-tech-report]] reports 890 bytes of global KV per token, one-quarter predecessor global-cache use, one-eighth persistent-cache use, minute-scale SWA retention in 10% of host DRAM, and bounded replay after local misses.
- [[ba-kv-cache-ya-suo-tui-dao-ji-zhi-zartbot]] derives the 890-byte accounting from four FP4 main-KV and indexer-K sources.

Training and capability profile:
- [[deepseek-v41-tech-report]] documents the 45T-token corpus, vision-encoder stages, SFT–RL–distillation pipeline, benchmark settings, effort tiers, scaffold tests, and preliminary agent-team experiments.

System implementation:
- [[deepseek-v41-tech-report]] describes EPD disaggregation, fused-kernel paths, attention-sharing state across pipeline stages, multimodal image sharding, asynchronous rollout handling, and [[DSec]] at million-sandbox scale.

## Qualifications
The detailed architecture is now supported directly by a first-party technical report rather than only a secondary reconstruction, but performance, quality-retention, scale, and deployment-cost claims still lack independent reproduction. The report does not isolate the causal contribution of each architecture or data component, fully disclose training data, or characterize all sparse-selection and replay-boundary failures. Its broad “over 95% of real-world tasks” claim has no defined task distribution, while the report itself records gaps on science-heavy agents, difficult reasoning, visual tasks, and scaffold-specific effort behavior. The model's “encoder” remains causal and should not be confused with a bidirectional Transformer encoder.

## What Changed
- Replaced report-mediated architecture confidence with direct first-party documentation while preserving the lack of independent replication.
- Added persistent-cache lifecycle and bounded-replay behavior, including the reported one-eighth predecessor footprint.
- Expanded the profile from architecture to multimodal pre-training, data-centered post-training, reasoning effort, and multi-agent evaluation.
- Added explicit robustness boundaries around sparse selection, approximate replay, benchmark scope, and scaffold sensitivity.

## Relationships
- [[CausalEncoderDecoderArchitecture]] - separates prompt-side global-memory production from decoder consumption.
- [[CompressedSparseAttention2]] - supplies sparse global attention and cross-layer cache or address reuse.
- [[HierarchicalSparseIndexer]] - bounds later decoder address selection to an earlier candidate pool.
- [[KVCacheCompression]] - describes the combined structural, precision, lifecycle, and recomputation reductions.
- [[DSpark]] - provides confidence-scheduled speculative decoding after backbone pre-training.
- [[ReasoningEffort]] - controls the learned cost-quality operating point of one checkpoint.
- [[DSec]] - provides the large-scale sandbox substrate used for agent post-training and evaluation.

---
title: "Grouped-Query Attention"
type: concept
tags: [transformers, attention, inference, kv-cache]
sources:
  - transformer-architectures
last_updated: 2026-10-24
knowledge_schema: synthesis-v1
---

## Definition
[[GroupedQueryAttention]] (GQA) is an attention arrangement in which several query heads share one key head and one value head, placing it between multi-head attention's separate KV heads and multi-query attention's single shared KV pair.

## Current Synthesis
Autoregressive decoding caches keys and values for every prior token. Standard multi-head attention gives every query head its own key and value projections, so cache size grows with the number of KV heads. GQA keeps many query heads but uses fewer KV heads, reducing cached state approximately by the query-to-KV grouping factor and making room for longer contexts or larger inference batches.

The source reports common grouping factors of four or eight and 23 of 53 sampled models using GQA, especially after LLaMA 2. This is an inference-economics tradeoff rather than a free algebraic equivalence: KV sharing removes per-query-head independence and can slightly affect quality, while realized latency and memory gains depend on implementation, model shape, batch size, context length, and kernels.

## Key Claims
- GQA uses more query heads than key-value heads and shares each KV head across a query-head group.
- KV-cache memory falls approximately with the reduction in KV-head count.
- Saved cache capacity can support longer contexts or larger autoregressive batches.
- GQA is an intermediate design between full multi-head and single-KV multi-query attention.
- Adoption reflects inference memory bandwidth and capacity as well as training quality.

## Evidence
Mechanism and memory effect:
- [[transformer-architectures]] defines separate query-head and KV-head counts, gives typical ratios of four or eight, and connects that ratio to cache reduction.

Adoption:
- [[transformer-architectures]] records GQA in 23 of 53 sampled models and describes it as dominant after LLaMA 2 for inference efficiency.

## Counterevidence & Qualifications
The source provides a cross-model survey rather than a controlled comparison of MHA, GQA, and MQA. Cache reduction does not guarantee the same proportional end-to-end speedup because projection work, attention kernels, memory layout, quantization, batching, and other bottlenecks remain. “Minimal” quality degradation is workload- and configuration-dependent, and the dataset's related model families are not independent observations.

## What Changed
- Created the concept around KV-head sharing and autoregressive cache economics.

## Related Concepts
- [[AttentionMechanism]] - supplies the query-key-value computation reorganized by GQA.
- [[KVCacheCompression]] - pursues the related goal of reducing retained attention state by other dimensions or representations.
- [[TransformerArchitecture]] - embeds GQA inside decoder blocks.
- [[TransformerArchitecturalConvergence]] - includes KV sharing in the modern default bundle.

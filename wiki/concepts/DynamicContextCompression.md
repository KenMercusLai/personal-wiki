---
title: "Dynamic Context Compression"
type: concept
tags: [ai, llm, context, memory]
sources:
  - yi-kou-qi-ba-suo-you-rang-ni-mu-xuan-de-llm-ming-ci-quan-dou-guo-yi-bian
last_updated: 2026-09-12
knowledge_schema: synthesis-v1
---

## Definition
[[DynamicContextCompression]] is an active context-management approach that continually removes, summarizes, or externalizes low-value context while preserving or retrieving the information needed for current reasoning.

## Current Synthesis
The source argues against passive compression that waits until the context window is almost full and then summarizes the whole conversation at once. A better design would monitor context quality continuously, evict wrong or low-relevance material, store useful detail externally, and retrieve it through RAG-like mechanisms when needed. The article points to [[MemGPT]] and [[Letta]] as examples of hierarchical memory management and notes a practical tension with prompt/KV caching: compression changes the prompt, while prefix caching benefits from stable text.

## Key Claims
- Passive end-of-window summarization happens at a bad time and can discard important detail.
- Dynamic compression should proactively remove wrong, low-relevance, or distracting context.
- External storage plus retrieval can preserve details without keeping everything in the active prompt.
- Hierarchical memory systems resemble operating-system virtual memory.
- Domain-specific compression can work when a strong prior identifies disposable information.
- Dynamic compression can invalidate prompt caches unless stable prefixes are separated from dynamic suffixes.

## Evidence
- Passive-compression critique: [[yi-kou-qi-ba-suo-you-rang-ni-mu-xuan-de-llm-ming-ci-quan-dou-guo-yi-bian]] says waiting until the context is near full causes a violent summarization step that may lose useful detail.
- Active alternative: [[yi-kou-qi-ba-suo-you-rang-ni-mu-xuan-de-llm-ming-ci-quan-dou-guo-yi-bian]] proposes ongoing supervision that removes errors and stores low-relevance details externally.
- MemGPT example: [[yi-kou-qi-ba-suo-you-rang-ni-mu-xuan-de-llm-ming-ci-quan-dou-guo-yi-bian]] describes MemGPT's working memory, archival memory, recall memory, and function-called eviction/retrieval.
- Computer Use example: [[yi-kou-qi-ba-suo-you-rang-ni-mu-xuan-de-llm-ming-ci-quan-dou-guo-yi-bian]] gives screenshot history pruning as a domain-specific lossy compression strategy.
- Cache tension: [[yi-kou-qi-ba-suo-you-rang-ni-mu-xuan-de-llm-ming-ci-quan-dou-guo-yi-bian]] says strict prefix caching conflicts with modifying earlier context, but stable system/tool prefixes can remain cacheable.

## Counterevidence & Qualifications
The source proposes an architectural direction but does not benchmark dynamic compression against passive summarization. It also does not resolve how a supervising model distinguishes false, low-value, and latent-but-important details in high-stakes domains.

## What Changed
- Created the concept page for active context compression and its relationship to memory, RAG, and prompt caching.

## Related Concepts
- [[LLMContextManagement]] - dynamic compression is one method for protecting context quality.
- [[AgentMemory]] - evicted information can be stored and retrieved through memory.
- [[RetrievalAugmentedGeneration]] - retrieval brings externally stored details back into the prompt.
- [[KVCacheAwareRouting]] - both concern KV reuse, though one is context editing and the other is serving-time routing.
- [[ComputerUse]] - Computer Use can benefit from domain-specific compression such as keeping only the latest screenshot.

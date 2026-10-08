---
title: "Dynamic Context Compression"
type: concept
tags: [ai, llm, context, memory]
sources:
  - yi-kou-qi-ba-suo-you-rang-ni-mu-xuan-de-llm-ming-ci-quan-dou-guo-yi-bian
  - ru-he-xiang-claude-code-yi-yang-shi-yong-si-you-api-guan-li-prompt-cache
  - mu-jiang-chui-zi-ding-zi
  - effective-context-engineering-for-ai-agents-anthropic
last_updated: 2026-10-08
knowledge_schema: synthesis-v1
---

## Definition
[[DynamicContextCompression]] is an active context-management approach that continually removes, summarizes, or externalizes low-value context while preserving or retrieving the information needed for current reasoning.

## Current Synthesis
The terminology source argues against passive compression that waits until the context window is almost full and then summarizes the whole conversation at once. A better design would monitor context quality continuously, evict wrong or low-relevance material, store useful detail externally, and retrieve it through RAG-like mechanisms when needed. The article points to [[MemGPT]] and [[Letta]] as examples of hierarchical memory management and notes a practical tension with prompt/KV caching: compression changes the prompt, while prefix caching benefits from stable text.

A concrete provider-specific answer to that tension is microcompact: large, fast-decaying tool results are marked with cache references, and later requests append cache-edit deletion instructions. This is dynamic compression at request-serialization time: local history remains complete, but the provider-side cached view can drop selected content while preserving much of the stable prefix.

[[TapeAndAnchors]] offers a more radical qualification. Compression, summaries, forks, merges, and handoffs all help finite contexts cope with long interaction histories, but they still often assume that history must be continuously inherited. The model reduces the compression burden by preserving raw history externally and carrying forward only minimal anchors.

Anthropic's account places compaction inside a broader long-horizon toolkit. A near-full conversation can be summarized into a fresh window, preserving decisions, unresolved problems, and implementation details while discarding redundant messages and old raw tool results. The tuning priority should begin with recall, because subtle information may become important only later; precision can then improve by removing clearly superfluous material. Structured notes or subagents may be better when state should remain external or exploration can be isolated.

## Key Claims
- End-of-window summarization can restore capacity but can discard latent-important detail unless its prompt is tuned for high recall before precision.
- Dynamic compression should proactively remove wrong, low-relevance, or distracting context.
- External storage plus retrieval can preserve details without keeping everything in the active prompt.
- Hierarchical memory systems resemble operating-system virtual memory.
- Domain-specific compression can work when a strong prior identifies disposable information.
- Dynamic compression can invalidate prompt caches unless stable prefixes are separated from dynamic suffixes, or provider-supported cache edits can logically delete selected cached blocks without rewriting the local transcript.
- Some context problems can be avoided by reconstructing from preserved history and anchors rather than compressing inherited state.

## Evidence
- Passive-compression critique: [[yi-kou-qi-ba-suo-you-rang-ni-mu-xuan-de-llm-ming-ci-quan-dou-guo-yi-bian]] says waiting until the context is near full causes a violent summarization step that may lose useful detail.
- Active alternative: [[yi-kou-qi-ba-suo-you-rang-ni-mu-xuan-de-llm-ming-ci-quan-dou-guo-yi-bian]] proposes ongoing supervision that removes errors and stores low-relevance details externally.
- MemGPT example: [[yi-kou-qi-ba-suo-you-rang-ni-mu-xuan-de-llm-ming-ci-quan-dou-guo-yi-bian]] describes MemGPT's working memory, archival memory, recall memory, and function-called eviction/retrieval.
- Computer Use example: [[yi-kou-qi-ba-suo-you-rang-ni-mu-xuan-de-llm-ming-ci-quan-dou-guo-yi-bian]] gives screenshot history pruning as a domain-specific lossy compression strategy.
- Cache tension: [[yi-kou-qi-ba-suo-you-rang-ni-mu-xuan-de-llm-ming-ci-quan-dou-guo-yi-bian]] says strict prefix caching conflicts with modifying earlier context, but stable system/tool prefixes can remain cacheable.
- Microcompact example: [[ru-he-xiang-claude-code-yi-yang-shi-yong-si-you-api-guan-li-prompt-cache]] describes Claude Code targeting large tool results with cache references and cache edits while leaving local message history unchanged.
- Continuity critique: [[mu-jiang-chui-zi-ding-zi]] groups compact, summary, fork, merge, and handoff as mechanisms built around the premise that state and history must continue.
- Anchor alternative: [[mu-jiang-chui-zi-ding-zi]] proposes ending tasks cleanly, storing minimal anchors, and reconstructing context only when needed.
- High-recall compaction: [[effective-context-engineering-for-ai-agents-anthropic]] recommends preserving decisions, unresolved bugs, and implementation detail first, then iterating to remove superfluous content.
- Tool-result clearing: [[effective-context-engineering-for-ai-agents-anthropic]] identifies old raw tool calls and results as a comparatively safe early target for light-touch compaction.
- Alternatives by task shape: [[effective-context-engineering-for-ai-agents-anthropic]] places compaction beside structured notes and subagents rather than treating it as the only continuity mechanism.

## Counterevidence & Qualifications
The sources propose architectural directions but do not benchmark dynamic compression against passive summarization. Claude Code's cache-edit behavior is provider-specific and partly inferred, and the sources do not resolve how a supervising model distinguishes false, low-value, and latent-but-important details in high-stakes domains.

This model shifts rather than solves several hard problems: retrieval quality, anchor design, provenance, and privacy still determine whether reconstructed context is adequate.

Anthropic does not supply a fidelity benchmark, trigger policy, or comparative threshold for choosing compaction over notes or subagents. Its Claude Code description is a product example, not evidence that the same retention recipe fits every domain, especially when later relevance is hard to predict.

## What Changed
- Reframed compaction as one long-horizon continuity mechanism beside structured notes and subagents.
- Added high recall before precision as the tuning order for summary-based compaction.
- Added old raw tool results as a comparatively safe first clearing target, while preserving the latent-relevance risk.

## Related Concepts
- [[LLMContextManagement]] - dynamic compression is one method for protecting context quality.
- [[AgentMemory]] - evicted information can be stored and retrieved through memory.
- [[RetrievalAugmentedGeneration]] - retrieval brings externally stored details back into the prompt.
- [[KVCacheAwareRouting]] - both concern KV reuse, though one is context editing and the other is serving-time routing.
- [[ComputerUse]] - Computer Use can benefit from domain-specific compression such as keeping only the latest screenshot.
- [[PromptCaching]] - cache edits reduce the usual conflict between compression and cache reuse.
- [[TapeAndAnchors]] - preserves raw history and minimal anchors instead of compressing all inherited state.

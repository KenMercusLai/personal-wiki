---
title: "一口气把所有让你目眩的 LLM 名词全都过一遍"
type: source
tags: [ai, llm, agents, context-management]
date: 2026-03-30
source_file: /mnt/ken_personal_wiki/Articles/一口气把所有让你目眩的 LLM 名词全都过一遍.md
---

## Summary
RORIRI explains LLM tooling terms through the shared problem of context management. The article contrasts [[LLMToolingSkills]], [[ModelContextProtocol]], [[RetrievalAugmentedGeneration]], [[AgentMemory]], [[DynamicContextCompression]], prompt caching, and [[ComputerUse]] as different ways to control what enters the model context and how LLMs act on the outside world.

## Key Claims
- [[LLMContextManagement]] is the common layer underneath Skills, MCP, RAG, Memory, dynamic compression, and Computer Use.
- [[LLMToolingSkills]] guide model reasoning by adding expert instructions, but their execution depends on model compliance rather than a hard runtime boundary.
- [[ModelContextProtocol]] compresses the model's action space into typed tool calls, but tool outputs can still pollute context if server responses are noisy.
- [[RetrievalAugmentedGeneration]] and [[AgentMemory]] are retrieval interfaces for keeping large document stores, histories, and saved facts out of the prompt until needed.
- [[DynamicContextCompression]] is presented as a better alternative to passive end-of-window summarization because it can proactively evict low-value or wrong information.
- Dynamic compression can conflict with prompt/KV caching, but stable prefixes plus dynamic suffixes can reduce cache invalidation.
- [[ComputerUse]] is treated as a product label over agentic operation of computers, with [[AccessibilityTree]] interaction as one cleaner route than raw pixel control.

## Key Quotes
> "LLM 本质是个概率模型" — the source frames generation as probabilistic next-token prediction.

> "Memory 也是同一类东西" — memory is grouped with retrieval systems rather than treated as a separate magic layer.

> "Computer Use...更接近一个品牌名" — Computer Use is framed as packaging rather than a distinct core technology.

## Connections
- [[RORIRI]] - author of the source.
- [[LLMContextManagement]] - central synthesis tying together the article's terminology.
- [[LLMToolingSkills]] - prompt-based expert-instruction layer.
- [[ModelContextProtocol]] - tool-call/RPC-style action layer.
- [[RetrievalAugmentedGeneration]] - retrieval layer for external knowledge.
- [[AgentMemory]] - writable retrieval layer for stored conversational or factual state.
- [[DynamicContextCompression]] - proposed active approach to preserving context quality.
- [[ComputerUse]] - agentic OS/software operation layer.
- [[AccessibilityTree]] - semantic UI route for Computer Use.
- [[MemGPT]] - example of hierarchical memory management.
- [[Letta]] - later open-source framework associated with the MemGPT line.
- [[Anthropic]] - provider mentioned in the prompt-caching discussion.

## Contradictions
- No direct contradiction with existing wiki pages. The source qualifies existing RAG and AI-framework material by reframing retrieval, memory, tool use, and prompt instructions as context-management mechanisms rather than separate categories.

---
title: "Effective context engineering for AI agents | Anthropic"
type: source
tags: [ai, agents, context-engineering, memory]
date: 2025-09-29
source_file: '/mnt/ken_personal_wiki/Articles/Effective context engineering for AI agents \ Anthropic.md'
---

## Summary
Anthropic defines [[LLMContextManagement|context engineering]] as curating and maintaining the information available to an LLM during inference, extending prompt engineering from instruction wording to system prompts, tools, examples, external data, and message history. The article treats model attention as a finite budget with diminishing returns, recommends the smallest sufficient set of high-signal tokens, and maps runtime retrieval, compaction, structured notes, and subagents to different context and task shapes.

## Key Claims
- Context engineering asks which configuration of tokens is most likely to produce the desired behavior, not merely how a prompt should be worded.
- Larger contexts remain subject to declining retrieval and long-range reasoning precision, so nominal window size does not remove the need to manage relevance and attention.
- System prompts should sit between brittle hardcoded logic and vague aspiration: minimal but sufficient, direct, and improved through observed failures.
- Agent tools should be self-contained, unambiguous, error-tolerant, token-efficient, and minimally overlapping; canonical diverse examples are preferable to exhaustive edge-case lists.
- Just-in-time context keeps lightweight identifiers in the prompt and lets agents retrieve files, queries, links, and other data as needed; metadata and progressive exploration help decide what to load.
- A hybrid design can preload stable high-value context for speed while leaving dynamic or task-specific material to runtime exploration.
- Long-horizon agents can preserve coherence through high-recall compaction, external structured notes, or specialized subagents that return distilled results to a coordinating agent.

## Key Quotes
> "find the smallest possible set of high-signal tokens" — the article's guiding context-selection principle.

> "do the simplest thing that works" — the article's task-dependent design advice.

## Connections
- [[Anthropic]] - publisher and first-party practitioner source for the context-engineering guidance.
- [[LLMContextManagement]] - central discipline defined as inference-time token selection and maintenance.
- [[DynamicContextCompression]] - compaction preserves long-horizon continuity by carrying a compressed state into a fresh window.
- [[AgentMemory]] - structured notes persist critical state outside the active prompt and restore it when needed.
- [[AgenticWorkflowPatterns]] - specialized subagents isolate deep work and return condensed findings to a coordinating agent.
- [[ClaudeCode]] - file navigation, targeted shell queries, project instructions, compaction, and recent-file retention illustrate the runtime approach.
- [[RetrievalAugmentedGeneration]] - pre-inference retrieval is contrasted with agent-directed just-in-time exploration and hybrid designs.
- [[PromptEngineering]] - context engineering is framed as its broader successor rather than a replacement for clear instructions and examples.

## Contradictions
- The article complements rather than directly contradicts the wiki's existing context material, but its favorable multi-agent account qualifies the one-main-loop preference in [[AgenticWorkflowPatterns]]: subagents are useful when task decomposition justifies their handoff cost, not as a universal default.
- The claims are first-party engineering guidance. The supplied article provides no evaluation protocol for context rot, compaction fidelity, runtime-retrieval tradeoffs, or the reported multi-agent improvement, and the transformer `n²` explanation is a simplified account rather than a complete causal analysis of attention degradation.

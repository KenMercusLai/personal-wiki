---
title: "Prompt Caching"
type: concept
tags: [ai, llm, caching, inference]
sources:
  - ru-he-xiang-claude-code-yi-yang-shi-yong-si-you-api-guan-li-prompt-cache
last_updated: 2026-09-12
knowledge_schema: synthesis-v1
---

## Definition
[[PromptCaching]] is an LLM serving mechanism that reuses previously processed prompt prefixes or marked prompt segments so repeated system prompts, tools, message history, and other stable inputs do not need to be fully recomputed on every request.

## Current Synthesis
The source presents prompt caching as both an infrastructure optimization and a product-design constraint. Anthropic-style prompt caching does not expose a user-defined cache key; instead, the effective key is inferred to include stable request parts such as system text, tools, model, message prefix, thinking configuration, and beta headers. Because tools and message prefixes are part of that reusable shape, clients that want good cache-hit rates must avoid gratuitously changing them.

[[ClaudeCode]] is the main case study. It improves cache reuse by keeping cache-covered structures stable and moving some changing control information into appended messages. Its private microcompact path extends this idea: large, low-value tool results can be assigned `cache_reference` names, then later `cache_edits` can delete those references from the provider-side cached view. The local conversation is not rewritten; instead, request serialization sends a persistent edit script that changes the effective cached prefix while preserving stable surrounding content.

## Key Claims
- Prompt-cache keys are shaped by stable request content rather than by a separate application-provided key.
- Cache breakpoints let a client choose which prompt prefix or segment should be cacheable.
- Cache efficiency depends on keeping system prompts, tool definitions, and reusable message prefixes stable.
- Claude Code's microcompact mechanism treats selected large tool results as logically deletable from the provider-side cached view.
- Replayed cache edits suggest a persistent "cached prefix plus edit script" model rather than a permanently rewritten cache object.
- Prompt caching links context-management quality with inference cost, latency, and routing concerns.

## Evidence
- Cache-key shape: [[ru-he-xiang-claude-code-yi-yang-shi-yong-si-you-api-guan-li-prompt-cache]] infers that Anthropic cache matching covers system, tools, model, message prefix, thinking config, and beta headers.
- Breakpoint behavior: [[ru-he-xiang-claude-code-yi-yang-shi-yong-si-you-api-guan-li-prompt-cache]] describes public cache-control breakpoints and notes that Claude Code commonly uses a small number of them.
- Stability tactics: [[ru-he-xiang-claude-code-yi-yang-shi-yong-si-you-api-guan-li-prompt-cache]] says Claude Code preserves tool definitions and appends system-reminder messages when tool availability changes.
- Microcompact semantics: [[ru-he-xiang-claude-code-yi-yang-shi-yong-si-you-api-guan-li-prompt-cache]] describes `cache_reference` and `cache_edits` as a logical deletion mechanism for old tool results.
- Edit replay: [[ru-he-xiang-claude-code-yi-yang-shi-yong-si-you-api-guan-li-prompt-cache]] argues that pinned cache edits being resent in later requests points to a stable request shape containing the edit script.

## Counterevidence & Qualifications
The source is based on code reading and inference about private provider behavior, not official public API documentation for the private cache-edit fields. It explicitly treats some serving-side consequences, such as whether freed KV blocks must be recomputed later, as uncertain.

## What Changed
- Created the concept page for prompt caching as a bridge between context management, Claude Code behavior, and inference-serving cost.

## Related Concepts
- [[LLMContextManagement]] - prompt caching rewards stable organization of instructions, tools, and history.
- [[DynamicContextCompression]] - cache edits make one form of compression compatible with cache reuse.
- [[KVCacheAwareRouting]] - both depend on reuse of cached prefix computation.
- [[InferenceLoadBalancing]] - cache reuse changes the true serving cost that routers may need to consider.
- [[InferenceTokenization]] - tokenized prompt structure determines the units of cached computation.

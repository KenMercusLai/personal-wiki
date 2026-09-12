---
title: "LLM Context Management"
type: concept
tags: [ai, llm, context]
sources:
  - yi-kou-qi-ba-suo-you-rang-ni-mu-xuan-de-llm-ming-ci-quan-dou-guo-yi-bian
  - yi-ge-ban-yue-gao-qiang-du-claude-code-shi-yong-hou-gan-shou
  - ru-he-xiang-claude-code-yi-yang-shi-yong-si-you-api-guan-li-prompt-cache
  - mu-jiang-chui-zi-ding-zi
last_updated: 2026-09-12
knowledge_schema: synthesis-v1
---

## Definition
[[LLMContextManagement]] is the practice of controlling what information, instructions, tool results, histories, and compressed summaries enter an LLM's context so the model can reason and act without being overwhelmed or misled.

## Current Synthesis
The sources treat many LLM terms and coding-agent workflows as answers to the same underlying problem: context is powerful but fragile. Skills add expert instructions, MCP narrows action choices through tool schemas, RAG retrieves only relevant outside information, memory writes and retrieves persistent information, dynamic compression removes or externalizes low-value material, and Computer Use introduces external action channels whose observations return to context. Onevcat's Claude Code retrospective turns that architecture into operational advice: decompose tasks, write plan documents, use subagents, compact at natural breakpoints, and start new sessions when a context is overloaded.

Context management also has a provider-facing request-shape layer. Stable system prompts, tools, message prefixes, and cache-control breakpoints can lower repeated inference cost, while private cache edits can make selected tool results disappear from the provider-side cached view without changing the local conversation.

PsiACE's agent essay adds a state-model layer. It argues that sessions, summaries, compaction, forks, merges, handoff, and memory often assume that state must be continuously inherited. [[TapeAndAnchors]] offers a different model: preserve history on an append-only tape, write minimal anchors at stage changes, and assemble context for each task through retrieval and selection rather than automatic continuation.

## Key Claims
- LLMs generate from probability distributions over tokens, so context strongly shapes both reasoning and action.
- Skills, MCP, RAG, Memory, and Computer Use can be understood as different context-management and action-interface patterns.
- Longer context windows reduce capacity pressure but do not remove noise, irrelevant material, misleading traces, or tool-call outputs that pollute later reasoning.
- Context quality can degrade through accumulated failed attempts, contradictory instructions, emotional pressure, lossy summarization, or overloaded sessions.
- Stable system/tool prefixes, dynamic conversation suffixes, and provider-side cache edits offer ways to balance context adaptation with prompt-cache reuse.
- Long coding-agent and group-chat sessions create practical failure modes when auto-compaction happens mid-task, topics run in parallel, or a task is too large for one session.
- Append-only history plus minimal anchors can reduce the pressure to keep every past state in active or summarized context.

## Evidence
- Shared framing: [[yi-kou-qi-ba-suo-you-rang-ni-mu-xuan-de-llm-ming-ci-quan-dou-guo-yi-bian]] explicitly says Skills, MCP, and coding-agent command execution are different openings from LLM text generation into the outside world, then frames them as solving context pollution.
- Retrieval framing: [[yi-kou-qi-ba-suo-you-rang-ni-mu-xuan-de-llm-ming-ci-quan-dou-guo-yi-bian]] says RAG keeps large knowledge bases and histories outside the prompt until retrieved.
- Noise risk: [[yi-kou-qi-ba-suo-you-rang-ni-mu-xuan-de-llm-ming-ci-quan-dou-guo-yi-bian]] argues that noisy tool returns, failed reasoning traces, and user emotional pressure can degrade later behavior.
- Compression and caching: [[yi-kou-qi-ba-suo-you-rang-ni-mu-xuan-de-llm-ming-ci-quan-dou-guo-yi-bian]] contrasts passive compression with dynamic compression and notes that modifying context conflicts with strict prefix-cache reuse.
- Coding-agent session tactics: [[yi-ge-ban-yue-gao-qiang-du-claude-code-shi-yong-hou-gan-shou]] describes context-window pressure, auto-compaction confusion, task decomposition, subagents, manual compacting at breakpoints, and plan documents for restarting work.
- Provider request shape: [[ru-he-xiang-claude-code-yi-yang-shi-yong-si-you-api-guan-li-prompt-cache]] shows Claude Code preserving cacheable prompt structures and using cache edits to logically remove high-volume tool results from the provider-side view.
- Tape and anchors: [[mu-jiang-chui-zi-ding-zi]] proposes treating history as an append-only tape, storing only minimal anchors, and assembling context through exploration and selection for each new task.

## Counterevidence & Qualifications
The sources are practitioner essays and code-reading analyses rather than empirical benchmarks. They give vivid model-behavior examples but do not provide controlled evidence for failure rates across models, tools, or task types. The private cache-edit account depends on inferred provider behavior, and the Computer Use section in the terminology source appears incomplete, covering only the first of an announced three routes.

The tape-and-anchors model is also conceptual: it gives a useful alternative to inherited session state, but does not yet specify anchor schemas, retrieval evaluation, conflict handling, or deletion/privacy semantics.

## What Changed
- Created the concept page for context management as the cross-cutting frame behind multiple LLM tooling terms.
- Added Claude Code session-management tactics as a practical context-management case.
- Added provider-side prompt-cache and cache-edit behavior as a context-management layer.
- Added tape and anchors as a context model that preserves history without default state inheritance.

## Related Concepts
- [[LLMToolingSkills]] - Skills manage context by adding expert instructions.
- [[ModelContextProtocol]] - MCP narrows the action surface through typed tool calls.
- [[RetrievalAugmentedGeneration]] - RAG retrieves context instead of preloading everything.
- [[AgentMemory]] - agent memory adds a writeable retrieval layer.
- [[DynamicContextCompression]] - dynamic compression actively preserves context quality.
- [[ComputerUse]] - Computer Use returns UI state and actions into the agent context loop.
- [[VibeCoding]] - coding-agent speed depends on keeping task and session context manageable.
- [[PromptCaching]] - prompt cache design rewards stable context shape and affects compression choices.
- [[TapeAndAnchors]] - append-only history and anchors provide an alternative context-reconstruction model.

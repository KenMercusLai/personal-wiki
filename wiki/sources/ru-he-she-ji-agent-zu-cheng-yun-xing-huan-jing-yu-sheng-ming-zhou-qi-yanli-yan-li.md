---
title: "如何设计 Agent：组成、运行环境与生命周期"
type: source
tags: [ai, agents, runtime, context-management, lifecycle, agent-skills]
date: 2026-09
source_file: "/mnt/ken_personal_wiki/Articles/如何设计 Agent：组成、运行环境与生命周期 | Yanli 盐粒.md"
---

## Summary
[[YanLi]] models an agent as the union of context and runtime: history plus instructions on one side, execution capability plus owned state on the other. The article compares compression with retrieval, basic with progressively injected instructions, and typed tools with the generality of shell and filesystem, then argues that [[LLMToolingSkills|Agent Skills]] and copy-on-write sandboxes leave unresolved boundaries around packaging and component state. It defines a stateful session containing history and workspace as one practical identity boundary for [[AgentLifecycleModel]], while steerable messages and asynchronous commands motivate a shift from turn-based execution toward continuous real-time interaction.

## Key Claims
- Agent architecture can be decomposed into context and runtime: context contains history and instructions, while runtime supplies execution and management of agent-owned state.
- History can be compressed inside the active context or kept outside and retrieved; retrieval design has independent axes for one-shot versus iterative search and unindexed filesystem search versus indexed semantic, full-text, or graph retrieval.
- Recall can compensate for low precision by covering more task-relevant evidence, but the compensation consumes context tokens and does not improve the retrieval result's precision.
- Instructions range from always-present prompts through conditionally injected prompt dictionaries to agent-selected progressive loading; `SKILL.md` is one carrier for the last pattern rather than the whole skill.
- Shell and filesystem make an operating system a general runtime because they provide broad execution and an explicit place for program, configuration, and working state.
- Agent Skills bundle instructions, OS-executable tools, and files, but do not standardize the boundary among immutable program content, configuration, and mutable runtime data; whole-filesystem CoW sandboxes provide snapshot and fork while remaining too coarse for component-level state transfer.
- A stateful session can define one agent by joining conversation history with workspace changes, but steering during execution and commands that outlive a turn weaken the turn as the fundamental lifecycle unit.

## Key Quotes
> “Agent = 上下文 + 运行环境” — the article's compact architectural decomposition.

> “这种基于 Turn 的建模正在被取代” — on steering, asynchronous work, and continuous interaction.

## Connections
- [[YanLi]] - author and PyCon China 2026 speaker whose second agent-architecture essay supplies this model.
- [[GenerativeAIAgentArchitecture]] - adds a context/runtime decomposition and explicit ownership questions for persistent state.
- [[AgentLifecycleModel]] - develops the session boundary, owned-state operations, and move beyond turn-only execution.
- [[SessionScopedMicroVMIsolation]] - a concrete session boundary that the article qualifies with whole-filesystem CoW granularity limits.
- [[LLMContextManagement]] - compares compression, one-shot and iterative retrieval, and indexed and unindexed history access.
- [[LLMToolingSkills]] - treats active progressive prompt loading as the instruction mechanism and exposes packaging/state-boundary gaps.
- [[AgentFilesystem]] - extends the filesystem from an intermediate-artifact store to a general mechanism for agent-owned state.
- [[BashAsMetaTool]] - supplies the execution half of the operating-system runtime.
- [[RetrievalAugmentedGeneration]] - indexed retrieval is one route for bringing externalized history back into context.
- [[ModelContextProtocol]] - protocol-level cross-call identifiers do not themselves save, copy, restore, or delete an agent and its state.

## Contradictions
- The article qualifies the runtime-free portability framing in [[LLMToolingSkills]]: a skill folder may be easy to move, but packaging it safely still requires a decision about whether configuration and mutable runtime state travel with code.
- It qualifies snapshot-based isolation as a complete state-management answer: a whole-filesystem CoW snapshot can fork a sandbox but may not isolate or migrate one component's configuration and state.
- Its claim that turn-based modeling is being replaced is a design-direction argument supported by steering and asynchronous execution examples, not evidence that turns have disappeared as scheduling, accounting, or API boundaries.
- The precision/recall, skill-distribution, MCP-specification, and ACP-v2 claims are practitioner analysis without benchmarks, adoption data, or a complete protocol comparison.
- No effective image references are present in the supplied Markdown, so no visual evidence or asset manifest was required.

---
title: "Generative AI Agent Architecture"
type: concept
tags: [ai, agents, architecture, tools]
sources:
  - blog-arthur-chiao-yi-ai-agent-ji-shu-bai-pi-shu-google-2024
last_updated: 2026-09-25
knowledge_schema: synthesis-v1
---

## Definition
[[GenerativeAIAgentArchitecture]] is an application structure that combines one or more language models with orchestration, memory or state, goals and instructions, and external tools so the system can plan, observe, act, and adjust toward an objective.

## Current Synthesis
The Google white paper locates agency in the application runtime rather than in the model alone. The model supplies language-based reasoning and decision support; orchestration maintains goals, instructions, short- and long-term memory, state, planning, stopping conditions, and the repeated observation-action loop; tools connect that loop to APIs, client code, and changing data. This makes an agent stateful and action-capable at the system level even when the underlying model call is stateless.

Its tool taxonomy is chiefly about execution and control boundaries. Extensions package API operations, parameters, and examples so the agent runtime can select and execute them. Function calling asks the model for a function name and structured arguments but leaves execution to client middleware, which is useful when authentication, ordering, private connectivity, or human review must remain outside the agent. Data stores expose indexed structured or unstructured information, commonly through a RAG pipeline.

ReAct is the paper's main orchestration example: the model alternates thoughts, actions, tool inputs, and observations until it can answer or a stopping condition fires. Tool-selection quality depends on both model capability and interface quality, while task-specific examples, retrieval, or fine-tuning can teach when and how to use available tools. The paper closes with an iterative-development boundary: architecture complexity should be refined against a concrete business need rather than treated as a one-shot design.

## Key Claims
- Agent capability emerges from the combination of model, orchestration, state, goals, instructions, and tools rather than from the base model alone.
- Orchestration owns the iterative observe-plan-act-adjust loop and the stopping condition.
- Extensions, client-executed function calls, and data stores create different execution, control, and information-access boundaries.
- ReAct makes tool use part of a repeated observation loop that can replace an unsupported initial guess with current external evidence.
- Tool performance depends on the model's selection ability and on clear tool definitions, parameters, examples, and returned observations.
- In-context examples, retrieval-based context, and fine-tuning are complementary ways to specialize tool selection.
- Agent architectures require iterative evaluation because added autonomy and tooling do not by themselves establish reliability or business value.

## Evidence
- Runtime structure: [[blog-arthur-chiao-yi-ai-agent-ji-shu-bai-pi-shu-google-2024]] depicts orchestration, memory, model-based reasoning, the model, and tools inside the agent runtime.
- Model/runtime distinction: [[blog-arthur-chiao-yi-ai-agent-ji-shu-bai-pi-shu-google-2024]] contrasts a model's training-bounded, stateless predictions with an agent application's external access and managed multi-turn state.
- ReAct loop: [[blog-arthur-chiao-yi-ai-agent-ji-shu-bai-pi-shu-google-2024]] walks through question, thought, action, action input, observation, repetition, and final answer.
- Extension boundary: [[blog-arthur-chiao-yi-ai-agent-ji-shu-bai-pi-shu-google-2024]] shows one agent selecting among extensions that map to different APIs.
- Function boundary: [[blog-arthur-chiao-yi-ai-agent-ji-shu-bai-pi-shu-google-2024]] shows the model returning structured function arguments while client middleware executes the external API call.
- Retrieval path: [[blog-arthur-chiao-yi-ai-agent-ji-shu-bai-pi-shu-google-2024]] shows query embedding, vector matching, retrieved content, agent decision, and response as a RAG request lifecycle.
- Prototype integration: [[blog-arthur-chiao-yi-ai-agent-ji-shu-bai-pi-shu-google-2024]] combines a Vertex model, search, places lookup, LangChain, and LangGraph in a two-hop example.

## Counterevidence & Qualifications
The source is an introductory Google white paper, not a controlled comparison of architectures. Its clean boundary between models and agents is pedagogically useful but product runtimes vary, later models may internalize more planning and structured-output behavior, and terms such as extension, function, plugin, and tool are provider-dependent. The examples demonstrate possible control flow, not production reliability, safety, cost, latency, authorization, observability, or error recovery. The ReAct trace also exposes internal “thought” text as an architectural teaching device; production systems need not reveal or depend on such text.

## What Changed
- Established a central system-level definition separating the model from the agent runtime.
- Added execution ownership as the key distinction among extensions, function calls, and data stores.
- Added targeted learning and iterative evaluation as design constraints on tool-using agents.

## Related Concepts
- [[AgenticWorkflowPatterns]] - provides a broader catalog of fixed and dynamic model-tool control flows.
- [[AgentComputerInterface]] - determines whether the model can understand and safely operate the available tools.
- [[RetrievalAugmentedGeneration]] - supplies external context through the data-store branch of the architecture.
- [[LLMAgentStages]] - traces structured output, tool calling, tool runtimes, and operating-system integration historically.
- [[AgentMemory]] - supplies persisted or reconstructed state beyond a single model call.
- [[AgentPermissionModel]] - constrains which external actions the runtime may perform.
- [[ProductionAgentInfrastructure]] - adds isolation, observability, resumability, recovery, and policy around long-running agents.

---
title: "Generative AI Agent Architecture"
type: concept
tags: [ai, agents, architecture, tools]
sources:
  - blog-arthur-chiao-yi-ai-agent-ji-shu-bai-pi-shu-google-2024
  - ru-he-she-ji-agent-zu-cheng-yun-xing-huan-jing-yu-sheng-ming-zhou-qi-yanli-yan-li
last_updated: 2026-10-07
knowledge_schema: synthesis-v1
---

## Definition
[[GenerativeAIAgentArchitecture]] is an application structure that joins model-mediated context with a runtime that manages goals, instructions, history, state, tools, execution, and the repeated observation-action process needed to pursue an objective.

## Current Synthesis
The sources agree that agency resides in the application system rather than in the language model alone. Google's white paper describes model, orchestration, memory or state, goals, instructions, and tools; Yan Li compresses the same system into context plus runtime. Context contains history and instructions. Runtime supplies execution and manages the state that belongs to the agent. The two views are compatible, but the second makes an ownership question explicit: external tool side effects are not automatically agent state, and the platform must define what is saved, copied, restored, or deleted with the agent.

Context architecture has two further axes. History can stay in the prompt through selective loss or compression, or live outside it and return through retrieval. Retrieval can be one-shot or agent-iterated and can search ordinary files without a dedicated index or use semantic, full-text, or graph indexes. Instructions can be always present, injected when preset conditions match, or actively loaded by the agent; skills are one packaging form for that last pattern.

Tool architecture determines execution and control boundaries. Extensions let the agent runtime choose and execute packaged API operations. Function calling asks the model for a function name and structured arguments but leaves execution to client middleware. Shell offers a highly general execution path, while the filesystem gives tools and agents a shared place for artifacts and owned state. ReAct remains one possible observation-action loop, but architecture is not complete until lifecycle, persistence, stopping, steering, asynchronous work, evaluation, and recovery boundaries are specified.

## Key Claims
- Agent capability emerges from a system of model-mediated context, orchestration or runtime, state, goals, instructions, and tools rather than from the base model alone.
- Context consists of selected history and instructions, while the runtime owns execution and the management of agent state.
- History compression and external retrieval trade retained detail, latency, infrastructure, precision, recall, and token use.
- Always-on, conditionally injected, and agent-selected instructions provide different timing and control over what enters context.
- Extensions, client-executed function calls, indexed data stores, shell, and filesystem create different execution, information-access, and state-ownership boundaries.
- ReAct is one iterative observe-plan-act-adjust loop, but steering and asynchronous commands require lifecycle models that extend beyond closed turns.
- Agent architectures require iterative evaluation because autonomy, broad tools, and persistent state do not by themselves establish reliability, safety, or value.

## Evidence
- Runtime structure: [[blog-arthur-chiao-yi-ai-agent-ji-shu-bai-pi-shu-google-2024]] depicts orchestration, memory, model-based reasoning, a model, and tools inside the agent runtime.
- Context/runtime decomposition: [[ru-he-she-ji-agent-zu-cheng-yun-xing-huan-jing-yu-sheng-ming-zhou-qi-yanli-yan-li]] defines the agent as context plus runtime and subdivides those into history, instructions, execution, and state management.
- History strategies: [[ru-he-she-ji-agent-zu-cheng-yun-xing-huan-jing-yu-sheng-ming-zhou-qi-yanli-yan-li]] contrasts compression with retrieval and separates retrieval frequency from index form.
- Instruction timing: [[ru-he-she-ji-agent-zu-cheng-yun-xing-huan-jing-yu-sheng-ming-zhou-qi-yanli-yan-li]] distinguishes basic, progressive, and actively progressive prompts.
- ReAct loop: [[blog-arthur-chiao-yi-ai-agent-ji-shu-bai-pi-shu-google-2024]] walks through question, thought, action, tool input, observation, repetition, and final answer.
- Execution boundaries: [[blog-arthur-chiao-yi-ai-agent-ji-shu-bai-pi-shu-google-2024]] contrasts runtime-executed extensions with client-executed function calls and indexed data stores.
- OS runtime: [[ru-he-she-ji-agent-zu-cheng-yun-xing-huan-jing-yu-sheng-ming-zhou-qi-yanli-yan-li]] presents shell and filesystem as the operating system's general execution and state-management primitives.
- State ownership: [[ru-he-she-ji-agent-zu-cheng-yun-xing-huan-jing-yu-sheng-ming-zhou-qi-yanli-yan-li]] distinguishes external side effects from state that should travel with the agent.
- Iterative development: [[blog-arthur-chiao-yi-ai-agent-ji-shu-bai-pi-shu-google-2024]] says complex agent architecture requires continuing refinement against a business need.

## Counterevidence & Qualifications
Both sources are architectural explanations rather than controlled comparisons. Google's 2024 paper is introductory and provider-centered; Li's 2026 essay is an opinionated practitioner account derived from a conference talk. Their categories clarify responsibility but do not measure reliability, latency, cost, security, retrieval quality, state consistency, or business outcomes. Terminology such as extension, function, tool, memory, skill, session, and runtime remains implementation-dependent. High recall can mitigate missing evidence at the cost of noise and tokens, but it does not improve retrieval precision. Broad OS access improves flexibility while increasing the need for permissions, isolation, packaging, observability, and recovery.

## What Changed
- Reframed the architecture as context plus runtime while preserving the earlier model-orchestration-tools view.
- Added history and instruction-loading strategies as explicit context architecture.
- Added agent-state ownership and lifecycle operations as runtime responsibilities.
- Extended the execution model beyond closed turns to steering and asynchronous work.

## Related Concepts
- [[AgentLifecycleModel]] - defines the identity, state ownership, and continuity rules around this architecture.
- [[AgenticWorkflowPatterns]] - catalogs fixed and dynamic model-tool control flows.
- [[AgentComputerInterface]] - determines whether the model can understand and safely operate available tools.
- [[LLMContextManagement]] - manages history, instructions, retrieved evidence, and tool observations.
- [[LLMToolingSkills]] - packages agent-selected instructions and executable or reference assets.
- [[AgentFilesystem]] - supplies a general artifact and state surface inside an OS runtime.
- [[AgentMemory]] - supplies persisted or reconstructed state beyond a single model call.
- [[ProductionAgentInfrastructure]] - adds isolation, observability, resumability, recovery, and policy around long-running agents.

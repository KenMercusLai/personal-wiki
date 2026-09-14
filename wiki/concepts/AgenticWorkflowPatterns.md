---
title: "Agentic Workflow Patterns"
type: concept
tags: [ai, agents, workflow-design]
sources:
  - blog-anthropic-building-effective-ai-agents
  - blog-minusx-nuwanda-what-makes-claude-code-so-damn-good
last_updated: 2026-09-14
knowledge_schema: synthesis-v1
---

## Definition
[[AgenticWorkflowPatterns]] are reusable LLM application structures that compose model calls, tools, checks, routing, parallel work, synthesis, and feedback loops to solve tasks that need more than a single prompt.

## Current Synthesis
Anthropic separates agentic systems into workflows and agents. Workflows are predefined code paths where developers decide the sequence and control logic, while agents are more dynamic loops where the model chooses steps and tool use. The practical advice is conservative: optimize the simplest single-call or retrieval-augmented design first, then add workflow or agent complexity only when evaluation shows a real performance gain.

The article's pattern catalog creates a useful fit map. Prompt chaining fits tasks that decompose cleanly into fixed steps, routing fits inputs with reliably distinguishable categories, parallelization fits independent subtasks or voting, orchestrator-workers fits tasks where the needed subtasks are not known in advance, and evaluator-optimizer fits tasks with clear evaluation criteria where critique improves the result. Autonomous agents extend beyond these workflows when the step count and path are too open-ended to hardcode, but they bring cost, latency, and compounding-error risk.

The MinusX Claude Code analysis adds a coding-agent control-loop pattern: keep one main message history and at most one branch. In this design, simple tasks proceed through iterative tool calls inside the main loop, while complex subtasks can be delegated to a subagent through a `Task` tool; the branch cannot spawn more branches, and its result returns into the main history as a tool response. The pattern gives the model some decomposition ability without turning the whole system into an opaque multi-agent graph.

## Key Claims
- Agentic systems should add complexity only when simpler prompting, retrieval, and in-context examples fall short.
- Workflows keep LLM/tool execution on predefined paths, while agents let the model dynamically control process and tool use.
- Prompt chaining, routing, parallelization, orchestrator-workers, and evaluator-optimizer loops cover common production workflow shapes.
- Pattern choice depends on task decomposition, classification confidence, independence of subtasks, uncertainty about subtasks, and availability of evaluation criteria.
- Autonomous agents fit open-ended tasks where fixed paths cannot be predicted, but need environmental feedback, stopping conditions, testing, guardrails, and human checkpoints.
- Coding-agent loops can preserve debuggability by using one main message history and limiting subagent branching.
- Todo lists and bounded subagents can let a coding agent decompose work while keeping focus on the user's final desired outcome.

## Evidence
- Simplicity gate: [[blog-anthropic-building-effective-ai-agents]] says many applications should use a simple LLM call with retrieval or examples before escalating to agentic systems.
- Workflow/agent boundary: [[blog-anthropic-building-effective-ai-agents]] defines workflows as predefined code paths and agents as systems where LLMs dynamically direct process and tool use.
- Fixed-step workflows: [[blog-anthropic-building-effective-ai-agents]] describes prompt chaining with intermediate gates for decomposable tasks such as outline checking before writing.
- Specialization workflows: [[blog-anthropic-building-effective-ai-agents]] describes routing for customer-service categories and model selection between cheaper and more capable models.
- Parallel workflows: [[blog-anthropic-building-effective-ai-agents]] describes sectioning and voting for independent subtasks, guardrails, evals, code review, and content moderation.
- Dynamic delegation: [[blog-anthropic-building-effective-ai-agents]] describes orchestrator-workers for tasks such as coding or search where subtasks cannot be known ahead of time.
- Iterative critique: [[blog-anthropic-building-effective-ai-agents]] describes evaluator-optimizer loops for translation and complex search when criteria and feedback can improve outputs.
- Agent loop: [[blog-anthropic-building-effective-ai-agents]] describes agents that clarify tasks with humans, act on environments, use ground-truth feedback, checkpoint with people, and terminate by completion or stopping conditions.
- Bounded branch: [[blog-minusx-nuwanda-what-makes-claude-code-so-damn-good]] argues that Claude Code uses one main thread and can spawn itself as a subagent without allowing further subagent spawning.
- Control-loop diagram: [[blog-minusx-nuwanda-what-makes-claude-code-so-damn-good]] shows a simple main-loop task and a complex task whose `Task` branch performs read/search/edit steps before returning to the main loop.

## Counterevidence & Qualifications
The sources are practitioner guidance rather than controlled benchmarks of each pattern. They also emphasize different levels: Anthropic catalogs general workflow structures, while MinusX interprets Claude Code's coding-agent loop from observed behavior. Bounded branching may improve debuggability, but very large projects can still require heavier role separation, file-backed state, and verification harnesses; the key qualification is that added agents should have a clear coordination and debugging story.

## What Changed
- Added the Claude Code one-main-loop plus bounded-branch pattern.
- Added todo-list coordination as a lightweight alternative to heavier handoff systems.
- Qualified general multi-agent use with a debuggability requirement.

## Related Concepts
- [[AgentExperience]] - workflow and agent structure shape how users clarify goals and recover from agent behavior.
- [[AgentComputerInterface]] - tools and environment feedback are the action surface for these patterns.
- [[ModelContextProtocol]] - structured tool interfaces can implement parts of these workflows.
- [[AgenticRAG]] - search/read loops are one retrieval-heavy workflow or agent pattern.
- [[AIApplicationFramework]] - frameworks often package these patterns but can obscure implementation details.
- [[SoftwareVerification]] - agent loops become more reliable when progress can be checked by tests or other objective signals.
- [[ClaudeCode]] - Claude Code provides the bounded-branch coding-agent example.
- [[AgentTeam]] - multi-agent teams are a heavier workflow form that needs file-backed state and verification.

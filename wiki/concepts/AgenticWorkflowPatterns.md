---
title: "Agentic Workflow Patterns"
type: concept
tags: [ai, agents, workflow-design]
sources:
  - blog-anthropic-building-effective-ai-agents
last_updated: 2026-09-14
knowledge_schema: synthesis-v1
---

## Definition
[[AgenticWorkflowPatterns]] are reusable LLM application structures that compose model calls, tools, checks, routing, parallel work, synthesis, and feedback loops to solve tasks that need more than a single prompt.

## Current Synthesis
Anthropic separates agentic systems into workflows and agents. Workflows are predefined code paths where developers decide the sequence and control logic, while agents are more dynamic loops where the model chooses steps and tool use. The practical advice is conservative: optimize the simplest single-call or retrieval-augmented design first, then add workflow or agent complexity only when evaluation shows a real performance gain.

The article's pattern catalog creates a useful fit map. Prompt chaining fits tasks that decompose cleanly into fixed steps, routing fits inputs with reliably distinguishable categories, parallelization fits independent subtasks or voting, orchestrator-workers fits tasks where the needed subtasks are not known in advance, and evaluator-optimizer fits tasks with clear evaluation criteria where critique improves the result. Autonomous agents extend beyond these workflows when the step count and path are too open-ended to hardcode, but they bring cost, latency, and compounding-error risk.

## Key Claims
- Agentic systems should add complexity only when simpler prompting, retrieval, and in-context examples fall short.
- Workflows keep LLM/tool execution on predefined paths, while agents let the model dynamically control process and tool use.
- Prompt chaining, routing, parallelization, orchestrator-workers, and evaluator-optimizer loops cover common production workflow shapes.
- Pattern choice depends on task decomposition, classification confidence, independence of subtasks, uncertainty about subtasks, and availability of evaluation criteria.
- Autonomous agents fit open-ended tasks where fixed paths cannot be predicted, but need environmental feedback, stopping conditions, testing, guardrails, and human checkpoints.
- Diagrams in the source make the control structure explicit: gates, routers, aggregators, orchestrators, synthesizers, evaluators, and environment-feedback loops are first-class system components.

## Evidence
- Simplicity gate: [[blog-anthropic-building-effective-ai-agents]] says many applications should use a simple LLM call with retrieval or examples before escalating to agentic systems.
- Workflow/agent boundary: [[blog-anthropic-building-effective-ai-agents]] defines workflows as predefined code paths and agents as systems where LLMs dynamically direct process and tool use.
- Fixed-step workflows: [[blog-anthropic-building-effective-ai-agents]] describes prompt chaining with intermediate gates for decomposable tasks such as outline checking before writing.
- Specialization workflows: [[blog-anthropic-building-effective-ai-agents]] describes routing for customer-service categories and model selection between cheaper and more capable models.
- Parallel workflows: [[blog-anthropic-building-effective-ai-agents]] describes sectioning and voting for independent subtasks, guardrails, evals, code review, and content moderation.
- Dynamic delegation: [[blog-anthropic-building-effective-ai-agents]] describes orchestrator-workers for tasks such as coding or search where subtasks cannot be known ahead of time.
- Iterative critique: [[blog-anthropic-building-effective-ai-agents]] describes evaluator-optimizer loops for translation and complex search when criteria and feedback can improve outputs.
- Agent loop: [[blog-anthropic-building-effective-ai-agents]] describes agents that clarify tasks with humans, act on environments, use ground-truth feedback, checkpoint with people, and terminate by completion or stopping conditions.

## Counterevidence & Qualifications
The source is practitioner guidance from Anthropic rather than a controlled benchmark of each pattern. It does not prove a universal ordering of patterns, and it leaves implementation details such as observability, permissions, security, and domain-specific evaluation to builders. The framework also assumes LLMs and tools are reliable enough for the chosen environment; unsafe or poorly instrumented environments may require narrower workflows even when a task looks open-ended.

## What Changed
- Created a pattern catalog for Anthropic's workflow-versus-agent distinction and five named workflow structures.
- Added a conservative complexity rule: escalate from single calls to workflows or agents only when evaluation justifies the tradeoff.
- Added diagram-derived control components as explicit evidence.

## Related Concepts
- [[AgentExperience]] - workflow and agent structure shape how users clarify goals and recover from agent behavior.
- [[AgentComputerInterface]] - tools and environment feedback are the action surface for these patterns.
- [[ModelContextProtocol]] - structured tool interfaces can implement parts of these workflows.
- [[AgenticRAG]] - search/read loops are one retrieval-heavy workflow or agent pattern.
- [[AIApplicationFramework]] - frameworks often package these patterns but can obscure implementation details.
- [[SoftwareVerification]] - agent loops become more reliable when progress can be checked by tests or other objective signals.

---
title: "Agent Experience"
type: concept
tags: [ai, agents, interaction-design]
sources:
  - agent-experience-dao-lun-luo-li-li-de-shu-ju-zhong-xin
  - blog-anthropic-building-effective-ai-agents
last_updated: 2026-09-14
knowledge_schema: synthesis-v1
---

## Definition
[[AgentExperience]] is the design practice of shaping products, interfaces, tools, and operating environments so AI agents can understand user intent, manage their internal context, and act on external systems reliably.

## Current Synthesis
RORIRI frames AX as more complex than UX or DX because it involves a human, an AI agent, and the outside world interacting through probabilistic interpretation and concrete side effects. The useful decomposition is threefold: user-to-agent communication, agent internal state, and agent-to-world action. Each layer creates a different pressure: ambiguous human intent, polluted or lossy context, and the need to compress probabilistic generation into deterministic operations.

Anthropic's agent-building article strengthens the same frame from an engineering-practice angle. Its autonomous-agent loop begins with a human command or interactive clarification, then depends on environmental ground truth, tool results, code execution, checkpoints, blockers, and stopping conditions. Its tool appendix also makes agent-to-world action an interface-design problem: the model needs obvious tool names, model-friendly formats, examples, edge cases, and mistake-resistant arguments.

## Key Claims
- AX spans user input, agent internal state, and external action rather than only the surface chat interface.
- User-to-agent design is an input-quality problem because ordinary human expression is fuzzy, emotional, incomplete, and inconsistent.
- Agent-to-world design is an output-control problem because filesystems, APIs, browsers, and operating systems require concrete actions.
- Internal state design is a context-management problem because instructions, feedback, screenshots, retrieved data, tool output, and emotional signals compete inside limited context.
- Open and closed agent systems redistribute risk: open chat increases intent ambiguity, while closed pipelines require more up-front process design.
- Reliable AX needs transparency, auditability, permissions, interface context delivery, environmental feedback, human checkpoints, and explicit stopping conditions.
- Tool schemas and action formats are part of AX because they determine whether the agent can safely translate intent into external action.

## Evidence
- Three-layer model: [[agent-experience-dao-lun-luo-li-li-de-shu-ju-zhong-xin]] divides AX into how users communicate with agents, how agents communicate with the external world, and how the agent manages internal state.
- Input quality: [[agent-experience-dao-lun-luo-li-li-de-shu-ju-zhong-xin]] says user expression is naturally fuzzy and should not require perfectly formal prompts.
- Output control: [[agent-experience-dao-lun-luo-li-li-de-shu-ju-zhong-xin]] says external systems do not tolerate LLM ambiguity, so tool calls, MCP, and event injection help constrain action.
- Internal context: [[agent-experience-dao-lun-luo-li-li-de-shu-ju-zhong-xin]] places MemGPT, dynamic compression, and screenshot pruning in the agent-state layer.
- Open/closed systems: [[agent-experience-dao-lun-luo-li-li-de-shu-ju-zhong-xin]] contrasts open chat windows with closed workflow pipelines and user-built pipeline builders.
- Governance layer: [[agent-experience-dao-lun-luo-li-li-de-shu-ju-zhong-xin]] argues that audit trails, behavior alarms, sandboxing, and tiered permissions are missing product infrastructure for high-authority agents.
- Agent loop: [[blog-anthropic-building-effective-ai-agents]] says agents may clarify tasks with humans, operate independently, gather ground truth from tools or code execution, and pause for human feedback at checkpoints or blockers.
- Tool interface: [[blog-anthropic-building-effective-ai-agents]] says tool definitions should include examples, edge cases, input requirements, and clear boundaries from similar tools.
- Stopping conditions: [[blog-anthropic-building-effective-ai-agents]] recommends completion or explicit iteration limits to maintain control over autonomous agents.

## Counterevidence & Qualifications
The sources are conceptual and practitioner-oriented rather than measured standards. Their product examples are source-scoped and may age quickly as agent interfaces, model capabilities, and permission systems change.

## What Changed
- Created the AX concept as a three-layer design frame connecting interaction design, context management, external action, and safety.
- Added Anthropic's engineering loop of clarification, environmental feedback, checkpoints, stopping conditions, and tool-interface design.

## Related Concepts
- [[LLMContextManagement]] - internal context quality is one AX layer.
- [[ComputerUse]] - agent operation of software is one external-action surface for AX.
- [[ConversationalUI]] - chat and canvas interfaces shape user-to-agent communication.
- [[AgentSystemTransparency]] - traceability lets users understand and recover from agent action.
- [[AgentPermissionModel]] - permission design controls the risk of agent side effects.
- [[AgentInterfaceAsContext]] - interfaces can deliver timely constraints and diagnostics to agents.
- [[HumanisticAgentDesign]] - AX includes how agents clarify user cognition and intent.
- [[AgenticWorkflowPatterns]] - workflow and agent structure determines where clarification, feedback, and checkpoints occur.
- [[AgentComputerInterface]] - ACI is the model-facing interface layer for external action.

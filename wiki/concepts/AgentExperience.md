---
title: "Agent Experience"
type: concept
tags: [ai, agents, interaction-design]
sources:
  - agent-experience-dao-lun-luo-li-li-de-shu-ju-zhong-xin
last_updated: 2026-09-13
knowledge_schema: synthesis-v1
---

## Definition
[[AgentExperience]] is the design practice of shaping products, interfaces, tools, and operating environments so AI agents can understand user intent, manage their internal context, and act on external systems reliably.

## Current Synthesis
RORIRI frames AX as more complex than UX or DX because it involves a human, an AI agent, and the outside world interacting through probabilistic interpretation and concrete side effects. The useful decomposition is threefold: user-to-agent communication, agent internal state, and agent-to-world action. Each layer creates a different pressure: ambiguous human intent, polluted or lossy context, and the need to compress probabilistic generation into deterministic operations.

## Key Claims
- AX spans user input, agent internal state, and external action rather than only the surface chat interface.
- User-to-agent design is an input-quality problem because ordinary human expression is fuzzy, emotional, incomplete, and inconsistent.
- Agent-to-world design is an output-control problem because filesystems, APIs, browsers, and operating systems require concrete actions.
- Internal state design is a context-management problem because instructions, feedback, screenshots, retrieved data, tool output, and emotional signals compete inside limited context.
- Open and closed agent systems redistribute risk: open chat increases intent ambiguity, while closed pipelines require more up-front process design.
- Reliable AX needs transparency, auditability, permissions, and interface context delivery in addition to better prompts or stronger models.

## Evidence
- Three-layer model: [[agent-experience-dao-lun-luo-li-li-de-shu-ju-zhong-xin]] divides AX into how users communicate with agents, how agents communicate with the external world, and how the agent manages internal state.
- Input quality: [[agent-experience-dao-lun-luo-li-li-de-shu-ju-zhong-xin]] says user expression is naturally fuzzy and should not require perfectly formal prompts.
- Output control: [[agent-experience-dao-lun-luo-li-li-de-shu-ju-zhong-xin]] says external systems do not tolerate LLM ambiguity, so tool calls, MCP, and event injection help constrain action.
- Internal context: [[agent-experience-dao-lun-luo-li-li-de-shu-ju-zhong-xin]] places MemGPT, dynamic compression, and screenshot pruning in the agent-state layer.
- Open/closed systems: [[agent-experience-dao-lun-luo-li-li-de-shu-ju-zhong-xin]] contrasts open chat windows with closed workflow pipelines and user-built pipeline builders.
- Governance layer: [[agent-experience-dao-lun-luo-li-li-de-shu-ju-zhong-xin]] argues that audit trails, behavior alarms, sandboxing, and tiered permissions are missing product infrastructure for high-authority agents.

## Counterevidence & Qualifications
The source is a conceptual essay rather than a measured framework or standard. Its product examples are source-scoped and may age quickly as agent interfaces, model capabilities, and permission systems change.

## What Changed
- Created the AX concept as a three-layer design frame connecting interaction design, context management, external action, and safety.

## Related Concepts
- [[LLMContextManagement]] - internal context quality is one AX layer.
- [[ComputerUse]] - agent operation of software is one external-action surface for AX.
- [[ConversationalUI]] - chat and canvas interfaces shape user-to-agent communication.
- [[AgentSystemTransparency]] - traceability lets users understand and recover from agent action.
- [[AgentPermissionModel]] - permission design controls the risk of agent side effects.
- [[AgentInterfaceAsContext]] - interfaces can deliver timely constraints and diagnostics to agents.
- [[HumanisticAgentDesign]] - AX includes how agents clarify user cognition and intent.

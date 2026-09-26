---
title: "Agent Computer Interface"
type: concept
tags: [ai, agents, tools, developer-experience]
sources:
  - blog-anthropic-building-effective-ai-agents
  - blog-arthur-chiao-yi-ai-agent-ji-shu-bai-pi-shu-google-2024
last_updated: 2026-09-25
knowledge_schema: synthesis-v1
---

## Definition
[[AgentComputerInterface]] is the design layer that makes external tools, APIs, files, computers, and environments understandable and safely usable by an AI agent.

## Current Synthesis
Anthropic extends the familiar HCI analogy into agent systems: if humans need carefully designed interfaces, agents also need carefully designed tool definitions, argument formats, examples, error boundaries, and feedback channels. Tool specifications are therefore not neutral plumbing. They are prompt-engineering surfaces that shape whether the model can choose the right action, format arguments correctly, interpret results, and recover from mistakes.

The article's advice is practical and model-facing. Tool formats should be close to naturally occurring text, avoid unnecessary overhead such as fragile line counts or excessive string escaping, and leave enough room for the model to reason before committing to an output format. Tool definitions should include examples, edge cases, input requirements, clear boundaries from similar tools, and argument names that make the intended operation obvious. Anthropic's SWE-bench example highlights a small interface change with large reliability impact: requiring absolute file paths prevented relative-path mistakes after the agent changed directories.

The Google white paper adds execution ownership to interface design. Extensions package API operations, parameters, and examples for selection and execution inside the agent runtime; function calling returns a name and structured arguments so client middleware can authenticate, review, sequence, or execute the action; and data stores expose retrieved context rather than an imperative operation. An agent-facing interface therefore includes not only schema clarity but also where execution happens, who controls side effects, and what observation returns to the orchestration loop.

## Key Claims
- Tool definitions deserve as much prompt-engineering attention as the rest of an agent prompt.
- Model-friendly tool formats reduce avoidable errors in code, structured output, and file-edit operations.
- Good tool interfaces provide examples, edge cases, input constraints, and boundaries between similar tools or execution modes.
- Argument names and descriptions should make correct tool use obvious from the model's point of view.
- Testing model-tool interaction against many example inputs is necessary because interface mistakes are empirical.
- Mistake-resistant tools can prevent predictable failures, such as path ambiguity, before the model acts.
- Interface architecture must make execution ownership and returned observations explicit: an extension may execute inside the agent runtime, while a function call may require client-side execution.

## Evidence
- Tool prompting: [[blog-anthropic-building-effective-ai-agents]] says tool definitions and specifications need prompt-engineering attention, not only the overall agent prompt.
- Format friction: [[blog-anthropic-building-effective-ai-agents]] contrasts diffs, whole-file rewrites, markdown code, and JSON code as formats with different model-writing difficulty.
- Natural format rule: [[blog-anthropic-building-effective-ai-agents]] recommends formats close to what models have seen naturally in text and avoiding overhead such as line-count bookkeeping or string escaping.
- Interface empathy: [[blog-anthropic-building-effective-ai-agents]] says designers should put themselves in the model's position and ask whether tool usage is obvious.
- Definition detail: [[blog-anthropic-building-effective-ai-agents]] says good tool definitions include examples, edge cases, input format requirements, and clear boundaries from other tools.
- Empirical testing: [[blog-anthropic-building-effective-ai-agents]] recommends testing tool use in many example inputs to discover mistakes and iterate.
- Absolute-path case: [[blog-anthropic-building-effective-ai-agents]] says Anthropic's SWE-bench agent became more reliable after a tool required absolute file paths rather than relative ones.
- Extension interface: [[blog-arthur-chiao-yi-ai-agent-ji-shu-bai-pi-shu-google-2024]] shows API method descriptions, usage examples, and required parameters teaching an agent how to select and call an extension.
- Execution boundary: [[blog-arthur-chiao-yi-ai-agent-ji-shu-bai-pi-shu-google-2024]] contrasts agent-side extension execution with function calls whose structured output returns through client middleware before the API is invoked.
- Observation loop: [[blog-arthur-chiao-yi-ai-agent-ji-shu-bai-pi-shu-google-2024]] shows tool output becoming the observation that guides the next ReAct step and final response.

## Counterevidence & Qualifications
The sources give design heuristics and illustrative architectures rather than a complete taxonomy or benchmark of tool-interface quality. Google's extension/function terminology is provider-specific, and later APIs may place execution boundaries differently. Some domains require stricter structured formats despite model-writing overhead, especially where downstream systems need strong validation, authorization, auditability, human review, or transactional guarantees; clear schemas alone do not make side effects safe.

## What Changed
- Added execution ownership and observation return paths to the interface model.
- Distinguished agent-side extensions from client-executed function calls and retrieval-oriented data stores.

## Related Concepts
- [[AgentExperience]] - ACI is the external-action layer of agent experience.
- [[ModelContextProtocol]] - MCP is one structured mechanism for exposing ACI-style tools.
- [[CodingAgentMinimalTooling]] - coding agents depend on file, shell, edit, and test interfaces that the model can use reliably.
- [[ComputerUse]] - Computer Use is an ACI surface over ordinary graphical or desktop software.
- [[AgentPermissionModel]] - permissions constrain which ACI actions an agent can perform.
- [[DeveloperExperience]] - agent-facing tools need clarity and recoverability much like human-facing developer tools.
- [[GenerativeAIAgentArchitecture]] - places the interface inside the larger model, orchestration, memory, and tools runtime.

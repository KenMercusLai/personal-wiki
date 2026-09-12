---
title: "Model Context Protocol"
type: concept
tags: [ai, llm, tools, protocol]
sources:
  - yi-kou-qi-ba-suo-you-rang-ni-mu-xuan-de-llm-ming-ci-quan-dou-guo-yi-bian
last_updated: 2026-09-12
knowledge_schema: synthesis-v1
---

## Definition
[[ModelContextProtocol]] is a tool-interface pattern where servers expose callable functions and schemas so an LLM can invoke external capabilities through structured calls rather than only generating free-form text.

## Current Synthesis
The source frames MCP as closer to RPC than prompting. Function names, parameter names, and types narrow the model's action space: instead of deciding among arbitrary textual plans, the model chooses from defined functions and structured arguments. This can make external actions more deterministic, but it does not automatically solve context pollution because tool responses also return to the model context.

## Key Claims
- MCP gives LLMs a structured outlet for modifying or querying the external world.
- Tool schemas create strong priors that constrain model sampling toward valid actions.
- Structured tool calls can replace many uncertain step-order decisions in UI or system-operation tasks.
- MCP has higher implementation cost than prompt-only Skills because it requires a server interface.
- Poorly designed MCP responses can still damage context quality through noisy JSON, oversized payloads, or verbose errors.

## Evidence
- RPC analogy: [[yi-kou-qi-ba-suo-you-rang-ni-mu-xuan-de-llm-ming-ci-quan-dou-guo-yi-bian]] says MCP resembles servers exposing functions for the LLM to call.
- Action-space compression: [[yi-kou-qi-ba-suo-you-rang-ni-mu-xuan-de-llm-ming-ci-quan-dou-guo-yi-bian]] argues that function names and typed parameters reduce arbitrary text generation into a smaller set of structured choices.
- UI-operation example: [[yi-kou-qi-ba-suo-you-rang-ni-mu-xuan-de-llm-ming-ci-quan-dou-guo-yi-bian]] contrasts many uncertain mouse-operation steps with fewer structured calls.
- Return-value risk: [[yi-kou-qi-ba-suo-you-rang-ni-mu-xuan-de-llm-ming-ci-quan-dou-guo-yi-bian]] warns that tool outputs can pollute context if server design is careless.

## Counterevidence & Qualifications
The source explains MCP at a conceptual level and does not compare specific MCP implementations, security models, permission boundaries, schema-design practices, or latency/cost tradeoffs.

## What Changed
- Created the concept page for MCP as a structured tool-call interface and context-management device.

## Related Concepts
- [[LLMContextManagement]] - MCP reduces action ambiguity while adding tool results back into context.
- [[LLMToolingSkills]] - Skills guide reasoning, while MCP provides callable external actions.
- [[ComputerUse]] - Computer Use can be implemented through MCP-style operations over windows, controls, and input events.
- [[NaturalLanguageInterface]] - MCP can turn natural-language requests into structured software operations.

---
title: "Model Context Protocol"
type: concept
tags: [ai, llm, tools, protocol]
sources:
  - yi-kou-qi-ba-suo-you-rang-ni-mu-xuan-de-llm-ming-ci-quan-dou-guo-yi-bian
  - blog-anthropic-building-effective-ai-agents
last_updated: 2026-09-14
knowledge_schema: synthesis-v1
---

## Definition
[[ModelContextProtocol]] is a tool-interface pattern where servers expose callable functions and schemas so an LLM can invoke external capabilities through structured calls rather than only generating free-form text.

## Current Synthesis
The sources frame MCP as closer to RPC than prompting. Function names, parameter names, and types narrow the model's action space: instead of deciding among arbitrary textual plans, the model chooses from defined functions and structured arguments. This can make external actions more deterministic, but it does not automatically solve context pollution because tool responses also return to the model context.

Anthropic's agent-building article adds MCP as one way to connect an augmented LLM to external tool ecosystems. In that framing, MCP is not the agent itself; it is an integration substrate for retrieval, tools, and memory around an LLM that still needs task-specific tailoring, clear documentation, evaluation, and guardrails.

## Key Claims
- MCP gives LLMs a structured outlet for modifying or querying the external world.
- Tool schemas create strong priors that constrain model sampling toward valid actions.
- Structured tool calls can replace many uncertain step-order decisions in UI or system-operation tasks.
- MCP has higher implementation cost than prompt-only Skills because it requires a server interface.
- Poorly designed MCP responses can still damage context quality through noisy JSON, oversized payloads, or verbose errors.
- MCP can serve as the integration layer for an augmented LLM, but reliability still depends on use-case-specific capability design and tool documentation.

## Evidence
- RPC analogy: [[yi-kou-qi-ba-suo-you-rang-ni-mu-xuan-de-llm-ming-ci-quan-dou-guo-yi-bian]] says MCP resembles servers exposing functions for the LLM to call.
- Action-space compression: [[yi-kou-qi-ba-suo-you-rang-ni-mu-xuan-de-llm-ming-ci-quan-dou-guo-yi-bian]] argues that function names and typed parameters reduce arbitrary text generation into a smaller set of structured choices.
- UI-operation example: [[yi-kou-qi-ba-suo-you-rang-ni-mu-xuan-de-llm-ming-ci-quan-dou-guo-yi-bian]] contrasts many uncertain mouse-operation steps with fewer structured calls.
- Return-value risk: [[yi-kou-qi-ba-suo-you-rang-ni-mu-xuan-de-llm-ming-ci-quan-dou-guo-yi-bian]] warns that tool outputs can pollute context if server design is careless.
- Augmented LLM substrate: [[blog-anthropic-building-effective-ai-agents]] presents MCP as a way to integrate retrieval, tools, and memory with an LLM through a growing third-party tool ecosystem.
- Tailoring requirement: [[blog-anthropic-building-effective-ai-agents]] says augmented capabilities should be tailored to the use case and exposed through easy, well-documented interfaces for the model.

## Counterevidence & Qualifications
The sources explain MCP at a conceptual level and do not compare specific MCP implementations, security models, permission boundaries, schema-design practices, or latency/cost tradeoffs. Anthropic's article cites MCP as one possible implementation route, not as a guarantee of agent reliability.

## What Changed
- Created the concept page for MCP as a structured tool-call interface and context-management device.
- Added Anthropic's augmented-LLM framing where MCP can connect retrieval, tools, and memory while still requiring good tool-interface design.

## Related Concepts
- [[LLMContextManagement]] - MCP reduces action ambiguity while adding tool results back into context.
- [[LLMToolingSkills]] - Skills guide reasoning, while MCP provides callable external actions.
- [[ComputerUse]] - Computer Use can be implemented through MCP-style operations over windows, controls, and input events.
- [[NaturalLanguageInterface]] - MCP can turn natural-language requests into structured software operations.
- [[AgentComputerInterface]] - MCP tools need model-readable schemas, argument names, examples, and boundaries.
- [[AgenticWorkflowPatterns]] - MCP can provide tool calls inside predefined workflows or autonomous agent loops.

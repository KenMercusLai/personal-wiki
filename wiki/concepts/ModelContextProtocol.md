---
title: "Model Context Protocol"
type: concept
tags: [ai, llm, tools, protocol]
sources:
  - yi-kou-qi-ba-suo-you-rang-ni-mu-xuan-de-llm-ming-ci-quan-dou-guo-yi-bian
  - blog-anthropic-building-effective-ai-agents
  - yan-li-how-llm-agents-became-what-they-look-like-in-2026
last_updated: 2026-09-17
knowledge_schema: synthesis-v1
---

## Definition
[[ModelContextProtocol]] is a tool-interface pattern where servers expose callable functions and schemas so an LLM can invoke external capabilities through structured calls rather than only generating free-form text.

## Current Synthesis
The sources frame MCP as closer to RPC than prompting. Function names, parameter names, and types narrow the model's action space: instead of deciding among arbitrary textual plans, the model chooses from defined functions and structured arguments. This can make external actions more deterministic, but it does not automatically solve context pollution because tool responses also return to the model context.

Anthropic's agent-building article adds MCP as one way to connect an augmented LLM to external tool ecosystems. In that framing, MCP is not the agent itself; it is an integration substrate for retrieval, tools, and memory around an LLM that still needs task-specific tailoring, clear documentation, evaluation, and guardrails.

A third source supplies both the clearest statement of what MCP uniquely adds and a direct critique of its ambition. In that staged history, plain tool calling only returns JSON arguments and never executes anything, so MCP contributes the missing tool runtime: the MCP client wraps tool calling, and the MCP server is the component that actually runs the tool. The same author then rejects the protocol as the endpoint, judging it over-engineered and unsuccessful as a universal solution, and arguing that a general shell reaches `curl`, `wget`, and `gh` well enough to make many MCP-style applications redundant. [[BashAsMetaTool]] and [[AgentFilesystem]] are presented as the general-purpose OS layer that replaces the specialized protocol for many tasks.

## Key Claims
- MCP gives LLMs a structured outlet for modifying or querying the external world.
- Tool schemas create strong priors that constrain model sampling toward valid actions.
- Structured tool calls can replace many uncertain step-order decisions in UI or system-operation tasks.
- MCP has higher implementation cost than prompt-only Skills because it requires a server interface.
- Poorly designed MCP responses can still damage context quality through noisy JSON, oversized payloads, or verbose errors.
- MCP can serve as the integration layer for an augmented LLM, but reliability still depends on use-case-specific capability design and tool documentation.
- MCP's distinctive contribution is the missing tool runtime - a client that wraps tool calling plus a server that executes - but one source judges the protocol over-engineered and not a universal solution, since a general shell can make many MCP-style applications redundant.

## Evidence
- RPC analogy: [[yi-kou-qi-ba-suo-you-rang-ni-mu-xuan-de-llm-ming-ci-quan-dou-guo-yi-bian]] says MCP resembles servers exposing functions for the LLM to call.
- Action-space compression: [[yi-kou-qi-ba-suo-you-rang-ni-mu-xuan-de-llm-ming-ci-quan-dou-guo-yi-bian]] argues that function names and typed parameters reduce arbitrary text generation into a smaller set of structured choices.
- UI-operation example: [[yi-kou-qi-ba-suo-you-rang-ni-mu-xuan-de-llm-ming-ci-quan-dou-guo-yi-bian]] contrasts many uncertain mouse-operation steps with fewer structured calls.
- Return-value risk: [[yi-kou-qi-ba-suo-you-rang-ni-mu-xuan-de-llm-ming-ci-quan-dou-guo-yi-bian]] warns that tool outputs can pollute context if server design is careless.
- Augmented LLM substrate: [[blog-anthropic-building-effective-ai-agents]] presents MCP as a way to integrate retrieval, tools, and memory with an LLM through a growing third-party tool ecosystem.
- Tailoring requirement: [[blog-anthropic-building-effective-ai-agents]] says augmented capabilities should be tailored to the use case and exposed through easy, well-documented interfaces for the model.
- Tool-runtime role: [[yan-li-how-llm-agents-became-what-they-look-like-in-2026]] says MCP introduces the missing role of tool runtime, with the MCP client wrapping tool calling and the MCP server executing the tool.
- Adoption critique: [[yan-li-how-llm-agents-became-what-they-look-like-in-2026]] states that MCP is over-engineered and ultimately failed to become the universal solution.
- Shell redundancy: [[yan-li-how-llm-agents-became-what-they-look-like-in-2026]] says that with bash an agent can run `curl`, `wget`, and `gh`, which makes many MCP-style applications redundant.

## Counterevidence & Qualifications
The sources explain MCP at a conceptual level and do not compare specific MCP implementations, security models, permission boundaries, schema-design practices, or latency/cost tradeoffs. Anthropic's article cites MCP as one possible implementation route, not as a guarantee of agent reliability. The staged-history source goes further and calls MCP over-engineered, but that verdict is an opinion about adoption and redundancy rather than a measured comparison against the shell on reliability, sandboxing, permissioning, or auditability.

## What Changed
- Created the concept page for MCP as a structured tool-call interface and context-management device.
- Added Anthropic's augmented-LLM framing where MCP can connect retrieval, tools, and memory while still requiring good tool-interface design.
- Added the tool-runtime role plus the dissenting view that MCP is over-engineered, not universal, and largely subsumed by a general shell.

## Related Concepts
- [[LLMContextManagement]] - MCP reduces action ambiguity while adding tool results back into context.
- [[LLMToolingSkills]] - Skills guide reasoning, while MCP provides callable external actions.
- [[ComputerUse]] - Computer Use can be implemented through MCP-style operations over windows, controls, and input events.
- [[NaturalLanguageInterface]] - MCP can turn natural-language requests into structured software operations.
- [[AgentComputerInterface]] - MCP tools need model-readable schemas, argument names, examples, and boundaries.
- [[AgenticWorkflowPatterns]] - MCP can provide tool calls inside predefined workflows or autonomous agent loops.
- [[LLMAgentStages]] - places MCP as the tool-runtime stage between tool calling and the OS layer.
- [[BashAsMetaTool]] - the general shell the newest source treats as a substitute for many MCP servers.
- [[AgentFilesystem]] - the artifact store that completes the general-purpose alternative to protocol-specific tools.

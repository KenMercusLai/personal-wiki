---
title: "Model Context Protocol"
type: concept
tags: [ai, llm, tools, protocol]
sources:
  - yi-kou-qi-ba-suo-you-rang-ni-mu-xuan-de-llm-ming-ci-quan-dou-guo-yi-bian
  - blog-anthropic-building-effective-ai-agents
  - yan-li-how-llm-agents-became-what-they-look-like-in-2026
  - context-engineering-from-the-inside-out
last_updated: 2026-09-26
knowledge_schema: synthesis-v1
---

## Definition
[[ModelContextProtocol]] is a tool-interface pattern where servers expose callable functions and schemas so an LLM can invoke external capabilities through structured calls rather than only generating free-form text.

## Current Synthesis
The sources frame MCP as closer to RPC than prompting. Function names, parameter names, and types narrow the model's action space: instead of deciding among arbitrary textual plans, the model chooses from defined functions and structured arguments. This can make external actions more deterministic, but it does not automatically solve context pollution because tool responses also return to the model context.

Anthropic's agent-building article adds MCP as one way to connect an augmented LLM to external tool ecosystems. In that framing, MCP is not the agent itself; it is an integration substrate for retrieval, tools, and memory around an LLM that still needs task-specific tailoring, clear documentation, evaluation, and guardrails.

A third source supplies both the clearest statement of what MCP uniquely adds and a direct critique of its ambition. In that staged history, plain tool calling only returns JSON arguments and never executes anything, so MCP contributes the missing tool runtime: the MCP client wraps tool calling, and the MCP server is the component that actually runs the tool. The same author then rejects the protocol as the endpoint, judging it over-engineered and unsuccessful as a universal solution, and arguing that a general shell reaches `curl`, `wget`, and `gh` well enough to make many MCP-style applications redundant. [[BashAsMetaTool]] and [[AgentFilesystem]] are presented as the general-purpose OS layer that replaces the specialized protocol for many tasks.

Context cost helps explain that critique. Full tool names, descriptions, and parameter schemas normally occupy the system prefix on every request; a broad MCP server can therefore consume effective attention even when most tools are irrelevant, and any change to the tool list can disrupt prefix-cache reuse. Recursive CLI help instead reveals one command branch at a time. MCP retains a useful niche for small, focused tool sets where structured I/O, automatic discovery, and integration simplicity outweigh the schema footprint.

## Key Claims
- MCP gives LLMs a structured outlet for modifying or querying the external world.
- Tool schemas create strong priors that constrain model sampling toward valid actions, but their always-loaded context cost grows with catalog breadth.
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
- Hidden schema context: [[context-engineering-from-the-inside-out]] shows full tool signatures inserted in the system prompt on every request and argues that unrelated schemas compete for attention.
- Qualified fit: [[context-engineering-from-the-inside-out]] prefers recursive CLI discovery for tool-heavy workflows but retains MCP for small focused tool sets, structured I/O, automatic discovery, and easy integration.

## Counterevidence & Qualifications
The sources explain MCP at a conceptual level and do not compare specific MCP implementations, security models, permission boundaries, schema-design practices, or latency/cost tradeoffs. Anthropic's article cites MCP as one possible implementation route, not as a guarantee of agent reliability. The staged-history and context-engineering sources prefer a general shell for broad capability sets, but this remains an architectural opinion rather than a measured comparison on reliability, sandboxing, permissioning, auditability, or the effect of provider-side tool search and schema masking.

## What Changed
- Added the hidden context and prefix-cache cost of always-loaded tool schemas.
- Narrowed the CLI critique by preserving MCP's fit for small focused sets, structured I/O, discovery, and integration simplicity.

## Related Concepts
- [[LLMContextManagement]] - MCP reduces action ambiguity while adding tool results back into context.
- [[LLMToolingSkills]] - Skills guide reasoning, while MCP provides callable external actions.
- [[ComputerUse]] - Computer Use can be implemented through MCP-style operations over windows, controls, and input events.
- [[NaturalLanguageInterface]] - MCP can turn natural-language requests into structured software operations.
- [[AgentComputerInterface]] - MCP tools need model-readable schemas, argument names, examples, and boundaries.
- [[AgenticWorkflowPatterns]] - MCP can provide tool calls inside predefined workflows or autonomous agent loops.
- [[LLMAgentStages]] - places MCP as the tool-runtime stage between tool calling and the OS layer.
- [[BashAsMetaTool]] - a general shell that can substitute for many broad MCP tool catalogs.
- [[AgentFilesystem]] - the artifact store that completes the general-purpose alternative to protocol-specific tools.

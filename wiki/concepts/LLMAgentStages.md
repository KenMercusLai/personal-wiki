---
title: "LLM Agent Stages"
type: concept
tags: [ai, agents, llm, tool-calling, history]
sources:
  - yan-li-how-llm-agents-became-what-they-look-like-in-2026
last_updated: 2026-09-17
knowledge_schema: synthesis-v1
---

## Definition
[[LLMAgentStages]] is the account of LLM agent architecture as a sequence of accumulating integration layers: structured output, tool calling, a protocol-level tool runtime, and finally a general-purpose operating system of bash and files.

## Current Synthesis
The source presents agent architecture as a stack of integration layers rather than a single design. Stage 1 makes the model emit a machine-readable format so the natural-language "magic function" can be embedded in ordinary programmatic functions. Stage 2, tool calling, is the first standardized wrapper around structured output, introduced by the [[OpenAI]] API that became the de facto standard; it names a tool with JSON arguments, but the API returns those arguments and executes nothing. Stage 3, [[ModelContextProtocol]], adds the role tool calling omits - the tool runtime - through an MCP client that wraps tool calling and an MCP server that runs the tool.

The same source then rejects the specialized protocol as the endpoint. Stage 4 falls back to the general environment: [[BashAsMetaTool]] reaches the command-line ecosystem, [[AgentFilesystem]] stores artifacts that cannot round-trip through the model in one step, and the OS is the runtime for both. The author reads later model progress - separated thinking and output, RL on structured JSON and coding, larger context windows - as further shrinking the scaffolding, since ReAct-style loops and chain-of-thought prompting were answers to problems that trained behaviors now handle. What remains outside the stack is the browser and the GUI, which bash cannot cover and which the source marks as the next stage.

## Key Claims
- Agent architecture is best read as accumulating integration layers rather than one settled design.
- Structured output is the foundation: it converts natural-language generation into a callable function that normal programs can embed.
- Tool calling standardizes that contract but deliberately stops at argument generation, leaving execution to the caller.
- [[ModelContextProtocol]] is positioned as the layer that supplies the missing tool runtime, not as a model capability.
- The source's preferred endpoint is the general-purpose OS layer - [[BashAsMetaTool]] plus [[AgentFilesystem]] - which it expects to subsume many narrow tool integrations.
- Model training progress (thinking/output separation, RL for JSON and coding, larger context) can obsolete workflow scaffolds that existed only to work around weaker models.
- The browser and GUI remain the acknowledged gap in the stack and are framed as the next stage.

## Evidence
- Stage sequence: [[yan-li-how-llm-agents-became-what-they-look-like-in-2026]] orders the history as structured output, tool calling, MCP, then bash, filesystem, and OS.
- Structured-output foundation: [[yan-li-how-llm-agents-became-what-they-look-like-in-2026]] says structured output is what lets the magic function be embedded into a normal programmatic function.
- Tool-calling contract: [[yan-li-how-llm-agents-became-what-they-look-like-in-2026]] says the API returns JSON arguments but does not execute the tool, making tool calling structured output with a more explicit interface.
- Tool-runtime role: [[yan-li-how-llm-agents-became-what-they-look-like-in-2026]] says MCP introduces the missing role of tool runtime, with the server doing the execution.
- OS endpoint: [[yan-li-how-llm-agents-became-what-they-look-like-in-2026]] answers "what is the runtime for bash and filesystem?" with "Yes, OS."
- Obsolete scaffolding: [[yan-li-how-llm-agents-became-what-they-look-like-in-2026]] claims ReAct became less necessary once structured output was standardized and that CoT prompting may matter less once thinking/output separation is trained in.
- Remaining gap: [[yan-li-how-llm-agents-became-what-they-look-like-in-2026]] names the browser as the ultimate GUI program that bash cannot cover.

## Counterevidence & Qualifications
The stage model is one practitioner's narrative rather than a measured history, and it compresses commercially and technically distinct products into four steps. The claim that MCP "failed to become the universal solution" is an opinion about adoption, not an adoption measurement, and the essay never compares MCP against bash on reliability, permissions, or auditability. The prediction that ReAct and chain-of-thought scaffolding become obsolete assumes continued model progress and does not address tasks where explicit reasoning traces remain valuable for inspection or control.

## What Changed
- Created the concept page for the source's staged history of LLM agent architecture.
- Added structured output and tool calling as the first two stages, with MCP as the tool-runtime stage.
- Added the OS layer - bash, filesystem, and runtime - as the source's preferred endpoint.

## Related Concepts
- [[BashAsMetaTool]] - the shell is the tool that anchors Stage 4.
- [[AgentFilesystem]] - the file layer is the other half of the OS stage.
- [[ModelContextProtocol]] - MCP is the protocol stage the essay argues is over-engineered.
- [[CodingAgentMinimalTooling]] - the same minimal-tool instinct applied specifically to coding agents.
- [[AgenticWorkflowPatterns]] - ReAct and workflow scaffolds are the structures this stage model expects to shrink.
- [[ComputerUse]] - the browser and GUI are the stage the model does not yet cover.
- [[AgentExperience]] - each stage changes what the agent can perceive and do in its environment.

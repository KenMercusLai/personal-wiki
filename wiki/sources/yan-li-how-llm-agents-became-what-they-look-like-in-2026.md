---
title: "How LLM Agents Became What They Look Like in 2026?"
type: source
tags: [ai, agents, llm, tool-calling, mcp, agent-skills, context-management]
date: 2026-09-17
source_file: "/mnt/ken_personal_wiki/Articles/Yan Li - How LLM Agents Became What They Look Like in 2026.md"
---

## Summary
[[YanLi]] reads the present shape of LLM agents as the product of four integration stages. Structured output first turned the model into an embeddable "magic function", [[OpenAI]]'s tool-calling API standardized that contract into named tools with JSON arguments while still executing nothing itself, and [[ModelContextProtocol]] added the missing tool runtime through an MCP client that wraps tool calling and an MCP server that actually runs the tool. The author judges MCP over-engineered and not a universal solution, and argues that the practical floor is instead [[LLMAgentStages]]'s Stage 4: a general-purpose operating system where [[BashAsMetaTool]] reaches `curl`, `wget`, and `gh` without bespoke integrations, and an [[AgentFilesystem]] holds the images, audio, and long text that cannot round-trip through the model in one step. The essay closes on [[AgentDeploymentTradeoffs]] - latency, reproducibility, privacy and cost, and multimodal interaction - and on agent-skills as a file-based dynamic-prompt-injection protocol that it expects to be adopted more widely than MCP.

## Key Claims
- Structured output is what lets an LLM be embedded in ordinary software: constraining generation to a machine-readable format converts natural-language in and natural-language out into a function a normal program can call.
- Tool calling is the first standardized wrapper around structured output, introduced by the [[OpenAI]] API that became the de facto standard for LLM APIs; the tool takes JSON arguments, but the API only returns those arguments and never executes the tool.
- [[ModelContextProtocol]] supplies the role tool calling omits - the tool runtime - through a client-server architecture in which the MCP client wraps tool calling and the MCP server executes the tool.
- The author's own verdict is that MCP is over-engineered and failed to become the universal solution, and that bash already makes many MCP-style applications redundant.
- [[BashAsMetaTool]]: because LLMs are strong at bash as well as JSON, one shell tool can reach `curl`, `wget`, `gh`, and the wider command-line ecosystem, making it "potentially the only tool an agent needs".
- The root cause of tool multiplicity is that intermediate artifacts - images, audio, long text - cannot be returned to the LLM in a single step, so each desired follow-up (summarize, zip, upload) would need its own tool and the combinations grow exponentially.
- [[AgentFilesystem]] is the decoupling answer: store the artifact, then let the agent choose what to do with it on a later turn by LLM decision, with the operating system as the runtime for both bash and the file layer.
- "Stage NEXT" is the browser and GUI, because the ultimate graphical program cannot be covered by bash, and GUI exists to bypass the TTY precisely because complex tasks overwhelm a human's context window.
- Model progress is reshaping the scaffolding around agents: separation of thinking and output, RL for structured JSON and coding, and larger context windows make ReAct loops and chain-of-thought-style prompting progressively less necessary.
- [[AgentDeploymentTradeoffs]] bound where agents fit: latency versus quality (the author puts acceptable chatbot TTFT at 20-30 seconds), reproducibility (predictable waits and consistent output, which is why workflows still matter), privacy and cost (small open-weight or edge models), and demand for browser-use, computer-use, and GUI-capable multimodal agents.
- Agent-skills is, in this account, "simply a protocol for dynamic prompt injection" in which the agent decides which prompts to load; in practice it is a set of files that can pack `prompt.md`, `tools.sh`, `helper.py`, executables, libraries, and arbitrary assets.
- Agent-skills should out-adopt MCP because it is a self-contained, distributable folder with no runtime or dependency requirements as long as the client agent already operates at Stage 4, and it can therefore be shipped by an OS package manager alongside ordinary programs.

## Key Quotes
> "Tool calling is essentially the first standardized wrapper around structured output" - Stage 2 of the essay's history.

> "MCP is an over-engineered approach that ultimately failed to become the universal solution." - the author's verdict on Stage 3.

> "Bash becomes a 'meta tool' for agents: potentially the only tool an agent needs." - on why one shell tool subsumes many integrations.

> "The root cause is that intermediate artifacts (images, audio, long texts) cannot be returned directly to the LLM in a single step." - the diagnosis behind the filesystem stage.

> "What if an OS distro can do `pacman -S someprogram someprogram-agent-skill`?" - the distribution metaphor for agent-skills.

## Connections
- [[YanLi]] - author of the essay.
- [[LLMAgentStages]] - the staged structured-output, tool-calling, MCP, and OS-runtime history this source supplies.
- [[BashAsMetaTool]] - the shell-as-single-tool claim the essay builds Stage 4-1 on.
- [[AgentFilesystem]] - the intermediate-artifact store that decouples tool combinations.
- [[AgentDeploymentTradeoffs]] - the latency, reproducibility, privacy/cost, and multimodality constraints the essay lists as problems.
- [[ModelContextProtocol]] - the source's central foil: MCP supplies the tool runtime but is judged over-engineered.
- [[OpenAI]] - credited with the tool-calling API that became the de facto standard.
- [[LLMToolingSkills]] - agent-skills as the source's dynamic prompt-injection and file-distribution framing.
- [[CodingAgentMinimalTooling]] - bash and filesystem as the minimal, deliberately shaped tool surface.
- [[ComputerUse]] - browser-use and computer-use as the uncaptured next stage.
- [[AgenticWorkflowPatterns]] - reproducibility is the stated reason workflows continue to matter.
- [[RetrievalAugmentedGeneration]] - latency pressure is the stated reason non-agentic RAG still exists.
- [[LLMContextManagement]] - tool results, artifacts, and context limits are the recurring constraint behind every stage.
- [[AgenticRAG]] - bash plus filesystem is the same minimal-tool retrieval loop applied to the general environment.
- [[ProductionAgentInfrastructure]] - long-running agents need the OS-level storage and execution layer the essay treats as the runtime.

## Contradictions
- Directly qualifies [[ModelContextProtocol]]'s framing as an integration substrate: the same source accepts that MCP adds a real tool runtime but argues it is over-engineered, failed as a universal solution, and is largely subsumed by bash.
- Tensions with the wiki's agent-skills and MCP material: [[LLMToolingSkills]] treats Skills as prompt-level guidance that still needs an execution channel, while this source packages execution (`tools.sh`, `bin/executable`, libraries) inside the skill folder.
- Qualifies [[ComputerUse]] and [[AgentComputerInterface]] by treating the GUI as an unsolved frontier rather than a solved action surface.
- No effective image references were present in the source Markdown; the only non-prose element is a link to the referenced external essay.

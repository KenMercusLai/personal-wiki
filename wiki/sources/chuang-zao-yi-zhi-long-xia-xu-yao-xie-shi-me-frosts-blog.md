---
title: "创造一只龙虾，需要些什么?"
type: source
tags: [ai, agents, ai-native, openclaw, bub]
date: 2026-02-12
source_file: "/mnt/ken_personal_wiki/Articles/创造一只龙虾，需要些什么? | Frost's Blog.md"
---

## Summary
[[FrostMing]] describes turning [[PsiACE]]'s [[Bub]] into an [[OpenClaw]]-like Telegram agent, then removing most framework-owned messaging behavior in favor of a reasoning core, basic shell and file tools, agent-created [[LLMToolingSkills|Skills]], and a container startup protocol. The article names this [[AINativeAgentArchitecture|AI-native agent architecture]]: humans issue natural-language requests while the agent manages its own instructions and small amounts of code as runtime artifacts. The deployment is a provocative practitioner prototype rather than evidence that unreviewed, prompt-governed autonomy is reliable or safe.

## Key Claims
- The first Bub prototype added Telegram handlers, message IDs, user metadata, media, stickers, and reactions in ordinary framework code, reaching much of OpenClaw's visible functionality apart from memory and tool differences.
- [[CodingAgentMinimalTooling]] can shrink the framework to a reasoning core plus shell and file access because an agent can use the operating system and HTTP APIs to compose missing capabilities.
- The source distinguishes framework-defined tools from agent-created, agent-editable [[LLMToolingSkills|Skills]], although it acknowledges that Skills may include small amounts of code managed outside the main codebase.
- [[AINativeAgentArchitecture]] is presented as a third stage after one-shot chatbots and tool-calling agents: the agent manages its own tools, skills, and implementation details while the human interacts through natural language.
- Bub learned Telegram sending as a Skill, including images, stickers, and reactions, which motivated removing the framework's built-in sender and then its listener.
- A startup protocol lets a Docker container run an agent-written startup script, with the built-in listener as fallback; one-shot command modes such as `codex exec <prompt>` or `claude <prompt>` let the script wake the agent.
- The author's strongest design claim is that behavior such as replying or heartbeats should not be forced by the framework; the agent should decide what to do after being awakened by Telegram or a scheduler.

## Key Quotes
> "我希望框架越小越好，小到只有一个推理核心，作为 AI 的大脑，把更多的自由留给 AI。" - on reducing the framework to a reasoning core.

> "我在 Bub 里趟出了一条不用 Bub 的路。" - on using Bub to discover a runtime pattern that removes most Bub-specific behavior.

## Connections
- [[FrostMing]] - author and practitioner describing the Bub experiment.
- [[PsiACE]] - Bub's creator and Frost Ming's collaborator on the experiment.
- [[Bub]] - project transformed from a small agent into a self-bootstrapping Telegram bot.
- [[OpenClaw]] - target whose visible personal-agent behavior motivated the initial reproduction.
- [[AINativeAgentArchitecture]] - name for the source's agent-managed tools, Skills, and runtime-artifact thesis.
- [[CodingAgentMinimalTooling]] - shell and file operations form the proposed minimum capability substrate.
- [[LLMToolingSkills]] - agent-created text and code artifacts replace framework-owned feature implementations.
- [[HeadlessAgentArchitecture]] - Telegram, a startup script, container process management, and one-shot execution create the event-driven runtime.
- [[AgentPermissionModel]] - supplies the main safety qualification to prompt-only behavioral control and unreviewed code.

## Contradictions
- The claim that all requirements should be expressed only through prompts and that compliance may be left to the agent directly conflicts with [[AgentPermissionModel]], which treats externally enforced isolation, scoped credentials, and sensitive-action gates as the root boundary.
- The source's willingness to leave agent-written code unread conflicts with [[SoftwareVerification]] and [[ProductionAgentInfrastructure]] when the agent holds a GitHub token, shell, filesystem, network, or messaging authority.
- The framework-elimination thesis qualifies rather than refutes [[OpenClaw]]'s larger runtime: the experiment demonstrates a minimal personal deployment, but supplies no benchmark for long-running memory, multi-user isolation, recovery, auditability, cost, or adversarial input.
- Results are first-person and qualitative. The article provides no reproducible configuration, task suite, failure rate, security review, or longitudinal comparison showing that the bot becomes more capable or more humanlike as model quality rises.
- The supplied Markdown contains no effective image references, so no visual assets or manifest were required.

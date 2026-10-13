---
title: "DeepChat"
type: entity
tags: [ai, agents, desktop, open-source]
sources:
  - zhuan-fang-deepchat-zuo-zhe-men-liao-liao-ben-di-you-xian-mcp-yu-agent-memory
last_updated: 2026-10-13
knowledge_schema: synthesis-v1
---

## Overview
[[DeepChat]] is an open-source, [[LocalFirstSoftware|local-first]] desktop agent client that evolved from a Vue chatbot into a model-independent workspace combining chat, files, tools, memory, and computer interaction.

## Current Profile
DeepChat keeps conversations, files, memories, configuration, and model credentials on the user's computer by default, with encrypted SQLite, system Keychain integration, and user-authorized export. Its developers describe the product as an unrestricted “ChatGPT + Codex” shape and as a customizable keyboard: useful directly, but intentionally open to modification.

The architecture combines shared AI SDK request primitives with provider-specific routing and an external model-metadata repository. MCP connections can use SSE, stdio, or an in-memory bridge, while bundled Node.js and Python environments reduce setup friction. Computer Use layers a Cua driver behind an MCP server and a Skill; Tape records execution evidence; and Memory derives durable conclusions with traceable links back to Tape.

## Key Characteristics
- Local-first desktop storage and interaction are the stable product principle across the chatbot-to-agent rewrite.
- Provider-neutral model access combines common SDK primitives, provider-specific adaptations, and externally refreshed capability metadata.
- Embedded runtimes turn MCP installation and dependency handling into product responsibility rather than a user prerequisite.
- Tape, anchors, and memory tools separate immutable execution evidence from distilled long-lived conclusions.
- Skills explain workflows over MCP and other tools, including the Cua-backed Computer Use integration.
- Three permission modes, encryption, Keychain storage, per-agent memory separation, and content-free audit events provide partial safety controls.
- A separate chat mode remains alongside agent workflows because product evolution did not remove demand for simple conversation.

## Evidence
- Product identity and evolution: [[zhuan-fang-deepchat-zuo-zhe-men-liao-liao-ben-di-you-xian-mcp-yu-agent-memory]] describes the 2025 start, three-to-four-month agent rewrite, and later restoration of chat mode.
- Local-first controls: [[zhuan-fang-deepchat-zuo-zhe-men-liao-liao-ben-di-you-xian-mcp-yu-agent-memory]] reports encrypted SQLite, Keychain integration, local credentials and data, and user-authorized export.
- Integration architecture: [[zhuan-fang-deepchat-zuo-zhe-men-liao-liao-ben-di-you-xian-mcp-yu-agent-memory]] describes AI SDK foundations, provider routing, public metadata, SSE, stdio, in-memory MCP, and bundled runtimes.
- Agent capabilities: [[zhuan-fang-deepchat-zuo-zhe-men-liao-liao-ben-di-you-xian-mcp-yu-agent-memory]] and its retained UI screenshot show memory, Tape, skills, planning, user-interaction, browser, and subagent surfaces.
- Safety boundary: [[zhuan-fang-deepchat-zuo-zhe-men-liao-liao-ben-di-you-xian-mcp-yu-agent-memory]] gives three approval modes and explains why stricter sandboxing can conflict with legitimate global tools.

## Qualifications
The profile comes from an interview with the project's developers rather than independent testing. The source supplies no benchmark of memory quality, model compatibility, task completion, security, stability, token cost, or comparative usability. Several capabilities—especially self-updating memory, insight formation, richer observability, and stronger sandboxing—are described as ongoing work.

## What Changed
- Established DeepChat as a local-first desktop agent client rather than only a chatbot.
- Separated its Tape evidence layer from its derived Memory layer.
- Added the embedded-runtime, provider-metadata, Computer Use, and permission architecture.

## Relationships
- [[LocalFirstSoftware]] - determines where DeepChat places user data, credentials, and workspace context.
- [[AgentMemory]] - DeepChat derives durable, inspectable conclusions from execution history.
- [[TapeAndAnchors]] - supplies the append-only ledger and recoverable context substrate.
- [[ModelContextProtocol]] - exposes external and internal resources through productized client connections.
- [[LLMToolingSkills]] - explains how DeepChat agents should combine tools and workflows.
- [[ComputerUse]] - implemented through a Cua driver, MCP server, and usage Skill.
- [[AgentPermissionModel]] - frames DeepChat's approval, encryption, isolation, and sandbox tradeoffs.

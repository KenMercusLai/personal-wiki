---
title: "DeepChat"
type: entity
tags: [ai, agents, desktop, open-source]
sources:
  - zhuan-fang-deepchat-zuo-zhe-men-liao-liao-ben-di-you-xian-mcp-yu-agent-memory
  - deepchat-tape
last_updated: 2026-10-25
knowledge_schema: synthesis-v1
---

## Overview
[[DeepChat]] is an open-source, [[LocalFirstSoftware|local-first]] desktop agent client that evolved from a Vue chatbot into a model-independent workspace combining chat, files, tools, memory, and computer interaction.

## Current Profile
DeepChat keeps conversations, files, memories, configuration, and model credentials on the user's computer by default, with encrypted SQLite, system Keychain integration, and user-authorized export. Its developers describe the product as an unrestricted “ChatGPT + Codex” shape and as a customizable keyboard: useful directly, but intentionally open to modification.

The architecture combines shared AI SDK request primitives with provider-specific routing and an external model-metadata repository. MCP connections can use SSE, stdio, or an in-memory bridge, while bundled Node.js and Python environments reduce setup friction. Computer Use layers a Cua driver behind an MCP server and a Skill; Tape records execution evidence; and Memory derives durable conclusions with traceable links back to Tape.

DeepChat introduced Tape incrementally beside its mutable message table. Model context is assembled from currently effective Tape facts, ViewManifest records the selected entries and request fingerprints, and Tape Inspector presents the resulting session, model, tool, anchor, and memory timeline. Its compactor can move an anchor without a new summary when that produces a smaller next view. Its Execution Journal writes dispatch intent before invoking a tool and parks dispatches with no recorded outcome as `indeterminate` rather than replaying them automatically.

## Key Characteristics
- Local-first desktop storage and interaction are the stable product principle across the chatbot-to-agent rewrite.
- Provider-neutral model access combines common SDK primitives, provider-specific adaptations, and externally refreshed capability metadata.
- Embedded runtimes turn MCP installation and dependency handling into product responsibility rather than a user prerequisite.
- Tape, anchors, per-request manifests, and memory tools separate immutable execution evidence, assembled model context, and distilled long-lived conclusions.
- Skills explain workflows over MCP and other tools, including the Cua-backed Computer Use integration.
- Three permission modes, encryption, Keychain storage, per-agent memory separation, write-ahead tool dispatch records, and content-free audit events provide partial safety controls.
- A separate chat mode remains alongside agent workflows because product evolution did not remove demand for simple conversation.

## Evidence
- Product identity and evolution: [[zhuan-fang-deepchat-zuo-zhe-men-liao-liao-ben-di-you-xian-mcp-yu-agent-memory]] describes the 2025 start, three-to-four-month agent rewrite, and later restoration of chat mode.
- Local-first controls: [[zhuan-fang-deepchat-zuo-zhe-men-liao-liao-ben-di-you-xian-mcp-yu-agent-memory]] reports encrypted SQLite, Keychain integration, local credentials and data, and user-authorized export.
- Integration architecture: [[zhuan-fang-deepchat-zuo-zhe-men-liao-liao-ben-di-you-xian-mcp-yu-agent-memory]] describes AI SDK foundations, provider routing, public metadata, SSE, stdio, in-memory MCP, and bundled runtimes.
- Agent capabilities: [[zhuan-fang-deepchat-zuo-zhe-men-liao-liao-ben-di-you-xian-mcp-yu-agent-memory]] and its retained UI screenshot show memory, Tape, skills, planning, user-interaction, browser, and subagent surfaces.
- Safety boundary: [[zhuan-fang-deepchat-zuo-zhe-men-liao-liao-ben-di-you-xian-mcp-yu-agent-memory]] gives three approval modes and explains why stricter sandboxing can conflict with legitimate global tools.
- Incremental Tape migration: [[deepchat-tape]] says the message table continued to render the UI while model context moved to Tape, and old conversations were migrated only when reopened.
- Context observability: [[deepchat-tape]] describes ViewManifest recording selected entries, anchor, budget allocation, and prompt and tool hashes; its retained Inspector screenshot shows session, model, tool, view, terminal, and memory events on one searchable timeline.
- Recovery behavior: [[deepchat-tape]] documents boundary-only compaction and the `run_started`, `dispatch_committed`, `tool_outcome`, and `run_terminal` execution journal.

## Qualifications
The profile comes from two first-party developer accounts rather than independent testing. They supply no benchmark of memory quality, model compatibility, task completion, security, stability, token cost, compaction fidelity, or comparative usability. The Execution Journal cannot determine whether an external effect occurred after dispatch but before an outcome was recorded; DeepChat therefore parks that state instead of claiming exactly-once execution. The ordinary chat UI still reads the mutable message table rather than a Tape projection, leaving a dual-representation seam. Several capabilities—especially self-updating memory, insight formation, fuller pre-edit inspection, and stronger sandboxing—remain incomplete.

## What Changed
- Added the incremental dual-store migration from message history to Tape-backed model context.
- Added ViewManifest and Tape Inspector as context and execution observability mechanisms.
- Added boundary-only compaction and the smaller-next-view success criterion.
- Added write-ahead tool dispatch and explicit `indeterminate` crash recovery.

## Relationships
- [[LocalFirstSoftware]] - determines where DeepChat places user data, credentials, and workspace context.
- [[AgentMemory]] - DeepChat derives durable, inspectable conclusions from execution history.
- [[TapeAndAnchors]] - supplies the append-only ledger and recoverable context substrate.
- [[ModelContextProtocol]] - exposes external and internal resources through productized client connections.
- [[LLMToolingSkills]] - explains how DeepChat agents should combine tools and workflows.
- [[ComputerUse]] - implemented through a Cua driver, MCP server, and usage Skill.
- [[AgentPermissionModel]] - frames DeepChat's approval, encryption, isolation, and sandbox tradeoffs.
- [[EffectLog]] - implemented through an Execution Journal that records dispatch before tool invocation and outcome afterward.
- [[AgentSystemTransparency]] - ViewManifest and Tape Inspector expose assembled context and execution evidence.

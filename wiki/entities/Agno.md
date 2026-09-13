---
title: "Agno"
type: entity
tags: [ai, agents, developer-tools]
sources:
  - ru-he-zi-jian-yi-ge-zi-ji-de-cursor-codebase
last_updated: 2026-09-13
knowledge_schema: synthesis-v1
---

## Overview
[[Agno]] is the AI agent framework used in the source's sample implementation of a local codebase analysis assistant.

## Current Profile
The source presents Agno as the wrapper around model configuration, agent description, structured instructions, custom Python tools, Markdown output, and an interactive CLI app. Its role is not the retrieval algorithm itself; instead, it provides the agent container that decides when to call `search_codebase` and `read_file_segment`, then turns those tool results into troubleshooting or code-analysis reports.

## Key Characteristics
- Hosts an agent with a model, description, instructions, tools, and Markdown output.
- Accepts ordinary Python functions as tools for repository search and file-segment reading.
- Supports a CLI interaction loop for asking codebase questions.
- Is used in the source to build a text-matching codebase assistant rather than a vector-indexed one.

## Evidence
- Agent setup: [[ru-he-zi-jian-yi-ge-zi-ji-de-cursor-codebase]] defines an Agno `Agent` with model configuration, role description, instructions, tools, and Markdown output.
- Tool integration: [[ru-he-zi-jian-yi-ge-zi-ji-de-cursor-codebase]] passes `search_codebase` and `read_file_segment` directly into the agent's tool list.
- Runtime use: [[ru-he-zi-jian-yi-ge-zi-ji-de-cursor-codebase]] shows screenshots where the agent calls those tools before producing a code explanation.

## Qualifications
The source is a small tutorial example, not a comparative evaluation of Agno against LangChain, Semantic Kernel, or other agent frameworks. It does not discuss Agno's production reliability, observability, permissions, or deployment model.

## What Changed
- Created the initial entity profile for Agno as a framework used to assemble a codebase QA agent.

## Relationships
- [[AIApplicationFramework]] - Agno is used as a framework for model calls, tools, instructions, and a CLI agent loop.
- [[AgenticRAG]] - Agno hosts the search/read loop used to retrieve code context on demand.
- [[CodingAgentMinimalTooling]] - the example exposes a small search/read tool surface to the agent.
- [[Cursor]] - the source positions Agno as a way to build a local approximation of Cursor-style codebase QA.

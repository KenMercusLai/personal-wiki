---
title: "Nowledge Mem"
type: entity
tags: [ai, agents, memory, knowledge-management]
sources:
  - wei-ai-agent-gou-jian-ji-yi-xi-tong
last_updated: 2026-10-08
knowledge_schema: synthesis-v1
---

## Overview
[[NowledgeMem]] is presented by its builder as a cross-tool personal and team memory layer that captures conversations, maintains an evolving knowledge graph, and exposes selected knowledge to AI agents.

## Current Profile
The product organizes knowledge as raw Traces, typed atomic Units, and multi-source Crystals. It combines a daily Markdown working-memory file, hybrid retrieval, bitemporal metadata, explicit evolution relationships, decay and confidence scores, background jobs, graph exploration, and connectors across coding tools, chat systems, browsers, notes, mobile apps, CLI, TUI, and MCP.

Its stated product thesis is that memory should outlive individual AI tools while remaining locally stored, exportable, inspectable, editable, and user-controlled. The source depicts a substantial architecture, but it is a first-party design account rather than an independently evaluated product profile.

## Key Characteristics
- Uses Trace, Unit, and Crystal as progressively denser knowledge forms.
- Produces a daily `~/ai-now/memory.md` attention brief readable by different agents.
- Combines vector, full-text, entity, community, label, graph, HyDE, and LLM-reranking retrieval paths.
- Represents knowledge change through `replaces`, `enriches`, `confirms`, and `challenges` relationships.
- Separates attention decay from accumulated confidence and uses conservative archival conditions.
- Runs scheduled and event-driven background intelligence under explicit cost and quality guards.
- Connects multiple agent and note-taking tools through capture, recall, and lifecycle hooks.

## Evidence
- Knowledge model and working memory: [[wei-ai-agent-gou-jian-ji-yi-xi-tong]] describes Trace, Unit, Crystal, daily focus selection, and the Markdown handoff file.
- Retrieval and time: [[wei-ai-agent-gou-jian-ji-yi-xi-tong]] specifies fast and deep search paths, source-thread expansion, event versus record time, precision, and bounded time boosts.
- Evolution and forgetting: [[wei-ai-agent-gou-jian-ji-yi-xi-tong]] documents four evolution relations, human conflict review, decay, confidence, importance floors, and archive gates.
- Operations and integration: [[wei-ai-agent-gou-jian-ji-yi-xi-tong]] describes 13 background tasks, cost guards, graph tools, native plugins, platform synchronization, local notes, apps, CLI, and MCP.

## Qualifications
The evidence is supplied by the product builder and does not include an external security audit, retrieval benchmark, longitudinal accuracy study, cost comparison, privacy threat model, conflict-resolution evaluation, or independently verified adoption data. Named thresholds and weights should be read as implementation choices, not established universal optima.

## What Changed
- Created a profile of Nowledge Mem as a cross-tool memory product and architecture.
- Recorded its progressive knowledge forms, retrieval paths, temporal model, maintenance policies, and control surface.

## Relationships
- [[AgentMemory]] - Nowledge Mem is an implementation of persistent cross-session agent memory.
- [[MemoryEvolution]] - its graph records progression and validation relationships among memories.
- [[MemoryConflictResolution]] - detected contradictions are presented for user adjudication.
- [[MemoryForgetting]] - its health model separates decay, confidence, importance floors, and archival.
- [[BitemporalMemory]] - its records carry event time and record time with explicit precision.
- [[LLMContextManagement]] - its working-memory file and context injection select bounded inputs for agents.
- [[LLMToolingSkills]] - corroborated knowledge is proposed as raw material for executable skills.

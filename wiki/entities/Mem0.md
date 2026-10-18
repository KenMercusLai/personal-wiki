---
title: "Mem0"
type: entity
tags: [ai, agents, memory, research]
sources:
  - custom-llm-memory-layer
last_updated: 2026-10-18
knowledge_schema: synthesis-v1
---

## Overview
[[Mem0]] is an agent-memory architecture represented here through a tutorial that adapts its extraction and update phases.

## Current Profile
The depicted architecture processes messages and historical context into candidate memories, retrieves similar stored memories, and uses tool-mediated add, update, delete, or no-op decisions before writing revised state. A central database supplies summaries, past messages, similar-memory retrieval, and persistence across the phases.

## Key Characteristics
- Separates candidate-memory extraction from state maintenance.
- Compares new candidates with similar existing memories before mutation.
- Exposes add, update, delete, and no-op as distinct maintenance outcomes.
- Uses a database as persistent context and updated-memory storage.

## Evidence
- Architecture: [[custom-llm-memory-layer]] reproduces a Mem0 paper diagram with extraction and update boundaries, database flows, and four maintenance actions.
- Adaptation: [[custom-llm-memory-layer]] implements a simplified Mem0-inspired lifecycle with DSPy ReAct tools and vector retrieval.

## Qualifications
This page is grounded in a secondary tutorial rather than a complete reading of the Mem0 paper or current product documentation. The tutorial simplifies the architecture, provides no direct Mem0 evaluation, and contains code inconsistencies that should not be attributed automatically to the original system.

## What Changed
- Established Mem0 as the source architecture for the tutorial's extraction-and-maintenance design.

## Relationships
- [[AgentMemory]] - is the broader capability Mem0 organizes into extraction, retrieval, and update phases.
- [[MemoryConflictResolution]] - motivates update and delete decisions when candidate facts differ from stored state.
- [[VectorDatabase]] - can supply similar-memory retrieval in a simplified implementation.
- [[DSPy]] - is used by the tutorial to reproduce a Mem0-inspired agent loop.

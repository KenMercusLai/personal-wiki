---
title: "DSPy"
type: entity
tags: [ai, llm, framework, agents]
sources:
  - custom-llm-memory-layer
last_updated: 2026-10-18
knowledge_schema: synthesis-v1
---

## Overview
[[DSPy]] is an LLM application framework represented here through signatures, structured prediction, asynchronous calls, tools, and ReAct agents used in a memory-system tutorial.

## Current Profile
The tutorial defines typed input and output contracts as DSPy signatures whose docstrings guide model behavior. It uses `Predict` for atomic-memory extraction and `ReAct` for both optional memory retrieval and maintenance actions, with ordinary asynchronous Python functions exposed as tools through their signatures and docstrings.

## Key Characteristics
- Declares structured model inputs and outputs through signatures.
- Uses signature documentation as behavioral instructions.
- Wraps ordinary Python functions as model-callable tools.
- Supports ReAct loops with bounded iteration counts.

## Evidence
- Structured extraction: [[custom-llm-memory-layer]] defines a `MemoryExtract` signature and calls `dspy.Predict` asynchronously.
- Selective retrieval: [[custom-llm-memory-layer]] gives a ReAct response generator a memory-search tool and a maximum of four iterations.
- Maintenance: [[custom-llm-memory-layer]] gives a second ReAct agent add, update, delete, and no-op tools.

## Qualifications
The source is a tutorial, not framework documentation or a comparative evaluation. Its claims and code reflect one point-in-time usage pattern, and several surrounding snippets contain undefined or mismatched variables.

## What Changed
- Established DSPy as the orchestration framework used across extraction, retrieval, and memory maintenance.

## Relationships
- [[AgentMemory]] - is the application capability assembled with DSPy in the source.
- [[Mem0]] - supplies the architectural inspiration implemented through DSPy.
- [[AgenticRAG]] - shares the pattern of model-directed, iterative tool retrieval.
- [[Qdrant]] - is accessed by the Python tools that DSPy's agents can invoke.

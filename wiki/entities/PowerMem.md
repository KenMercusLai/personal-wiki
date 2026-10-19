---
title: "PowerMem"
type: entity
tags: [ai, agents, memory]
sources:
  - powermem-forgetting-design
last_updated: 2026-10-19
knowledge_schema: synthesis-v1
---

## Overview
[[PowerMem]] is an open-source agent-memory project whose version 1.1.1 forgetting design is described in a project-authored engineering article.

## Current Profile
The described subsystem converts an importance score into working, short-term, or long-term placement, applies tier-specific exponential decay, and uses access or importance to promote memories. Retrieval multiplies semantic relevance by the current decay factor, while separate components inject lifecycle logic and reduce redundancy through exact deduplication, semantic deduplication, and LLM compression.

This is a coherent configurable design, but the available source is explanatory and promotional. It does not establish that the thresholds, multipliers, biological mappings, or retrieval formula outperform alternative memory policies.

## Key Characteristics
- Places memories into working, short-term, and long-term tiers from an importance score.
- Applies decay-rate multipliers of 2.0, 1.5, and 1.0 across those tiers.
- Promotes lower-tier memories after repeated access or sufficient importance.
- Injects management logic when memories are created, accessed, and searched.
- Ranks retrieval by multiplying relevance by a time-sensitive decay factor.
- Combines decay with exact deduplication, semantic deduplication, and LLM compression.

## Evidence
- Tiering and promotion: [[powermem-forgetting-design]] specifies the three levels, importance boundaries, access threshold, and decay multipliers.
- Retrieval control: [[powermem-forgetting-design]] gives the `relevance_score × decay_factor` ranking formula.
- Component architecture: [[powermem-forgetting-design]] separates `ImportanceEvaluator`, `EbbinghausAlgorithm`, `EbbinghausIntelligencePlugin`, and `MemoryOptimizer` responsibilities.
- Optimization methods: [[powermem-forgetting-design]] names MD5 exact matching, cosine-similarity semantic matching, and LLM compression.

## Qualifications
The sole evidence is a project-authored article about version 1.1.1. It supplies no code-level verification, retrieval benchmark, calibration study, ablation, storage-cost result, false-forgetting rate, security analysis, or comparison with learned ranking, explicit feedback, FSRS, ACT-R, or another agent-memory implementation. Its neuroscience and Shannon-information framing should be read as design motivation, not validation of the numeric policy.

## What Changed
- Created the project profile and recorded its three-tier forgetting architecture.
- Distinguished continuous retrieval decay from deletion and from separate compaction operations.
- Preserved the source-specific numeric thresholds while marking them as unvalidated defaults.

## Relationships
- [[AgentMemory]] - PowerMem implements persistence, lifecycle management, and selective recall for agents.
- [[MemoryForgetting]] - PowerMem turns time, importance, and access into retrieval salience and promotion decisions.
- [[MemoryCompaction]] - PowerMem pairs decay with deduplication and compression.
- [[AttentionManagement]] - its decay-weighted ranking allocates finite retrieval attention.

---
title: "Zhou Yifan"
type: entity
tags: [author, ai, gpu-programming]
sources:
  - flashattention-1
last_updated: 2026-10-15
knowledge_schema: synthesis-v1
---

## Overview
[[ZhouYifan]] (周弈帆) is the author of a Chinese-language tutorial that derives the core memory-avoidance intuition behind [[FlashAttention]] for readers without CUDA experience.

## Current Profile
In the available source, Zhou teaches GPU programming through a minimal logical model rather than hardware-specific terminology. The article moves from HBM/SRAM traffic and work partitioning through standard attention to a simplified fused streaming loop, while repeatedly marking its pedagogical scope and directing readers toward later Triton implementation work and the original paper for full detail.

## Key Characteristics
- Explains performance algorithms from first principles and incremental pseudocode transformations.
- Targets AI researchers who know Transformer mathematics but not GPU programming.
- Prioritizes memory movement, fusion, and parallel decomposition over CUDA terminology.
- Explicitly distinguishes the tutorial's simplified result from the real FlashAttention algorithm.

## Evidence
- Teaching method: [[flashattention-1]] introduces only the storage and parallel-programming ideas needed for the later derivation.
- Incremental derivation: [[flashattention-1]] rewrites naive attention step by step until sequence-length intermediates disappear.
- Scope discipline: [[flashattention-1]] states that the final program is not the actual FlashAttention algorithm and proposes later Triton coverage.

## Qualifications
The wiki has only this one tutorial as evidence about Zhou's work. It does not establish a broader publication record, implementation expertise, institutional affiliation, or independent evaluation of the teaching method.

## What Changed
- Created the author profile from the FlashAttention tutorial.

## Relationships
- [[FlashAttention]] - tutorial subject and target of the simplified derivation.
- [[OperatorFusion]] - central optimization technique in the tutorial.
- [[GPUMemoryHierarchy]] - conceptual foundation used to explain attention performance.
- [[ParallelProgramming]] - GPU work-partitioning model introduced for non-specialists.

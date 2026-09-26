---
title: "Search-R1"
type: entity
tags: [project, ai, reinforcement-learning, search, rag]
sources:
  - yuan-chao-fa-rag-jin-hua-zhi-lu-chuan-tong-rag-dao-gong-ju-yu-qiang-hua-xue-xi-shuang-lun-qu-dong-de-agentic-rag
last_updated: 2026-09-26
knowledge_schema: synthesis-v1
---

## Overview
[[SearchR1]] is a reinforcement-learning framework for training language models to interleave reasoning, multi-turn search, retrieved information, and final answers.

## Current Profile
The source presents Search-R1 as a learned alternative to hand-written Agentic RAG policies. A policy model emits explicit search or answer actions within a maximum action budget; search results are inserted back into the rollout, malformed actions trigger a rethink instruction, and answer-level correctness supplies the training reward.

## Key Characteristics
- Learns when to search, what query to issue, and how to use returned information.
- Interleaves reasoning and search over multiple turns rather than retrieving once before generation.
- Uses explicit search, information, and answer tags to structure interaction with the retriever.
- Bounds the rollout with an action budget and includes a recovery path for invalid actions.
- Optimizes the policy with outcome-based reward, with GRPO named as the actual algorithm in contrast to the article's simplified policy-gradient example.

## Evidence
- Control loop: [[yuan-chao-fa-rag-jin-hua-zhi-lu-chuan-tong-rag-dao-gong-ju-yu-qiang-hua-xue-xi-shuang-lun-qu-dong-de-agentic-rag]] diagrams reasoning, a search decision, query generation, retrieval, and continued reasoning.
- Rollout protocol: [[yuan-chao-fa-rag-jin-hua-zhi-lu-chuan-tong-rag-dao-gong-ju-yu-qiang-hua-xue-xi-shuang-lun-qu-dong-de-agentic-rag]] reproduces the bounded multi-turn algorithm with search, answer, end-of-sequence, and rethink branches.
- Worked trajectory: [[yuan-chao-fa-rag-jin-hua-zhi-lu-chuan-tong-rag-dao-gong-ju-yu-qiang-hua-xue-xi-shuang-lun-qu-dong-de-agentic-rag]] shows repeated searches and comparisons before a final common-profession answer.
- Optimization: [[yuan-chao-fa-rag-jin-hua-zhi-lu-chuan-tong-rag-dao-gong-ju-yu-qiang-hua-xue-xi-shuang-lun-qu-dong-de-agentic-rag]] describes final-answer reward and names PPO or GRPO as policy-optimization approaches.

## Qualifications
The source is a secondary tutorial summary and simplifies the implementation with policy-gradient pseudocode. It does not provide the original paper's full experimental setup, benchmark results, ablations, retrieval-token masking details, training cost, or failure analysis; claims of greater adaptability therefore remain architectural in this wiki entry.

## What Changed
- Created a source-bounded project profile focused on Search-R1's search-action protocol and learning objective.

## Relationships
- [[ReinforcementLearning]] - Search-R1 applies outcome-based policy optimization to retrieval behavior.
- [[AgenticRAG]] - Search-R1 learns the search decisions that prompt-based agents encode manually.
- [[YuanChaofa]] - Yuan introduces and simplifies the framework in the ingested source.

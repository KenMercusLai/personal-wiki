---
title: "MemGPT"
type: entity
tags: [ai, memory, framework]
sources:
  - yi-kou-qi-ba-suo-you-rang-ni-mu-xuan-de-llm-ming-ci-quan-dou-guo-yi-bian
last_updated: 2026-09-12
knowledge_schema: synthesis-v1
---

## Overview
[[MemGPT]] is presented in the source as a 2023 UC Berkeley system for hierarchical LLM memory management.

## Current Profile
The source uses MemGPT as the clearest precedent for dynamic context compression. It describes the system as separating limited working context from external archival and recall memory, with the LLM using function calls to decide what to evict and what to retrieve. The author compares this design to virtual memory paging in operating systems.

## Key Characteristics
- Provides a concrete example of active memory and context management.
- Separates limited main context from external memory stores.
- Uses archival memory and recall memory as secondary storage layers.
- Lets the LLM decide through function calls what to evict or retrieve.
- Is described as the predecessor line that later evolved into [[Letta]].

## Evidence
- Architecture: [[yi-kou-qi-ba-suo-you-rang-ni-mu-xuan-de-llm-ming-ci-quan-dou-guo-yi-bian]] describes MemGPT's working context, archival memory, recall memory, and function-call-mediated memory operations.
- Analogy: [[yi-kou-qi-ba-suo-you-rang-ni-mu-xuan-de-llm-ming-ci-quan-dou-guo-yi-bian]] compares MemGPT's design to operating-system virtual memory paging.
- Evolution: [[yi-kou-qi-ba-suo-you-rang-ni-mu-xuan-de-llm-ming-ci-quan-dou-guo-yi-bian]] says MemGPT later evolved into the open-source framework Letta.

## Qualifications
The source summarizes MemGPT from a practitioner perspective and does not evaluate its implementation, paper results, current project status, or production reliability.

## What Changed
- Created an entity profile for MemGPT as a reference architecture for hierarchical agent memory.

## Relationships
- [[DynamicContextCompression]] - MemGPT is used as evidence for active context and memory management.
- [[AgentMemory]] - MemGPT implements memory as external storage plus retrieval.
- [[Letta]] - Letta is described as the later framework in the same lineage.
- [[RetrievalAugmentedGeneration]] - MemGPT retrieves stored information back into model context.

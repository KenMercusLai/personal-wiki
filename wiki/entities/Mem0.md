---
title: "Mem0"
type: entity
tags: [ai, agents, memory, research]
sources:
  - custom-llm-memory-layer
  - wei-shen-me-wo-kan-hao-turbopuffer-cong-personal-agent-shuo-qi
last_updated: 2026-10-27
knowledge_schema: synthesis-v1
---

## Overview
[[Mem0]] is an agent-memory architecture and product represented through a tutorial adapting its maintenance phases and a practitioner account of its reported production retrieval migration.

## Current Profile
The depicted architecture processes messages and historical context into candidate memories, retrieves similar stored memories, and uses tool-mediated add, update, delete, or no-op decisions before writing revised state. A central database supplies summaries, past messages, similar-memory retrieval, and persistence across the phases.

At reported production scale, the architecture splits authoritative records from its search index. Original memories remain in [[PostgreSQL]], while text, embeddings, metadata, and IDs pointing back to those records are indexed in [[Turbopuffer]]. Retrieval narrows candidates in a customer-scoped namespace before complete content is fetched from PostgreSQL. This makes Turbopuffer a search building block rather than the authority for the full memory record and avoids performing every vector query against one global HNSW table filtered simultaneously by organization, project, user, agent, and session.

## Key Characteristics
- Separates candidate-memory extraction from state maintenance.
- Compares new candidates with similar existing memories before mutation.
- Exposes add, update, delete, and no-op as distinct maintenance outcomes.
- Uses a database as persistent context and updated-memory storage.
- Separates reported production search-index records from PostgreSQL-held original memories.
- Uses customer-scoped search namespaces to reduce global vector-filtering conflict.

## Evidence
- Architecture: [[custom-llm-memory-layer]] reproduces a Mem0 paper diagram with extraction and update boundaries, database flows, and four maintenance actions.
- Adaptation: [[custom-llm-memory-layer]] implements a simplified Mem0-inspired lifecycle with DSPy ReAct tools and vector retrieval.
- Production storage split: [[wei-shen-me-wo-kan-hao-turbopuffer-cong-personal-agent-shuo-qi]] relays that Mem0 keeps original memories in PostgreSQL and indexed text, vectors, metadata, and source IDs in Turbopuffer.
- Tenant-scoped retrieval: [[wei-shen-me-wo-kan-hao-turbopuffer-cong-personal-agent-shuo-qi]] describes the migration from one globally filtered HNSW table to customer namespaces.

## Qualifications
This page is grounded in a secondary tutorial and a practitioner retelling of a vendor customer case rather than a complete reading of the Mem0 paper, current product documentation, or migration data. The tutorial simplifies the architecture, provides no direct Mem0 evaluation, and contains code inconsistencies that should not be attributed automatically to the original system. The migration account provides no corpus size, recall target, latency distribution, cost comparison, synchronization failure rate, authorization test, or independent benchmark; a customer namespace also need not equal every user or permission scope inside the product.

## What Changed
- Established Mem0 as the source architecture for the tutorial's extraction-and-maintenance design.
- Added the reported PostgreSQL source-of-truth and Turbopuffer index split.
- Added customer-scoped namespaces as a response to multi-dimensional vector filtering.

## Relationships
- [[AgentMemory]] - is the broader capability Mem0 organizes into extraction, retrieval, and update phases.
- [[MemoryConflictResolution]] - motivates update and delete decisions when candidate facts differ from stored state.
- [[VectorDatabase]] - can supply similar-memory retrieval in a simplified implementation.
- [[DSPy]] - is used by the tutorial to reproduce a Mem0-inspired agent loop.
- [[Turbopuffer]] - supplies the reported customer-scoped retrieval index.
- [[PostgreSQL]] - retains the reported original memory records fetched after candidate search.
- [[PersonalAgentRetrieval]] - frames the multi-tenant search workload beneath memory semantics.

---
title: "Kapa AI"
type: entity
tags: [ai, rag, developer-tools]
sources:
  - kapa-prune-rag
last_updated: 2026-10-17
knowledge_schema: synthesis-v1
---

## Overview
[[KapaAI]] is presented as a company building AI assistants and retrieval infrastructure over technical documentation, API references, PDFs, forums, and support material.

## Current Profile
The available first-party account describes Kapa's retrieval stack as embedding and keyword search over large product knowledge bases, reranking to roughly 15 chunks, optional listwise pruning, and generation. Kapa reports deploying pruning by default in its Product Agent SDK knowledge-base search and as an option in its retrieval API and MCP servers.

## Key Characteristics
- Provides retrieval and end-to-end assistant infrastructure for product knowledge bases.
- Uses hybrid candidate search, reranking, and a small-LLM listwise pruning stage before generation.
- Evaluates pruning through labeled necessary chunks and replayed production conversations.
- Prioritizes agent integrations where repeated search can recover missing evidence and smaller tool outputs preserve context capacity.

## Evidence
- Product scope: [[kapa-prune-rag]] describes assistants and a retrieval API spanning documentation, API references, PDFs, forums, and support threads.
- Retrieval pipeline: [[kapa-prune-rag]] illustrates a roughly 200,000-to-200-to-15-to-five chunk funnel before generation.
- Evaluation and rollout: [[kapa-prune-rag]] reports labeled recall evaluation, production replay, a selected 68% compression point, and SDK/API/MCP availability.

## Qualifications
All current evidence comes from one Kapa-authored article. It does not expose the evaluation sample size, underlying conversations, selected model and threshold, confidence intervals, end-answer quality, customer distribution, or independent replication.

## What Changed
- Established Kapa's source-bounded profile as a product-knowledge retrieval and assistant provider.
- Added its reported listwise-pruning architecture and deployment boundary.

## Relationships
- [[LarsBaltensperger]] - authors the available account of Kapa's pruning system.
- [[RAGContextPruning]] - Kapa implements the concept as a small-model stage before generation.
- [[RetrievalAugmentedGeneration]] - Kapa's product architecture retrieves and reranks product knowledge for grounded answers.
- [[AgenticRAG]] - Kapa first enables pruning where retrieval is one repeatable tool among many.

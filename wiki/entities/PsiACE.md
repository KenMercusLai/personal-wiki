---
title: "PsiACE"
type: entity
tags: [ai, agents, rag, open-source]
sources:
  - mu-jiang-chui-zi-ding-zi
  - tape-x-topic-wo-dui-zhi-neng-ti-shang-xia-wen-de-zu-zhi-fang-shi
last_updated: 2026-09-24
knowledge_schema: synthesis-v1
---

## Overview
[[PsiACE]] is an author and agent-system practitioner, also writing as 泉达, represented through work across databases, RAG, agents, sandboxes, protocols, open source, and context architecture.

## Current Profile
Within this wiki, PsiACE adds a practitioner view of agent design that sits between coding-agent implementation, infrastructure reuse, and product framing. The earlier source says he worked on databases, RAG, agents, protocols, sandboxes, and open source, and uses [[Bub]] to compare coding and group-chat agents. The newer article develops Tape's entries, anchors, views, and handoff into [[AgentTopicLifecycle]] for enterprise knowledge-base support, including recall, unfinished-topic recovery, sharing, fact extraction, and cost accounting.

## Key Characteristics
- Works across databases, RAG, agents, protocols, sandboxes, and open source.
- Uses [[Bub]] as the source's main project example.
- Treats coding agents as model plus tools plus loop.
- Critiques naive RAG for live codebase use and favors agent-loop retrieval where appropriate.
- Reframes long-running context as append-only history plus minimal anchors instead of mandatory continuity.
- Extends Tape with business-level topic boundaries and lifecycle hooks for enterprise knowledge work.

## Evidence
- Background: [[mu-jiang-chui-zi-ding-zi]] says PsiACE has worked on databases, RAG, agents, sandboxes, protocols, and open source.
- Project frame: [[mu-jiang-chui-zi-ding-zi]] says renewed work on Bub motivates the article's agent reflections.
- Agent definition: [[mu-jiang-chui-zi-ding-zi]] defines agents as model plus tools plus loop.
- Retrieval critique: [[mu-jiang-chui-zi-ding-zi]] argues that static RAG can be costly and semantically weak for changing codebases.
- Context model: [[mu-jiang-chui-zi-ding-zi]] proposes tape and anchors as a different context-management model.
- Tape specification: [[tape-x-topic-wo-dui-zhi-neng-ti-shang-xia-wen-de-zu-zhi-fang-shi]] explains immutable entries, anchors, views, handoff, and storage portability.
- Topic extension: [[tape-x-topic-wo-dui-zhi-neng-ti-shang-xia-wen-de-zu-zhi-fang-shi]] proposes topic boundary anchors, lifecycle hooks, recall, recovery, and token accounting for a codebase-support agent.

## Qualifications
The page is based on two reflective design articles rather than a full profile of PsiACE's public work. It preserves the sources' self-description and proposals without independently verifying project metrics, employment history, implementation maturity, or the reliability of the proposed lifecycle hooks.

## What Changed
- Created the initial entity page for PsiACE.
- Added PsiACE's Tape specification and Topic proposal for enterprise knowledge-base agents.

## Relationships
- [[Bub]] - PsiACE uses Bub as the article's central project and design example.
- [[CodingAgentMinimalTooling]] - PsiACE explains why a small tool surface can be enough for coding agents.
- [[AgenticRAG]] - PsiACE favors grep/read/agent-loop retrieval for live codebases.
- [[TapeAndAnchors]] - PsiACE proposes this model for context reconstruction.
- [[LLMContextManagement]] - PsiACE's article contributes a new context-management frame.
- [[AgentTopicLifecycle]] - PsiACE proposes topic boundaries and hooks as a business-facing layer over Tape.
- [[AgentMemory]] - PsiACE argues that durable entries and anchors can make temporal recall native.

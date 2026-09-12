---
title: "PsiACE"
type: entity
tags: [ai, agents, rag, open-source]
sources:
  - mu-jiang-chui-zi-ding-zi
last_updated: 2026-09-12
knowledge_schema: synthesis-v1
---

## Overview
[[PsiACE]] is the author of the source, also writing as 泉达, and is presented as a practitioner with experience across databases, RAG, agents, sandboxes, protocols, and open-source ecosystem work.

## Current Profile
Within this wiki, PsiACE adds a practitioner view of agent design that sits between coding-agent implementation and product framing. The source says he previously worked on databases, RAG, agents, and open source, and currently works on open-source ecosystem work at OceanBase. His argument is less a deep technical specification than a reflective model of how agent tools, retrieval, memory, context, and group-chat coexistence should be understood.

## Key Characteristics
- Works across databases, RAG, agents, protocols, sandboxes, and open source.
- Uses [[Bub]] as the source's main project example.
- Treats coding agents as model plus tools plus loop.
- Critiques naive RAG for live codebase use and favors agent-loop retrieval where appropriate.
- Reframes long-running context as append-only history plus minimal anchors instead of mandatory continuity.

## Evidence
- Background: [[mu-jiang-chui-zi-ding-zi]] says PsiACE has worked on databases, RAG, agents, sandboxes, protocols, and open source.
- Project frame: [[mu-jiang-chui-zi-ding-zi]] says renewed work on Bub motivates the article's agent reflections.
- Agent definition: [[mu-jiang-chui-zi-ding-zi]] defines agents as model plus tools plus loop.
- Retrieval critique: [[mu-jiang-chui-zi-ding-zi]] argues that static RAG can be costly and semantically weak for changing codebases.
- Context model: [[mu-jiang-chui-zi-ding-zi]] proposes tape and anchors as a different context-management model.

## Qualifications
The page is based on one reflective article rather than a full profile of PsiACE's public work. It preserves the source's self-description without independently verifying project metrics or employment history.

## What Changed
- Created the initial entity page for PsiACE.

## Relationships
- [[Bub]] - PsiACE uses Bub as the article's central project and design example.
- [[CodingAgentMinimalTooling]] - PsiACE explains why a small tool surface can be enough for coding agents.
- [[AgenticRAG]] - PsiACE favors grep/read/agent-loop retrieval for live codebases.
- [[TapeAndAnchors]] - PsiACE proposes this model for context reconstruction.
- [[LLMContextManagement]] - PsiACE's article contributes a new context-management frame.

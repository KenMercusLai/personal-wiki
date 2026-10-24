---
title: "PsiACE"
type: entity
tags: [ai, agents, rag, open-source]
sources:
  - mu-jiang-chui-zi-ding-zi
  - tape-x-topic-wo-dui-zhi-neng-ti-shang-xia-wen-de-zu-zhi-fang-shi
  - chuang-zao-yi-zhi-long-xia-xu-yao-xie-shi-me-frosts-blog
  - tapexbee
  - deepchat-tape
last_updated: 2026-10-25
knowledge_schema: synthesis-v1
---

## Overview
[[PsiACE]] is an author and agent-system practitioner, also writing as 泉达, represented through work across databases, RAG, agents, sandboxes, protocols, open source, and context architecture.

## Current Profile
Within this wiki, PsiACE adds a practitioner view of agent design that sits between coding-agent implementation, infrastructure reuse, and product framing. The earlier source says he worked on databases, RAG, agents, protocols, sandboxes, and open source, and uses [[Bub]] to compare coding and group-chat agents. His Tape work separates immutable history from reconstructed views, then develops entries, anchors, views, and handoff into [[AgentTopicLifecycle]] for enterprise knowledge-base support. The Bee article specializes Topic for Job and Cron work, joining human-maintained Skills, BDD criteria, DAG checkpoints, human review, and Kubernetes or Argo execution in [[AgentTaskOrchestration]]. A DeepChat implementation account credits this design as the basis for a production migration that added view manifests, compaction fallback, execution evidence, and inspection. Frost Ming's account independently adds PsiACE as the original Bub builder and collaborator in an experiment that moved Telegram behavior from framework code into agent-managed Skills and startup artifacts.

## Key Characteristics
- Works across databases, RAG, agents, protocols, sandboxes, and open source.
- Uses [[Bub]] as the source's main project example.
- Treats coding agents as model plus tools plus loop.
- Critiques naive RAG for live codebase use and favors agent-loop retrieval where appropriate.
- Reframes long-running context as append-only facts plus reconstructed views and minimal anchors instead of mandatory continuity.
- Extends Tape first with business-level topic boundaries, then with Bee orchestration for bounded Job and Cron work.
- Collaborated on using Bub as a minimal, self-bootstrapping Telegram-agent runtime.

## Evidence
- Background: [[mu-jiang-chui-zi-ding-zi]] says PsiACE has worked on databases, RAG, agents, sandboxes, protocols, and open source.
- Project frame: [[mu-jiang-chui-zi-ding-zi]] says renewed work on Bub motivates the article's agent reflections.
- Agent definition: [[mu-jiang-chui-zi-ding-zi]] defines agents as model plus tools plus loop.
- Retrieval critique: [[mu-jiang-chui-zi-ding-zi]] argues that static RAG can be costly and semantically weak for changing codebases.
- Context model: [[mu-jiang-chui-zi-ding-zi]] proposes tape and anchors as a different context-management model.
- Tape specification: [[tape-x-topic-wo-dui-zhi-neng-ti-shang-xia-wen-de-zu-zhi-fang-shi]] explains immutable entries, anchors, views, handoff, and storage portability.
- Topic extension: [[tape-x-topic-wo-dui-zhi-neng-ti-shang-xia-wen-de-zu-zhi-fang-shi]] proposes topic boundary anchors, lifecycle hooks, recall, recovery, and token accounting for a codebase-support agent.
- Task orchestration: [[tapexbee]] describes Bee templates, DAG state, review gates, DAG anchors, and reuse of Kubernetes or Argo for execution.
- Collaboration: [[chuang-zao-yi-zhi-long-xia-xu-yao-xie-shi-me-frosts-blog]] credits PsiACE's Bub as the substrate for Frost Ming's OpenClaw reproduction and AI-native architecture experiment.
- Product influence: [[deepchat-tape]] credits PsiACE's punch-tape model and later Tape framework as the basis for DeepChat's append-only history, reconstructed model views, and searchable anchors.
- Design stance: [[deepchat-tape]] attributes to PsiACE the principle that reliable interaction matters more than increasingly clever memory and traces the idea through Bub and later Tape essays.

## Qualifications
The page is based on reflective practitioner articles and one adopter's first-party implementation narrative rather than a full profile of PsiACE's public work. It preserves the sources' self-description, proposals, and attribution without independently verifying project metrics, employment history, implementation maturity, the reliability of lifecycle hooks and DAG recovery, or Bub's self-bootstrapping behavior. DeepChat demonstrates concrete adoption but does not isolate Tape's effects through comparative evaluation. The Bee article's OpenClaw and Hermes comparison is explicitly AI-summarized rather than based on the author's code review.

## What Changed
- Added DeepChat's concrete adoption of PsiACE's immutable-history and reconstructed-view model.
- Distinguished the original design language from DeepChat's later compaction, execution-journal, and inspection mechanisms.
- Preserved the first-party, unbenchmarked implementation boundary.

## Relationships
- [[Bub]] - PsiACE uses Bub as the article's central project and design example.
- [[CodingAgentMinimalTooling]] - PsiACE explains why a small tool surface can be enough for coding agents.
- [[AgenticRAG]] - PsiACE favors grep/read/agent-loop retrieval for live codebases.
- [[TapeAndAnchors]] - PsiACE proposes this model for context reconstruction.
- [[LLMContextManagement]] - PsiACE's article contributes a new context-management frame.
- [[AgentTopicLifecycle]] - PsiACE proposes topic boundaries and hooks as a business-facing layer over Tape.
- [[AgentTaskOrchestration]] - PsiACE's Bee proposal applies Topic and Tape to reviewable DAG work.
- [[AgentMemory]] - PsiACE argues that durable entries and anchors can make temporal recall native.
- [[FrostMing]] - collaborator who applied the Bub project to a minimal OpenClaw-like deployment.
- [[AINativeAgentArchitecture]] - architecture experiment conducted on top of Bub.

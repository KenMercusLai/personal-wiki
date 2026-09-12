---
title: "Agent Memory"
type: concept
tags: [ai, llm, memory, retrieval]
sources:
  - yi-kou-qi-ba-suo-you-rang-ni-mu-xuan-de-llm-ming-ci-quan-dou-guo-yi-bian
  - mu-jiang-chui-zi-ding-zi
  - yong-claude-code-jiang-san-wan-hang-go-xiang-mu-yi-zhi-dao-rust-agent-team-shi-jian-yu-harness-xiao-lu-you-hua
last_updated: 2026-09-12
knowledge_schema: synthesis-v1
---

## Definition
[[AgentMemory]] is an LLM-agent pattern where information can be written to external storage and later retrieved into context when useful.

## Current Synthesis
The source places Memory in the same family as RAG. RAG retrieves relevant outside information from a larger corpus, while Memory adds an agent-controlled write path: the model decides what to store, when to store it, and when to retrieve it. This makes memory less like a special faculty and more like a writeable retrieval interface that helps keep long histories out of the active prompt.

PsiACE's essay adds a qualification: memory is often asked to solve a continuity problem created by assuming state must survive across sessions. In multi-person and multi-topic settings, memory can drift and require high calibration effort. [[TapeAndAnchors]] offers a narrower alternative in which durable history remains available, but only minimal anchors are carried forward by default.

The mihomo-rust case study narrows memory even further for coding work. Its Claude Code memories are feedback rules about agent behavior, such as avoiding `CatchPanic`, remembering limits of `tokio::time::pause()`, and respawning teammates at milestone boundaries. The source warns against storing code conventions, git history, fixed debugging plans, or temporary task state in memory when files or tools are more authoritative.

## Key Claims
- Memory addresses context limits by storing information outside the immediate prompt.
- Agent memory is RAG-like because saved information must be retrieved back into context to affect generation.
- The distinguishing feature is write access: the LLM can decide what to save.
- Memory depends on model judgment about storage and retrieval timing.
- Memory can compose with Skills, tools, and external knowledge systems rather than replacing them.
- Memory can drift when treated as a persistent personality or state-continuity layer.
- Minimal anchors and compact feedback memories can preserve task-stage continuity without asking memory to inherit everything or repeat prior agent mistakes.

## Evidence
- RAG relationship: [[yi-kou-qi-ba-suo-you-rang-ni-mu-xuan-de-llm-ming-ci-quan-dou-guo-yi-bian]] says Memory is the same class of problem as RAG.
- Write path: [[yi-kou-qi-ba-suo-you-rang-ni-mu-xuan-de-llm-ming-ci-quan-dou-guo-yi-bian]] characterizes Memory as RAG with write capability.
- Composition example: [[yi-kou-qi-ba-suo-you-rang-ni-mu-xuan-de-llm-ming-ci-quan-dou-guo-yi-bian]] combines a Skill, Python tool, and NotebookLM-like external knowledge interface in one workflow.
- Continuity critique: [[mu-jiang-chui-zi-ding-zi]] says memory systems try to preserve personality or state across sessions, but drift and calibration costs can exceed expectations.
- Anchor alternative: [[mu-jiang-chui-zi-ding-zi]] proposes anchors as minimal state packets while history remains available on an append-only tape.
- Feedback memory: [[yong-claude-code-jiang-san-wan-hang-go-xiang-mu-yi-zhi-dao-rust-agent-team-shi-jian-yu-harness-xiao-lu-you-hua]] describes seven `feedback` memories used to prevent repeated agent mistakes and preserve milestone-reset procedure.

## Counterevidence & Qualifications
The sources do not fully discuss memory privacy, deletion, retrieval ranking, staleness, user control, or how to evaluate whether the model saved the right facts. PsiACE's critique is strongest for session-spanning identity and group-chat continuity; it does not prove that narrower, user-controlled memory is ineffective.

## What Changed
- Created the concept page for agent memory as writeable retrieval rather than an independent category.
- Added the critique that memory drift and calibration costs make full continuity a risky default.
- Added a narrow coding-agent feedback-memory pattern and a warning against storing facts better represented in code, git, or task files.

## Related Concepts
- [[RetrievalAugmentedGeneration]] - agent memory is framed as RAG plus write capability.
- [[LLMContextManagement]] - memory keeps persistent facts out of the prompt until needed.
- [[DynamicContextCompression]] - dynamic compression can evict information into external memory.
- [[SecondBrain]] - personal knowledge systems can become memory-like external stores for agents.
- [[TapeAndAnchors]] - anchors are a lighter continuity mechanism than broad memory inheritance.
- [[AgentTeam]] - feedback memory supports role respawn across milestone boundaries.

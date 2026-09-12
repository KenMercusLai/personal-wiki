---
title: "Agent Memory"
type: concept
tags: [ai, llm, memory, retrieval]
sources:
  - yi-kou-qi-ba-suo-you-rang-ni-mu-xuan-de-llm-ming-ci-quan-dou-guo-yi-bian
last_updated: 2026-09-12
knowledge_schema: synthesis-v1
---

## Definition
[[AgentMemory]] is an LLM-agent pattern where information can be written to external storage and later retrieved into context when useful.

## Current Synthesis
The source places Memory in the same family as RAG. RAG retrieves relevant outside information from a larger corpus, while Memory adds an agent-controlled write path: the model decides what to store, when to store it, and when to retrieve it. This makes memory less like a special faculty and more like a writeable retrieval interface that helps keep long histories out of the active prompt.

## Key Claims
- Memory addresses context limits by storing information outside the immediate prompt.
- Agent memory is RAG-like because saved information must be retrieved back into context to affect generation.
- The distinguishing feature is write access: the LLM can decide what to save.
- Memory depends on model judgment about storage and retrieval timing.
- Memory can compose with Skills, tools, and external knowledge systems rather than replacing them.

## Evidence
- RAG relationship: [[yi-kou-qi-ba-suo-you-rang-ni-mu-xuan-de-llm-ming-ci-quan-dou-guo-yi-bian]] says Memory is the same class of problem as RAG.
- Write path: [[yi-kou-qi-ba-suo-you-rang-ni-mu-xuan-de-llm-ming-ci-quan-dou-guo-yi-bian]] characterizes Memory as RAG with write capability.
- Composition example: [[yi-kou-qi-ba-suo-you-rang-ni-mu-xuan-de-llm-ming-ci-quan-dou-guo-yi-bian]] combines a Skill, Python tool, and NotebookLM-like external knowledge interface in one workflow.

## Counterevidence & Qualifications
The source does not discuss memory privacy, deletion, retrieval ranking, staleness, user control, or how to evaluate whether the model saved the right facts. Its framing is architectural rather than product-specific.

## What Changed
- Created the concept page for agent memory as writeable retrieval rather than an independent category.

## Related Concepts
- [[RetrievalAugmentedGeneration]] - agent memory is framed as RAG plus write capability.
- [[LLMContextManagement]] - memory keeps persistent facts out of the prompt until needed.
- [[DynamicContextCompression]] - dynamic compression can evict information into external memory.
- [[SecondBrain]] - personal knowledge systems can become memory-like external stores for agents.

---
title: "木匠,锤子,钉子"
type: source
tags: [ai, agents, coding-agent, rag, context-management]
date: 2026-02-27
source_file: /mnt/ken_personal_wiki/Articles/木匠，锤子，钉子.md
---

## Summary
[[PsiACE]] reflects on several years of work around RAG, sandboxes, protocols, and agents, using the renewed development of [[Bub]] to compare coding-agent tool design, RAG's limits, personal-assistant agents, group-chat agents, and context-management models. The article argues that a coding agent can be understood as model plus tools plus loop, that `bash`, read, write, and edit form a surprisingly capable minimal tool surface, and that live codebase retrieval often works better through grep-style exploration inside an agent loop than through static naive RAG. Its central context claim is that agent systems should treat history as an append-only material store assembled on demand, rather than assuming every session state and memory must be continuously inherited.

## Key Claims
- [[CodingAgentMinimalTooling]] can be built from a small tool set: read/write for input and output, edit for precise intervention, and bash as a bridge to existing command-line and programmable tools.
- [[RetrievalAugmentedGeneration]] is not automatically effective for coding agents because frequently changing codebases create indexing freshness costs, and common embeddings can fail to bridge natural language and code semantics.
- [[AgenticRAG]] can replace static indexing in coding contexts by letting an agent search, read, and refine retrieval through an interactive loop.
- [[OpenClaw]] and [[Bub]] represent different agent product frames: OpenClaw is described as a personal assistant entering everyday life, while Bub is designed for multi-person or multi-agent group-chat coexistence.
- Group-chat agents need identity awareness and effective communication because they face incomplete context, fuzzy intent, parallel topics, and situations where not every message requires a reply.
- [[TapeAndAnchors]] reframes [[LLMContextManagement]] by treating history as an append-only tape, anchors as minimal stage state, and context assembly as exploration plus selection rather than automatic state inheritance.
- The hammer metaphor warns that tools shape problem perception, but mature tool use means knowing when not to use the hammer, recognizing real nails, and switching tools when needed.

## Key Quotes
> "Agent 大致可以看作模型 + 工具 + 循环调用。" - The article's compact definition of an agent.

> "grep + 读 + Agent Loop,成为了一个更巧妙、更符合直觉、也更有效的方案" - On why agentic retrieval can fit live code better than static codebase RAG.

> "历史不是必须继承的负担,而是可以按需读取的素材库。" - The key shift behind the tape-and-anchor context model.

## Connections
- [[PsiACE]] - author and practitioner reflecting from work on databases, RAG, agents, protocols, and open source.
- [[Bub]] - the article's renewed project and main example of a group-chat-oriented coding agent.
- [[OpenClaw]] - used as the contrasting personal-assistant agent paradigm.
- [[CodingAgentMinimalTooling]] - explains the four-tool coding-agent surface.
- [[RetrievalAugmentedGeneration]] - qualified by the article's critique of naive RAG for changing codebases.
- [[AgenticRAG]] - names the grep/read/agent-loop retrieval pattern for code.
- [[AgentMemory]] - treated as part of the broader attempt to extend agent continuity across sessions.
- [[DynamicContextCompression]] - placed among compact, summary, fork, merge, and handoff tactics for finite-context continuity.
- [[LLMContextManagement]] - the article's largest conceptual target.
- [[TapeAndAnchors]] - the article's alternative model for persistent history and minimal context reconstruction.
- [[ModelContextProtocol]] - part of the author's broader agent/protocol work and the wiki's existing tool-interface thread.

## Contradictions
- No direct contradictions with existing wiki pages were found. The source qualifies earlier RAG and memory material by arguing that codebase freshness, semantic mismatch, and multi-topic group contexts can make inherited state or static retrieval less appropriate than on-demand context assembly.

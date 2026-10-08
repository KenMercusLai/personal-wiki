---
title: "为 AI Agent 构建记忆系统"
type: source
tags: [ai, agents, memory, knowledge-graph, retrieval]
date: 2026-03-21
source_file: /mnt/ken_personal_wiki/Articles/为 AI Agent 构建记忆系统.md
---

## Summary
This first-party engineering account presents [[NowledgeMem]] as a cross-tool personal memory layer and decomposes mature [[AgentMemory]] into distillation, retrieval, temporal representation, evolution, and forgetting. Its architecture preserves raw traces, extracts typed Units, promotes claims corroborated by at least three sources into Crystals, combines hybrid retrieval with progressive disclosure, and keeps user visibility and adjudication in the loop.

![Human sensory, working, episodic, semantic, procedural, consolidation, and forgetting constraints mapped to memory-system components](../../wiki-assets/wei-ai-agent-gou-jian-ji-yi-xi-tong/cognitive-memory-architecture.webp)

The cognitive map pairs sensory input with raw capture, limited working memory with a daily Markdown focus file, episodic memory with threads, semantic memory with eight Unit types, procedural memory with skills, sleep consolidation with background jobs, and forgetting with an explicit decay model.

## Key Claims
- [[AgentMemory]] should be treated as a decision system rather than a database: it must decide what to retain, how to represent it, what to retrieve, how knowledge changes, and what should fade.
- A daily working-memory file can act as attention prefetch by selecting a small set of currently relevant items from more than 10,000 memories using community, decay, and recent-activity signals.

![Nowledge Mem timeline showing a daily focus briefing selected from related memories, insights, and graph context](../../wiki-assets/wei-ai-agent-gou-jian-ji-yi-xi-tong/working-memory-dashboard.webp)

- Distillation moves from high-fidelity Trace to atomic typed Unit to corroborated Crystal; a roughly 50-token triage gate sends only about 10% of conversations into full extraction, while manual user intent receives a more permissive threshold.

![Conversation distillation pipeline with a low-cost triage gate, structured LLM extraction, memory storage, evolution detection, entity extraction, labeling, and crystals](../../wiki-assets/wei-ai-agent-gou-jian-ji-yi-xi-tong/memory-distillation-pipeline.webp)

- Retrieval uses a fast parallel path for most queries and an intent-routed deep path for harder ones, retaining `source_thread_id` pointers so an agent can expand into original evidence only when needed.

![Two-level memory retrieval pipeline combining fast multi-source fusion with intent-routed deep search, reranking, and on-demand thread expansion](../../wiki-assets/wei-ai-agent-gou-jian-ji-yi-xi-tong/hybrid-search-pipeline.webp)

- [[BitemporalMemory]] separates event time from record time, stores precision, declines to invent low-confidence dates, and lets semantic relevance dominate time boosts in ranking.

![Nowledge Mem timeline beside knowledge counts, an activity calendar, and an item requiring attention](../../wiki-assets/wei-ai-agent-gou-jian-ji-yi-xi-tong/temporal-timeline-dashboard.webp)

- [[MemoryEvolution]] distinguishes progression (`replaces`, `enriches`) from validation (`confirms`, `challenges`); detected conflicts are surfaced for user decision rather than silently resolved.

![Nowledge Mem evolution review showing confirms and enriches events, confidence, linked memory IDs, and a user-controlled conflict decision](../../wiki-assets/wei-ai-agent-gou-jian-ji-yi-xi-tong/memory-evolution-review.webp)

- [[MemoryForgetting]] separates time-decaying attention from non-decreasing accumulated confidence, protects important memories with a floor, and archives only when low decay, zero interaction, age over 90 days, and active state all hold.

![Nowledge Mem health panel reporting refreshed decay scores, confidence, and high, medium, low, and stale memory counts](../../wiki-assets/wei-ai-agent-gou-jian-ji-yi-xi-tong/memory-health-dashboard.webp)

- The graph supports progressive traversal through Trace, Unit, Entity, Evolution, Community, Crystal, and Quality layers rather than loading the whole knowledge base at once.

![Seven-layer progressive knowledge graph from raw traces through units, entities, evolution, communities, crystals, and quality](../../wiki-assets/wei-ai-agent-gou-jian-ji-yi-xi-tong/progressive-knowledge-graph.jpeg)

- Background intelligence combines scheduled consolidation and event-driven cascades under debounce, rate, token-budget, context-size, and code-level quality gates.

![Nowledge Mem graph explorer with community clusters, node relationships, importance inspection, and graph algorithms](../../wiki-assets/wei-ai-agent-gou-jian-ji-yi-xi-tong/graph-community-explorer.webp)

- Cross-tool continuity depends on capture and recall lifecycle hooks, open local formats, export, and user-visible control rather than a bare MCP call.

![Personal knowledge graph connecting coding, chat, browser, mobile, CLI, notebook, and Markdown tools through capture and recall lifecycle hooks](../../wiki-assets/wei-ai-agent-gou-jian-ji-yi-xi-tong/cross-tool-memory-layer.webp)

## Key Quotes
> “没有遗忘的记忆系统是垃圾场。” — on why retention needs active decay and archival policy.

> “记忆系统的核心不是数据库，是一条决策链。” — on intelligence rather than storage as the main bottleneck.

> “看不到就不信任，不信任就不用，不用和没有一样。” — on visibility and user control as adoption requirements.

## Connections
- [[NowledgeMem]] - product and engineering system described by the source.
- [[AgentMemory]] - central architecture whose lifecycle the article decomposes.
- [[MemoryCompaction]] - consolidation and Crystal formation reduce repetitive raw state.
- [[MemoryEvolution]] - explicit progression and validation relationships represent changing knowledge.
- [[MemoryConflictResolution]] - conflicting memories remain visible for human adjudication.
- [[MemoryForgetting]] - decay, confidence, importance floors, and conservative archival manage attention.
- [[BitemporalMemory]] - event time and record time answer different temporal questions.
- [[AgenticRAG]] - intent-routed, multi-source retrieval and progressive expansion place search inside an agent decision loop.
- [[LLMContextManagement]] - working-memory prefetch and bounded context injection govern what reaches the model.
- [[LLMToolingSkills]] - the proposed end state turns corroborated experience into executable skills.

## Contradictions
- The source argues that a cross-tool memory product is a necessary aggregation layer, while [[TapeAndAnchors]] proposes that durable history, bounded summaries, and recall anchors can make memory native to context organization rather than a separate service. These positions can coexist, but the product boundary is unresolved.
- The confidence rule `max(new_value, old_value)` prevents accumulated support from declining; this is a product policy, not proof that evidence quality or belief confidence can never weaken. A challenged, stale, or discredited source may require recalibration even when attention decay remains separate.
- The reported token reductions, latencies, query shares, weights, thresholds, source counts, task limits, integration counts, and user behavior are first-party engineering choices or anecdotes without comparative benchmarks, calibration studies, cost data, or independent validation.

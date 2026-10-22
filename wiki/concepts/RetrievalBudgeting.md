---
title: "Retrieval Budgeting"
type: concept
tags: [agents, retrieval, systems, latency]
sources:
  - psql-bm25s
last_updated: 2026-10-22
knowledge_schema: synthesis-v1
---

## Definition
[[RetrievalBudgeting]] is the way query latency, compute cost, and tool limits influence when an agent harness searches accumulated state, how broadly it searches, and whether retrieval is a default action or a fallback.

## Current Synthesis
The source argues that retrieval cost is not merely an infrastructure metric because the harness adapts its behavior around that cost. Slow lookup encourages fewer calls, narrower memory slices, overloaded queries, and later grounding; cheap lookup makes several focused queries and repeated state checks practical.

This is a systems hypothesis rather than proof that more retrieval always improves agents. Search frequency still interacts with recall, ranking quality, freshness, context capacity, evidence interpretation, and memory policy. A fast lexical primitive changes the feasible control policy but does not choose the right policy by itself.

## Key Claims
- Retrieval latency and tool budgets shape the harness's evidence-seeking behavior.
- High query cost can turn retrieval from a default grounding step into a rationed fallback.
- Low query cost permits multiple focused searches and repeated checks against accumulated state.
- Retrieval frequency is distinct from retrieval quality, evidence usefulness, and safe context use.

## Evidence
Cost-to-policy mechanism:
- [[psql-bm25s]] argues that slow search narrows the searched memory surface and caps query frequency, while cheap search enables repeated grounding.

Concrete implementation motivation:
- [[psql-bm25s]] presents [[PsqlBm25s]] as a PostgreSQL-native primitive intended to reduce that query cost over application and agent state.

Control-layer boundary:
- [[psql-bm25s]] explicitly separates the retrieval primitive from the runtime, reranker, and memory-policy engine that decide what to store, retrieve, summarize, or forget.

## Counterevidence & Qualifications
The source does not measure agent task success as retrieval latency changes, compare alternative harness policies, or quantify the point at which search becomes cheap enough to use by default. More frequent retrieval can add irrelevant context, reinforce stale or incorrect memory, increase downstream token use, or distract the model. The argument should therefore be treated as a plausible control-system mechanism supported by infrastructure measurements, not a demonstrated causal law of agent performance.

## What Changed
- Added retrieval cost as a determinant of agent evidence-seeking policy.
- Separated a cheaper query surface from the higher-level policy that decides whether retrieved evidence is useful.

## Related Concepts
- [[AgentMemory]] - supplies the accumulated state whose retrieval cost is being budgeted.
- [[HarnessEngineering]] - controls when tools run and how retrieved evidence enters the work loop.
- [[BM25]] - provides the lexical ranking used in the source's low-cost implementation.
- [[LLMContextManagement]] - decides which retrieved material should enter limited model context.
- [[RetrievalAugmentedGeneration]] - broader pattern in which external retrieval grounds model output.

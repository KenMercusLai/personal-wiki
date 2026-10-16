---
title: "RAG Context Pruning"
type: concept
tags: [ai, rag, retrieval, context-management]
sources:
  - kapa-prune-rag
last_updated: 2026-10-17
knowledge_schema: synthesis-v1
---

## Definition
[[RAGContextPruning]] is a post-retrieval step that removes chunks judged unnecessary for answering a question before those chunks enter the generator's context.

## Current Synthesis
The available Kapa implementation places one small, cheap LLM call after search and reranking but before the larger generator. Rather than judging query-chunk pairs independently, it shows the model the question and complete retrieved set, assigns each chunk one of five verbally defined relevance levels, retains chunks at or above a threshold, and can preserve the top reranked chunks as a safeguard.

The set-level view matters because one chunk may provide a prerequisite, constraint, or second half of an answer without repeating the query's terminology. A pointwise reranker can order individually similar chunks, but its scores need not be calibrated across queries and cannot infer that two individually incomplete chunks jointly answer the question. Pruning is therefore an evidence-set selection problem, not merely a lower top-k.

The decision boundary is operational. More compression reduces generator input cost and frees agent context, but each removed necessary chunk risks an incomplete or wrong answer. Kapa's selected first-party point reportedly drops about 68% of chunks, preserves every labeled necessary chunk on about 96% of questions, lowers cost about 34% net of pruning, and adds about 0.7 seconds. Those figures define one workload-specific operating point, not a universal threshold.

## Key Claims
- Context pruning belongs after broad retrieval and reranking but before expensive generation.
- Relevance can depend on relationships among chunks, so set-aware grading can retain prerequisites and complementary evidence that pointwise scoring misses.
- Verbally anchored relevance levels support a fixed policy more directly than uncalibrated reranker scores.
- Threshold, pruner model, and keep-top-k jointly determine the compression, recall, cost, and latency tradeoff.
- Full-needed-set recall is stricter than average chunk recall because one missing required chunk makes the question count as a failure.
- Agentic settings can tolerate pruning better when another search is possible, but the extra model call remains a critical-path latency cost.

## Evidence
- Pipeline placement and cost target: [[kapa-prune-rag]] shows a small pruner reducing roughly 15 reranked chunks to about five before generation and reports retrieved chunks as 65.3% of its assistant query cost.
- Set-dependent relevance: [[kapa-prune-rag]] shows an audit-log answer requiring both a high-scoring location chunk and a low-scoring constraint chunk.
- Grading policy: [[kapa-prune-rag]] defines essential, contributing, supporting, tangential, and unrelated levels plus a keep-top-k safeguard.
- Operating frontier: [[kapa-prune-rag]] plots scoring, budget selection, direct keep/drop, and naive top-N configurations against compression and full-needed-set recall, with scoring forming the reported upper frontier.
- Deployment tradeoff: [[kapa-prune-rag]] reports about 34% net cost reduction, 0.7-second pruning latency, and initial rollout in agent-oriented retrieval.

## Counterevidence & Qualifications
The only current evidence is a first-party Kapa account. It does not disclose sample size, class balance, confidence intervals, pruner identity, prompts, thresholds, keep-top-k, corpus distribution, end-answer accuracy, or adversarial behavior. Labeled necessary chunks may also miss alternative valid evidence sets, and full-needed-set recall does not by itself measure whether the generator uses retained evidence faithfully. A second model call increases cost, latency, operational complexity, and exposure to grading errors; small retrieval sets or cheap generators may not leave enough savings to justify it.

## What Changed
- Established listwise post-rerank pruning as a distinct RAG context-selection pattern.
- Added set-dependent chunk relevance as the reason pointwise cutoffs can fail.
- Added full-needed-set recall, compression, net cost, and latency as a joint evaluation frame.

## Related Concepts
- [[RetrievalAugmentedGeneration]] - context pruning narrows retrieved evidence before RAG generation.
- [[LLMContextManagement]] - pruning allocates finite attention and token cost to higher-value evidence.
- [[AgenticRAG]] - repeatable search can mitigate missing evidence while tool outputs make context savings more valuable.
- [[DynamicContextCompression]] - both remove low-value context, but RAG pruning acts on a retrieved evidence set before generation.
- [[EvalsDrivenAIDevelopment]] - labeled necessary chunks and production replay are evaluation inputs for choosing an operating point.

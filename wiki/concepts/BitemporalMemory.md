---
title: "Bitemporal Memory"
type: concept
tags: [ai, agents, memory, temporal-data]
sources:
  - wei-ai-agent-gou-jian-ji-yi-xi-tong
last_updated: 2026-10-08
knowledge_schema: synthesis-v1
---

## Definition
[[BitemporalMemory]] is an agent-memory model that separately records when an event occurred and when the system learned or stored it.

## Current Synthesis
Event time answers questions about the world, while record time answers questions about the knowledge system itself. Keeping both prevents a memory saved today about a 2020 event from being ranked or displayed as though the event happened today. Precision and confidence are part of this model: a year-only statement should remain year-precision, and a vague low-confidence relative date should not be converted into invented certainty.

Temporal retrieval should be gated because most queries have no time intent. In the described design, cheap pattern checks and a tiny classifier precede full extraction, and a capped time boost remains subordinate to semantic relevance.

## Key Claims
- Event time and record time answer different classes of question and should not share one `created_at` field.
- Temporal precision must be stored so interfaces do not display fabricated month or day detail.
- Low-confidence inferred dates should be omitted rather than guessed.
- Cheap gates can prevent expensive temporal extraction on queries without time intent.
- Time can refine ranking without displacing semantic relevance as the primary signal.

## Evidence
- Dual clocks: [[wei-ai-agent-gou-jian-ji-yi-xi-tong]] contrasts “what happened in 2020” with “what was added this week.”
- Precision and confidence: [[wei-ai-agent-gou-jian-ji-yi-xi-tong]] stores `2020-01-01` with year precision for a year-only statement and rejects inferred dates below a confidence threshold.
- Cascaded extraction: [[wei-ai-agent-gou-jian-ji-yi-xi-tong]] uses regex filtering, a three-token intent gate, and full structured extraction only when needed.
- Ranking boundary: [[wei-ai-agent-gou-jian-ji-yi-xi-tong]] caps time contribution while assigning the dominant weight to semantic similarity.

## Counterevidence & Qualifications
The source reports one product design, not a comparison against temporal databases or alternative retrieval policies. It does not specify correction semantics for wrongly inferred dates, interval uncertainty, recurring events, time zones, delayed reporting, or cases where record time itself is revised. Its numeric gates and weights are unvalidated outside the described workload.

## What Changed
- Established event time, record time, precision, and confidence as separate memory metadata.
- Added gated temporal extraction and bounded temporal reranking as retrieval policies.

## Related Concepts
- [[AgentMemory]] - bitemporal metadata keeps recalled facts historically and operationally interpretable.
- [[MemoryEvolution]] - event time and validity help distinguish supersession from contradiction.
- [[MemoryConflictResolution]] - temporal context can explain apparently incompatible records.
- [[LLMContextManagement]] - temporal intent helps select the appropriate evidence for the active prompt.
- [[NowledgeMem]] - supplies the source implementation of the two-clock model.

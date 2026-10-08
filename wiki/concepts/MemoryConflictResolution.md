---
title: "Memory Conflict Resolution"
type: concept
tags: [ai, agents, memory, provenance]
sources:
  - ai-memory-de-zhen-zheng-nan-dian-wei-shen-me-vector-store-embedding-yuan-yuan-bu-gou
  - wei-ai-agent-gou-jian-ji-yi-xi-tong
last_updated: 2026-09-24
knowledge_schema: synthesis-v1
---

## Definition
[[MemoryConflictResolution]] is the process of detecting incompatible memory claims and deciding whether they represent change, context-dependent truth, inconsistent evidence, or an erroneous inference.

## Current Synthesis
Conflict resolution cannot rely on vector similarity or unconditional latest-wins. A useful policy considers when each claim applied, how it was obtained, and how strongly it is supported; it may replace the current state while retaining older versions for historical questions. Explicit user statements normally outrank model inference, but even direct statements can conflict or describe different contexts, so provenance and confidence inform rather than mechanically settle the judgment.

Nowledge Mem adds a conservative product boundary: a `challenges` edge detects incompatibility but does not authorize automatic resolution. The interface presents both versions and lets the user keep the newer claim, retain both, or ignore the challenge. This preserves agency and auditability, though it moves rather than solves the burden of ambiguous or high-volume adjudication.

## Key Claims
- Contradictions can arise from genuine behavior change, inconsistent statements, or model inference errors.
- Recency is useful when a claim clearly supersedes an earlier state but is not a universal truth rule.
- Direct user statements should generally carry more authority than model-derived guesses.
- Confidence and provenance must travel with a memory to support later adjudication.
- Multiple time-bounded versions can preserve valid history while exposing one current state, and unresolved challenges should remain visible rather than being silently flattened.

## Evidence
- Conflict classes: [[ai-memory-de-zhen-zheng-nan-dian-wei-shen-me-vector-store-embedding-yuan-yuan-bu-gou]] separates user change, inconsistent expression, and erroneous LLM inference.
- Recency limit: [[ai-memory-de-zhen-zheng-nan-dian-wei-shen-me-vector-store-embedding-yuan-yuan-bu-gou]] presents latest-wins for a diet change but says it is not always correct.
- Source priority: [[ai-memory-de-zhen-zheng-nan-dian-wei-shen-me-vector-store-embedding-yuan-yuan-bu-gou]] ranks explicit user statements above inference in its example.
- Version preservation: [[ai-memory-de-zhen-zheng-nan-dian-wei-shen-me-vector-store-embedding-yuan-yuan-bu-gou]] retains vegetarian and meat-eating periods with different validity ranges.
- Challenge semantics: [[wei-ai-agent-gou-jian-ji-yi-xi-tong]] separates `challenges` validation edges from `replaces` progression edges.
- User adjudication: [[wei-ai-agent-gou-jian-ji-yi-xi-tong]] presents conflicting memories side by side and offers keep-new, keep-both, and ignore choices.

## Counterevidence & Qualifications
The sources provide heuristics and one product workflow, not a complete adjudication protocol. They do not address deception, ambiguous language, multi-user authority, source independence, domain-specific stakes, user appeals, notification fatigue, or cases where behavior and stated preference legitimately differ. Confidence scores can create false precision unless their meaning and calibration are defined, and human review does not scale automatically with conflict volume.

## What Changed
- Established provenance, confidence, and time as separate conflict signals.
- Rejected unconditional latest-wins in favor of qualified, version-preserving adjudication.
- Added explicit challenge edges and user-visible keep-new, keep-both, or ignore decisions.

## Related Concepts
- [[AgentMemory]] - conflict handling prevents retrieval from surfacing incompatible claims without context.
- [[MemoryEvolution]] - genuine state change is one conflict class and may require temporal versions.
- [[MemoryCompaction]] - compaction must not merge contradictory records into a false generalization.
- [[Embeddings]] - similarity detects related records but does not determine which claim is valid.
- [[TapeAndAnchors]] - immutable history preserves the evidence needed to revisit a resolution.
- [[BitemporalMemory]] - separate event and record time can distinguish changed reality from delayed recording.
- [[NowledgeMem]] - supplies the user-visible challenge and adjudication workflow.

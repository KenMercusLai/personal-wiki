---
title: "Trust Topology"
type: concept
tags: [ai, agents, verification, software-engineering, reliability]
sources:
  - duo-agent-xie-zuo-ben-zhi-shi-fen-bu-shi-xi-tong-wen-ti-mo-xing-duo-qiang-ye-mei-yong
last_updated: 2026-09-13
knowledge_schema: synthesis-v1
---

## Definition
[[TrustTopology]] is Michael Rothrock's framework for arranging verification gates so unreliable AI agents can produce more reliable software systems.

## Current Synthesis
The source presents Trust Topology as the empirical counterpart to the distributed-consensus argument. Instead of treating model intelligence as the source of reliability, Rothrock treats reliability as an arrangement property: deterministic checks provide cheap guarantees, LLM reviewers cover semantic gaps probabilistically, and humans act as expensive oracles when intent or architecture cannot be inferred from artifacts.

The framework is diagnostic as well as architectural. Gate overlap indicates duplicated signal rather than independent checking; upstream gates amplify downstream reliability by narrowing the space of acceptable outputs; deterministic checks create a floor but cannot prove semantic correctness; and too many gates can destroy liveness by forcing endless retries. The system improves when repeated probabilistic or human judgments are encoded into cheaper, more deterministic rules.

## Key Claims
- Reliability in agent pipelines is an orchestration property, not merely a model property.
- Heterogeneous gates are more valuable than repeated checks with highly overlapping rejection signals.
- Deterministic checks provide proof-like guarantees only for the behavior they cover.
- LLM reviewers can fill semantic gaps but add probabilistic rather than formal guarantees.
- Human judgment should be routed to irreducible intent and architecture questions.
- Verification boundaries should migrate as recurring failures become deterministic checks or reviewer rules.

## Evidence
- Empirical dataset: [[duo-agent-xie-zuo-ben-zhi-shi-fen-bu-shi-xi-tong-wen-ti-mo-xing-duo-qiang-ye-mei-yong]] reports 5,109 gate checks and 1,450 explicit rejections across Rothrock's eight projects.
- Error structure: [[duo-agent-xie-zuo-ben-zhi-shi-fen-bu-shi-xi-tong-wen-ti-mo-xing-duo-qiang-ye-mei-yong]] says 87% of errors were predictable categories: omissions, systematic errors, and incoherence.
- Gate specialization: [[duo-agent-xie-zuo-ben-zhi-shi-fen-bu-shi-xi-tong-wen-ti-mo-xing-duo-qiang-ye-mei-yong]] says plan review mainly caught omissions, design review mainly caught systematic errors, and file-level code review missed incoherence.
- Liveness risk: [[duo-agent-xie-zuo-ben-zhi-shi-fen-bu-shi-xi-tong-wen-ti-mo-xing-duo-qiang-ye-mei-yong]] warns that excessive rejection rates can create retry storms.

## Counterevidence & Qualifications
The wiki currently has only a secondary summary of Rothrock's work, not the original dataset. The reported percentages should therefore be treated as source-specific evidence for one pipeline design, not as universal rates for every agent system.

## What Changed
- Created the concept page from the multi-agent distributed-systems source.

## Related Concepts
- [[SoftwareVerification]] - Trust Topology arranges verification into a reliability architecture.
- [[OracleRouting]] - human escalation is the top layer in the topology.
- [[AgentTeam]] - multi-agent teams need non-overlapping gates and global review to avoid incoherence.
- [[HarnessEngineering]] - trust topology is a verification-centered harness pattern.
- [[AIFirstEngineering]] - AI-first workflows need verification topology to make fast generation reliable.
- [[DistributedConsensus]] - trust topology is a practical response to multi-agent coordination limits.

---
title: "Distributed Consensus"
type: concept
tags: [distributed-systems, ai, agents, reliability]
sources:
  - duo-agent-xie-zuo-ben-zhi-shi-fen-bu-shi-xi-tong-wen-ti-mo-xing-duo-qiang-ye-mei-yong
last_updated: 2026-09-13
knowledge_schema: synthesis-v1
---

## Definition
[[DistributedConsensus]] is the problem of getting multiple independent nodes or agents to agree on one coherent decision or state despite asynchronous communication, partial failure, and inconsistent local views.

## Current Synthesis
The source applies distributed consensus to multi-agent software development. A natural-language prompt is underspecified, so there are many valid programs that could satisfy it. When several agents work in parallel, each local design decision narrows the acceptable solution space for the others; successful collaboration therefore requires convergence on one compatible interpretation, not just merging separately written components.

This framing explains why stronger models do not erase coordination limits. Agents can run asynchronously, hang, lose tool calls, or misunderstand the prompt. FLP-style reasoning says an asynchronous system with possible crash failures cannot guarantee safety, liveness, and fault tolerance together, while Byzantine-style reasoning makes prompt misunderstanding a hard coordination risk.

## Key Claims
- Multi-agent software development is joint synthesis over an underspecified prompt.
- Prompt precision cannot be made complete without moving toward code-level specification.
- Asynchronous progress and possible agent crashes create FLP-like safety, liveness, and fault-tolerance tradeoffs.
- Prompt misunderstanding can act like a Byzantine fault even when no agent is malicious.
- Failure detectors and external verification can improve practical consensus behavior without removing theoretical limits.

## Evidence
- Joint synthesis: [[duo-agent-xie-zuo-ben-zhi-shi-fen-bu-shi-xi-tong-wen-ti-mo-xing-duo-qiang-ye-mei-yong]] describes agents producing refinements that must fit one shared program interpretation.
- Underspecification: [[duo-agent-xie-zuo-ben-zhi-shi-fen-bu-shi-xi-tong-wen-ti-mo-xing-duo-qiang-ye-mei-yong]] argues that natural-language software prompts necessarily leave design choices open.
- Consensus limits: [[duo-agent-xie-zuo-ben-zhi-shi-fen-bu-shi-xi-tong-wen-ti-mo-xing-duo-qiang-ye-mei-yong]] maps agent tool hangs, self-kills, and unreturned calls onto possible crash failures.
- Byzantine analogy: [[duo-agent-xie-zuo-ben-zhi-shi-fen-bu-shi-xi-tong-wen-ti-mo-xing-duo-qiang-ye-mei-yong]] says misunderstood requirements can make an agent work against the intended shared system.

## Counterevidence & Qualifications
The article does not say multi-agent development is impossible. Its claim is narrower: practical systems can work through ad hoc or explicit coordination mechanisms, but those mechanisms make tradeoffs rather than escaping consensus boundaries.

## What Changed
- Created the concept page from the multi-agent distributed-systems source.

## Related Concepts
- [[AgentTeam]] - agent teams are a software-workflow instance of multi-agent coordination.
- [[ProductionAgentInfrastructure]] - production agent runtimes need failure detection, recovery, and capability controls around consensus limits.
- [[SoftwareVerification]] - external checks can stop or correct some divergent agent work.
- [[SystemReliability]] - consensus limits are one reliability concern in distributed systems.
- [[TrustTopology]] - verification topology is a practical architecture for making unreliable agents more dependable.

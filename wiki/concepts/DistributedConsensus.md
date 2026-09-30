---
title: "Distributed Consensus"
type: concept
tags: [distributed-systems, ai, agents, reliability]
sources:
  - duo-agent-xie-zuo-ben-zhi-shi-fen-bu-shi-xi-tong-wen-ti-mo-xing-duo-qiang-ye-mei-yong
  - unmesh-joshi-paxos
  - unmesh-joshi-replicated-log
  - laisky-reading-notes-on-designing-data-intensive-applications
last_updated: 2026-10-01
knowledge_schema: synthesis-v1
---

## Definition
[[DistributedConsensus]] is the problem of getting multiple independent nodes or agents to agree on one coherent decision or state despite asynchronous communication, partial failure, and inconsistent local views.

## Current Synthesis
Distributed consensus covers both classical replica agreement and coordination among software agents. In replicated systems, competing nodes may need to choose one value without a leader even when nodes fail, links break, or a participant reaches a majority and disappears before broadcasting the outcome. [[Paxos]] addresses safe choice across competing rounds by using prepare and accept to establish a chosen value, then a separate commit step to disseminate it.

Agreement on isolated state changes is not enough to guarantee identical state: replicas can apply the same accepted requests in different orders and diverge. A [[ReplicatedLog]] makes ordering part of the agreement by giving every node the same sequence of requests to execute sequentially.

In multi-agent software development, the value being coordinated is an interpretation of an underspecified prompt. There are many valid programs that could satisfy it, and each agent's local design decisions narrow the acceptable solution space for the others; successful collaboration therefore requires convergence on one compatible interpretation, not just merging separately written components.

This framing explains why stronger models do not erase coordination limits. Agents can run asynchronously, hang, lose tool calls, or misunderstand the prompt. FLP-style reasoning says an asynchronous system with possible crash failures cannot guarantee safety, liveness, and fault tolerance together, while Byzantine-style reasoning makes prompt misunderstanding a hard coordination risk.

Laisky's reading notes sharpen the boundary among neighboring guarantees. Serializability constrains the outcome of multi-object transactions, while linearizability makes single-object operations appear atomic and current. Total-order broadcast can underpin state-machine replication, terms or views fence obsolete leaders, and partial synchrony or timeouts make practical progress without disproving FLP. Two-phase commit solves atomic commitment across participants but can block behind a failed coordinator; it is related to coordination but is not itself a consensus protocol.

## Key Claims
- Classical consensus must preserve an earlier chosen value even when only part of the cluster learned it.
- Paxos uses generations, prior accepted values, and overlapping majorities to protect agreement safety across rounds.
- Replicated state requires agreement on one request order, not only agreement on each request in isolation.
- Multi-agent software development is joint synthesis over an underspecified prompt whose precision cannot be made complete without approaching code-level specification.
- Asynchronous progress and possible agent crashes create FLP-like safety, liveness, and fault-tolerance tradeoffs.
- Prompt misunderstanding can act like a Byzantine fault even when no agent is malicious.
- Serializability, linearizability, total-order broadcast, consensus, and atomic commit solve different ordering or commitment problems.

## Evidence
- Replica agreement: [[unmesh-joshi-paxos]] describes competing nodes seeking a majority while failures can prevent the whole cluster from learning a chosen value.
- Paxos safety structure: [[unmesh-joshi-paxos]] says prepare gathers the latest generation and previously accepted values before accept proposes a value for that generation.
- Ordered state convergence: [[unmesh-joshi-replicated-log]] says replicas can diverge after agreeing on individual requests unless they also agree on and sequentially execute one common log.
- Joint synthesis: [[duo-agent-xie-zuo-ben-zhi-shi-fen-bu-shi-xi-tong-wen-ti-mo-xing-duo-qiang-ye-mei-yong]] describes agents producing refinements that must fit one shared program interpretation.
- Underspecification: [[duo-agent-xie-zuo-ben-zhi-shi-fen-bu-shi-xi-tong-wen-ti-mo-xing-duo-qiang-ye-mei-yong]] argues that natural-language software prompts necessarily leave design choices open.
- Consensus limits: [[duo-agent-xie-zuo-ben-zhi-shi-fen-bu-shi-xi-tong-wen-ti-mo-xing-duo-qiang-ye-mei-yong]] maps agent tool hangs, self-kills, and unreturned calls onto possible crash failures.
- Byzantine analogy: [[duo-agent-xie-zuo-ben-zhi-shi-fen-bu-shi-xi-tong-wen-ti-mo-xing-duo-qiang-ye-mei-yong]] says misunderstood requirements can make an agent work against the intended shared system.
- Guarantee boundaries: [[laisky-reading-notes-on-designing-data-intensive-applications]] distinguishes transaction serializability from single-object linearizability and relates total-order broadcast to state-machine replication.
- Progress and commit: [[laisky-reading-notes-on-designing-data-intensive-applications]] presents FLP as a finite-time guarantee limit in pure asynchrony and contrasts elected-term consensus with blocking two-phase commit.

## Counterevidence & Qualifications
The multi-agent article does not say collaborative development is impossible. Its claim is narrower: practical systems can work through ad hoc or explicit coordination mechanisms, but those mechanisms make tradeoffs rather than escaping consensus boundaries. The Paxos, replicated-log, and book-note sources are compressed descriptions and do not provide complete protocol specifications, safety proofs, recovery procedures, or liveness analyses; they should not be treated as sufficient implementation guidance. Timeouts and partial synchrony support practical liveness assumptions but do not turn unreliable networks into perfectly synchronous ones.

## What Changed
- Distinguished consensus from serializability, linearizability, total-order broadcast, and atomic commitment.
- Added terms, partial synchrony, and the blocking boundary of two-phase commit.

## Related Concepts
- [[Paxos]] - classical consensus protocol family using quorum intersection and ordered proposal generations.
- [[ReplicatedLog]] - applies consensus across ordered log positions so replicas execute one shared history.
- [[AgentTeam]] - agent teams are a software-workflow instance of multi-agent coordination.
- [[ProductionAgentInfrastructure]] - production agent runtimes need failure detection, recovery, and capability controls around consensus limits.
- [[SoftwareVerification]] - external checks can stop or correct some divergent agent work.
- [[SystemReliability]] - consensus limits are one reliability concern in distributed systems.
- [[TrustTopology]] - verification topology is a practical architecture for making unreliable agents more dependable.
- [[DataIntensiveSystems]] - consensus is one coordination mechanism within a larger data-system design space.

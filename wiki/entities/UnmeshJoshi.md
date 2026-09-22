---
title: "Unmesh Joshi"
type: entity
tags: [author, distributed-systems]
sources:
  - unmesh-joshi-paxos
  - unmesh-joshi-replicated-log
  - unmesh-joshi-two-phase-commit
last_updated: 2026-09-23
knowledge_schema: synthesis-v1
---

## Overview
[[UnmeshJoshi]] is the author of concise pattern descriptions of [[Paxos]], [[ReplicatedLog]], and [[TwoPhaseCommit]].

## Current Profile
In the available evidence, Joshi explains distributed-systems patterns through their problem, failure scenario, and solution structure. His Paxos article frames agreement around proposal phases, overlapping majorities, and partial dissemination; his replicated-log article explains why replicas also need one agreed execution order to reach the same state; and his two-phase-commit article separates durable preparation from the final commit-or-rollback decision for an atomic multi-node update.

## Key Characteristics
- Writes concise, problem-and-solution descriptions of distributed-systems patterns.
- Presents Paxos through prepare, accept, and commit phases.
- Distinguishes consensus on individual changes from consensus on their ordering.
- Explains atomic commitment through participant promises, unanimous preparation, and durable recovery state.
- Connects protocol mechanics to node and network failure scenarios.

## Evidence
- Authorship and scope: [[unmesh-joshi-paxos]] and [[unmesh-joshi-replicated-log]] identify Joshi as the author and place both articles in Patterns of Distributed Systems.
- Explanatory approach: [[unmesh-joshi-paxos]] moves from leaderless quorum competition and disconnection risk to the three protocol phases.
- Protocol framing: [[unmesh-joshi-paxos]] distinguishes the first two consensus-building phases from final dissemination.
- Ordered replication: [[unmesh-joshi-replicated-log]] moves from per-request agreement to the additional need for one common log and sequential execution.
- Atomic commitment: [[unmesh-joshi-two-phase-commit]] explains how prepare promises and durable decisions support one commit-or-rollback outcome across participating nodes.

## Qualifications
This profile is limited to three short articles in one pattern series. It does not establish Joshi's broader biography, affiliations, or complete body of work, and the articles are conceptual summaries rather than complete protocol specifications.

## What Changed
- Extended the profile from one consensus protocol to Joshi's explanation of ordered replicated state.
- Added Joshi's account of atomic multi-node updates through two-phase commit.

## Relationships
- [[Paxos]] - Joshi explains the protocol as a three-phase distributed-systems pattern.
- [[ReplicatedLog]] - Joshi explains how one agreed request order keeps replica state synchronized.
- [[TwoPhaseCommit]] - Joshi explains how participants prepare durably before one atomic commit-or-rollback decision.
- [[DistributedConsensus]] - Joshi's article applies this broader problem to replicated nodes under partial failure.
- [[LeslieLamport]] - Joshi credits Lamport with developing Paxos.

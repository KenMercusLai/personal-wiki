---
title: "Paxos"
type: concept
tags: [distributed-systems, consensus, fault-tolerance]
sources:
  - unmesh-joshi-paxos
last_updated: 2026-09-22
knowledge_schema: synthesis-v1
---

## Definition
[[Paxos]] is a distributed-consensus protocol family for choosing one value safely among competing proposals even when some nodes or network links fail.

## Current Synthesis
The source presents Paxos as a three-phase pattern. Prepare establishes the newest proposal generation and discovers values replicas have already accepted; accept proposes a value for that generation; commit disseminates the chosen result to the remaining replicas. The safety logic depends on majority quorums overlapping: a later proposer must learn about prior accepted state rather than select a conflicting value in ignorance.

This separation matters because choosing a value and informing every replica are different events. A node can gather a majority and then disconnect before broadcasting the result, so a later attempt must preserve the earlier decision even when some participants have not learned it.

## Key Claims
- Paxos separates agreement-building from dissemination of the chosen value.
- Prepare discovers the latest generation and any value already accepted by replicas.
- Accept asks a majority to accept a proposal associated with that generation.
- Commit informs remaining replicas after a value has been chosen.
- Overlapping majorities allow later rounds to preserve prior accepted state despite partial failures.

## Evidence
- Phase structure: [[unmesh-joshi-paxos]] describes prepare and accept as the consensus-building phases and commit as communication of the result.
- Prior-state preservation: [[unmesh-joshi-paxos]] says prepare gathers the latest generation and any already accepted values before a new proposal proceeds.
- Partial-failure case: [[unmesh-joshi-paxos]] describes a node reaching a majority and disconnecting before it can notify the whole cluster.
- Protocol lineage: [[unmesh-joshi-paxos]] attributes Paxos to [[LeslieLamport]] and his 1998 paper "The Part-Time Parliament."

## Counterevidence & Qualifications
The source is a short pattern overview, not a full Paxos specification or proof. It does not detail proposal-number construction, proposer and acceptor rules, quorum-intersection proofs, competing-round behavior, retry policy, leader-based optimizations, or liveness conditions. Its “commit phase” is best read as a learning or dissemination step: the first two phases establish the chosen value, while notifying every replica can lag or fail.

## What Changed
- Created a protocol-specific page that distinguishes choosing a value from disseminating it.
- Added the role of generations and previously accepted values in preserving safety across rounds.

## Related Concepts
- [[DistributedConsensus]] - Paxos is a classical protocol family for solving the agreement problem under partial failure.
- [[SystemReliability]] - Paxos preserves agreement safety when nodes or network links fail.
- [[DistributedProgramming]] - Paxos addresses a coordination problem that arises once computation and state span independent nodes.

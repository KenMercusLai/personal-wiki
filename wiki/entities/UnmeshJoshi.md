---
title: "Unmesh Joshi"
type: entity
tags: [author, distributed-systems]
sources:
  - unmesh-joshi-paxos
last_updated: 2026-09-22
knowledge_schema: synthesis-v1
---

## Overview
[[UnmeshJoshi]] is the author of the source article's concise pattern description of [[Paxos]].

## Current Profile
In the available evidence, Joshi explains distributed-systems patterns through their problem, failure scenario, and protocol phases. His Paxos article frames the protocol around leaderless agreement, overlapping majorities, and the risk that a node chooses a value but disconnects before the whole cluster learns it.

## Key Characteristics
- Writes concise, problem-and-solution descriptions of distributed-systems patterns.
- Presents Paxos through prepare, accept, and commit phases.
- Connects protocol mechanics to node and network failure scenarios.

## Evidence
- Authorship and scope: [[unmesh-joshi-paxos]] identifies Joshi as the author and describes the article as part of Patterns of Distributed Systems.
- Explanatory approach: [[unmesh-joshi-paxos]] moves from leaderless quorum competition and disconnection risk to the three protocol phases.
- Protocol framing: [[unmesh-joshi-paxos]] distinguishes the first two consensus-building phases from final dissemination.

## Qualifications
This profile is limited to one short article. It does not establish Joshi's broader biography, affiliations, or complete body of work.

## What Changed
- Created the entity page from the Paxos pattern article.

## Relationships
- [[Paxos]] - Joshi explains the protocol as a three-phase distributed-systems pattern.
- [[DistributedConsensus]] - Joshi's article applies this broader problem to replicated nodes under partial failure.
- [[LeslieLamport]] - Joshi credits Lamport with developing Paxos.

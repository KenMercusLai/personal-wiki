---
title: "Paxos"
type: source
tags: [distributed-systems, paxos, consensus]
date: 2023-11-23
source_file: /mnt/ken_personal_wiki/Articles/Unmesh Joshi - Paxos.md
---

## Summary
[[UnmeshJoshi]] presents [[Paxos]] as a three-phase pattern for reaching safe [[DistributedConsensus]] when nodes can fail or disconnect and no single leader can reliably impose a value. Prepare discovers the latest generation and any previously accepted value, accept asks replicas to accept a proposal for that generation, and commit tells the remaining replicas which value was chosen.

## Key Claims
- Replicated nodes may need to agree on a value even when there is no leader, including when choosing a new leader.
- Competing nodes can each seek a majority while failures and disconnections leave them with incomplete knowledge of what other nodes accepted.
- Paxos uses prepare and accept to build agreement around a safe value, then commit to communicate the chosen value to the rest of the replicas.
- The prepare phase gathers the latest generation and any value already accepted, preventing a new round from disregarding prior acceptance.
- [[LeslieLamport]] developed Paxos and published its original presentation in the 1998 paper "The Part-Time Parliament."

## Key Quotes
> "The first two phases act to build consensus around a value and the last phase then communicates that consensus to the remaining replicas." - distinction between choosing and disseminating a value.

## Connections
- [[UnmeshJoshi]] - author of this concise pattern description.
- [[LeslieLamport]] - originator of the Paxos algorithm.
- [[Paxos]] - consensus protocol pattern explained by the article.
- [[DistributedConsensus]] - the broader agreement problem Paxos addresses under partial failure.
- [[SystemReliability]] - Paxos protects agreement safety despite node or network failures.

## Contradictions
- No direct contradiction with existing wiki content. The source extends the agent-oriented [[DistributedConsensus]] page with a classical replica-consensus mechanism; its three-phase account is a simplified pattern description rather than a complete protocol or liveness analysis.

---
title: "Replicated Log"
type: source
tags: [distributed-systems, consensus, replication, write-ahead-log]
date: 2023-11-23
source_file: /mnt/ken_personal_wiki/Articles/Unmesh Joshi - Replicated Log.md
---

## Summary
[[UnmeshJoshi]] presents a [[ReplicatedLog]] as the bridge between [[DistributedConsensus]] on individual state changes and identical replicated state. Cluster nodes agree on the same sequence of write-ahead-log entries, then execute the recorded requests in order so that failures or disconnections do not leave replicas applying the same operations in different sequences.

## Key Claims
- Replicas that share state must agree despite node crashes and network disconnections.
- Agreement on each state-change request is insufficient when replicas can execute the agreed requests in different orders.
- Each cluster node maintains a write-ahead log whose entries contain the consensus state and the user request.
- Nodes build consensus over log entries so that every replica converges on the same ordered log.
- Sequential execution of that common log makes replicas apply the same requests in the same order and therefore maintain the same state.

## Key Quotes
> "Each replica also needs to execute requests in the same order" - why per-request agreement alone does not guarantee convergent state.

## Connections
- [[UnmeshJoshi]] - author of this concise distributed-systems pattern description.
- [[ReplicatedLog]] - the ordered-log pattern explained by the article.
- [[DistributedConsensus]] - agreement must cover each ordered log position, not only isolated requests.
- [[Paxos]] - a related consensus protocol pattern in Joshi's series; this source does not prescribe it as the replicated log's implementation.
- [[SystemReliability]] - common ordering preserves consistent replicated state through crashes and disconnections.

## Contradictions
- No direct contradiction with existing wiki content. The source extends the existing consensus material by distinguishing agreement on individual requests from agreement on one execution order; it is a short pattern overview rather than an implementation, proof, recovery protocol, or performance analysis.

---
title: "Two-Phase Commit"
type: source
tags: [distributed-systems, transactions, atomicity, write-ahead-log]
date: 2023-11-23
source_file: /mnt/ken_personal_wiki/Articles/Unmesh Joshi - Two-Phase Commit.md
---

## Summary
[[UnmeshJoshi]] explains [[TwoPhaseCommit]] as a coordinator-led protocol for making one update atomic across multiple nodes. Participants first prepare by acquiring the resources they need and durably promising whether they can commit; the coordinator then tells every participant either to commit if all voted yes or to roll back if any could not promise.

## Key Claims
- A multi-node update should not become visible until the participating nodes' ability to complete it is known.
- During prepare, each participant acquires required resources such as locks and promises the coordinator that it can commit later.
- Any participant that cannot prepare causes the coordinator to abort the transaction and tell all participants to roll back and release their locks.
- The commit phase begins only after every participant has promised it can commit.
- Participants must durably record their decisions, for example with a write-ahead log, so a restarted node can finish the protocol after a crash.

## Key Quotes
> "The prepare phase asks each node if it can promise to carry out the update." - the first phase establishes whether every participant can commit later.

## Connections
- [[UnmeshJoshi]] - author of this concise distributed-systems pattern description.
- [[TwoPhaseCommit]] - atomic-commit protocol explained by the article.
- [[AggregateTransactionBoundary]] - determines whether one invariant actually needs an atomic update across multiple resources.
- [[EventDrivenConsistency]] - an alternative for consistency across service boundaries when one distributed transaction is undesirable.
- [[SystemReliability]] - durable decisions allow participants to resume the protocol after a crash.

## Contradictions
- No direct contradiction with existing wiki content. [[christian-posta-the-hardest-part-about-microservices-your-data]] qualifies the pattern's scope by arguing that microservice teams should usually shrink transaction boundaries and communicate cross-boundary consistency with events rather than use two-phase commit across services.

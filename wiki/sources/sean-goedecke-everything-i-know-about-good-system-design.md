---
title: "Everything I know about good system design"
type: source
tags: [system-design, software-architecture, databases, reliability]
date: 2025-06-21
source_file: "/mnt/ken_personal_wiki/Articles/Sean Goedecke - Everything I know about good system design.md"
---

## Summary
[[SeanGoedecke]] presents [[PragmaticSystemDesign]] as the assembly of services around carefully owned state, workload-specific data paths, and mature operational primitives. Good design is deliberately uneventful: it begins simply, adds state and distribution only when justified, concentrates attention on critical or high-volume paths, and defines observable, bounded behavior for overload and partial failure.

## Key Claims
- System design concerns how services and infrastructure components fit together, and a working complex system should evolve from a simpler working system rather than begin over-designed.
- Stateful components deserve special restraint because corrupted, stale, full, or inconsistent state cannot usually be repaired by restarting a process; one service should normally own database writes for a domain.
- Database schemas should remain legible, indexes should reflect common query shapes, database work should stay in the database where practical, replicas should absorb lag-tolerant reads, and spikes of writes or transactions should be throttled.
- Interactive work should complete the minimum useful response quickly and move slow remainder work to background jobs; durable, far-future scheduling may fit a queryable database table better than an ephemeral queue.
- Caches and event buses add state or indirection and should follow a demonstrated need: optimize the underlying operation before caching, and prefer direct requests when the caller needs an immediate, inspectable result.
- Architecture should focus first on correctness-critical and high-volume hot paths, log unhappy-path decisions, and monitor tail latency, resource usage, queue depth, and work duration rather than averages alone.
- Failure handling requires bounded retries, circuit breakers, idempotency for ambiguous writes, killswitches, and an explicit choice to fail open or closed according to the safety obligation of each feature.

## Key Quotes
> "Good system design is not about clever tricks" - the article's closing distinction between architecture judgment and impressive machinery.

> "A complex system that works always evolves from a simple system that works." - the article's case against beginning with unearned complexity.

## Connections
- [[SeanGoedecke]] - author drawing on ten years of practitioner experience.
- [[PragmaticSystemDesign]] - integrated model of simple architecture, state ownership, data paths, operations, and failure semantics.
- [[BoringTechnology]] - mature, well-trodden components are preferred until a requirement earns custom machinery.
- [[DistributedSystemRestraint]] - complexity should be introduced from demonstrated scale, workload, or organizational needs rather than prestige.
- [[SystemReliability]] - explicit overload, retry, observability, and degraded-mode behavior make ordinary architecture dependable.
- [[DependencyDegradation]] - fail-open, fail-closed, circuit-breaker, and retry choices determine how dependency trouble propagates.
- [[ServiceObservability]] - unhappy-path logs and tail metrics expose behavior that averages and success-path logging hide.
- [[DatabaseOverloadProtection]] - query placement, replicas, throttling, and spike control protect the system's central stateful component.

## Contradictions
- The article qualifies its own simplicity preference: some workloads earn distributed or custom complexity, but they should evolve toward it from evidence rather than start there.
- Centralized state ownership is a default rather than an absolute rule; the author allows direct cross-service reads when an ownership-preserving API would impose disproportionate latency.
- Caching is treated as dangerous state, yet the author uses it extensively when the underlying operation has first been optimized and staleness is acceptable.
- Push versus pull and fail-open versus fail-closed decisions are explicitly workload- and safety-dependent, so the source does not offer one universal topology or degradation policy.
- The article is a first-person practitioner synthesis without comparative measurements, workload traces, formal availability targets, or evidence that its recommendations generalize across organizations and regulated domains.

---
title: "You Are Not Google"
type: source
tags: [engineering, architecture, decision-making, technology]
date: 2017-06-07
source_file: /mnt/ken_personal_wiki/Articles/You Are Not Google - Bradfield.md
---

## Summary
[[OzNova]] argues that engineers should choose technology from the scale, workload, team, and constraints of their own problem rather than imitate systems built by much larger companies. The article presents the UNPHAT checklist as a disciplined alternative: understand the problem, enumerate candidates, read the paper, recover historical context, weigh tradeoffs, and state what evidence would change the decision.

## Key Claims
- Technology adoption becomes cargo culting when a team copies a large company's solution without matching the conditions that made it necessary.
- A technology's design history explains its priorities: Cassandra inherits Amazon's requirement for write availability, while Kafka reflects LinkedIn's enormous event throughput.
- Orders-of-magnitude checks can expose architecture mismatch before implementation; a 4 GB read-heavy dataset or a few dozen daily transactions do not automatically justify distributed infrastructure.
- Service-oriented architecture addressed Amazon's coordination needs at roughly 7,800 employees and $3 billion in sales, not a universal need for very small teams to split simple applications into services.
- Google created GFS and MapReduce for web-scale computation and later stopped using MapReduce for indexing when it no longer fit, showing that even originators replace celebrated tools.
- UNPHAT makes technology selection falsifiable by requiring multiple candidates, explicit advantages and disadvantages, problem fit, and a fact that would change the chooser's mind.

## Key Quotes
> "Understand the problem." - the first step in UNPHAT.

> "What fact would need to be different for you to change your mind?" - the framework's test against attachment to a favored solution.

## Connections
- [[OzNova]] - author of the article and the UNPHAT framework.
- [[ContextualTechnologySelection]] - the article's method for comparing technologies against the actual problem and the history that shaped each candidate.
- [[DistributedSystemRestraint]] - the scale examples show why distributed systems should be deferred until workload and organization justify them.
- [[TechnologyStackComplexity]] - unnecessary distributed components add operational and reasoning cost without compensating benefit.
- [[BoringTechnology]] - adjacent practice of preferring proven tools when novelty does not solve a real constraint.
- [[Google]] - source of GFS and MapReduce and the article's central warning against imitating exceptional scale.
- [[Amazon]] - Dynamo and service-oriented architecture are explained as responses to Amazon-specific availability and organizational needs.
- [[LinkedIn]] - Kafka's original throughput context is contrasted with a very low-volume adopter.
- [[ApacheKafka]] - example of a sound technology selected for a workload many orders of magnitude smaller than its motivating case.
- [[PostgreSQL]] - the article argues that tuning it was more appropriate than replacing it for a roughly 4 GB read-heavy dataset.

## Contradictions
- No direct contradiction found. The article strengthens the wiki's stage-sensitive warnings about distributed systems while preserving the qualification that large-scale tools are appropriate when the adopting system actually shares their constraints.

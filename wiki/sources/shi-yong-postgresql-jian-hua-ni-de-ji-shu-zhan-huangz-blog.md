---
title: "使用PostgreSQL简化你的技术栈 - HUANGZ.BLOG"
type: source
tags: [database, architecture, simplicity]
date: 2024-05-24
source_file: /mnt/ken_personal_wiki/Articles/使用PostgreSQL简化你的技术栈 — HUANGZ.BLOG.md
---

## Summary
黄健宏 summarizes the "PostgreSQL for everything" argument as an antidote to database sprawl: when teams adopt a different datastore for transactions, search, time series, vectors, and analytics too early, the architecture becomes harder to learn, operate, and reason about. The article argues that [[PostgreSQL]] is unusually suitable for [[DatabaseConsolidation]] because it is mature, broadly deployed, and extensible enough to cover many specialized workloads before a team needs another database. Its local cartoon image reinforces this point by contrasting a cart full of specialized systems with one person carrying PostgreSQL.

## Key Claims
- Database sprawl creates [[TechnologyStackComplexity]] because every added datastore introduces a new language, consistency model, operational model, and data-flow boundary.
- [[DatabaseConsolidation]] can reduce the "dotted line" complexity that appears when data moves among many systems.
- [[PostgreSQL]] is a strong consolidation candidate because it combines relational maturity with extensions and workload breadth across full-text search, time-series data, vectors, and analytics.
- The "right tool for the job" principle should be evaluated globally: a specialized database is justified only when its benefits outweigh the added multi-system complexity.
- A PostgreSQL-first architecture may eventually hit scale or feature limits, but that later migration pressure can be healthier than premature multi-database fragility.

## Key Quotes
> "使用PostgreSQL解决所有问题" - the article's shorthand for choosing PostgreSQL first where it can reasonably cover the job.

> "虚线" - the author's metaphor for the extra complexity created by data moving between paired systems.

## Connections
- [[PostgreSQL]] - central database proposed as the default consolidation platform.
- [[Timescale]] - company promoted as a way to scale PostgreSQL-centered systems.
- [[DatabaseConsolidation]] - architectural strategy advocated by the article.
- [[TechnologyStackComplexity]] - problem created by adopting many specialized databases too early.
- [[VectorDatabase]] - one workload category the article argues may not require a separate specialized datastore if PostgreSQL is sufficient.
- [[Redis]] - one example in the image/source of a specialized data system that can add operational surface area when introduced as a separate dependency.

## Contradictions
- None identified. The article qualifies its own argument by saying PostgreSQL-first does not mean never using specialized databases.

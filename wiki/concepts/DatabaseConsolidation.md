---
title: "Database Consolidation"
type: concept
tags: [architecture, database, simplicity]
sources:
  - shi-yong-postgresql-jian-hua-ni-de-ji-shu-zhan-huangz-blog
last_updated: 2026-09-13
knowledge_schema: synthesis-v1
---

## Definition
[[DatabaseConsolidation]] is the architectural strategy of using one sufficiently capable database for multiple workload types so a system avoids unnecessary data-system proliferation.

## Current Synthesis
The source argues for consolidation as a response to early architecture sprawl. A product team can easily choose PostgreSQL for transactions, Elasticsearch for search, InfluxDB for time series, Pinecone for vectors, and ClickHouse for analytics, but each additional system creates new knowledge, operations, and consistency burdens.

Consolidation does not deny that specialized databases can be valuable. Its claim is temporal and systemic: start from the whole architecture, use [[PostgreSQL]] when it satisfies current needs, and add another database only when a missing critical capability or scaling limit justifies the extra coordination cost.

## Key Claims
- One capable database can reduce the operational surface area of a young or moderate system.
- Consolidating workloads lowers cross-system data-flow and consistency complexity.
- PostgreSQL is a strong consolidation platform because it is mature, extensible, and broadly supported.
- Specialized databases should be adopted when they solve a critical gap whose benefit exceeds the complexity cost.
- Outgrowing a consolidated architecture can be a success signal rather than evidence that early specialization was necessary.

## Evidence
- Sprawl example: [[shi-yong-postgresql-jian-hua-ni-de-ji-shu-zhan-huangz-blog]] describes teams using separate databases for transactions, search, time series, vector operations, and analytics.
- Complexity reduction: [[shi-yong-postgresql-jian-hua-ni-de-ji-shu-zhan-huangz-blog]] says fewer databases make data flow and consistency easier to model mentally.
- PostgreSQL fit: [[shi-yong-postgresql-jian-hua-ni-de-ji-shu-zhan-huangz-blog]] names PostgreSQL's extension architecture, maturity, production history, and ecosystem support.
- Adoption gate: [[shi-yong-postgresql-jian-hua-ni-de-ji-shu-zhan-huangz-blog]] says teams should add another database when PostgreSQL lacks key functionality and after weighing the management burden.

## Counterevidence & Qualifications
The argument is a heuristic for architectural restraint, not a proof that PostgreSQL will outperform specialized systems. The source acknowledges that a PostgreSQL-first system may eventually exceed PostgreSQL's design capacity or require capabilities better served by another datastore.

## What Changed
- Created the concept to capture the article's PostgreSQL-first simplification strategy.

## Related Concepts
- [[TechnologyStackComplexity]] - database consolidation is a proposed remedy for stack sprawl.
- [[PostgreSQL]] - PostgreSQL is the source's preferred consolidation default.
- [[SystemReliability]] - fewer operational systems can make reliability reasoning simpler, though not automatically solved.
- [[VectorDatabase]] - vector search is one workload category considered in the consolidation tradeoff.
- [[CloudHighAvailability]] - consolidated database choices still need mature recovery and availability patterns.

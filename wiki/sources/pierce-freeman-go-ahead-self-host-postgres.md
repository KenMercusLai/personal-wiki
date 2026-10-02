---
title: "Go ahead, self-host Postgres"
type: source
tags: [postgresql, self-hosting, databases, infrastructure, cloud-cost]
date: 2025-07-02
source_file: "/mnt/ken_personal_wiki/Articles/Pierce Freeman - Go ahead, self-host Postgres.md"
---

## Summary
[[PierceFreeman]] argues from two years of operating [[PostgreSQL]] for production products that self-hosting can be a practical alternative to [[AmazonRDS]] when a team can own incident response, tuning, backups, patching, monitoring, and recovery tests. His case links [[CloudCostOptimization]] to operational competence: a dedicated [[DigitalOcean]] server reportedly delivered comparable or better performance at lower direct cost, but the comparison is a first-person account rather than a controlled total-cost or reliability study. The article turns that position into a concrete [[SelfHostedDatabaseOperations]] checklist covering memory, connection pooling, NVMe-aware query planning, write-ahead logging, slow-query review, capacity planning, and disaster recovery.

## Key Claims
- Managed database services primarily add operational tooling and response around a familiar open-source engine; their value should be compared with the actual work a team would assume, not with the idea that the underlying database is fundamentally different.
- Freeman reports running self-hosted PostgreSQL for thousands of users and tens of millions of daily queries with one 30-minute stressful manual-migration episode over roughly two years, but supplies no availability series, incident log, or independent audit.
- A migration from RDS reportedly required about four hours of hands-on work plus several weeks of observation before production cutover; the author's higher-availability stacks then required roughly weekly checks, monthly maintenance, and optional quarterly recovery exercises.
- [[SelfHostedDatabaseOperations]] requires explicit memory sizing, conservative per-connection memory, connection pooling, storage-aware planner settings, WAL configuration, verified backups, patching, disk monitoring, slow-query review, and capacity planning.
- Self-hosting transfers incident response and platform decisions to the operator; managed services also fail, but may provide automated setup, support, compliance attestations, and provider-only recovery capabilities.
- The article argues for a broad self-hosting sweet spot while exempting very early builders, very large organizations that benefit from outsourced database expertise, and regulated workloads needing contractual or compliance support.
- Direct hosting price is incomplete evidence: application workload, staff skill, availability targets, recovery design, support, compliance, and the cost of operational attention determine the real comparison.

## Key Quotes
> "The value proposition is operational" - on what managed database services add around the database engine.

> "The main operational difference is that you're responsible for incident response." - on the responsibility transferred by self-hosting.

## Connections
- [[PierceFreeman]] - author and operator reporting the self-hosted PostgreSQL case.
- [[PostgreSQL]] - database engine being self-hosted, tuned, monitored, backed up, and patched.
- [[AmazonRDS]] - managed service used as the article's principal operational and cost comparison.
- [[DigitalOcean]] - provider of the reported 16-vCPU, 32-GB, 400-GB dedicated server.
- [[SelfHostedDatabaseOperations]] - operating discipline synthesized from the article's maintenance and configuration guidance.
- [[CloudCostOptimization]] - direct infrastructure savings are weighed against labor, risk, support, and compliance.
- [[DatabaseEngineeringTradeoffs]] - workload, configuration, query behavior, storage, and connection management shape the result.
- [[BackupAndRecovery]] - backup verification and disaster-recovery tests remain operator responsibilities.
- [[ServiceObservability]] - slow queries, disk growth, alerts, and performance trends make the database operable.

## Contradictions
- The article's price, provider implementation, outage, and product-capability statements are time-sensitive and are preserved as source claims, not current market facts.
- The claim that managed and self-hosted PostgreSQL have the same performance characteristics is too broad. The reported dump-and-restore comparison covers one application and allegedly identical specifications; storage, networking, extensions, configuration access, failover, support, and platform limits can still differ.
- The reported reliability and maintenance burden are a skilled operator's self-report without availability measurements, full incident accounting, labor valuation, recovery results, or a matched managed-service comparison. They support feasibility for this case, not the conclusion that self-hosting is right for nearly everyone.
- The parameter values are starting points rather than universal production settings. PostgreSQL version, workload, connection count, query concurrency, storage, durability requirements, and available memory must govern configuration.

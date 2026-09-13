---
title: "AWS costs every programmer should know"
type: source
tags: [aws, cloud-cost, infrastructure, reference-numbers]
date: 2026-03-30
source_file: /mnt/ken_personal_wiki/Articles/AWS costs every programmer should know.md
---

## Summary
The article gives order-of-magnitude reference costs for [[AWS]] compute, memory, storage, and bandwidth so programmers can reject obviously unaffordable architecture ideas before doing detailed budget work. It emphasizes relative scale rather than exact estimates: reservations can materially lower compute and RAM cost, S3 storage can be cheap while requests are expensive, and data transfer becomes important for user-facing or replicated systems. Two referenced chart images were not available at the local paths in the source tree, so their visual details were not ingested.

## Key Claims
- [[CloudCostOptimization]] starts with architectural sanity checks: a design should be tested against rough per-vCPU, per-GB-memory, storage, and transfer costs before scale makes the bill painful.
- One modern AWS vCPU is framed as roughly $58 per month on demand in eu-west-1, falling to about $43 with a 1-year convertible reservation and $30 with either a 3-year convertible reservation or estimated spot pricing.
- RAM is much more expensive than durable storage in the article's reference table: about $10 per GB-month on EC2 versus roughly $0.11 for SSD, $0.05 for hard disk, $0.02 for S3, and $0.004 for S3 Glacier.
- Storage architecture must include access patterns, because in-memory databases also require always-on compute and S3-heavy workloads can be dominated by request costs rather than stored bytes.
- Bandwidth is a meaningful design variable: the article lists 1GB transfer costs from $0 inside one availability zone to $0.01 between availability zones, about $0.05-$0.08 to the internet, and higher APAC cross-region costs than EU/US.
- AWS discounts, reservations, and spot pricing can change the practical economics enough that the numbers should be treated as scale intuition, not a final budget.

## Key Quotes
> "Those numbers are not meant for accurate budget estimation." - the author frames the tables as design-intuition references.

> "consider the orders of magnitude and relative values rather than the absolute values." - the source's main caution about pricing interpretation.

## Connections
- [[AWS]] - cloud provider whose EC2, storage, S3, Glacier, availability-zone, region, and internet-transfer costs are summarized.
- [[CloudCostOptimization]] - central design practice supported by the article's cost-reference tables.
- [[TechnologyStackComplexity]] - memory-first, S3-heavy, and cross-region designs can look simple architecturally while hiding cost complexity.

## Contradictions
- No direct contradictions found. The article complements the existing Vercel-to-AWS/Cloudflare migration note by adding provider-level unit-cost intuition, but its exact prices are source-date-specific and region-specific.

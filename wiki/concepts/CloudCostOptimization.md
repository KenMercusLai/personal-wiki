---
title: "Cloud Cost Optimization"
type: concept
tags: [cloud, cost, deployment, infrastructure]
sources:
  - wo-ba-wang-zhan-qian-yi-dao-cf-sheng-le-ji-wan-kuai
last_updated: 2026-09-12
knowledge_schema: synthesis-v1
---

## Definition
[[CloudCostOptimization]] is the practice of changing infrastructure choices, service boundaries, and deployment models to reduce cloud spending while preserving acceptable product behavior and operations effort.

## Current Synthesis
The source presents cost optimization as a practical response to a bill shock rather than an abstract FinOps exercise. The author first identifies Vercel's metered cost centers, then chooses alternatives that fit the project's tolerance for operations work: EC2 with PM2 or Docker when self-management is acceptable, and Cloudflare Pages when a low-cost hosted platform is preferred.

The broader lesson is that cost reduction can involve many layers at once. Compute moves from Vercel serverless functions to EC2 processes, containers, or Cloudflare edge; static and full-stack hosting moves to Pages; DNS and security consolidate under Cloudflare; object storage can move to R2; and database choices may shift toward D1 or edge-compatible Postgres clients.

## Key Claims
- Cloud bills can grow through many small metered features, not only base hosting fees.
- Convenience platforms trade operations effort for higher and sometimes less predictable cost.
- Self-hosting can lower direct platform spend but increases responsibility for process management, reverse proxying, TLS, and maintenance.
- Cloudflare can reduce cost by bundling low-cost hosting, DNS, security, object storage, workers, and database options.
- Compatibility and migration effort must be counted as part of the cost decision.

## Evidence
- Bill pressure: [[wo-ba-wang-zhan-qian-yi-dao-cf-sheng-le-ji-wan-kuai]] reports more than $5,000 in monthly Vercel spend for an AI search project.
- Metered components: [[wo-ba-wang-zhan-qian-yi-dao-cf-sheng-le-ji-wan-kuai]] names serverless function billing, analytics, storage, image optimization, and paid team use.
- Self-hosting tradeoff: [[wo-ba-wang-zhan-qian-yi-dao-cf-sheng-le-ji-wan-kuai]] shows the PM2 and Docker paths require Nginx, DNS, and Certbot configuration.
- Cloudflare substitution: [[wo-ba-wang-zhan-qian-yi-dao-cf-sheng-le-ji-wan-kuai]] lists Pages, Workers, DNS, D1, and R2 as low-cost services for small sites.
- Migration cost: [[wo-ba-wang-zhan-qian-yi-dao-cf-sheng-le-ji-wan-kuai]] details changes to database clients and Node API usage required for Cloudflare Pages.

## Counterevidence & Qualifications
The source emphasizes cost savings for a small independent web product. It does not quantify labor cost, reliability risk, support needs, compliance needs, or the value of Vercel's integrated workflow for teams with different constraints.

## What Changed
- Created the concept page for cloud-cost optimization grounded in a Vercel-to-AWS/Cloudflare migration.

## Related Concepts
- [[NextJSDeployment]] - deployment model is the main lever used to reduce cost in the source.
- [[EdgeRuntime]] - Cloudflare's lower-cost path has runtime compatibility costs.
- [[InferenceLoadBalancing]] - both address infrastructure efficiency, but this page focuses on cloud spend rather than inference routing.

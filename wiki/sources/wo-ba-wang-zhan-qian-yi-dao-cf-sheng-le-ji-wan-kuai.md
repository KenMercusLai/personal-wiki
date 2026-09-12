---
title: "我把网站迁移到 cf，省了几万块"
type: source
tags: [cloudflare, vercel, nextjs, deployment, cost-optimization]
date: 2026-03-18
source_file: /mnt/ken_personal_wiki/Articles/我把网站迁移到 cf，省了几万块.md
---

## Summary
idoubi describes moving a high-traffic Next.js project from Vercel to AWS and Cloudflare after Vercel monthly costs reportedly reached more than $5,000. The article compares Vercel's convenience with its metered-cost exposure, then walks through three alternatives: PM2 on an EC2 server, Docker on a server, and Cloudflare Pages with `@cloudflare/next-on-pages`. It emphasizes that Cloudflare can sharply reduce hosting, DNS, security, database, and object-storage costs for small web products, but requires edge-runtime compatibility work.

## Key Claims
- [[Vercel]] is attractive for [[NextJS]] projects because it combines GitHub CI/CD, preview deployments, generated subdomains, logs, analytics, environment variables, firewall controls, and framework-native support.
- Vercel's convenience can become expensive when serverless function time, analytics, storage, image optimization, and team features are billed separately.
- [[NextJSDeployment]] can be moved from Vercel to self-managed PM2 or Docker deployments on [[AWS]] EC2 when lower cost is worth additional operations work.
- [[Cloudflare]] Pages can host Next.js projects at low cost, but [[EdgeRuntime]] constraints require route/page runtime declarations and replacement of incompatible Node.js APIs or libraries.
- [[CloudCostOptimization]] is not only a provider switch; it also involves choosing where DNS, security, compute, database, and object storage belong.

## Key Quotes
> "一个月给我干到了 5000 多刀的支出" — the author frames the migration as a response to a surprisingly high Vercel bill.

> "关键要考虑两点：服务费用和运维复杂度。" — the article summarizes the deployment-choice tradeoff as cost versus operational complexity.

> "只支持 edge 运行时" — the author highlights Cloudflare Pages' main Next.js compatibility constraint.

## Connections
- [[Idoubi]] — author of the migration case study.
- [[Vercel]] — original hosting platform whose cost triggered the migration.
- [[Cloudflare]] — target platform used for Pages, DNS, security, Workers, D1, and R2.
- [[AWS]] — self-hosting option used through EC2 and compared with Vercel's underlying infrastructure.
- [[NextJS]] — application framework whose deployment choices structure the article.
- [[NextJSDeployment]] — main technical workflow described by the source.
- [[CloudCostOptimization]] — central reason for the migration and service substitution.
- [[EdgeRuntime]] — compatibility boundary for Cloudflare-hosted Next.js routes and pages.

## Contradictions
- None identified. The article is a practical migration report; pricing, product capabilities, and compatibility details may have changed after the source date.

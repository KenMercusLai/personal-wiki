---
title: "Next.js Deployment"
type: concept
tags: [nextjs, deployment, hosting, web-development]
sources:
  - wo-ba-wang-zhan-qian-yi-dao-cf-sheng-le-ji-wan-kuai
last_updated: 2026-09-12
knowledge_schema: synthesis-v1
---

## Definition
[[NextJSDeployment]] is the process of building, hosting, and operating a [[NextJS]] application across managed platforms, self-managed servers, containers, or edge platforms.

## Current Synthesis
The source frames Next.js deployment as a tradeoff between platform convenience, operating burden, runtime compatibility, and cost. Vercel offers the smoothest integrated path, but the author treats that convenience as expensive once traffic and feature usage grow. Self-hosting on AWS EC2 with PM2 or Docker gives more cost control but requires server administration, reverse proxying, DNS, and HTTPS setup.

Cloudflare Pages provides a low-cost managed alternative but changes the runtime contract. Instead of simply moving the same Node.js application, the developer must use `@cloudflare/next-on-pages`, configure Wrangler, declare edge runtime for routes and pages, and replace dependencies that rely on unsupported Node.js APIs.

## Key Claims
- The easiest deployment path is not necessarily the cheapest path once traffic and metered features grow.
- Self-hosted PM2 deployment is simple and lightweight but moves operations work onto the developer.
- Docker deployment improves isolation and portability at the cost of image-building and container-management complexity.
- Cloudflare Pages can reduce hosting cost while preserving managed deployment, but it imposes edge-runtime constraints.
- Database and library compatibility are part of deployment design, not afterthoughts.

## Evidence
- Vercel workflow: [[wo-ba-wang-zhan-qian-yi-dao-cf-sheng-le-ji-wan-kuai]] lists Vercel's GitHub CI/CD, previews, logs, analytics, and Next.js ecosystem support.
- PM2 workflow: [[wo-ba-wang-zhan-qian-yi-dao-cf-sheng-le-ji-wan-kuai]] deploys a built Next.js app with PM2, Nginx, DNS A records, and Certbot.
- Docker workflow: [[wo-ba-wang-zhan-qian-yi-dao-cf-sheng-le-ji-wan-kuai]] uses standalone output, a multi-stage Dockerfile, `.dockerignore`, and localhost port mapping.
- Cloudflare workflow: [[wo-ba-wang-zhan-qian-yi-dao-cf-sheng-le-ji-wan-kuai]] configures `@cloudflare/next-on-pages`, `wrangler.toml`, and Cloudflare Pages deployment.
- Compatibility work: [[wo-ba-wang-zhan-qian-yi-dao-cf-sheng-le-ji-wan-kuai]] replaces `pg`, `fs`, `http`, and Axios-dependent code paths for edge runtime.

## Counterevidence & Qualifications
The source is a migration walkthrough for one project, not a benchmark or universal hosting rule. A different workload may justify Vercel's premium, use managed Kubernetes, or avoid Cloudflare if edge-runtime rewrites are too costly.

## What Changed
- Created the concept page for Next.js deployment as a multi-option infrastructure tradeoff.

## Related Concepts
- [[CloudCostOptimization]] - deployment choice is driven by the source's cost-reduction goal.
- [[EdgeRuntime]] - Cloudflare Pages deployment depends on edge-runtime compatibility.
- [[PrivateDataChatbot]] - both concern full-stack application deployment, though this page focuses on hosting rather than AI retrieval architecture.

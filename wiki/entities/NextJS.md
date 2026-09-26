---
title: "Next.js"
type: entity
tags: [framework, react, web-development, deployment]
sources:
  - wo-ba-wang-zhan-qian-yi-dao-cf-sheng-le-ji-wan-kuai
  - blog-innei-lobehub-performance-and-dx-optimization
last_updated: 2026-09-25
knowledge_schema: synthesis-v1
---

## Overview
[[NextJS]] is the full-stack web framework whose deployment options are compared in the source.

## Current Profile
The deployment source treats Next.js as the framework behind the author's web products and as the reason Vercel is initially attractive. Its migration shows that Next.js can run on several infrastructure models, but each model changes the required build output, runtime assumptions, and operational responsibilities. The LobeHub source adds a development-workstation boundary: its author reports a Next.js server using more than 10 GB and is investigating Vite as a lower-memory replacement, but the migration is not complete.

## Key Characteristics
- Has first-class perceived support on Vercel through framework integration and templates.
- Can be self-hosted on a server using PM2 after building with `pnpm build`.
- Can be containerized with standalone output and a production Dockerfile.
- Can run on Cloudflare Pages when adapted for edge runtime and `@cloudflare/next-on-pages`.
- Can impose substantial development-server memory cost in the LobeHub codebase, motivating an exploratory migration rather than establishing a universal framework benchmark.

## Evidence
- Vercel support: [[wo-ba-wang-zhan-qian-yi-dao-cf-sheng-le-ji-wan-kuai]] says Vercel and Next.js belong to the same company and that Vercel has strong Next.js templates and support.
- PM2 deployment: [[wo-ba-wang-zhan-qian-yi-dao-cf-sheng-le-ji-wan-kuai]] gives `pnpm install`, `pnpm build`, and `pm2 start pnpm -- start` steps.
- Docker deployment: [[wo-ba-wang-zhan-qian-yi-dao-cf-sheng-le-ji-wan-kuai]] sets `output: "standalone"` and copies `.next/standalone` into a Node Alpine image.
- Cloudflare deployment: [[wo-ba-wang-zhan-qian-yi-dao-cf-sheng-le-ji-wan-kuai]] configures `@cloudflare/next-on-pages`, `wrangler.toml`, and `export const runtime = "edge"`.
- Development footprint: [[blog-innei-lobehub-performance-and-dx-optimization]] reports more than 10 GB for LobeHub's current Next.js server and a little above 1 GB for an experimental Vite configuration.

## Qualifications
The sources describe practitioner-specific deployment paths and one preliminary development-memory comparison. They should not be treated as complete Next.js documentation, a guarantee that all features work equally across platforms, or a controlled framework benchmark. Project size, configuration, plugins, cache state, operating system, and workload can dominate memory use, while the proposed LobeHub migration may reveal compatibility and engineering costs not captured by the experiment.

## What Changed
- Created the Next.js entity profile around deployment portability and runtime constraints.
- Added LobeHub's development-memory concern and explicitly kept the Vite migration provisional.

## Relationships
- [[Vercel]] - Vercel is the most integrated deployment platform in the article.
- [[Cloudflare]] - Cloudflare Pages is a low-cost edge-hosting target for Next.js.
- [[AWS]] - AWS EC2 supports the source's self-hosted Next.js examples.
- [[NextJSDeployment]] - deployment tradeoffs are the source's main treatment of Next.js.
- [[DeveloperExperience]] - local server memory determines which contributor hardware can run the project comfortably.
- [[LobeHub]] - application evaluating a migration away from Next.js in the source.

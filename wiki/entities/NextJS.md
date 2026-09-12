---
title: "Next.js"
type: entity
tags: [framework, react, web-development, deployment]
sources:
  - wo-ba-wang-zhan-qian-yi-dao-cf-sheng-le-ji-wan-kuai
last_updated: 2026-09-12
knowledge_schema: synthesis-v1
---

## Overview
[[NextJS]] is the full-stack web framework whose deployment options are compared in the source.

## Current Profile
The article treats Next.js as the framework behind the author's web products and as the reason Vercel is initially attractive. The migration shows that Next.js can run on several infrastructure models, but each model changes the required build output, runtime assumptions, and operational responsibilities.

## Key Characteristics
- Has first-class perceived support on Vercel through framework integration and templates.
- Can be self-hosted on a server using PM2 after building with `pnpm build`.
- Can be containerized with standalone output and a production Dockerfile.
- Can run on Cloudflare Pages when adapted for edge runtime and `@cloudflare/next-on-pages`.

## Evidence
- Vercel support: [[wo-ba-wang-zhan-qian-yi-dao-cf-sheng-le-ji-wan-kuai]] says Vercel and Next.js belong to the same company and that Vercel has strong Next.js templates and support.
- PM2 deployment: [[wo-ba-wang-zhan-qian-yi-dao-cf-sheng-le-ji-wan-kuai]] gives `pnpm install`, `pnpm build`, and `pm2 start pnpm -- start` steps.
- Docker deployment: [[wo-ba-wang-zhan-qian-yi-dao-cf-sheng-le-ji-wan-kuai]] sets `output: "standalone"` and copies `.next/standalone` into a Node Alpine image.
- Cloudflare deployment: [[wo-ba-wang-zhan-qian-yi-dao-cf-sheng-le-ji-wan-kuai]] configures `@cloudflare/next-on-pages`, `wrangler.toml`, and `export const runtime = "edge"`.

## Qualifications
The source describes one practitioner's deployment paths. It should not be treated as complete Next.js hosting documentation or a guarantee that all Next.js features work equally across platforms.

## What Changed
- Created the Next.js entity profile around deployment portability and runtime constraints.

## Relationships
- [[Vercel]] - Vercel is the most integrated deployment platform in the article.
- [[Cloudflare]] - Cloudflare Pages is a low-cost edge-hosting target for Next.js.
- [[AWS]] - AWS EC2 supports the source's self-hosted Next.js examples.
- [[NextJSDeployment]] - deployment tradeoffs are the source's main treatment of Next.js.

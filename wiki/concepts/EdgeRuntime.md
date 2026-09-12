---
title: "Edge Runtime"
type: concept
tags: [edge, runtime, cloudflare, nextjs, compatibility]
sources:
  - wo-ba-wang-zhan-qian-yi-dao-cf-sheng-le-ji-wan-kuai
last_updated: 2026-09-12
knowledge_schema: synthesis-v1
---

## Definition
[[EdgeRuntime]] is a web-application execution environment optimized for edge platforms that supports web-standard APIs but does not fully support Node.js runtime APIs such as `fs` or `http`.

## Current Synthesis
The article treats edge runtime as the main technical constraint when moving Next.js from Vercel or a Node server to Cloudflare Pages. The application is not merely redeployed; route and page files must opt into edge runtime, database clients must be compatible with edge execution, and libraries that depend on Node-specific APIs must be replaced or rewritten around `fetch` and other web APIs.

This makes edge runtime both an enabler and a constraint. It enables low-cost managed deployment on Cloudflare's edge platform, but can force code changes in data access, local-file reads, authentication packages, HTTP clients, and any dependency that assumes a traditional Node process.

## Key Claims
- Edge runtime compatibility is a prerequisite for Cloudflare-hosted Next.js applications in the source.
- Node-oriented database clients such as `pg` may need replacement with edge-compatible clients.
- Dependencies on `fs`, `http`, or libraries built on those APIs can block deployment.
- Rewriting Node-specific code toward `fetch` and remote resources can make an application portable to edge environments.
- Edge constraints should be evaluated before choosing Cloudflare Pages as a cost-saving target.

## Evidence
- Runtime declaration: [[wo-ba-wang-zhan-qian-yi-dao-cf-sheng-le-ji-wan-kuai]] says each relevant `route.ts` and `page.tsx` file needs `export const runtime = "edge"`.
- Database clients: [[wo-ba-wang-zhan-qian-yi-dao-cf-sheng-le-ji-wan-kuai]] replaces `pg` with Neon for native Postgres and uses `@supabase/supabase-js` for Supabase.
- File APIs: [[wo-ba-wang-zhan-qian-yi-dao-cf-sheng-le-ji-wan-kuai]] changes local `fs.readFileSync` logic to fetch remote files.
- HTTP libraries: [[wo-ba-wang-zhan-qian-yi-dao-cf-sheng-le-ji-wan-kuai]] describes modifying a Google One Tap package because Axios depended on unsupported HTTP APIs.

## Counterevidence & Qualifications
The source focuses on Cloudflare Pages and the author's dependency set. Other edge platforms, Next.js versions, compatibility flags, adapters, or package versions may support different subsets of functionality.

## What Changed
- Created the edge-runtime concept page as a deployment-compatibility constraint.

## Related Concepts
- [[NextJSDeployment]] - edge runtime determines whether a Next.js project can deploy cleanly to Cloudflare Pages.
- [[CloudCostOptimization]] - edge compatibility is one migration cost of using Cloudflare to reduce spend.
- [[HTTP]] - edge runtime favors web-standard request APIs, though this page focuses on application runtime rather than protocol evolution.

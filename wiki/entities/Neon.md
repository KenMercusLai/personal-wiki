---
title: "Neon"
type: entity
tags: [database, postgres, serverless, edge-runtime]
sources:
  - wo-ba-wang-zhan-qian-yi-dao-cf-sheng-le-ji-wan-kuai
last_updated: 2026-09-12
knowledge_schema: synthesis-v1
---

## Overview
[[Neon]] is mentioned in the source as an edge-runtime-compatible Postgres client option for Cloudflare-hosted Next.js applications.

## Current Profile
The article introduces Neon as a replacement for the Node-oriented `pg` package when a Next.js application moves to Cloudflare Pages. In the source's framing, Neon works for native Postgres access in edge runtime, but does not replace Supabase's own client when the application uses Supabase.

## Key Characteristics
- Provides a serverless Postgres access pattern compatible with edge runtime.
- Replaces `pg` in the source's Cloudflare migration example.
- Uses tagged SQL queries through `@neondatabase/serverless`.
- Does not cover Supabase-backed projects in the author's account.

## Evidence
- Edge-compatible client: [[wo-ba-wang-zhan-qian-yi-dao-cf-sheng-le-ji-wan-kuai]] recommends replacing `pg` with `neon` from `@neondatabase/serverless`.
- Query example: [[wo-ba-wang-zhan-qian-yi-dao-cf-sheng-le-ji-wan-kuai]] shows Neon executing `SELECT version()` through `DATABASE_URL`.
- Scope limit: [[wo-ba-wang-zhan-qian-yi-dao-cf-sheng-le-ji-wan-kuai]] says the Neon approach works for native Postgres but not Supabase.

## Qualifications
The source treats Neon as a practical migration component, not as a broader database product review.

## What Changed
- Created the Neon entity profile as an edge-compatible Postgres access option.

## Relationships
- [[EdgeRuntime]] - Neon is introduced because edge runtime cannot use the normal `pg` client.
- [[Supabase]] - Neon is contrasted with Supabase's official client path.
- [[NextJS]] - Neon is used in a Cloudflare-hosted Next.js database-access example.
- [[Cloudflare]] - Cloudflare Pages is the deployment target requiring the database-client change.

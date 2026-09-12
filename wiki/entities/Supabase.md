---
title: "Supabase"
type: entity
tags: [database, backend, postgres, edge-runtime]
sources:
  - wo-ba-wang-zhan-qian-yi-dao-cf-sheng-le-ji-wan-kuai
last_updated: 2026-09-12
knowledge_schema: synthesis-v1
---

## Overview
[[Supabase]] appears in the source as a Postgres-backed service whose official JavaScript client can run in edge-runtime environments, but with some query limitations in the author's migration experience.

## Current Profile
The source mentions Supabase while discussing the database-client changes required for Cloudflare-hosted Next.js applications. The author says the normal `pg` package is incompatible with edge runtime, Neon can replace it for native Postgres, and Supabase projects need `@supabase/supabase-js` instead because Neon is not compatible with Supabase.

## Key Characteristics
- Represents a hosted Postgres-style backend used by some Next.js projects.
- Needs its official JavaScript client in the source's Cloudflare edge-runtime path.
- Is distinguished from generic Postgres because Neon is described as incompatible with Supabase.
- May require application-query changes when moving to Cloudflare.

## Evidence
- Client replacement: [[wo-ba-wang-zhan-qian-yi-dao-cf-sheng-le-ji-wan-kuai]] says `pg` is not supported in edge runtime and must be replaced.
- Supabase-specific path: [[wo-ba-wang-zhan-qian-yi-dao-cf-sheng-le-ji-wan-kuai]] uses `createClient` from `@supabase/supabase-js` for Supabase-backed projects.
- Compatibility boundary: [[wo-ba-wang-zhan-qian-yi-dao-cf-sheng-le-ji-wan-kuai]] says Neon does not work with Supabase.
- Query limitation: [[wo-ba-wang-zhan-qian-yi-dao-cf-sheng-le-ji-wan-kuai]] reports trouble with `select * from xxx order by random()` through the Supabase client.

## Qualifications
This is a narrow migration note rather than a full Supabase evaluation. The query behavior and client capabilities may vary by version and implementation.

## What Changed
- Created the Supabase entity profile as a database dependency affected by edge-runtime migration.

## Relationships
- [[EdgeRuntime]] - Supabase is discussed because Cloudflare edge runtime constrains database clients.
- [[NextJS]] - Supabase-backed Next.js projects may need client changes before Cloudflare deployment.
- [[Cloudflare]] - Cloudflare Pages is the target environment that exposes the compatibility issue.
- [[CloudCostOptimization]] - Supabase is compared indirectly with Cloudflare D1 as a possible cost target.

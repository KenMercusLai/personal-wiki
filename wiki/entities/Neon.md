---
title: "Neon"
type: entity
tags: [database, postgres, serverless, edge-runtime]
sources:
  - wo-ba-wang-zhan-qian-yi-dao-cf-sheng-le-ji-wan-kuai
  - training-100x-cheaper-retrieval-models-neon-and-castform
  - p4385-pandis
last_updated: 2026-10-18
knowledge_schema: synthesis-v1
---

## Overview
[[Neon]] is a serverless Postgres platform and open-source disaggregated database architecture represented through edge-runtime access, elastic retrieval-agent workloads, and the storage foundation beneath [[Lakebase]].

## Current Profile
One migration article introduces Neon as a replacement for the Node-oriented `pg` package when a Next.js application moves to Cloudflare Pages. The joint case study with [[Castform]] uses Neon more broadly: raw documents remain in Postgres, Lakebase text and vector search form one hybrid tool across synthetic-data generation, reinforcement-learning rollouts, and production inference, and dynamic compute absorbs bursty parallel searches.

The Lakebase paper supplies the underlying systems model. PostgreSQL computes cache pages locally while Safekeepers quorum-replicate WAL, Pageservers reconstruct versioned pages, and object storage preserves durable PostgreSQL-format layers. NeonVM adds in-place CPU, memory, and disk scaling inside Kubernetes-hosted QEMU/KVM virtual machines. These mechanisms turn previously proposed database branches and time travel into measured production primitives, while Databricks-specific governance, Lakehouse integration, and service claims belong to Lakebase rather than Neon alone.

## Key Characteristics
- Provides a serverless Postgres access pattern compatible with edge runtime.
- Replaces `pg` in the source's Cloudflare migration example.
- Combines corpus storage with text and vector search across training and inference.
- Dynamically allocates compute for bursty parallel retrieval rollouts.
- Offers branching and time travel as proposed primitives for isolated stateful-agent environments.
- Supplies Safekeeper, Pageserver, timeline, and NeonVM foundations used by Lakebase for disaggregated durability, branching, and elastic compute.

## Evidence
- Edge-compatible client: [[wo-ba-wang-zhan-qian-yi-dao-cf-sheng-le-ji-wan-kuai]] recommends replacing `pg` with `neon` from `@neondatabase/serverless`.
- Query example: [[wo-ba-wang-zhan-qian-yi-dao-cf-sheng-le-ji-wan-kuai]] shows Neon executing `SELECT version()` through `DATABASE_URL`.
- Scope limit: [[wo-ba-wang-zhan-qian-yi-dao-cf-sheng-le-ji-wan-kuai]] says the Neon approach works for native Postgres but not Supabase.
- Shared retrieval substrate: [[training-100x-cheaper-retrieval-models-neon-and-castform]] uses `lakebase_text` and `lakebase_vector` during task generation, reinforcement-learning rollouts, and production inference.
- Elastic workload handling: [[training-100x-cheaper-retrieval-models-neon-and-castform]] shows a bursty CPU trace and attributes peak absorption and idle scale-down to dynamic compute allocation.
- Stateful isolation path: [[training-100x-cheaper-retrieval-models-neon-and-castform]] proposes per-rollout branches, resets, and time-travel inspection for agents that modify data.
- Storage architecture: [[p4385-pandis]] describes quorum-replicated Safekeepers, versioned Pageserver layers, object-store persistence, and timeline-based branching built with Neon engineers and the open-source Neon community.
- Elastic compute: [[p4385-pandis]] describes NeonVM in-place vertical scaling and warm-pool startup, with displayed production p95 below 500 ms.

## Qualifications
All three accounts are practitioner, vendor, or vendor-authored research sources rather than independent platform evaluations. The edge-runtime article is time-sensitive and excludes Supabase. The Castform case study shows only one CPU trace and no controlled latency or cost comparison. The Lakebase paper validates related mechanisms more deeply, but its production and benchmark claims concern a Databricks service, anonymize comparison systems, and do not isolate which outcomes transfer to Neon deployments.

## What Changed
- Grounded Neon's branching and elastic-compute role in the Safekeeper, Pageserver, timeline, and NeonVM architecture used by Lakebase.
- Distinguished Neon architectural foundations from Databricks-specific service, governance, and Lakehouse claims.

## Relationships
- [[EdgeRuntime]] - Neon is introduced because edge runtime cannot use the normal `pg` client.
- [[Supabase]] - Neon is contrasted with Supabase's official client path.
- [[NextJS]] - Neon is used in a Cloudflare-hosted Next.js database-access example.
- [[Cloudflare]] - Cloudflare Pages is the deployment target requiring the database-client change.
- [[Castform]] - uses Neon as the database and search environment for post-training retrieval models.
- [[AgenticRAG]] - generates the repeated, bursty search workload described in the joint case study.
- [[ReinforcementLearning]] - creates parallel rollouts that repeatedly query the Neon environment.
- [[Lakebase]] - Databricks service built with Neon architecture and engineering contributions.
- [[DisaggregatedTransactionalDatabase]] - describes the separation implemented through computes, Safekeepers, Pageservers, and object storage.
- [[DatabaseBranching]] - is implemented with parent timelines and branch LSNs.

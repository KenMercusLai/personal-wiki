---
title: "Origin"
type: entity
tags: [git, developer-platform, cursor, infrastructure]
sources:
  - ren-yi-gui-mo-de-git
last_updated: 2026-10-09
knowledge_schema: synthesis-v1
---

## Overview
[[Origin]] is Cursor's Git hosting platform, presented as a high-reliability, high-scale home for Git protocol traffic and repository-backed web, API, and agent operations.

## Current Profile
Origin is the product layer built on [[Continuity]]. The source positions it as Cursor's response to growth in agent-generated code, pull requests, continuous integration, and large numbers of small repositories, while also targeting read-heavy monorepositories that may need many replicas.

The launch article emphasizes migration ease, reliability, performance, and scale rather than documenting Origin's user-facing feature set, availability terms, pricing, security model, regional deployment, or migration procedure. It explicitly presents Origin as a production commitment rather than an experiment, but the evidence remains Cursor's own announcement.

## Key Characteristics
- Uses Continuity as its Git storage foundation.
- Serves clone and fetch traffic plus repository-level web, REST API, and agent operations.
- Targets both high-traffic monorepositories and large populations of small or ephemeral agent-created repositories.
- Is positioned around reliability, performance, elastic scale, and low-friction migration.
- Is introduced as a production platform, although public operational and commercial details are absent from the supplied source.

## Evidence
- Product foundation: [[ren-yi-gui-mo-de-git]] introduces Origin after describing Continuity's WAL-backed storage architecture.
- Workload scope: [[ren-yi-gui-mo-de-git]] connects the platform to clones, fetches, web UI, REST APIs, agent interfaces, pull requests, and CI.
- Market position: [[ren-yi-gui-mo-de-git]] says Cursor is focusing on a smooth migration path toward greater reliability, performance, and scale.

## Qualifications
The supplied article is an architecture-led launch narrative, not a product specification or independent review. It does not establish current availability, customer adoption, service guarantees, security controls, pricing, migration compatibility, or observed production outcomes. Its performance evidence concerns Continuity tests and should not automatically be treated as end-to-end Origin performance.

## What Changed
- Created the entity profile for Cursor's Git hosting platform.

## Relationships
- [[Cursor]] - company developing and presenting Origin.
- [[Continuity]] - storage system underlying Origin.
- [[GitHostingArchitecture]] - architecture domain in which Origin is positioned.
- [[GitHub]] - established centralized Git host and architectural comparison in the source.

---
title: "Rob Horn"
type: entity
tags: [software-architecture, legacy-modernization]
sources:
  - blog-ian-cartwright-rob-horn-james-lewis-martinfowler-com-legacy-mimic
  - blog-ian-cartwright-rob-horn-james-lewis-martinfowler-com-divert-the-flow
  - blog-ian-cartwright-rob-horn-james-lewis-martinfowler-com-transitional-architecture
last_updated: 2026-09-25
knowledge_schema: synthesis-v1
---

## Overview
[[RobHorn]] is a coauthor of legacy-displacement pattern articles on Martin Fowler's site.

## Current Profile
In the ingested sources, Horn is represented through architecture guidance for incremental legacy replacement. The material spans temporary mimic components that preserve legacy-facing contracts, an aggregator-first strategy that redirects reporting toward better source data, and a staged storefront example where bridge components are removed as routing, reporting, and processing ownership moves.

## Key Characteristics
- Coauthor of legacy-displacement pattern articles.
- Associated in this wiki with transitional architecture and migration sequencing.
- Explains old/new system coexistence through service-providing and service-consuming mimic examples.
- Treats source mapping, user needs, validation, and monitoring as part of architecture migration.
- Frames temporary construction as justified when earlier value and reduced risk outweigh its full lifecycle cost.

## Evidence
- Authorship: [[blog-ian-cartwright-rob-horn-james-lewis-martinfowler-com-legacy-mimic]] lists Rob Horn as an author.
- Migration framing: [[blog-ian-cartwright-rob-horn-james-lewis-martinfowler-com-legacy-mimic]] says incremental replacement cannot cleanly isolate old and new worlds.
- Pattern examples: [[blog-ian-cartwright-rob-horn-james-lewis-martinfowler-com-legacy-mimic]] uses event interception and metrics replication as mimic examples.
- Sequencing alternative: [[blog-ian-cartwright-rob-horn-james-lewis-martinfowler-com-divert-the-flow]] compares replacing a critical aggregator first with supporting it through mimic feeds until later.
- Operational evidence: [[blog-ian-cartwright-rob-horn-james-lewis-martinfowler-com-divert-the-flow]] recommends output reconciliation, staged cutover, and feed monitoring.
- Staged evolution: [[blog-ian-cartwright-rob-horn-james-lewis-martinfowler-com-transitional-architecture]] uses progressive routing and contract-specific adapters to decommission middleware before the whole legacy system is gone.

## Qualifications
This page only represents Horn as he appears in three ingested legacy-displacement pattern sources. It is not a full biography or outcome study.

## What Changed
- Added the transitional-architecture example's value test, staged routing, and bridge retirement.

## Relationships
- [[IanCartwright]] - coauthor of all three ingested pattern articles.
- [[JamesLewis]] - coauthor of all three ingested pattern articles.
- [[LegacyMimic]] - compatibility pattern described in one coauthored source.
- [[DivertTheFlow]] - migration strategy described in the newer source.
- [[TransitionalArchitecture]] - architecture context and lifecycle discipline shared across all three articles.

---
title: "Ian Cartwright"
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
[[IanCartwright]] is a coauthor of legacy-displacement pattern articles on Martin Fowler's site.

## Current Profile
In the ingested sources, Cartwright contributes to practitioner guidance on incremental legacy displacement. [[LegacyMimic]] describes temporary compatibility for old/new coexistence, [[DivertTheFlow]] shows how replacing a cross-cutting [[CriticalAggregator]] early can release upstream systems from legacy data contracts, and [[TransitionalArchitecture]] supplies the cost-benefit and removal discipline for the bridge components between those states.

## Key Characteristics
- Coauthor of legacy-displacement pattern articles.
- Associated in this wiki with transitional architecture and legacy-system migration guidance.
- Presents architecture patterns through diagrams and examples rather than product-specific implementation detail.
- Connects migration sequencing to data provenance, output reconciliation, and operational monitoring.
- Treats decommissioning and removability as part of architecture design rather than post-migration cleanup.

## Evidence
- Authorship: [[blog-ian-cartwright-rob-horn-james-lewis-martinfowler-com-legacy-mimic]] lists Ian Cartwright as an author.
- Pattern focus: [[blog-ian-cartwright-rob-horn-james-lewis-martinfowler-com-legacy-mimic]] explains service-providing and service-consuming legacy mimics.
- Visual explanation: [[blog-ian-cartwright-rob-horn-james-lewis-martinfowler-com-legacy-mimic]] uses logistics-system diagrams to explain the migration sequence.
- Aggregator sequencing: [[blog-ian-cartwright-rob-horn-james-lewis-martinfowler-com-divert-the-flow]] contrasts early replacement with maintaining a legacy aggregator until later.
- Validation guidance: [[blog-ian-cartwright-rob-horn-james-lewis-martinfowler-com-divert-the-flow]] joins source mapping, parallel running, staged cutover, and monitoring.
- Transition lifecycle: [[blog-ian-cartwright-rob-horn-james-lewis-martinfowler-com-transitional-architecture]] compares early value and risk reduction with temporary cost, then removes bridge components as their dependencies disappear.

## Qualifications
This page only represents Cartwright as he appears in three ingested legacy-displacement pattern sources. It is not a full biography or independent evaluation of the patterns.

## What Changed
- Added transitional architecture's cost-benefit framing and dependency-ordered decommissioning.

## Relationships
- [[RobHorn]] - coauthor of all three ingested pattern articles.
- [[JamesLewis]] - coauthor of all three ingested pattern articles.
- [[LegacyMimic]] - temporary compatibility pattern described in one coauthored source.
- [[DivertTheFlow]] - aggregator-first strategy described in the newer source.
- [[TransitionalArchitecture]] - temporary bridgework and retirement discipline described in the newest source.
- [[LegacyDisplacement]] - modernization context shared by both articles.

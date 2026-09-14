---
title: "ZooKeeper"
type: entity
tags: [software, distributed-systems, coordination]
sources:
  - blog-mahesh-balakrishnan-42-things-i-learned-from-building-a-production-database
last_updated: 2026-09-14
knowledge_schema: synthesis-v1
---

## Overview
[[ZooKeeper]] appears in the wiki through Mahesh Balakrishnan's Delos essay as the incumbent coordination/storage infrastructure that [[Delos]] was replacing within [[Facebook]].

## Current Profile
The source does not explain ZooKeeper's architecture. It uses ZooKeeper as a reference point for the production role of Delos: Balakrishnan tells readers to think of Delos as Facebook's version of ZooKeeper and says Delos was replacing all Facebook uses of ZooKeeper as of the 2021 article.

## Key Characteristics
- Serves as the familiar reference system used to explain Delos' infrastructure role.
- Was important enough at Facebook that replacing its uses required a production storage-system project.
- Appears as an incumbent system rather than the article's design focus.

## Evidence
- Reference point: [[blog-mahesh-balakrishnan-42-things-i-learned-from-building-a-production-database]] compares Delos to Facebook's version of ZooKeeper.
- Replacement context: [[blog-mahesh-balakrishnan-42-things-i-learned-from-building-a-production-database]] says Delos was replacing all uses of ZooKeeper at Facebook.
- Scope limit: [[blog-mahesh-balakrishnan-42-things-i-learned-from-building-a-production-database]] does not elaborate ZooKeeper's own design.

## Qualifications
This entity is intentionally source-scoped. The wiki does not yet contain a primary ZooKeeper source, so the page should not be read as a complete technical profile.

## What Changed
- Created a source-scoped ZooKeeper entity so Delos' replacement relationship has a canonical target.

## Relationships
- [[Delos]] - replacement system for Facebook's ZooKeeper uses in the source.
- [[Facebook]] - organization where the Delos replacement effort occurred.
- [[ProductionInfrastructureLeadership]] - ZooKeeper is part of the internal ecosystem a production infrastructure team had to understand.

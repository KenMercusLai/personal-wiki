---
title: "MongoDB"
type: entity
tags: [database, backend, scalability]
sources:
  - building-a-shop-with-sub-second-page-loads-lessons-learned
last_updated: 2026-09-15
knowledge_schema: synthesis-v1
---

## Overview
[[MongoDB]] appears in the wiki as the primary database used in Baqend's Thinks webshop backend.

## Current Profile
The source uses MongoDB as the main data store in an ecommerce architecture built for short traffic spikes. It appears both in the static architecture description and in the load-test section, where Baqend ran MongoDB on two AWS t2.large instances while application servers handled incoming traffic through the CDN.

MongoDB also appears in a concrete payment bottleneck: the team changed stock updates from an optimistic `findAndModify` approach to partial update operations using `$inc`, after which the system reportedly handled the load with low request latency.

## Key Characteristics
- Primary database for the Thinks webshop in Baqend's stack.
- Ran as two t2.large AWS instances during the reported load test.
- Part of a horizontally scalable backend architecture fronted by CDN and stateless application servers.
- Stock-update implementation details affected payment-path performance.

## Evidence
- Stack role: [[building-a-shop-with-sub-second-page-loads-lessons-learned]] says MongoDB was the main database for the Thinks webshop.
- Load-test setup: [[building-a-shop-with-sub-second-page-loads-lessons-learned]] says MongoDB ran on two t2.large instances while 20 load machines simulated 200,000 users.
- Payment bottleneck: [[building-a-shop-with-sub-second-page-loads-lessons-learned]] says the team moved from `findAndModify`-based optimistic stock updates to partial update operations using `$inc`.

## Qualifications
The source is not a general MongoDB evaluation. It shows MongoDB inside one Baqend-managed ecommerce architecture and one payment-path optimization.

## What Changed
- Created the MongoDB entity page from the Thinks case study.

## Relationships
- [[Baqend]] - platform stack using MongoDB as primary storage.
- [[Thinks]] - webshop whose data was stored in MongoDB.
- [[WebPerformanceOptimization]] - database write paths can become backend-performance bottlenecks.
- [[Redis]] - complementary data system used for high-write-throughput Bloom-filter maintenance.

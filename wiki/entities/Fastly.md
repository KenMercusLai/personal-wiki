---
title: "Fastly"
type: entity
tags: [cdn, web-performance]
sources:
  - building-a-shop-with-sub-second-page-loads-lessons-learned
last_updated: 2026-09-15
knowledge_schema: synthesis-v1
---

## Overview
[[Fastly]] appears in the wiki as the CDN used by Baqend for the Thinks webshop performance case study.

## Current Profile
The source names Fastly as part of the network-performance strategy for Thinks. In the article's architecture, a CDN reduces user-to-cache distance, terminates nearby TCP/TLS connections, caches static and dynamic resources where possible, and can act as a load-balancing layer before application servers.

## Key Characteristics
- Used as the CDN in the Thinks webshop implementation.
- Helps reduce round-trip distance and connection setup costs for users.
- Participates in the cache hierarchy that lets Baqend serve dynamic web requests quickly.
- Supports the case study's reported high CDN cache-hit rate during the DHDL traffic spike.

## Evidence
- CDN choice: [[building-a-shop-with-sub-second-page-loads-lessons-learned]] says Thinks used the Fastly CDN.
- Cache-hit result: [[building-a-shop-with-sub-second-page-loads-lessons-learned]] reports a 98.5% CDN cache-hit rate during the DHDL airing.
- Load-test architecture: [[building-a-shop-with-sub-second-page-loads-lessons-learned]] shows load generators reaching the CDN before Baqend application servers, MongoDB, and Redis.

## Qualifications
The source does not evaluate Fastly against other CDNs; it uses Fastly as one component in Baqend's broader caching and backend architecture.

## What Changed
- Created the Fastly entity page from the Thinks case study.

## Relationships
- [[Baqend]] - uses Fastly as the CDN component in the source architecture.
- [[Thinks]] - webshop that used Fastly during the TV traffic spike.
- [[WebPerformanceOptimization]] - CDN placement is one network-latency lever.
- [[DynamicContentCaching]] - CDN caching works with Baqend's browser-cache freshness checks.

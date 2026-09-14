---
title: "Thinks"
type: entity
tags: [ecommerce, webshop, case-study]
sources:
  - building-a-shop-with-sub-second-page-loads-lessons-learned
last_updated: 2026-09-15
knowledge_schema: synthesis-v1
---

## Overview
[[Thinks]] is the webshop case study used by Baqend to show how an ecommerce site can remain fast during a high-visibility TV traffic spike.

## Current Profile
The source describes Thinks as a startup appearing on the German version of Shark Tank, DHDL, where TV exposure drove a sudden rush of shoppers to its Towell+ product. Baqend built the webshop to handle hundreds of thousands of visitors while keeping page loads below one second.

The reported production results are the page's main evidence: during the 30-minute airing, Thinks received millions of requests, hundreds of thousands of visitors, and tens of thousands of concurrent visitors while maintaining high CDN cache-hit rates and low server CPU load. The comparison screenshot claims several other shops from the same episode were down or much slower, making Thinks the article's contrast case for performance as conversion infrastructure.

## Key Characteristics
- Ecommerce webshop exposed to a short, intense burst of demand from TV coverage.
- Used Baqend, Fastly, browser caching, CDN caching, MongoDB, Redis, and stateless application servers.
- Reportedly sustained up to about 50,000 concurrent visitors and 20,000 requests per second.
- Kept page-load time below one second during the traffic spike.
- Reportedly converted at 7.8% while peer shops in the same episode were unavailable or slower.

## Evidence
- Traffic event: [[building-a-shop-with-sub-second-page-loads-lessons-learned]] says DHDL aired the Thinks pitch on September 6 with 2.7 million viewers.
- Production metrics: [[building-a-shop-with-sub-second-page-loads-lessons-learned]] reports 3.4 million requests, 300,000 visitors, up to 50,000 concurrent visitors, and up to 20,000 requests per second during the 30-minute airing.
- Performance metrics: [[building-a-shop-with-sub-second-page-loads-lessons-learned]] reports sub-second page loads, 98.5% CDN cache hit rate, 3% average server CPU load, and 7.8% conversion.
- Comparison screenshot: [[building-a-shop-with-sub-second-page-loads-lessons-learned]] shows Thinks as the only sub-second shop in a same-episode comparison where four other shops are marked down.

## Qualifications
The production metrics are reported by the vendor that built the platform, and the article does not provide raw logs or independent analytics exports. The case is still useful as a concrete architecture-and-load-testing narrative.

## What Changed
- Created the Thinks entity page from the Baqend performance case study.

## Relationships
- [[Baqend]] - platform that built and hosted the performance architecture.
- [[WebPerformanceOptimization]] - Thinks is the concrete ecommerce example.
- [[ProductPageOptimization]] - the webshop depends on fast product browsing during purchase intent.
- [[ConversionRateOptimization]] - the source ties sub-second load time to the reported 7.8% conversion rate.

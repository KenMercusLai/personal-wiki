---
title: "Frontera"
type: entity
tags: [software, web-scraping, crawl-frontier]
sources:
  - for-e-commerce-data-scientists-lessons-learned-scraping-100-billion-products-pages
last_updated: 2026-09-28
knowledge_schema: synthesis-v1
---

## Overview
[[Frontera]] is the open-source crawl frontier used in the source to illustrate coordination between product-discovery and product-extraction workers.

## Current Profile
The article presents Frontera as queueing infrastructure: discovery spiders traverse product categories and add product URLs, while extraction spiders consume those URLs and parse the heavier product pages. Although originally designed for [[Scrapy]], the source describes the frontier as framework-agnostic.

## Key Characteristics
- Coordinates URLs between discovery and extraction stages.
- Supports a distributed crawling architecture rather than serial request loops.
- Was originally associated with Scrapy but is described as usable independently.

## Evidence
- Pipeline role: [[for-e-commerce-data-scientists-lessons-learned-scraping-100-billion-products-pages]] uses a crawl frontier to queue discovered product URLs for extraction spiders.
- Scaling role: [[for-e-commerce-data-scientists-lessons-learned-scraping-100-billion-products-pages]] presents this separation as a way to allocate more capacity to slower extraction work.
- Compatibility: [[for-e-commerce-data-scientists-lessons-learned-scraping-100-billion-products-pages]] says Frontera was designed for Scrapy but is framework-agnostic.

## Qualifications
The source provides an architectural illustration rather than a performance comparison or current maintenance assessment. Its recommendation is historical, and current suitability would require checking supported backends, failure semantics, scheduling behavior, and project status.

## What Changed
- Created the entity profile around Frontera's discovery-to-extraction queueing role.

## Relationships
- [[Scrapy]] - framework for which Frontera was originally designed.
- [[Scrapinghub]] - organization identified with Frontera in the source.
- [[LargeScaleWebScraping]] - architectural context for its crawl-frontier role.

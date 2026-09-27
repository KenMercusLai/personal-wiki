---
title: "Scrapy"
type: entity
tags: [software, web-scraping, python]
sources:
  - for-e-commerce-data-scientists-lessons-learned-scraping-100-billion-products-pages
last_updated: 2026-09-28
knowledge_schema: synthesis-v1
---

## Overview
[[Scrapy]] is an open-source web-crawling framework identified in the source as a major part of [[Scrapinghub]]'s scraping ecosystem.

## Current Profile
The article names Scrapy as Scrapinghub's crawling framework and places it beside [[Frontera]], which was originally designed to provide crawl-frontier support for Scrapy while remaining framework-agnostic. The source does not explain Scrapy's API or compare it with alternatives.

## Key Characteristics
- Open-source framework for building web crawlers and extraction spiders.
- Maintained in the historical Scrapinghub ecosystem described by the article.
- Can be paired with a crawl frontier to separate URL discovery and extraction work.

## Evidence
- Ownership context: [[for-e-commerce-data-scientists-lessons-learned-scraping-100-billion-products-pages]] calls Scrapinghub the author of Scrapy.
- Architecture context: [[for-e-commerce-data-scientists-lessons-learned-scraping-100-billion-products-pages]] says Frontera was originally designed for Scrapy but can support other frameworks.
- Operational context: [[for-e-commerce-data-scientists-lessons-learned-scraping-100-billion-products-pages]] places configurable spiders inside a broader high-throughput, quality-monitored scraping system.

## Qualifications
The source makes broad popularity and robustness claims without comparative evidence and gives no implementation-level account of Scrapy. Tool status, stewardship, APIs, and ecosystem position are time-sensitive and require current documentation for present-day decisions.

## What Changed
- Created a bounded profile of Scrapy's role in the source's large-scale crawling stack.

## Relationships
- [[Scrapinghub]] - company identified as Scrapy's author in the source.
- [[Frontera]] - crawl frontier originally designed for use with Scrapy.
- [[LargeScaleWebScraping]] - operational setting in which Scrapy-based spiders are discussed.

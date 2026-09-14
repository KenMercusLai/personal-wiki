---
title: "Crawlee"
type: entity
tags: [web-scraping, browser-automation, crawling]
sources:
  - building-a-universal-ai-scraper
last_updated: 2026-09-15
knowledge_schema: synthesis-v1
---

## Overview
[[Crawlee]] appears in the wiki as the crawler library Tim Connors chose for his universal AI scraper prototype.

## Current Profile
The source presents Crawlee as backend crawling infrastructure that wraps Playwright and adds scraper-oriented conveniences. Connors values it for browser automation support, human-like scraping enhancements, and request-queue management that could matter if the scraper becomes a shared API.

## Key Characteristics
- Wraps Playwright for browser-based crawling.
- Adds scraper-specific ergonomics beyond direct browser automation.
- Includes request-queue support for managing crawl order.
- Is positioned as useful backend infrastructure even though the project was built in Next.js for possible frontend expansion.

## Evidence
- Playwright wrapper: [[building-a-universal-ai-scraper]] says Crawlee offers a wrapper around Playwright.
- Scraper ergonomics: [[building-a-universal-ai-scraper]] says Crawlee adds enhancements that make it easier to disguise the scraper as a human user.
- Queue support: [[building-a-universal-ai-scraper]] says Crawlee's request queue would help manage request order if the project were deployed for others.

## Qualifications
The source gives a practitioner's reasons for selecting Crawlee, but it does not compare Crawlee with other crawling libraries or evaluate its reliability, compliance controls, or anti-bot behavior.

## What Changed
- Created the entity profile for Crawlee's role in the AI scraper stack.

## Relationships
- [[Playwright]] - Crawlee wraps Playwright in the prototype.
- [[AIGuidedWebScraping]] - Crawlee supplies crawler infrastructure for the AI-guided scraper.
- [[WebScrapingProxyPool]] - both address operational scraping concerns, though at different layers.
- [[NextJS]] - Connors uses Next.js for the backend project while Crawlee handles crawling.

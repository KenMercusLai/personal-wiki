---
title: "Tim Connors"
type: entity
tags: [author, ai, web-scraping]
sources:
  - building-a-universal-ai-scraper
last_updated: 2026-09-15
knowledge_schema: synthesis-v1
---

## Overview
[[TimConnors]] appears in the wiki as the author and builder of the "Building a Universal AI Scraper" prototype.

## Current Profile
The source presents Tim Connors as a practitioner experimenting with AI-assisted browser scraping. He frames the project as work in progress, explains failed and successful approaches, shares implementation details around model choice and browser tooling, and later notes interest in productizing the scraper as an API.

## Key Characteristics
- Builds experimental AI tooling around web scraping and browser automation.
- Explains implementation tradeoffs through failed approaches, not only the final architecture.
- Uses model capability tiers pragmatically, assigning stronger models to harder selector and code-generation steps.
- Treats the scraper as potentially productizable infrastructure while still calling it fragile.

## Evidence
- Builder role: [[building-a-universal-ai-scraper]] says the author set out to build a universal scraper that navigates iteratively until it finds the target information.
- Failed approaches: [[building-a-universal-ai-scraper]] documents screenshot-plus-vision and full-HTML prompting before settling on hybrid ranked search.
- Model-tiering: [[building-a-universal-ai-scraper]] uses GPT-4-Turbo for assistant orchestration and GPT-4-32K for harder element-picking and action-writing stages.
- Productization intent: [[building-a-universal-ai-scraper]] says popularity led the author to consider turning the prototype into an API.

## Qualifications
The wiki has only this source for Tim Connors, so the profile is limited to one technical blog post and should not be treated as a broader biography.

## What Changed
- Created the entity profile for the author of the AI scraper prototype.

## Relationships
- [[AIGuidedWebScraping]] - Tim Connors' prototype is the source of the concept in this wiki.
- [[Playwright]] - browser automation tool he uses for page selectors and interactions.
- [[Crawlee]] - crawler library he uses around Playwright.
- [[OpenAI]] - model provider used for assistant orchestration, vision summaries, and element/action reasoning.

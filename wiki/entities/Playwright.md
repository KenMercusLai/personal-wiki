---
title: "Playwright"
type: entity
tags: [browser-automation, web-scraping, testing]
sources:
  - building-a-universal-ai-scraper
last_updated: 2026-09-15
knowledge_schema: synthesis-v1
---

## Overview
[[Playwright]] appears in the wiki as the browser automation layer used by Tim Connors' AI scraper prototype.

## Current Profile
In the source, Playwright provides the action substrate for a goal-directed scraper. The system ultimately needs selectors so it can click, fill, and navigate browser pages. Connors uses Crawlee's wrapper around Playwright for crawling, then has a stronger model generate async Playwright snippets for interactions selected by the assistant.

## Key Characteristics
- Identifies page elements through selectors before performing actions.
- Supports browser interactions such as clicking and filling elements.
- Serves as the execution layer beneath the AI assistant's higher-level decisions.
- Can be wrapped by crawler infrastructure such as Crawlee.
- Becomes risky when model-written Playwright code is executed dynamically without strong sandboxing.

## Evidence
- Selector substrate: [[building-a-universal-ai-scraper]] explains that Playwright works by identifying an element through a selector and then performing an action such as `click()` or `fill()`.
- Crawlee integration: [[building-a-universal-ai-scraper]] says Crawlee offers a wrapper around Playwright.
- Generated action: [[building-a-universal-ai-scraper]] shows GPT-4-32K writing an async Playwright action that clicks the Mojave Desert link.
- Execution risk: [[building-a-universal-ai-scraper]] passes generated action strings into the crawler and executes them with `eval`, which the author explicitly flags as dangerous.

## Qualifications
The source treats Playwright as a browser-automation dependency, not as a full evaluation of Playwright's testing, scraping, security, or cross-browser feature set.

## What Changed
- Created the entity profile for Playwright's role in AI-guided scraping.

## Relationships
- [[Crawlee]] - wraps Playwright in the prototype's crawling stack.
- [[AIGuidedWebScraping]] - Playwright executes the browser actions selected by the agent.
- [[ComputerUse]] - Playwright provides a DOM/action route for browser computer use.
- [[AgentComputerInterface]] - selectors and generated actions are part of the agent's computer interface.

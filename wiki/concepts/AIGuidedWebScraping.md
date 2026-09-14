---
title: "AI-Guided Web Scraping"
type: concept
tags: [ai, agents, web-scraping, browser-automation]
sources:
  - building-a-universal-ai-scraper
last_updated: 2026-09-15
knowledge_schema: synthesis-v1
---

## Definition
[[AIGuidedWebScraping]] is a scraping pattern where an LLM-guided agent searches page structure, selects relevant elements, performs browser interactions, and iterates toward a user-specified extraction goal.

## Current Synthesis
Tim Connors' prototype treats scraping as a goal-directed agent problem rather than a fixed selector script. A user supplies a starting URL and high-level goal; the assistant then chooses search terms, invokes a GET_ELEMENT tool to find relevant HTML, decides whether the retrieved element satisfies the goal, and optionally invokes an interaction tool that produces Playwright code.

The most important design move is hybrid retrieval over page structure. Pure screenshot analysis loses detail on tall pages and does not naturally produce selectors. Pure full-HTML prompting leaves the model inside a large, noisy, fuzzy relevance problem. The working approach lets a model generate ranked terms, uses deterministic regex search to collect candidates, caps token usage while favoring higher-ranked terms, and then asks a stronger model to select the best candidate.

The prototype also shows why browser-agent context is not just "the matching node." Useful information may be in a sibling or parent element, so the search function exposes a parent-depth parameter and defaults to including the immediate parent. Page-state summaries after interactions let the assistant notice navigation success, failed loads, popups, or other obstacles before retrying.

## Key Claims
- Universal scraping can be decomposed into page analysis, relevant-element extraction, optional interaction, and iterative goal checking.
- Vision-only page understanding is fragile for tall pages and selector recovery.
- Full-HTML prompting can fit within large context windows while still producing poor selector choices.
- Hybrid model-generated search terms plus deterministic HTML search can narrow the candidate set before model judgment.
- Parent-context retrieval is necessary when the answer or action target is adjacent to, rather than inside, the matching text node.
- Tool schemas and tool outputs should expose retry signals such as per-term match counts and page-state summaries.
- Generated browser-action code can extend scraper capability, but executing model-written code creates safety and reliability risk.

## Evidence
- Agent loop: [[building-a-universal-ai-scraper]] defines the scraper spec as analyze, extract, interact, and repeat until the goal is reached.
- Vision limitation: [[building-a-universal-ai-scraper]] reports that GPT-4-Turbo-Vision sometimes refused transcription and that very tall screenshots became unreadable after preprocessing.
- Full HTML limitation: [[building-a-universal-ai-scraper]] says GPT-4-Turbo often picked wrong elements or overly broad selectors even when cleaned page HTML fit in context.
- Hybrid retrieval: [[building-a-universal-ai-scraper]] generates 15-20 ranked search terms, searches HTML concurrently, and passes a capped candidate list to GPT-4-32K for final choice.
- Token-budget selection: [[building-a-universal-ai-scraper]] uses a final list that favors candidates from higher-ranked search terms while stopping at a predefined token limit.
- Parent context: [[building-a-universal-ai-scraper]] adds a parent-depth parameter so matching elements can return parent or grandparent HTML when sibling nodes contain the answer.
- Tool interface: [[building-a-universal-ai-scraper]] defines GET_ELEMENT with ranked search terms, URL, directive, matching-element counts, and returned relevant element.
- Interaction interface: [[building-a-universal-ai-scraper]] defines INTERACT_WITH_ELEMENT as assistant-described intent that a stronger model translates into async Playwright code.
- End-to-end test: [[building-a-universal-ai-scraper]] navigates from the United States Wikipedia page to Mojave Desert and extracts the infobox area of 81,000 km2 or 31,000 sq mi.

## Counterevidence & Qualifications
The source is a prototype report, not a benchmark. Its successful Wikipedia run uses a reliable site with abundant links and regular structure, while the author says the system is still fragile. The implementation relies on deprecated or time-bound model names, model-written code execution via `eval`, and a goal of bypassing obstacles such as captchas and popups that raises safety, legal, and site-policy questions. Future improvements named by the author include better search-term generation, fuzzy search, image/icon labeling, and stealthier crawling through residential proxies.

## What Changed
- Created the concept from Tim Connors' universal AI scraper prototype.
- Added hybrid ranked-term HTML retrieval, parent-context element selection, and model-generated browser actions as the core architecture.
- Added explicit qualifications around fragility, generated-code execution, and anti-bot/captcha implications.

## Related Concepts
- [[ComputerUse]] - AI-guided web scraping is a browser-specific computer-use pattern.
- [[AgentComputerInterface]] - GET_ELEMENT and INTERACT_WITH_ELEMENT are model-facing action interfaces.
- [[AgenticWorkflowPatterns]] - the scraper uses a retrying tool loop with goal checks and stopping conditions.
- [[AgenticRAG]] - ranked search over live HTML is an agentic retrieval loop over a current environment.
- [[WebScrapingProxyPool]] - proxy and stealth techniques are one operational layer the author wants to improve.
- [[Playwright]] - supplies selectors, clicks, and browser execution for the prototype.
- [[Crawlee]] - supplies crawler ergonomics and request-queue support around Playwright.

---
title: "Building a Universal AI Scraper"
type: source
tags: [ai, agents, web-scraping, browser-automation]
date: 2026-04-12
source_file: /mnt/ken_personal_wiki/Articles/Building a Universal AI Scraper.md
---

## Summary
[[TimConnors]] describes a work-in-progress [[AIGuidedWebScraping]] system that starts from a URL and goal, uses language models to find relevant page elements, and iterates through browser interactions until the goal is reached. The implementation combines [[NextJS]], [[Crawlee]], [[Playwright]], [[OpenAI]], and Azure OpenAI models, with a GET_ELEMENT tool for ranked HTML search and an INTERACT_WITH_ELEMENT tool that turns model-described actions into executable Playwright code.

## Key Claims
- A universal scraper can be framed as an agent loop: analyze the current page, extract relevant information, optionally interact with an element, and repeat until the goal is reached.
- Screenshot-plus-vision extraction is brittle for whole-page scraping because tall screenshots are downscaled, transcription can fail, and text alone does not easily recover a usable DOM selector.
- Passing entire HTML to a text model is also unreliable because real pages contain too much noisy structure and "relevant element" selection is fuzzy.
- A hybrid GET_ELEMENT approach works better: have a model generate ranked search terms, use fast regex search over HTML to gather candidate elements, cap the token budget while favoring higher-ranked terms, then ask a stronger model to choose the most relevant element.
- Returning parent HTML around matching elements is important because the answer or action target may live in a sibling or containing element rather than the exact text match.
- Tool-result metadata, including match counts per search term and page-state summaries, helps the assistant decide whether to retry with broader search terms or proceed.
- Generating and `eval`-executing Playwright actions from model output can navigate pages successfully, but the author explicitly flags it as dangerous and the final system remains fragile.

## Key Quotes
> "Given a starting URL and a high-level goal" - on the target abstraction for the scraper.

> "This approach quickly fell apart" - on screenshot-plus-vision extraction for full pages.

> "yes, I know this could be dangerous" - on executing generated Playwright code with `eval`.

## Connections
- [[TimConnors]] - author and builder of the prototype.
- [[AIGuidedWebScraping]] - central architecture for model-guided element search, browser action, and iterative goal completion.
- [[AgenticWorkflowPatterns]] - the scraper alternates tool calls, result evaluation, retries, and stopping conditions.
- [[AgentComputerInterface]] - GET_ELEMENT and INTERACT_WITH_ELEMENT show tool schemas as model-facing interfaces.
- [[ComputerUse]] - the system controls a browser through DOM/Playwright actions rather than only screenshots or accessibility trees.
- [[Crawlee]] - browser-crawling library used on top of Playwright.
- [[Playwright]] - browser automation layer used for selectors, clicks, page actions, and crawler execution.
- [[OpenAI]] - model provider for GPT-4-Turbo, GPT-4-Turbo-Vision, and the Assistant API.
- [[NextJS]] - backend project framework chosen partly to leave room for a future frontend.

## Contradictions
- Qualifies screenshot-driven computer-use approaches by showing that full-page vision can fail under image resizing, transcription refusal, and selector-recovery constraints.
- Qualifies simple "send the HTML to the model" approaches by showing that large noisy HTML can fit a context window while still producing wrong or overly broad selectors.

## Image Evidence
- The first two flow diagrams contrast failed GET_ELEMENT attempts: screenshot plus vision followed by HTML text search, and raw HTML plus text model selection.
- The third flow diagram shows the successful hybrid path: ranked search terms feed HTML, regex filtering narrows candidates, and a text model picks the most relevant element.
- The ranked-list and token-budget diagrams show candidate elements grouped by search term and merged into a final token-limited list that favors earlier, more relevant terms.
- The code screenshot shows `getElements` collecting candidate lists concurrently, tracking match counts, and adding elements until a token limit is reached.
- The Cuba example diagrams show why parent context matters: the search term may appear in one element while the answer appears in a sibling under a common parent.
- The prompt screenshots define how the stronger model should choose a single candidate element and how the assistant should call GET_ELEMENT with 10-15 ranked terms, a URL, and a directive.
- The interaction diagrams and prompt screenshots define INTERACT_WITH_ELEMENT as a two-step action interface: the assistant describes the desired interaction, then a stronger model writes Playwright code and may set `actionOutput`.
- The `eval` screenshot shows generated async Playwright code being executed inside the crawler, explicitly creating a safety concern.
- The final flow diagram shows the assistant loop: generate search terms, call GET_ELEMENT, check completion, optionally call INTERACT_WITH_ELEMENT, summarize state, and repeat or finish.
- The Wikipedia test screenshot confirms the target result in an infobox row: Mojave Desert area is 81,000 km2 or 31,000 sq mi.

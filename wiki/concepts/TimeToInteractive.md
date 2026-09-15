---
title: "Time To Interactive"
type: concept
tags: [web-performance, metrics, frontend]
sources:
  - can-you-afford-it-real-world-web-performance-budgets-infrequently-noted
last_updated: 2026-09-15
knowledge_schema: synthesis-v1
---

## Definition
[[TimeToInteractive]] is a web performance metric for when a page has loaded enough critical resources and completed enough main-thread work to respond reliably to user input.

## Current Synthesis
Alex Russell's source uses Time to Interactive as the practical boundary between a page that merely displays pixels and a page that users can actually operate. This matters most for JavaScript-heavy applications: HTML and CSS may render visible content while scripts are still downloading, parsing, compiling, executing, constructing UI, or blocking input on the main thread.

In the article, TTI becomes the top-level budget target. Russell recommends under five seconds for first loads and under two seconds for repeat loads, then derives rough critical-path transfer limits from those targets, a slow-3G network baseline, and JavaScript evaluation cost.

## Key Claims
- TTI is more user-relevant than visual loading alone because users need responsive input, not just painted pixels.
- JavaScript-heavy pages often delay TTI through fetch, decompression, parse, compile, execution, and main-thread work.
- First-load TTI budgets should be calculated against representative low-end devices and networks.
- Repeat-load TTI should be much faster when Service Workers and offline-first architecture can avoid fresh network fetches for the application shell.

## Evidence
- Metric choice: [[can-you-afford-it-real-world-web-performance-budgets-infrequently-noted]] makes TTI the main performance budget target for PWA work.
- First-load target: [[can-you-afford-it-real-world-web-performance-budgets-infrequently-noted]] recommends under five seconds TTI for first loads.
- Repeat-load target: [[can-you-afford-it-real-world-web-performance-budgets-infrequently-noted]] recommends under two seconds TTI for subsequent loads.
- Main-thread cost: [[can-you-afford-it-real-world-web-performance-budgets-infrequently-noted]] explains that input processing, DOM construction, layout, and JavaScript execution share the main thread.

## Counterevidence & Qualifications
The source uses the 2017 Lighthouse-era TTI framing. Later performance practice may prefer or supplement other user-centric metrics, but the underlying distinction between visible pixels and responsive interaction remains important.

## What Changed
- Created the concept from the performance-budget source.

## Related Concepts
- [[PerformanceBudget]] - TTI provides the time target used to calculate the budget.
- [[CriticalRenderingPath]] - critical-path work delays TTI when it blocks main-thread availability.
- [[WebPerformanceOptimization]] - TTI is one metric for evaluating user-visible performance.

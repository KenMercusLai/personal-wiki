---
title: "Performance Budget"
type: concept
tags: [web-performance, frontend, pwa, measurement]
sources:
  - can-you-afford-it-real-world-web-performance-budgets-infrequently-noted
last_updated: 2026-09-15
knowledge_schema: synthesis-v1
---

## Definition
[[PerformanceBudget]] is a measurable limit on the time, bytes, and critical-path resources a web product can spend while still meeting a user-facing performance target on representative devices and networks.

## Current Synthesis
Alex Russell's source treats performance budgets as both a technical constraint and an organizational contract. The budget starts with a real user environment rather than developer machines: a roughly $200 Android phone on a 400ms RTT, 400Kbps connection. From there, the team works backward from a target [[TimeToInteractive]] to decide how much critical-path HTML, CSS, JavaScript, and data can be afforded.

The key move is to make performance a hard product constraint early enough to influence technology choices. A JavaScript framework, router, data layer, analytics bundle, third-party origin, or large application shell is not "free" merely because it is common. The source's rough first-load calculation leaves about 170KB for low-JS critical paths and about 130KB for JavaScript-heavy ones, making budget overruns visible before they become product crises.

## Key Claims
- Performance budgets should be set early enough to shape stack and architecture choices.
- Budgets must be tied to representative devices and networks, not the fastest hardware carried by the product team.
- [[TimeToInteractive]] is a useful budget target because it measures whether the page can respond to user input.
- JavaScript deserves special scrutiny because its transfer size understates the cost of parsing, compilation, execution, and main-thread delay.
- CI and commit-queue checks should turn budget regressions into hard failures when product access depends on speed.
- Second and later loads should use offline-first caching and Service Workers so the application shell can become interactive without a fresh network trip.

## Evidence
- Baseline definition: [[can-you-afford-it-real-world-web-performance-budgets-infrequently-noted]] recommends a roughly $200 Android phone, 400ms RTT, and 400Kbps transfer as a conservative global benchmark.
- First-load target: [[can-you-afford-it-real-world-web-performance-budgets-infrequently-noted]] proposes under five seconds TTI for first loads.
- Subsequent-load target: [[can-you-afford-it-real-world-web-performance-budgets-infrequently-noted]] proposes under two seconds TTI for repeat loads and points to Service Workers and offline-first architecture.
- Byte calculation: [[can-you-afford-it-real-world-web-performance-budgets-infrequently-noted]] estimates about 170KB of critical-path transfer for low-JS sites and about 130KB for JavaScript-heavy sites.
- Tooling discipline: [[can-you-afford-it-real-world-web-performance-budgets-infrequently-noted]] recommends WebPageTest, scripted Lighthouse, SpeedCurve, Calibre, webpack performance budgets, bundlesize, and PR-bot-like CI enforcement.
- Organizational risk: [[can-you-afford-it-real-world-web-performance-budgets-infrequently-noted]] describes late performance firefighting as delaying launches, slowing product learning, and harming team morale.

## Counterevidence & Qualifications
The numeric budget is explicitly a rough 2017 calculation, not a universal current standard. Device classes, networks, browser engines, HTTP behavior, and framework tooling evolve, so teams should update the baseline with their own RUM and customer evidence. The deeper claim is more durable: budget math should be derived from user conditions and enforced before architecture choices become expensive to reverse.

## What Changed
- Created the concept from Alex Russell's article on real-world web performance budgets.

## Related Concepts
- [[WebPerformanceOptimization]] - performance budgets operationalize broad optimization work into measurable constraints.
- [[CriticalRenderingPath]] - critical-path bytes and blocking work determine whether the budget can be met.
- [[TimeToInteractive]] - primary time target used by the source.
- [[HTTP2]] - protocol feature that can help route-aware loading fit within a small critical path.
- [[ProductPageOptimization]] - budget failures can harm conversion and product access before checkout.
- [[ConversionRateOptimization]] - speed becomes a measurable product and business lever.

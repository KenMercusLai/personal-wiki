---
title: "Critical Rendering Path"
type: concept
tags: [frontend, browser, performance]
sources:
  - building-a-shop-with-sub-second-page-loads-lessons-learned
last_updated: 2026-09-15
knowledge_schema: synthesis-v1
---

## Definition
[[CriticalRenderingPath]] is the browser sequence that turns HTML, CSS, JavaScript, and layout information into painted pixels for the initial visible page.

## Current Synthesis
The Baqend source presents the critical rendering path as the main frontend-performance lever. The browser parses HTML into the DOM, parses CSS into the CSSOM, combines them into the render tree, computes layout, and paints pixels. CSS blocks rendering until the CSSOM is ready, while JavaScript can block DOM parsing and wait on CSS because scripts can read and mutate both DOM and CSSOM.

Optimization therefore focuses on reducing critical resources, minimizing their byte size, and shortening the number of sequential round trips needed before first render. The article recommends inlining above-the-fold CSS or JavaScript, asynchronously loading noncritical resources, concatenating resources when they cannot be asynchronous, minifying and compressing CSS/JS/images, placing CSS high and JavaScript low in HTML, and using browser caching.

## Key Claims
- The DOM and CSSOM are the largest frontend constraints on first render.
- CSS is render-blocking because the page cannot be displayed until necessary style information exists.
- JavaScript is parser-blocking when it can alter DOM or CSSOM before parsing continues.
- Critical resources should be reduced, inlined, loaded asynchronously, concatenated where appropriate, minified, compressed, and cached.
- CRP length is partly a network problem because sequential resource fetches add round trips.

## Evidence
- Browser steps: [[building-a-shop-with-sub-second-page-loads-lessons-learned]] describes DOM, CSSOM, render tree, layout, and paint as the necessary display sequence.
- Blocking behavior: [[building-a-shop-with-sub-second-page-loads-lessons-learned]] explains CSS as render-blocking and JavaScript as parser-blocking because scripts can access both DOM and CSSOM.
- Optimization tactics: [[building-a-shop-with-sub-second-page-loads-lessons-learned]] lists critical-resource reduction, byte minimization, CRP shortening, and browser caching as the core CRP strategies.
- Tooling examples: [[building-a-shop-with-sub-second-page-loads-lessons-learned]] names PageSpeed Insights, GTmetrix, WebPageTest, Critical, processhtml, PostCSS, TinyPNG, UglifyJS, cssmin, and Google Closure as supporting tools.

## Counterevidence & Qualifications
The article is a 2016 practitioner source, so individual tools and browser behavior details may have evolved. The structural point remains useful: first render depends on resource dependency ordering, bytes, and round trips, not only raw server speed.

## What Changed
- Created the critical rendering path concept from the Baqend source.

## Related Concepts
- [[WebPerformanceOptimization]] - CRP optimization is the frontend pillar of page-load work.
- [[LatencyHierarchy]] - CRP length turns frontend dependency chains into network-latency costs.
- [[ProductPageOptimization]] - product pages lose purchase intent when first render is delayed.
- [[ConversionRateOptimization]] - render speed can affect completion rates before checkout.

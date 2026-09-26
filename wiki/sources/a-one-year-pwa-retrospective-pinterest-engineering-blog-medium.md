---
title: "A One Year PWA Retrospective"
type: source
tags: [pwa, mobile-web, web-performance, product-growth]
date: 2018-07-20
source_file: "/mnt/ken_personal_wiki/Articles/A one year PWA retrospective - Pinterest Engineering Blog - Medium.md"
---

## Summary
[[ZackArgyle]] describes how [[Pinterest]] rebuilt its mobile website as [[ProgressiveWebApps|a progressive web app]] after a native-app-first strategy left low-bandwidth and logged-out users with a weak experience and conversion funnel. The cross-functional [[ProjectDuplo]] team shipped logged-in and logged-out versions over seven months, using [[Gestalt]], route and component code-splitting, preloading, normalized client state, an app shell, service workers, caching, push notifications, and homescreen installation. Pinterest reports large year-over-year gains in usage, engagement, login, signup, and homescreen use, while the retrospective also shows that preserving those gains required explicit [[PerformanceRegressionPrevention|bundle-regression controls]].

## Key Claims
- Pinterest treated mobile web as a global-access and acquisition surface because more than half its users were outside the United States and many faced low bandwidth or limited data plans.
- A combined web-platform and growth team rewrote the mobile site, shipping to logged-in users by September 2017 and logged-out users by February 2018.
- [[Gestalt]] and compositional mobile layout components helped the team deliver a consistent full-featured rewrite quickly.
- Route-level code-splitting, component-level lazy loading, route preloading, and a normalized Redux store reduced initial transfer and made navigation feel immediate while fuller data loaded.
- The PWA used a server-rendered user-specific app shell, service-worker asset caching, homescreen installation, and push notifications to create native-like repeat visits.
- [[PerformanceRegressionPrevention]] mattered after launch: bundle-size graphs and growth alerts exposed regressions, while a custom ESLint rule blocked imports known to pull desktop-heavy dependencies into mobile web.
- Pinterest reports that the new experience coincided with 103% growth in weekly active mobile-web users, 296% longer sessions, 370% more logins, 843% more signups, and 800,000 weekly homescreen users, all without establishing causal attribution.

![Two Pinterest progressive web app screens showing a profile and a Pin detail view in a native-like mobile interface](../../wiki-assets/a-one-year-pwa-retrospective-pinterest-engineering-blog-medium/pinterest-pwa-mobile-ui.png)

## Key Quotes
> "mobile web can be as good as a native app." - the rewrite team's central product hypothesis.

> "It's really hard to maintain performance!" - the retrospective's warning after the codebase grew to roughly 600 JavaScript files.

## Connections
- [[Pinterest]] - company that funded and measured the mobile-web rewrite.
- [[ZackArgyle]] - Pinterest engineering manager and author of the retrospective.
- [[ProjectDuplo]] - internal cross-functional initiative that rebuilt Pinterest's mobile website.
- [[ProgressiveWebApps]] - product and delivery model used for the new mobile experience.
- [[Gestalt]] - open-source component library that encoded Pinterest's design language and layout primitives.
- [[WebPerformanceOptimization]] - code-splitting, preloading, caching, and normalized state were used to reduce initial and navigation latency.
- [[PerformanceRegressionPrevention]] - build-size alerts and import restrictions defended the performance budget as the codebase grew.
- [[ConversionRateOptimization]] - the rewrite targeted the logged-out-to-login, signup, and app-install funnel.

![Small Gestalt layout diagram showing nested page components and a full-width section crossing container boundaries](../../wiki-assets/a-one-year-pwa-retrospective-pinterest-engineering-blog-medium/gestalt-layout-boundaries.png)

## Contradictions
- The results qualify any blanket claim that native apps are inherently more engaging or commercially valuable than mobile web: Pinterest reports that a sufficiently capable PWA became its largest source of new signups.
- The performance and growth figures are company-reported year-over-year comparisons from a retrospective, not a controlled causal study. Product quality, rollout expansion, market growth, seasonality, and other changes may have contributed, and the source does not provide absolute baselines or confidence intervals.
- The 60x32-pixel Gestalt diagram is legible only as a coarse component-boundary illustration; the surrounding prose, not the image, supplies the reliable component names and behavior.

---
title: "Performance Regression Prevention"
type: concept
tags: [web-performance, tooling, governance, javascript]
sources:
  - a-one-year-pwa-retrospective-pinterest-engineering-blog-medium
last_updated: 2026-09-24
knowledge_schema: synthesis-v1
---

## Definition
[[PerformanceRegressionPrevention]] is the engineering practice of turning performance goals into monitored limits and dependency rules that stop routine code changes from silently degrading user experience.

## Current Synthesis
Pinterest's PWA retrospective shows why initial optimization is insufficient in a growing JavaScript application: across roughly 600 files and shared subsites, one import could add enough dependency weight to bloat the mobile bundle. The team's defense combined build-size graphs, alerts when bundles exceeded permitted growth rates, and a custom ESLint rule that prohibited imports from known heavy desktop code while allowing an explicit safe shared-package boundary. This makes performance an ongoing architectural constraint enforced close to code review rather than a periodic rescue project.

## Key Claims
- Performance gains decay unless teams measure bundle growth continuously after launch.
- Alerts need an explicit permitted growth rate or budget to distinguish signal from ordinary change.
- Static import restrictions can encode architectural knowledge about dependency-heavy boundaries before code reaches users.
- Safe shared-package allowlists can preserve reuse without granting unrestricted access to a heavier codebase.
- Prevention complements runtime measurement; bundle size alone does not capture parse, execution, caching, network, or interaction cost.

## Evidence
- Scale pressure: [[a-one-year-pwa-retrospective-pinterest-engineering-blog-medium]] reports roughly 600 JavaScript files after one year and warns that one poorly chosen import can bloat a bundle.
- Monitoring control: [[a-one-year-pwa-retrospective-pinterest-engineering-blog-medium]] describes build-size graphs and alerts when bundles exceed permitted growth rates.
- Architecture control: [[a-one-year-pwa-retrospective-pinterest-engineering-blog-medium]] describes a custom ESLint rule blocking imports from dependency-heavy files and from the desktop codebase, except for a safe shared-package directory.

## Counterevidence & Qualifications
The source does not quantify alert thresholds, prevented regressions, false positives, developer friction, or the causal effect of the custom rule. Bundle size is only a proxy: compressed transfer, caching, device CPU, main-thread work, data fetching, rendering, and user-perceived latency also need measurement. Strict dependency bans can duplicate code or freeze poor boundaries unless teams maintain the safe-sharing interface.

## What Changed
- Created the concept from Pinterest's post-launch bundle monitoring and dependency-boundary controls.

## Related Concepts
- [[PerformanceBudget]] - supplies the measurable limit that regression controls enforce.
- [[WebPerformanceOptimization]] - broader practice whose gains need protection as systems evolve.
- [[ProgressiveWebApps]] - rich client capability makes dependency and bundle discipline especially important.
- [[CriticalRenderingPath]] - additional JavaScript can delay parsing, execution, and interactivity.
- [[CodeReviewPractice]] - automated checks move repeatable performance constraints into the change-review path.

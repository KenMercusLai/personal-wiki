---
title: "Confidence-Based Testing"
type: concept
tags: [software-testing, software-quality, risk-management]
sources:
  - kent-beck-i-get-paid-for-code-that-works-not-for-tests
last_updated: 2026-10-01
knowledge_schema: synthesis-v1
---

## Definition
[[ConfidenceBasedTesting]] is a testing strategy that selects tests by the confidence they add against plausible, consequential failures relative to their creation, execution, diagnosis, and maintenance cost.

## Current Synthesis
The source begins with [[KentBeck]]'s personal allocation rule: write as little testing as necessary to reach a chosen confidence level, spending more effort on mistakes that the individual or team repeatedly makes and on logic known to be error-prone. This rejects test count and coverage percentage as ends in themselves without rejecting high confidence or disciplined testing.

The comment discussion widens the decision beyond immediate coding mistakes. Regression protection, future maintainers, project longevity, team turnover, customer outcomes, and the cost of failures can justify tests that the current author does not personally need. Conversely, trivial framework behavior, assignment mechanics, or tests added only to reach a target can consume effort without adding useful evidence.

Test type is part of the allocation problem, not settled by the thread. Some commenters prefer more smoke or integration testing and stronger static types in place of repetitive unit checks, while the existing [[TestPyramid]] source warns that higher-level suites can become slower, less local, and more brittle. The appropriate portfolio therefore depends on failure risk, feedback speed, diagnostic value, maintenance burden, and system boundaries rather than a universal layer ratio.

## Key Claims
- Testing effort should be calibrated to a required confidence level rather than maximized without limit.
- Recurring individual and team mistake patterns are useful signals for where additional tests may have high value.
- Coverage percentages and test counts are weak proxies when they can be raised through tests that add little behavioral confidence.
- Regression protection and future maintainability can justify tests beyond the current programmer's known error profile.
- Unit, integration, smoke, static-type, and other checks are partial substitutes only when they cover the relevant failure mode with acceptable feedback and diagnostic cost.
- A useful test strategy begins by asking what risk a check addresses and what decision its result enables.

## Evidence
- Personal error targeting: [[kent-beck-i-get-paid-for-code-that-works-not-for-tests]] quotes Beck prioritizing mistakes he tends to make and complex conditional logic.
- Team adaptation: [[kent-beck-i-get-paid-for-code-that-works-not-for-tests]] quotes Beck changing his strategy to cover errors the team collectively tends to make.
- Metric failure: [[kent-beck-i-get-paid-for-code-that-works-not-for-tests]] includes reports of pointless tests written during coverage-target sprints and tests of simple field assignment.
- Lifecycle qualification: [[kent-beck-i-get-paid-for-code-that-works-not-for-tests]] includes a critique that tests also protect later corrections and long-lived shared systems.
- Portfolio alternatives: [[kent-beck-i-get-paid-for-code-that-works-not-for-tests]] includes practitioner claims for smoke tests, integration tests, and strong typing as substitutes for some unit checks.

## Counterevidence & Qualifications
The source is a saved quotation followed by heterogeneous comments, not a controlled comparison of testing strategies. It gives no defect rates, suite timings, maintenance costs, project outcomes, or criteria for translating a desired confidence level into sufficient tests. Personal error history can miss novel, interaction, security, concurrency, accessibility, data-integrity, and low-frequency catastrophic failures. Commenters' claims that smoke tests or static types replace many unit tests are experience reports whose validity depends on language, architecture, observability, failure cost, and test quality. Confidence can also be miscalibrated, so risk analysis, production evidence, and independent review may be needed beyond developer intuition.

## What Changed
- Created the concept from Beck's confidence rule and the thread's maintainability, metrics, and test-portfolio debate.

## Related Concepts
- [[SoftwareVerification]] - broader system of behavioral checks in which confidence-based test selection operates.
- [[TestPyramid]] - proposes a layer distribution whose costs and benefits must be reconciled with confidence needs.
- [[InternalSoftwareQuality]] - long-term changeability and regression safety expand the value horizon of tests.
- [[ExtremeProgramming]] - practice tradition associated with Beck and test-guided development.
- [[DeterministicTesting]] - stable test behavior improves the information value of each check.
- [[CoreRegressionTestSeparation]] - distinguishes correctness-critical tests from broader continuity evidence by purpose.

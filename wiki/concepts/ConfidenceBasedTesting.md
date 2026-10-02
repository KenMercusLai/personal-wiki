---
title: "Confidence-Based Testing"
type: concept
tags: [software-testing, software-quality, risk-management]
sources:
  - kent-beck-i-get-paid-for-code-that-works-not-for-tests
  - the-tragedy-of-100-code-coverage
last_updated: 2026-10-02
knowledge_schema: synthesis-v1
---

## Definition
[[ConfidenceBasedTesting]] is a testing strategy that selects tests by the confidence they add against plausible, consequential failures relative to their creation, execution, diagnosis, and maintenance cost.

## Current Synthesis
[[KentBeck]] supplies the personal allocation rule: write as little testing as necessary to reach a chosen confidence level, spending more effort on mistakes that the individual or team repeatedly makes and on logic known to be error-prone. [[DanLebrero]] adds two concrete mismatch cases: branch-free callback glue surrounded by Mockito difficulty, and a map lookup surrounded by a Cucumber scenario, step definitions, mocking, reflection, and setup. Together they reject test count and coverage percentage as ends in themselves without rejecting high confidence or disciplined testing.

The comment discussion widens the decision beyond immediate coding mistakes. Regression protection, future maintainers, project longevity, team turnover, customer outcomes, and the cost of failures can justify tests that the current author does not personally need. Conversely, trivial framework behavior, assignment mechanics, or tests added only to reach a target can consume effort without adding useful evidence.

Test type and tool fit are part of the allocation problem. Some commenters prefer more smoke or integration testing and stronger static types in place of repetitive unit checks, while the existing [[TestPyramid]] source warns that higher-level suites can become slower, less local, and more brittle. Lebrero's examples make that cost visible when a mandated framework expands incidental scaffolding without expanding the behavior checked. The appropriate portfolio therefore depends on failure risk, feedback speed, diagnostic value, maintenance burden, and system boundaries rather than a universal layer ratio or organization-wide tool rule.

Coverage extremes can still have bounded learning value. Lebrero recommends enforcing 100% coverage and TDD on one project so practitioners experience the opposite of an untested codebase and learn where the marginal test becomes counterproductive. This is an experiment for calibrating judgment, not evidence that the threshold should become permanent policy.

## Key Claims
- Testing effort should be calibrated to a required confidence level rather than maximized without limit.
- Recurring individual and team mistake patterns are useful signals for where additional tests may have high value.
- Coverage percentages and test counts are weak proxies when they can be raised through tests that add little behavioral confidence.
- Mandatory tools and tests for every class can turn a quality practice into rule compliance while increasing scaffolding and future maintenance.
- Regression protection and future maintainability can justify tests beyond the current programmer's known error profile.
- Unit, integration, smoke, static-type, and other checks are partial substitutes only when they cover the relevant failure mode with acceptable feedback and diagnostic cost.
- A useful test strategy begins by asking what risk a check addresses, what decision its result enables, and whether a deliberate extreme is being used temporarily to learn rather than permanently to govern.

## Evidence
- Personal error targeting: [[kent-beck-i-get-paid-for-code-that-works-not-for-tests]] quotes Beck prioritizing mistakes he tends to make and complex conditional logic.
- Team adaptation: [[kent-beck-i-get-paid-for-code-that-works-not-for-tests]] quotes Beck changing his strategy to cover errors the team collectively tends to make.
- Metric failure: [[kent-beck-i-get-paid-for-code-that-works-not-for-tests]] includes reports of pointless tests written during coverage-target sprints and tests of simple field assignment.
- Boundary mismatch: [[the-tragedy-of-100-code-coverage]] shows branch-free callback glue and a single map lookup receiving test machinery disproportionate to the behavior checked.
- Tool mandates: [[the-tragedy-of-100-code-coverage]] attributes the Mockito and Cucumber choices to blanket team or management rules rather than a behavior-specific need.
- Lifecycle qualification: [[kent-beck-i-get-paid-for-code-that-works-not-for-tests]] includes a critique that tests also protect later corrections and long-lived shared systems.
- Portfolio alternatives: [[kent-beck-i-get-paid-for-code-that-works-not-for-tests]] includes practitioner claims for smoke tests, integration tests, and strong typing as substitutes for some unit checks.
- Extreme as experiment: [[the-tragedy-of-100-code-coverage]] recommends pursuing 100% coverage in one project to learn the costs and limits of the practice.

## Counterevidence & Qualifications
Both sources are practitioner discussions, not controlled comparisons of testing strategies. They give no defect rates, suite timings, measured maintenance costs, project outcomes, or criteria for translating a desired confidence level into sufficient tests. Lebrero's two examples show disproportionate machinery but do not prove that simple-looking glue is harmless: integration contracts, concurrency, configuration, generated behavior, or expensive failures can justify checks outside the visible method. Personal error history can miss novel, security, accessibility, data-integrity, and low-frequency catastrophic failures. Claims that smoke tests, static types, or no isolated unit test preserve confidence remain dependent on language, architecture, observability, failure cost, and test quality. Confidence can also be miscalibrated, so risk analysis, production evidence, and independent review may be needed beyond developer intuition.

## What Changed
- Added concrete evidence that blanket coverage and framework rules can create disproportionate scaffolding without checking more behavior.
- Added a bounded role for one 100%-coverage project as a calibration experiment rather than a permanent target.

## Related Concepts
- [[SoftwareVerification]] - broader system of behavioral checks in which confidence-based test selection operates.
- [[TestPyramid]] - proposes a layer distribution whose costs and benefits must be reconciled with confidence needs.
- [[InternalSoftwareQuality]] - long-term changeability and regression safety expand the value horizon of tests.
- [[ExtremeProgramming]] - practice tradition associated with Beck and test-guided development.
- [[DeterministicTesting]] - stable test behavior improves the information value of each check.
- [[CoreRegressionTestSeparation]] - distinguishes correctness-critical tests from broader continuity evidence by purpose.

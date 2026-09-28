---
title: "Iterative Product Shipping"
type: concept
tags: [product-development, iteration, shipping]
sources:
  - 7-ways-to-use-the-rule-of-threes-to-build-great-products
  - unknown-unknowns-why-you-should-release-early-and-often
  - your-product-manager-super-power-not-knowing-everything-mind-the-product
  - halide-one-year-later-halide
last_updated: 2026-09-29
knowledge_schema: synthesis-v1
---

## Definition
[[IterativeProductShipping]] is the practice of releasing product work in frequent staged versions so each release can reduce bugs, inform users, gather data, and validate product direction before larger investment.

## Current Synthesis
The sources treat shipping as a learning system rather than merely a delivery event. The rule-of-threes source recommends aiming to ship every two weeks for six versions: integer releases such as V1, V2, and V3 are fully built features grounded in user and data insights, while half-step releases such as V0, V1.5, and V2.5 test ideas and gather more data. Karlsson extends the logic to the period before software exists: a customer conversation, paper mockup, or proof of concept can function as an early release by exposing false certainty and [[UnknownUnknowns]]. Together they make iteration an epistemic discipline in which each staged exposure creates evidence before more resources become attached to the current product theory.

Mind the Product adds a scope-quality test: a small release should deliver some value or generate valuable learning. Teams therefore need to find minimum independent deliverables, identify ordering and parallelism, and distinguish increments that create value alone from components that only work together. Iteration is not simply cutting work into smaller tickets; it requires [[ValueBasedProductScoping]] that preserves a meaningful outcome.

The [[Halide]] retrospective adds a year-long commercial case. Versions 1.1 through 1.8 mixed stability, compatibility, speed, device-specific redesign, requested features, accessibility, and an editing partnership, eventually producing what the team called an episodically delivered Halide 2. The releases reportedly raised slow-day revenue over time, but the case also exposes incentive distortion: large, clearly messaged features created stronger sales spikes than maintenance, even though delayed fixes produced support cost and user frustration.

## Key Claims
- Consistent shipping can keep a product current, reduce accumulated bug risk, and compound into a major product change without withholding improvements for a single upgrade event.
- Releases should be designed to collect data, not only to publish finished features.
- A two-week cadence across six versions can support useful learning cycles.
- Full feature versions, early test artifacts, and independently valuable increments serve different roles in the same iteration system.
- Continuous shipping helps validate whether the product works before more resources are committed.
- The first useful release may be a conversation, mockup, or proof of concept rather than working production software.
- Fear of criticism and failure can be a more important barrier to early release than lack of technique.

## Evidence
- Cadence: [[7-ways-to-use-the-rule-of-threes-to-build-great-products]] says aiming to ship every two weeks for six versions worked well for the author.
- Version roles: [[7-ways-to-use-the-rule-of-threes-to-build-great-products]] defines V1, V2, and V3 as fully built features and V0, V1.5, and V2.5 as early shipments for testing ideas and gathering data.
- Learning value: [[7-ways-to-use-the-rule-of-threes-to-build-great-products]] says continuous shipping helps answer big product questions and validate a product before investing more time and resources.
- Pre-product release: [[unknown-unknowns-why-you-should-release-early-and-often]] recommends calls, paper mockups, and weekend proofs of concept to expose foundational assumptions before full implementation.
- Behavioral barrier: [[unknown-unknowns-why-you-should-release-early-and-often]] says perfectionism and fear make an unreleased product feel safe even as the risk of building the wrong thing grows.
- Increment quality: [[your-product-manager-super-power-not-knowing-everything-mind-the-product]] says teams should map dependencies and release smaller pieces only when they create value or useful learning.
- Product accumulation: [[halide-one-year-later-halide]] traces seven first-year versions whose combined redesigns, fixes, and features were substantial enough for the team to call the current app an episodically delivered Halide 2.
- Commercial feedback: [[halide-one-year-later-halide]] reports that large, clearly messaged releases produced bigger spikes and that successive major updates raised the slow-day revenue baseline.
- Maintenance tension: [[halide-one-year-later-halide]] says release-tied sales made visible features easier to justify than maintenance, despite the team's commitment to alternate quieter “Snow” releases with blockbusters.

## Counterevidence & Qualifications
The sources offer practitioner guidance and one company-authored retrospective rather than comparative outcome evidence, and the recommended two-week cadence is not a universal delivery law. Halide's sales timing does not isolate release effects from press, App Store featuring, price, seasonality, or new-device adoption, and it shows that shipping incentives can systematically underfund maintenance. Regulated, safety-critical, privacy-sensitive, infrastructure-heavy, tightly coupled, or enterprise-integrated products may need simulation, staged exposure, or stronger release gates. Early feedback can also mislead when the test audience is unrepresentative or the artifact does not preserve the core value being tested; arbitrary decomposition can produce small releases that teach nothing.

## What Changed
- Extended release from a software cadence into pre-product tests that expose false certainty and unknown unknowns.
- Added emotional avoidance as a practical obstacle to obtaining early evidence.
- Added independently valuable scope and dependency analysis as conditions for useful small releases.
- Added Halide's commercial case in which episodic releases compounded into a major product change and raised the reported sales baseline.
- Added the counterpressure that feature-linked sales can make necessary maintenance harder to prioritize.

## Related Concepts
- [[RuleOfThreesProductDevelopment]] - supplies the V1, V2, and V3 iteration frame.
- [[ProductEvolution]] - frequent releases create the evidence and user contact that later product evolution builds on.
- [[ReleaseFocusedSideProjects]] - both emphasize usable releases as a precondition for feedback.
- [[StartupHypothesisTesting]] - test releases operationalize product hypotheses.
- [[ProductMetricLadder]] - each iteration needs measurable signals to guide the next one.
- [[ChangeSafety]] - frequent releases still require appropriate risk control and recovery practices.
- [[UnknownUnknowns]] - early release can reveal gaps a team did not know to investigate.
- [[MinimumViableProduct]] - minimal artifacts can produce learning before a complete product exists.
- [[ValueBasedProductScoping]] - identifies increments that preserve value or learning instead of optimizing for smallness alone.
- [[Halide]] - first-year case of accumulating fixes, redesigns, and major features through repeated releases.

---
title: "Iterative Product Shipping"
type: concept
tags: [product-development, iteration, shipping]
sources:
  - 7-ways-to-use-the-rule-of-threes-to-build-great-products
  - unknown-unknowns-why-you-should-release-early-and-often
last_updated: 2026-09-22
knowledge_schema: synthesis-v1
---

## Definition
[[IterativeProductShipping]] is the practice of releasing product work in frequent staged versions so each release can reduce bugs, inform users, gather data, and validate product direction before larger investment.

## Current Synthesis
The sources treat shipping as a learning system rather than merely a delivery event. The rule-of-threes source recommends aiming to ship every two weeks for six versions: integer releases such as V1, V2, and V3 are fully built features grounded in user and data insights, while half-step releases such as V0, V1.5, and V2.5 test ideas and gather more data. Karlsson extends the logic to the period before software exists: a customer conversation, paper mockup, or proof of concept can function as an early release by exposing false certainty and [[UnknownUnknowns]]. Together they make iteration an epistemic discipline in which each staged exposure creates evidence before more resources become attached to the current product theory.

## Key Claims
- Consistent shipping keeps a product current, gives engineers momentum, and reduces accumulated bug risk.
- Releases should be designed to collect data, not only to publish finished features.
- A two-week cadence across six versions can support useful learning cycles.
- Full feature versions and early test versions serve different roles in the same iteration system.
- Continuous shipping helps validate whether the product works before more resources are committed.
- The first useful release may be a conversation, mockup, or proof of concept rather than working production software.
- Fear of criticism and failure can be a more important barrier to early release than lack of technique.

## Evidence
- Cadence: [[7-ways-to-use-the-rule-of-threes-to-build-great-products]] says aiming to ship every two weeks for six versions worked well for the author.
- Version roles: [[7-ways-to-use-the-rule-of-threes-to-build-great-products]] defines V1, V2, and V3 as fully built features and V0, V1.5, and V2.5 as early shipments for testing ideas and gathering data.
- Learning value: [[7-ways-to-use-the-rule-of-threes-to-build-great-products]] says continuous shipping helps answer big product questions and validate a product before investing more time and resources.
- Pre-product release: [[unknown-unknowns-why-you-should-release-early-and-often]] recommends calls, paper mockups, and weekend proofs of concept to expose foundational assumptions before full implementation.
- Behavioral barrier: [[unknown-unknowns-why-you-should-release-early-and-often]] says perfectionism and fear make an unreleased product feel safe even as the risk of building the wrong thing grows.

## Counterevidence & Qualifications
Both sources offer practitioner guidance rather than comparative outcome evidence, and the recommended two-week cadence is not a universal delivery law. Regulated, safety-critical, privacy-sensitive, infrastructure-heavy, or enterprise-integrated products may need simulation, staged exposure, or stronger release gates. Early feedback can also mislead when the test audience is unrepresentative or the artifact does not preserve the core value being tested.

## What Changed
- Extended release from a software cadence into pre-product tests that expose false certainty and unknown unknowns.
- Added emotional avoidance as a practical obstacle to obtaining early evidence.

## Related Concepts
- [[RuleOfThreesProductDevelopment]] - supplies the V1, V2, and V3 iteration frame.
- [[ProductEvolution]] - frequent releases create the evidence and user contact that later product evolution builds on.
- [[ReleaseFocusedSideProjects]] - both emphasize usable releases as a precondition for feedback.
- [[StartupHypothesisTesting]] - test releases operationalize product hypotheses.
- [[ProductMetricLadder]] - each iteration needs measurable signals to guide the next one.
- [[ChangeSafety]] - frequent releases still require appropriate risk control and recovery practices.
- [[UnknownUnknowns]] - early release can reveal gaps a team did not know to investigate.
- [[MinimumViableProduct]] - minimal artifacts can produce learning before a complete product exists.

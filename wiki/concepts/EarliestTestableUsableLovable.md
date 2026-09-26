---
title: "Earliest Testable, Usable, and Lovable Product"
type: concept
tags: [product-development, experimentation, user-feedback]
sources:
  - crisps-blog-making-sense-of-mvp-minimum-viable-product-and-why-i-prefer-earliest-testable-usable-lovable
last_updated: 2026-09-26
knowledge_schema: synthesis-v1
---

## Definition
[[EarliestTestableUsableLovable]] is [[HenrikKniberg]]'s three-threshold vocabulary for distinguishing a product that can generate feedback, one that early adopters willingly use, and one customers love, recommend, and will pay for.

## Current Synthesis
The framework replaces the ambiguous words "minimum" and "viable" with an explicit maturity sequence. An Earliest Testable Product is the first release that lets a customer do something and gives the team evidence, even if customer value is incidental. An Earliest Usable Product improves an early adopter's situation enough for voluntary continued use. An Earliest Lovable Product crosses into strong advocacy and willingness to pay, while still remaining open to substantial change. The thresholds are learning states rather than prescribed feature counts: teams should identify the underlying customer outcome, expose the cheapest coherent test to real users, and allow evidence to change both the implementation and the imagined destination.

## Key Claims
- Testability, usability, and lovability are different product thresholds and should not be collapsed into one undefined notion of viability.
- The earliest testable release primarily buys learning; immediate customer satisfaction or broad market readiness is not required.
- A usable release must improve an early adopter's position enough that they choose to use it, while a lovable release adds recommendation and willingness to pay.
- Each release should deliver a coherent slice of the customer outcome rather than an unusable component of a fixed end solution.
- Real-user feedback can justify stopping early, changing direction, or producing a different and simpler solution than originally requested.
- Up-front analysis should inform experiments but cannot substitute for observing actual use in uncertain product work.

## Evidence
- Threshold definitions: [[crisps-blog-making-sense-of-mvp-minimum-viable-product-and-why-i-prefer-earliest-testable-usable-lovable]] defines testable as feedback-producing, usable as voluntarily adopted by early users, and lovable as recommendable and marketable.
- Outcome slices: [[crisps-blog-making-sense-of-mvp-minimum-viable-product-and-why-i-prefer-earliest-testable-usable-lovable]] contrasts an unusable wheel with skateboard, bicycle, and motorcycle metaphors that each provide transportation value.
- Technical learning: [[crisps-blog-making-sense-of-mvp-minimum-viable-product-and-why-i-prefer-earliest-testable-usable-lovable]] says [[Spotify]] used a rough, limited prototype to test near-instant, stable music playback with friends and family.
- External feedback: [[crisps-blog-making-sense-of-mvp-minimum-viable-product-and-why-i-prefer-earliest-testable-usable-lovable]] contrasts [[Minecraft]] and [[PUST]] releases to users with Lego Universe's prolonged internal-only iteration.

## Counterevidence & Qualifications
The framework comes from one practitioner essay supported by retrospective cases rather than comparative research. Its labels still require local definitions and do not say how much evidence is sufficient, how to sample users, or how regulated and safety-critical products should separate prototype testing from public release. Commenters in the source argue that an MVP can be an experiment with no usable product at all and that the skateboard sequence may discard implementation rather than incrementally build it. The framework is therefore most useful for clarifying release intent and customer-value thresholds, not as a universal replacement for every meaning of [[MinimumViableProduct]].

## What Changed
- Created the concept as a three-threshold alternative to the ambiguous word "viable."
- Distinguished learning, voluntary use, and market affection as separate release outcomes.
- Preserved the critique that Lean Startup experiments can precede any usable product.

## Related Concepts
- [[MinimumViableProduct]] - overlapping validation concept whose scope is broader and terminology more contested.
- [[CustomerLedProductDevelopment]] - real-user observation drives movement between the three thresholds.
- [[JobsToBeDone]] - the framework tests progress toward an underlying need rather than fidelity to a requested artifact.
- [[StartupHypothesisTesting]] - the testable stage should expose named assumptions to evidence.
- [[ProductEvolution]] - feedback can change both the route and the eventual product form.
- [[AgileSoftwareDevelopment]] - coherent, feedback-producing increments distinguish the framework from component-only delivery.

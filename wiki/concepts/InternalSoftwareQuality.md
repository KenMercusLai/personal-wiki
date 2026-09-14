---
title: "Internal Software Quality"
type: concept
tags: [software-quality, technical-practices, agile]
sources:
  - blog-martin-fowler-foreword-to-the-art-of-agile-development
last_updated: 2026-09-14
knowledge_schema: synthesis-v1
---

## Definition
[[InternalSoftwareQuality]] is the codebase and design quality that lets teams change software safely and cheaply, even when users do not directly see that quality.

## Current Synthesis
Fowler's foreword frames internal quality as economically counterintuitive but central to reliable agile delivery. The visible outcome is faster and cheaper feature delivery, but the cause is technical work that protects changeability: testing, refactoring, design discipline, and collaborative development.

The concept also links delivery speed to learning speed. When internal quality enables DevOps culture and [[ContinuousDelivery]], teams can put features into production frequently and observe whether the software is valuable in practice.

## Key Claims
- High internal quality can decrease cost rather than merely add polish.
- Internal quality increases delivery speed by making change safer.
- Testing, refactoring, design, and collaborative development are key quality practices in the source.
- Internal quality is part of genuine [[AgileSoftwareDevelopment]], not a separate engineering luxury.
- Frequent production delivery turns quality into a product-learning accelerator.

## Evidence
- Cost claim: [[blog-martin-fowler-foreword-to-the-art-of-agile-development]] says high internal quality decreases cost and increases delivery speed.
- Practice base: [[blog-martin-fowler-foreword-to-the-art-of-agile-development]] ties reliable delivery to testing, refactoring, design, and collaborative development.
- Learning loop: [[blog-martin-fowler-foreword-to-the-art-of-agile-development]] says frequent production features let teams learn what is valuable by observing real software use.

## Counterevidence & Qualifications
The source argues strongly for internal quality but does not provide quantitative cost evidence. This page should keep the claim as a practitioner synthesis until additional empirical sources are ingested.

## What Changed
- Created the concept from Fowler's foreword.

## Related Concepts
- [[AgileSoftwareDevelopment]] - internal quality is part of real agile capability.
- [[ExtremeProgramming]] - practice tradition associated with testing and refactoring.
- [[ContinuousDelivery]] - delivery capability enabled by strong technical quality.
- [[TestPyramid]] - related testing strategy for fast quality feedback.
- [[TechnicalDebtTracking]] - adjacent practice for surfacing quality liabilities.

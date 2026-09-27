---
title: "Single Responsibility Principle"
type: concept
tags: [software-design, object-oriented-programming, refactoring]
sources:
  - do-one-thing
last_updated: 2026-09-27
knowledge_schema: synthesis-v1
---

## Definition
The [[SingleResponsibilityPrinciple]] is a software-design guideline that asks a function, class, component, or other unit to own one coherent responsibility rather than combine independently changing concerns.

## Current Synthesis
The principle is best treated as a prompt for boundary judgment, not a mechanical pass/fail test. A unit can perform several operations yet remain coherent at one useful level of abstraction, while a locally tidy unit can later prove too broad when another caller needs one of its internal capabilities independently.

Batchelder's [[Zellij]] example makes the principle temporal. `PointMap` initially packaged fuzzy point equality with keyed storage and appeared to do one thing. Later needs exposed fuzzy equality as a reusable capability, so extracting `Defuzzer` and combining it with a standard dictionary produced a smaller and more useful design. The earlier class was not therefore objectively “wrong”; the better boundary became visible through change.

Alternative formulations—one reason to change, one stakeholder, one external factor, or one clear coherent unit—can guide discussion, but none removes interpretation. Teaching the principle well requires naming that ambiguity, examining surrounding code and expected evolution, and comparing the clarity and change cost of candidate boundaries.

## Key Claims
- Responsibility depends on the chosen level of abstraction, so operation count alone cannot determine whether a unit does one thing.
- Reasons to change and stakeholders are diagnostic questions rather than objective measures.
- Reuse and change pressure can reveal a responsibility boundary that was not visible in the initial design.
- Smaller decomposition is beneficial only when it improves coherence, clarity, reuse, or change isolation.
- Binary compliance language obscures the judgment involved and can mislead learners.

## Evidence
- Ambiguous grouping: [[do-one-thing]] contrasts examples that list several operations yet label them one responsibility.
- Evolving boundary: [[do-one-thing]] describes replacing Zellij's `PointMap` with a reusable `Defuzzer` plus a standard dictionary after new needs emerged.
- Diagnostic limits: [[do-one-thing]] records objections that “one reason to change” and one-stakeholder formulations can still group multiple independent changes.
- Fragmentation risk: [[do-one-thing]] includes a commenter’s report that aggressive small-class decomposition made program flow difficult to follow.

## Counterevidence & Qualifications
The source supports the principle's direction while disputing precise compliance tests; it does not show that responsibility boundaries are arbitrary or that large mixed units are acceptable. The Zellij case and comments are practitioner examples rather than controlled evidence, and the proposed “clearest coherent unit” alternative is also subjective. Change history can expose a better boundary, but speculative decomposition before such evidence may add indirection and navigation cost.

## What Changed
- Created the concept as a judgment-dependent and change-sensitive design guideline.
- Added Zellij's `PointMap`-to-`Defuzzer` extraction as the main boundary-discovery example.
- Added fragmentation and teaching risks as explicit qualifications.

## Related Concepts
- [[FunctionDesign]] - applies responsibility judgment at the function level.
- [[InternalSoftwareQuality]] - responsibility boundaries matter because they affect clarity, reuse, testing, and change cost.
- [[TechnologyStackComplexity]] - both concepts require judging global reasoning cost rather than minimizing a local count.
- [[DistributedSystemRestraint]] - warns that extracting more units or boundaries can impose costs that outweigh local neatness.

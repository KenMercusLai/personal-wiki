---
title: "Minimum Viable Experience"
type: concept
tags: [product-management, migration, scope, prioritization]
sources:
  - real-world-engineering-challenges-8-breaking-up-a-monolith
last_updated: 2026-10-01
knowledge_schema: synthesis-v1
---

## Definition
[[MinimumViableExperience]] is a migration milestone defined by the smallest set of existing behaviors whose absence would materially change a product's identity or core user experience.

## Current Synthesis
Khan Academy used MVE instead of MVP because it already had a mature product: the task was not to discover a new viable product but to identify which existing experiences had to survive the first migration phase. Product managers scoped identity-preserving capabilities such as content publishing and delivery, progress tracking, and user management, allowing the program to prioritize a coherent first finish line while deferring nonessential behavior and internal tools.

MVE improved focus but did not mean the migration was nearly done in effort terms. At the milestone, 32 services handled roughly 95% of traffic after two years, yet substantial Python code, lower-traffic behavior, and internal tools remained and required another 18 months.

## Key Claims
- Migration scoping should distinguish product viability from continuity of an already viable experience.
- Essential behavior can be defined by asking what removals would materially alter product identity.
- Product managers can supply the user-experience view needed to prioritize technical migration work.
- A coherent experience milestone creates an earlier finish line without pretending all legacy scope has moved.
- Traffic coverage can overstate completion when low-volume behavior and internal tools remain costly.

## Evidence
- Scope definition: [[real-world-engineering-challenges-8-breaking-up-a-monolith]] says Khan Academy framed MVE around features essential to its identity.
- Product involvement: [[real-world-engineering-challenges-8-breaking-up-a-monolith]] says product managers largely selected the first-phase experience boundary.
- Included behavior: [[real-world-engineering-challenges-8-breaking-up-a-monolith]] names content publishing, content delivery, progress tracking, and user management among MVE capabilities.
- Milestone outcome: [[real-world-engineering-challenges-8-breaking-up-a-monolith]] reports 32 services and about 95% of traffic after 24 months, followed by an 18-month endgame.

## Counterevidence & Qualifications
The concept is supported here by one retrospective case and no comparison with alternative scoping methods. Product identity is contestable, low-traffic behavior can still be legally or operationally critical, and deferring internal tools can transfer substantial cost into an under-resourced endgame. MVE should therefore be paired with a complete residual-scope inventory rather than treated as percent-complete accounting.

## What Changed
- Established MVE as an identity-preserving migration scope distinct from a new-product MVP.
- Added traffic coverage and residual-scope limits to milestone interpretation.

## Related Concepts
- [[ValueBasedProductScoping]] - both define coherent scope through user value rather than component count.
- [[IncrementalMonolithMigration]] - MVE supplies a milestone for a longer staged transition.
- [[MinimumViableProduct]] - differs because an MVE preserves an established product rather than testing initial viability.
- [[TechnicalDecisionReview]] - residual scope and milestone metrics need explicit failure and completeness tests.

---
title: "Kent Beck"
type: entity
tags: [agile, extreme-programming, user-stories, software-testing]
sources:
  - blog-paulo-caroli-martinfowler-com-product-backlog-building-canvas
  - dont-make-it-perfect-make-it-work-and-refine-8th-light
  - finding-time-to-become-a-better-developer
  - kent-beck-i-get-paid-for-code-that-works-not-for-tests
last_updated: 2026-10-01
knowledge_schema: synthesis-v1
---

## Overview
[[KentBeck]] is represented in the wiki as an [[ExtremeProgramming]] practitioner associated with the origin of [[UserStories]], simple design, iterative development, and a confidence-oriented philosophy of software testing.

## Current Profile
The PBB article uses Beck as a historical anchor, crediting him with introducing user stories inside Extreme Programming and linking contemporary backlog practice to conversational requirements. Nick Dyer cites Beck's Four Rules of Simple Design as support for making the simplest tested solution first and then iterating, while the developer-time essay attributes “make it work, make it right, make it fast” to Beck as a sequence separating function, design refinement, and performance optimization.

The new thread supplies Beck's own testing allocation rule: he aims to write the least testing needed for a chosen confidence level, pays particular attention to mistakes he or his team repeatedly makes, and treats test-selection knowledge as immature enough to warrant experimentation. The surrounding comments qualify that personal-error emphasis with regression, maintenance, project-longevity, test-cost, coverage-metric, type-system, and test-layer concerns.

## Key Characteristics
- Introduced the term User Story in the source's account and is associated with its conversational requirements context.
- Associated with [[ExtremeProgramming]] as the practice context for user stories and test-guided incremental design.
- Credited with simple-design rules that favor small tested steps followed by refinement.
- Credited by a practitioner essay with the “make it work, make it right, make it fast” development sequence.
- Advocates adapting test effort to required confidence and recurring individual or team error patterns rather than maximizing test quantity.

## Evidence
- User-story lineage: [[blog-paulo-caroli-martinfowler-com-product-backlog-building-canvas]] says Beck introduced the User Story term as part of Extreme Programming to foster conversational requirements.
- Simple-design connection: [[dont-make-it-perfect-make-it-work-and-refine-8th-light]] cites Beck's Four Rules of Simple Design in an argument for the smallest tested solution, reversible decisions, and later refinement.
- Phase-order attribution: [[finding-time-to-become-a-better-developer]] credits Beck with a work-right-fast sequence and applies it to iterative software design.
- Confidence rule: [[kent-beck-i-get-paid-for-code-that-works-not-for-tests]] quotes Beck choosing the minimum testing needed for a confidence level and targeting error-prone logic.
- Team adaptation: [[kent-beck-i-get-paid-for-code-that-works-not-for-tests]] quotes Beck changing the strategy around mistakes the team collectively tends to make.
- Epistemic boundary: [[kent-beck-i-get-paid-for-code-that-works-not-for-tests]] quotes Beck treating universal test-selection theory as immature and recommending experimentation.

## Qualifications
This page records roles and statements attributed to Beck by four saved practitioner sources. It does not independently verify the exact origin of every aphorism or reconstruct Beck's broader work on XP, test-driven development, patterns, or software design. The testing source preserves Beck's explicit uncertainty, while commenters dispute whether individual and team mistake histories adequately cover long-term regression and maintenance risk. Their alternative claims about smoke tests, integration tests, coverage targets, and static types are not comparative evidence about Beck's full method.

## What Changed
- Added Beck's confidence-based test-selection rule and its adaptation to collective team mistakes.
- Added the source's explicit uncertainty about a universal theory of worthwhile tests.
- Preserved maintainability and regression objections as qualifications rather than attributing them to Beck.

## Relationships
- [[ExtremeProgramming]] - practice tradition in which the User Story term was introduced and tested incremental design is situated.
- [[UserStories]] - conversational requirements format attributed to Beck in the source.
- [[ProductBacklogBuilding]] - later canvas technique that builds on the user-story tradition.
- [[IterativeRefinement]] - Beck's cited simple-design rules and phase sequence support implementation followed by improvement.
- [[ConfidenceBasedTesting]] - formalizes the testing allocation philosophy quoted from Beck and debated by commenters.
- [[InternalSoftwareQuality]] - maintainability and change cost qualify the amount and kind of testing that is sufficient.

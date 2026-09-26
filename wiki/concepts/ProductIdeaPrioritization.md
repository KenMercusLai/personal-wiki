---
title: "Product Idea Prioritization"
type: concept
tags: [product-management, prioritization, growth]
sources:
  - being-a-product-manager-how-to-get-your-products-built
  - building-products-the-year-of-the-looking-glass-medium
  - calculate-what-feature-to-build-next-baremetrics
last_updated: 2026-09-26
knowledge_schema: synthesis-v1
---

## Definition
[[ProductIdeaPrioritization]] is the practice of generating, comparing, and ranking product proposals by expected business or user impact, effort or difficulty, evidence quality, and the growth or retention mechanism they are meant to improve.

## Current Synthesis
The sources present prioritization as a pre-greenlight discipline for product teams with more ideas than development capacity. PMInsider emphasizes scoring ideas by potential impact on company KPIs and difficulty to build, then sorting them into growth, activation, engagement, reactivation, and revenue. Baremetrics makes customer evidence explicit through its DIE score: Demand represents repeated requests or observed problems, Impact asks how strongly the feature could move the company's current goal, and Effort captures the design, research, engineering, time, and money required. Lower combined scores rank more favorably, with high-demand, high-impact, XS-effort work as the ideal case.

Building Products adds an upstream exploration discipline: before a team chooses a winner, it should go broad enough to expose non-obvious solutions, then use empirical evidence, higher-fidelity prototypes, and user reactions to narrow the set. Together, the sources make prioritization a business and learning argument rather than only a taste argument: a PM should be able to explain which scoreboard the idea moves, what customer evidence supports demand, why the expected behavior matters, what alternatives were considered, and what delivery tradeoff the team is accepting.

PMInsider's category list also keeps growth from collapsing into acquisition alone. Growth means signups and invite loops; activation means reaching the magic moment quickly; engagement means getting existing users to participate more often; reactivation means bringing dormant users back through channels such as push or email; and revenue means creating money while preserving the core user experience. Building Products adds that a thin exploration set is itself a warning sign: if a team cannot answer whether it considered another plausible solution, the prioritization process may have skipped the creative breadth needed before scoring or testing.

## Key Claims
- Product teams need a way to choose among many plausible ideas before development is greenlit.
- Strong scoring compares customer demand, KPI or goal impact, and build difficulty while treating unsupported hunches as weak demand evidence.
- Coarse effort bands can reduce false precision when delivery estimates are inherently uncertain, but scores should structure judgment rather than automatically decide the roadmap.
- Product ideas can be grouped by growth, activation, engagement, reactivation, and revenue.
- Activation ideas depend on identifying the product's magic moment and accelerating new users toward it.
- Reactivation work needs personalization, timing, and context so push or email messages do not become spam.
- Revenue ideas should preserve the core user experience, and prioritization should follow broad solution exploration and empirical narrowing rather than premature commitment.

## Evidence
- Scoring dimensions: [[being-a-product-manager-how-to-get-your-products-built]] recommends assigning scores based on potential KPI impact and difficulty to build.
- Growth bucket: [[being-a-product-manager-how-to-get-your-products-built]] defines growth ideas as products that drive signups and invite loops, including incentivized invites.
- Activation bucket: [[being-a-product-manager-how-to-get-your-products-built]] says activation ideas improve early retention by getting users to the magic moment quickly.
- Engagement bucket: [[being-a-product-manager-how-to-get-your-products-built]] uses [[Facebook]] News Feed as the canonical example of a feature that made existing users more active.
- Reactivation bucket: [[being-a-product-manager-how-to-get-your-products-built]] says dormant users must be reached outside the core experience, usually through push or email.
- Revenue bucket: [[being-a-product-manager-how-to-get-your-products-built]] argues that revenue ideas should create money without damaging the core experience.
- Broad exploration: [[building-products-the-year-of-the-looking-glass-medium]] recommends brainstorming 10, 20, or 50 solutions before picking a winner because later ideas are less likely to be obvious.
- Alternative-check warning: [[building-products-the-year-of-the-looking-glass-medium]] treats "have you considered X?" with no prior answer as a red flag about weak exploration.
- Evidence-based narrowing: [[building-products-the-year-of-the-looking-glass-medium]] recommends team favorites, higher-fidelity designs or prototypes, and user reactions to choose among candidate ideas.
- DIE dimensions: [[calculate-what-feature-to-build-next-baremetrics]] evaluates each recorded idea through demonstrated demand, impact on the current company goal, and estimated effort.
- Demand quality: [[calculate-what-feature-to-build-next-baremetrics]] rates recurring requests or observed customer problems above an unevidenced founder hunch.
- Coarse effort: [[calculate-what-feature-to-build-next-baremetrics]] uses XS-to-XL bands to avoid overanalyzing uncertain estimates while allowing days or money as alternatives.
- Decision-aid boundary: [[calculate-what-feature-to-build-next-baremetrics]] says a lower score favors a feature but does not categorically make the decision.

## Counterevidence & Qualifications
The sources are practitioner guidance, not formal prioritization frameworks with calibrated scoring, empirical weights, or controlled comparisons. Baremetrics provides endpoint examples of 3 and 11 but the supplied prose does not specify every rating-to-number mapping, validate the scale, or show that ordinal demand, impact, and effort judgments are commensurable. Customer requests can overrepresent vocal users, impact is hard to forecast, and effort estimates can be wrong. A five-bucket growth taxonomy may also miss risk reduction, infrastructure, quality, compliance, accessibility, or strategic-option work. Broad ideation can become theater if the team generates many weak options without evidence, constraints, or target-user clarity, while a neat score can conceal strategic dependencies or confidence differences among estimates.

## What Changed
- Added explicit customer demand to KPI impact and build difficulty as a prioritization dimension.
- Added DIE's lower-is-better ranking and its high-demand, high-impact, low-effort ideal.
- Added coarse effort bands as a defense against false precision.
- Clarified that scoring guides judgment rather than automatically choosing a roadmap.

## Related Concepts
- [[ProductManagement]] - product idea prioritization is one pre-greenlight responsibility of the PM.
- [[ProductMetricLadder]] - prioritization depends on knowing which company or product metric an idea should move.
- [[GrowthHacking]] - several buckets overlap with product-led growth mechanisms.
- [[ViralLoops]] - invite loops are one growth-prioritization category.
- [[ProductFlowFriction]] - activation prioritization often means reducing the path to the product's magic moment.
- [[ProductLedRetention]] - activation, engagement, and reactivation ideas are retention-adjacent prioritization categories.
- [[StartupHypothesisTesting]] - prioritized ideas become stronger when they are framed as testable assumptions.
- [[CustomerLedProductDevelopment]] - customer requests and observed problems provide evidence for the demand dimension.

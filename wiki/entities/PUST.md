---
title: "PUST"
type: entity
tags: [project, government, software, agile]
sources:
  - crisps-blog-making-sense-of-mvp-minimum-viable-product-and-why-i-prefer-earliest-testable-usable-lovable
last_updated: 2026-09-26
knowledge_schema: synthesis-v1
---

## Overview
[[PUST]] was a Swedish Police field-investigation software initiative used in the source to contrast bounded rollout and feedback with a later big-bang replacement.

## Current Profile
The source describes the 60-person PUST Java project as reducing scope along two dimensions: it initially supported only a few crime types and only a handful of officers in Östergötland. Their harsh feedback changed assumptions and drove improvements before the system expanded to more crimes, regions, and an eventual nationwide rollout to 12,000 police. Kniberg contrasts this with PUST Siebel, which reportedly spent two years in analysis and testing without real-user releases before a nationwide launch and shutdown.

## Key Characteristics
- Sliced initial scope by both geography and crime type.
- Used a small group of informed field testers before nationwide rollout.
- Fed operational criticism back into product changes.
- Expanded only after users in the first region began accepting the system.
- Serves as a contrast between staged external validation and big-bang replacement.

## Evidence
- Scope design: [[crisps-blog-making-sense-of-mvp-minimum-viable-product-and-why-i-prefer-earliest-testable-usable-lovable]] says version 1.0 covered a few crime types and a handful of officers in Östergötland.
- Feedback loop: [[crisps-blog-making-sense-of-mvp-minimum-viable-product-and-why-i-prefer-earliest-testable-usable-lovable]] reports that user feedback invalidated assumptions and displaced some up-front use-case specifications.
- Expansion: [[crisps-blog-making-sense-of-mvp-minimum-viable-product-and-why-i-prefer-earliest-testable-usable-lovable]] describes progressive regional and crime-type growth before nationwide training and rollout.
- Failure contrast: [[crisps-blog-making-sense-of-mvp-minimum-viable-product-and-why-i-prefer-earliest-testable-usable-lovable]] attributes the later PUST Siebel failure to prolonged analysis without release followed by simultaneous deployment.

## Qualifications
The account comes from a coach involved in the earlier project and supplies no independent project records or controlled comparison. Its cost, award, rollout, and societal-loss figures are reported through the essay and should be treated as source-scoped. The projects also differed in technology and context, so release strategy cannot be isolated as the sole cause of their different outcomes.

## What Changed
- Created the entity as a staged government-software rollout case.
- Preserved the later replacement as a qualified failure contrast rather than a controlled comparison.

## Relationships
- [[HenrikKniberg]] - reports coaching the PUST Java project.
- [[EarliestTestableUsableLovable]] - PUST 1.0 illustrates a bounded early usable release.
- [[MinimumViableProduct]] - limited crime and regional scope served as the project's first evidence-producing product.
- [[AgileSoftwareDevelopment]] - staged field release created repeated opportunities for adaptation.

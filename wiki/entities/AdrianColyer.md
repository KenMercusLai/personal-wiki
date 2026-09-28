---
title: "Adrian Colyer"
type: entity
tags: [person, software-architecture, distributed-systems]
sources:
  - getting-beyond-mvp-the-morning-paper
last_updated: 2026-09-28
knowledge_schema: synthesis-v1
---

## Overview
[[AdrianColyer]] is represented here as the author of *the morning paper*, applying classic modular-design ideas to the engineering transition after a successful [[MinimumViableProduct]].

## Current Profile
Colyer presents prototype code as a context-dependent tradeoff rather than a moral failure: rapid transaction scripts and manual testing may be rational while a team is testing demand. Once real users make continued operation likely, he recommends installing a deployment safety loop and growing tested abstractions from the bottom upward while customer-visible development continues.

## Key Characteristics
- Translates older software-design ideas into a practical startup-codebase migration.
- Favors incremental restructuring over pausing delivery for a second-system rewrite.
- Builds from tested low-level modules toward more powerful higher-level abstractions.
- Uses thin vertical feature towers to combine product progress with structural improvement.
- Treats the target domain model and module hierarchy as sketches that should change with learning.

## Evidence
- Context-sensitive prototype judgment: [[getting-beyond-mvp-the-morning-paper]] says a quickly built MVP may appropriately avoid engineering whose value depends on the product surviving validation.
- Safety baseline: [[getting-beyond-mvp-the-morning-paper]] requires CI, automatic staging deployment, and production promotion before structural work.
- Bottom-up migration: [[getting-beyond-mvp-the-morning-paper]] proposes extracting and testing low-level modules, then refactoring existing transaction scripts to use them.
- Feature continuity: [[getting-beyond-mvp-the-morning-paper]] proposes bottom-to-top feature towers so external progress continues while the internal foundation improves.

## Qualifications
This profile is bounded to one 2016 practitioner essay and its appended discussion, not an independent biography or evaluation of Colyer's broader work. The article does not compare migration strategies empirically, quantify the engineering allocation, or show that its preferred module hierarchy generalizes to every technology, team, or risk environment.

## What Changed
- Created a source-bounded profile around Colyer's post-MVP modernization guidance.

## Relationships
- [[MinimumViableProduct]] - starting context whose engineering tradeoffs change after validation.
- [[IncrementalMVPModernization]] - bottom-up migration strategy he proposes.
- [[ContinuousDelivery]] - safety baseline he installs before structural refactoring.
- [[ModularMonolith]] - adjacent architecture that preserves one deployment while improving internal boundaries.
- [[InternalSoftwareQuality]] - intended source of safer changes, easier onboarding, and sustained delivery speed.

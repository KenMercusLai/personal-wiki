---
title: "Zellij"
type: entity
tags: [software-project, geometry, python]
sources:
  - do-one-thing
last_updated: 2026-09-27
knowledge_schema: synthesis-v1
---

## Overview
[[Zellij]] is [[NedBatchelder]]'s geometric software toy, used in “Do one thing” as a concrete case of discovering a narrower responsibility boundary through refactoring.

## Current Profile
Zellij needed to treat two-dimensional points with slight numeric differences as equivalent. Batchelder first combined that fuzzy matching with keyed storage in `PointMap`. When other parts of the project needed the same matching behavior to make nearly equal points exactly equal, he extracted a `Defuzzer` class and replaced the custom mapping behavior with `Defuzzer` plus a standard dictionary.

The project matters to the source as an evolutionary design case: changing usage revealed that fuzzy equality was the reusable responsibility, while point storage could remain a standard collection concern.

## Key Characteristics
- Geometric project handling two-dimensional points and floating-point inaccuracy.
- Originally used a custom `PointMap` for fuzzy equality and keyed storage.
- Later extracted `Defuzzer` as the narrower reusable matching abstraction.
- Demonstrates how new uses can reveal a better software boundary over time.

## Evidence
- Original design: [[do-one-thing]] says `PointMap` stored values by points while accommodating slight inaccuracies.
- Reuse pressure: [[do-one-thing]] says the project later needed fuzzy equality to align nearly equal points outside the map.
- New composition: [[do-one-thing]] says `Defuzzer` plus a standard dictionary replaced `PointMap` with a simpler arrangement.

## Qualifications
The source provides a design narrative rather than code metrics, maintenance outcomes, or a full architectural account. It supports the usefulness of this extraction in Batchelder's context, not a general rule that every combined abstraction should be split.

## What Changed
- Created the project profile from Batchelder's refactoring example.

## Relationships
- [[NedBatchelder]] - developer who used Zellij to explain evolving responsibility boundaries.
- [[SingleResponsibilityPrinciple]] - Zellij provides the source's main example of interpreting the principle over time.
- [[FunctionDesign]] - the extraction illustrates how reuse pressure can reshape code-unit boundaries.

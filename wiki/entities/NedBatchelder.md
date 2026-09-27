---
title: "Ned Batchelder"
type: entity
tags: [software-developer, author, python]
sources:
  - do-one-thing
last_updated: 2026-09-27
knowledge_schema: synthesis-v1
---

## Overview
[[NedBatchelder]] is a software developer and author represented here by an essay about the ambiguity of the [[SingleResponsibilityPrinciple]] and a refactoring in his geometric toy [[Zellij]].

## Current Profile
Batchelder favors single responsibility as a design direction while rejecting claims that it yields precise, binary compliance decisions. His account emphasizes that useful abstractions emerge through work: `PointMap` originally seemed cohesive, but a later need to reuse fuzzy point matching led him to extract `Defuzzer` and combine it with a standard dictionary.

His teaching stance is correspondingly explicit about uncertainty. Principles can orient design, but examples should show how scope, reuse, surrounding code, and changing understanding affect the boundary instead of presenting subjective judgment as rule violation.

## Key Characteristics
- Treats software-design principles as judgment aids rather than mechanically enforceable laws.
- Uses a concrete refactoring from his own project to examine changing abstraction boundaries.
- Values smaller abstractions when they improve independent reuse and simplify composition.
- Advocates teaching the ambiguity and evolution of design decisions openly.

## Evidence
- Principle stance: [[do-one-thing]] calls single responsibility a good idea while arguing that it is neither quantifiable nor precise.
- Refactoring practice: [[do-one-thing]] describes extracting `Defuzzer` from `PointMap` when fuzzy point equality became useful elsewhere in Zellij.
- Teaching position: [[do-one-thing]] argues that presenting subjective design judgment as binary violation does learners a disservice.

## Qualifications
This profile comes from one 2018 essay and its comment thread. It establishes Batchelder's view of this design principle, not a comprehensive account of his software work or later positions.

## What Changed
- Created the profile from “Do one thing.”

## Relationships
- [[Zellij]] - Batchelder's geometric toy supplies the essay's refactoring example.
- [[SingleResponsibilityPrinciple]] - Batchelder supports its goal while emphasizing its interpretive boundary.
- [[FunctionDesign]] - his critique qualifies function-level “do one thing” advice.

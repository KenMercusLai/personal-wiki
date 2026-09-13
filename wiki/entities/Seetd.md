---
title: "seetd"
type: entity
tags: [tool, optimization, workplace]
sources:
  - be-smarter-be-seetd-stitch-fix-technology-multithreaded
last_updated: 2026-09-14
knowledge_schema: synthesis-v1
---

## Overview
[[Seetd]] is a [[StitchFix]] seating-allocation tool that casts people-to-seat assignment as a multi-term optimization problem.

## Current Profile
The source describes seetd as a practical tool for going beyond random office seating. It models seating through a cost function with terms for team placement, personal preferences, distance from current seats, new-neighbor distance, and optionally past configurations. Its search procedure combines [[SimulatedAnnealing]] with local optimization: simulated annealing explores the assignment space and can accept worse moves, while the local step greedily accepts nearby improvements after a candidate arrangement is accepted.

## Key Characteristics
- Allocates people to seats or offices by minimizing a weighted objective function.
- Supports subjective organizational choices by converting them into explicit cost terms.
- Can encourage teams to cluster or disperse by changing team-specific interaction weights.
- Uses assignment-matrix terms for preferences and movement away from current seats.
- Uses simulated annealing plus local search to find approximate low-cost arrangements.

## Evidence
- Objective-function design: [[be-smarter-be-seetd-stitch-fix-technology-multithreaded]] says seetd casts people-to-seat allocation as an optimization problem with several cost terms.
- Team controls: [[be-smarter-be-seetd-stitch-fix-technology-multithreaded]] explains team-by-team interaction terms that can push members apart or make them agglomerate.
- Preference and movement terms: [[be-smarter-be-seetd-stitch-fix-technology-multithreaded]] describes matrices for seat preferences and distance from current location.
- Search method: [[be-smarter-be-seetd-stitch-fix-technology-multithreaded]] presents simulated annealing with local optimization pseudocode.

## Qualifications
The article explains the modeling and optimization approach, but it does not report adoption outcomes, employee satisfaction data, productivity measurements, or the full source code inside the ingested Markdown. Several referenced GIFs were missing locally, so the animation evidence could not be independently inspected.

## What Changed
- Created seetd as the internal seating-allocation tool from the Stitch Fix source.

## Relationships
- [[StitchFix]] - developer and organizational context for the tool.
- [[OfficeSeatingOptimization]] - problem domain seetd addresses.
- [[SimulatedAnnealing]] - global-search method used by seetd.
- [[LinearProgramming]] - simpler preference-only assignment subproblem mentioned in the source.

---
title: "Linear Programming"
type: concept
tags: [optimization, mathematics, algorithms]
sources:
  - be-smarter-be-seetd-stitch-fix-technology-multithreaded
last_updated: 2026-09-14
knowledge_schema: synthesis-v1
---

## Definition
[[LinearProgramming]] is an optimization approach for maximizing or minimizing a linear objective subject to linear constraints.

## Current Synthesis
The Stitch Fix source mentions linear programming as the natural method for simpler seating subproblems, especially when the goal is to maximize individual seat preferences under one-person-per-seat and one-seat-per-person assignment constraints. In the broader seetd model, the problem becomes richer than this preference-only formulation because team-distance costs, neighbor-distance changes, past configurations, and nonlinear distance weighting add objectives that motivate more flexible search.

## Key Claims
- Person-by-seat assignment can be represented as a matrix with row and column constraints.
- Preference maximization becomes a linear objective when each person-seat pair has a preference weight.
- Linear programming is appropriate for simpler formulations where the objective and constraints remain linear.
- More complex seating objectives can push the problem toward heuristic search methods such as [[SimulatedAnnealing]].

## Evidence
- Assignment matrix: [[be-smarter-be-seetd-stitch-fix-technology-multithreaded]] defines a matrix whose rows represent people and columns represent seats.
- Constraint structure: [[be-smarter-be-seetd-stitch-fix-technology-multithreaded]] requires each person to occupy one seat and each seat to hold one person.
- Preference objective: [[be-smarter-be-seetd-stitch-fix-technology-multithreaded]] encodes personal seat preferences as another matrix and says such maximization or minimization functions are readily solved with linear programming.
- Broader model: [[be-smarter-be-seetd-stitch-fix-technology-multithreaded]] then combines preference-like terms with team, current-seat, neighbor, and past-configuration costs.

## Counterevidence & Qualifications
The source only briefly mentions linear programming and does not describe solver choice, integrality conditions, runtime, or how the assignment constraints are handled in production. This page should be expanded with stronger sources before being treated as a general reference on linear programming.

## What Changed
- Created linear programming as the simpler optimization frame referenced by the seating-allocation article.

## Related Concepts
- [[OfficeSeatingOptimization]] - includes assignment-matrix formulations that can become linear programs.
- [[SimulatedAnnealing]] - contrasts as a flexible heuristic used when the full objective becomes more complex.
- [[ComputationalThinking]] - relates through representing messy allocation decisions as formal variables and constraints.
- [[Seetd]] - source tool that mentions linear programming before using simulated annealing for the full model.

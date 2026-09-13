---
title: "Simulated Annealing"
type: concept
tags: [optimization, algorithms, search]
sources:
  - be-smarter-be-seetd-stitch-fix-technology-multithreaded
last_updated: 2026-09-14
knowledge_schema: synthesis-v1
---

## Definition
[[SimulatedAnnealing]] is a probabilistic optimization method that explores neighboring candidate solutions and sometimes accepts worse moves according to a temperature-controlled probability.

## Current Synthesis
The Stitch Fix source uses simulated annealing for office seating because the assignment problem can include many cost terms and future constraints. Unlike a purely greedy search, simulated annealing can move uphill in the cost landscape, giving it a chance to escape local minima before the temperature schedule makes worse moves less likely. In [[Seetd]], this global exploration is paired with a local greedy step that accepts immediate neighbor swaps when they lower the seating cost.

## Key Claims
- Simulated annealing is useful for hard or flexible optimization problems where exact methods may be awkward or too restrictive.
- Accepting worse moves with finite probability helps the search escape local minima.
- The temperature parameter controls how often worse moves are accepted.
- Annealing reduces that acceptance tendency over time, shifting from exploration toward exploitation.
- Pairing simulated annealing with local search can improve candidate solutions after broader exploration.

## Evidence
- Method choice: [[be-smarter-be-seetd-stitch-fix-technology-multithreaded]] says seetd solves seating assignments with simulated annealing and local optimization.
- Local-minima rationale: [[be-smarter-be-seetd-stitch-fix-technology-multithreaded]] explains that simulated annealing can find approximate global solutions by moving in directions that increase the cost function.
- Temperature behavior: [[be-smarter-be-seetd-stitch-fix-technology-multithreaded]] describes high temperature as accepting worse moves more often and low temperature as rarely doing so.
- Hybrid procedure: [[be-smarter-be-seetd-stitch-fix-technology-multithreaded]] shows pseudocode that accepts a candidate, then applies `local_optimize`.

## Counterevidence & Qualifications
The source provides an applied explanation rather than a proof of convergence or parameter-tuning guide. It does not compare simulated annealing with exact assignment solvers, integer programming, genetic algorithms, constraint programming, or other metaheuristics for this seating problem.

## What Changed
- Created simulated annealing as the source's approximate search method for seetd.

## Related Concepts
- [[OfficeSeatingOptimization]] - applied problem where the source uses simulated annealing.
- [[Seetd]] - tool that combines simulated annealing with local optimization.
- [[StochasticGradientDescent]] - relates as another optimization method that balances iterative movement with objective improvement.
- [[ComputationalThinking]] - relates through algorithmic search over a modeled problem space.
- [[LinearProgramming]] - contrasts with simpler exact optimization when the objective and constraints stay linear.

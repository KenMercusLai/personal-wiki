---
title: "Office Seating Optimization"
type: concept
tags: [optimization, workplace, operations]
sources:
  - be-smarter-be-seetd-stitch-fix-technology-multithreaded
last_updated: 2026-09-14
knowledge_schema: synthesis-v1
---

## Definition
[[OfficeSeatingOptimization]] is the practice of assigning people to desks or offices by translating collaboration, preference, movement, and adjacency goals into constraints and weighted cost terms.

## Current Synthesis
The Stitch Fix source treats seating as a case where subjective workplace preferences can become objective computation after the organization chooses its criteria. A seating arrangement can favor team clustering, team dispersion, personal seat preferences, movement away from current seats, new neighbor exposure, and distance from past configurations. The durable lesson is not that the mathematically lowest-cost seating chart is inherently best, but that explicit objective terms make tradeoffs inspectable and tunable.

## Key Claims
- Random seating can avoid obvious extrema, but more directed seating requires making implicit goals explicit.
- Team-placement goals can be represented by neighbor or distance-weighted interactions among people or sub-teams.
- Assignment matrices can encode one-person-per-seat constraints as well as individual seat preferences.
- Moving people away from current seats and current neighbors can be modeled as additional cost terms.
- Cost-term weighting matters because heterogeneous objectives otherwise dominate each other arbitrarily.
- Seating optimization remains approximate and policy-laden: the model depends on which human goals are chosen before optimization begins.

## Evidence
- Modeling move: [[be-smarter-be-seetd-stitch-fix-technology-multithreaded]] casts people-to-seat allocation as an optimization problem after subjective criteria are selected.
- Team interactions: [[be-smarter-be-seetd-stitch-fix-technology-multithreaded]] compares same-team neighbor terms to spin-glass Hamiltonians and later extends them with distance weighting and team-specific signs.
- Assignment constraints: [[be-smarter-be-seetd-stitch-fix-technology-multithreaded]] describes a person-by-seat matrix with row and column constraints for one person per seat and one seat per person.
- Movement and new-neighbor terms: [[be-smarter-be-seetd-stitch-fix-technology-multithreaded]] adds costs based on distance from current locations and current neighbors.
- Weighting: [[be-smarter-be-seetd-stitch-fix-technology-multithreaded]] proposes using random configurations to estimate average term values and scale terms onto roughly equal footing.

## Counterevidence & Qualifications
The source does not prove that optimized seating improves collaboration, comfort, or productivity. Its model depends on chosen cost terms and weights, so the main risk is false objectivity: a precise optimizer can only optimize the organization's selected proxy goals.

## What Changed
- Created the concept page for office seating as a weighted, constraint-based optimization problem.

## Related Concepts
- [[SimulatedAnnealing]] - provides the approximate search method used for complex seating objectives.
- [[ComputationalThinking]] - relates through decomposition of a workplace problem into variables, constraints, and algorithms.
- [[WorkEnvironment]] - seating is one material component of the workplace field.
- [[LinearProgramming]] - solves simpler assignment formulations when the objective remains linear.
- [[Seetd]] - concrete tool implementing the source's seating optimization model.

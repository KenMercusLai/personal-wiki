---
title: "Be smarter. Be seetd. | Stitch Fix Technology - Multithreaded"
type: source
tags: [optimization, workplace, data-science]
date: 2017-06-29
source_file: /mnt/ken_personal_wiki/Articles/Be smarter. Be seetd. - Stitch Fix Technology – Multithreaded.md
---

## Summary
This Stitch Fix Technology post presents [[Seetd]], an internal tool that assigns people to office seats by treating seating as a weighted optimization problem. The model combines team-neighbor costs, personal seat preferences, distance from current seats, and distance from current neighbors, then searches for low-cost arrangements using [[SimulatedAnnealing]] plus local greedy improvement. The article frames office layout as a playful but real instance of [[OfficeSeatingOptimization]], with analogies to spin glasses, urban segregation models, logistics, economics, and magnetism.

## Key Claims
- [[OfficeSeatingOptimization]] can turn subjective workplace goals into objective cost terms once the organization chooses which factors matter.
- Team seating can be modeled through neighbor or distance-weighted interactions, allowing different sub-teams to be dispersed or clustered by changing interaction signs and strengths.
- Personal preferences and distance-from-current-seat terms can be represented as assignment-matrix costs under one-person-per-seat and one-seat-per-person constraints.
- New-neighbor costs can encourage people who were previously close together to sit farther apart in the next arrangement.
- Weighting cost terms by averages from random configurations can put heterogeneous objectives on roughly equal footing before optimization.
- [[SimulatedAnnealing]] is useful because it can accept temporary cost increases, escape local minima, and support future complex seating constraints.
- The available preview image is decorative/title-like: it shows seetd branding over a forest background with the tagline "You like to sit. seetd does too." The local Markdown references four optimization GIFs and one title image that were not present on disk during ingest, so their details could not be independently inspected.

## Key Quotes
> "casting the allocation of people to seats (or offices) as an optimization problem" - the source's central modeling move.

> "The ultimate goal is to then find an arrangement which minimises our overall cost function." - the article's framing of seating allocation as cost minimization.

## Connections
- [[StitchFix]] - company and technology-blog context for the post.
- [[Seetd]] - internal seating allocation tool described by the article.
- [[OfficeSeatingOptimization]] - core problem formulation across teams, preferences, neighbor changes, and past configurations.
- [[SimulatedAnnealing]] - optimization method used with local search to find low-cost seating assignments.
- [[ComputationalThinking]] - the article decomposes a messy office-planning problem into variables, constraints, cost terms, and search procedures.
- [[LinearProgramming]] - preference-only assignment costs are described as readily solved with linear programming.

## Contradictions
- No direct contradictions found. The source complements existing optimization material by applying cost-function thinking to workplace seating rather than cloud spend, conversion funnels, or performance estimation.

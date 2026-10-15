---
title: "Nonmonotonic Reasoning"
type: concept
tags: [artificial-intelligence, default-reasoning, knowledge-representation, uncertainty]
sources:
  - "2309.02009"
last_updated: 2026-10-15
knowledge_schema: synthesis-v1
---

## Definition
[[NonmonotonicReasoning]] draws defeasible conclusions from incomplete information and permits those conclusions to be withdrawn when exceptions or stronger information arrive.

## Current Synthesis
The current source treats nonmonotonic reasoning as the mechanism that lets a joke listener go beyond the literal setup. Strict rules form integrity constraints, while default rules rank interpretations so normal cases are preferred over exceptional ones. The context can therefore induce a provisional conclusion without entailing it classically; the punchline redirects reasoning to an exceptional but explanatory interpretation.

Possibility distributions, System-Z-style stratification, best-out ordering, and lexicographic ordering are presented as ways to derive the required plausibility preorder. The choice among orderings matters: the paper's doctor-office example is revealing under the finer lexicographic ranking but not under the coarser best-out ranking.

## Key Claims
- Default conclusions let an agent interpret incomplete situations without enumerating every exception.
- A set of strict formulas and consistent defaults can induce an ordering over interpretations and thereby a [[BeliefRevision]] policy.
- A listener using only strict rules does not form the defeasible expectation required by the paper's definition of surprise.
- Different default-ranking methods can change whether a punchline counts as revealing.
- Treating a default as a norm makes its exceptional violation a candidate source of incongruity.

## Evidence
- Default mechanism: [[2309.02009]] translates defaults into comparative possibility constraints and derives preferred interpretations.
- Psycho-rigidity result: [[2309.02009]] proves that an empty default set prevents a consistent context-punchline pair from being potentially funny under the proposed construction.
- Ordering sensitivity: [[2309.02009]] shows that lexicographic and best-out rankings differ on whether the waiting-room punchline explains reluctance.

## Counterevidence & Qualifications
The formal result applies to the paper's specific definition of potential funniness and its induced revision construction; it does not show that people who reason cautiously cannot experience humor. Real listeners may use graded, probabilistic, linguistic, social, or embodied expectations that are not captured by propositional defaults. The source assumes consistent strict and default bases and does not explain how a natural-language narrative is mapped into them.

## What Changed
- Created the concept around defeasible expectations and exception-sensitive joke interpretation.
- Added the distinction between strict integrity constraints and ranked defaults.
- Recorded that ordering choice can change the analysis.

## Related Concepts
- [[BeliefRevision]] - selects preferred models after new context or punchline information arrives.
- [[IncongruityResolution]] - interprets a violated default or strict rule as a listener-relative norm.
- [[ComputationalHumor]] - uses defeasible expectation formation as one component of joke comprehension.
- [[BayesianUpdating]] - also revises belief under uncertainty but through probabilistic rather than default-logical machinery.

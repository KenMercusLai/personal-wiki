---
title: "Stable Matching"
type: concept
tags: [combinatorics, matching, algorithms, vector-search]
sources:
  - combinatorial-stable-marriages-for-dbms-semantic-joins
last_updated: 2026-10-11
knowledge_schema: synthesis-v1
---

## Definition
[[StableMatching]] pairs members of two groups so that no unmatched pair would both prefer one another to their assigned partners.

## Current Synthesis
The classical proposal procedure assumes explicit rankings: a free proposer approaches the highest-ranked candidate not yet tried, and the recipient keeps the preferred proposal while releasing any current partner. The source emphasizes that storing complete rankings becomes the dominant obstacle at extreme scale, even before the proposal loop runs.

Its database adaptation replaces stored rankings with candidate lists retrieved from vector indexes. That makes the process operationally different from classical exact matching: similarity models stand in for declared preferences, approximate search may omit candidates, and a proposal cap terminates work. The design preserves the proposal-and-displacement structure but weakens any automatic claim to exact stability over complete underlying rankings.

## Key Claims
- Stability is a pairwise blocking condition, not a claim that every participant receives a globally optimal partner.
- Classical proposal algorithms depend on access to ordered preferences for both groups.
- Complete preferences require quadratic storage when both groups grow together.
- Unequal group sizes can be accommodated by changing termination conditions.
- On-demand approximate candidate retrieval reduces stored preference state but introduces search error and incomplete exploration.
- Proposal caps create a practical convergence boundary rather than an unconditional exact guarantee.

## Evidence
- Stability condition: [[combinatorial-stable-marriages-for-dbms-semantic-joins]] defines a solution as stable when no man and woman both prefer each other to their current partners.
- Proposal mechanics: [[combinatorial-stable-marriages-for-dbms-semantic-joins]] reproduces the Gale-Shapley loop in which recipients retain a preferred proposer and free the displaced partner.
- Storage pressure: [[combinatorial-stable-marriages-for-dbms-semantic-joins]] uses a billion-by-billion population to illustrate the infeasibility of complete materialized rankings.
- Mismatched sets: [[combinatorial-stable-marriages-for-dbms-semantic-joins]] cites McVitie and Wilson's termination-condition modification.
- Approximate adaptation: [[combinatorial-stable-marriages-for-dbms-semantic-joins]] replaces lists with two USearch indexes and limits proposals per participant.

## Counterevidence & Qualifications
The source's memory and dollar estimates are illustrative and contain malformed formatting in the supplied Markdown; they are not independently checked here. Its binary dating metaphor is inherited from the classical presentation and does not define the range of real matching-market structures. Vector similarity also encodes model behavior rather than genuine human preferences, and approximate retrieval plus early stopping can alter stability and fairness.

## What Changed
- Established the classical stability condition and its memory-bounded vector-search adaptation.
- Made explicit the guarantee gap between complete rankings and approximate, capped proposals.

## Related Concepts
- [[SemanticJoin]] - applies stable-matching mechanics to database records in a shared vector space.
- [[ApproximateNearestNeighborSearch]] - retrieves proposed partners dynamically.
- [[Embeddings]] - convert records into the similarity space used as a preference proxy.
- [[NeuralSemanticMatching]] - related use of learned representations to score compatibility between items.

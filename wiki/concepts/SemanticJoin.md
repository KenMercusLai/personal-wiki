---
title: "Semantic Join"
type: concept
tags: [databases, vector-search, matching, embeddings]
sources:
  - combinatorial-stable-marriages-for-dbms-semantic-joins
last_updated: 2026-10-11
knowledge_schema: synthesis-v1
---

## Definition
A [[SemanticJoin]] pairs records across two collections according to learned vector similarity and a matching rule rather than equality of explicit keys.

## Current Synthesis
The source's design combines two ideas: [[ApproximateNearestNeighborSearch]] generates candidates on demand, and [[StableMatching]] resolves competing preferences into one-to-one pairs. This removes the need to materialize every pairwise ranking, making very large candidate spaces conceivable by exchanging quadratic memory for repeated search and bounded proposal work.

The benchmark also shows why retrieval quality and join quality are not interchangeable. Correct pairing requires the true counterpart to rank well across both collections and survive global competition from other proposals. In the reported text experiment, within-collection self-recall remained near perfect while cross-recall and correct joins declined with collection size. Image-text representations failed more sharply, so a fast index cannot compensate for a poorly aligned shared space.

## Key Claims
- Dynamic candidate search can replace complete stored preference lists with a compute-for-memory tradeoff.
- A semantic join is a global matching problem, not merely independent nearest-neighbor retrieval for every row.
- Cross-collection recall is more relevant than within-collection self-recall, but it still does not by itself guarantee correct final pairs.
- Larger candidate pools introduce more competitors and can reduce correct join rates even when average paired similarity stays stable.
- Quantization can improve execution efficiency without materially changing join quality in at least the reported text workload.
- Multimodal semantic joins are constrained primarily by cross-modal representation alignment in the reported experiments.

## Evidence
- Memory substitution: [[combinatorial-stable-marriages-for-dbms-semantic-joins]] proposes encoding both populations, building two ANN indexes, and recomputing candidate preferences when needed.
- Global pairing: [[combinatorial-stable-marriages-for-dbms-semantic-joins]] adapts proposal-and-displacement logic rather than independently assigning every record its nearest neighbor.
- Text scaling: [[combinatorial-stable-marriages-for-dbms-semantic-joins]] reports correct title-abstract joins declining from 87.85% at 10,000 records to 57.67% at one million.
- Quantization: [[combinatorial-stable-marriages-for-dbms-semantic-joins]] reports 57.59% correct joins at one million with int8 E5 vectors versus 57.67% with float32.
- Multimodal limit: [[combinatorial-stable-marriages-for-dbms-semantic-joins]] reports 9.02% correct OpenCLIP ViT-B-16 image-text joins and 13.46% for ViT-G/14 at one million pairs.

## Counterevidence & Qualifications
The article evaluates known one-to-one paired datasets, not noisy production tables with duplicates, missing counterparts, asymmetric cardinalities, evolving records, fairness constraints, or no valid match. Its approximate search and proposal cap can stop before exploring all preferences, so the result should not be assumed to satisfy the exact stability guarantee of complete Gale-Shapley rankings. All displayed results come from one implementation and fixed model/dataset choices.

## What Changed
- Established semantic joins as a composition of candidate retrieval, competitive matching, and shared-space representation quality.
- Distinguished self-recall, cross-recall, joined coverage, and correct-join rate as separate evaluation layers.

## Related Concepts
- [[StableMatching]] - supplies the proposal-and-displacement matching rule.
- [[ApproximateNearestNeighborSearch]] - generates candidate preferences without exhaustive comparison.
- [[Embeddings]] - define the semantic geometry used to rank cross-collection candidates.
- [[HNSWIndex]] - graph index used by the source's implementation.
- [[VectorDatabase]] - database category into which semantic join capability could be integrated.

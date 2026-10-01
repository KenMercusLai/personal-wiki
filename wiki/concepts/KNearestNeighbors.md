---
title: "K-Nearest Neighbors"
type: concept
tags: [machine-learning, classification, instance-based-learning]
sources:
  - pokemon-recognition
last_updated: 2026-10-01
knowledge_schema: synthesis-v1
---

## Definition
[[KNearestNeighbors]] (kNN) is an instance-based method that predicts from the labels of the nearest stored training examples under a chosen feature representation and distance measure.

## Current Synthesis
The Pokémon tutorial uses kNN as a simpler raw-pixel comparison to SVM and selects the neighbor count through grid search. It reportedly fits and evaluates much faster than the searched SVM but yields lower average precision and recall. The comparison illustrates that computational simplicity and predictive performance can trade off, while also showing how raw high-dimensional pixel distances may be a poor measure of visual similarity.

## Key Claims
- kNN behavior depends on the feature representation, distance metric, scaling, neighbor count, and local class distribution.
- Training is light because examples are retained, but prediction can become expensive as the stored dataset grows.
- Distance comparisons in very high-dimensional raw-pixel space can be dominated by nuisance variation such as crop, background, and pose.
- A small single-dataset comparison cannot establish a general accuracy or speed ranking against SVM.

## Evidence
- Model selection: [[pokemon-recognition]] grid-searches neighbor counts from 1 through 14.
- Reported result: [[pokemon-recognition]] gives average precision 0.8725, recall 0.825, and about ten seconds of computation.
- Comparative result: [[pokemon-recognition]] reports lower aggregate metrics but shorter runtime than its raw-pixel SVM search.

## Counterevidence & Qualifications
The source does not report the selected neighbor count, distance metric experiments, scaling alternatives, class-level behavior, fold variance, hardware, or prediction-time scaling. With only 80 curated examples and 40,000 raw pixel dimensions, the result says little about kNN on learned or reduced representations and should not be generalized.

## What Changed
- Created the concept from the tutorial's simple raw-pixel baseline.

## Related Concepts
- [[ImageClassification]] - task used for the reported comparison.
- [[SupportVectorMachine]] - stronger but slower reported raw-pixel classifier in the source.
- [[DimensionalityReduction]] - can change whether distance meaningfully reflects similarity.

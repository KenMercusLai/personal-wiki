---
title: "Principal Component Analysis"
type: concept
tags: [machine-learning, dimensionality-reduction, linear-algebra]
sources:
  - pokemon-recognition
last_updated: 2026-10-01
knowledge_schema: synthesis-v1
---

## Definition
[[PrincipalComponentAnalysis]] (PCA) is a linear [[DimensionalityReduction]] method that maps data onto orthogonal directions ordered by the variance they capture.

## Current Synthesis
In the Pokémon tutorial, PCA is fitted on each training set and configured to retain more than 80% of its variance. It reduces 40,000 flattened grayscale pixel features to a reported 18 coordinates, after which an SVM reaches nearly the same aggregate precision and recall with substantially less reported fitting time. Reshaping component vectors back to 200×200 images produces “eigenpokemon,” and combining increasing numbers of components yields progressively clearer reconstructions.

This is a useful demonstration of low-rank representation, but variance is not identical to class relevance. PCA fitting has its own cost, the retained dimension depends on the sample and scaling, and the small evaluation does not show that the same tradeoff survives new data or more realistic image variation.

## Key Claims
- PCA orders orthogonal directions by captured variance and represents each example through coordinates on selected directions.
- PCA must be fitted only from training data and then applied unchanged to held-out data to avoid leakage.
- A variance threshold chooses representation size indirectly; it does not guarantee preservation of label-discriminative structure.
- Component vectors can be reshaped into image-like bases, and weighted combinations can approximate source images.
- Runtime comparisons must include PCA fitting and transformation as well as downstream classifier fitting.

## Evidence
- Feature reduction: [[pokemon-recognition]] reports a drop from 40,000 raw pixel features to 18 components while retaining more than 80% of training-set variance.
- Evaluation boundary: [[pokemon-recognition]] shows PCA fitted on `X_train`, followed by transformation of both `X_train` and `X_test`.
- Classification result: [[pokemon-recognition]] reports PCA-SVM precision 0.935 and recall 0.925 in about five seconds, compared with raw-pixel SVM precision 0.95 and recall 0.9375 in about two minutes.
- Interpretability: [[pokemon-recognition]] visualizes twelve reshaped components and partial reconstructions of Gengar and Charizard images.

## Counterevidence & Qualifications
The experiment has only 80 images and does not report PCA fitting time, hardware, fold variation, component counts by fold, or independent-test behavior. High-variance directions can reflect background, crop, lighting, or other nuisance variation rather than class identity. The author's claim that a larger and better dataset would make PCA-SVM more accurate than raw-pixel SVM remains an untested expectation in this source.

## What Changed
- Created the concept with the Pokémon tutorial as a visual, historically bounded example.

## Related Concepts
- [[DimensionalityReduction]] - PCA is a linear variance-preserving member of this broader method family.
- [[ImageClassification]] - downstream task used to evaluate the compressed representation.
- [[SupportVectorMachine]] - classifier trained on the tutorial's PCA coordinates.

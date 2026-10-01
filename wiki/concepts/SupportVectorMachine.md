---
title: "Support Vector Machine"
type: concept
tags: [machine-learning, classification, supervised-learning]
sources:
  - pokemon-recognition
last_updated: 2026-10-01
knowledge_schema: synthesis-v1
---

## Definition
[[SupportVectorMachine]] (SVM) is a supervised learning method that separates labeled examples using a maximum-margin decision boundary, optionally expressed through a kernel transformation.

## Current Synthesis
The Pokémon tutorial uses an SVM as the stronger of two classical baselines for four-class image recognition. It searches linear and radial-basis-function kernels plus values for `C` and `gamma`, first on 40,000 raw grayscale pixels and then on 18 PCA coordinates. The reported reduced representation cuts stated classifier runtime sharply while producing only slightly lower aggregate precision and recall.

Those numbers demonstrate one workflow, not an inherent ranking. The tiny high-dimensional sample, nested search details, preprocessing cost, hardware, and lack of an independent test set prevent a general conclusion that SVM is accurate for this task or that PCA will preserve its performance elsewhere.

## Key Claims
- SVM performance and cost depend on the input representation, kernel, regularization, and kernel parameters.
- Hyperparameter selection must stay inside the training side of performance estimation to avoid optimistic evaluation.
- A high score in a small, high-dimensional dataset can be unstable and should not be mistaken for open-world robustness.
- Comparing raw and reduced features requires the same evaluation protocol and complete end-to-end timing.

## Evidence
- Search design: [[pokemon-recognition]] grid-searches linear and RBF kernels, several `C` values, and several `gamma` values with balanced class weights.
- Raw-pixel result: [[pokemon-recognition]] reports average precision 0.95, recall 0.9375, and about two minutes of computation.
- PCA result: [[pokemon-recognition]] reports average precision 0.935, recall 0.925, and about five seconds of classifier computation on 18 components.
- Baseline comparison: [[pokemon-recognition]] reports higher precision and recall for SVM than k-nearest neighbors on the same small dataset.

## Counterevidence & Qualifications
The article does not report selected hyperparameters, per-fold metrics, class-level errors, uncertainty, leakage audits, preprocessing time, PCA fitting time, or an independent test set. The score may be affected by correlated or duplicated images and by the unusually high feature-to-example ratio. Runtime is specific to 2015 software, hardware, data size, and the stated grids.

## What Changed
- Created the concept from the raw-pixel and PCA-reduced Pokémon comparison.

## Related Concepts
- [[ImageClassification]] - application task in the source.
- [[PrincipalComponentAnalysis]] - preprocessing step used before the second SVM experiment.
- [[DimensionalityReduction]] - representation change that reduces the reported SVM fitting cost.
- [[KNearestNeighbors]] - alternative classifier reported as faster but less accurate on raw pixels.

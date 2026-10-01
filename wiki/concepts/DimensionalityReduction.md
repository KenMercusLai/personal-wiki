---
title: "Dimensionality Reduction"
type: concept
tags: [machine-learning, representation, computation]
sources:
  - pokemon-recognition
last_updated: 2026-10-01
knowledge_schema: synthesis-v1
---

## Definition
[[DimensionalityReduction]] transforms data into a representation with fewer features while attempting to preserve information useful for analysis, reconstruction, or prediction.

## Current Synthesis
The Pokémon case shows why reduction can matter when sample count is tiny relative to feature count: 80 images become points with 40,000 raw pixel coordinates. PCA reduces that representation to a reported 18 coordinates, after which SVM fitting is much faster while aggregate precision and recall decline only slightly in the reported folds.

The durable decision is not simply to minimize feature count. A reduction method must be fitted without test leakage, evaluated on the downstream objective, and charged for its own computation. Reconstruction quality, variance preservation, classifier performance, storage, and inference cost answer different questions and can point to different representation sizes.

## Key Claims
- Very high-dimensional inputs can increase computation and make learning fragile when observations are scarce.
- Reduction is useful only relative to an objective such as predictive performance, reconstruction, visualization, storage, or runtime.
- Unsupervised criteria such as retained variance do not guarantee preservation of label-relevant information.
- The reduction transform must be learned from training data and applied consistently to held-out or future inputs.
- End-to-end evaluation must count transformation cost and uncertainty, not only downstream model-fitting time.

## Evidence
- Dimensional imbalance: [[pokemon-recognition]] constructs 80 observations with 40,000 grayscale pixel features each.
- PCA result: [[pokemon-recognition]] reports 18 retained components at an 80% variance threshold.
- Downstream tradeoff: [[pokemon-recognition]] reports a large SVM fitting-time reduction alongside modestly lower aggregate precision and recall after PCA.
- Reconstruction: [[pokemon-recognition]] visually shows that more principal components yield a clearer approximation of the original image.

## Counterevidence & Qualifications
The source provides one tiny, curated classification example and omits preprocessing and PCA timing from its speed comparison. It does not establish a universal dimensionality threshold, prove improved generalization, or compare supervised selection, learned image features, regularization, or nonlinear reduction. Its numerical result is specific to the data, folds, implementation, search grid, and hardware.

## What Changed
- Created the concept around the objective-dependent tradeoff between representation size, information, and end-to-end cost.

## Related Concepts
- [[PrincipalComponentAnalysis]] - specific linear reduction method used in the source.
- [[ImageClassification]] - downstream task whose metrics qualify whether the reduced representation remains useful.
- [[SupportVectorMachine]] - downstream estimator whose reported fitting time falls after reduction.

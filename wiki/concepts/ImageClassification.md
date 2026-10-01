---
title: "Image Classification"
type: concept
tags: [machine-learning, computer-vision, classification]
sources:
  - pokemon-recognition
last_updated: 2026-10-01
knowledge_schema: synthesis-v1
---

## Definition
[[ImageClassification]] is the task of assigning an image to one of a predefined set of labels using features derived from its visual content.

## Current Synthesis
The Pokémon tutorial supplies a historically simple version of the task: normalize every image to the same shape and color representation, flatten the pixels into fixed-length vectors, and learn a four-class decision rule. This makes the mechanics legible, but also exposes the weaknesses of raw pixels: feature count grows with resolution, position and background changes are not explicitly handled, and a tiny curated dataset can make cross-validation scores unstable or optimistic.

PCA can compress this fixed-size representation before classification, but retained variance is not necessarily the information most useful for distinguishing classes. The experiment therefore demonstrates a workflow and a computational tradeoff rather than a generally adequate approach to image recognition.

## Key Claims
- Classification requires a consistent input representation and predefined target labels.
- Flattened grayscale pixels provide a simple fixed-length representation but discard spatial structure as an explicit modeling assumption.
- Small image datasets need careful separation, duplicate control, class-wise reporting, and uncertainty estimates before performance claims can generalize.
- Feature compression can reduce classifier cost while changing accuracy, but the complete preprocessing and reduction cost must be included in the comparison.

## Evidence
- Task construction: [[pokemon-recognition]] uses four Pokémon labels with 20 images per class.
- Input representation: [[pokemon-recognition]] fits images to 200×200 grayscale pixels and flattens them into 40,000-feature vectors.
- Model comparison: [[pokemon-recognition]] reports SVM, k-nearest-neighbor, and PCA-SVM results under cross-validation.
- Visual variability: [[pokemon-recognition]] shows that even examples of one character differ in crop, pose, source dimensions, and background.

## Counterevidence & Qualifications
The source is a pedagogical 2015 experiment, not a representative benchmark. Its dataset has only 80 images, the selection process and duplicate rate are unknown, class-wise errors and uncertainty are absent, and the evaluation does not test new sources or open-world inputs. Modern image classification often uses learned spatial features and augmentation rather than raw flattened pixels, but that broader comparison is outside this source's evidence.

## What Changed
- Created the concept from a four-class raw-pixel and PCA-based tutorial case.

## Related Concepts
- [[PrincipalComponentAnalysis]] - compresses the tutorial's flattened image vectors before classification.
- [[DimensionalityReduction]] - broader family of representation-reduction methods that can change cost and predictive information.
- [[SupportVectorMachine]] - classifier with the strongest reported aggregate metrics in the tutorial.
- [[KNearestNeighbors]] - simpler comparison model used on the same raw-pixel inputs.
- [[DeepLearning]] - later image-recognition approaches learn hierarchical features rather than relying only on flattened raw pixels.

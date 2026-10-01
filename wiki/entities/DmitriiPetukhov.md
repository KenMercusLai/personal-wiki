---
title: "Dmitrii Petukhov"
type: entity
tags: [machine-learning, python, technical-writing]
sources:
  - pokemon-recognition
last_updated: 2026-10-01
knowledge_schema: synthesis-v1
---

## Overview
[[DmitriiPetukhov]] is represented in this wiki as the author of a 2015 Python tutorial that compares raw-pixel classification with PCA-reduced classification on a small Pokémon image dataset.

## Current Profile
Petukhov uses a deliberately approachable four-class example to explain image preprocessing, flattened pixel features, cross-validation, SVM and k-nearest-neighbor classifiers, principal components, and image reconstruction. His account is strongest as a visual introduction to the workflow and tradeoff, not as comparative evidence about modern image-recognition methods.

## Key Characteristics
- Explains machine-learning ideas through a compact, reproducible image-classification example.
- Connects the eigenfaces method to a playful “eigenpokemon” visualization.
- Reports runtime and aggregate precision/recall for raw-pixel SVM, k-nearest neighbors, and PCA followed by SVM.
- Acknowledges that the tiny, high-dimensional dataset can make the raw-pixel SVM result misleadingly strong.

## Evidence
- Tutorial scope: [[pokemon-recognition]] builds an 80-image, four-class Pokémon classifier in Python and scikit-learn.
- Comparative experiment: [[pokemon-recognition]] reports raw-pixel and PCA-reduced SVM results alongside a k-nearest-neighbor baseline.
- Visual explanation: [[pokemon-recognition]] illustrates normalization, vectorization, PCA geometry, principal components, and reconstruction.

## Qualifications
This profile is based on one saved 2015 article and does not establish Petukhov's broader biography, later work, or current views. The experiment is small and underspecified, and its software APIs and performance observations are historically bounded.

## What Changed
- Created the author profile from the Pokémon recognition tutorial.

## Relationships
- [[ImageClassification]] - task Petukhov uses to introduce a complete machine-learning workflow.
- [[PrincipalComponentAnalysis]] - technique he explains and applies before classification.
- [[DimensionalityReduction]] - broader tradeoff illustrated by his reported feature and runtime reduction.
- [[SupportVectorMachine]] - classifier with the strongest reported metrics in his experiment.
- [[KNearestNeighbors]] - simpler baseline that he reports as faster but less accurate.

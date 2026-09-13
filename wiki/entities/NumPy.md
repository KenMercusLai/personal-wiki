---
title: "NumPy"
type: entity
tags: [python, data-science, scientific-computing]
sources:
  - an-introduction-to-scientific-python-numpy-data-dependence
last_updated: 2026-09-13
knowledge_schema: synthesis-v1
---

## Overview
[[NumPy]] is the Python numerical-computing library introduced by the Data Dependence tutorial as a foundational tool for scientific Python, data science, and machine learning.

## Current Profile
The source presents NumPy as a C-backed math library whose central abstraction is the array. Its practical value comes from letting Python users represent vectors, matrices, and higher-dimensional structures, inspect their shape and storage properties, and apply fast element-wise operations, slicing, masking, and dot products without writing manual Python loops.

## Key Characteristics
- Provides the array abstraction that anchors the tutorial's version of [[ScientificPython]].
- Represents vectors, matrices, and higher-dimensional data through [[NumPyArrayModel]].
- Supports [[MultidimensionalArraySlicing]] with separate row and column slice expressions.
- Enables [[VectorizedArrayOperations]] such as element-wise arithmetic, comparisons, sums, cumulative sums, and dot products.
- Supports [[BooleanMasking]] and fancy indexing for selecting elements by conditions or explicit index lists.

## Evidence
- Library role: [[an-introduction-to-scientific-python-numpy-data-dependence]] calls NumPy a fast Python math library with many underlying functions written in C.
- Array model: [[an-introduction-to-scientific-python-numpy-data-dependence]] explains one-dimensional arrays as vector representations and nested sequences as matrix or higher-dimensional array inputs.
- Slicing and masking: [[an-introduction-to-scientific-python-numpy-data-dependence]] includes inspected diagrams for multidimensional slicing and conditional point selection on a sine plot.
- Operations: [[an-introduction-to-scientific-python-numpy-data-dependence]] distinguishes element-wise arithmetic and comparisons from `dot()`, which returns a scalar dot product.

## Qualifications
The source is a beginner tutorial from 2016. It does not cover modern NumPy API conventions, broadcasting in detail, memory layout, performance pitfalls, random-number APIs, interoperability with pandas/SciPy, or current best practices for machine learning workflows.

## What Changed
- Created NumPy as a canonical entity for the wiki's scientific Python and data-science material.

## Relationships
- [[Python]] - NumPy extends Python with numerical array computing.
- [[ScientificPython]] - NumPy is presented as a key library in this stack.
- [[NumPyArrayModel]] - NumPy's array abstraction is the concept's subject.
- [[VectorizedArrayOperations]] - NumPy supplies the operations described by the concept.
- [[BooleanMasking]] - NumPy arrays support condition-based element selection.

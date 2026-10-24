---
title: "SPFresh"
type: entity
tags: [vector-search, approximate-nearest-neighbor-search, indexing]
sources:
  - ann-v3
last_updated: 2026-10-24
knowledge_schema: synthesis-v1
---

## Overview
[[SPFresh]] is represented here as a centroid-based approximate-nearest-neighbor index that supports incremental updates.

## Current Profile
The Turbopuffer source says ANN v3 is based on SPFresh and extends the paper's SPTAG graph-based index by nesting clusters in a multidimensional tree. Each cluster is summarized by a centroid; a query first compares against centroids, then searches selected child clusters rather than the full vector set.

## Key Characteristics
- Centroid-based approximate-nearest-neighbor indexing.
- Supports incremental updates according to the source.
- Uses SPTAG graph indexing in the cited original design.
- Supplies the base that Turbopuffer extends into a hierarchical tree.

## Evidence
Method lineage:
- [[ann-v3]] explicitly identifies SPFresh as the basis of Turbopuffer's vector indexes and names the hierarchical SPTAG extension.

System role:
- [[ann-v3]] connects centroid grouping to candidate narrowing, spatial locality, and bounded tree-height traversal.

## Qualifications
This page is derived from Turbopuffer's brief characterization rather than a full ingest of the SPFresh paper. It does not independently verify update mechanics, original evaluation, graph structure, or which parts of ANN v3 remain faithful to the published design.

## What Changed
- Established SPFresh as ANN v3's cited centroid-index foundation.
- Recorded the boundary between the cited base and Turbopuffer's hierarchical extension.

## Relationships
- [[ANNv3]] - hierarchical production design derived from SPFresh.
- [[ApproximateNearestNeighborSearch]] - search problem addressed by the index.
- [[Turbopuffer]] - organization applying and extending the design.

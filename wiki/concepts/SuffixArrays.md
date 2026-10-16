---
title: "Suffix Arrays"
type: concept
tags: [string-algorithms, indexing, compression]
sources:
  - suffix-bwt
last_updated: 2026-10-16
knowledge_schema: synthesis-v1
---

## Definition

A suffix array records the starting offsets of a string's suffixes in lexicographic order, providing a compact ordering primitive for text indexing and for constructing suffix-based transforms such as the [[BurrowsWheelerTransform]].

## Current Synthesis

For BWT construction, the important property is not merely that suffixes are sorted but that high-performance linear-time builders such as SA-IS and optimized libraries such as libsais are practically available. Their ordinary suffix semantics do not automatically equal cyclic-rotation semantics at the end of the string. Cyclic ordering can nevertheless be recovered by building over a doubled string and filtering starts, or by first rotating the input to its lexicographically smallest cyclic shift.

## Key Claims

- The suffix array supplies the row order needed to emit each suffix's preceding character in suffix BWT.
- SA-IS offers linear-time construction and, through optimized implementations, makes suffix BWT an attractive encoder choice.
- Sorting suffixes and sorting cyclic shifts differ at the string boundary, especially when one suffix prefixes another.
- Suffixes of a doubled string that begin in the first copy compare like the corresponding rotations, apart from harmless ties among equal periodic rotations.
- Rotating to the lexicographically smallest cyclic shift makes its suffix order usable for cyclic BWT, while separate work is needed to restore the original primary index.

## Evidence

### Direct BWT construction

- [[suffix-bwt]] describes constructing a suffix array, replacing the full-suffix boundary with the empty suffix, and emitting `s[sa[i] - 1]`, including libsais as a practical implementation.

### Cyclic-order adaptation

- [[suffix-bwt]] gives the doubled-string filtering method and the minimum-rotation method, then explains suffix-array lookup or Z-function counting for primary-index recovery.

### Semantic boundary

- [[suffix-bwt]] demonstrates that suffixes `a`, `aba`, and `acaba` order differently from their wrapped cyclic counterparts, invalidating a naive fictitious predecessor.

## Counterevidence & Qualifications

- The source names SA-IS as the most practical approach without benchmarking it against other suffix-array builders on current hardware or varied workloads.
- Doubling the string increases the processed input size; minimum rotation avoids that full cost but adds Duval computation and complicates recovery of the original primary index.
- A cited cyclic SA-IS variation weakens any claim that suffix arrays are inherently limited to non-cyclic construction, though implementation availability remains a practical distinction.

## What Changed

- Added suffix arrays as the practical construction bridge between suffix BWT and cyclic-shift BWT.
- Distinguished ordinary suffix order from wrap-around rotation order.
- Captured doubled-string and minimum-rotation adaptations with their costs.

## Related Concepts

- [[BurrowsWheelerTransform]] - consumes suffix or rotation order to group preceding symbols by context.
- [[Purplesyringa]] - connects suffix-array construction to decoder and deployment tradeoffs.

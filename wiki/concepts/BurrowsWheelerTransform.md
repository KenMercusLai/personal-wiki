---
title: "Burrows–Wheeler Transform"
type: concept
tags: [compression, string-algorithms, reversible-transforms]
sources:
  - suffix-bwt
last_updated: 2026-10-16
knowledge_schema: synthesis-v1
---

## Definition

The [[BurrowsWheelerTransform]] (BWT) is a reversible rearrangement of a string that orders contexts and emits the character preceding each ordered context, tending to group symbols with similar following text for downstream compression or indexed search.

## Current Synthesis

Two closely related constructions have materially different boundary behavior. Cyclic-shift BWT sorts all rotations, emits their last column, and uses LF mapping plus a primary index to recover the exact starting rotation. Suffix BWT instead sorts suffixes including the empty suffix and omits the full suffix's nonexistent predecessor; its decoder must compensate for both the empty row and omitted position. Suffix BWT is usually easier to encode efficiently because mature [[SuffixArrays|suffix-array]] construction is available, whereas cyclic-shift BWT offers a smaller, cleaner decoder and can be reduced to suffix sorting when necessary.

## Key Claims

- Both variants group preceding characters by lexicographically adjacent right contexts, but they do not generally produce the same row order.
- LF mapping preserves occurrence ranks between the last and first columns for cyclic rotations, enabling linear reconstruction up to rotation.
- Suffix boundaries break the naive cyclic rank correspondence when one suffix is a prefix of another, so decoder index corrections are semantically necessary.
- A unique sentinel outside the working alphabet can eliminate much of the practical distinction, but full alphabets require explicit boundary handling.
- Suffix BWT generally favors encoder performance and ecosystem support; cyclic-shift BWT favors minimal decoder logic.
- Cyclic-shift BWT can reuse suffix-array algorithms through string doubling or a minimum-rotation reduction.

## Evidence

### Variant semantics and inversion

- [[suffix-bwt]] works both variants on `bcacaba`, derives LF-style decoding, and shows the ordering failure caused by assigning a fictitious predecessor to the full suffix.

### Engineering tradeoff

- [[suffix-bwt]] identifies SA-IS and libsais as practical suffix-BWT construction routes, while qualifying cyclic-shift construction with a later-found cyclic SA-IS variation that apparently lacks an optimized implementation.

### Reductions and boundary techniques

- [[suffix-bwt]] explains sentinel-based equivalence, doubled-string filtering, minimum rotation through Duval's algorithm, and primary-index recovery through suffix arrays or the Z-function.

## Counterevidence & Qualifications

- The performance comparison is not backed by benchmarks in the source and will depend on implementation, alphabet, data distribution, and whether encoding or decoding dominates.
- Periodic inputs can contain equal cyclic shifts; the source says their internal order is irrelevant to the BWT output, but this is a narrower claim than a general guarantee about every metadata convention.
- The author's initial literature observation was revised after finding a cyclic SA-IS paper, so absence of convenient implementations should not be confused with absence of linear-time algorithms.

## What Changed

- Added an explicit distinction between cyclic-shift BWT and suffix BWT.
- Established boundary handling, encoder ecosystem, and decoder size as the main selection criteria.
- Added two suffix-array-based routes for constructing cyclic-shift BWT.

## Related Concepts

- [[SuffixArrays]] - provides the practical sorted-suffix order used to encode suffix BWT and emulate cyclic sorting.
- [[Purplesyringa]] - supplies the source's implementation-oriented comparison and qualifications.

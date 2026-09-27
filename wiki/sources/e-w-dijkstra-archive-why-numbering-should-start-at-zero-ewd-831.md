---
title: "Why numbering should start at zero (EWD 831)"
type: source
tags: [computer-science, indexing, intervals, programming-language-design]
date: 1982-08-11
source_file: "/mnt/ken_personal_wiki/Articles/E.W. Dijkstra Archive- Why numbering should start at zero (EWD 831).md"
---

## Summary
[[EdsgerWDijkstra]] argues that integer ranges should include their lower bound and exclude their upper bound because this makes range length equal to the difference between bounds, makes adjacent ranges share a boundary, and represents both the first natural number and the empty range without unnatural endpoints. Applied to a sequence of length N, that [[HalfOpenIntervals|half-open interval]] convention makes [[ZeroBasedIndexing]] the simpler choice: `0 ≤ i < N`, with an element's ordinal equal to the number of elements before it. He cites Mesa programmers' experience with all four interval conventions as practical, though unquantified, evidence that the alternatives produce clumsiness and mistakes.

## Key Claims
- Of four open/closed endpoint conventions for integer subsequences, an inclusive lower bound and exclusive upper bound is preferable.
- For a half-open integer range, the difference between upper and lower bounds equals the number of elements, and adjacent ranges meet where one's upper bound equals the other's lower bound.
- Including the lower endpoint avoids needing a value below the smallest natural number when a range begins there; excluding the upper endpoint keeps an empty prefix representable without an unnatural upper endpoint.
- A sequence of length N indexed from zero has the compact range `0 ≤ i < N`, and each index counts the elements preceding that position.
- Experience with Mesa's four explicit interval notations reportedly led programmers to discourage the other three conventions because they caused recurring clumsiness and mistakes.

## Key Quotes
> "So let us let our ordinals start at zero: an element's ordinal (subscript) equals the number of elements preceding it in the sequence." — Dijkstra's bridge from half-open ranges to zero-based indexing.

> "We conclude that convention a) is to be preferred." — conclusion after comparing endpoint behavior at the smallest natural number and the empty sequence.

## Connections
- [[EdsgerWDijkstra]] — author of the 1982 EWD 831 note.
- [[HalfOpenIntervals]] — the inclusive-lower, exclusive-upper range convention defended in the note.
- [[ZeroBasedIndexing]] — the numbering convention derived by applying the preferred range form to a sequence of length N.

## Contradictions
- No direct contradiction with an existing wiki claim was identified. The note's Mesa evidence is anecdotal and unquantified, so it supports a design preference rather than proving that half-open ranges or zero-based indexing minimize errors in every context.

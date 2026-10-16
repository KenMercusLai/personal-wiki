---
title: "Suffix BWT vs cyclic shift BWT, and fast computation"
type: source
tags: [compression, string-algorithms, bwt, suffix-arrays]
date: 2026-07-03
source_file: /mnt/ken_personal_wiki/Articles/suffix-bwt.md
---

## Summary
[[Purplesyringa]] distinguishes the cyclic-shift and suffix formulations of the [[BurrowsWheelerTransform]], showing why their sorted orders and decoders differ when one suffix prefixes another. The article argues that suffix BWT is usually the practical choice because mature [[SuffixArrays|suffix-array]] construction—especially SA-IS—makes encoding fast, while cyclic-shift BWT remains attractive when decoder size or simplicity matters and can still be computed through doubled strings or a minimum-rotation reduction.

## Key Claims
- Cyclic-shift BWT sorts rotations and emits each rotation's preceding character; LF mapping inverts the result up to rotation, while a transmitted primary index identifies the original input exactly.
- Suffix BWT sorts suffixes, prepends the empty suffix, and omits the full suffix's missing predecessor, so decoding must adjust ranks around both boundaries and receive the omitted position.
- Dropping the empty suffix instead does not repair suffix decoding: pretending that the full suffix has a cyclic predecessor can change order when the corresponding wrapped string is not itself a suffix.
- [[SuffixArrays]] make suffix BWT easier and faster to encode in practice because SA-IS and optimized implementations such as libsais are readily available; similarly mature cyclic-shift tooling is less common.
- A unique smallest sentinel can make the variants coincide operationally, but a full alphabet removes that escape hatch and exposes their different boundary semantics.
- Cyclic-shift BWT can be computed with suffix-array machinery either by sorting suffixes of a doubled string and filtering starts, or by rotating to the lexicographically smallest cyclic shift before computing suffix BWT.
- Duval's algorithm can find the minimum rotation in linear time, while the primary index of the unrotated input can be recovered from its suffix array or by using the Z-function to count smaller rotations.

## Key Quotes
> "While suffix BWT is a little trickier and slower to decode, it's much faster to encode." — the article's central implementation tradeoff.

> "The easiest way to implement wrap-around semantics is to double the string." — on reusing suffix-array construction for cyclic shifts.

> "In most cases, suffix BWT is better" — the conclusion, qualified by tiny-decoder and full-alphabet use cases.

## Connections
- [[Purplesyringa]] - practitioner-author comparing the two transforms and deriving practical construction techniques.
- [[BurrowsWheelerTransform]] - central reversible context-grouping transform whose suffix and cyclic-shift variants are distinguished.
- [[SuffixArrays]] - mature suffix-ordering machinery used to construct suffix BWT and adapted to cyclic rotations.

## Contradictions
- No direct contradiction with existing wiki pages was found; this is the wiki's first focused treatment of BWT and suffix-array construction.
- The author explicitly presents the terminology and literature survey as an attempt to clarify a poorly documented distinction, later adding a cyclic SA-IS paper after initially reporting no linear-time cyclic-shift algorithm.
- Performance conclusions are qualitative: the article supplies pseudocode and implementation links but no controlled benchmark across encoders, decoders, alphabets, input distributions, or libraries.

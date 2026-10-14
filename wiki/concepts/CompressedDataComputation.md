---
title: "Compressed-Data Computation"
type: concept
tags: [columnar-storage, compression, query-execution, late-materialization]
sources:
  - vortex-one-format-for-any-shape
last_updated: 2026-10-14
knowledge_schema: synthesis-v1
---

## Definition
[[CompressedDataComputation]] evaluates an operation by exploiting an encoded representation's structure before, during, or instead of reconstructing every logical value.

## Current Synthesis
Compression is not only a storage-size choice; it can expose reusable structure. Run ends already encode multiplicity, so a sum kernel can multiply each distinct run value by its length. Dictionary values separate distinct strings from per-row codes, so a comparison can run once per distinct value and reuse codes to recover a row mask, while filtering can operate on codes without touching the dictionary values.

Vortex implements these paths through specialized kernels and optimizer rewrite rules over an array tree. Optimization remains partial and safe because every logical type has a canonical encoding: when no kernel or rule applies, execution moves the array toward canonical form and completes the operation there. The design therefore separates correctness coverage from performance coverage, allowing new encodings to work through canonicalization before they gain optimized operations.

## Key Claims
- Encodings can preserve counts, equality classes, ordering, or address structure that reduces later query work.
- Specialized kernels execute an operation directly over a compatible encoding.
- Rewrite rules move operations to cheaper children while reusing unaffected encoded structure.
- Cascaded encoding trees let optimization target the simplest relevant component rather than the whole logical array.
- Canonical materialization is a correctness fallback, not the default required path for every operation.
- Benefits depend on data shape, operation compatibility, cascade structure, and optimizer or kernel coverage.

## Evidence
- Run multiplicity: [[vortex-one-format-for-any-shape]] shows a run-end kernel computing `10×2 + 30×3 + 50×4` without expanding nine integers.
- Dictionary comparison: [[vortex-one-format-for-any-shape]] compares two distinct city strings, then uses unchanged codes to form a seven-row boolean mask.
- Dictionary filtering: [[vortex-one-format-for-any-shape]] filters codes while reusing the untouched dictionary values.
- Cascaded structure: [[vortex-one-format-for-any-shape]] places run-end and bit-packed arrays beneath dictionary codes, allowing rules to preserve or target subtrees.
- Fallback: [[vortex-one-format-for-any-shape]] describes execution toward a canonical encoding when no specialized path applies.

## Counterevidence & Qualifications
The source uses tiny pedagogical examples rather than a controlled performance evaluation. Long runs or small dictionaries can make the avoided work large, while high-cardinality, irregular, short, or incompatible data may offer little advantage. Kernels still may need to canonicalize children, rewrite rules require validity guards, and a fixed-point optimizer needs termination protection. Maintaining encoded paths increases implementation, testing, metadata, and compatibility work; the canonical fallback preserves correctness but may lose the expected speedup.

## What Changed
- Established encoded structure as an execution resource rather than treating compression only as storage reduction.
- Distinguished specialized kernels, rewrite rules, and canonical fallback as three complementary paths.

## Related Concepts
- [[Vortex]] - implements compressed-data computation over extensible array encodings.
- [[ColumnarStorageTradeoffs]] - places encoded execution beside size, I/O, decoding, and compatibility choices.
- [[FilterPushdown]] - moves predicates closer to stored data, while compressed-data computation changes how those predicates execute inside an encoding.
- [[LiquidCache]] - evaluates compatible predicates and selectively decodes an ephemeral compressed representation.
- [[ApacheParquet]] - durable format whose decode path supplies a comparison boundary in related sources.

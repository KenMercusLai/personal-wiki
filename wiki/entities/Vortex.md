---
title: "Vortex"
type: entity
tags: [software, columnar-storage, data-format, rust]
sources:
  - vortex-one-format-for-any-shape
last_updated: 2026-10-14
knowledge_schema: synthesis-v1
---

## Overview
[[Vortex]] is an open-source, Rust-based columnar data format under the Linux Foundation, presented as a self-describing and extensible substrate for complex analytical data with zero-copy-compatible Apache Arrow canonical forms.

## Current Profile
Vortex separates three decisions that conventional formats often bind together: a logical `DType` describes values, an array encoding describes their in-memory or serialized physical representation, and a layout tree determines which segments are stored and fetched together. Types, encodings, layouts, and selected computations can be registered through sessions, allowing third-party crates to extend the system without forking the container format.

Its array model is recursive. Dictionary, run-end, bit-packed, and other encodings can form trees whose children are independently encoded, while specialized kernels and rewrite rules operate on encoded structure. A canonical encoding per logical type supplies the compatibility fallback when no optimized path applies. Layout trees separately compose column, chunk, flat, page, and pruning choices for local files, memory, caches, or object storage.

## Key Characteristics
- Separates logical type, physical array encoding, and storage layout into independently extensible layers.
- Composes encodings recursively and selects compression cascades from sampled data.
- Supports specialized kernels and rewrite rules that avoid unnecessary full decompression.
- Provides canonical encodings as general compute and Arrow-interchange fallbacks.
- Registers third-party types, encodings, layouts, compression schemes, and functions through sessions.
- Shares one Rust implementation across language bindings, reducing but not eliminating extension-distribution work.
- Targets complex values including vectors, geospatial data, nested documents, images, and video.

## Evidence
- Layer separation: [[vortex-one-format-for-any-shape]] distinguishes `DType`, `Array` encodings, and `Layout` trees, with diagrams of alternative encodings and selective segment fetching.
- Recursive compression: [[vortex-one-format-for-any-shape]] builds a dictionary-to-run-end-to-bit-packed tree and describes a sampling-based compressor inspired by BtrBlocks.
- Encoded execution: [[vortex-one-format-for-any-shape]] shows a run-end sum kernel plus dictionary comparison and filter rewrites.
- Extensibility fallback: [[vortex-one-format-for-any-shape]] explains session registration and execution toward one canonical encoding per logical type.
- Complex types: [[vortex-one-format-for-any-shape]] defines a vector extension over fixed-size float-list storage and cites vector, polygon, image, video, and geospatial implementations.
- Performance claim: [[vortex-one-format-for-any-shape]] points to first-party benchmarks reporting Parquet-comparable size and faster writes, scans, and random access.

## Qualifications
Readers still need an extension's code to decode or compute with it; unknown structures can be retained only as unusable placeholders. Registration alone does not provide validation, serialization, compressor selection, optimized kernels, stable identifiers, version compatibility, or cross-language packaging. The article is a first-party architectural explanation, and its benchmark conclusion is linked rather than reproduced with workload details in the source. Flexibility therefore expands the design space while moving responsibility into extension code, registries, compatibility policy, and workload-specific tuning.

## What Changed
- Established Vortex as a three-layer extensible format rather than only a faster Parquet alternative.
- Added recursive compression, encoded computation, canonical fallback, and layout composition as the core mechanisms.
- Recorded the reader-code and first-party benchmark boundaries on the extensibility claim.

## Relationships
- [[ApacheParquet]] - mature fixed-specification comparison point whose PAX hierarchy Vortex layouts can reproduce.
- [[ColumnarStorageTradeoffs]] - design space Vortex expands through independent encoding and layout composition.
- [[CompressedDataComputation]] - execution strategy implemented through encoding-specific kernels and rewrites.
- [[LiquidCache]] - related use of cascading encodings and encoded predicate evaluation at a private cache boundary.
- [[LanceFormat]] - alternative columnar format targeting vectors, multimodal data, extensibility, and selective access.

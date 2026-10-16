---
title: "Columnar Storage Tradeoffs"
type: concept
tags: [columnar-storage, data-formats, random-access, scan-performance]
sources:
  - lance-mian-xiang-ai-chang-jing-de-shu-ju-cun-chu-ge-shi
  - p5662-hao-corrected
  - vortex-one-format-for-any-shape
  - "2504.15247"
  - beyond-indexes
last_updated: 2026-10-16
knowledge_schema: synthesis-v1
---

## Definition
[[ColumnarStorageTradeoffs]] are the coupled choices among compression, scan throughput, selective random access, decoding CPU, page and metadata granularity, write or transcoding cost, interoperability, and format evolvability in a columnar data representation.

## Current Synthesis
Columnar storage does not have one universally optimal physical boundary. Row groups align horizontal partitions across columns, supporting coordinated scans and familiar distributed processing, but one row-group size must serve columns whose encoded widths may differ by orders of magnitude. A wide tensor or media column can therefore make a conventional group contain few records, while a very large group can require more write memory and reduce read parallelism.

Point lookup exposes another boundary. A page index can locate a candidate page without locating one value inside the page, so fetching sparse rows may still decompress or read much more data than returned. Removing row groups and paging columns independently lets page size follow the storage system and each column's width, but shifts coordination into row-range metadata, scheduling, decoding, and format implementations.

The new primary comparison makes page size, structural encoding, and cache scale concrete. Tuned Parquet can reduce one nested value lookup to one small page read and improve random access by more than 60 times over defaults, but one-page-per-large-value indexes consume substantial RAM. Arrow-style separate buffers avoid page decoding yet add dependent reads as variable-width nesting grows. Lance therefore chooses miniblocks for small values, where vectorized opaque decoding amortizes work, and full zip for large values, where per-value work is affordable and a repetition index avoids nesting-dependent I/O.

Metadata design similarly trades a simple common footer against selective loading. Per-column metadata and a small locator footer reduce work for very wide schemas, while flexible page-, column-, global-, or external-scope metadata makes indexes and encodings easier to evolve. That flexibility also enlarges the behavioral contract among writers, readers, extensions, and dataset manifests.

LiquidCache adds execution-aware encoding to the design space. Parquet compresses well but its page-oriented representation makes selective filter execution pay decompression and decoding costs; Arrow eliminates decode work but can use several times more memory. A cache-private representation can combine independent element decoding with cascading compression and evaluate some predicates on encoded values, but it adds transcoding, engine coupling, and a second physical representation. Keeping that representation ephemeral avoids imposing a new durable interoperability contract, while also preventing unrelated readers from consuming it directly.

Vortex generalizes these choices by separating logical types, recursive array encodings, and segment-fetch layouts. Its layout trees can reproduce a PAX hierarchy or compose different chunking and pruning for a storage system, while encoding trees can combine dictionary, run-end, bit-packed, and other representations beneath the same logical type. Canonical encodings provide a general compute fallback; registries let third-party crates add faster or more specialized paths. This moves flexibility into extension code, identifiers, metadata, validation, versioning, and reader distribution rather than removing compatibility cost.

The open-table-format view adds a hierarchy above the file. Table partitioning and sorting decide which values become colocated; manifests describe files; Parquet statistics describe row groups; and compaction repairs small-file and cross-write locality drift. Metadata does not create locality: broad overlapping ranges faithfully report that little can be pruned. Supporting incompatible query shapes therefore requires either a compromise layout or maintained alternate representations such as materialized views.

## Key Claims
- A shared row-group size can become inefficient when column widths differ greatly.
- Page-level indexes can make Parquet point lookup fast, but trade sparse-read amplification and index RAM against page size.
- Independent column paging can align I/O granularity with column width and storage read units.
- Separating I/O scheduling from decoding can overlap storage and CPU work more freely than row-group-bound execution.
- Selectively addressable column metadata can reduce projection overhead for extremely wide schemas.
- Structural encoding should adapt to value width, nesting, storage read units, and whether scan or point-decode work dominates.
- Extensibility and query diversity can live in a durable format, table metadata, shared implementation, private cache, or alternate materialized layout, with different interoperability and maintenance responsibilities.

## Evidence
- Row-group and page boundary: [[lance-mian-xiang-ai-chang-jing-de-shu-ju-cun-chu-ge-shi]] diagrams Parquet's row-group, column-chunk, page, page-index, and footer hierarchy.
- Sparse lookup: [[lance-mian-xiang-ai-chang-jing-de-shu-ju-cun-chu-ge-shi]] shows target rows spread across groups while full pages remain the read unit.
- Width imbalance: [[lance-mian-xiang-ai-chang-jing-de-shu-ju-cun-chu-ge-shi]] compares large memory-intensive groups with conventional groups that fragment narrow columns.
- Independent paging and execution: [[lance-mian-xiang-ai-chang-jing-de-shu-ju-cun-chu-ge-shi]] shows unequal page counts and a separate scheduling, I/O, and decode pipeline.
- Metadata scope: [[lance-mian-xiang-ai-chang-jing-de-shu-ju-cun-chu-ge-shi]] locates per-column metadata through offset tables and illustrates page-, column-, and shared-dictionary placement.
- Encoding choice: [[lance-mian-xiang-ai-chang-jing-de-shu-ju-cun-chu-ge-shi]] contrasts scan-oriented compression with mini-block and indexed full-zip random-access compromises.
- Decode-versus-space boundary: [[p5662-hao-corrected]] reports Arrow-like CPU with Parquet-like memory for LiquidCache on selected ClickBench queries, while profiling Parquet pushdown's decode cost and Arrow's memory stalls.
- Independent decoding: [[p5662-hao-corrected]] diagrams element-selective decoding, late filter materialization, and dictionary-aware predicate evaluation.
- Transcoding boundary: [[p5662-hao-corrected]] reports full Liquid at 2.0 GB versus 2.4 GB Parquet and 12.9 GB Arrow for one large string column, with background conversion usually hidden by I/O.
- Layer separation: [[vortex-one-format-for-any-shape]] distinguishes logical types, array-encoding trees, and layout trees, and shows one layout fetching only a requested column and row range.
- Composable compression: [[vortex-one-format-for-any-shape]] constructs a dictionary-to-run-end-to-bit-packed tree and uses sampled data to choose bounded cascades.
- Compute fallback: [[vortex-one-format-for-any-shape]] combines encoded kernels and rewrites with execution toward one canonical encoding per logical type.
- Storage baseline: [[2504.15247]] shows NVMe favoring sector-scale random reads while S3 gains bandwidth only at much larger requests.
- Adaptive structure: [[2504.15247]] compares Parquet pages, Arrow buffers, Lance miniblocks, and full zip across nesting, cache size, random access, compression, and scans.
- Benchmark controls: [[2504.15247]] shows coalesced-access benefits shrinking with dataset scale and reports tuned Parquet more than 60 times faster than its default small-scalar configuration.
- Packing tradeoff: [[2504.15247]] shows multi-field struct lookup improving when fields share an access unit while single-field scan throughput declines.
- Table-to-file hierarchy: [[beyond-indexes]] connects partitions, sort order, manifests, Parquet row-group statistics, Bloom filters, compaction, and alternate projections as layers of analytical I/O avoidance.

## Counterevidence & Qualifications
The primary Lance paper now supplies a controlled benchmark, but it remains first-party, uses one NVMe device and CPU, selected datasets, warm metadata, parquet-rs 54, and experimental Lance versions. Its Arrow result uses Lance 2.0 as a proxy rather than Arrow IPC, and several Lance mechanisms were incomplete. LiquidCache and Vortex add separate first-party and prototype boundaries, while the open-table-format account is conceptual rather than measured. Parquet's maturity and interoperability may outweigh selective-access costs; Arrow may remain best in memory; and pushdown can lose on non-selective predicates. Every design moves complexity among metadata, readers, cache RAM, decoding, registries, transcoding, partition choice, rewrite maintenance, layout selection, and scheduling. Outcomes remain conditional on schema, value width, nesting, distribution, predicates, compression, storage minimum reads, cache state, concurrency, implementation quality, and operational workload.

## What Changed
- Added controlled evidence that tuned Parquet point lookup can be strong while remaining sensitive to page size and index RAM.
- Added adaptive structural encoding by value width and nesting as a distinct design axis from compression.
- Added table-level locality, hierarchical pruning, compaction drift, and alternate physical copies above file-level layout choices.

## Related Concepts
- [[LanceFormat]] - implements independent pages, selective column metadata, and extensible encodings.
- [[ApacheParquet]] - represents the row-group-oriented comparison design.
- [[ApacheArrow]] - represents the direct, multi-buffer in-memory layout and its nested storage-I/O cost.
- [[LiquidCache]] - adds a cache-private, independently decodable point in the design space.
- [[Vortex]] - makes logical types, recursive encodings, and storage layouts separately extensible in one durable format.
- [[CompressedDataComputation]] - uses encoding structure to reduce materialization and predicate or aggregation work.
- [[FilterPushdown]] - makes decoding and encoding compatibility part of predicate-placement cost.
- [[ApacheDataFusion]] - demonstrates that engine integration can outweigh nominal format properties.
- [[DatabaseEngineeringTradeoffs]] - broader principle that database choices depend on workload and operational constraints.
- [[StoragePerformanceBenchmarking]] - provides the measurement discipline needed to test layout claims.
- [[VectorDatabase]] - selective candidate-row fetching makes random-access costs operationally important.
- [[DataFormatInteroperability]] - flexible encodings and readers must still preserve shared data meaning.
- [[OpenTableFormats]] - add partition, manifest, maintenance, and alternate-layout choices above columnar files.
- [[DataPruning]] - turns physical locality and statistics into avoided I/O.

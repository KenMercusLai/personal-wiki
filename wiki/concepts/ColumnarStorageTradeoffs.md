---
title: "Columnar Storage Tradeoffs"
type: concept
tags: [columnar-storage, data-formats, random-access, scan-performance]
sources:
  - lance-mian-xiang-ai-chang-jing-de-shu-ju-cun-chu-ge-shi
  - p5662-hao-corrected
last_updated: 2026-10-13
knowledge_schema: synthesis-v1
---

## Definition
[[ColumnarStorageTradeoffs]] are the coupled choices among compression, scan throughput, selective random access, decoding CPU, page and metadata granularity, write or transcoding cost, interoperability, and format evolvability in a columnar data representation.

## Current Synthesis
Columnar storage does not have one universally optimal physical boundary. Row groups align horizontal partitions across columns, supporting coordinated scans and familiar distributed processing, but one row-group size must serve columns whose encoded widths may differ by orders of magnitude. A wide tensor or media column can therefore make a conventional group contain few records, while a very large group can require more write memory and reduce read parallelism.

Point lookup exposes another boundary. A page index can locate a candidate page without locating one value inside the page, so fetching sparse rows may still decompress or read much more data than returned. Removing row groups and paging columns independently lets page size follow the storage system and each column's width, but shifts coordination into row-range metadata, scheduling, decoding, and format implementations.

Metadata design similarly trades a simple common footer against selective loading. Per-column metadata and a small locator footer reduce work for very wide schemas, while flexible page-, column-, global-, or external-scope metadata makes indexes and encodings easier to evolve. That flexibility also enlarges the behavioral contract among writers, readers, extensions, and dataset manifests.

LiquidCache adds execution-aware encoding to the design space. Parquet compresses well but its page-oriented representation makes selective filter execution pay decompression and decoding costs; Arrow eliminates decode work but can use several times more memory. A cache-private representation can combine independent element decoding with cascading compression and evaluate some predicates on encoded values, but it adds transcoding, engine coupling, and a second physical representation. Keeping that representation ephemeral avoids imposing a new durable interoperability contract, while also preventing unrelated readers from consuming it directly.

## Key Claims
- A shared row-group size can become inefficient when column widths differ greatly.
- Page-level indexes reduce search scope but do not eliminate sparse-read amplification within a page.
- Independent column paging can align I/O granularity with column width and storage read units.
- Separating I/O scheduling from decoding can overlap storage and CPU work more freely than row-group-bound execution.
- Selectively addressable column metadata can reduce projection overhead for extremely wide schemas.
- Independently decodable encodings can reduce selective-filter CPU while retaining compression.
- Extensibility can live in a durable format or a private cache layer, with different interoperability responsibilities.

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

## Counterevidence & Qualifications
The Lance source explains layouts but does not supply a controlled benchmark, so it cannot establish that Lance is generally faster than Parquet. The LiquidCache evidence is a first-party prototype benchmark over selected workloads and one engine/hardware setup; warm transcoding, predicate compatibility, implementation maturity, and the absence of TLS or production multi-tenancy narrow its scope. Parquet's maturity, interoperability, compression, and scan orientation may outweigh selective-access and decode costs. Arrow may remain best when data fits memory, and pushdown can lose when predicates are non-selective. Lance's flexibility and LiquidCache's private representation both move complexity into metadata, readers, engine coupling, transcoding, or cache policy. Outcomes depend on schema, value sizes, selectivity, compression, storage minimum reads, cache state, concurrency, object-store behavior, and implementation quality.

## What Changed
- Created the synthesis around physical boundaries rather than treating Parquet and Lance as a simple old-versus-new ranking.
- Added decoding CPU, filter compatibility, transient transcoding, and durable-versus-ephemeral evolution boundaries.

## Related Concepts
- [[LanceFormat]] - implements independent pages, selective column metadata, and extensible encodings.
- [[ApacheParquet]] - represents the row-group-oriented comparison design.
- [[LiquidCache]] - adds a cache-private, independently decodable point in the design space.
- [[FilterPushdown]] - makes decoding and encoding compatibility part of predicate-placement cost.
- [[ApacheDataFusion]] - demonstrates that engine integration can outweigh nominal format properties.
- [[DatabaseEngineeringTradeoffs]] - broader principle that database choices depend on workload and operational constraints.
- [[StoragePerformanceBenchmarking]] - provides the measurement discipline needed to test layout claims.
- [[VectorDatabase]] - selective candidate-row fetching makes random-access costs operationally important.
- [[DataFormatInteroperability]] - flexible encodings and readers must still preserve shared data meaning.

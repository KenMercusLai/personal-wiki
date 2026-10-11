---
title: "Lance Format"
type: entity
tags: [storage-format, columnar-storage, vector-search, multimodal-data]
sources:
  - lance-mian-xiang-ai-chang-jing-de-shu-ju-cun-chu-ge-shi
last_updated: 2026-10-11
knowledge_schema: synthesis-v1
---

## Overview
[[LanceFormat]] is represented as a storage family for vector and multimodal data, comprising a columnar file format and a dataset-level table format.

## Current Profile
The file format uses independently sized and placed column pages rather than shared row groups. Per-column metadata blocks are located through offset tables and a small fixed footer, so a reader can seek metadata for selected columns without first loading the metadata of every column. Pages may contain encoded values or metadata, and dictionaries, statistics, and indexes can be placed at page, column, global, or dataset scope.

Lance reuses the Arrow type system but makes physical encodings extensible through metadata descriptions and matching encoder-decoder implementations. The source presents mini-block and full-zip structural encodings as a workload-dependent compromise: small values accept bounded read amplification inside a compressed chunk, while large or nested values add an index to keep random access within two I/O operations.

At dataset level, Lance Table Format groups data files with version manifests, secondary indexes, and deletion files. Externalizing type, encoding, index, statistics, version, and deletion information is intended to permit evolution without rewriting all primary data, while native vector and text retrieval target AI workloads.

## Key Characteristics
- Eliminates shared row groups in favor of independently paged columns.
- Uses a small fixed footer and separately addressable per-column metadata.
- Reuses Arrow types while allowing encoding implementations to evolve as extensions.
- Permits flexible placement of data, dictionaries, statistics, and indexes across scopes.
- Adds manifests, secondary indexes, and deletion files at dataset level.
- Targets selective random access as well as scan, vector, text, and multimodal workloads.

## Evidence
- Physical layout: [[lance-mian-xiang-ai-chang-jing-de-shu-ju-cun-chu-ge-shi]] diagrams data pages, column metadata, two offset tables, global buffers, and the footer.
- Page independence: [[lance-mian-xiang-ai-chang-jing-de-shu-ju-cun-chu-ge-shi]] shows columns with unequal page counts and interleaved physical placement.
- I/O pipeline: [[lance-mian-xiang-ai-chang-jing-de-shu-ju-cun-chu-ge-shi]] separates metadata scheduling, asynchronous reads, and CPU decode tasks.
- Encoding model: [[lance-mian-xiang-ai-chang-jing-de-shu-ju-cun-chu-ge-shi]] compares Arrow, Parquet, mini-block, and full-zip representations of nested values.
- Dataset organization: [[lance-mian-xiang-ai-chang-jing-de-shu-ju-cun-chu-ge-shi]] lists data, version-manifest, secondary-index, and deletion directories.

## Qualifications
The profile comes from one secondary technical article largely translated from Lance's own materials and current only through the stated v2.1 scope. It explains mechanisms but does not reproduce the scan-performance comparison, million-column claim, random-access I/O bounds, or operational advantages. Flexible metadata and encoding placement can improve evolvability while also increasing implementation and interoperability responsibility; the source does not compare write amplification, ecosystem maturity, recovery behavior, cost, or long-term compatibility.

## What Changed
- Created the format profile and separated file-layout decisions from dataset-level version, index, and deletion metadata.

## Relationships
- [[LanceDB]] - database project that uses Lance as its storage format.
- [[ApacheParquet]] - established columnar comparison point with row-group-oriented layout.
- [[ColumnarStorageTradeoffs]] - frames the scan, random-access, metadata, and extensibility choices embodied by Lance.
- [[VectorDatabase]] - selective vector retrieval is a target workload for the format.
- [[MultimodalDataPipelines]] - wide tensor and media columns motivate independent paging and flexible encoding.
- [[StoragePerformanceBenchmarking]] - format claims require measurement under representative access patterns and storage systems.

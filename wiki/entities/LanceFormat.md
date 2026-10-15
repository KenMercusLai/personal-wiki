---
title: "Lance Format"
type: entity
tags: [storage-format, columnar-storage, vector-search, multimodal-data]
sources:
  - lance-mian-xiang-ai-chang-jing-de-shu-ju-cun-chu-ge-shi
  - lancedb-xuan-xing-zhi-nan-ta-wei-shen-me-zhe-me-huo-yi-ji-ni-de-xiang-mu-shi-fou-gai-yong-ta
  - "2504.15247"
last_updated: 2026-10-15
knowledge_schema: synthesis-v1
---

## Overview
[[LanceFormat]] is a storage family for vector and multimodal data, comprising a columnar file format and a dataset-level table format used by [[LanceDB]] and training-data workflows.

## Current Profile
The file format uses independently sized and placed column pages rather than shared row groups. Per-column metadata blocks are found through offset tables and a small fixed footer, allowing a reader to seek metadata for selected columns without first loading every column's metadata. Pages may contain encoded values or metadata, and dictionaries, statistics, and indexes can live at page, column, global, or dataset scope.

Lance reuses the Arrow type system while making physical encodings extensible through metadata descriptions and matching encoder-decoder implementations. The primary paper specifies an adaptive boundary at roughly 128 bytes per value: miniblocks keep compression and decoding vectorized for small values while accepting one small chunk of read amplification; full zip interleaves control words with each large value and uses a repetition index for variable width. This targets one I/O for fixed-width and two for variable-width point access without adding I/O for deeper nesting.

The tested implementation makes those goals conditional rather than absolute. Miniblock metadata consumes search-cache RAM, full zip requires independently decodable compression and may retain filler for fixed-width nulls, and the evaluated reader supported only one level of list lookup. Struct packing improves multi-field lookup by sacrificing single-field projection. On one NVMe system, Lance generally tied or beat optimized Parquet for random access and matched or exceeded its best scan result in seven of eight data categories, while leaving additional sector alignment, asynchronous I/O, and compression work open.

At dataset level, Lance groups data files with version manifests, secondary indexes, and deletion files. External type, encoding, index, statistics, version, and deletion information is intended to permit evolution without rewriting all primary data. The selection guide adds a cross-workflow role: the same versioned dataset may keep embeddings, structured metadata, images, audio, video, annotations, and source records together and feed PyTorch or TensorFlow data pipelines. This can reduce copies and synchronization between retrieval, labeling, and training, although the exact integration belongs to Lance's data APIs rather than LanceDB's query layer.

## Key Characteristics
- Eliminates shared row groups in favor of independently paged columns.
- Uses a small fixed footer and separately addressable per-column metadata.
- Reuses Arrow types while adaptively selecting miniblock or full-zip structural encoding by value width.
- Permits data, dictionaries, statistics, and indexes at multiple scopes.
- Adds manifests, secondary indexes, and deletion files at dataset level.
- Targets one-I/O fixed-width and two-I/O variable-width lookup while retaining scan, compression, and multimodal access.

## Evidence
- Physical layout: [[lance-mian-xiang-ai-chang-jing-de-shu-ju-cun-chu-ge-shi]] diagrams data pages, per-column metadata, offset tables, global buffers, and the footer.
- Page independence: [[lance-mian-xiang-ai-chang-jing-de-shu-ju-cun-chu-ge-shi]] shows columns with unequal page counts and interleaved placement.
- I/O pipeline: [[lance-mian-xiang-ai-chang-jing-de-shu-ju-cun-chu-ge-shi]] separates metadata scheduling, asynchronous reads, and CPU decoding.
- Encoding model: [[lance-mian-xiang-ai-chang-jing-de-shu-ju-cun-chu-ge-shi]] compares Arrow, Parquet, mini-block, and full-zip representations of nested values.
- Dataset organization: [[lance-mian-xiang-ai-chang-jing-de-shu-ju-cun-chu-ge-shi]] lists data, version-manifest, secondary-index, and deletion directories.
- Workflow reuse: [[lancedb-xuan-xing-zhi-nan-ta-wei-shen-me-zhe-me-huo-yi-ji-ni-de-xiang-mu-shi-fou-gai-yong-ta]] describes one dataset serving retrieval, annotation, random-access sampling, and PyTorch or TensorFlow training.
- Adaptive encoding: [[2504.15247]] specifies miniblock structure, full-zip control words, repetition indexes, and the approximately 128-byte selection threshold.
- Measured tradeoffs: [[2504.15247]] compares point lookup, compression, scans, nesting, search-cache size, and struct packing against tuned Parquet and an Arrow-style Lance 2.0 proxy.

## Qualifications
The new primary paper replaces some design-only evidence with reproducible scripts and controlled measurements, but it remains a first-party LanceDB evaluation on one 2020-era NVMe drive and CPU, selected data types, warm metadata, parquet-rs 54, and experimental Lance 2.1. It does not establish current or universal results across clouds, devices, versions, writes, failures, or production mixtures. One-level nested lookup was implemented even though the repetition-index design is more general, and run-length full zip, sector alignment, and `io_uring` were future work. The selection guide's statement that Lance is based on Parquet remains imprecise: Lance is not a Parquet-compatible file. Flexible layout also increases reader, interoperability, cleanup, recovery, and compatibility responsibility.

## What Changed
- Replaced design-only encoding claims with the primary paper's miniblock, full-zip, repetition-index, and search-cache details.
- Added measured random-access, scan, compression, nesting, and struct-packing tradeoffs against tuned comparison formats.
- Added implementation limits and the single-system, first-party benchmark boundary.

## Relationships
- [[LanceDB]] - database project built on Lance.
- [[ApacheParquet]] - mature row-group-oriented comparison point, not an interchangeable file representation.
- [[ApacheArrow]] - supplies the type system and the multi-buffer structural layout that Lance adapts for storage.
- [[ColumnarStorageTradeoffs]] - frames compression, scans, random access, metadata, and evolvability choices.
- [[VectorDatabase]] - selective vector retrieval is one target workload.
- [[MultimodalDataPipelines]] - mixed tensor and media records motivate independent paging and shared workflow storage.
- [[VectorDatabaseSelection]] - unified data and training access can influence architecture fit.
- [[StoragePerformanceBenchmarking]] - format and training claims require representative measurement.

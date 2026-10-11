---
title: "Lance Format"
type: entity
tags: [storage-format, columnar-storage, vector-search, multimodal-data]
sources:
  - lance-mian-xiang-ai-chang-jing-de-shu-ju-cun-chu-ge-shi
  - lancedb-xuan-xing-zhi-nan-ta-wei-shen-me-zhe-me-huo-yi-ji-ni-de-xiang-mu-shi-fou-gai-yong-ta
last_updated: 2026-10-11
knowledge_schema: synthesis-v1
---

## Overview
[[LanceFormat]] is a storage family for vector and multimodal data, comprising a columnar file format and a dataset-level table format used by [[LanceDB]] and training-data workflows.

## Current Profile
The file format uses independently sized and placed column pages rather than shared row groups. Per-column metadata blocks are found through offset tables and a small fixed footer, allowing a reader to seek metadata for selected columns without first loading every column's metadata. Pages may contain encoded values or metadata, and dictionaries, statistics, and indexes can live at page, column, global, or dataset scope.

Lance reuses the Arrow type system while making physical encodings extensible through metadata descriptions and matching encoder-decoder implementations. The format account presents mini-block and full-zip structural encodings as workload-dependent compromises: small values accept bounded read amplification inside a compressed chunk, while large or nested values add an index to target one or two I/O operations for random access.

At dataset level, Lance groups data files with version manifests, secondary indexes, and deletion files. External type, encoding, index, statistics, version, and deletion information is intended to permit evolution without rewriting all primary data. The selection guide adds a cross-workflow role: the same versioned dataset may keep embeddings, structured metadata, images, audio, video, annotations, and source records together and feed PyTorch or TensorFlow data pipelines. This can reduce copies and synchronization between retrieval, labeling, and training, although the exact integration belongs to Lance's data APIs rather than LanceDB's query layer.

## Key Characteristics
- Eliminates shared row groups in favor of independently paged columns.
- Uses a small fixed footer and separately addressable per-column metadata.
- Reuses Arrow types while allowing encoding implementations to evolve as extensions.
- Permits data, dictionaries, statistics, and indexes at multiple scopes.
- Adds manifests, secondary indexes, and deletion files at dataset level.
- Targets selective random access, scans, vector and text retrieval, multimodal records, and model-training access.

## Evidence
- Physical layout: [[lance-mian-xiang-ai-chang-jing-de-shu-ju-cun-chu-ge-shi]] diagrams data pages, per-column metadata, offset tables, global buffers, and the footer.
- Page independence: [[lance-mian-xiang-ai-chang-jing-de-shu-ju-cun-chu-ge-shi]] shows columns with unequal page counts and interleaved placement.
- I/O pipeline: [[lance-mian-xiang-ai-chang-jing-de-shu-ju-cun-chu-ge-shi]] separates metadata scheduling, asynchronous reads, and CPU decoding.
- Encoding model: [[lance-mian-xiang-ai-chang-jing-de-shu-ju-cun-chu-ge-shi]] compares Arrow, Parquet, mini-block, and full-zip representations of nested values.
- Dataset organization: [[lance-mian-xiang-ai-chang-jing-de-shu-ju-cun-chu-ge-shi]] lists data, version-manifest, secondary-index, and deletion directories.
- Workflow reuse: [[lancedb-xuan-xing-zhi-nan-ta-wei-shen-me-zhe-me-huo-yi-ji-ni-de-xiang-mu-shi-fou-gai-yong-ta]] describes one dataset serving retrieval, annotation, random-access sampling, and PyTorch or TensorFlow training.

## Qualifications
Both sources are secondary accounts drawing heavily on project materials. They explain mechanisms and intended workflows but do not reproduce scan performance, million-column scalability, random-access bounds, distributed sampling, or training-throughput claims. The selection guide's statement that Lance is based on Parquet is imprecise relative to the distinct row-group-free physical design described by the format account; Lance should not be assumed to be a Parquet-compatible file. Flexible layout and metadata can improve evolvability while increasing reader, interoperability, compaction, cleanup, recovery, and compatibility responsibility. Pure sequential, stable, very large training corpora may still fit mature shard-streaming formats better.

## What Changed
- Added the format's role as a shared retrieval, annotation, and model-training data layer.
- Distinguished Arrow ecosystem compatibility and columnar lineage from Parquet file compatibility.
- Added sequential-training maturity and operational responsibility as explicit limits.

## Relationships
- [[LanceDB]] - database project built on Lance.
- [[ApacheParquet]] - mature row-group-oriented comparison point, not an interchangeable file representation.
- [[ColumnarStorageTradeoffs]] - frames compression, scans, random access, metadata, and evolvability choices.
- [[VectorDatabase]] - selective vector retrieval is one target workload.
- [[MultimodalDataPipelines]] - mixed tensor and media records motivate independent paging and shared workflow storage.
- [[VectorDatabaseSelection]] - unified data and training access can influence architecture fit.
- [[StoragePerformanceBenchmarking]] - format and training claims require representative measurement.

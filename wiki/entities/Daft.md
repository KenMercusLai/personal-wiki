---
title: "Daft"
type: entity
tags: [dataframe, multimodal-data, query-engine, rust, distributed-computing]
sources:
  - dang-ai-yu-shang-shu-ju-guan-dao-daft-yi-ge-duo-mo-tai-shi-dai-de-shu-ju-yin-qing
last_updated: 2026-10-07
knowledge_schema: synthesis-v1
---

## Overview
[[Daft]] is represented as a Python-facing, Rust-backed DataFrame engine designed to make heterogeneous file, image, tensor, embedding, and model operations visible to query planning and execution.

## Current Profile
The available source positions Daft between single-machine analytical engines and conventional distributed data systems. Users build lazy plans through a Python API, Arrow FFI connects that layer to Rust without copying compatible buffers, Swordfish streams bounded morsels through separately scheduled I/O and compute stages, and Flotilla extends the same logical plan across node-level workers. The distinctive claim is not merely support for media files or UDFs, but that operations such as downloading, decoding, resizing, and inference carry enough structure for pushdown, stage splitting, batching, memory control, and resource-aware execution.

This profile is architectural and source-scoped. It records how the article says Daft works and where it fits; it does not independently establish the performance, reliability, adoption, or priority claims made for the project.

## Key Characteristics
- Treats multimodal operations as structured expressions that the optimizer can inspect and rearrange.
- Combines a [[Python]] API and model boundary with Rust execution through Arrow-compatible memory interchange.
- Streams work through Swordfish with separate I/O and compute runtimes plus cooperative memory backpressure.
- Carries lazy evaluation from logical plans through scan-task creation to on-demand file reads.
- Uses one Flotilla worker per cluster node to share memory and fractional GPU capacity across operations.

## Evidence
- Visible operations: [[dang-ai-yu-shang-shu-ju-guan-dao-daft-yi-ge-duo-mo-tai-shi-dai-de-shu-ju-yin-qing]] shows `download`, `decode`, and `resize` becoming separate plan stages after filters are pushed down.
- Language boundary: [[dang-ai-yu-shang-shu-ju-guan-dao-daft-yi-ge-duo-mo-tai-shi-dai-de-shu-ju-yin-qing]] describes PyO3 bindings and Arrow's C Data Interface between the Python layer and Rust engine.
- Streaming control: [[dang-ai-yu-shang-shu-ju-guan-dao-daft-yi-ge-duo-mo-tai-shi-dai-de-shu-ju-yin-qing]] describes morsels, asynchronous channels, isolated I/O and compute runtimes, and permit-governed memory allocation.
- Lazy I/O: [[dang-ai-yu-shang-shu-ju-guan-dao-daft-yi-ge-duo-mo-tai-shi-dai-de-shu-ju-yin-qing]] places scan materialization after pushdown and delays file content reads until an operation needs bytes.
- Distributed resources: [[dang-ai-yu-shang-shu-ju-guan-dao-daft-yi-ge-duo-mo-tai-shi-dai-de-shu-ju-yin-qing]] depicts a node-level Swordfish worker sharing memory and GPU capacity, exchanging Arrow Flight data, and spilling to NVMe.

## Qualifications
The single available article supplies no raw benchmark data, reproducible configurations, version-pinned source references, or independent production testimony. Its comparisons compress the design space of Pandas, Polars, DuckDB, Spark, and Ray Data, and its claims about being first, avoiding failures, saving compute, and running without bugs should be treated as reported rather than verified. Zero-copy, batching, thresholds, operator rules, and resource behavior are conditional on data layout, operation type, runtime configuration, and software version.

## What Changed
- Created a source-bounded profile of Daft's optimizer-visible multimodal operations.
- Recorded Swordfish streaming, three-layer laziness, and Flotilla node-level resource management as connected parts of one execution model.
- Preserved benchmark, comparison, version, and zero-copy limitations rather than treating promotional claims as established results.

## Relationships
- [[MultimodalDataPipelines]] - workload class Daft is designed to execute.
- [[AdaptiveBackpressure]] - related mechanism that bounds work and memory as downstream stages slow.
- [[DataIntensiveSystems]] - broader architecture domain containing Daft's storage, execution, and scheduling decisions.
- [[DistributedProgramming]] - Flotilla extends the plan across cluster nodes.
- [[Python]] - user API, UDF, and model-inference boundary.
- [[ApacheParquet]] - columnar format used in the article's examples and deployments.

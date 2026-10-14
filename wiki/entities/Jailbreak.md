---
title: "Jailbreak"
type: entity
tags: [database, storage, apache-arrow, code-synthesis]
sources:
  - 2607.07696
last_updated: 2026-10-13
knowledge_schema: synthesis-v1
---

## Overview
[[Jailbreak]] is a Cornell research project that bypasses PostgreSQL and MySQL server and wire-protocol paths by decoding database storage files directly into Apache Arrow buffers.

## Current Profile
The evaluated artifact consists of self-contained C++17 shared libraries for PostgreSQL heap files and MySQL InnoDB `.ibd` files. Each accepts a runtime column specification, performs a sequential storage scan, builds typed Arrow buffers, and transfers them through the Arrow C Data Interface without copying into a downstream engine-specific representation.

The broader project adds a four-role generation pipeline: a Dataset Generator creates deterministic test data, an Architect writes a storage-format specification, a Coder produces the shared library, and a QA Tester compiles and compares its Arrow output with database-derived ground truth. Compilation, runtime, and result failures feed another coding attempt, with checkpointing and a default ten-attempt budget.

## Key Characteristics
- Removes the database server and JDBC, ODBC, or connector row path from controlled analytical extraction.
- Targets table-independent runtime decoding into zero-copy Apache Arrow RecordBatches.
- Uses deterministic generated data and output statistics as its main correctness oracle.
- Applies iterative LLM diagnosis and regeneration only after deterministic checks fail.
- Remains an early snapshot-oriented prototype rather than a demonstrated general live-database replacement.

## Evidence
- Storage readers: [[2607.07696]] describes roughly 800-line PostgreSQL and MySQL C++17 readers with no dependency beyond the standard library.
- Interchange boundary: [[2607.07696]] exports ArrowSchema and ArrowArray through the Arrow C Data Interface for DuckDB, DataFusion, PyArrow, cuDF, Spark, and Spark RAPIDS consumers.
- Verification loop: [[2607.07696]] shows the four sequential roles and a QA-to-Coder failure loop, with deterministic aggregates and checkpointed retries.
- Reported performance: [[2607.07696]] reports up to 5.1x PostgreSQL and 26.9x MySQL acceleration on its TPC-H SF=1 database-to-Parquet benchmark.

## Qualifications
The source is a first-party early evaluation on one AWS instance, one approximately 880 MB TPC-H table, selected schemas, and unspecified database-version breadth. Best-of-three wall-clock results combine source access with engine startup and Parquet writing, so they do not isolate reader throughput. Snapshot operation avoids the hardest live-concurrency boundary, PostgreSQL visibility is deliberately lightweight, numeric values are reduced to float64, and systematic agent-pipeline convergence, latency, retry, and ablation results remain future work.

## What Changed
- Created a project profile separating the evaluated storage readers from the less fully evaluated automated generation pipeline.

## Relationships
- [[VictorGiannakouris]] - coauthor and project researcher.
- [[ImmanuelTrummer]] - coauthor and project researcher.
- [[DatabaseBypass]] - core data-access strategy implemented by Jailbreak.
- [[AgenticStorageReaderSynthesis]] - generation method proposed for extending Jailbreak to other formats.
- [[PostgreSQL]] - source system whose heap files and BRIN metadata are decoded.
- [[MySQL]] - source system whose InnoDB tablespace pages are decoded.
- [[AgenticWorkflowPatterns]] - supplies the generate-evaluate-repair control-loop pattern.

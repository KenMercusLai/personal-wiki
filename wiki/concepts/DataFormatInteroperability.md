---
title: "Data Format Interoperability"
type: concept
tags: [data-engineering, interoperability, serialization, schemas, compatibility]
sources:
  - data-wrangling-at-slack-several-people-are-coding
last_updated: 2026-09-27
knowledge_schema: synthesis-v1
---

## Definition
[[DataFormatInteroperability]] is the ability of different processing engines and software versions to read and write shared persisted data with the same structure, values, and meaning over time.

## Current Synthesis
A common file-format label is only the visible part of the contract. Interoperability also depends on library versions, patched bugs, null and nested-value semantics, field identity by name or position, physical encodings, catalog metadata, partition schemas, and the readers still operating during an upgrade. Slack's case shows two failure classes: explicit errors that stop a job and silent semantic corruption that returns plausible values in the wrong columns. Preserving tool choice therefore requires constraining writes to a tested common subset, validating every reader/writer combination, and sometimes owning a stable serialization boundary rather than inheriting each engine's bundled implementation.

## Key Claims
- Shared format support does not imply identical read and write behavior across engines.
- Persisted-data compatibility includes physical files, table metadata, partition metadata, and every live reader version.
- Silent value reinterpretation is more dangerous than a visible exception because it can survive normal job-success checks.
- Null handling, nested structures, column identity, and schema offsets are part of the effective data contract.
- Append-oriented flat schemas can reduce rewrite costs but exchange structural expressiveness for evolution safety.
- Version-pinned serialization and deserialization can isolate data from engine upgrades when accompanied by cross-version testing.
- Multi-engine flexibility may require limiting data to the intersection of supported features.

## Evidence
- Version divergence: [[data-wrangling-at-slack-several-people-are-coding]] reports Hive, Spark, and Presto using different Parquet-library versions and different subsets of fixes.
- Null semantics: [[data-wrangling-at-slack-several-people-are-coding]] describes Hive and Presto failures involving absent scalar data and null keys in complex structures.
- Schema layers: [[data-wrangling-at-slack-several-people-are-coding]] says file, table, and partition schemas all had to agree for correct reads.
- Silent corruption: [[data-wrangling-at-slack-several-people-are-coding]] shows Presto's position-based default mapping values into the wrong columns where Hive's name-based reads remained correct.
- Stable boundary: [[data-wrangling-at-slack-several-people-are-coding]] describes Slack-owned Hive input and Parquet output formats that pinned encoding and decoding behavior across EMR versions.

## Counterevidence & Qualifications
The synthesis is grounded in one historical, first-party Slack account using specific 2016 versions of EMR, Hive, Presto, Spark, and Parquet. It does not show that custom format forks are always preferable to coordinated upgrades, upstream fixes, format conformance suites, or managed table formats. Flattening and restricting schemas can reduce immediate compatibility risk while increasing duplication, weakening nested modeling, perpetuating legacy workarounds, and shifting maintenance responsibility onto the platform team.

## What Changed
- Created the concept to treat implementation behavior, metadata, and live reader versions as one persisted-data contract.
- Distinguished visible job failures from silent semantic corruption.
- Added version-pinned serialization and feature-intersection design as source-scoped mitigation patterns.

## Related Concepts
- [[APIBackwardCompatibility]] - applies a similar compatibility obligation to service interfaces and client integrations.
- [[ChangeSafety]] - schema and engine upgrades need staged validation, bounded rollout, and recovery paths.
- [[LayeredDataWarehouse]] - warehouse organization depends on data remaining interpretable across transformation and consumption layers.
- [[DataManagementPlatform]] - shared storage and metadata become useful only when participating tools preserve consistent meaning.
- [[SchemaBasedReasoning]] - explicit schemas help structure data but do not by themselves guarantee consistent implementation semantics.

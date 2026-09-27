---
title: "Apache Parquet"
type: entity
tags: [software, data-engineering, columnar-storage, file-format]
sources:
  - data-wrangling-at-slack-several-people-are-coding
last_updated: 2026-09-27
knowledge_schema: synthesis-v1
---

## Overview
[[ApacheParquet]] is represented as the shared columnar file format in Slack's 2016 S3 data warehouse and as the boundary where supposedly compatible analytics engines exposed materially different behavior.

## Current Profile
Slack selected Parquet because Hive, Presto, and Spark could all use it and because columnar storage improved query and space efficiency. The source shows, however, that the effective format included more than a specification: each engine brought a different library version, patches, null semantics, schema mapping behavior, and encoding support. Slack ultimately pinned Parquet writing and Hive reading behind formats it owned so cluster upgrades would not silently redefine persisted data.

## Key Characteristics
- Stores columnar files with a schema embedded in each file.
- Serves as a shared persistence layer across Hive, Presto, and Spark in the Slack account.
- Exposes implementation-dependent behavior around nulls, complex structures, field ordering, and encoding versions.
- Must remain compatible with table and partition metadata as schemas evolve.
- Can require an owned, version-pinned read/write boundary when engine-bundled libraries diverge.

## Evidence
- Shared foundation: [[data-wrangling-at-slack-several-people-are-coding]] says all three engines supported Parquet and benefited from its query and storage efficiency.
- Divergent implementations: [[data-wrangling-at-slack-several-people-are-coding]] reports different library versions and bug-fix subsets across Hive, Spark, and Presto.
- Schema interaction: [[data-wrangling-at-slack-several-people-are-coding]] describes file, table, and partition schemas that had to remain aligned.
- Compatibility control: [[data-wrangling-at-slack-several-people-are-coding]] says Slack wrote a Parquet output format and Hive input format that pinned serialization behavior.

## Qualifications
This profile reflects one 2016 Slack deployment, not Parquet's complete specification, current implementations, or present-day best practice. The source does not compare Parquet with other formats, quantify storage or query gains, or establish that the reported bugs and defaults remain in current releases.

## What Changed
- Created a source-bounded profile of Parquet as both Slack's common warehouse format and its main cross-engine compatibility boundary.

## Relationships
- [[Slack]] - company operating the multi-engine warehouse in the source.
- [[DataFormatInteroperability]] - Parquet is the concrete format through which incompatible implementations surfaced.
- [[APIBackwardCompatibility]] - related obligation to preserve existing consumers as encodings evolve.
- [[ChangeSafety]] - format and engine upgrades need explicit compatibility validation.

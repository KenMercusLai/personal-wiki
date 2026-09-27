---
title: "GreptimeDB"
type: entity
tags: [database, time-series, lsm-tree, parquet]
sources:
  - eric-fu-dao-di-shi-yao-shi-xu-shu-ju-ku
last_updated: 2026-09-27
knowledge_schema: synthesis-v1
---

## Overview
[[GreptimeDB]] is presented as an emerging time-series database with named, tagged series, multiple fields, and an LSM-tree storage engine using columnar Parquet files.

## Current Profile
The source places GreptimeDB inside its time-series data model while noting its relational borrowing. It describes SST files ordered by tags and then timestamp, a layout the author infers may preserve time-range scan performance while accommodating updates and point lookups.

## Key Characteristics
- Represents series through a metric name and tags.
- Permits multiple fields within the model.
- Uses an LSM-tree storage engine.
- Stores SST data in columnar Parquet ordered by tags and timestamp.

## Evidence
- Series model: [[eric-fu-dao-di-shi-yao-shi-xu-shu-ju-ku]] says GreptimeDB uses metric names and tags and can carry several fields.
- Storage engine: [[eric-fu-dao-di-shi-yao-shi-xu-shu-ju-ku]] identifies an LSM-tree design with Parquet SST files.
- Sort order: [[eric-fu-dao-di-shi-yao-shi-xu-shu-ju-ku]] reports ordering by `(tag-1, ..., tag-m, timestamp)`.

## Qualifications
The article calls the performance rationale for this sort order a guess. It supplies no benchmark, version pin, or production comparison, so the evidence supports the described structure more strongly than its claimed tradeoffs.

## What Changed
- Established GreptimeDB's time-series model and its reported LSM-Parquet storage layout.

## Relationships
- [[TimeSeriesDatabase]] - GreptimeDB fits the source's name-label-series definition.
- [[InfluxDB]] - both expose a relationally influenced metric, tag, and field model.
- [[QuestDB]] - both use columnar structures but are classified differently by the source.
- [[EricFu]] - author providing the storage-layout interpretation.

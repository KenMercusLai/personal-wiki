---
title: "Time Series Database"
type: concept
tags: [database, time-series, data-model, analytics]
sources:
  - eric-fu-dao-di-shi-yao-shi-xu-shu-ju-ku
last_updated: 2026-09-27
knowledge_schema: synthesis-v1
---

## Definition
[[TimeSeriesDatabase]] is a database category organized around sequences of timestamp-value pairs, where a metric or table name plus a label set identifies each series and time supplies the ordered dimension.

## Current Synthesis
The source offers a deliberately narrow, data-model-first definition. A time series is not merely any row containing a timestamp: fixing the metric name and labels yields a vector of values ordered by time. A collection of series can then be viewed either as vectors chosen by name and labels or as relational-like snapshots repeated at each query time.

That dual view explains why temporal databases need more than ordinary grouping syntax. Time-axis operations transform one series, often resampling it and filling gaps; label-axis operations combine multiple series at corresponding timestamps. Joins add another alignment problem because independently collected series rarely share exact timestamps.

The resulting category boundary is analytical rather than commercial. Engines may store temporal data efficiently while retaining a general relational or append-mostly model. Under this definition, product fit depends on whether the workload really consists of stable name-label series and needs their specialized storage and operators—not simply on the presence of time columns.

## Key Claims
- Metric or table name, label set, and timestamp jointly identify a time-series observation.
- Vector and snapshot perspectives are equivalent views that encourage different query-language designs.
- Time-axis and label-axis aggregation have different inputs, output shapes, gap behavior, and operator implementations.
- Columnar timestamp-value vectors enable compression, sequential scans, and vectorized execution.
- Joins require an explicit timestamp-alignment policy such as rounding or as-of matching.
- “Time-series database” is an overloaded market label, so data-model fit should be separated from temporal-workload optimization.

## Evidence
- Data model: [[eric-fu-dao-di-shi-yao-shi-xu-shu-ju-ku]] defines series through timestamp-value pairs and identifies them with metric names and labels.
- Equivalent views: [[eric-fu-dao-di-shi-yao-shi-xu-shu-ju-ku]] and its retained diagrams contrast whole-vector selection with repeated time snapshots.
- Aggregation split: [[eric-fu-dao-di-shi-yao-shi-xu-shu-ju-ku]] maps time aggregation from one series to one series and label aggregation from several series to one series.
- Storage consequence: [[eric-fu-dao-di-shi-yao-shi-xu-shu-ju-ku]] describes contiguous columnar timestamp and value storage as a basis for compression and query speed.
- Join alignment: [[eric-fu-dao-di-shi-yao-shi-xu-shu-ju-ku]] contrasts fixed-interval alignment with `AS OF JOIN` matching to the latest earlier timestamp.
- Category boundary: [[eric-fu-dao-di-shi-yao-shi-xu-shu-ju-ku]] includes Prometheus, InfluxDB, GreptimeDB, and TDengine under its model while excluding TimescaleDB and QuestDB.

## Counterevidence & Qualifications
The category boundary comes from one practitioner's conceptual essay and is not an industry standard. Commercial products can support several data models, evolve their storage engines, or call themselves time-series databases for workload and performance reasons even when their core abstraction is relational. The article gives architectural descriptions but no comparative benchmarks, and its GreptimeDB performance explanation is explicitly speculative. Label cardinality, update patterns, transactions, joins, ecosystem fit, and operating cost still matter when choosing an engine.

## What Changed
- Established a data-model-first definition that distinguishes true series vectors from generic timestamped rows.
- Separated time-axis aggregation, label-axis aggregation, and timestamp alignment as distinct operator concerns.
- Added an explicit qualification that market category names and internal data models need not coincide.

## Related Concepts
- [[DatabaseConsolidation]] - specialized time-series storage is justified only when its workload benefit exceeds added system complexity.
- [[TechnologyStackComplexity]] - adopting a separate temporal engine adds operational and consistency boundaries.
- [[AggregationTheory]] - time-series systems distinguish aggregation across time from aggregation across labeled series.
- [[VectorDatabase]] - both categories specialize storage around vectors, but their vector semantics and retrieval operations differ.

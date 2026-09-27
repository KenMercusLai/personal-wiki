---
title: "TDengine"
type: entity
tags: [database, time-series, supertable]
sources:
  - eric-fu-dao-di-shi-yao-shi-xu-shu-ju-ku
last_updated: 2026-09-27
knowledge_schema: synthesis-v1
---

## Overview
[[TDengine]] is presented as a time-series database using named tables, tags, fields, and a supertable abstraction that groups tag-partitioned subtables.

## Current Profile
The source describes an evolution from recommending one table per collection point toward supertables. The earlier physical-table approach optimized local efficiency but made growing queries enumerate ever more tables; the later abstraction restores one logical table divided into subtables by tag values.

## Key Characteristics
- Uses table names and tags to identify series-like partitions.
- Supports multiple fields.
- Historically encouraged one table per collection point for efficiency.
- Uses supertables to group tag-partitioned subtables behind one logical table.

## Evidence
- Data model: [[eric-fu-dao-di-shi-yao-shi-xu-shu-ju-ku]] maps TDengine tables, tags, and fields onto the article's series model.
- Early approach: [[eric-fu-dao-di-shi-yao-shi-xu-shu-ju-ku]] says users were advised to create a table for each collection point.
- Query pressure: [[eric-fu-dao-di-shi-yao-shi-xu-shu-ju-ku]] says scaling required queries to reference increasing numbers of tables.
- Supertable response: [[eric-fu-dao-di-shi-yao-shi-xu-shu-ju-ku]] describes one logical table split into subtables by tags.

## Qualifications
The article gives a concise historical account without version dates, measurements, or independent validation. Its comparison with InfluxDB is conceptual and does not establish equivalent operational behavior.

## What Changed
- Established TDengine's table-per-collector history and supertable response to query scaling.

## Relationships
- [[TimeSeriesDatabase]] - TDengine fits the source's named and tagged series definition.
- [[InfluxDB]] - the source compares supertable tag partitioning with InfluxDB's tag-defined vectors.
- [[GreptimeDB]] - another relationally influenced engine included in the author's narrow category.
- [[DatabaseConsolidation]] - TDengine illustrates both specialized fit and the cost of physical partition proliferation.

---
title: "InfluxDB"
type: entity
tags: [database, time-series, storage]
sources:
  - eric-fu-dao-di-shi-yao-shi-xu-shu-ju-ku
last_updated: 2026-09-27
knowledge_schema: synthesis-v1
---

## Overview
[[InfluxDB]] is presented as a time-series database whose measurements, tags, and fields organize data into time-ordered series.

## Current Profile
The source uses InfluxDB as the main vector-perspective example. InfluxQL resembles SQL but selects one or more series by measurement and tags before applying operations across their points. Its Time-Structured Merge Tree storage groups series by tags and orders their values by timestamp.

## Key Characteristics
- Uses measurements as names, tags as series identity, and fields as recorded values.
- Encourages a data-oriented or whole-series query perspective through InfluxQL.
- Stores tag-partitioned series in timestamp order through its TSM engine.
- Is sensitive to high tag cardinality because distinct tag combinations create more series.

## Evidence
- Data model: [[eric-fu-dao-di-shi-yao-shi-xu-shu-ju-ku]] maps InfluxDB measurements and tags onto metric names and labels.
- Query design: [[eric-fu-dao-di-shi-yao-shi-xu-shu-ju-ku]] describes InfluxQL as SQL-like and vector-oriented.
- Storage layout: [[eric-fu-dao-di-shi-yao-shi-xu-shu-ju-ku]] says TSM separates series by tags and sorts by timestamp.
- Cardinality limit: [[eric-fu-dao-di-shi-yao-shi-xu-shu-ju-ku]] warns that too many tags create too many vectors and hurt queries.

## Qualifications
The source offers a high-level architectural description rather than a version-specific product evaluation or benchmark. “Too many” tags is not quantified and depends on workload, schema, engine version, and deployment.

## What Changed
- Established InfluxDB as the vector-oriented reference case in the time-series data model.

## Relationships
- [[TimeSeriesDatabase]] - InfluxDB closely fits the source's named and labeled series definition.
- [[Prometheus]] - contrasted as a snapshot-oriented query system.
- [[TDengine]] - its tag-partitioned supertable design is compared with InfluxDB's series grouping.
- [[TechnologyStackComplexity]] - InfluxDB can add a specialized datastore boundary when a general database might suffice.

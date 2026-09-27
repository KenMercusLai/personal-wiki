---
title: "InfluxDB"
type: entity
tags: [database, time-series, storage]
sources:
  - eric-fu-dao-di-shi-yao-shi-xu-shu-ju-ku
  - fastnetmon-grafana-jian-kong-wang-duan-liu-liang-ji-ddos-yu-jing
last_updated: 2026-09-28
knowledge_schema: synthesis-v1
---

## Overview
[[InfluxDB]] is presented as a time-series database whose measurements, tags, and fields organize data into time-ordered series and whose protocol adapters can receive operational metrics.

## Current Profile
One source uses InfluxDB as the main vector-perspective example: InfluxQL selects series by measurement and tags before applying operations across their points, while its Time-Structured Merge Tree storage groups series by tags and orders values by timestamp. A second, older source supplies an operational example in which InfluxDB's Graphite listener maps [[FastNetMon]] metric paths into stored traffic series that [[Grafana]] queries.

## Key Characteristics
- Uses measurements as names, tags as series identity, and fields as recorded values.
- Encourages a data-oriented or whole-series query perspective through InfluxQL.
- Stores tag-partitioned series in timestamp order through its TSM engine.
- Is sensitive to high tag cardinality because distinct tag combinations create more series.
- Can ingest hierarchical Graphite metrics through templates that assign path segments to measurements and tags.
- Serves as the storage and query boundary between FastNetMon collection and Grafana visualization in the demonstrated monitoring pipeline.

## Evidence
- Data model: [[eric-fu-dao-di-shi-yao-shi-xu-shu-ju-ku]] maps InfluxDB measurements and tags onto metric names and labels.
- Query design: [[eric-fu-dao-di-shi-yao-shi-xu-shu-ju-ku]] describes InfluxQL as SQL-like and vector-oriented.
- Storage layout: [[eric-fu-dao-di-shi-yao-shi-xu-shu-ju-ku]] says TSM separates series by tags and sorts by timestamp.
- Cardinality limit: [[eric-fu-dao-di-shi-yao-shi-xu-shu-ju-ku]] warns that too many tags create too many vectors and hurt queries.
- Protocol ingestion: [[fastnetmon-grafana-jian-kong-wang-duan-liu-liang-ji-ddos-yu-jing]] configures a TCP Graphite listener and templates for host, network, total, direction, and resource path segments.
- Monitoring role: [[fastnetmon-grafana-jian-kong-wang-duan-liu-liang-ji-ddos-yu-jing]] places InfluxDB between FastNetMon's metric export and Grafana's traffic dashboard.

## Qualifications
The data-model source offers a high-level architectural description rather than a version-specific product evaluation or benchmark. “Too many” tags is not quantified and depends on workload, schema, engine version, and deployment. The monitoring source uses InfluxDB 1.7.6-era configuration and proves only that its chosen Graphite mapping produced dashboard data; it does not evaluate retention, cardinality, durability, access control, or current compatibility.

## What Changed
- Established InfluxDB as the vector-oriented reference case in the time-series data model.
- Added Graphite protocol ingestion and a concrete network-monitoring role alongside the conceptual data model.

## Relationships
- [[TimeSeriesDatabase]] - InfluxDB closely fits the source's named and labeled series definition.
- [[Prometheus]] - contrasted as a snapshot-oriented query system.
- [[TDengine]] - its tag-partitioned supertable design is compared with InfluxDB's series grouping.
- [[TechnologyStackComplexity]] - InfluxDB can add a specialized datastore boundary when a general database might suffice.
- [[FastNetMon]] - emits the hierarchical traffic metrics received by InfluxDB in the monitoring example.
- [[Grafana]] - queries InfluxDB to render traffic gauges, trends, and top-talker tables.
- [[DDoSTrafficMonitoring]] - uses InfluxDB as the historical metric store between detection and visualization.

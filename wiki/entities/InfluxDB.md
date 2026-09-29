---
title: "InfluxDB"
type: entity
tags: [database, time-series, storage]
sources:
  - eric-fu-dao-di-shi-yao-shi-xu-shu-ju-ku
  - fastnetmon-grafana-jian-kong-wang-duan-liu-liang-ji-ddos-yu-jing
  - how-i-turned-a-cheap-weather-station-into-a-personal-devops-dashboard
last_updated: 2026-09-29
knowledge_schema: synthesis-v1
---

## Overview
[[InfluxDB]] is presented as a time-series database whose measurements, tags, and fields organize time-ordered series and whose integrations receive operational or sensor events for historical query.

## Current Profile
The conceptual source uses InfluxDB as a vector-perspective example: InfluxQL selects series by measurement and tags before operations across points, while TSM storage groups series by tags and time. Two operational examples then show distinct ingestion paths. FastNetMon sends hierarchical Graphite metrics through a listener; [[HomeAssistant]] writes events through its native integration using an organization, bucket, and token. In both, InfluxDB separates durable history from [[Grafana]] presentation, while the weather case adds Flux windowing, pivoting, quantiles, and reshaping.

## Key Characteristics
- Uses measurements as names, tags as series identity, and fields as recorded values.
- Encourages a data-oriented or whole-series query perspective through InfluxQL.
- Stores tag-partitioned series in timestamp order through its TSM engine.
- Is sensitive to high tag cardinality because distinct tag combinations create more series.
- Can ingest hierarchical Graphite metrics through templates that assign path segments to measurements and tags.
- Can receive Home Assistant events into a version-2 organization and bucket through token-authenticated integration.
- Serves as a durable storage and query boundary between collection systems and Grafana visualization.

## Evidence
- Data model: [[eric-fu-dao-di-shi-yao-shi-xu-shu-ju-ku]] maps InfluxDB measurements and tags onto metric names and labels.
- Query design: [[eric-fu-dao-di-shi-yao-shi-xu-shu-ju-ku]] describes InfluxQL as SQL-like and vector-oriented.
- Storage layout: [[eric-fu-dao-di-shi-yao-shi-xu-shu-ju-ku]] says TSM separates series by tags and sorts by timestamp.
- Cardinality limit: [[eric-fu-dao-di-shi-yao-shi-xu-shu-ju-ku]] warns that too many tags create too many vectors and hurt queries.
- Protocol ingestion: [[fastnetmon-grafana-jian-kong-wang-duan-liu-liang-ji-ddos-yu-jing]] configures a TCP Graphite listener and templates for host, network, total, direction, and resource path segments.
- Monitoring role: [[fastnetmon-grafana-jian-kong-wang-duan-liu-liang-ji-ddos-yu-jing]] places InfluxDB between FastNetMon's metric export and Grafana's traffic dashboard.
- Home integration: [[how-i-turned-a-cheap-weather-station-into-a-personal-devops-dashboard]] configures Home Assistant to write events to a named InfluxDB 2 bucket with a dedicated token.
- Historical analysis: [[how-i-turned-a-cheap-weather-station-into-a-personal-devops-dashboard]] queries retained weather entities with Flux windowing, pivots, filters, and quantiles for Grafana panels.

## Qualifications
The data-model source offers a high-level architecture rather than a benchmark, and “too many” tags is workload- and version-dependent. The two deployments use historical 1.7.6 and 2.5.1 configurations. They prove that chosen Graphite and Home Assistant paths produced dashboard data, not retention guarantees, durability, backup recovery, access control, current compatibility, or analytical correctness.

## What Changed
- Added a second ingestion pattern based on Home Assistant's native InfluxDB 2 integration and token-separated clients.
- Extended the operational profile from network metrics to long-lived personal sensor history and Flux analysis.

## Relationships
- [[TimeSeriesDatabase]] - InfluxDB closely fits the source's named and labeled series definition.
- [[Prometheus]] - contrasted as a snapshot-oriented query system.
- [[TDengine]] - its tag-partitioned supertable design is compared with InfluxDB's series grouping.
- [[TechnologyStackComplexity]] - InfluxDB can add a specialized datastore boundary when a general database might suffice.
- [[FastNetMon]] - emits the hierarchical traffic metrics received by InfluxDB in the monitoring example.
- [[Grafana]] - queries InfluxDB to render traffic gauges, trends, and top-talker tables.
- [[DDoSTrafficMonitoring]] - uses InfluxDB as the historical metric store between detection and visualization.
- [[HomeAssistant]] - writes the demonstrated household sensor events into an InfluxDB bucket.
- [[PersonalTelemetryPipeline]] - InfluxDB supplies durable retention and query semantics between integration and visualization.

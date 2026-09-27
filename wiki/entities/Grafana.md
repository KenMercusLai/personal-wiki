---
title: "Grafana"
type: entity
tags: [observability, dashboard, visualization]
sources:
  - fastnetmon-grafana-jian-kong-wang-duan-liu-liang-ji-ddos-yu-jing
last_updated: 2026-09-28
knowledge_schema: synthesis-v1
---

## Overview
[[Grafana]] is represented as the dashboard layer used to inspect stored network-traffic metrics.

## Current Profile
In the source's historical monitoring stack, Grafana queries [[InfluxDB]] data populated from [[FastNetMon]]'s Graphite export. The inspected dashboard combines current gauges, short time-series traces, and ranked per-host tables to make direction, volume, packet rate, and heavy talkers visible together.

## Key Characteristics
- Uses InfluxDB as a configured data source in the demonstrated deployment.
- Displays inbound and outbound bandwidth in Mbps and packet rates in kpps.
- Combines aggregate gauges and trends with per-host average and current values.
- Supports dashboard templates, although the cited template and Grafana release are version-specific historical references.

## Evidence
- Data-source role: [[fastnetmon-grafana-jian-kong-wang-duan-liu-liang-ji-ddos-yu-jing]] places Grafana after FastNetMon's Graphite export and InfluxDB storage.
- Dashboard composition: the retained screenshot in [[fastnetmon-grafana-jian-kong-wang-duan-liu-liang-ji-ddos-yu-jing]] shows Mbps In/Out, PPS In/Out, time traces, and Top Incoming/Outgoing tables.
- Operational view: [[fastnetmon-grafana-jian-kong-wang-duan-liu-liang-ji-ddos-yu-jing]] shows a five-second refresh over the last hour, making it a near-real-time view rather than proof of long-term alert quality.

## Qualifications
The source demonstrates visualization, not Grafana-based alert evaluation or response automation. The screenshot is one configured dashboard from 2019, with host labels blurred and no evidence about retention, query cost, dashboard correctness, access control, or current compatibility.

## What Changed
- Established Grafana as the presentation layer for FastNetMon-derived network traffic in this source.
- Added a concrete dashboard example that joins aggregate rates with top-talker detail.

## Relationships
- [[FastNetMon]] - originates the traffic metrics visualized in the dashboard.
- [[InfluxDB]] - acts as Grafana's data source in the demonstrated pipeline.
- [[DDoSTrafficMonitoring]] - dashboards provide situational awareness around detection and investigation.
- [[TimeSeriesDatabase]] - supplies timestamped measurements for trends and current-state views.

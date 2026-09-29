---
title: "Grafana"
type: entity
tags: [observability, dashboard, visualization]
sources:
  - fastnetmon-grafana-jian-kong-wang-duan-liu-liang-ji-ddos-yu-jing
  - how-i-turned-a-cheap-weather-station-into-a-personal-devops-dashboard
last_updated: 2026-09-29
knowledge_schema: synthesis-v1
---

## Overview
[[Grafana]] is represented as a programmable dashboard layer for inspecting stored operational and sensor time series.

## Current Profile
Across two historical practitioner stacks, Grafana queries [[InfluxDB]] while remaining separate from metric acquisition and storage. The network-monitoring case combines current gauges, short traces, and ranked hosts. The personal-weather case uses Flux, dashboard variables, plugins, mappings, thresholds, overrides, heatmaps, wind roses, and percentile bands to explore noisy sensor history. Together they show Grafana as both an operational display and an analytical workbench whose output depends on upstream query semantics.

## Key Characteristics
- Uses InfluxDB as a configured data source in the demonstrated deployment.
- Combines summary values, temporal trends, distributions, directional views, and ranked detail in composed dashboards.
- Exposes source-native queries, including Flux transformations for filtering, windowing, pivoting, quantiles, and field shaping.
- Supports variables, plugins, mappings, thresholds, and per-series overrides for domain-specific interaction and presentation.
- Makes alternative views easy to compare, but does not by itself guarantee valid aggregation, alignment, or statistical interpretation.

## Evidence
- Data-source role: [[fastnetmon-grafana-jian-kong-wang-duan-liu-liang-ji-ddos-yu-jing]] places Grafana after FastNetMon's Graphite export and InfluxDB storage.
- Dashboard composition: the retained screenshot in [[fastnetmon-grafana-jian-kong-wang-duan-liu-liang-ji-ddos-yu-jing]] shows Mbps In/Out, PPS In/Out, time traces, and Top Incoming/Outgoing tables.
- Query workbench: [[how-i-turned-a-cheap-weather-station-into-a-personal-devops-dashboard]] uses Flux to align wind direction and speed, calculate windowed summaries and percentiles, and reshape fields for panels.
- Specialized presentation: [[how-i-turned-a-cheap-weather-station-into-a-personal-devops-dashboard]] demonstrates a wind-rose plugin, a speed heatmap, compass mappings, directional thresholds, and style overrides.
- Complementary horizons: [[fastnetmon-grafana-jian-kong-wang-duan-liu-liang-ji-ddos-yu-jing]] shows a near-real-time network view, while [[how-i-turned-a-cheap-weather-station-into-a-personal-devops-dashboard]] emphasizes retained history and adjustable analysis windows.

## Qualifications
Both sources demonstrate configured visualizations rather than Grafana alert quality, response automation, access control, query cost, or long-term operational reliability. They use historical versions and plugins. The weather case also exposes analytical hazards: exact alignment may drop samples, angle percentiles can be misleading across the north boundary, and attractive panels can conceal transformation assumptions.

## What Changed
- Expanded Grafana from a network-monitoring display into a source-native analytical workbench for noisy sensor data.
- Added domain-specific plugins, dashboard variables, heatmaps, percentile bands, mappings, thresholds, and style overrides.

## Relationships
- [[FastNetMon]] - originates the traffic metrics visualized in the dashboard.
- [[InfluxDB]] - acts as Grafana's data source in the demonstrated pipeline.
- [[DDoSTrafficMonitoring]] - dashboards provide situational awareness around detection and investigation.
- [[TimeSeriesDatabase]] - supplies timestamped measurements for trends and current-state views.
- [[HomeAssistant]] - forwards the weather entities retained in InfluxDB and later explored in Grafana.
- [[PersonalTelemetryPipeline]] - Grafana supplies the analysis and presentation stage.

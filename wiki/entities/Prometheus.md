---
title: "Prometheus"
type: entity
tags: [database, monitoring, time-series, open-source]
sources:
  - eric-fu-dao-di-shi-yao-shi-xu-shu-ju-ku
last_updated: 2026-09-27
knowledge_schema: synthesis-v1
---

## Overview
[[Prometheus]] is an open-source monitoring and time-series system whose metrics are named, labeled series queried through PromQL.

## Current Profile
The source presents Prometheus as the clearest example of the snapshot perspective. A PromQL expression is evaluated at a particular query time, while a range query repeats instant evaluations across a start time, end time, and step. Range selectors expose preceding samples when an operator such as `rate` needs temporal context.

## Key Characteristics
- Models a metric as a name plus labels identifying a time series.
- Evaluates PromQL primarily against a selected time snapshot.
- Uses range selectors for operations that need samples preceding the current query time.
- Builds range-query results by repeating instant evaluations over a time interval.

## Evidence
- Metric identity: [[eric-fu-dao-di-shi-yao-shi-xu-shu-ju-ku]] gives `cpu_usage{cluster="prod", node="node1"}` as a named labeled series.
- Snapshot semantics: [[eric-fu-dao-di-shi-yao-shi-xu-shu-ju-ku]] describes query time as a parameter evaluated with the PromQL expression.
- Temporal context: [[eric-fu-dao-di-shi-yao-shi-xu-shu-ju-ku]] uses `rate(count_requests[1m])` to illustrate a one-minute lookback.
- Range results: [[eric-fu-dao-di-shi-yao-shi-xu-shu-ju-ku]] explains the range API as repeated instant queries merged into series.

## Qualifications
The source values PromQL's simplicity but argues that some cross-time expressions require difficult or inefficient subqueries. It is a conceptual comparison, not a current performance benchmark or complete Prometheus operations guide.

## What Changed
- Established Prometheus as the snapshot-oriented reference case in the time-series data model.

## Relationships
- [[TimeSeriesDatabase]] - Prometheus closely fits the source's name-label-series definition.
- [[InfluxDB]] - contrasted as a more vector-oriented query design.
- [[EricFu]] - author using Prometheus to explain snapshot semantics.
- [[AggregationTheory]] - PromQL applies aggregation within snapshots and across selected time ranges.

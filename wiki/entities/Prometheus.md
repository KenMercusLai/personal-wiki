---
title: "Prometheus"
type: entity
tags: [database, monitoring, time-series, open-source]
sources:
  - eric-fu-dao-di-shi-yao-shi-xu-shu-ju-ku
  - health-checks-and-graceful-degradation-in-distributed-systems
last_updated: 2026-09-29
knowledge_schema: synthesis-v1
---

## Overview
[[Prometheus]] is an open-source monitoring and time-series system whose metrics are named, labeled series queried through PromQL.

## Current Profile
The time-series source presents Prometheus as the clearest example of the snapshot perspective. A PromQL expression is evaluated at a particular query time, while a range query repeats instant evaluations across a start time, end time, and step. Range selectors expose preceding samples when an operator such as `rate` needs temporal context. The Imgix source adds an operational case: Spillway broker queue depth was monitored closely and alerted when it crossed a threshold, using backlog as evidence that adaptive routing and admission were approaching their limits.

## Key Characteristics
- Models a metric as a name plus labels identifying a time series.
- Evaluates PromQL primarily against a selected time snapshot.
- Uses range selectors for operations that need samples preceding the current query time.
- Builds range-query results by repeating instant evaluations over a time interval.
- Supports operational monitoring and alerting on queue saturation signals.

## Evidence
- Metric identity: [[eric-fu-dao-di-shi-yao-shi-xu-shu-ju-ku]] gives `cpu_usage{cluster="prod", node="node1"}` as a named labeled series.
- Snapshot semantics: [[eric-fu-dao-di-shi-yao-shi-xu-shu-ju-ku]] describes query time as a parameter evaluated with the PromQL expression.
- Temporal context: [[eric-fu-dao-di-shi-yao-shi-xu-shu-ju-ku]] uses `rate(count_requests[1m])` to illustrate a one-minute lookback.
- Range results: [[eric-fu-dao-di-shi-yao-shi-xu-shu-ju-ku]] explains the range API as repeated instant queries merged into series.
- Queue monitoring: [[health-checks-and-graceful-degradation-in-distributed-systems]] says Imgix used Prometheus to monitor and alert on aggregate Spillway broker queue depth.

## Qualifications
The time-series source values PromQL's simplicity but argues that some cross-time expressions require difficult or inefficient subqueries. The queue example is a historical operational anecdote whose archived chart and alert are only tiny thumbnails; it does not specify the threshold, duration, false-positive rate, or measured incident reduction. Neither source is a current performance benchmark or complete Prometheus operations guide.

## What Changed
- Added queue-depth monitoring and alerting as an operational overload-control example.
- Retained Prometheus as the snapshot-oriented reference case in the time-series data model.

## Relationships
- [[TimeSeriesDatabase]] - Prometheus closely fits the source's name-label-series definition.
- [[InfluxDB]] - contrasted as a more vector-oriented query design.
- [[EricFu]] - author using Prometheus to explain snapshot semantics.
- [[AggregationTheory]] - PromQL applies aggregation within snapshots and across selected time ranges.
- [[Spillway]] - broker whose aggregate queue depth was monitored.
- [[AdaptiveBackpressure]] - queue metrics reveal when feedback and admission controls are nearing saturation.

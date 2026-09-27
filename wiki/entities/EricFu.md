---
title: "Eric Fu"
type: entity
tags: [author, database, time-series]
sources:
  - eric-fu-dao-di-shi-yao-shi-xu-shu-ju-ku
last_updated: 2026-09-27
knowledge_schema: synthesis-v1
---

## Overview
[[EricFu]] is represented as a technical author proposing a data-model-centered definition of time-series databases.

## Current Profile
Fu's article treats “time-series database” as an overloaded term and rebuilds the category from timestamp-value vectors, metric names, and labels. He uses geometric diagrams and operator signatures to connect abstract modeling choices with query languages, aggregation behavior, joins, storage layout, and product classification.

## Key Characteristics
- Explains database categories through their data models rather than vendor positioning.
- Uses vector and snapshot perspectives to unify different query-language designs.
- Distinguishes time-axis aggregation from label-axis aggregation at both conceptual and implementation levels.
- Applies the framework critically across six database products.

## Evidence
- Modeling approach: [[eric-fu-dao-di-shi-yao-shi-xu-shu-ju-ku]] derives time-series behavior from timestamp-value pairs identified by names and labels.
- Visual explanation: [[eric-fu-dao-di-shi-yao-shi-xu-shu-ju-ku]] includes diagrams for the model, its two perspectives, and both aggregation axes.
- Product analysis: [[eric-fu-dao-di-shi-yao-shi-xu-shu-ju-ku]] compares Prometheus, InfluxDB, GreptimeDB, TDengine, TimescaleDB, and QuestDB.

## Qualifications
The wiki currently has one article by Fu. Its product taxonomy is an argued definition rather than a consensus standard, and the GreptimeDB performance interpretation is explicitly labeled as a guess.

## What Changed
- Established Fu's profile as a technical author focused on time-series data modeling and database architecture.

## Relationships
- [[TimeSeriesDatabase]] - subject Fu defines through a narrow data-model lens.
- [[Prometheus]] - example used for snapshot-oriented query semantics.
- [[InfluxDB]] - example used for vector-oriented query semantics.
- [[DatabaseConsolidation]] - provides the architectural tradeoff surrounding Fu's preference for specialized fit.

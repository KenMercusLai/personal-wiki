---
title: "Apache DataFusion"
type: entity
tags: [software, query-engine, apache-arrow, database-systems]
sources:
  - p5662-hao-corrected
last_updated: 2026-10-13
knowledge_schema: synthesis-v1
---

## Overview
[[ApacheDataFusion]] is an embeddable analytical query engine represented as the implementation substrate and embedded execution layer for [[LiquidCache]].

## Current Profile
LiquidCache uses DataFusion on both sides of its integration boundary: a compute-side `TableProvider` and optimizer rule replace ordinary Parquet scanning with cache access, while an embedded cache-side engine evaluates pushed filters, projections, and simple aggregations. The paper reports about 22,000 lines in the prototype and a further 5,000 lines contributed upstream across DataFusion, Arrow, and Parquet.

The source also treats query-engine integration as part of format performance. Parquet outperforms similarly compressed ORC in its TPC-H comparison partly because DataFusion has stronger Parquet support, while StringView buffer reuse and decompression-buffer reuse reduce transcoding work.

## Key Characteristics
- Embeddable analytical engine used to execute LiquidCache's pushdown plans.
- Accepts a replaceable table-provider and physical-optimizer integration.
- Uses Arrow representations and Arrow Flight for the cache/compute data path.
- Supplies mature Parquet integration that materially affects measured performance.
- Received upstream engineering changes developed during LiquidCache work.

## Evidence
- Integration: [[p5662-hao-corrected]] describes the `TableProvider`, physical optimizer, embedded cache engine, and internal serialized plan path.
- Implementation: [[p5662-hao-corrected]] reports the prototype and upstream contribution sizes.
- Format interaction: [[p5662-hao-corrected]] attributes part of Parquet's advantage over ORC to stronger engine integration and describes StringView and decompression-buffer reuse.

## Qualifications
The profile reflects DataFusion through one project and does not cover its complete architecture, governance, supported operators, current API, or comparative performance. The paper's internal plan coupling is specifically identified as a limitation that future Substrait support could remove.

## What Changed
- Established DataFusion as LiquidCache's embedded execution and integration layer.
- Added query-engine maturity as a qualification on file-format benchmarks.

## Relationships
- [[LiquidCache]] - prototype built on and embedded within DataFusion.
- [[AndrewLamb]] - coauthor associated with DataFusion and StringView work.
- [[XiangpengHao]] - lead author associated with upstream implementation work.
- [[ApacheParquet]] - deeply integrated durable file format in the evaluated engine.
- [[FilterPushdown]] - optimization executed by the embedded cache-side engine.

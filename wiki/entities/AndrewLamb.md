---
title: "Andrew Lamb"
type: entity
tags: [researcher, software-engineer, database-systems]
sources:
  - p5662-hao-corrected
last_updated: 2026-10-13
knowledge_schema: synthesis-v1
---

## Overview
[[AndrewLamb]] is an InfluxData-affiliated database engineer and researcher represented as a coauthor of the [[LiquidCache]] paper.

## Current Profile
The source associates Lamb with LiquidCache's design and implementation on [[ApacheDataFusion]]. It also cites Hao and Lamb's prior DataFusion writing about StringView, an Arrow string representation whose buffer-reuse design became part of the project's Parquet-reading path.

## Key Characteristics
- Coauthor of the LiquidCache paper.
- Affiliated with InfluxData in the source.
- Connected to Apache DataFusion, Arrow, and Parquet engineering.
- Associated with StringView work used to reduce string-decoding copies.

## Evidence
- Authorship and affiliation: [[p5662-hao-corrected]] lists Lamb as an InfluxData-affiliated coauthor.
- System work: [[p5662-hao-corrected]] describes the DataFusion-based LiquidCache prototype and upstream contributions.
- String representation: [[p5662-hao-corrected]] cites Hao and Lamb's StringView explanations and reports that StringView became DataFusion's default string representation.

## Qualifications
The profile relies on one research paper and its references. It does not establish Lamb's complete employment history, exact division of work, or current role.

## What Changed
- Established Lamb's source-bounded relationship to LiquidCache, DataFusion, and StringView.

## Relationships
- [[LiquidCache]] - coauthored cache system.
- [[XiangpengHao]] - lead author and StringView collaborator cited by the paper.
- [[ApacheDataFusion]] - implementation platform and upstream contribution target.
- [[ApacheParquet]] - durable input format and reader integration boundary.

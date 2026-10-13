---
title: "Xiangpeng Hao"
type: entity
tags: [researcher, database-systems, data-analytics]
sources:
  - p5662-hao-corrected
last_updated: 2026-10-13
knowledge_schema: synthesis-v1
---

## Overview
[[XiangpengHao]] is a University of Wisconsin-Madison researcher represented as the lead author of the [[LiquidCache]] paper.

## Current Profile
In the supplied source, Hao co-designs a pushdown cache and ephemeral columnar representation around the observation that Parquet decoding dominates predicate-evaluation cost. The paper also attributes upstream Apache Arrow, Parquet, and [[ApacheDataFusion]] engineering work, including StringView integration, to the LiquidCache effort.

## Key Characteristics
- Lead author of the LiquidCache system paper.
- Affiliated with the University of Wisconsin-Madison in the source.
- Works at the intersection of analytical databases, caching, columnar encoding, and resource disaggregation.
- Coauthor of implementation work contributed to the Apache data ecosystem.

## Evidence
- Authorship and affiliation: [[p5662-hao-corrected]] lists Hao first and associates him with the University of Wisconsin-Madison.
- Research contribution: [[p5662-hao-corrected]] presents LiquidCache's architecture, Liquid representation, filter-aware decoding, and evaluation.
- Engineering contribution: [[p5662-hao-corrected]] reports roughly 5,000 lines contributed upstream across DataFusion, Arrow, and Parquet.

## Qualifications
This profile is bounded to one paper and its author list. It does not establish Hao's full biography, role allocation among coauthors, current affiliation, or independent production deployment of LiquidCache.

## What Changed
- Established Hao as the lead author associated with LiquidCache and filter-aware cache encoding.

## Relationships
- [[LiquidCache]] - system for which Hao is lead author.
- [[AndrewLamb]] - coauthor and InfluxData-affiliated collaborator.
- [[YiboWu]] - University of Wisconsin-Madison coauthor.
- [[AndreaArpaciDusseau]] - University of Wisconsin-Madison coauthor.
- [[RemziArpaciDusseau]] - University of Wisconsin-Madison coauthor.
- [[ApacheDataFusion]] - implementation substrate and upstream contribution target.

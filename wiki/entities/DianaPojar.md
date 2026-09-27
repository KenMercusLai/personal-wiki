---
title: "Diana Pojar"
type: entity
tags: [author, data-engineering, slack]
sources:
  - data-wrangling-at-slack-several-people-are-coding
last_updated: 2026-09-27
knowledge_schema: synthesis-v1
---

## Overview
[[DianaPojar]] is represented as a coauthor of Slack's 2016 account of building a multi-engine data warehouse and controlling cross-version Parquet compatibility.

## Current Profile
Pojar's source contribution is a first-party engineering explanation rather than a personal biography. With [[RonnieChen]], she connects Slack's workload-specific use of Presto, Hive, and Spark to the less visible operational problem of preserving data meaning across their differing libraries, schemas, and upgrade paths.

## Key Characteristics
- Coauthored the Slack data-platform architecture account.
- Frames data engineering as enabling company-wide, data-informed product decisions.
- Emphasizes system discrepancies, compatibility testing, and schema evolution over isolated code construction.
- Presents owned serialization formats as a way to decouple persisted data from cluster-bundled libraries.

## Evidence
- Authorship and context: [[data-wrangling-at-slack-several-people-are-coding]] identifies Pojar as a coauthor writing from Slack's data-engineering perspective.
- Technical scope: [[data-wrangling-at-slack-several-people-are-coding]] covers ingestion, warehouse access, engine specialization, metadata, schema evolution, and upgrades.
- Operating judgment: [[data-wrangling-at-slack-several-people-are-coding]] concludes that understanding interactions among tools was harder and more consequential than merely writing code.

## Qualifications
The source establishes Pojar's coauthorship and technical perspective but provides no broader career history, individual division of labor, or independent assessment of her contributions.

## What Changed
- Created a source-bounded profile centered on Pojar's coauthorship of Slack's interoperability account.

## Relationships
- [[RonnieChen]] - coauthor of the Slack data-engineering source.
- [[Slack]] - company and system context for the account.
- [[DataFormatInteroperability]] - central engineering problem explained in the source.
- [[ApacheParquet]] - shared format whose implementations motivated Slack's compatibility controls.

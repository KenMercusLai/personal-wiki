---
title: "Todaypuffer"
type: entity
tags: [search, bm25, object-storage, prototype]
sources:
  - wei-shen-me-wo-kan-hao-turbopuffer-cong-personal-agent-shuo-qi
last_updated: 2026-10-27
knowledge_schema: synthesis-v1
---

## Overview
[[Todaypuffer]] is [[ZuoJu]]'s reported prototype of an object-storage-backed search system inspired by [[Turbopuffer]].

## Current Profile
The initial BM25 derivative was one JSON object. At roughly 40,000 MS MARCO documents it had reached about 46 MB, and a 64 MiB write ceiling meant an older 100,000-document snapshot had no persisted BM25 index. Queries then scanned source data, with one reported request taking about 24 seconds and a hybrid-search test driving the machine out of memory.

The redesign partitions term postings across 256 buckets addressed by a manifest. For the same reported 100,000-document material, the result was 257 objects totaling about 60 MB; queries fetched relevant buckets, selected candidates, and then read committed source records, returning warm BM25 to tens-of-milliseconds latency. The design remains an intermediate prototype because it decodes entire buckets, lacks block-level skipping and fine range reads, and rebuilds a derivative for each namespace head.

## Key Characteristics
- Keeps committed source records separate from derived search indexes.
- Uses a manifest plus 256 postings buckets instead of one monolithic BM25 JSON object.
- Fetches only buckets associated with query terms before resolving candidate source records.
- Exposes index-build CPU, object writes, cache size, and remote-read granularity as coupled costs.
- Remains a prototype without demonstrated production multi-tenant scale or complete latency and recall evaluation.

## Evidence
Initial failure mode:
- [[wei-shen-me-wo-kan-hao-turbopuffer-cong-personal-agent-shuo-qi]] reports the 46 MB index at 40,000 documents, the 64 MiB persistence ceiling, the 24-second scan, and an OOM during hybrid testing.

Bucketed redesign:
- [[wei-shen-me-wo-kan-hao-turbopuffer-cong-personal-agent-shuo-qi]] reports 256 postings buckets plus a manifest, 257 objects totaling about 60 MB at 100,000 documents, and warm BM25 in the tens of milliseconds.

## Qualifications
All measurements are first-person and source-scoped. The article does not provide code, hardware, repetitions, latency distributions, recall targets, cold-query measurements, object-store pricing, concurrent-tenant tests, or a controlled baseline. The author explicitly identifies whole-bucket decoding, missing block skipping, coarse reads, and repeated derivative construction as unresolved limitations.

## What Changed
- Established the monolithic-index failure and bucketed-postings redesign.
- Preserved the reported performance recovery separately from unresolved production-scale costs.

## Relationships
- [[ZuoJu]] - author and reported builder of the prototype.
- [[Turbopuffer]] - architectural inspiration and comparison point.
- [[BM25]] - lexical ranking method implemented by the derived index.
- [[ObjectStorageNativeDatabase]] - related physical-design problem around remote requests, bytes, manifests, and caching.
- [[PersonalAgentRetrieval]] - workload family the prototype is intended to explore.

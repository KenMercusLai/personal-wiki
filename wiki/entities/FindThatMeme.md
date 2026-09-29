---
title: "FindThatMeme"
type: entity
tags: [project, search-engine, memes, ocr]
sources:
  - image-stacks-and-iphone-racks-building-an-internet-scale-meme-search-engine
last_updated: 2026-09-29
knowledge_schema: synthesis-v1
---

## Overview
[[FindThatMeme]] is a side-project search engine that indexes text from meme images and videos so users can retrieve a remembered meme by its words instead of manually scrolling through saved media.

## Current Profile
The 2023 account presents FindThatMeme as an end-to-end ingestion and retrieval system. Scrapers collect media from meme sites; images go to an iPhone OCR farm, while videos first become ten evenly spaced frames; files live in a Linode S3-compatible bucket; [[PostgreSQL]] holds authoritative text and metadata; PGSync projects searchable fields into a single-node Elasticsearch cluster; and an API or app serves search. The author reports indexing and searching about 17 million memes with sub-second queries on a shared six-core, 16 GB RAM host, but provides no reproducible benchmark or independent traffic, coverage, availability, or quality evidence.

## Key Characteristics
- Makes text embedded in highly varied meme images searchable through Apple's on-device Vision OCR.
- Extends the image path to videos by sampling ten frames with ffmpeg and OCRing each frame.
- Keeps authoritative records in PostgreSQL while treating Elasticsearch as a rebuildable search projection.
- Uses a low-cost cluster of impaired secondhand iPhones behind Raspberry Pi and NGINX load balancing.
- Accepts operational compromises—single-node search and restart-based phone recovery—to keep a personal project affordable.
- Reports a corpus of roughly 17 million memes and sub-second text queries on modest shared hardware without publishing benchmark methodology.

## Evidence
- Retrieval problem and scope: [[image-stacks-and-iphone-racks-building-an-internet-scale-meme-search-engine]] says the project began because niche memes were difficult to find mid-conversation by scrolling through a phone.
- OCR path: [[image-stacks-and-iphone-racks-building-an-internet-scale-meme-search-engine]] contrasts Tesseract failures with successful iOS recognition of distorted text and describes a Swift HTTP service around Vision.
- Video ingestion: [[image-stacks-and-iphone-racks-building-an-internet-scale-meme-search-engine]] describes ffmpeg extraction of ten evenly spaced frames followed by OCR of every frame.
- Data architecture: [[image-stacks-and-iphone-racks-building-an-internet-scale-meme-search-engine]] makes PostgreSQL canonical and uses PGSync plus Redis to populate a replaceable Elasticsearch index.
- Physical cluster: [[image-stacks-and-iphone-racks-building-an-internet-scale-meme-search-engine]] shows five wired iPhones and a Raspberry Pi and describes NGINX distributing OCR requests across the phones.
- Reported scale: [[image-stacks-and-iphone-racks-building-an-internet-scale-meme-search-engine]] claims around 17 million indexed memes and searches under one second on six cores and 16 GB of RAM.

## Qualifications
The corpus contains one founder-written architecture post, not an independent audit or current service profile. It does not measure search relevance, OCR precision and recall, duplicate handling, coverage, end-to-end ingestion throughput, p95/p99 latency, availability, security, moderation, or total ownership cost. Sampling ten video frames cannot capture every caption or audio cue, and carrier-locked or blocklisted devices may carry provenance, maintenance, lifecycle, and platform-policy risks that a purchase-price comparison does not resolve.

## What Changed
- Created the project profile from the 2023 architecture account.
- Recorded the separation among scraping, media storage, OCR, canonical data, derived search data, and query serving.
- Preserved the distinction between reported scale and reproducible performance evidence.

## Relationships
- [[VisualTextIndexing]] - FindThatMeme turns image and sampled-video text into a searchable corpus.
- [[CostConstrainedInfrastructure]] - its physical phone farm and single-node search cluster prioritize sustainable cost.
- [[RebuildableDerivedIndex]] - its Elasticsearch state can be regenerated from PostgreSQL through PGSync.
- [[PostgreSQL]] - authoritative store for meme text and structured context.
- [[SystemReliability]] - restart recovery and index reconstruction bound failures without providing full redundancy.
- [[Apple]] - iOS Vision and Guided Access enable the OCR workers and crash recovery.

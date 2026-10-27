---
title: "ByteDance"
type: entity
tags: [company, machine-learning, data-infrastructure]
sources:
  - magnus-p4964-song
last_updated: 2026-10-27
knowledge_schema: synthesis-v1
---

## Overview
[[ByteDance]] is represented here as the company that developed and deployed [[Magnus]] for large-scale search, recommendation, advertising, multimodal, and feature-engineering workloads.

## Current Profile
The source describes ByteDance's offline training data as EB-scale with PB-scale daily growth and presents its environment as spanning conventional ML, large recommendation models, and large multimodal models. Its internal data stack connects distributed storage to Flink, Spark, Ray, Krypton, Primus, and BytedStreaming through Magnus tables and services.

This is a narrow infrastructure profile, not a general account of the company's products, organization, finances, governance, or wider technical stack.

## Key Characteristics
- Operates source-reported EB-scale offline ML training data with PB-scale daily growth.
- Uses heterogeneous ingestion, engineering, analytics, and training engines.
- Develops internal storage formats and native readers for wide-table and multimodal workloads.
- Organizes production recommendation and multimodal training around specialized data layouts and planners.

## Evidence
- Scale and workload: [[magnus-p4964-song]] reports offline training-data volume and the mix of search, recommendation, advertising, LRM, and LMM use cases.
- Systems stack: [[magnus-p4964-song]] maps Magnus to ByteDance's storage, table services, compute engines, and training frameworks.
- Production deployment: [[magnus-p4964-song]] says Magnus has operated internally for more than five years and supplies production benchmark cases.

## Qualifications
All claims come from one company-authored systems paper and should be read as source-reported. The paper does not independently audit ByteDance's scale, costs, operational reliability, or business outcomes, and its selected workloads do not characterize every team or data system at the company.

## What Changed
- Created a source-bounded company profile focused on ByteDance's ML data infrastructure.

## Relationships
- [[Magnus]] - internal data-management system developed and deployed by ByteDance.
- [[ApacheIceberg]] - open table foundation adapted for the company's ML workloads.
- [[MachineLearningDataManagement]] - infrastructure domain represented by the source.
- [[MultimodalDataPipelines]] - one workload family supported by ByteDance's storage and planning stack.

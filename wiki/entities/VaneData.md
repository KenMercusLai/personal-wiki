---
title: "Vane Data"
type: entity
tags: [data-processing, distributed-computing, ai]
sources:
  - vane-data-jev-building-an-end-to-end-voice-analytics-pipeline
last_updated: 2026-10-07
knowledge_schema: synthesis-v1
---

## Overview
[[VaneData]] is a data-processing framework presented as organizing heterogeneous local and external computation into one deferred Relation query plan.

## Current Profile
In the banking example, Vane Data connects Parquet input, CPU audio tasks, a persistent GPU transcription actor, transcript checks, external [[Jev]] actors, SQL field shaping, and file output without intermediate materialization. Its value in this source is orchestration and row lineage: resource needs are declared at the operator boundary, failed records remain present, and model responses return to the originating rows for later SQL and evaluation.

## Key Characteristics
- Uses Relation as a table-like deferred-computation abstraction between operators.
- Schedules ordinary functions as tasks and reusable callable classes or Jev executors as actors, by default on Ray.
- Declares batch schemas and CPU, GPU, actor-count, and concurrency requirements at pipeline stages.
- Preserves failed rows and error fields so downstream outputs and evaluations retain the selected population.
- Integrates typed external judgments into the same data plan used for deterministic preparation and SQL shaping.

## Evidence
- Plan composition: [[vane-data-jev-building-an-end-to-end-voice-analytics-pipeline]] chains decode, transcription, checks, judgment, SQL, and output through one Relation.
- Resource roles: [[vane-data-jev-building-an-end-to-end-voice-analytics-pipeline]] assigns stateless decoding to CPU tasks, model reuse to a GPU actor, and external-call coordination to Jev actors.
- Failure visibility: [[vane-data-jev-building-an-end-to-end-voice-analytics-pipeline]] keeps decode and transcript failures in the result set and evaluation denominator.
- External integration: [[vane-data-jev-building-an-end-to-end-voice-analytics-pipeline]] writes validated Jev responses back as a column aligned with the input rows.

## Qualifications
The source demonstrates one example rather than benchmarking Vane Data against other orchestration systems. It reports no pipeline throughput, scheduling overhead, retry behavior under failure, scaling curve, production deployment, or cost, and its Jev integration is described as a development build from TestPyPI.

## What Changed
- Created the initial profile around Vane Data's deferred Relation plan, heterogeneous resource scheduling, row alignment, and failure preservation.

## Relationships
- [[Jev]] - Vane Data exposes Jev judgment as an operator inside a Relation plan.
- [[VoiceAnalyticsPipeline]] - Vane Data orchestrates the pipeline's deterministic, GPU, external, and SQL stages.
- [[TextClassification]] - Vane Data carries transcript rows into intent classification and evaluation.
- [[SQLFirstBusinessAutomation]] - SQL remains the transparent field-shaping and rule layer after semantic judgment.

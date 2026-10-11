---
title: "Vane Data"
type: entity
tags: [data-processing, distributed-computing, ai]
sources:
  - vane-data-jev-building-an-end-to-end-voice-analytics-pipeline
  - chong-xin-chu-fa-xiang-wei-zhi-hang-xing
last_updated: 2026-10-11
knowledge_schema: synthesis-v1
---

## Overview
[[VaneData]] is a data-processing framework presented as organizing heterogeneous local and external computation into one deferred Relation query plan and, in a later founder announcement, as the data component of [[AstroVela]]'s [[Vane]] product family.

## Current Profile
In the banking example, Vane Data connects Parquet input, CPU audio tasks, a persistent GPU transcription actor, transcript checks, external [[Jev]] actors, SQL field shaping, and file output without intermediate materialization. Its evidenced technical value is orchestration and row lineage: resource needs are declared at the operator boundary, failed records remain present, and model responses return to the originating rows for later SQL and evaluation.

The later AstroVela announcement places Vane Data beside Vane Core, Vane RL, and Vane Agent and says it was planned for open source in July 2026. That adds company and roadmap context, not evidence that the release occurred or that the four components form a shipped integrated architecture.

## Key Characteristics
- Uses Relation as a table-like deferred-computation abstraction between operators.
- Schedules ordinary functions as tasks and reusable callable classes or Jev executors as actors, by default on Ray.
- Declares batch schemas and CPU, GPU, actor-count, and concurrency requirements at pipeline stages.
- Preserves failed rows and error fields so downstream outputs and evaluations retain the selected population.
- Integrates typed external judgments into the same data plan used for deterministic preparation and SQL shaping.
- Occupies the data role in the announced four-part Vane product family.

## Evidence
- Plan composition: [[vane-data-jev-building-an-end-to-end-voice-analytics-pipeline]] chains decode, transcription, checks, judgment, SQL, and output through one Relation.
- Resource roles: [[vane-data-jev-building-an-end-to-end-voice-analytics-pipeline]] assigns stateless decoding to CPU tasks, model reuse to a GPU actor, and external-call coordination to Jev actors.
- Failure visibility: [[vane-data-jev-building-an-end-to-end-voice-analytics-pipeline]] keeps decode and transcript failures in the result set and evaluation denominator.
- External integration: [[vane-data-jev-building-an-end-to-end-voice-analytics-pipeline]] writes validated Jev responses back as a column aligned with the input rows.
- Product context: [[chong-xin-chu-fa-xiang-wei-zhi-hang-xing]] names Vane Data as one of four [[Vane]] components and states a July 2026 open-source plan.

## Qualifications
The banking source demonstrates one example rather than benchmarking Vane Data against other orchestration systems. It reports no pipeline throughput, scheduling overhead, retry behavior under failure, scaling curve, production deployment, or cost, and its Jev integration is described as a development build from TestPyPI. The founder essay is a product announcement: its planned July 2026 open-source date is not confirmation of a release, and it provides no interface or integration detail for the rest of Vane.

## What Changed
- Added AstroVela ownership, Vane product-family placement, and the explicitly unverified open-source roadmap.

## Relationships
- [[Jev]] - Vane Data exposes Jev judgment as an operator inside a Relation plan.
- [[VoiceAnalyticsPipeline]] - Vane Data orchestrates the pipeline's deterministic, GPU, external, and SQL stages.
- [[TextClassification]] - Vane Data carries transcript rows into intent classification and evaluation.
- [[SQLFirstBusinessAutomation]] - SQL remains the transparent field-shaping and rule layer after semantic judgment.
- [[Vane]] - umbrella product family in which Vane Data supplies the announced data component.
- [[AstroVela]] - company positioning Vane Data as part of its multimodal and Physical AI infrastructure bet.

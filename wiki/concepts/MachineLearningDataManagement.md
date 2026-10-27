---
title: "Machine Learning Data Management"
type: concept
tags: [machine-learning, data-management, data-lake, training-infrastructure]
sources:
  - magnus-p4964-song
last_updated: 2026-10-27
knowledge_schema: synthesis-v1
---

## Definition
[[MachineLearningDataManagement]] is the coordinated storage, indexing, versioning, mutation, planning, governance, and delivery of datasets used in feature engineering and model training.

## Current Synthesis
At large scale, managing training data is not reducible to choosing a file format or object store. Wide feature tables amplify footer and manifest costs; multimodal records combine compact metadata with very large binary values; iterative feature work requires isolated but reconcilable versions; delayed labels and annotations require partial updates; and training frameworks need stable, balanced shards rather than raw file paths.

The Magnus case shows one vertically integrated response. Table metadata provides snapshots and lifecycle boundaries, workload-specific formats reduce wide-table or media access costs, primary-key and search indexes support mutation and retrieval, merge-on-read shifts work from writes toward controlled reads, and engine integration turns metadata into executable training tasks. The design also shows that logical correctness and physical efficiency remain coupled: sequence ordering defines conflict outcomes, compaction bounds read degradation, layout determines pruning value, and shard granularity determines worker memory.

## Key Claims
- Training-data infrastructure must coordinate table metadata, physical format, indexing, mutation, and execution rather than optimize each independently.
- Wide tables and large binary values create different metadata, memory, and read-amplification problems.
- Merge-on-read can make frequent partial updates cheap only if readers, ordering rules, and compaction control accumulated complexity.
- Reproducible experimentation benefits from immutable snapshot tags and isolated branches, while integration requires explicit merge and rebase semantics.
- Training throughput depends on data organization and planning granularity as well as model-side computation.

## Evidence
- Integrated architecture: [[magnus-p4964-song]] connects storage, table metadata, indexes, services, engines, and training scenarios in one system.
- Workload-shaped layout: [[magnus-p4964-song]] uses Krypton for wide tables, Blob references for media, and Main-Extra tables for repeated recommendation sequences.
- Mutation control: [[magnus-p4964-song]] combines position and equality deltas, bucketed primary keys, sequence precedence, native MOR, and compaction.
- Experimentation and planning: [[magnus-p4964-song]] adds manifest indexes, branches, tags, merge, rebase, row-range tasks, and compressed plan objects.
- Outcome evidence: [[magnus-p4964-song]] reports production improvements in storage, planning, write cost, memory, startup time, and training throughput.

## Counterevidence & Qualifications
The synthesis currently rests on one first-party ByteDance system and may overrepresent workloads with extremely wide tables, high mutation rates, or proprietary engine integration. Vertical integration can improve cross-layer optimization while increasing implementation burden, lock-in, operational coupling, and interoperability risk. Merge-on-read transfers work to readers and maintenance; branching adds semantic conflict questions; fine-grained sharding increases planning state; and specialized formats require durable reader support. Reported gains do not establish that every ML platform should reproduce the same stack.

## What Changed
- Established a cross-layer model of training-data management from storage through executable model input.
- Added mutation, experimental version control, and planning granularity as first-class design dimensions.

## Related Concepts
- [[OpenTableFormats]] - provide snapshot, schema, manifest, and transaction foundations for managed datasets.
- [[ColumnarStorageTradeoffs]] - governs format and access choices for wide features and large values.
- [[MultimodalDataPipelines]] - consumes media-bearing datasets under heterogeneous resource constraints.
- [[DataPruning]] - converts layout and statistics into avoided planning and scan work.
- [[StoragePerformanceBenchmarking]] - is required to distinguish workload-specific gains from general design claims.
- [[DatabaseEngineeringTradeoffs]] - frames the movement of complexity among writes, reads, metadata, and maintenance.

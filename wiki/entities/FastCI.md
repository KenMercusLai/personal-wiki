---
title: "FastCI"
type: entity
tags: [continuous-integration, software-testing, gpu-infrastructure, llm-training]
sources:
  - 2610.01967
last_updated: 2026-10-13
knowledge_schema: synthesis-v1
---

## Overview
[[FastCI]] is a framework for reducing the latency and GPU cost of continuous integration for LLM training frameworks while retaining evidence that selected tests execute modified code.

## Current Profile
FastCI maintains a sampled function-and-call runtime evidence graph plus test failure history. For each merge request it selects tests linked to changed entities, expands selection when evidence is absent, prunes context-equivalent jobs, prioritizes high-risk failures, and applies reversible workload overrides outside each test's validation purpose.

The source reports deployment in ByteDance's LLM training-framework CI after shadow validation and a staged rollout. On-demand graph materialization and locally derived test configuration replaced early designs that timed out or added persistent-storage traffic.

## Key Characteristics
- Uses sampled function-level runtime evidence rather than relying only on file-path mappings.
- Expands conservatively through class peers and callers when a changed entity is missing from traces.
- Prunes only tests with matching local execution context and validation metadata.
- Orders tests from historical change-linked failure risk and recent instability.
- Reduces out-of-scope workload dimensions and periodically checks reduced jobs against original configurations.
- Supports staged enablement and configuration-only rollback to the existing CI workflow.

## Evidence
Design:
- [[2610.01967]] specifies the runtime graph, missing-evidence expansion, context equivalence, combined risk score, and validation-scope-aware workload overrides.

Evaluation:
- [[2610.01967]] reports shadow-CI comparisons against full CI, path mapping, NameRTS, an LLM baseline, and COLEMAN, including latency, GPU, queueing, coverage-retention, and first-failure metrics.

Deployment:
- [[2610.01967]] describes a four-stage production rollout, 784 observed runs over three weeks, on-demand graph materialization, local configuration derivation, and two rollback levels.

## Qualifications
FastCI is supported by a first-party study of one proprietary framework. Its runtime evidence is incomplete by design, its coverage reference excludes native and module-level execution, and its context and pass/fail equivalence checks do not prove equal semantic fault detection. The reported production period is short, and no independent implementation or cross-framework cost comparison is supplied.

## What Changed
- Established FastCI as a canonical project entity with its four optimization stages, safeguards, and reported deployment evidence.

## Relationships
- [[GPUIntensiveContinuousIntegration]] - problem domain and systems design that FastCI implements.
- [[TianshuoQiao]] - Peking University-affiliated coauthor of the FastCI paper.
- [[NaiqianZheng]] - Peking University-affiliated coauthor.
- [[XiaopengLiu]] - ByteDance Seed-affiliated coauthor.
- [[ShuguangWang]] - ByteDance Seed-affiliated coauthor.
- [[DiandianGu]] - ByteDance Seed-affiliated coauthor.
- [[XuanzheLiu]] - Peking University-affiliated coauthor.
- [[XinJin]] - Peking University-affiliated coauthor.

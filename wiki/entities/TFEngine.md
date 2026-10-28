---
title: "TFEngine"
type: entity
tags: [terraform, infrastructure, cloud, cmdb]
sources:
  - ai-harness-engineering
last_updated: 2026-10-27
knowledge_schema: synthesis-v1
---

## Overview
[[TFEngine]] is [[Zhu327]]'s lightweight Terraform execution engine for CMDB-driven infrastructure lifecycle operations.

## Current Profile
TFEngine accepts HCL templates and execution parameters from a CMDB, generates plans, applies changes, destroys resources, manages state and work directories, controls an execution queue, and returns results plus streaming logs. Operations staff maintain the resource templates, while ordinary users request resources through forms and can see the underlying Terraform plan and apply output.

In the retained architecture, TFEngine owns declarative create, update, and delete operations and does not call [[CloudKitService|CloudKit]] directly. The CMDB separately invokes CloudKit for imperative Day 2 actions. Both paths share identity, account, role, and credential controls.

## Key Characteristics
- Wraps Terraform plan, apply, and destroy operations behind a CMDB-facing execution boundary.
- Parses and renders HCL while managing state, queues, concurrency, work directories, and streaming logs.
- Keeps infrastructure templates under operations-team ownership and presents them to end users as forms.
- Exposes execution details so operators can diagnose failed requests without routing every failure through application developers.
- Separates declarative lifecycle work from provider-SDK Day 2 operations.

## Evidence
- Product workflow: [[ai-harness-engineering]] says operations staff maintain HCL templates while users request resources through platform forms and receive Terraform logs.
- Engine responsibilities: [[ai-harness-engineering]] and its architecture diagram show plan, apply, destroy, HCL rendering, state, queue, concurrency, working-directory, and log components.
- System boundary: [[ai-harness-engineering]] shows the CMDB calling TFEngine for IaC lifecycle work and CloudKit separately for Day 2 operations.

## Qualifications
The source is a creator-authored architecture account. It supplies no released-version boundary, benchmark, state-backend detail, locking and failure semantics, security review, provider test matrix, adoption measure, or comparison with direct Terraform orchestration and other execution engines.

## What Changed
- Created the initial profile of TFEngine and its CMDB, Terraform, and CloudKit boundaries.

## Relationships
- [[Zhu327]] - reported developer of TFEngine.
- [[Terraform]] - core provisioning engine and SDK beneath TFEngine.
- [[InfrastructureAsCode]] - lifecycle model implemented through HCL templates and Terraform execution.
- [[MultiCloudLifecycleManagement]] - TFEngine owns the declarative half of the split architecture.
- [[CloudKitService]] - sibling service for imperative Day 2 operations, invoked separately by the CMDB.

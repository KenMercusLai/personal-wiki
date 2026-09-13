---
title: "Papermill"
type: entity
tags: [open-source, notebooks, workflow]
sources:
  - beyond-interactive-notebook-innovation-at-netflix-netflix-techblog-medium
last_updated: 2026-09-14
knowledge_schema: synthesis-v1
---

## Overview
[[Papermill]] is the notebook parameterization, execution, and analysis library used in Netflix's notebook infrastructure.

## Current Profile
The Netflix source presents Papermill as the bridge between a notebook as an interactive document and a notebook as a reusable execution unit. Users can define parameters, run notebooks with different parameter sets, execute them concurrently, and collect metrics from executed notebooks.

In Netflix's broader architecture, that makes notebooks useful as templates and scheduled workflows. A data scientist can vary experiment coefficients, a data engineer can run audit collections, and an engineer can send troubleshooting output without rewriting the notebook as a separate script.

## Key Characteristics
- Parameterizes notebooks so input values can be supplied at runtime.
- Executes notebooks as repeatable artifacts.
- Can run multiple notebooks with different parameter sets.
- Can collect and summarize metrics from executed notebooks.
- Supports notebook templates and scheduled execution patterns.

## Evidence
- Library role: [[beyond-interactive-notebook-innovation-at-netflix-netflix-techblog-medium]] defines Papermill as a library for parameterizing, executing, and analyzing Jupyter notebooks.
- Concurrent execution: [[beyond-interactive-notebook-innovation-at-netflix-netflix-techblog-medium]] says Papermill can spawn multiple notebooks with different parameter sets and execute them concurrently.
- Metrics role: [[beyond-interactive-notebook-innovation-at-netflix-netflix-techblog-medium]] says Papermill can collect and summarize notebook metrics.
- Template use: [[beyond-interactive-notebook-innovation-at-netflix-netflix-techblog-medium]] describes reusable notebook templates for experiments, audits, stakeholder exploration, and troubleshooting scripts.

## Qualifications
This page captures Papermill through Netflix's 2018 platform narrative. It does not document the current API, installation, maintenance status, or non-Netflix usage patterns.

## What Changed
- Created the entity profile for Papermill as Netflix's notebook execution and parameterization layer.

## Relationships
- [[Jupyter]] - Papermill operates on Jupyter notebooks.
- [[NotebookWorkflowInfrastructure]] - Papermill turns notebooks into parameterized executable artifacts.
- [[Nteract]] - both are part of the nteract-adjacent notebook ecosystem used by Netflix.
- [[DeploymentAutomation]] - scheduled notebook execution resembles an operationalized recurring workflow.

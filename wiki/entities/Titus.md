---
title: "Titus"
type: entity
tags: [containers, cloud, netflix, infrastructure]
sources:
  - beyond-interactive-notebook-innovation-at-netflix-netflix-techblog-medium
last_updated: 2026-09-14
knowledge_schema: synthesis-v1
---

## Overview
[[Titus]] is Netflix's container management platform used in the notebook source to run data-platform jobs and notebook servers on scalable cloud infrastructure.

## Current Profile
The Netflix source presents Titus as the compute substrate behind notebooks. When a user launches a notebook server, Netflix provisions a container, applies default or requested resources, supplies a prepared image with common libraries and kernels, and includes security groups, roles, and identity-oriented environment variables.

For the notebook platform, Titus hides much of the AWS container-management complexity from data users. It lets users focus on analysis and workflow while the platform manages execution environments, resource defaults, and integration with Netflix's broader data platform.

## Key Characteristics
- Provides scalable and reliable container execution in Netflix's AWS environment.
- Runs notebook servers and other data-platform jobs in containers.
- Supports prepared notebook images with common libraries and default kernels.
- Lets users request more compute resources when defaults are insufficient.
- Carries user security groups, roles, and identity-related environment variables into notebook environments.

## Evidence
- Platform role: [[beyond-interactive-notebook-innovation-at-netflix-netflix-techblog-medium]] defines Titus as Netflix's container management platform for scalable, reliable container execution and AWS integration.
- Notebook launch: [[beyond-interactive-notebook-innovation-at-netflix-netflix-techblog-medium]] says a container is provisioned when a user launches a notebook server.
- Resource defaults: [[beyond-interactive-notebook-innovation-at-netflix-netflix-techblog-medium]] says default resources work for most execution patterns and users can request more through a simple interface.
- Environment defaults: [[beyond-interactive-notebook-innovation-at-netflix-netflix-techblog-medium]] says the prepared image includes common libraries, default kernels, security groups, roles, and environment variables.
- Abstraction goal: [[beyond-interactive-notebook-innovation-at-netflix-netflix-techblog-medium]] says Netflix wanted to abstract away compute-management complexity.

## Qualifications
This page summarizes Titus only through the notebook article. It does not describe Titus's full architecture, later open-source evolution, scheduler internals, or non-notebook production workloads.

## What Changed
- Created the entity profile for Titus as Netflix's notebook compute substrate.

## Relationships
- [[Netflix]] - Titus is an internal Netflix platform.
- [[NotebookWorkflowInfrastructure]] - Titus supplies the container compute layer.
- [[AWS]] - Titus integrates with Netflix's AWS-based cloud environment in the source.
- [[InternalDeveloperPlatform]] - Titus hides infrastructure complexity behind a managed execution layer.

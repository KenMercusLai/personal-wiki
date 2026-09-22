---
title: "Dan McKinley"
type: entity
tags: [software-engineering, deployment, reliability]
sources:
  - you-cant-have-a-rollback-button-skyliner
last_updated: 2026-09-23
knowledge_schema: synthesis-v1
---

## Overview
[[DanMcKinley]] is the software practitioner identified as the author of the Skyliner article "You Can't Have a Rollback Button."

## Current Profile
In the source represented here, McKinley argues from a systems view of web deployment: application code cannot be isolated from databases, caches, browsers, and concurrently running copies. His operational advice replaces confidence in a universal rollback control with small deployments, gradual exposure, feature off switches, and forward repair of the system's actual current state.

## Key Characteristics
- Treats running applications as evolving distributed state rather than self-contained reversible versions.
- Challenges deployment controls that promise more recovery certainty than their system boundary permits.
- Prefers small, staged, disableable releases and verifiable forward corrections.

## Evidence
- Systems model: [[you-cant-have-a-rollback-button-skyliner]] says deployed code changes the databases, caches, browsers, and concurrent instances around it.
- Rollback critique: [[you-cant-have-a-rollback-button-skyliner]] argues that restoring a server SHA does not reverse those external effects.
- Deployment guidance: [[you-cant-have-a-rollback-button-skyliner]] recommends dark code, gradual ramp-up, off switches, and small roll-forward corrections.

## Qualifications
This profile is based on one short 2017 practitioner essay. It does not establish McKinley's broader career, all of his deployment views, or comparative evidence that the recommended controls outperform rollback in every architecture.

## What Changed
- Created the profile from McKinley's rollback critique and forward-remediation guidance.

## Relationships
- [[ChangeSafety]] - McKinley's central subject is recovery from harmful production changes.
- [[DeploymentAutomation]] - he warns that an automated code-reversion control does not reverse whole-system state.
- [[ContinuousDelivery]] - he recommends small staged releases with activation and shutdown controls.

---
title: "Russ White"
type: entity
tags: [network-engineering, incident-learning, technical-writing]
sources:
  - rule-11-reader-learning-from-the-post-mortem
last_updated: 2026-10-02
knowledge_schema: synthesis-v1
---

## Overview
[[RussWhite]] is a network engineer and Rule 11 Reader author represented here through a systems-oriented method for learning from network incidents.

## Current Profile
White draws on three decades of network-engineering experience to argue that postmortems in the field are uncommon or ineffective when they narrow too quickly to configuration errors, vendor defects, or individual innocence. His proposed alternative maps the setup, detection, and troubleshooting workflows around a failure, using the resulting record to change deployment conditions, improve telemetry, and make future diagnosis faster.

## Key Characteristics
- Treats network failures as products of organizational and technical workflows rather than isolated configuration mistakes.
- Emphasizes detection dwell time, false-positive trade-offs, and missing instrumentation as post-incident learning targets.
- Advocates recording diagnostic choices, methods, and findings in a reusable troubleshooting flowchart.

## Evidence
- Systems perspective: [[rule-11-reader-learning-from-the-post-mortem]] argues that appliance and configuration detail can crowd out analysis of organizational process and political commitments.
- Detection perspective: [[rule-11-reader-learning-from-the-post-mortem]] proposes reconstructing where detection could have occurred sooner while accounting for false-positive collateral damage.
- Diagnostic practice: [[rule-11-reader-learning-from-the-post-mortem]] recommends recording each troubleshooting check, its rationale, method, and result for later analysis.

## Qualifications
The profile is bounded to one short 2020 practitioner essay. Its claims about postmortem rarity and ineffectiveness come from personal experience rather than a systematic survey, and the proposed workflow method is not evaluated against incident outcomes.

## What Changed
- Established White's profile through his three-workflow approach to network postmortems.

## Relationships
- [[BlamelessPostmortem]] - White proposes a workflow-mapping method intended to turn incident review into system learning.
- [[IncidentManagement]] - White treats recorded troubleshooting decisions as reusable response knowledge.
- [[ServiceObservability]] - White connects detection reconstruction to lower dwell time and better instrumentation.

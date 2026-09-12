---
title: "Netflix Conductor"
type: entity
tags: [workflow, orchestration, infrastructure]
sources:
  - wei-shen-me-xian-you-de-agent-infra-wu-fa-zhi-cheng-sheng-chan-ji-ying-yong
last_updated: 2026-09-12
knowledge_schema: synthesis-v1
---

## Overview
[[NetflixConductor]] is a workflow orchestration system discussed in the source alongside [[Temporal]] as useful durable execution infrastructure that does not replace agent-specific semantic primitives.

## Current Profile
The article groups Netflix Conductor with Temporal as an orchestrator that can provide workflow history, recovery, and retry in conventional microservice settings. For agents, the source says orchestration can organize higher-level processes only after side-effect semantics and capability boundaries have been established elsewhere.

## Key Characteristics
- Represents durable workflow orchestration in the source's comparison.
- Helps organize tasks under conventional workflow assumptions.
- Does not solve untrusted LLM output or capability isolation.
- Can sit above effect logs and capability gateways but not replace them.

## Evidence
- Category role: [[wei-shen-me-xian-you-de-agent-infra-wu-fa-zhi-cheng-sheng-chan-ji-ying-yong]] mentions Conductor with Temporal as solving durable execution under different assumptions.
- Layering claim: [[wei-shen-me-xian-you-de-agent-infra-wu-fa-zhi-cheng-sheng-chan-ji-ying-yong]] says orchestration can sit above semantic primitives but cannot be the semantic foundation.
- Trust boundary gap: [[wei-shen-me-xian-you-de-agent-infra-wu-fa-zhi-cheng-sheng-chan-ji-ying-yong]] argues workflow systems do not protect against prompt-injected agent logic.

## Qualifications
The source gives fewer details about Netflix Conductor than Temporal. This page therefore captures its role as a comparison point rather than an independent technical evaluation.

## What Changed
- Created the entity page for Netflix Conductor.

## Relationships
- [[Temporal]] - both are workflow orchestrators contrasted with agent-specific recovery needs.
- [[ProductionAgentInfrastructure]] - Conductor may organize workflows above semantic agent primitives.
- [[SemanticIsolation]] - Conductor does not provide the capability trust boundary described by the source.

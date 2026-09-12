---
title: "Modal"
type: entity
tags: [infrastructure, code-execution, ai]
sources:
  - wei-shen-me-xian-you-de-agent-infra-wu-fa-zhi-cheng-sheng-chan-ji-ying-yong
last_updated: 2026-09-12
knowledge_schema: synthesis-v1
---

## Overview
[[Modal]] is a Python-native execution platform discussed in the source as reducing deployment friction without solving production-agent capability isolation or recovery semantics.

## Current Profile
The article treats Modal as useful at the code-execution sandbox or runtime layer. Its limitation for agents is that a clean execution environment still allows the agent to call external services if raw credentials are available, and it does not automatically provide effect logging, idempotent replay, or irreversible-operation handling.

## Key Characteristics
- Provides Python-native execution infrastructure.
- Reduces deployment and runtime friction.
- Addresses code execution rather than capability isolation.
- Does not by itself provide agent side-effect recovery.

## Evidence
- Platform role: [[wei-shen-me-xian-you-de-agent-infra-wu-fa-zhi-cheng-sheng-chan-ji-ying-yong]] says Modal's Python-native execution environment reduces deployment friction.
- Boundary distinction: [[wei-shen-me-xian-you-de-agent-infra-wu-fa-zhi-cheng-sheng-chan-ji-ying-yong]] separates code isolation from capability isolation.
- Recovery gap: [[wei-shen-me-xian-you-de-agent-infra-wu-fa-zhi-cheng-sheng-chan-ji-ying-yong]] says crash recovery, side-effect records, and idempotent replay still need application-layer implementation.

## Qualifications
The source does not compare Modal features comprehensively; it only addresses the mismatch between code-execution infrastructure and production-agent semantics.

## What Changed
- Created the entity page for Modal.

## Relationships
- [[SemanticIsolation]] - Modal is discussed as code-execution infrastructure rather than semantic isolation.
- [[ProductionAgentInfrastructure]] - Modal may be a runtime layer beneath agent-specific primitives.
- [[EffectLog]] - effect logs cover recovery behavior Modal does not provide by itself.

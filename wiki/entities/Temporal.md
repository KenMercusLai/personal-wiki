---
title: "Temporal"
type: entity
tags: [workflow, orchestration, infrastructure]
sources:
  - wei-shen-me-xian-you-de-agent-infra-wu-fa-zhi-cheng-sheng-chan-ji-ying-yong
last_updated: 2026-09-12
knowledge_schema: synthesis-v1
---

## Overview
[[Temporal]] is a durable workflow system discussed in the source as useful for deterministic orchestration but insufficient as the semantic base for nondeterministic, untrusted LLM agents.

## Current Profile
The article says Temporal provides durable workflow history, recovery, and idempotent retry in microservice orchestration. Its core mismatch with LLM agents is that Temporal relies on deterministic, trusted workflow code, while agents make probabilistic decisions and may act on maliciously injected instructions.

## Key Characteristics
- Provides durable workflow execution and history.
- Depends on deterministic workflow replay semantics.
- Assumes workflow logic is trusted, while infrastructure failures are the main fault source.
- Can orchestrate above agent primitives but cannot replace effect logs and capability isolation.
- LLM calls need cached outputs during replay to avoid divergent decisions.

## Evidence
- Workflow value: [[wei-shen-me-xian-you-de-agent-infra-wu-fa-zhi-cheng-sheng-chan-ji-ying-yong]] credits Temporal with durable workflow history, breakpoint recovery, and idempotent retry.
- Determinism mismatch: [[wei-shen-me-xian-you-de-agent-infra-wu-fa-zhi-cheng-sheng-chan-ji-ying-yong]] says Temporal's replay model assumes deterministic workflow code, while LLM replay may choose a different path.
- Trust mismatch: [[wei-shen-me-xian-you-de-agent-infra-wu-fa-zhi-cheng-sheng-chan-ji-ying-yong]] says Temporal will faithfully execute prompt-injected logic unless a separate capability boundary exists.
- Layering role: [[wei-shen-me-xian-you-de-agent-infra-wu-fa-zhi-cheng-sheng-chan-ji-ying-yong]] says Temporal can serve as upper orchestration after semantic primitives are established.

## Qualifications
The source does not say Temporal is poor infrastructure. It says Temporal's assumptions fit deterministic workflow code better than nondeterministic, untrusted agent decision loops.

## What Changed
- Created the entity page for Temporal as the article's main durable-workflow comparison point.

## Relationships
- [[ForkRecovery]] - Temporal's replay model is contrasted with agent fork recovery.
- [[AgentResumability]] - Temporal supports durable execution but not full agent resumability on its own.
- [[SemanticIsolation]] - Temporal lacks a trust boundary for LLM-chosen actions.
- [[ProductionAgentInfrastructure]] - Temporal may be an upper orchestration layer after agent-specific primitives.

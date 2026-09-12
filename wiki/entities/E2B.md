---
title: "E2B"
type: entity
tags: [ai, agents, sandboxing, code-execution]
sources:
  - wei-shen-me-xian-you-de-agent-infra-wu-fa-zhi-cheng-sheng-chan-ji-ying-yong
last_updated: 2026-09-12
knowledge_schema: synthesis-v1
---

## Overview
[[E2B]] is an agent code-execution sandbox discussed in the source as valuable but insufficient for capability isolation and side-effect recovery.

## Current Profile
The article recognizes E2B's positioning around letting agents safely execute code. It argues that code sandboxing is a different problem from controlling what external systems an agent can affect with real credentials or how those effects should be recovered after failure.

## Key Characteristics
- Provides a sandbox for agent code execution.
- Helps isolate code-running environments.
- Does not remove risk from external credentials held by the agent.
- Does not automatically supply effect logs, idempotent replay, or irreversible-action recovery.

## Evidence
- Sandbox role: [[wei-shen-me-xian-you-de-agent-infra-wu-fa-zhi-cheng-sheng-chan-ji-ying-yong]] describes E2B as explicitly positioned around safe agent code execution.
- Credential limit: [[wei-shen-me-xian-you-de-agent-infra-wu-fa-zhi-cheng-sheng-chan-ji-ying-yong]] says an agent in a clean sandbox can still use real API keys against external services.
- Recovery limit: [[wei-shen-me-xian-you-de-agent-infra-wu-fa-zhi-cheng-sheng-chan-ji-ying-yong]] says side-effect logging and replay semantics remain unsolved by code sandboxes.

## Qualifications
The source does not evaluate E2B's sandbox implementation in depth. Its claim is about the broader category boundary between code execution and semantic agent infrastructure.

## What Changed
- Created the entity page for E2B.

## Relationships
- [[SemanticIsolation]] - E2B is contrasted with semantic isolation.
- [[ComputerUse]] - agent code-execution sandboxes can support broader agent action workflows.
- [[CapabilityGateway]] - external capability mediation addresses risks outside the sandbox.

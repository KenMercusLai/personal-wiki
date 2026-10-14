---
title: "AutoMem"
type: entity
tags: [ai, agents, memory, research]
sources:
  - "2607.01224"
last_updated: 2026-10-14
knowledge_schema: synthesis-v1
---

## Overview
[[AutoMem]] is a research framework for automatically improving an LLM agent's file-backed memory structure and its proficiency at choosing memory operations.

## Current Profile
AutoMem wraps a long-horizon agent in two sequential outer loops. The first uses a meta-LLM to review complete episode traces and revise the code, prompts, action vocabulary, validation logic, and file schema. The second uses another meta-LLM as a training engine to select useful memory decisions from the agent's own trajectories and configure LoRA training for a dedicated memory specialist.

At inference, the specialist handles LOG and memory-consultation operations while an unmodified base model commits world actions. This separation targets memory behavior without directly fine-tuning gameplay behavior, although both models share conversation history and operate inside the evolved scaffold.

## Key Characteristics
- Exposes file operations as first-class actions in the same trajectory as task actions.
- Separates post-observation logging from pre-action planning and retrieval.
- Accepts scaffold revisions only when fixed-seed average progression improves.
- Curates supervised examples from the base agent's own memory-operation outputs.
- Deploys a LoRA-trained memory specialist beside a frozen task model.
- Optimizes separate scaffolds and specialists for Crafter, MiniHack, and NetHack.

## Evidence
- Architecture and workflow: [[2607.01224]] specifies the shared inner-loop agent, complete-trajectory scaffold reviewer, data-and-configuration training engine, and two-model inference handoff.
- Scaffold behavior: [[2607.01224]] reports fewer unproductive actions, redundant writes, empty searches, and context tokens after schema and prompt evolution.
- Performance: [[2607.01224]] reports progression gains from the v0 file-memory agent through scaffold optimization and memory-specialist training in three games.
- Learned policy: [[2607.01224]] reports lower write-to-search ratios after training, consistent with a consult-before-write discipline.

## Qualifications
The framework is supported by one first-party paper using one base-model family and three games. Evaluation uses small fixed-seed samples, per-environment optimization, and memory reset between episodes; it does not establish cross-domain transfer, persistent-memory governance, matched inference economics, independent replication, or safe high-stakes deployment. The comparison with larger and proprietary models also does not hold cost, latency, and serving configuration constant.

## What Changed
- Established AutoMem as a canonical research entity.

## Relationships
- [[AgentMemory]] - AutoMem treats memory-operation choice as an optimizable agent skill.
- [[Metamemory]] - AutoMem operationalizes monitoring and control over what an agent records and retrieves.
- [[LLMContextManagement]] - its file schema and retrieval actions regulate active context.
- [[ParameterEfficientFineTuning]] - LoRA trains the dedicated memory specialist.
- [[SoftwareVerification]] - fixed-seed evaluation gates scaffold revisions.

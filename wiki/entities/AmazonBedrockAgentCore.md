---
title: "Amazon Bedrock AgentCore"
type: entity
tags: [aws, ai-agents, runtime, microvm]
sources:
  - seven-years-of-firecracker-marcs-blog
last_updated: 2026-10-07
knowledge_schema: synthesis-v1
---

## Overview
[[AmazonBedrockAgentCore]] is an [[AWS]] service represented here through its runtime model for executing AI-agent code in session-scoped [[Firecracker]] microVMs.

## Current Profile
AgentCore Runtime gives each agent session a separate microVM and destroys that VM when the session ends. A session may contain multiple user interactions, tool calls, and model calls over as much as eight hours, while deliberate cross-session state goes through AgentCore Memory or other stateful tools rather than shared code-level state. Firecracker supports the workload range by allowing CPU and memory use to grow or shrink while the VM is running.

## Key Characteristics
- Assigns one Firecracker microVM to each agent session.
- Supports sessions ranging from milliseconds to as much as eight hours.
- Keeps code-level state separate across concurrent sessions.
- Makes cross-session persistence an explicit external-service operation.
- Accommodates highly variable CPU, memory, context, tool-call, and model-call demand.

## Evidence
- Session boundary: [[seven-years-of-firecracker-marcs-blog]] states that every session receives its own microVM, which is terminated after the session.
- Visual architecture: [[seven-years-of-firecracker-marcs-blog]] shows sessions A, B, and C entering distinct agent-code instances inside separate Firecracker microVMs within AgentCore Runtime.
- Duration and interaction range: [[seven-years-of-firecracker-marcs-blog]] describes sessions from milliseconds to hours, with multi-turn sessions lasting up to eight hours and making thousands of tool or model calls.
- Explicit persistence: [[seven-years-of-firecracker-marcs-blog]] says inter-session interaction occurs through AgentCore Memory or stateful tools rather than through shared code state.
- Resource flexibility: [[seven-years-of-firecracker-marcs-blog]] attributes economic feasibility partly to resizing VM CPU and memory in place.

## Qualifications
The profile rests on a first-party AWS architecture description without comparative isolation tests, pricing, startup latency, utilization distributions, failure behavior, or independent security evaluation. MicroVM teardown removes local execution state, not information already sent to external tools, memory services, logs, or other provider systems.

## What Changed
- Created the entity page for AgentCore's session-scoped runtime design.

## Relationships
- [[AWS]] - provider of AgentCore.
- [[Firecracker]] - microVM technology implementing the per-session execution boundary.
- [[SessionScopedMicroVMIsolation]] - runtime pattern used to separate and retire agent sessions.
- [[SemanticIsolation]] - complementary layer needed for the meaning and authorization of external actions.
- [[ProductionAgentInfrastructure]] - AgentCore is a production runtime for variable-duration agent execution.

---
title: "Server-Side Agent Architecture"
type: concept
tags: [ai, agents, architecture, multi-tenancy, runtime]
sources:
  - xiao-yi-agent-harness-she-ji-shang-de-tradeoff
last_updated: 2026-10-13
knowledge_schema: synthesis-v1
---

## Definition
[[ServerSideAgentArchitecture]] runs the agent loop as a shared multi-tenant service while managing session state, tools, isolated execution, and orchestration as explicit responsibilities rather than co-locating one persistent agent process and operating system per user.

## Current Synthesis
Coding agents naturally inherit the user's machine or a dedicated cloud workspace because most useful actions touch a filesystem, compiler, debugger, or deployment environment. General workplace agents accessed from web or mobile clients need remote execution but often do not need a complete operating system for every request. A server-side architecture can therefore retain session and orchestration in a shared service, call tools directly, allocate a lightweight runtime for common file or scripting operations, and fall back to a full sandbox or microVM only when compatibility or isolation requires it.

This decomposition reduces dependence on long-lived “pet” containers and makes failure domains more explicit, but it transfers complexity into multi-tenant session management. Context policy is not merely stored chat history: compaction, notes, history retrieval, system reminders, memory, skills, and model-specific behaviors decide what the agent can know and do. The architecture should isolate expensive or risky execution without freezing those fast-moving policies behind prematurely rigid module boundaries.

Evaluation is part of the architecture. A useful offline test must run the production harness—or a behaviorally equivalent build—against reproducible tool environments and must separate harness faults, event-delivery faults, runtime failures, and model behavior. Otherwise improvements measured in a convenient local sandbox may not transfer to the multi-tenant service users actually receive.

## Key Claims
- Runtime placement should follow workload needs: local or dedicated environments fit OS-intensive coding, while shared server execution fits many web- and mobile-mediated work tasks.
- Session, tools, sandbox, and orchestration are distinct responsibilities, but their interfaces should reflect the current rate of change rather than an idealized permanent modularity.
- A sandbox is a conditional execution resource, not necessarily the identity or durable state boundary of an agent.
- Lightweight runtimes can handle common file and scripting operations, reserving full Linux microVMs for compatibility, privilege, or isolation requirements.
- Multi-tenant session state must carry context policy across users and model variants without leaking data or assuming one compaction strategy.
- Offline evaluation must preserve production-harness fidelity and reproducible tool execution.

## Evidence
- Workload split: [[xiao-yi-agent-harness-she-ji-shang-de-tradeoff]] contrasts workspace-bound coding with general work accessed through cloud-backed web and mobile clients.
- Failure boundary: [[xiao-yi-agent-harness-she-ji-shang-de-tradeoff]] cites session loss, indistinguishable WebSocket and container failures, and unsafe shell debugging as costs of an all-in-one per-user container.
- Conditional execution: [[xiao-yi-agent-harness-she-ji-shang-de-tradeoff]] argues that requests without Bash or Python need no sandbox and proposes JavaScript-first execution with microVM fallback.
- Session coupling: [[xiao-yi-agent-harness-she-ji-shang-de-tradeoff]] uses compaction, notes, history, and provider-specific reminder mechanisms to show why context policy remains tightly coupled to harness evolution.
- Evaluation fidelity: [[xiao-yi-agent-harness-she-ji-shang-de-tradeoff]] identifies production-equivalent harness behavior and repeatable tool environments as requirements for offline evaluation.

## Counterevidence & Qualifications
The concept currently rests on one practitioner design essay without comparative cost, latency, reliability, isolation, or developer-productivity measurements. A per-user sandbox may remain appropriate for strong tenancy boundaries, customer-controlled environments, data residency, long-lived desktop state, or operational simplicity. A shared server creates its own noisy-neighbor, secret-handling, scheduling, privacy, and blast-radius risks. JavaScript-first execution can reduce runtime weight only where its APIs, package ecosystem, observability, and security model cover the workload. Finally, keeping session policy coupled for experimentation can accelerate learning but also make testing, replacement, and failure isolation harder.

## What Changed
- Established the concept around workload-sensitive runtime placement, conditional sandboxing, evolving session policy, and production-fidelity evaluation.

## Related Concepts
- [[HarnessEngineering]] - supplies the wider scaffolding, constraints, feedback, and validation discipline implemented by the server-side architecture.
- [[AgentLifecycleModel]] - defines the owned session state that must survive independently of any disposable execution environment.
- [[AgenticSandboxInfrastructure]] - supplies isolated execution when a request needs operating-system compatibility or stronger containment.
- [[LLMContextManagement]] - governs the histories, reminders, notes, memories, and tools carried by multi-tenant sessions.
- [[ProductionAgentInfrastructure]] - adds durable effects, capability boundaries, recovery, observability, and accountability around the shared agent service.
- [[SoftwareVerification]] - provides the repeatable offline and online evidence needed to validate harness behavior.

---
title: "Session-Scoped MicroVM Isolation"
type: concept
tags: [microvm, isolation, ai-agents, lifecycle]
sources:
  - seven-years-of-firecracker-marcs-blog
last_updated: 2026-10-07
knowledge_schema: synthesis-v1
---

## Definition
[[SessionScopedMicroVMIsolation]] assigns each interaction session its own microVM and destroys that execution environment when the session ends.

## Current Synthesis
The AgentCore case makes the session, rather than the function call or permanent agent identity, the local execution boundary. A session can contain many turns, tool calls, model calls, and changing resource needs while retaining local continuity; teardown then removes that VM's code-level state. Any intended persistence or interaction across sessions moves into explicit external memory or stateful tools, making the local-state boundary easier to reason about without claiming that external effects are erased.

## Key Claims
- Session scope can preserve multi-turn local continuity while separating concurrent users.
- Destroying the microVM retires local code and memory state at a clear lifecycle boundary.
- Explicit external persistence makes cross-session state transfer visible in the architecture.
- In-place CPU and memory changes help one isolation model span very short and very long sessions.
- Execution isolation does not determine whether an externally authorized action is semantically safe.

## Evidence
- One VM per session: [[seven-years-of-firecracker-marcs-blog]] states and diagrams separate Firecracker microVMs for sessions A, B, and C.
- Stateful session: [[seven-years-of-firecracker-marcs-blog]] allows multiple interactions and many tool and model calls during one session of up to eight hours.
- Teardown: [[seven-years-of-firecracker-marcs-blog]] says the VM is destroyed after the session and local session context is forgotten.
- Explicit cross-session path: [[seven-years-of-firecracker-marcs-blog]] identifies AgentCore Memory and stateful tools as deliberate inter-session channels.
- Variable resources: [[seven-years-of-firecracker-marcs-blog]] reports that VM CPU and memory can grow or shrink in place.

## Counterevidence & Qualifications
The source supplies no isolation benchmark, attack analysis, resource-resizing measurements, or failure and recovery model. Teardown cannot retract tool calls, remote writes, logs, model-provider disclosures, or information stored in external memory. Long-lived sessions also retain local compromise and accumulation risk until the boundary closes.

## What Changed
- Created the concept from AgentCore's per-session microVM design.

## Related Concepts
- [[SemanticIsolation]] - session microVMs isolate execution, while semantic isolation governs capabilities and side effects.
- [[ProductionAgentInfrastructure]] - session-scoped execution is one lower-layer runtime pattern for production agents.
- [[AgentResumability]] - recovery across a destroyed or failed session requires explicit durable state beyond the microVM.
- [[BoundedLifetimeSimplification]] - teardown uses a lifetime boundary to reclaim accumulated local state.
- [[ServerlessComputing]] - sessions receive demand-created managed execution environments.

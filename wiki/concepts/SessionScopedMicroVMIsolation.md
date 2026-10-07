---
title: "Session-Scoped MicroVM Isolation"
type: concept
tags: [microvm, isolation, ai-agents, lifecycle]
sources:
  - seven-years-of-firecracker-marcs-blog
  - ru-he-she-ji-agent-zu-cheng-yun-xing-huan-jing-yu-sheng-ming-zhou-qi-yanli-yan-li
last_updated: 2026-10-07
knowledge_schema: synthesis-v1
---

## Definition
[[SessionScopedMicroVMIsolation]] assigns each interaction session its own microVM and destroys that local execution environment when the session ends, while placing intended cross-session state in explicit external channels.

## Current Synthesis
The AgentCore case makes the session, rather than the function call or permanent agent identity, the local execution boundary. A session can contain many turns, tool calls, model calls, and changing resource needs while retaining local continuity; teardown then removes that VM's code-level state. Any intended persistence or interaction across sessions moves into explicit external memory or stateful tools, making the local-state boundary easier to reason about without claiming that external effects are erased.

Yan Li's broader CoW-sandbox analysis adds a management-granularity limit. Snapshot and fork can reproduce a complete microVM or container filesystem, but a platform may instead need to capture one tool's configuration and local state and apply only that component elsewhere. Session-scoped isolation therefore gives a strong coarse execution boundary; it does not by itself define portable component state or distinguish program files from mutable configuration and runtime data.

## Key Claims
- Session scope can preserve multi-turn local continuity while separating concurrent users.
- Destroying the microVM retires local code and memory state at a clear lifecycle boundary.
- Explicit external persistence makes cross-session state transfer visible in the architecture.
- Snapshot and fork support efficient whole-environment reproduction but may be too coarse for component-level state migration.
- In-place CPU and memory changes help one isolation model span very short and very long sessions.
- Execution isolation does not determine whether an externally authorized action is semantically safe or reversible.

## Evidence
- One VM per session: [[seven-years-of-firecracker-marcs-blog]] states and diagrams separate Firecracker microVMs for sessions A, B, and C.
- Stateful session: [[seven-years-of-firecracker-marcs-blog]] allows multiple interactions and many tool and model calls during one session of up to eight hours.
- Teardown: [[seven-years-of-firecracker-marcs-blog]] says the VM is destroyed after the session and local session context is forgotten.
- Explicit cross-session path: [[seven-years-of-firecracker-marcs-blog]] identifies AgentCore Memory and stateful tools as deliberate inter-session channels.
- Variable resources: [[seven-years-of-firecracker-marcs-blog]] reports that VM CPU and memory can grow or shrink in place.
- CoW scope: [[ru-he-she-ji-agent-zu-cheng-yun-xing-huan-jing-yu-sheng-ming-zhou-qi-yanli-yan-li]] describes microVM- or container-backed CoW sandboxes with snapshot and fork at whole-filesystem granularity.
- Component boundary: [[ru-he-she-ji-agent-zu-cheng-yun-xing-huan-jing-yu-sheng-ming-zhou-qi-yanli-yan-li]] identifies per-tool configuration and local-state transfer as a finer-grained need that ordinary whole-sandbox snapshots do not meet.

## Counterevidence & Qualifications
The sources supply no comparative isolation benchmark, attack analysis, state-transfer implementation, resource-resizing measurements, or complete failure and recovery model. Teardown cannot retract tool calls, remote writes, logs, model-provider disclosures, or information stored in external memory. Long-lived sessions retain local compromise and accumulation risk until the boundary closes. Component-level snapshots may improve portability but also require explicit ownership, consistency, dependency, versioning, secret, and conflict semantics.

## What Changed
- Added whole-filesystem snapshot granularity as a limitation on component-level portability.
- Separated session execution isolation from program, configuration, and runtime-data ownership.

## Related Concepts
- [[AgentLifecycleModel]] - defines the session identity and state operations around the disposable runtime.
- [[SemanticIsolation]] - session microVMs isolate execution, while semantic isolation governs capabilities and side effects.
- [[ProductionAgentInfrastructure]] - session-scoped execution is one lower-layer runtime pattern for production agents.
- [[AgentResumability]] - recovery across a destroyed or failed session requires explicit durable state beyond the microVM.
- [[BoundedLifetimeSimplification]] - teardown uses a lifetime boundary to reclaim accumulated local state.
- [[VMSnapshotCloning]] - restores prepared whole-VM state and renews per-instance uniqueness.
- [[ServerlessComputing]] - sessions receive demand-created managed execution environments.

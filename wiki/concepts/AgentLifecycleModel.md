---
title: "Agent Lifecycle Model"
type: concept
tags: [ai, agents, lifecycle, sessions, state-management]
sources:
  - ru-he-she-ji-agent-zu-cheng-yun-xing-huan-jing-yu-sheng-ming-zhou-qi-yanli-yan-li
  - xiao-yi-agent-harness-she-ji-shang-de-tradeoff
last_updated: 2026-10-13
knowledge_schema: synthesis-v1
---

## Definition
[[AgentLifecycleModel]] defines what counts as one persistent agent, which context and runtime state belong to it, and how that state is created, saved, copied, restored, and retired while interaction and background execution continue.

## Current Synthesis
The source proposes a stateful session as the practical identity boundary for one agent. Conversation history and workspace changes accumulated under that session form one continuous trajectory, while the runtime must decide which program, configuration, and working files belong to that trajectory and should follow it during save, fork, migration, restoration, or deletion.

This makes lifecycle design a state-ownership problem rather than merely a protocol-session feature. Explicit cross-call identifiers can reconnect application state, but they do not decide what belongs to the agent or implement lifecycle operations. A directory-scoped filesystem gives those operations a concrete boundary, and a CoW sandbox can snapshot or fork a complete environment, but whole-filesystem granularity is too coarse when only one component's configuration and state should move.

The action boundary is also changing. A turn remains a useful conversational or API unit, but steering can insert new messages while work is underway and asynchronous commands can continue after the model becomes idle. A lifecycle model therefore needs continuous event and process state, not only a sequence of closed request-response turns.

The server-side harness source moves that state boundary into a multi-tenant service. Durable session state should not disappear with a failed execution container, and a request that does not need operating-system tools should not require a sandbox at all. Yet session state is more than stored messages: compaction, notes, history retrieval, system reminders, and model-specific fallbacks are active policies. Keeping those policies adaptable can matter more than prematurely enforcing a perfectly clean separation from the rest of the harness.

## Key Claims
- A stateful session can serve as one agent's identity boundary by joining context history with workspace state.
- Agent state must be defined by ownership and lifecycle operations, not inferred from every side effect produced by a tool.
- Protocol-level session or state identifiers can reference continuity but do not themselves save, copy, restore, migrate, or delete an agent.
- Directory-scoped state makes lifecycle operations concrete, while whole-filesystem snapshots may be too coarse for component-level transfer.
- Steering and asynchronous commands require lifecycle tracking beyond a sequence of closed turns.
- Greater OS-level freedom increases pressure for packaging, isolation, state-location, and collaboration conventions.
- Multi-tenant services should separate durable session state from disposable execution while preserving room to evolve model-specific context policy.

## Evidence
- Identity boundary: [[ru-he-she-ji-agent-zu-cheng-yun-xing-huan-jing-yu-sheng-ming-zhou-qi-yanli-yan-li]] defines a stateful session through its context history and workspace changes.
- State ownership: [[ru-he-she-ji-agent-zu-cheng-yun-xing-huan-jing-yu-sheng-ming-zhou-qi-yanli-yan-li]] separates external tool side effects from the state that should belong to and travel with an agent.
- Lifecycle operations: [[ru-he-she-ji-agent-zu-cheng-yun-xing-huan-jing-yu-sheng-ming-zhou-qi-yanli-yan-li]] asks how owned state is saved, copied, deleted, created, and restored.
- Filesystem boundary: [[ru-he-she-ji-agent-zu-cheng-yun-xing-huan-jing-yu-sheng-ming-zhou-qi-yanli-yan-li]] proposes explicit directories for program, configuration, and runtime data.
- Granularity limit: [[ru-he-she-ji-agent-zu-cheng-yun-xing-huan-jing-yu-sheng-ming-zhou-qi-yanli-yan-li]] says whole-filesystem CoW does not directly snapshot and apply one tool's configuration and local state.
- Continuous interaction: [[ru-he-she-ji-agent-zu-cheng-yun-xing-huan-jing-yu-sheng-ming-zhou-qi-yanli-yan-li]] uses steering and turn-outliving asynchronous commands to argue against turn-only lifecycle modeling.
- Multi-tenant durability: [[xiao-yi-agent-harness-she-ji-shang-de-tradeoff]] uses lost sessions in failed all-in-one containers to argue that session state should outlive a particular sandbox process.
- Policy-bearing sessions: [[xiao-yi-agent-harness-she-ji-shang-de-tradeoff]] shows that compaction, notes, history tools, reminders, and model switching make a session an active context-management policy rather than a passive transcript.

## Counterevidence & Qualifications
The synthesis rests on two September 2026 practitioner essays. They propose architectural boundaries without measuring competing lifecycle systems, specifying crash recovery or concurrent-state semantics, or resolving security, privacy, garbage collection, noisy-neighbor behavior, and distributed consistency. A session is one useful identity boundary, not a universal one: products may separate user identity, tenant, task, workspace, process, conversation, and durable memory differently. Turn-based APIs can also remain useful inside a continuously interactive runtime. Keeping session policy coupled to a rapidly evolving harness may accelerate experiments but can impede independent testing, replacement, and fault isolation.

## What Changed
- Extended the lifecycle model from one stateful agent to durable multi-tenant sessions separated from disposable execution.
- Added compaction, notes, history, reminders, and model fallbacks as policy-bearing parts of session state.
- Created a lifecycle model centered on session identity, explicit state ownership, and continuous interaction.
- Distinguished reference mechanisms from actual save, copy, restore, migration, and deletion semantics.
- Added component-level state granularity as a limit of whole-sandbox snapshots.

## Related Concepts
- [[GenerativeAIAgentArchitecture]] - supplies the wider context-plus-runtime system whose continuity the lifecycle model governs.
- [[SessionScopedMicroVMIsolation]] - uses session teardown as a concrete local execution-state boundary.
- [[AgentFilesystem]] - provides a potential storage boundary for agent-owned program, configuration, and working state.
- [[AgentResumability]] - requires sufficient durable state to continue safely after interruption or environment loss.
- [[ForkRecovery]] - applies snapshot or checkpoint state to create a recoverable execution branch.
- [[TapeAndAnchors]] - preserves and reconstructs interaction history without requiring all prior state in active context.
- [[BoundedLifetimeSimplification]] - uses explicit lifetime limits to simplify cleanup and state reasoning.
- [[ServerSideAgentArchitecture]] - hosts session continuity independently of conditional sandbox allocation.

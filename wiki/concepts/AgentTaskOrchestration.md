---
title: "Agent Task Orchestration"
type: concept
tags: [ai, agents, orchestration, workflows, reliability]
sources:
  - tapexbee
last_updated: 2026-10-22
knowledge_schema: synthesis-v1
---

## Definition
[[AgentTaskOrchestration]] is the practice of expressing bounded agent work as reviewable milestones with explicit dependencies, completion criteria, runtime state, checkpoints, and execution on established job or workflow infrastructure.

## Current Synthesis
The Bee proposal separates three layers. A template describes intent and acceptance through DAG metadata, private configuration, a business-facing Skill, and BDD scenarios. An agent runtime turns each DAG node into Tape entries and maintains a workspace-local state projection for the UI. An executor such as Kubernetes or Argo Workflows supplies scheduling, isolation, resource control, and operational tooling. This division treats the agent as an intelligent worker inside a familiar delivery system rather than making the LLM runtime responsible for every scheduler concern.

Reviewability and recovery shape the node boundaries. Milestones deliberately slow an otherwise fast agent so a person can inspect outputs and retrigger a node after changing its Skill. Frequent node-final and DAG-checkpoint anchors bound context growth and preserve external-call results for retry decisions. The pattern improves observability, but safe recovery still requires idempotent operations, effect records, compensation, and consistency between projected workflow state and the underlying Tape.

## Key Claims
- Reuse mature Job, Cron, CI, container, and workflow schedulers for execution concerns that are not uniquely agentic.
- Separate template intent, agent execution history, and infrastructure scheduling into distinct but linked layers.
- Represent business work as a DAG when dependencies and reviewable milestones are known, while allowing the agent to implement the work inside each node.
- Use executable acceptance criteria to supplement prose instructions and make node completion more observable.
- Checkpoint node and whole-workflow state frequently enough to bound context growth and inform retries.
- Keep human review, revision, and deployment as explicit lifecycle branches rather than assuming that generated output should ship automatically.

## Evidence
- Infrastructure reuse: [[tapexbee]] recommends Kubernetes Jobs or CronJobs and Argo Workflows for scaling, resource control, isolation, audit, and DAG execution.
- Template contract: [[tapexbee]] combines `metadata.json`, `config.toml`, `SKILL.md`, and BDD `.feature` files.
- Runtime projection: [[tapexbee]] describes `task.json` as the changing DAG state mapped from the workspace to the interface.
- Review loop: [[tapexbee]] and its retained architecture diagram route actual output through approval, revision, or deployment.
- Milestone visibility: [[tapexbee]] and its retained product screenshot show ordered nodes, dependency blocking, manual and automatic modes, node replay, and selected-node details.
- Checkpoint model: [[tapexbee]] defines task, node, and DAG anchors around ordinary thinking, tool, message, and run entries.

## Counterevidence & Qualifications
The evidence is one author's first-party implementation account and a single redacted product example, not a comparative evaluation. A DAG can encode the wrong decomposition; BDD scenarios can reward superficial compliance; milestone review can become a bottleneck; and node replay can duplicate external effects. The source does not specify transactional consistency between `task.json` and Tape, scheduler-versus-agent authority, concurrent update handling, compensation, exactly-once semantics, checkpoint retention, or measured recovery quality. Kubernetes and Argo reduce scheduler implementation work but add their own operational and security costs.

## What Changed
- Created the concept from Bee's separation of template, agent runtime, and established executor infrastructure.
- Added human review, executable acceptance criteria, and frequent DAG checkpoints as core orchestration controls.
- Distinguished context-aware retry from side-effect-safe resumability.

## Related Concepts
- [[AgenticWorkflowPatterns]] - supplies the broader catalog of fixed workflows, dynamic agent loops, routing, parallelization, and evaluation patterns.
- [[AgentTopicLifecycle]] - provides the bounded Topic identity that Bee specializes for Job and Cron work.
- [[TapeAndAnchors]] - supplies the durable entry history and checkpoint vocabulary beneath the workflow.
- [[AgentResumability]] - requires stronger recovery semantics for external effects than contextual checkpoints alone provide.
- [[Kubernetes]] - provides the proposed workload execution, isolation, resource, and audit substrate.
- [[LLMToolingSkills]] - carries per-Bee behavior and access to deployment or orchestration capabilities.

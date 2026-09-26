---
title: "System Architecture Principles"
type: concept
tags: [software-architecture, reliability, operability, standards, technical-debt]
sources:
  - wo-zuo-xi-tong-jia-gou-de-yi-xie-yuan-ze-ku-ke-coolshell
  - blog-andrew-harmel-law-martinfowler-com-scaling-the-practice-of-architecture-conversationally
last_updated: 2026-09-25
knowledge_schema: synthesis-v1
---

## Definition
[[SystemArchitecturePrinciples]] are outcome-oriented rules for designing complex software so delivery, reliability, cost, correctness, interoperability, change, and operation improve together rather than optimizing one component or fashionable technology in isolation.

## Current Synthesis
The source's most durable frame starts with benefits: architecture should lower coordination and delivery friction, improve service stability, or reduce human, time, and financial cost. A service-and-API viewpoint then gives development and operations a shared unit of reasoning, while standards let monitoring and control systems interpret behavior consistently.

The lifecycle argument joins completeness, extensibility, and operability. Preserve strong invariants before taking performance shortcuts; decouple business capabilities through services, events, workflows, gateways, or discovery; and centralize reusable control concerns such as traffic, resilience, configuration, telemetry, deployment, resources, and middleware. This is not a demand to centralize all business logic. It is a proposal to separate specialized control-plane knowledge from domain logic and make the common controls observable and governable.

Technology selection remains conditional. Mature global ecosystems and standard components often reduce integration and staffing risk, but diagnosis, workload, team context, alternatives, and reversal criteria must outrank a categorical language choice. The same lifecycle discipline applies to legacy systems: repay debt when feasible or isolate it behind an anti-corruption boundary so new work does not inherit every old constraint. Deliberate exploration is compatible with this caution when experiments target a plausible future shift, remain bounded, and generate evidence.

Principles themselves need a governance test. To guide autonomous teams without direct control, they should be specific, measurable, achievable, realistic, and testable; support business strategy; state their implications; and remain few enough to remember. Teams should co-create and maintain them so they feel ownership, while [[ArchitectureDecisionRecords]] explicitly identify applicable principles and justify deviations. A deviation can reveal either an exceptional decision or a principle that needs revision.

## Key Claims
- Architecture should be evaluated by delivery flow, service stability, and total cost rather than technical novelty.
- Service and external-API boundaries can align product, development, operations, monitoring, and automation around shared outcomes.
- Correctness, completeness, and recoverable invariants should usually precede performance shortcuts whose constraints are hard to restore later.
- Standards and centralized control capabilities make distributed behavior more observable, automatable, and governable.
- Extensibility and operability are lifecycle properties that require loose business coupling plus explicit deployment, recovery, and change controls.
- Technology choices and experiments should combine mature ecosystem priors with data, root-problem discovery, comparison, and explicit tradeoffs.
- Principles for autonomous teams should provide testable decision criteria, strategic direction, and explicit implications rather than restating generic practices.

## Evidence
- Outcome test: [[wo-zuo-xi-tong-jia-gou-de-yi-xie-yuan-ze-ku-ke-coolshell]] defines useful architecture through faster team delivery, higher stability or SLA, and lower human, time, and financial cost.
- Shared viewpoint: [[wo-zuo-xi-tong-jia-gou-de-yi-xie-yuan-ze-ku-ke-coolshell]] argues that services and external APIs provide a more coherent cross-functional frame than isolated resources or technologies.
- Completeness before optimization: [[wo-zuo-xi-tong-jia-gou-de-yi-xie-yuan-ze-ku-ke-coolshell]] recommends preserving relational and ACID guarantees as the base and adding looser NoSQL models where evidence justifies them.
- Standards and controls: [[wo-zuo-xi-tong-jia-gou-de-yi-xie-yuan-ze-ku-ke-coolshell]] connects shared API, naming, logging, monitoring, configuration, middleware, and version rules to traffic, resilience, telemetry, and deployment controls.
- Lifecycle design: [[wo-zuo-xi-tong-jia-gou-de-yi-xie-yuan-ze-ku-ke-coolshell]] links loose service coupling, discovery, gateways, workflow, and event-driven patterns to change and operational flexibility.
- Debt boundary: [[wo-zuo-xi-tong-jia-gou-de-yi-xie-yuan-ze-ku-ke-coolshell]] recommends direct repayment or an anti-corruption layer that keeps legacy constraints out of a new system area.
- Decision method: [[wo-zuo-xi-tong-jia-gou-de-yi-xie-yuan-ze-ku-ke-coolshell]] favors diagnostic data, research, alternative comparison, X-Y problem discovery, and deliberate exploration over habit or novelty alone.
- Decision criteria: [[blog-andrew-harmel-law-martinfowler-com-scaling-the-practice-of-architecture-conversationally]] says architectural principles should be SMART, strategy-linked, explicit about implications, and limited to a memorable set.
- Collective ownership: [[blog-andrew-harmel-law-martinfowler-com-scaling-the-practice-of-architecture-conversationally]] recommends sourcing and maintaining principles with teams rather than imposing them only from above.
- Governed deviation: [[blog-andrew-harmel-law-martinfowler-com-scaling-the-practice-of-architecture-conversationally]] asks ADR authors to name relevant principles and clearly justify conflicts, with principle changes recorded separately.

## Counterevidence & Qualifications
The sources are practitioner accounts rather than comparative evidence that the proposed principles or creation process improve outcomes across organizations. The complex-systems source may overfit simpler and low-volume applications; centralized control planes can become coupling, outage, ownership, or organizational bottlenecks; and “completeness before performance” does not mean every workload requires a relational database or maximum consistency. Its Java recommendation is especially overbroad because runtime constraints, team skills, workload, deployment model, safety, and migration cost can support other choices. Reader comments also dispute its stack assumptions and one tracing implementation detail.

SMART framing can make principles easier to test, but rigid measurement may privilege quantifiable outcomes and team sourcing can still reproduce existing power imbalances. A small memorable set cannot replace technical strategy, cross-functional requirements, local expertise, or explicit exception handling.

## What Changed
- Created a benefits-first synthesis of Chen Hao's eleven architecture principles.
- Preserved the distinction between reusable control-plane capabilities and centralized business logic.
- Qualified mature-technology and Java prescriptions with contextual selection and source-evidence limits.
- Added testability, strategic fit, team ownership, and explicit ADR-based deviation as governance properties of architectural principles.

## Related Concepts
- [[SoftwareEngineering]] - architecture is one part of delivering and maintaining useful, operable software.
- [[ContextualTechnologySelection]] - turns technology choice into a problem-fit and tradeoff judgment.
- [[APIErrorHandling]] - shows how shared protocol semantics support both clients and operations.
- [[SystemReliability]] - supplies the stability, degradation, recovery, and change outcomes architecture must protect.
- [[ServiceObservability]] - centralizes signals needed to understand distributed service behavior.
- [[TechnicalDebtTracking]] - makes debt visible, while architecture governance decides whether to repay, tolerate, or isolate it.
- [[ArchitectureAlignmentForces]] - qualifies how much governance and coupling different organizational scopes can sustain.
- [[DecentralizedArchitectureGovernance]] - uses shared principles to align local decisions without central approval.
- [[ArchitectureDecisionRecords]] - record which principles apply and why a decision follows or overrides them.

---
title: "Spec-Driven Agent Development"
type: concept
tags: [ai, software-engineering, specifications, agents]
sources:
  - yong-claude-code-jiang-san-wan-hang-go-xiang-mu-yi-zhi-dao-rust-agent-team-shi-jian-yu-harness-xiao-lu-you-hua
  - wei-shen-me-ai-xie-dai-ma-geng-kuai-dan-jiao-fu-mei-bian-yi-ji-wo-zen-me-ba-ta-ban-hui-lai-de
  - spec-driven-development-with-spec-kit
last_updated: 2026-10-07
knowledge_schema: synthesis-v1
---

## Definition
[[SpecDrivenAgentDevelopment]] is a coding-agent workflow where specifications, architectural decisions, test plans, task state, and acceptance criteria act as durable interfaces between agents, humans, and implementation phases.

## Current Synthesis
The sources argue that specs become more valuable, not less, when agents write much of the code. In the mihomo-rust workflow, the Architect decides architectural constraints, the PM translates those decisions into ordered roadmap work, the Engineer implements against structured specs, and QA derives tests from the same documents. Specs reduce duplicated source-code exploration because each agent can read a shared interface instead of independently interpreting upstream code.

There is also a lighter individual or team workflow. Specs are not bureaucracy for every task; they are persistent business-state context for existing systems, compatibility-sensitive changes, and complex rules. A minimal spec can capture current behavior, desired behavior, invariants that must not change, and edge cases, giving the agent a decision surface that temporary plan-mode reasoning cannot preserve or share.

The [[GitHubSpecKit]] case adds a staged single-developer variant: constitution, specification, clarification, technical plan, tasks, pre-implementation analysis, phased implementation, and post-implementation convergence. Repository artifacts made agent restarts, fresh chats, and different models practical, while analysis surfaced cross-document conflicts before coding. The same case sets a hard boundary on the method: artifact consistency and mandatory TDD did not prevent stale dependencies, missed UI intent, a broken menu interaction, destructive tag editing, or a missing container dependency. Spec-driven development therefore improves coordination and inspectability; it does not make specifications complete or implementation self-verifying.

## Key Claims
- Specs are durable coordination interfaces for agents, not merely human bureaucracy.
- ADRs or constitutions should settle non-negotiable architecture and governance before feature specs and plans fill in negotiable details.
- Effective specs make behavior, invariants, edge cases, schemas, interfaces, divergence policy, acceptance scenarios, and verification plans explicit.
- Tables, precise references, checked tasks, and explicit state labels are easier for agents to resume and share than vague prose or conversation-only plans.
- Analysis before coding and convergence after coding can expose conflicts and implementation gaps across the specification chain.
- The value of specs rises with project size, compatibility risk, role separation, context pressure, and the need to reuse state across sessions.
- Specification depth has setup, review, token, and cost overhead and cannot replace runtime testing, usability inspection, dependency maintenance, or human acceptance.

## Evidence
- Multi-agent coordination: [[yong-claude-code-jiang-san-wan-hang-go-xiang-mu-yi-zhi-dao-rust-agent-team-shi-jian-yu-harness-xiao-lu-you-hua]] shows gap analysis, ADRs, roadmap tasks, structured implementation specs, independent test plans, and verification across PM, Architect, Engineer, and QA roles.
- Agent-readable structure: [[yong-claude-code-jiang-san-wan-hang-go-xiang-mu-yi-zhi-dao-rust-agent-team-shi-jian-yu-harness-xiao-lu-you-hua]] lists YAML schema, struct shapes, error types, divergence tables, precise references, and explicit `completed / in-progress / blocked` states as coordination devices.
- Minimal persistent context: [[wei-shen-me-ai-xie-dai-ma-geng-kuai-dan-jiao-fu-mei-bian-yi-ji-wo-zen-me-ba-ta-ban-hui-lai-de]] says a lightweight spec should record current and desired behavior, protected invariants, and edge cases in a team-owned file rather than one temporary plan-mode conversation.
- Throughput boundary: [[wei-shen-me-ai-xie-dai-ma-geng-kuai-dan-jiao-fu-mei-bian-yi-ji-wo-zen-me-ba-ta-ban-hui-lai-de]] argues that specification and full-SDLC discipline help only when verification, review capacity, and WIP limits prevent faster coding from enlarging downstream queues.
- Staged workflow: [[spec-driven-development-with-spec-kit]] documents a greenfield sequence from constitution through convergence, with generated user stories, contracts, plans, 129 initial tasks, and checked progress.
- Early conflict detection: [[spec-driven-development-with-spec-kit]] reports that analysis found critical conflicts involving secrets, versioning, TDD ordering, dependencies, limits, and measurable outcomes before implementation.
- Persistence and recovery: [[spec-driven-development-with-spec-kit]] reports that repository artifacts and checked tasks let work resume after slow or restarted agent sessions and supported clean conversation boundaries.
- Residual defects and cost: [[spec-driven-development-with-spec-kit]] reports that convergence found gaps and manual testing still found several bugs; it also reports roughly 7,000 credits for the initial release and estimates, without measurement, a 20–30% token premium.

## Counterevidence & Qualifications
The sources are practitioner reports, not controlled comparisons. They warn that this structure can be overkill for small scripts, exploratory prototypes, routine refactors, or changes whose context is already obvious. Precise but wrong specifications can coordinate agents toward the wrong result, and documented acceptance criteria can omit behavior users actually care about. The GitHub Spec Kit case is greenfield and explicitly leaves brownfield reverse engineering and non-technical stakeholder editing unresolved. Its cost figures depend on one model mix, subscription, tool release, and project, while its screenshots and author testing establish feature presence rather than independent correctness or maintainability.

## What Changed
- Added a full staged workflow that joins pre-implementation analysis with post-implementation convergence.
- Added evidence that repository task state supports restarts, fresh chats, phased work, and model changes.
- Narrowed the judgment: specification consistency and TDD improve control but do not guarantee behavioral fidelity or defect-free implementation.
- Added project-scale, token-cost, and brownfield-adoption boundaries to the choice between full specs and lighter planning.

## Related Concepts
- [[AgentTeam]] - specs are the main interface between specialized agent roles.
- [[HarnessEngineering]] - specifications and checked state are harness artifacts that constrain and orient agent work.
- [[AICodingPractice]] - specification depth is one operating choice alongside model selection, fresh sessions, review, and direct debugging.
- [[SoftwareVerification]] - executable checks and human acceptance determine whether specification-backed work actually behaves correctly.
- [[UpstreamDivergencePolicy]] - divergence tables are one recurring spec component in compatibility-sensitive porting.
- [[BottleneckAwareAICoding]] - specification rigor helps only when review, verification, and WIP constraints are managed across the delivery system.
- [[VibeCoding]] - spec-driven work trades some improvisational speed for persistent intent, staged review, and resumability.

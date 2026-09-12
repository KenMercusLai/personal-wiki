---
title: "Spec-Driven Agent Development"
type: concept
tags: [ai, software-engineering, specifications, agents]
sources:
  - yong-claude-code-jiang-san-wan-hang-go-xiang-mu-yi-zhi-dao-rust-agent-team-shi-jian-yu-harness-xiao-lu-you-hua
last_updated: 2026-09-12
knowledge_schema: synthesis-v1
---

## Definition
[[SpecDrivenAgentDevelopment]] is a coding-agent workflow where specifications, ADRs, test plans, and status documents act as formal interfaces between agents and humans.

## Current Synthesis
The source argues that specs become more valuable, not less, when agents write much of the code. In the mihomo-rust workflow, the Architect decides architectural constraints, the PM translates those decisions into ordered roadmap work, the Engineer implements against structured specs, and QA derives tests from the same documents. Specs reduce duplicated source-code exploration because each agent can read a shared interface instead of independently interpreting the upstream Go code.

## Key Claims
- Specs are coordination interfaces for agents, not merely human bureaucracy.
- ADRs should settle non-negotiable architecture before implementation specs fill in details.
- Effective specs include YAML schema, Rust struct shapes, error types, divergence tables, and linked test plans.
- Tables, precise references, and explicit state labels are easier for agents to use than vague prose.
- Status documents can preserve owner, task, commit, and decision state across agent sessions.
- The value of specs rises with project size, role separation, and context-window pressure.

## Evidence
- Transport-layer pipeline: [[yong-claude-code-jiang-san-wan-hang-go-xiang-mu-yi-zhi-dao-rust-agent-team-shi-jian-yu-harness-xiao-lu-you-hua]] shows gap analysis, ADR-0001, roadmap tasks, `transport-layer.md`, implementation, test-plan generation, and verification.
- Spec structure: [[yong-claude-code-jiang-san-wan-hang-go-xiang-mu-yi-zhi-dao-rust-agent-team-shi-jian-yu-harness-xiao-lu-you-hua]] lists YAML schema, struct shapes, error types, divergence tables, and independent test plans as the fixed sections.
- Agent interface: [[yong-claude-code-jiang-san-wan-hang-go-xiang-mu-yi-zhi-dao-rust-agent-team-shi-jian-yu-harness-xiao-lu-you-hua]] says Architect defines type signatures, Engineer implements them, and QA generates tests from error types.
- Agent-readable documents: [[yong-claude-code-jiang-san-wan-hang-go-xiang-mu-yi-zhi-dao-rust-agent-team-shi-jian-yu-harness-xiao-lu-you-hua]] recommends tables, exact references, and explicit `completed / in-progress / blocked` states.

## Counterevidence & Qualifications
The article warns that this structure is overkill for small projects and exploratory prototypes. Specs also depend on human or architect-agent quality: a precise but wrong spec can coordinate agents toward the wrong implementation.

## What Changed
- Created the concept page for using specs as agent-facing coordination interfaces.

## Related Concepts
- [[AgentTeam]] - specs are the main interface between specialized agent roles.
- [[HarnessEngineering]] - specs are harness artifacts that constrain and orient agent work.
- [[AICodingPractice]] - specs help keep AI-generated changes understandable and reviewable.
- [[SoftwareVerification]] - test plans and CI validate whether specs were implemented correctly.
- [[UpstreamDivergencePolicy]] - divergence tables are one recurring spec component in porting work.

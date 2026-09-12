---
title: "Agent Team"
type: concept
tags: [ai, agents, software-engineering, collaboration]
sources:
  - yong-claude-code-jiang-san-wan-hang-go-xiang-mu-yi-zhi-dao-rust-agent-team-shi-jian-yu-harness-xiao-lu-you-hua
last_updated: 2026-09-12
knowledge_schema: synthesis-v1
---

## Definition
[[AgentTeam]] is a multi-agent software workflow where specialized agents hold different project roles, model assignments, responsibilities, and file-owned state.

## Current Synthesis
The source presents Agent Team as a way to make a large codebase fit into multiple bounded working roles instead of asking one coding agent to hold global architecture, task priority, implementation detail, and verification state at once. In the mihomo-rust port, PM, Architect, Engineer, and QA agents communicated through files rather than conversation alone. The important design is not merely parallelism; it is role separation plus document ownership, so architecture, roadmap, specs, test plans, and CI state stay durable across sessions and milestone resets.

## Key Claims
- Agent teams are most useful when a project is too large for one context window and one generic agent role.
- Role separation lets stronger models handle architecture while cheaper or faster models handle structured execution and testing work.
- File-system state can serve as the shared communication substrate among agents.
- ADRs, specs, roadmaps, test plans, and CI status prevent decision loops between agents.
- Milestone boundaries are natural points to restart agents and reload durable project state.

## Evidence
- Role design: [[yong-claude-code-jiang-san-wan-hang-go-xiang-mu-yi-zhi-dao-rust-agent-team-shi-jian-yu-harness-xiao-lu-you-hua]] assigns PM and Engineer to Sonnet, Architect to Opus, and QA to Haiku.
- File ownership: [[yong-claude-code-jiang-san-wan-hang-go-xiang-mu-yi-zhi-dao-rust-agent-team-shi-jian-yu-harness-xiao-lu-you-hua]] maps PM to `vision.md` and `roadmap.md`, Architect to gap analysis and ADRs, QA to test plans and CI status, and shared specs plus `CLAUDE.md` to the team.
- Decision hierarchy: [[yong-claude-code-jiang-san-wan-hang-go-xiang-mu-yi-zhi-dao-rust-agent-team-shi-jian-yu-harness-xiao-lu-you-hua]] states that ADRs determine architecture, specs fill details, and test plans verify specs.
- Milestone reset: [[yong-claude-code-jiang-san-wan-hang-go-xiang-mu-yi-zhi-dao-rust-agent-team-shi-jian-yu-harness-xiao-lu-you-hua]] records a memory requiring all teammates to shut down and respawn at milestone completion.

## Counterevidence & Qualifications
The source explicitly says Agent Team is not always worth the overhead. It is less suitable for small projects under roughly 5,000 lines, exploratory prototypes, or projects without test infrastructure, because the role and document structure can become heavier than the work itself.

## What Changed
- Created the concept page for multi-agent role separation as a coding-agent workflow.

## Related Concepts
- [[AIAgentCollaboration]] - Agent Team is a structured, multi-agent form of collaboration.
- [[AICodingPractice]] - agent teams require disciplined engineering norms to stay reviewable.
- [[HarnessEngineering]] - role files, specs, and tests are part of the harness that makes an agent team usable.
- [[LLMContextManagement]] - role separation and milestone respawn manage context pressure.
- [[SpecDrivenAgentDevelopment]] - specs are the interface between Agent Team roles.
- [[SoftwareVerification]] - QA and CI supply the validation boundary for Agent Team output.

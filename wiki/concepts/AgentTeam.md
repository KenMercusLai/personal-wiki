---
title: "Agent Team"
type: concept
tags: [ai, agents, software-engineering, collaboration]
sources:
  - yong-claude-code-jiang-san-wan-hang-go-xiang-mu-yi-zhi-dao-rust-agent-team-shi-jian-yu-harness-xiao-lu-you-hua
  - duo-agent-xie-zuo-ben-zhi-shi-fen-bu-shi-xi-tong-wen-ti-mo-xing-duo-qiang-ye-mei-yong
last_updated: 2026-09-13
knowledge_schema: synthesis-v1
---

## Definition
[[AgentTeam]] is a multi-agent software workflow where specialized agents hold different project roles, model assignments, responsibilities, and file-owned state.

## Current Synthesis
The sources present Agent Team as a way to make large AI coding work fit into multiple bounded roles without pretending that parallel agents can simply write components independently and merge them later. In the mihomo-rust port, PM, Architect, Engineer, and QA agents communicated through files rather than conversation alone. The important design is not merely parallelism; it is role separation plus document ownership, so architecture, roadmap, specs, test plans, and CI state stay durable across sessions and milestone resets.

At the theoretical level, multi-agent software development is a [[DistributedConsensus]] problem over an underspecified prompt. Agent teams therefore need explicit coordination artifacts, failure detection, and verification topology because each agent's local interpretation can constrain or contradict the others. Bigger models can raise first-pass quality, but they do not remove consensus, Byzantine-style misunderstanding, or liveness tradeoffs.

## Key Claims
- Agent teams are most useful when a project is too large for one context window and one generic agent role.
- Role separation lets stronger models handle architecture while cheaper or faster models handle structured execution and testing work.
- File-system state can serve as the shared communication substrate among agents.
- ADRs, specs, roadmaps, test plans, and CI status prevent decision loops between agents.
- Milestone boundaries are natural points to restart agents and reload durable project state.
- Agent teams need explicit consensus and verification mechanisms because prompt interpretation is structurally underspecified.

## Evidence
- Role design: [[yong-claude-code-jiang-san-wan-hang-go-xiang-mu-yi-zhi-dao-rust-agent-team-shi-jian-yu-harness-xiao-lu-you-hua]] assigns PM and Engineer to Sonnet, Architect to Opus, and QA to Haiku.
- File ownership: [[yong-claude-code-jiang-san-wan-hang-go-xiang-mu-yi-zhi-dao-rust-agent-team-shi-jian-yu-harness-xiao-lu-you-hua]] maps PM to `vision.md` and `roadmap.md`, Architect to gap analysis and ADRs, QA to test plans and CI status, and shared specs plus `CLAUDE.md` to the team.
- Decision hierarchy: [[yong-claude-code-jiang-san-wan-hang-go-xiang-mu-yi-zhi-dao-rust-agent-team-shi-jian-yu-harness-xiao-lu-you-hua]] states that ADRs determine architecture, specs fill details, and test plans verify specs.
- Milestone reset: [[yong-claude-code-jiang-san-wan-hang-go-xiang-mu-yi-zhi-dao-rust-agent-team-shi-jian-yu-harness-xiao-lu-you-hua]] records a memory requiring all teammates to shut down and respawn at milestone completion.
- Consensus limit: [[duo-agent-xie-zuo-ben-zhi-shi-fen-bu-shi-xi-tong-wen-ti-mo-xing-duo-qiang-ye-mei-yong]] argues that parallel agents must converge on one compatible interpretation of an underspecified prompt.
- Verification topology: [[duo-agent-xie-zuo-ben-zhi-shi-fen-bu-shi-xi-tong-wen-ti-mo-xing-duo-qiang-ye-mei-yong]] says decomposition can reduce incoherence while increasing omissions, so agent teams need both local and global gates.

## Counterevidence & Qualifications
The case-study source explicitly says Agent Team is not always worth the overhead. It is less suitable for small projects under roughly 5,000 lines, exploratory prototypes, or projects without test infrastructure, because the role and document structure can become heavier than the work itself. The distributed-systems source adds that coordination mechanisms improve practical outcomes but cannot guarantee safety, liveness, and fault tolerance in every asynchronous failure scenario.

## What Changed
- Created the concept page for multi-agent role separation as a coding-agent workflow.
- Added the distributed-consensus qualification: agent teams require coordination and verification topology, not only role separation.

## Related Concepts
- [[AIAgentCollaboration]] - Agent Team is a structured, multi-agent form of collaboration.
- [[AICodingPractice]] - agent teams require disciplined engineering norms to stay reviewable.
- [[HarnessEngineering]] - role files, specs, and tests are part of the harness that makes an agent team usable.
- [[LLMContextManagement]] - role separation and milestone respawn manage context pressure.
- [[SpecDrivenAgentDevelopment]] - specs are the interface between Agent Team roles.
- [[SoftwareVerification]] - QA and CI supply the validation boundary for Agent Team output.
- [[DistributedConsensus]] - agent teams must converge on a shared prompt interpretation.
- [[TrustTopology]] - heterogeneous gates help make multi-agent output reliable.

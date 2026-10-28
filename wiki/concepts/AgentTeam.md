---
title: "Agent Team"
type: concept
tags: [ai, agents, software-engineering, collaboration]
sources:
  - yong-claude-code-jiang-san-wan-hang-go-xiang-mu-yi-zhi-dao-rust-agent-team-shi-jian-yu-harness-xiao-lu-you-hua
  - duo-agent-xie-zuo-ben-zhi-shi-fen-bu-shi-xi-tong-wen-ti-mo-xing-duo-qiang-ye-mei-yong
  - xiang-zuo-xiang-you-leetao
  - agent-shi-dai-de-clice
  - sui-shi-sui-di-zhi-hui-ni-de-agent-tuan-dui-leon7hao
  - ai-harness-engineering
last_updated: 2026-10-27
knowledge_schema: synthesis-v1
---

## Definition
[[AgentTeam]] is a multi-agent software workflow where specialized agents hold different project roles, model assignments, responsibilities, and file-owned state.

## Current Synthesis
The sources present Agent Team as a way to make large AI coding work fit into multiple bounded roles without pretending that parallel agents can simply write components independently and merge them later. In the mihomo-rust port, PM, Architect, Engineer, and QA agents communicated through files rather than conversation alone. The important design is not merely parallelism; it is role separation plus document ownership, so architecture, roadmap, specs, test plans, and CI state stay durable across sessions and milestone resets.

At the theoretical level, multi-agent software development is a [[DistributedConsensus]] problem over an underspecified prompt. Agent teams therefore need explicit coordination artifacts, failure detection, and verification topology because each agent's local interpretation can constrain or contradict the others. Bigger models can raise first-pass quality, but they do not remove consensus, Byzantine-style misunderstanding, or liveness tradeoffs.

Kuafu supplies a smaller practitioner case: after connecting several coding CLIs, Leetao assigned implementation to one agent and review to another and reports that the arrangement felt useful. This supports role separation at a minimal scale while also showing how little a two-role demo establishes without shared specifications, independent tests, measured defect detection, or a clear escalation rule.

The clice developer adds an operator-interface case between those extremes. A custom web orchestrator presents multiple workspaces, branches, pull requests, agents, and resource status in one VS Code view, while a mobile view supports remote supervision. The workflow uses multiple agents for implementation, cross-review, and acceptance, but the author still supplies missing context and keeps architecture under human control. This extends Agent Team from role and file topology into an observability and control surface without showing that more agents independently improve code quality.

The Lody roadmap adds model heterogeneity and a shared context layer to this control-surface view. Its proposed leader would interpret intent, decompose work, route UI, logic, review, search, and small tasks to models selected for those strengths, and let agents request help from stronger models. That proposal usefully separates agent count from capability diversity, but it remains a design hypothesis: the source offers no completed routing system, comparison with a single strong model, or quality-adjusted cost result.

Zhu327 adds a task-topology case between a role-based team and model router. A large requirement is converted into a product document, then split into vertical issues with explicit dependencies so several subagents can implement independent slices in parallel. The intended reliability gain comes from smaller local context and clearer interfaces, not concurrency alone; human QA and code review return findings to the issue board, while architecture and abstraction remain human design responsibilities. This supports dependency-aware decomposition as a practical Agent Team input, but the source reports no task graph, integration-failure rate, elapsed-time comparison, or controlled single-agent baseline.

## Key Claims
- Agent teams are most useful when a project is too large for one context window and can be split into roles or dependency-aware vertical tasks with explicit interfaces.
- Role separation and heterogeneous routing can assign architecture, UI, logic, review, search, or small tasks to models chosen for capability and cost, but routing quality must be demonstrated rather than assumed.
- File-system state and issue boards can serve as shared coordination substrates, while a desktop or mobile control surface can expose concurrent workspaces, reviews, dependencies, and resource state to the operator.
- ADRs, specs, roadmaps, test plans, and CI status prevent decision loops between agents.
- Milestone boundaries are natural points to restart agents and reload durable project state.
- Agent teams need explicit consensus and verification mechanisms because prompt interpretation is structurally underspecified.
- A coding-agent/review-agent pair is a lightweight role split, but role labels alone do not establish independent or effective verification.

## Evidence
- Role design: [[yong-claude-code-jiang-san-wan-hang-go-xiang-mu-yi-zhi-dao-rust-agent-team-shi-jian-yu-harness-xiao-lu-you-hua]] assigns PM and Engineer to Sonnet, Architect to Opus, and QA to Haiku.
- File ownership: [[yong-claude-code-jiang-san-wan-hang-go-xiang-mu-yi-zhi-dao-rust-agent-team-shi-jian-yu-harness-xiao-lu-you-hua]] maps PM to `vision.md` and `roadmap.md`, Architect to gap analysis and ADRs, QA to test plans and CI status, and shared specs plus `CLAUDE.md` to the team.
- Decision hierarchy: [[yong-claude-code-jiang-san-wan-hang-go-xiang-mu-yi-zhi-dao-rust-agent-team-shi-jian-yu-harness-xiao-lu-you-hua]] states that ADRs determine architecture, specs fill details, and test plans verify specs.
- Milestone reset: [[yong-claude-code-jiang-san-wan-hang-go-xiang-mu-yi-zhi-dao-rust-agent-team-shi-jian-yu-harness-xiao-lu-you-hua]] records a memory requiring all teammates to shut down and respawn at milestone completion.
- Consensus limit: [[duo-agent-xie-zuo-ben-zhi-shi-fen-bu-shi-xi-tong-wen-ti-mo-xing-duo-qiang-ye-mei-yong]] argues that parallel agents must converge on one compatible interpretation of an underspecified prompt.
- Verification topology: [[duo-agent-xie-zuo-ben-zhi-shi-fen-bu-shi-xi-tong-wen-ti-mo-xing-duo-qiang-ye-mei-yong]] says decomposition can reduce incoherence while increasing omissions, so agent teams need both local and global gates.
- Lightweight pairing: [[xiang-zuo-xiang-you-leetao]] reports using one CLI agent to write code and another to review a recent commit through Telegram.
- Orchestration interface: [[agent-shi-dai-de-clice]] shows inspected desktop and mobile views with multiple workspaces, agents, branches, pull requests, resource status, and review output.
- Human boundary: [[agent-shi-dai-de-clice]] says multiple agents can implement and cross-review while the developer continues to provide context and control the system architecture.
- Heterogeneous routing proposal: [[sui-shi-sui-di-zhi-hui-ni-de-agent-tuan-dui-leon7hao]] proposes a leader that decomposes intent, assigns work by model strength and cost, permits inter-agent help, and automates verifiable steps.
- Shared context surface: [[sui-shi-sui-di-zhi-hui-ni-de-agent-tuan-dui-leon7hao]] proposes versioned local-first decisions, conversations, designs, and code history as inherited team context.
- Dependency-aware work graph: [[ai-harness-engineering]] converts a requirements conversation into a product document and vertically sliced issues whose dependencies determine which subagents can work concurrently.
- Human integration boundary: [[ai-harness-engineering]] keeps architecture, abstraction, QA, code review, and issue creation around parallel implementation rather than treating subagent completion as delivery.

## Counterevidence & Qualifications
The large case-study source explicitly says Agent Team is not always worth the overhead. It is less suitable for small projects under roughly 5,000 lines, exploratory prototypes, or projects without test infrastructure, because the role and document structure can become heavier than the work itself. The distributed-systems source adds that coordination mechanisms improve practical outcomes but cannot guarantee safety, liveness, and fault tolerance in every asynchronous failure scenario. Kuafu, clice, and Zhu327 provide unmeasured first-person reports; reviewers using similar models, context, or mistaken requirements may reproduce rather than catch the writer's errors, and no source demonstrates that more agents independently reduce defects. Zhu327's dependency-aware issue flow supplies no graph, concurrency level, integration-failure count, elapsed-time comparison, or single-agent baseline. Lody's heterogeneous routing, context inheritance, and automated verification loop are roadmap claims partly motivated by a secondhand homogeneous-agent paper and a speculative tenfold speedup premise, not comparative evidence.

## What Changed
- Added dependency-aware vertical issue decomposition as an alternative to long-lived role decomposition.
- Added issue-board feedback and human integration judgment as explicit boundaries around parallel subagent work.
- Preserved the qualification that smaller context and concurrency are plausible mechanisms, not measured proof of faster or more reliable delivery.

## Related Concepts
- [[AIAgentCollaboration]] - Agent Team is a structured, multi-agent form of collaboration.
- [[AICodingPractice]] - agent teams require disciplined engineering norms to stay reviewable.
- [[HarnessEngineering]] - role files, specs, and tests are part of the harness that makes an agent team usable.
- [[LLMContextManagement]] - role separation and milestone respawn manage context pressure.
- [[SpecDrivenAgentDevelopment]] - specs are the interface between Agent Team roles.
- [[SoftwareVerification]] - QA and CI supply the validation boundary for Agent Team output.
- [[DistributedConsensus]] - agent teams must converge on a shared prompt interpretation.
- [[TrustTopology]] - heterogeneous gates help make multi-agent output reliable.
- [[AgentComputerInterface]] - orchestration dashboards are human control surfaces around agent work rather than proof of reliable coordination.
- [[Lody]] - product and roadmap case combining cross-device control, worktree isolation, shared context, and heterogeneous routing.
- [[LocalFirstSoftware]] - proposed team context remains locally owned while synchronizing across devices and collaborators.
- [[VerificationDrivenAgentDelegation]] - executable acceptance and human escalation determine which decomposed tasks can proceed concurrently.

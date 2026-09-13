---
title: "Harness Engineering"
type: concept
tags: [ai, software-engineering, agents]
sources:
  - wei-shen-me-ni-de-ai-you-xian-zhan-lue-ke-neng-da-cuo-te-cuo
  - wei-shen-me-xian-you-de-agent-infra-wu-fa-zhi-cheng-sheng-chan-ji-ying-yong
  - yong-claude-code-jiang-san-wan-hang-go-xiang-mu-yi-zhi-dao-rust-agent-team-shi-jian-yu-harness-xiao-lu-you-hua
  - agent-shi-dai-de-tdd-zhi-guan-zhu-xing-wei-de-can-cha
last_updated: 2026-09-13
knowledge_schema: synthesis-v1
---

## Definition
[[HarnessEngineering]] is the practice of building the scaffolds, constraints, runtime boundaries, feedback signals, and validation systems that allow AI agents to perform useful work reliably.

## Current Synthesis
The sources use harness engineering to name a shift in engineering work: when agents can generate code or operate external systems, the scarce skill becomes designing the environment in which they operate. At the software-workflow layer, that environment includes repository architecture, structured tasks, deterministic CI/CD, review gates, tests, feature flags, logs, metrics, triage loops, and rollback mechanisms. The production-agent source adds a runtime layer: effect logs, capability gateways, scoped credentials, and forkable checkpoints are also harnesses because they make model errors predictable, bounded, and recoverable.

The mihomo-rust case study adds a project-local harness layer. For coding agents, the harness can include `CLAUDE.md`, role-owned docs, ADRs, specs, test plans, milestone resets, narrow feedback memory, and explicit state documents. These artifacts make large-agent work repeatable by moving durable state out of fragile conversation context and into reviewable files.

Harness engineering can also be a smaller workflow discipline: keep either the implementation or the test suite fixed, then let the agent self-correct against the side that did not move. Deterministic execution, snapshot baselines, and a core/regression test split turn behavior into a cheap feedback surface, so human attention goes to residual diffs and core expectations instead of every generated artifact.

## Key Claims
- Harness engineering treats agent failure as a scaffold problem rather than a prompt-effort problem.
- The more system state agents can inspect, validate, and modify, the more useful leverage they provide.
- Monorepos or unified architecture can improve agent reasoning by making cross-system effects visible.
- Deterministic pipelines let agents and humans reason about failures consistently.
- Observability and structured logs are part of the agent work environment, not only human operations tools.
- Feature flags, A/B tests, rollback, triage loops, concise project instructions, specs, role documents, memory rules, milestone resets, deterministic tests, and snapshot baselines turn agent work into a controlled cycle.
- High-permission agents also need runtime harnesses for side effects, capabilities, and resumability.

## Evidence
- Failure framing: [[wei-shen-me-ni-de-ai-you-xian-zhan-lue-ke-neng-da-cuo-te-cuo]] says the response to AI errors should be to ask what capability or constraint the agent lacked.
- Inspectable system state: [[wei-shen-me-ni-de-ai-you-xian-zhan-lue-ke-neng-da-cuo-te-cuo]] argues that fragmented repositories are opaque to agents, while unified architecture lets them reason across the whole system.
- Pipeline determinism: [[wei-shen-me-ni-de-ai-you-xian-zhan-lue-ke-neng-da-cuo-te-cuo]] describes a six-stage deployment pipeline with type checks, linting, unit tests, integration tests, Docker builds, Playwright tests, and environment checks.
- Observability: [[wei-shen-me-ni-de-ai-you-xian-zhan-lue-ke-neng-da-cuo-te-cuo]] emphasizes structured CloudWatch logs, alarms, custom metrics, Sentry errors, and AI-readable signals.
- Feedback loop: [[wei-shen-me-ni-de-ai-you-xian-zhan-lue-ke-neng-da-cuo-te-cuo]] describes daily health summaries, automatic issue triage, duplicate detection, regression reopening, post-deploy verification, and automatic ticket closure.
- Release controls: [[wei-shen-me-ni-de-ai-you-xian-zhan-lue-ke-neng-da-cuo-te-cuo]] describes feature flags, staged rollout, A/B testing, one-click disablement, and circuit-breaker rollback.
- Runtime boundaries: [[wei-shen-me-xian-you-de-agent-infra-wu-fa-zhi-cheng-sheng-chan-ji-ying-yong]] argues that production agents need [[EffectLog]], [[CapabilityGateway]], and [[ForkRecovery]] so real side effects and credentials remain bounded across crashes and attacks.
- Project-local harness: [[yong-claude-code-jiang-san-wan-hang-go-xiang-mu-yi-zhi-dao-rust-agent-team-shi-jian-yu-harness-xiao-lu-you-hua]] shows `CLAUDE.md`, ADRs, specs, test plans, state documents, and feedback memory coordinating a large [[ClaudeCode]] port.
- Residual harness: [[agent-shi-dai-de-tdd-zhi-guan-zhu-xing-wei-de-can-cha]] uses fixed implementation during test writing, fixed tests during implementation, deterministic outputs, and snapshots to make agent feedback cheap.

## Counterevidence & Qualifications
The AI-first source presents harness engineering through one company's reported practice and the article's interpretation of an OpenAI term. The agent-infrastructure source is also a design argument rather than a validated standard. The residual-testing source is likewise a practitioner workflow proposal. Together they do not prove that every team should adopt monorepos, AI review gates, fully automated triage, effect logs, capability gateways, or snapshot-heavy regression immediately; the payoff depends on product risk, agent autonomy, permission scope, test quality, architecture, observability maturity, determinism, and tolerance for organizational disruption.

## What Changed
- Expanded harness engineering from software-delivery scaffolds into runtime boundaries for high-permission production agents.
- Added project-local coding-agent harnesses: concise instructions, file-backed state, specs, memory, milestone respawn, and layered tests.
- Added residual-focused testing as a lightweight harness for reducing agent verification and review cost.

## Related Concepts
- [[AIFirstEngineering]] - harness engineering is the enabling discipline for AI-first software workflows.
- [[SoftwareVerification]] - test and deployment harnesses are key parts of the agent scaffold.
- [[LLMContextManagement]] - both make useful information visible to AI systems, though this page focuses on engineering workflow rather than prompt context.
- [[AICodingPractice]] - harnesses operationalize responsible agent use at team scale.
- [[PRReviewHygiene]] - automated review and merge queues are part of the broader review harness.
- [[InferenceLoadBalancing]] - both are systems-engineering responses to AI workloads, but at different layers.
- [[ProductionAgentInfrastructure]] - production agent infrastructure is a runtime form of harness engineering.
- [[CapabilityGateway]] - capability gateways enforce the capability side of an agent harness.
- [[EffectLog]] - effect logs make side effects inspectable and recoverable inside the harness.
- [[AgentTeam]] - role separation is one concrete harness pattern for large coding-agent work.
- [[SpecDrivenAgentDevelopment]] - specs and ADRs turn the harness into agent-readable interfaces.
- [[AgentTDDResidual]] - alternates stable sides of the codebase so the harness exposes behavior residuals.
- [[SnapshotTesting]] - stores broad behavior baselines as a cheap feedback surface.
- [[DeterministicTesting]] - makes that feedback surface stable enough for agent self-correction.

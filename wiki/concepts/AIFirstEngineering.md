---
title: "AI-First Engineering"
type: concept
tags: [ai, software-engineering, engineering-process]
sources:
  - wei-shen-me-ni-de-ai-you-xian-zhan-lue-ke-neng-da-cuo-te-cuo
  - wei-shen-me-xian-you-de-agent-infra-wu-fa-zhi-cheng-sheng-chan-ji-ying-yong
  - ting-de-shi-hou-quan-dong-yi-dong-bi-quan-fei-gui-gu-xu-lao-shi-da-shi-ke-shang-de-eq-tq-iq
  - modern-engineering-values
  - the-coding-agent-is-dead
last_updated: 2026-10-18
knowledge_schema: synthesis-v1
---

## Definition
[[AIFirstEngineering]] is an engineering operating model that redesigns planning, implementation, verification, deployment, runtime control, knowledge placement, and team responsibility around AI agents as primary execution systems.

## Current Synthesis
AI-first engineering is a workflow and organization redesign rather than a coding-tool upgrade. The bounded evidence converges on a layered model: humans select goals, encode product and architectural judgment, define ownership boundaries, and accept outcomes; repositories concentrate durable context; deterministic tests, linting, CI/CD, observability, feature flags, rollback, and fast tooling constrain implementation; production runtimes additionally isolate capabilities, log side effects, and recover long-running work safely.

The sources disagree less about whether agents can write code than about the strength and location of controls. CREAO's reported workflow places agents across implementation, review, deployment, monitoring, and triage. Nakazawa's project account similarly reports broad delegation, but keeps planning, review, taste, domain expertise, and risk-sensitive acceptance with the human. Mai Yang's factory-electrification analogy warns that inserting AI into inherited rituals can automate waste, while her outcome test asks whether local speed improves a customer or business result. Guanlan adds the runtime boundary: ordinary CI and code sandboxes do not safely govern long-running agents with credentials and irreversible side effects.

Amp makes the constraint shift explicit from the product side: as coding models become capable through many competent wrappers, repository organization and organizational use become the differentiators. Its decision to withdraw editor extensions in favor of a CLI embodies a move from synchronous sidebar assistance toward work that can continue outside the editor. This is a directional company bet, not evidence that wrapper quality, editor context, or supervision has ceased to matter.

The organizational implication is conditional. Cheap implementation can favor smaller ownership units and make core-stack ownership more economical, but coordination, maintenance, security, and dependency costs do not disappear. The best fit remains work with explicit goals, fast measurable feedback, clean architecture, and reversible delivery; UI-dense, safety-critical, regulated, or weakly observable systems need stronger human and runtime gates.

## Key Claims
- AI-first engineering redesigns the whole delivery system around agent execution and real outcomes rather than adding AI to inherited steps or treating the agent interface as the durable source of advantage.
- Human value shifts toward goal selection, domain ownership, architecture, taste, risk judgment, and acceptance as implementation becomes cheaper.
- Repository-local specifications, principles, commands, and product context reduce repeated context loss for both agents and people.
- Strict automated guardrails and fast scalable feedback loops determine whether agent speed becomes useful throughput or rapid error production.
- Long-running high-permission agents require capability isolation, durable effect records, and resumable execution beyond ordinary CI/CD and sandboxes.
- Small teams and selective core-stack ownership can gain leverage from agents, but only when their coordination and lifecycle costs remain supportable.
- Adoption should be judged by product, customer, reliability, and business outcomes rather than commits, lines changed, or local task speed alone.

## Evidence
- Workflow and outcome redesign: [[wei-shen-me-ni-de-ai-you-xian-zhan-lue-ke-neng-da-cuo-te-cuo]] places agents across the delivery lifecycle, while [[ting-de-shi-hou-quan-dong-yi-dong-bi-quan-fei-gui-gu-xu-lao-shi-da-shi-ke-shang-de-eq-tq-iq]] distinguishes process redesign from automating inherited steps and requires outcome ownership.
- Human judgment and ownership: [[modern-engineering-values]] reports that broad agent implementation moves the bottleneck toward product judgment, review, domain context, and taste.
- Repository context: [[modern-engineering-values]] argues that code, specifications, architecture, values, and operational knowledge should be colocated because each agent session resembles a new contributor with incomplete context.
- Guardrails and feedback: [[wei-shen-me-ni-de-ai-you-xian-zhan-lue-ke-neng-da-cuo-te-cuo]] lists tests, CI/CD, feature flags, monitoring, task granularity, and architecture; [[modern-engineering-values]] adds changed-file scalability and test-first bug diagnosis.
- Production runtime boundary: [[wei-shen-me-xian-you-de-agent-infra-wu-fa-zhi-cheng-sheng-chan-ji-ying-yong]] requires [[EffectLog]], [[CapabilityGateway]], [[ForkRecovery]], and [[AgentResumability]] for high-permission side-effecting work.
- Team and stack design: [[modern-engineering-values]] proposes small explicit ownership units and re-evaluating third-party dependencies when agent labor lowers implementation cost.
- Context fit: [[wei-shen-me-ni-de-ai-you-xian-zhan-lue-ke-neng-da-cuo-te-cuo]] favors backend-heavy, measurable, internal-tool, and early-stage work over UI-dense or safety-critical domains.
- Constraint shift: [[the-coding-agent-is-dead]] argues that capable coding models make repository organization and organizational adoption more limiting than prompts or tool wrappers, and uses Amp's editor-extension shutdown as its product-level response.

## Counterevidence & Qualifications
The evidence is practitioner-led rather than comparative organizational research. CREAO's transformation and Nakazawa's quality and productivity claims are self-reported; commits and changed lines do not establish customer value, maintainability, safety, or sustainable pace. Amp's wrapper-commoditization claim is promotional and unsupported by named-model, task, migration, security, or outcome comparisons. The electrification analogy does not identify the right redesign for a particular company, and some reliability, compliance, accessibility, learning, or option-value work lacks an immediate revenue line. Small repositories and direct-to-main workflows can increase cross-system coordination or governance risk. Owning more of a stack can improve control while adding maintenance, security, compatibility, and staffing burdens. Finally, strong code-level verification remains insufficient when agents hold credentials or cause irreversible effects, and even semantic runtime controls cannot prove that the human goal or product decision was correct.

## What Changed
- Added repository-local context as shared human-agent infrastructure.
- Added explicit ownership boundaries, small-team coordination, and selective stack ownership to the operating model.
- Added risk-sensitive review and changed-file feedback speed as practical control surfaces.
- Tightened the measurement boundary between implementation activity and product or business outcomes.
- Added the product-level claim that repository and organizational design can become more differentiating than the coding-agent wrapper as model capability rises.

## Related Concepts
- [[HarnessEngineering]] - provides the instructions, tools, constraints, and feedback scaffolds used by AI-first workflows.
- [[AICodingPractice]] - governs individual planning, delegation, review, verification, and learning inside the wider operating model.
- [[SoftwareVerification]] - supplies deterministic behavioral evidence and release gates for generated changes.
- [[LLMContextManagement]] - determines which repository and task information reaches an agent at the right time.
- [[ProductionAgentInfrastructure]] - adds capability, side-effect, recovery, and audit controls for autonomous production work.
- [[EngineeringManagerRoleDesign]] - allocates technical leadership, domain knowledge, and people responsibility under increased agent leverage.
- [[DeveloperExperience]] - fast, scalable tooling controls the latency of agent feedback and correction.

---
title: "Vibe Coding 时代的角色与架构"
type: source
tags: [ai, software-engineering, vibe-coding, product-development]
date: 2026-07-04
source_file: /mnt/ken_personal_wiki/Articles/vibe-coding.md
---

## Summary
[[RORIRI]] argues that [[VibeCoding]] changes code-production speed without removing the ordered reasoning, evidence, architecture, and accountability required to build sustainable products. The proposed response is to reinvest saved implementation time in real user research, low-fidelity prototyping, explicit specifications, documentation, tests, review, executable constraints, and [[TechnicalDebt]] reduction rather than treating faster generation as proof of faster delivery.

## Key Claims
- Product development is a dependency stack: problem and user definition shape experience and information design, which in turn constrain engineering architecture; changes nearer the foundation therefore have a wider blast radius.
- Faster code generation can accelerate architectural decay because every implementation adds dependencies and maintenance surface, so AI-assisted throughput is not automatically delivery throughput.
- LLMs can organize interviews, classify observations, compare records, and critique research artifacts, but cannot substitute for contact with real users or supply lived experience and genuine empathy.
- Teams should move from evidence-backed personas and Epics through User Stories, Job Stories, journey maps, prototypes, user feedback, architecture, implementation, and layered verification rather than jumping from an idea directly to code.
- Model choice should be based on recurring performance in the team's own tasks, with provider diversity used to expose blind spots; public benchmarks and one model version do not settle local fit.
- Agent quality benefits from durable standards, precise and falsifiable language, hooks and linters for machine-detectable failures, memory for recurring qualitative errors, tests, and documentation that records current intent rather than superseded implementation history.
- Multi-agent development can separate planning, implementation, and review contexts, but it needs explicit review criteria, persistent artifacts, failure handling, and protection against fabricated success or documentation drift.
- Agile discovery and delivery may proceed in parallel across a team, but an individual feature still requires the problem space and product risks to be understood before a technical solution is treated as complete.
- Humans remain responsible for problem definition, direction, quality judgment, accountability, and the consequences of deploying software even when models perform most implementation work.

## Key Quotes
> “Vibe Coding 省下来的时间应当被用来清理一切可能的历史债务” - on reinvesting generation speed in maintainability.

> “人的价值在于提出好问题” - on the human role after implementation becomes cheaper.

## Connections
- [[RORIRI]] - author of the lifecycle, architecture, and human-responsibility argument.
- [[VibeCoding]] - central practice whose speed and role claims the source qualifies.
- [[TechnicalDebt]] - architectural decay is presented as the main nonlinear cost of unchecked generation.
- [[SpecDrivenAgentDevelopment]] - requirements, architecture notes, review records, and phase artifacts coordinate agent work.
- [[AgileSoftwareDevelopment]] - discovery and delivery remain distinct but coordinated tracks.
- [[HumanCodeResponsibility]] - people retain decision authority and accountability for generated systems.
- [[UserJourneyMapping]] - journey maps connect observed user experience to product opportunities and measures.
- [[UserTesting]] - prototypes should be iterated with users before implementation hardens assumptions.
- [[AgentTeam]] - planning, implementation, and review are separated to protect context and judgment.
- [[SoftwareVerification]] - unit, integration, and end-to-end tests are mandatory quality boundaries.
- [[DeveloperDocumentation]] - durable technical, case, requirement, and review records preserve intent and auditability.

## Contradictions
- The source directly qualifies productivity-centered [[VibeCoding]] accounts: faster output may bring an unmaintainable architecture threshold forward unless research, design, repair, and verification capacity rise with it.
- Its sequential product-development model tensions improvisational prototype-first practice, but the source still endorses rough prototypes and iteration; its stronger claim is that hypotheses must be tested before architecture and code are mistaken for validated value.
- The claims about model empathy, provider diversity, cumulative multi-agent approval, documentation taxonomies, and specific lint rules are practitioner prescriptions without comparative defect, throughput, cost, or user-outcome measurements.

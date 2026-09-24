---
title: "我做系统架构的一些原则"
type: source
tags: [software-architecture, api, reliability, technical-debt, technology-selection]
date: 2021-12-21
source_file: /mnt/ken_personal_wiki/Articles/我做系统架构的一些原则 酷 壳 - CoolShell.md
---

## Summary
[[ChenHao]] presents eleven practitioner principles for complex-system architecture, arguing that architecture should be judged by team throughput, service stability, and reduced human, time, and financial cost rather than by technical novelty. The article connects a service-and-API viewpoint with mature technology, completeness before optimization, standards, operability, centralized control-plane capabilities, technical-debt repayment, evidence-based decisions, root-problem discovery, and bounded experimentation. Its strongest prescriptions are useful as an operating framework, while its near-default endorsement of Java is broader than the evidence supplied and conflicts with the wiki's context-first approach to technology selection.

## Key Claims
- Architecture has value only when it improves delivery flow, system stability, or total cost; technology is a means rather than the objective.
- Teams should reason from application services and external APIs across development and operations instead of optimizing isolated resources or components.
- Mature, globally adopted technologies and standards usually lower long-term ecosystem, staffing, interoperability, and maintenance risk, but choices still need workload and organizational context.
- Completeness and recoverable constraints should precede performance shortcuts: relational integrity can be loosened or supplemented later, whereas reconstructing lost invariants is difficult.
- Shared API, naming, logging, monitoring, configuration, middleware, and version conventions make automation, observability, retries, circuit breaking, and organizational scaling more tractable.
- Extensibility and operability require loose service coupling plus centralized control capabilities for traffic, service governance, telemetry, deployment, resources, and middleware.
- Legacy debt should be repaid or isolated behind an anti-corruption layer rather than allowed to lower the design quality of new systems.
- Architecture decisions should use diagnostic data, comparative research, and the original problem behind a proposed solution; exploration is valuable when it is deliberate rather than novelty-driven.

## Key Quotes
> “关注于真正的收益而不是技术本身” - on judging architecture by outcomes.

> “千万要小心 X-Y 问题，要追问原始需求” - on diagnosing the underlying problem before selecting a solution.

## Connections
- [[ChenHao]] - author drawing the principles from more than twenty years of architecture work.
- [[SystemArchitecturePrinciples]] - synthesis of the article's benefits, standards, completeness, operability, debt, evidence, and experimentation rules.
- [[ContextualTechnologySelection]] - the article combines a preference for mature mainstream tools with research, diagnosis, and fit, but overgeneralizes Java as a default.
- [[APIErrorHandling]] - HTTP status semantics are used to show how standards enable monitoring and automated recovery behavior.
- [[SystemReliability]] - stability, planned and unplanned downtime, degradation, and operability are treated as architecture outcomes.
- [[ServiceObservability]] - logs, metrics, traces, probes, and centralized correlation are part of the proposed control plane.
- [[TechnicalDebtTracking]] - visibility supports debt decisions, while this source emphasizes repayment or isolation rather than passive accommodation.
- [[SoftwareEngineering]] - architecture is framed as part of the wider work of delivery, maintenance, operations, and cost control.

## Contradictions
- The claim that Java is usually the only safe choice for a growing complex system conflicts with [[ContextualTechnologySelection]], which requires workload, constraints, team capability, alternatives, and disconfirming evidence before choosing a stack. The article partly narrows its own claim to complex systems and acknowledges tradeoffs, while several reader comments dispute its language, resource assumptions, and cloud-native relevance.
- The article calls Zipkin the underlying implementation of Spring Cloud Sleuth; a technically specific reader comment says Sleuth is an instrumentation abstraction that can export to Zipkin rather than being implemented by the Zipkin server. The wiki records this as an unresolved source-level correction rather than an established contradiction.

---
title: "Advice Process"
type: concept
tags: [decision-making, architecture-governance, team-autonomy, consultation]
sources:
  - blog-andrew-harmel-law-martinfowler-com-scaling-the-practice-of-architecture-conversationally
last_updated: 2026-09-25
knowledge_schema: synthesis-v1
---

## Definition
The [[AdviceProcess]] is a distributed decision rule: anyone may make an architectural decision after seeking advice from everyone meaningfully affected and from people with relevant expertise.

## Current Synthesis
The process separates consultation from approval. Decision-takers must seek, listen to, and record advice, including dissent, but they are not required to reach consensus or follow every recommendation. Decision ownership and accountability therefore remain with the person or team experiencing the need.

Consultation scope doubles as a sizing signal. A long list of affected parties indicates a large blast radius and may lead the decision-taker to abandon, narrow, or split a proposal into smaller decisions. Actively seeking people likely to disagree improves exposure to blind spots without giving every advisor veto power.

The rule depends on supporting infrastructure. [[ArchitectureDecisionRecords]] preserve the advice and response; an [[ArchitectureAdvisoryForum]] makes relevant experts and affected teams easier to reach; principles and the [[TechnologyRadar]] supply shared context. Without inclusive participation and genuine decision ownership, the process can degrade into approval theater or shadow centralization.

## Key Claims
- Architectural authority and accountability can sit with the person or team that needs the decision.
- Affected people and relevant experts must be consulted, but consultation does not imply consensus or veto.
- Recording advice and the decision-taker's response makes dissent and reasoning inspectable.
- Consultation breadth reveals decision size and encourages narrower decisions when coordination cost is high.
- Deliberately seeking disagreement can improve learning and surface blind spots.
- The process requires trust, inclusion, and protection from covert override by senior architects.

## Evidence
- Rule and qualifier: [[blog-andrew-harmel-law-martinfowler-com-scaling-the-practice-of-architecture-conversationally]] states that anyone can decide after consulting affected parties and relevant experts.
- Non-consensus boundary: [[blog-andrew-harmel-law-martinfowler-com-scaling-the-practice-of-architecture-conversationally]] requires advice to be heard and recorded but not necessarily accepted.
- Decision sizing: [[blog-andrew-harmel-law-martinfowler-com-scaling-the-practice-of-architecture-conversationally]] says a large advice scope often causes proposals to be reconsidered or subdivided.
- Dissent and learning: [[blog-andrew-harmel-law-martinfowler-com-scaling-the-practice-of-architecture-conversationally]] recommends seeking advisors likely to disagree.

## Counterevidence & Qualifications
The source reports better, faster, and more accountable decisions from experience but supplies no comparative measurements. Consultation may create coordination overhead, and identifying every meaningfully affected person is itself a judgment vulnerable to blind spots and power structures. Advice without veto can also leave affected groups exposed unless cross-functional requirements, escalation paths, and organizational safeguards define non-negotiable constraints.

## What Changed
- Created the concept from the article's core decision-making rule and consultation qualifier.

## Related Concepts
- [[DecentralizedArchitectureGovernance]] - uses the Advice Process as its core decision mechanism.
- [[ArchitectureDecisionRecords]] - record advice, options, consequences, and the final decision.
- [[ArchitectureAdvisoryForum]] - provides a recurring venue for multi-party advice.
- [[ArchitectureAlignmentForces]] - helps interpret consultation scope and organizational distance.
- [[PsychologicalSafety]] - makes disagreement and admission of uncertainty safer.

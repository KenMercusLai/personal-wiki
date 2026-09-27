---
title: "Algorithmic Bias"
type: concept
tags: [artificial-intelligence, fairness, data, governance]
sources:
  - exclusive-ideos-plan-to-stage-an-ai-revolution
last_updated: 2026-09-27
knowledge_schema: synthesis-v1
---

## Definition
[[AlgorithmicBias]] is systematic disparity or distortion in an algorithmic system's inputs, objectives, operation, or outcomes that unfairly advantages, disadvantages, misrepresents, or burdens people or groups.

## Current Synthesis
The article rejects the assumption that mathematical form makes an algorithm objective. Bias can enter through historical or unrepresentative data, a poorly framed target, implementation choices, opaque use, institutional conditions, or developers' unexamined assumptions. Its criminal-risk-assessment example is used to argue that teams should investigate foreseeable negative outcomes before deployment.

That anticipatory work is necessary but incomplete. A system can satisfy stated user needs and still enforce an unjust policy, distribute errors unequally, or hide consequential decisions from affected people. Addressing bias therefore combines participatory inquiry with domain expertise, subgroup evaluation, documentation, monitoring, contestability, and accountable authority over whether and how the system is used.

## Key Claims
- Mathematical and data-driven systems are not automatically objective or trustworthy.
- Bias can arise from data, problem framing, objectives, implementation, deployment context, and institutional power.
- Opacity makes it harder to identify what a system was designed to do and who bears its errors.
- Exploring negative outcomes before deployment can expose foreseeable discrimination and guide redesign.
- Human-centered inquiry is one safeguard, not a complete fairness guarantee.

## Evidence
Objectivity critique:
- [[exclusive-ideos-plan-to-stage-an-ai-revolution]] says numerical foundations lead people to presume AI is trustworthy even though systems can discriminate, undermine institutions, and remain opaque.

Criminal-risk example:
- [[exclusive-ideos-plan-to-stage-an-ai-revolution]] summarizes ProPublica's 2016 reporting on racially biased and inaccurate criminal risk assessments.

Design response:
- [[exclusive-ideos-plan-to-stage-an-ai-revolution]] quotes [[MikeStringer]] arguing that human-centered design should explore possible negative outcomes before an algorithm perpetuates bias.

## Counterevidence & Qualifications
The source summarizes, links to, and interprets external reporting rather than reproducing its methods or the subsequent debate over fairness definitions, base rates, calibration, and error tradeoffs. It provides no tested bias-mitigation process or outcome data from IDEO and Datascope. Bias is also not only a developer-awareness problem: objectives, law, procurement, incentives, deployment practice, data access, and institutional power can preserve harmful disparities despite careful design work.

## What Changed
- Established a multi-stage account of bias spanning data, framing, objectives, implementation, and deployment.
- Positioned anticipatory human-centered inquiry as useful but insufficient without technical and institutional safeguards.

## Related Concepts
- [[HumanCenteredDesign]] - can surface affected people's needs and foreseeable harms before and after deployment.
- [[AugmentedIntelligence]] - requires attention to whose capability is extended and who bears automation errors.
- [[ResponsibleAIRelease]] - governs staged exposure, monitoring, contracts, and downstream accountability for AI systems.
- [[OrganizationalSecrecy]] - opacity and restricted challenge can prevent consequential system failures from being identified or corrected.

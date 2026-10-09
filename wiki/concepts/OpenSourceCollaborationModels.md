---
title: "Open-Source Collaboration Models"
type: concept
tags: [open-source, collaboration, governance, incentives]
sources:
  - dui-kai-yuan-mo-shi-yan-bian-de-yi-xie-xiang-fa-xie-zai-kai-shi-can-yu-kai-yuan-10-nian-hou
last_updated: 2026-10-09
knowledge_schema: synthesis-v1
---

## Definition
[[OpenSourceCollaborationModels]] describes how publicly available software is actually initiated, governed, maintained, changed, and credited, beyond the legal permissions expressed by its license.

## Current Synthesis
[[Inoki]] extends the classic cathedral and bazaar distinction with a third “street-stall” model. A cathedral concentrates planning and implementation among a small group; a bazaar depends on sustained multi-party collaboration and feedback; a street stall is a low-cost repository that an individual can publish, change unpredictably, or abandon with little institutional support. GitHub's low publishing and contribution costs make the third pattern widespread and allow some stalls to mature into organized communities.

These modes are not fixed labels. A bazaar needs stable maintainers, roadmaps, review, and norms, but the same structures can concentrate decision rights, reward insiders, and turn contribution into months of procedural and relational work. It may therefore remain publicly visible while operating internally like many small cathedrals. Conversely, the street-stall mode enables experimentation but offers weak continuity and support guarantees.

The source connects governance to incentive design. Corporate funding and career rewards can sustain work, but product strategy, license changes, contribution counts, and résumé value can redirect behavior away from community needs or unmeasured upstream reasoning. AI adds another possible transition: rapid private generation can strengthen the corporate cathedral while leaving fewer public intermediate artifacts and beginner tasks through which outsiders learn and earn trust.

## Key Claims
- License openness, repository visibility, participation access, and decision authority are distinct dimensions of collaboration.
- Cathedral, bazaar, and street-stall modes describe concentrated planning, sustained distributed governance, and low-commitment individual publication respectively.
- Projects can move between modes, and mature bazaars can become internally cathedral-like as review load, insider norms, and decision scarcity accumulate.
- Maintenance capacity and contribution friction are coupled: stronger quality controls support stability but can also raise entry costs and exhaust both maintainers and contributors.
- Contribution metrics shape behavior by making final PRs more visible than diagnosis, discussion, mentoring, and other upstream work.
- AI acceleration may lower creation cost while centralizing evolution and weakening public learning paths when high-speed work remains private.

## Evidence
- Model taxonomy: [[dui-kai-yuan-mo-shi-yan-bian-de-yi-xie-xiang-fa-xie-zai-kai-shi-can-yu-kai-yuan-10-nian-hou]] contrasts planned cathedrals, stable multi-party bazaars, and casual GitHub street stalls.
- Mode transitions: [[dui-kai-yuan-mo-shi-yan-bian-de-yi-xie-xiang-fa-xie-zai-kai-shi-can-yu-kai-yuan-10-nian-hou]] says stalls can become organizations, while mature communities can acquire hierarchical and exclusionary internal rules.
- Capacity and access: [[dui-kai-yuan-mo-shi-yan-bian-de-yi-xie-xiang-fa-xie-zai-kai-shi-can-yu-kai-yuan-10-nian-hou]] uses Linux maintenance, Asahi Linux, and a driver-patch experience to illustrate review bottlenecks, burnout, and contributor disengagement.
- Incentive effects: [[dui-kai-yuan-mo-shi-yan-bian-de-yi-xie-xiang-fa-xie-zai-kai-shi-can-yu-kai-yuan-10-nian-hou]] contrasts visible PR credit with less visible issue investigation and compares count-driven programs with GSoC's project-and-mentor model.
- AI centralization: [[dui-kai-yuan-mo-shi-yan-bian-de-yi-xie-xiang-fa-xie-zai-kai-shi-can-yu-kai-yuan-10-nian-hou]] argues that private, fast-moving AI-assisted work can erase intermediate documentation and beginner-sized tasks.

## Counterevidence & Qualifications
The taxonomy is a practitioner metaphor, not an empirical classification tested across projects. A small personal repository can be reliable, a corporate-led project can accept meaningful external governance, and a rigorous review process can protect newcomers and users rather than exclude them. The article's cases do not measure how common mode transitions, credit appropriation, maintainer bottlenecks, or AI-driven centralization are. Contribution counts can also aid triage and recognition when interpreted alongside qualitative evidence, while mentorship-based programs introduce subjective selection and evaluation.

## What Changed
- Created a three-mode framework that adds the low-commitment street stall to cathedral and bazaar collaboration.
- Made transitions between collaboration modes, contribution accounting, and AI-driven centralization explicit.

## Related Concepts
- [[OpenSourceProjectMaintenance]] - maintenance capacity determines whether a collaboration mode remains sustainable and accessible.
- [[PublicSoftware]] - distinguishes public visibility and social stewardship from license-defined rights.
- [[OpenSourceCommercialization]] - company funding and value capture can support or reshape project governance.
- [[VibeCoding]] - accelerated code generation changes participation costs, review load, and public learning traces.
- [[WorkplaceLearning]] - newcomers need observable reasoning, documentation, mentorship, and appropriately scoped tasks.
- [[CodeReviewPractice]] - review is both a quality mechanism and a potential participation bottleneck.

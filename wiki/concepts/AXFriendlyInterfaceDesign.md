---
title: "AX-Friendly Interface Design"
type: concept
tags: [ai, agents, ui, interaction-design]
sources:
  - agent-experience-dao-lun-luo-li-li-de-shu-ju-zhong-xin
last_updated: 2026-09-13
knowledge_schema: synthesis-v1
---

## Definition
[[AXFriendlyInterfaceDesign]] is interface design that keeps important state, guidance, constraints, and affordances legible to AI agents as well as human users.

## Current Synthesis
RORIRI argues that several familiar UX patterns become fragile when an agent observes the interface through DOM summaries or screenshots. Hidden help, transient animation, auto-disappearing toasts, and hover-only tooltips may be acceptable or merely annoying for people, but for LLM agents they can be invisible. AX-friendly design therefore favors visible, persistent, semantically summarized defaults for important warnings, diagnostics, and workflow guidance.

## Key Claims
- Hidden interface information often becomes nonexistent information for agents.
- Animation and transient notifications can be missed by screenshot-based Computer Use.
- Tooltip-only guidance is brittle because agents may not know what they do not know and may not hover to discover it.
- DOM or accessibility-tree routes need concise semantic summaries for complex interfaces such as spreadsheet-like grids.
- Screenshot routes need spatially legible, persistent state because the agent sees sampled frames rather than continuous experience.
- Progressive disclosure must be rebalanced when the observer is an agent with limited exploration instincts.

## Evidence
- Animation problem: [[agent-experience-dao-lun-luo-li-li-de-shu-ju-zhong-xin]] says screenshot protocols can miss animated warnings or messages that appear between captures.
- Toast problem: [[agent-experience-dao-lun-luo-li-li-de-shu-ju-zhong-xin]] treats auto-disappearing notifications as unsynchronized with agent screenshot cadence.
- Tooltip problem: [[agent-experience-dao-lun-luo-li-li-de-shu-ju-zhong-xin]] says an agent may not know to hover a help icon before acting.
- Hidden navigation evidence: [[agent-experience-dao-lun-luo-li-li-de-shu-ju-zhong-xin]] cites NN/G and Don Norman's discoverability critique to argue that hidden information was already a human UX problem.
- DOM limitation: [[agent-experience-dao-lun-luo-li-li-de-shu-ju-zhong-xin]] says pure DOM semantics may not reveal spatial relations in Excel-like tables.
- Balance qualification: [[agent-experience-dao-lun-luo-li-li-de-shu-ju-zhong-xin]] says the answer is not dumping every detail onto the screen, but choosing defaults that do not hide valuable guidance.

## Counterevidence & Qualifications
The source is strongest for agents that operate through screenshots, DOM, or accessibility-like summaries. More capable multimodal models, richer UI metadata standards, or agent-specific APIs could reduce some of these constraints without eliminating the need for visible critical state.

## What Changed
- Created the concept page for interface patterns that help agents perceive warnings, state, spatial relations, and workflow guidance.

## Related Concepts
- [[ComputerUse]] - AX-friendly design depends on how agents inspect and act on software.
- [[AccessibilityTree]] - semantic UI structures are one route for exposing state.
- [[AgentInterfaceAsContext]] - persistent visible guidance is one way interfaces deliver context.
- [[ConstraintShapedInterfaceDesign]] - agent observation constraints can shape durable UI conventions.
- [[AgentExperience]] - AX-friendly UI is the design-language layer of Agent Experience.

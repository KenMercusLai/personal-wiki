---
title: "Figma"
type: entity
tags: [design-tool, platform, ecosystem]
sources:
  - zhang-xiaoji-jian-ru-jia-jing-xie-gang-cheng-xu-yuan-de-shu-zi-you-min-zhuan-xing-zhi-lu
  - figma-realtime-editing-of-ordered-sequences
last_updated: 2026-09-28
knowledge_schema: synthesis-v1
---

## Overview
[[Figma]] is a collaborative UI/UX design platform represented here through both its plugin ecosystem and the ordering architecture behind multiplayer document editing.

## Current Profile
Figma functions as both a production-and-distribution platform and a collaborative document system. [[TableToFigma]] and [[FitCurve]] depend on its workflows and marketplace, while Figma's engineering account describes compound objects as ordered child lists edited concurrently across clients. For those bounded lists, the platform chose [[FractionalIndexing]] over [[OperationalTransformation]] because single-value moves and simpler implementation mattered more than non-interleaved concurrent insertion.

## Key Characteristics
- Provides the workflow surface for batch design generation and curve-drawing plugins.
- Offers a plugin marketplace that can expose new tools to early users.
- Appears in the source as a growing ecosystem rather than merely a neutral design app.
- Attracts product opportunities because many designers and adjacent product/development roles use it.
- Applies client edits immediately and relays them through a server while requiring eventual document convergence.
- Orders compound-object children with arbitrary-precision fractional positions so insertion and movement can update one value.

## Evidence
- Workflow surface: [[zhang-xiaoji-jian-ru-jia-jing-xie-gang-cheng-xu-yuan-de-shu-zi-you-min-zhuan-xing-zhi-lu]] describes both [[TableToFigma]] and [[FitCurve]] as Figma plugins.
- Marketplace exposure: [[zhang-xiaoji-jian-ru-jia-jing-xie-gang-cheng-xu-yuan-de-shu-zi-you-min-zhuan-xing-zhi-lu]] says new plugins receive a period of beginner traffic support, with Fit Curve's support lasting about a month.
- Ecosystem growth: [[zhang-xiaoji-jian-ru-jia-jing-xie-gang-cheng-xu-yuan-de-shu-zi-you-min-zhuan-xing-zhi-lu]] includes charts showing Figma rising strongly from 2018 through 2023 and dominating primary UI-design-tool usage.
- Opportunity density: [[zhang-xiaoji-jian-ru-jia-jing-xie-gang-cheng-xu-yuan-de-shu-zi-you-min-zhuan-xing-zhi-lu]] links Figma's designer, developer-mode, and presentation improvements to a larger addressable platform.
- Collaborative state: [[figma-realtime-editing-of-ordered-sequences]] says clients apply edits locally before server relay and may receive concurrent operations in different orders, making convergence the central requirement.
- Ordering choice: [[figma-realtime-editing-of-ordered-sequences]] documents arbitrary-precision string fractions, open interval bounds, server-side duplicate-position repair, and the decision not to use OT for design-object sequences.

## Qualifications
The ecosystem claims rely on survey screenshots and one creator's interpretation; a growing platform still creates dependency on marketplace rules, ranking, and internal demand. The collaboration architecture is a first-party 2017 explanation, not a complete protocol or independent reliability study, and it omits offline reconciliation, transport guarantees, persistence, undo, permissions, and failure measurements.

## What Changed
- Expanded the profile from plugin-platform context to the multiplayer ordering architecture.
- Added the workload-specific choice of fractional indexing over operational transformation.

## Relationships
- [[TableToFigma]] - Figma plugin for data-driven batch design.
- [[FitCurve]] - Figma plugin for smooth curve drawing.
- [[SmallProductPortfolio]] - platform selection shaped two products in the portfolio.
- [[SaaSMarketing]] - marketplace and launch exposure function as acquisition channels.
- [[RealtimeCollaborativeEditing]] - Figma's clients trade immediate local response for a later convergence requirement.
- [[FractionalIndexing]] - position representation selected for ordered design-object children.
- [[OperationalTransformation]] - text-oriented alternative Figma considered and rejected for this workload.

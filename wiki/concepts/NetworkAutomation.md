---
title: "Network Automation"
type: concept
tags: [networking, automation, operations]
sources:
  - adapting-network-design-to-support-automation-ipspace-net-blog
last_updated: 2026-09-13
knowledge_schema: synthesis-v1
---

## Definition
[[NetworkAutomation]] is the use of code, repeatable procedures, and explicit models to configure, operate, or change networks while accounting for the design properties that make those operations practical and safe.

## Current Synthesis
The ipSpace source treats network automation as technically broad but economically constrained. If an operation can be described precisely enough for a computer to execute, it can be automated in principle. In practice, snowflake topologies and organically accumulated exceptions can make the description and implementation cost too high to justify.

The article's strongest design claim is that automation support should be handled like any other network requirement. Simplifying a network or moving toward a spine-and-leaf design can be sensible when it also preserves security, convergence, latency, jitter, and other requirements. It is a mistake to treat automation as a sacred reason to flatten a design regardless of tradeoffs.

The source also makes automation a change-safety problem. Automation code is executable operational knowledge, so it must change with the network; stale automation can fail more violently than stale documentation because it can act directly on infrastructure.

## Key Claims
- Anything that can be specified precisely enough can be automated in principle.
- Automation feasibility depends on the cost of describing and implementing operations, not only on theoretical computability.
- Simpler, more regular network designs lower automation cost when they do not sacrifice other required properties.
- Automation support is a business and design requirement alongside security, convergence, jitter, and reliability.
- Automation code must be kept synchronized with network design to avoid unsafe execution.
- Engineers still need protocol and troubleshooting understanding because automated networks can fail in ways code alone does not explain.

## Evidence
- Automatable scope: [[adapting-network-design-to-support-automation-ipspace-net-blog]] says any operation specified precisely enough can be automated, including messy environments.
- Cost constraint: [[adapting-network-design-to-support-automation-ipspace-net-blog]] argues that describing convoluted operations in snowflake designs can become impractical.
- Design tradeoff: [[adapting-network-design-to-support-automation-ipspace-net-blog]] frames easy-to-automate design as worthwhile only if other network properties are not sacrificed.
- Business requirement framing: [[adapting-network-design-to-support-automation-ipspace-net-blog]] explicitly places automation support beside requirements such as security, fast convergence, and low jitter.
- Operational drift: [[adapting-network-design-to-support-automation-ipspace-net-blog]] warns that network design changes must be synchronized with automation code.
- Skill continuity: [[adapting-network-design-to-support-automation-ipspace-net-blog]] argues that people will still be needed to diagnose automated network crashes until networking is far more commoditized.

## Counterevidence & Qualifications
The source is an opinion essay rather than a comparative study of network topologies or automation tools. It does not claim that spine-and-leaf is wrong; it argues that changing topology solely for automation should be evaluated against the whole requirement set. It also treats career change broadly, so its pay-scale and skill-market comments are directional rather than a detailed labor-market analysis.

## What Changed
- Created the concept to capture network automation as a design requirement with practical cost and change-safety constraints.

## Related Concepts
- [[InfrastructureAsCode]] - both turn operational infrastructure into explicit, repeatable code-backed descriptions.
- [[DeploymentAutomation]] - both require automated changes to be paired with verification and operational judgment.
- [[ChangeSafety]] - stale or poorly scoped automation can create unsafe infrastructure changes.
- [[AutomationFriendlyCLI]] - both treat automation support as a design requirement rather than an afterthought.
- [[SystemReliability]] - reliable networks depend on automation that preserves diagnosability and required service properties.

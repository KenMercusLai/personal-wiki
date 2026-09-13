---
title: "Network Automation"
type: concept
tags: [networking, automation, operations]
sources:
  - adapting-network-design-to-support-automation-ipspace-net-blog
  - ansible-charges-into-network-automation-with-cisco-juniper-the-register
last_updated: 2026-09-13
knowledge_schema: synthesis-v1
---

## Definition
[[NetworkAutomation]] is the use of code, repeatable procedures, and explicit models to configure, validate, operate, or change networks while accounting for the design properties, vendor surfaces, and safety checks that make those operations practical.

## Current Synthesis
The ipSpace source treats network automation as technically broad but economically constrained. If an operation can be described precisely enough for a computer to execute, it can be automated in principle. In practice, snowflake topologies and organically accumulated exceptions can make the description and implementation cost too high to justify.

The article's strongest design claim is that automation support should be handled like any other network requirement. Simplifying a network or moving toward a spine-and-leaf design can be sensible when it also preserves security, convergence, latency, jitter, and other requirements. It is a mistake to treat automation as a sacred reason to flatten a design regardless of tradeoffs.

Tooling and platform coverage make the idea concrete. [[Ansible]]'s network modules use Playbooks for network command, configuration, and templating across named vendors such as [[AristaNetworks]], [[Cisco]], [[Juniper]], [[CumulusNetworks]], and [[OpenSwitch]]. That support list also shows a limit: [[Huawei]] was called out as absent, so "multivendor" coverage still depends on actual platform support.

Network automation is also a change-safety and organizational-translation problem. Automation code is executable operational knowledge, so it must change with the network; stale automation can fail more violently than stale documentation because it can act directly on infrastructure. Ansible's launch framing adds testing, validation of existing state, and continuous compliance against drift as explicit goals, while insisting that network engineers and programmers should collaborate without being forced into identical roles.

## Key Claims
- Anything that can be specified precisely enough can be automated in principle.
- Automation feasibility depends on the cost of describing and implementing operations, not only on theoretical computability.
- Simpler, more regular network designs lower automation cost when they do not sacrifice other required properties.
- Automation support is a business and design requirement alongside security, convergence, jitter, and reliability.
- Automation code must be kept synchronized with network design and concrete platform support to avoid unsafe execution.
- Validation, continuous compliance, and drift checks make network automation part of operational safety rather than only configuration speed.
- Engineers still need protocol and troubleshooting understanding because automated networks can fail in ways code alone does not explain.

## Evidence
- Automatable scope: [[adapting-network-design-to-support-automation-ipspace-net-blog]] says any operation specified precisely enough can be automated, including messy environments.
- Cost constraint: [[adapting-network-design-to-support-automation-ipspace-net-blog]] argues that describing convoluted operations in snowflake designs can become impractical.
- Design tradeoff: [[adapting-network-design-to-support-automation-ipspace-net-blog]] frames easy-to-automate design as worthwhile only if other network properties are not sacrificed.
- Business requirement framing: [[adapting-network-design-to-support-automation-ipspace-net-blog]] explicitly places automation support beside requirements such as security, fast convergence, and low jitter.
- Operational drift: [[adapting-network-design-to-support-automation-ipspace-net-blog]] warns that network design changes must be synchronized with automation code.
- Tool implementation: [[ansible-charges-into-network-automation-with-cisco-juniper-the-register]] says [[Ansible]] 2.0 added core network modules for command, configuration, and templates.
- Vendor support: [[ansible-charges-into-network-automation-with-cisco-juniper-the-register]] names Arista, Cisco, Juniper, Cumulus Networks, and OpenSwitch as supported at launch, while calling Huawei absent.
- Safety goals: [[ansible-charges-into-network-automation-with-cisco-juniper-the-register]] reports Peter Sprygada's pillars of configuration automation, testing and validation of existing network state, and continuous compliance for configuration drift.
- Role translation: [[ansible-charges-into-network-automation-with-cisco-juniper-the-register]] quotes Sprygada's claim that networking teams can join DevOps practice without becoming programmers.
- Skill continuity: [[adapting-network-design-to-support-automation-ipspace-net-blog]] argues that people will still be needed to diagnose automated network crashes until networking is far more commoditized.

## Counterevidence & Qualifications
The sources are not controlled comparisons of network topologies, automation tools, or vendor module quality. The ipSpace source does not claim that spine-and-leaf is wrong; it argues that changing topology solely for automation should be evaluated against the whole requirement set. The Register source is a launch report, so it captures intent, support claims, and role framing rather than measured adoption, reliability, or later ecosystem coverage.

## What Changed
- Added Ansible's network-module launch as a concrete multivendor implementation case.
- Added validation, continuous compliance, drift detection, and role-translation goals to the current judgment.
- Qualified multivendor automation by noting that platform coverage is explicit and incomplete.

## Related Concepts
- [[InfrastructureAsCode]] - both turn operational infrastructure into explicit, repeatable code-backed descriptions.
- [[DeploymentAutomation]] - both require automated changes to be paired with verification and operational judgment.
- [[ChangeSafety]] - stale or poorly scoped automation can create unsafe infrastructure changes.
- [[AutomationFriendlyCLI]] - both treat automation support as a design requirement rather than an afterthought.
- [[SystemReliability]] - reliable networks depend on automation that preserves diagnosability and required service properties.

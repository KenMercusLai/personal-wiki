---
title: "Network Automation"
type: concept
tags: [networking, automation, operations]
sources:
  - adapting-network-design-to-support-automation-ipspace-net-blog
  - ansible-charges-into-network-automation-with-cisco-juniper-the-register
  - ansible-vs-nornir-speed-challenge
  - enabling-devops-approach-with-cisco-nx-os-and-ansible-cisco-blog
last_updated: 2026-09-27
knowledge_schema: synthesis-v1
---

## Definition
[[NetworkAutomation]] is the use of code, repeatable procedures, and explicit models to configure, validate, operate, collect data from, or change networks while accounting for the design properties, vendor surfaces, performance constraints, and safety checks that make those operations practical.

## Current Synthesis
The ipSpace source treats network automation as technically broad but economically constrained. If an operation can be described precisely enough for a computer to execute, it can be automated in principle. In practice, snowflake topologies and organically accumulated exceptions can make the description and implementation cost too high to justify.

The article's strongest design claim is that automation support should be handled like any other network requirement. Simplifying a network or moving toward a spine-and-leaf design can be sensible when it also preserves security, convergence, latency, jitter, and other requirements. It is a mistake to treat automation as a sacred reason to flatten a design regardless of tradeoffs.

Tooling and platform coverage make the idea concrete. [[Ansible]]'s network modules use Playbooks for network command, configuration, and templating across named vendors such as [[AristaNetworks]], [[Cisco]], [[Juniper]], [[CumulusNetworks]], and [[OpenSwitch]]. That support list also shows a limit: [[Huawei]] was called out as absent, so "multivendor" coverage still depends on actual platform support.

Cisco's contemporary post adds depth beneath one item on that vendor list. For [[CiscoNXOS]] on [[CiscoNexus]], Ansible 2.0 exposed separate command, configuration, and template modules over SSH or NX-API, with linked examples spanning Day 0 provisioning and Day 1/Day 2 operations. The post also treats credential transport as part of automation design: jump-host delegation and managed SSH keys can reduce the need to embed device passwords in configuration files, though this does not establish a complete secrets-management model.

Network automation is also a change-safety and organizational-translation problem. Automation code is executable operational knowledge, so it must change with the network; stale automation can fail more violently than stale documentation because it can act directly on infrastructure. Ansible's launch framing adds testing, validation of existing state, and continuous compliance against drift as explicit goals, while insisting that network engineers and programmers should collaborate without being forced into identical roles.

The Ansible-versus-Nornir benchmark adds a performance dimension to tool fit. [[PatrickOgenstad]] shows that even before touching the network, local inventory, task, template, and data-processing overhead can dominate a workflow. In his test, [[Nornir]] scales from 0.621 seconds at 100 hosts to 17.217 seconds at 10,000 hosts, while [[Ansible]] grows from 18.217 seconds to 41 minutes 22.106 seconds over the same host counts. The result does not make speed the only evaluation criterion, but it does show that scheduled data collection, large inventories, and large command outputs can make automation architecture a practical constraint rather than an implementation detail.

## Key Claims
- Anything specified precisely enough can be automated in principle, but practical feasibility depends on the cost of describing and implementing the operation.
- Simpler, more regular network designs lower automation cost when they do not sacrifice other required properties.
- Automation support is a business and design requirement alongside security, convergence, jitter, and reliability.
- Automation code must be kept synchronized with network design and concrete platform support to avoid unsafe execution.
- Validation, continuous compliance, and drift checks make network automation part of operational safety rather than only configuration speed.
- Useful network automation spans initial provisioning, ongoing configuration, operational commands, transport selection, and credential handling.
- Tool choice and operator skill still matter because large inventories, rendered templates, collected device data, and automated failure modes can exceed what code alone explains.

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
- Cisco implementation: [[enabling-devops-approach-with-cisco-nx-os-and-ansible-cisco-blog]] names separate NX-OS command, configuration, and template modules using SSH or NX-API.
- Lifecycle and credentials: [[enabling-devops-approach-with-cisco-nx-os-and-ansible-cisco-blog]] points to Day 0/1/2 automation and describes jump-host delegation plus SSH-key management.
- Tool-fit benchmark: [[ansible-vs-nornir-speed-challenge]] reports [[Nornir]] completing the 10,000-host local template-generation workload in 17.217 seconds while [[Ansible]] takes 41 minutes 22.106 seconds.
- Data-volume ceiling: [[ansible-vs-nornir-speed-challenge]] says an earlier Ansible playbook collecting IOS XR DHCP binding data from roughly 90 devices could not finish inside a five-minute schedule.
- Chart evidence: [[ansible-vs-nornir-speed-challenge]] includes a shared-axis chart where Ansible's runtimes visually dwarf Nornir and a Nornir-only chart showing approximately linear growth across the tested host counts.
- Skill continuity: [[adapting-network-design-to-support-automation-ipspace-net-blog]] argues that people will still be needed to diagnose automated network crashes until networking is far more commoditized.

## Counterevidence & Qualifications
The sources are not controlled comparisons of network topologies, automation tools, or vendor module quality. The ipSpace source does not claim that spine-and-leaf is wrong; it argues that changing topology solely for automation should be evaluated against the whole requirement set. The Register source is a launch report, and Cisco's companion post is vendor-authored and tied to Ansible 1.9/2.0-era examples, so they capture intent, named interfaces, support claims, and role framing rather than measured adoption, reliability, security, or current ecosystem coverage. The Ogenstad benchmark is a 2019 local templating test using Ansible 2.9.0 and Nornir 2.3.0 on a small dedicated-CPU host, so it should qualify tool fit rather than serve as a universal performance law.

## What Changed
- Added a concrete NX-OS implementation across commands, configuration, templates, SSH, and NX-API.
- Extended lifecycle scope from configuration to Day 0 provisioning and Day 1/Day 2 operations.
- Added authentication routing and key management as part of network-automation design.
- Preserved Ansible's later performance qualification for high-volume local processing.

## Related Concepts
- [[InfrastructureAsCode]] - both turn operational infrastructure into explicit, repeatable code-backed descriptions.
- [[DeploymentAutomation]] - both require automated changes to be paired with verification and operational judgment.
- [[ChangeSafety]] - stale or poorly scoped automation can create unsafe infrastructure changes.
- [[AutomationFriendlyCLI]] - both treat automation support as a design requirement rather than an afterthought.
- [[SystemReliability]] - reliable networks depend on automation that preserves diagnosability and required service properties.

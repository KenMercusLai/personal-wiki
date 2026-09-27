---
title: "Enabling DevOps Approach with Cisco NX-OS and Ansible"
type: source
tags: [networking, automation, devops, nx-os, ansible]
date: 2016-02-15
source_file: "/mnt/ken_personal_wiki/Articles/Enabling DevOps Approach with Cisco NX-OS and Ansible - Cisco Blog.md"
---

## Summary
[[Cisco]] presents [[Ansible]] 2.0 as a practical automation layer for [[CiscoNXOS]] and [[CiscoNexus]] data-center infrastructure. The article points to playbooks and demonstrations spanning Day 0 provisioning through Day 1 and Day 2 operations, while naming NX-OS modules, transports, and credential-handling features that make the claim concrete. Its product-flexibility and security-compliance conclusions are vendor claims from 2016 rather than comparative evidence.

## Key Claims
- Ansible 2.0 added the `nxos_command`, `nxos_config`, and `nxos_template` core modules for Nexus devices.
- The modules could send CLI commands or push configuration files to NX-OS through SSH or NX-API.
- Cisco's linked examples presented Ansible playbooks and demonstrations for Day 0, Day 1, and Day 2 network operations.
- Authentication could be delegated through a jump host, and SSH keys could support passwordless access so passwords did not need to be stored in Ansible configuration files.
- Cisco positioned ACI and do-it-yourself NX-OS deployment as alternatives sharing a common Nexus automation model.
- The event schedules, Ansible 1.9 examples, and Ansible 2.0 feature descriptions are historically bounded to February 2016.

## Key Quotes
> "new Ansible Core modules specific to Nexus devices" - Cisco on `nxos_command`, `nxos_config`, and `nxos_template` in Ansible 2.0.

> "customers don’t need to store passwords in the Ansible configuration files" - Cisco's stated security benefit of delegated authentication and SSH-key management.

## Connections
- [[Cisco]] - vendor publishing the NX-OS and Nexus automation guidance.
- [[Ansible]] - automation platform and module framework described in the article.
- [[CiscoNXOS]] - network operating system automated through commands, configuration files, SSH, and NX-API.
- [[CiscoNexus]] - data-center switching platform targeted by the NX-OS modules and examples.
- [[NetworkAutomation]] - central practice spanning provisioning, configuration, and ongoing operations.
- [[DevOpsCulture]] - organizational framing used for bringing repeatable automation to network operations.
- [[ConfigurationManagement]] - Ansible applies repeatable configuration changes to existing network devices.
- [[ChangeSafety]] - password handling and repeatable playbooks affect the security and reliability of automated changes.

## Contradictions
- No direct contradiction identified. The source adds Cisco-specific implementation detail to the existing Ansible 2.0 launch material, while [[ansible-vs-nornir-speed-challenge]] separately qualifies Ansible's fit for high-volume local processing.

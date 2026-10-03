---
title: "Linux Server Hardening"
type: concept
tags: [linux, security, server, operations]
sources:
  - my-first-5-minutes-on-a-server
last_updated: 2026-10-03
knowledge_schema: synthesis-v1
---

## Definition
[[LinuxServerHardening]] is the reduction of a Linux host's avoidable attack surface through controlled administration, restricted network exposure, timely patching, monitoring, and preserved recovery access.

## Current Synthesis
The source provides a compact first-login sequence rather than a complete security program. Its durable model is layered: update the host; create a named non-root administrator; install public keys; retain a protected recovery route; disable remote root and password authentication; restrict SSH by source address; permit only intended public ports; automate security patches; and review authentication and system activity.

Order matters. Accounts, keys, sudo, recovery credentials, and preferably a second tested session should be in place before SSH is restricted or restarted. The exact 2013 commands should be adapted to the distribution, cloud image, network design, and current access tooling. Maintainability is itself a control: a smaller baseline that is reviewed and tested is more useful than nominally strong configuration that silently drifts or locks out legitimate operators.

## Key Claims
- Host hardening should be a repeatable operating baseline, not a one-time collection of commands.
- Administrative access should identify individual non-root users and prefer public-key authentication over reusable SSH passwords.
- Root-login restrictions, authentication restrictions, source-network policy, and firewall rules provide distinct layers around remote administration.
- Patch currency, automated security updates, login monitoring, and log review complement preventive access controls.
- Recovery access must be designed and tested before restrictive controls are activated.
- Minimal public exposure should follow workload intent; in the source's web-server case, only HTTP and HTTPS are public.

## Evidence
- Maintainable baseline: [[my-first-5-minutes-on-a-server]] frames poor maintenance of otherwise sufficient procedures as a common cause of breaches.
- Administrative identity: [[my-first-5-minutes-on-a-server]] creates a deploy user, installs authorized public keys, grants sudo, and disables SSH root and password login.
- Network layers: [[my-first-5-minutes-on-a-server]] restricts the SSH user by source address and repeats that restriction in UFW while allowing ports 80 and 443.
- Patch layers: [[my-first-5-minutes-on-a-server]] performs an immediate package update and enables unattended security upgrades.
- Detection and review: [[my-first-5-minutes-on-a-server]] installs Fail2ban for suspicious login activity and Logwatch for a daily email digest.
- Recovery boundary: [[my-first-5-minutes-on-a-server]] retains a long root password for loss of SSH or sudo access.

## Counterevidence & Qualifications
The evidence is one 2013 Debian/Ubuntu-oriented practitioner checklist, not a benchmark or current security standard. Exact commands and defaults vary: account creation may need explicit home and shell options; sudoers changes should preserve distribution and automation requirements; fixed-IP allowlists are brittle for dynamic or roaming administrators; and email summaries depend on a configured mail path. Setting a root password may be less safe than leaving root locked when provider-console recovery exists. Fail2ban adds limited protection against SSH password guessing once password authentication is off. The source also omits contemporary provider-level policy, MFA, VPN or identity-aware access, per-user key lifecycle, infrastructure as code, backups, audit configuration, vulnerability management, and rollback testing.

## What Changed
- Created a layered first-login hardening model with explicit sequencing and recovery requirements.
- Separated durable principles from dated, distribution-specific commands.
- Added lockout, root-password, fixed-IP, mail-delivery, and defense-overlap qualifications.

## Related Concepts
- [[ProductionAccessControl]] - defines who may administer the host and through which exceptional path.
- [[RemoteAdministrationExposure]] - narrows the high-impact SSH control surface through authentication and network layers.
- [[DefensivePortTriage]] - verifies that actual listeners and reachability match the intended firewall policy.
- [[StartupSecurityDebt]] - early host defaults can become persistent operational risk if not standardized.
- [[CentralizedLogging]] - extends local daily summaries into shared, searchable incident evidence.

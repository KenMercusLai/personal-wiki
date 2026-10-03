---
title: "My First 5 Minutes On A Server; Or, Essential Security for Linux Servers"
type: source
tags: [linux, security, server, sysadmin]
date: 2013-03-03
source_file: "/mnt/ken_personal_wiki/Articles/My First 5 Minutes On A Server.md"
---

## Summary
[[BryanKennedy]] presents a ten-step [[LinuxServerHardening]] checklist for a newly provisioned Debian- or Ubuntu-like server. The design combines package updates, a non-root deployment account, SSH public-key authentication, disabled remote root and password login, source-IP restrictions, a host firewall, automated security updates, login-attempt blocking, and daily log summaries. Its durable contribution is the layered sequence and recovery awareness, while several exact commands and assumptions are dated, distribution-specific, or operationally brittle.

## Key Claims
- Initial hardening should be a short, repeatable procedure that operators can maintain rather than a complicated policy that decays.
- Remote administration should use a named non-root account and public keys, with direct root login and SSH password authentication disabled.
- SSH exposure can be narrowed further with source-IP restrictions in both OpenSSH and the host firewall.
- Host defense should combine current packages, automatic security updates, firewall rules, login-attempt monitoring, and log review rather than relying on one control.
- Recovery credentials and an alternate access path must exist before restrictive SSH changes are activated.
- The proposed server exposes only HTTP and HTTPS publicly while limiting SSH to known administrative addresses.

## Key Quotes
> "Most security breaches are caused either by insufficient security procedures or sufficient procedures poorly maintained." — the article's case for a maintainable baseline.

> "Developers log in with their public keys, not passwords" — the central administrative-access rule.

## Connections
- [[BryanKennedy]] — author of the server-hardening checklist.
- [[LinuxServerHardening]] — layered baseline synthesized from the article's ten-step sequence.
- [[ProductionAccessControl]] — the deploy account, sudo boundary, public keys, and recovery credential define the administrative path.
- [[RemoteAdministrationExposure]] — disabling root and password login and restricting source addresses reduce the exposed SSH surface.
- [[DefensivePortTriage]] — the UFW rules make intended public and administrative ports explicit.
- [[StartupSecurityDebt]] — a repeatable first-login procedure prevents insecure defaults from becoming operating habits.
- [[CentralizedLogging]] — the local Logwatch digest is a lightweight precursor to the wiki's broader queryable logging model.

## Contradictions
- No direct contradiction with the existing wiki. The source supplies a host-level implementation beneath broader production-access and security-debt principles.
- The checklist is from 2013 and is not a current universal runbook. `useradd deploy` may omit expected home-directory and shell setup; commenting all existing sudo grants can remove necessary distribution or automation access; fixed office-IP allowlists can cause lockout or fail under dynamic addressing; and Logwatch email requires working mail delivery.
- Setting a root password is recovery advice for the source's assumed environment, but some cloud images deliberately keep root password login locked and provide console or provider recovery instead.
- Fail2ban offers less incremental protection against password guessing after SSH password authentication is disabled, although it may still suppress noisy traffic or protect other monitored services.
- The source does not cover modern controls such as provider firewalls, MFA-backed access proxies, VPN or zero-trust administration, configuration management, secure boot, disk encryption, audit policy, backup verification, vulnerability scanning, or tested rollback.

---
title: "Bryan Kennedy"
type: entity
tags: [linux, security, author]
sources:
  - my-first-5-minutes-on-a-server
last_updated: 2026-10-03
knowledge_schema: synthesis-v1
---

## Overview
[[BryanKennedy]] is represented in this wiki as the author of a 2013 checklist for the first minutes of [[LinuxServerHardening]].

## Current Profile
In the bounded source, Kennedy favors a compact, maintainable server-security routine over a complicated regime likely to decay. His design uses a named deployment account, SSH public keys, sudo, root-login and password-login restrictions, source-address filtering, UFW, unattended security updates, Fail2ban, and Logwatch. The source does not provide enough biographical evidence for a broader profile.

## Key Characteristics
- Authors an operator-oriented Linux server-security checklist.
- Emphasizes maintainability as part of security effectiveness.
- Uses layered controls across identity, network exposure, patching, monitoring, and recovery.
- Separates ordinary non-root administration from emergency root recovery.

## Evidence
- Authorship and scope: [[my-first-5-minutes-on-a-server]] presents Kennedy's ten-step first-login procedure for Linux servers.
- Access model: [[my-first-5-minutes-on-a-server]] configures a deploy account with public-key SSH access and sudo while disabling remote root and password login.
- Layered defense: [[my-first-5-minutes-on-a-server]] combines updates, Fail2ban, UFW, unattended security upgrades, and Logwatch.
- Operating philosophy: [[my-first-5-minutes-on-a-server]] attributes many breaches to absent procedures or to adequate procedures that are poorly maintained.

## Qualifications
This profile is restricted to one 2013 article. It does not establish Kennedy's wider biography, later practice, or the present-day suitability of every command in the checklist.

## What Changed
- Created a source-bounded profile centered on the Linux server-hardening checklist.

## Relationships
- [[LinuxServerHardening]] - security practice Kennedy turns into a short operational sequence.
- [[ProductionAccessControl]] - administrative boundary implemented through the deploy account, keys, sudo, and recovery credentials.
- [[RemoteAdministrationExposure]] - risk reduced through SSH authentication and network restrictions.

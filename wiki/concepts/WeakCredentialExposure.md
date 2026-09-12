---
title: "Weak Credential Exposure"
type: concept
tags: [security, authentication, credentials]
sources:
  - chang-yong-duan-kou-li-yong-zong-jie-infvies-blog
last_updated: 2026-09-12
knowledge_schema: synthesis-v1
---

## Definition
[[WeakCredentialExposure]] is the security risk created when externally reachable services can be accessed with guessed, default, reused, blank, or otherwise weak credentials.

## Current Synthesis
The source repeatedly treats weak credentials as a cross-service risk rather than a problem limited to one protocol. Remote shells, file-transfer services, desktop-control tools, database servers, and middleware consoles all become dangerous when authentication can be guessed or defaults remain in place.

This makes credential hygiene a defensive baseline for exposed infrastructure. Strong passwords are not enough by themselves, but weak credentials can collapse other controls because many of the listed services are designed to administer hosts, read data, deploy applications, or execute privileged operations.

## Key Claims
- Weak credentials recur across many network services and should be treated as a systemic exposure class.
- Administrative and remote-control services are especially sensitive to credential weakness.
- Database and middleware consoles can turn credential compromise into data access, application deployment, or command execution.
- Default or blank credentials are distinct from ordinary password weakness because they often come from unsafe initial configuration.
- Brute-force resistance depends on authentication policy, monitoring, rate limits, network placement, and service hardening.

## Evidence
- Cross-service recurrence: [[chang-yong-duan-kou-li-yong-zong-jie-infvies-blog]] labels FTP, SSH, Telnet, POP3, LDAP, Rexec/Rlogin, databases, RDP, VNC, WebLogic, Tomcat/JBoss, WebSphere, Redis, and MongoDB with brute force or weak-password risks.
- Administrative sensitivity: [[chang-yong-duan-kou-li-yong-zong-jie-infvies-blog]] discusses SSH, Telnet, RDP, VNC, pcAnywhere, and Radmin as remote access or remote-control paths.
- Database sensitivity: [[chang-yong-duan-kou-li-yong-zong-jie-infvies-blog]] describes MSSQL, Oracle, MySQL, PostgreSQL, Redis, and MongoDB as credential-exposed data services.
- Default and blank credentials: [[chang-yong-duan-kou-li-yong-zong-jie-infvies-blog]] gives examples such as anonymous FTP and default-like middleware or database credentials.

## Counterevidence & Qualifications
The source names brute force frequently but does not quantify real-world prevalence, lockout behavior, multi-factor authentication, password policy, or rate-limiting controls. Defensive judgment should therefore combine this checklist with actual access logs, authentication configuration, exposure scope, and service-specific hardening guidance.

## What Changed
- Created the concept page for weak credentials as a recurring service-exposure class.

## Related Concepts
- [[DefensivePortTriage]] - port triage uses credential risk as one of its first classification axes.
- [[RemoteAdministrationExposure]] - remote administration services are especially harmed by weak credentials.
- [[DatabaseServiceExposure]] - exposed databases often combine credential risk with data-access impact.
- [[UnauthenticatedServiceExposure]] - both concern access control failure, but unauthenticated exposure removes the credential barrier entirely.
- [[CapabilityGateway]] - both concern access mediation, though capability gateways focus on scoped credentials for agents.

---
title: "An Infrastructure Guide for Founders"
type: source
tags: [aws, infrastructure, security, devops, startups]
date: 2017-10-20
source_file: /mnt/ken_personal_wiki/Articles/An Infrastructure Guide for Founders - Starting Up Security - Medium.md
---

## Summary
[[Magoo]] argues that founding teams moving from proof of concept to AWS production should design security into infrastructure choices before habits harden into debt. The article frames [[StartupSecurityDebt]] as a shared reliability and velocity problem: centralized logs, multiple account planning, controlled production access, infrastructure as code, network segmentation, and secrets management all reduce incident blast radius while improving operations.

## Key Claims
- [[CentralizedLogging]] is an early high-leverage investment because security incidents and availability incidents both need queryable application, system, and cloud-provider logs.
- [[CloudAccountSegmentation]] should be considered early because separate accounts, shared identity, centralized logs, and AWS Organizations can reduce blast radius before later growth makes refactoring painful.
- [[ProductionAccessControl]] should make direct production troubleshooting rare, intentional, logged, and temporary rather than a casual default.
- [[InfrastructureAsCode]] lets infrastructure share normal engineering standards through repositories, review, tests, CI/CD, limited console access, and reduced configuration drift.
- [[NetworkSegmentation]] should expose services intentionally, keeping internal tools, caches, and databases away from public networks and unsafe `0.0.0.0/0` rules.
- [[SecretManagement]] is a priority for early teams because leaked API keys and credentials in repositories, chat, environment variables, or copy-paste buffers are a common root cause of incidents.

## Key Quotes
> "If you don't have a coherent strategy around logging, you will be mostly useless during a security incident." - on why logging design belongs in early infrastructure planning.

> "The highest priority issue is keeping secrets out of repositories, Slack channels, and copy paste buffers, by any means necessary." - on early secrets-management priorities.

## Connections
- [[Magoo]] - author of the security infrastructure guide.
- [[AWS]] - cloud context for the article's account, logging, IAM role, CloudTrail, CloudWatch Logs, VPC, and security-group guidance.
- [[StartupSecurityDebt]] - the source's core frame: predictable cloud incidents often come from long-standing design debt.
- [[CentralizedLogging]] - the recommended default for incident response, troubleshooting, and usage-informed policy decisions.
- [[CloudAccountSegmentation]] - early multi-account planning for blast radius, centralized logs, identity, roles, policies, and billing.
- [[ProductionAccessControl]] - controlled routes for direct production troubleshooting through monitoring, bastions, and temporary access.
- [[InfrastructureAsCode]] - Terraform, CloudFormation, review, tests, and CI/CD are presented as ways to bring engineering discipline to cloud infrastructure.
- [[NetworkSegmentation]] - public/private layout and disciplined security groups prevent accidental exposure of internal services.
- [[SecretManagement]] - source-code, Slack, environment-variable, and laptop-buffer secrets are treated as high-priority security debt.
- [[ServiceObservability]] - centralized logs and monitoring reduce the need for invasive production debugging.
- [[RemoteAdministrationExposure]] - bastions and temporary production access limit the risk of administrative surfaces and stolen credentials.

## Contradictions
- None identified. The source complements existing reliability and infrastructure pages by shifting similar practices earlier in the company lifecycle and framing them as security-debt prevention.

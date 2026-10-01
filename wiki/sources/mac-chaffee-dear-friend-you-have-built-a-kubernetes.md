---
title: "Dear friend, you have built a Kubernetes"
type: source
tags: [kubernetes, infrastructure, containers, devops]
date: 2024-11-23
source_file: "/mnt/ken_personal_wiki/Articles/Mac Chaffee - Dear Friend You Have Built a Kubernetes.md"
---

## Summary
[[MacChaffee]] argues that rejecting [[Kubernetes]] as excessive does not remove the operating problems it addresses. A supposedly simple container setup can accrete a configuration format, deployment and rollback logic, multi-host networking, service discovery, immutable machine configuration, and a restricted control API until the team has assembled an informal orchestrator with weaker standardization, testing, documentation, and maintainership.

## Key Claims
- Docker Compose standardizes container configuration but does not by itself provide deployment, rolling updates, rollback, or scaling.
- Moving from one server to several can add firewall configuration, an overlay network, and service discovery because special hardware, availability, or geographic latency makes distribution necessary.
- Moving shell scripts and undocumented host changes into [[Ansible]] can improve reproducibility and version control, but it does not eliminate the operational model the team must maintain.
- Letting an application mount the Docker socket creates a dangerous privilege boundary; a separate service exposing a restricted subset of the Docker API recreates an API-server role.
- A custom stack containing configuration, deployment, networking, discovery, immutable nodes, and a control API has reconstructed much of the problem surface associated with an orchestrator.
- The article does not claim that every workload should use Kubernetes; it cautions teams to understand the responsibilities Kubernetes bundles before dismissing its complexity.

## Key Quotes
> "A standard config format, a deployment method, an overlay network, service discovery, immutable nodes, and an API server." - the accumulated capabilities that turn a small container setup into an informal orchestrator.

> "make sure you understand the problems Kubernetes solves before dismissing it as overly-complex." - the article's explicit qualification.

## Connections
- [[MacChaffee]] - author of the cautionary infrastructure essay.
- [[Kubernetes]] - standardized orchestration platform whose responsibilities the custom stack gradually recreates.
- [[BoringTechnology]] - choosing familiar tools can fail as a simplification strategy when their integration recreates a platform locally.
- [[EssentialAndAccidentalComplexity]] - removing a named platform may redistribute rather than remove operational complexity.
- [[DeploymentAutomation]] - custom scripts accumulate rollout, rollback, and scaling responsibilities.
- [[InfrastructureAsCode]] - Ansible makes host configuration reproducible and version-controlled in the article's progression.
- [[ImmutableInfrastructure]] - the desired treatment of configured virtual machines before replacement or expansion.
- [[Docker]] - container runtime and API around which the improvised control plane develops.
- [[Tailscale]] - proposed overlay network and service-discovery layer between servers.
- [[Ansible]] - tool used to replace undocumented shell commands and host edits with versioned configuration.

## Contradictions
- The article qualifies [[kubernetes-maybe-a-few-bashpython-scripts-is-enough]]: scripts may be proportionate for a bounded system, but the advantage narrows as deployment, networking, discovery, node management, and programmatic scheduling requirements accumulate.
- The [[wenbin-fang-the-boring-technology-behind-a-one-person-internet-company]] case remains a counterexample to any universal Kubernetes recommendation: one experienced operator reports maintaining Ansible, a small release script, monitoring, and over-provisioned servers without needing an orchestrator. The difference is workload scope and whether the custom operating surface continues to expand.

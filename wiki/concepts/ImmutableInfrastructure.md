---
title: "Immutable Infrastructure"
type: concept
tags: [infrastructure, deployment, cloud, containers, reliability]
sources:
  - configuration-management-is-an-antipattern-by
  - immutable-infrastructure-using-packer-ansible-and-terraform
last_updated: 2026-09-30
knowledge_schema: synthesis-v1
---

## Definition
[[ImmutableInfrastructure]] is an operating model in which application code, dependencies, and much of the machine configuration are assembled into versioned images that are promoted and replaced as units instead of being changed repeatedly in place.

## Current Synthesis
The source's proposed pipeline begins with a maintained base image containing security updates and platform-wide agents. The application is built as an operating-system package, installed with its dependencies into an application-specific AMI or container image, distributed to target regions, and promoted through test and production. Configuration management may help construct the image, but it should not run inside each application container as an ongoing convergence layer.

This shifts operational reasoning from many unknown transition paths to a smaller artifact question: which image version should run? Precomputation can reduce startup time, make instance replacement practical, improve environment parity, and remove accumulated host cruft. Rolling replacement accommodates some stateful availability needs, while blue/green deployment creates a quick traffic-switch path to the prior fleet.

Immutability is not universal or complete. Bare-metal systems still require a minimal managed host layer, databases need persistent storage and version-compatible formats, and runtime configuration, secrets, external services, and mixed-version periods remain mutable. A trustworthy image pipeline also requires build automation, artifact distribution, canarying, deployment control, service discovery, observability, and sometimes feature flags.

The Packer tutorial supplies a compact implementation of the build boundary: Terraform creates the AWS network, Packer starts a builder in the resulting subnet, Ansible installs the static site and enables Nginx, and Terraform later launches EC2 from the tagged AMI. This supports the build-and-replace model while exposing a promotion weakness: choosing the most recent image carrying a shared tag is less explicit than pinning an approved artifact ID.

## Key Claims
- Building once and promoting the same artifact reduces dependency, package, and environment drift.
- Moving installation work to image build time can shorten scaling and failure-recovery startup paths.
- Replacement avoids repairing or cleaning up a uniquely damaged long-lived node.
- Rolling and blue/green strategies separate image construction from controlled production activation.
- Persistent data and runtime dependencies remain outside the immutable artifact and need their own compatibility and recovery design.
- Image immutability pays only when the supporting build, distribution, discovery, rollout, and observability systems are reliable.

## Evidence
- Build path: [[configuration-management-is-an-antipattern-by]] describes installing an application package and dependencies onto a security- and performance-reviewed base AMI, then distributing the derived image across AWS regions.
- Startup and recovery: [[configuration-management-is-an-antipattern-by]] contrasts prebuilt images with configuration-managed launches that can take an hour or more before receiving traffic.
- Fleet parity: [[configuration-management-is-an-antipattern-by]] argues that nodes launched from the same image avoid partial Chef-style convergence and accumulated system cruft.
- Release strategy: [[configuration-management-is-an-antipattern-by]] describes rolling replacement for state-sensitive clusters and blue/green traffic switching with a temporary old fleet.
- Stateful boundary: [[configuration-management-is-an-antipattern-by]] says database images still depend on persistent EBS or mounted storage, compatible on-disk formats, and scripted primary/standby failover.
- Concrete toolchain: [[immutable-infrastructure-using-packer-ansible-and-terraform]] connects a Terraform-created subnet to a Packer Amazon EBS builder, invokes Ansible during the bake, and launches EC2 from the resulting AMI.
- Startup readiness: [[immutable-infrastructure-using-packer-ansible-and-terraform]] enables Nginx during image construction so a launched instance does not wait for a post-launch configuration pass.
- Promotion ambiguity: [[immutable-infrastructure-using-packer-ansible-and-terraform]] selects `most_recent = true` among available AMIs sharing one tag rather than demonstrating explicit approval of a pinned image ID.

## Counterevidence & Qualifications
Neither source measures total build time, artifact storage, regional transfer, replacement cost, deployment capacity, failed-image rates, or comparative reliability. Claims that nodes are identical hold only for image contents, not runtime configuration, data, secrets, traffic, or post-start state. Blue/green fallback restores an earlier fleet but cannot automatically undo incompatible data or external effects. The tutorial's historical syntax, public-IP builder, local state dependency, and shared-tag image selection demonstrate a workflow, not current production security or promotion practice.

## What Changed
- Added a concrete Terraform-Packer-Ansible handoff that moves Nginx configuration into AMI construction.
- Made explicit image promotion—not merely image creation—a condition of trustworthy immutability.

## Related Concepts
- [[ConfigurationManagement]] - mutable convergence predecessor that may still be used to construct base images.
- [[DeploymentAutomation]] - promotes, verifies, activates, and retires versioned images.
- [[InfrastructureAsCode]] - provides reproducible definitions for the resources around immutable artifacts.
- [[ContinuousDelivery]] - benefits from one artifact moving through test and production.
- [[ChangeSafety]] - canaries, rolling exposure, blue/green switching, and compatibility controls bound replacement risk.
- [[RuntimeConfiguration]] - captures environment-specific state that remains outside a shared image.
- [[Packer]] - constructs the AMI used as the replaceable machine artifact.
- [[Terraform]] - provisions the network and EC2 capacity around the image.

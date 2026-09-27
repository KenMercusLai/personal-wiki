---
title: "Rig"
type: entity
tags: [platform-engineering, deployment, paas, buzzfeed]
sources:
  - deploy-with-haste-the-story-of-rig-buzzfeed-tech
last_updated: 2026-09-27
knowledge_schema: synthesis-v1
---

## Overview
[[Rig]] is [[Buzzfeed]]'s opinionated internal platform for developing, testing, deploying, observing, and operating containerized services on AWS.

## Current Profile
Rig emerged from a January 2016 hack-week PaaS prototype and became generally available that April. It defines a standard service interface through metadata, a Dockerfile, configuration, encrypted secrets, stateless runtime behavior, logs, lifecycle expectations, and health checks, then uses those conventions to automate local development, CI, image delivery, ECS scheduling, networking, DNS, TLS, logging, metrics, and alerts.

Its design is compositional rather than vertically proprietary. A Python CLI and web deployment interface present a cohesive experience over Docker, Jenkins, Terraform, AWS EC2, ELB and ECS, Papertrail, DataDog, and Nagios. BuzzFeed reports 227 production services and about 150 daily deployments by February 2017, while also identifying Terraform workflows and GPG secret management as unresolved product problems.

## Key Characteristics
- Standardizes application metadata, packaging, runtime behavior, health checks, configuration, and per-cluster secrets.
- Provides a repeatable VM and CLI workflow for running services, dependencies, and tests with live code reloading.
- Builds and tests versioned container images through a bundled Jenkins service before registry publication.
- Deploys selected images to ECS clusters and can provision load balancing, TLS, and DNS for new HTTP services.
- Makes searchable logs, metrics, resource discovery, alerts, and notification routing platform defaults.
- Uses Terraform to provision repeatable clusters on AWS infrastructure that BuzzFeed already understood.
- Is managed as an internal product through support, office hours, talks, interviews, surveys, and a feedback-driven roadmap.

## Evidence
- Service contract and local workflow: [[deploy-with-haste-the-story-of-rig-buzzfeed-tech]] specifies the service files and runtime requirements, then demonstrates `rig run` and `rig test` through the CLI.
- Delivery path: [[deploy-with-haste-the-story-of-rig-buzzfeed-tech]] describes Jenkins-based builds, container registry publication, web-selected images and clusters, ECS scheduling, and automatic load balancer, TLS, and DNS setup.
- Operational defaults: [[deploy-with-haste-the-story-of-rig-buzzfeed-tech]] describes Papertrail logging, DataDog instrumentation, and Nagios-based resource discovery and alert routing.
- Adoption and throughput: [[deploy-with-haste-the-story-of-rig-buzzfeed-tech]] reports 227 production services and 18,228 tracked deployments, averaging about 150 per day.
- Product feedback: [[deploy-with-haste-the-story-of-rig-buzzfeed-tech]] names support channels, office hours, talks, interviews, surveys, difficult Terraform scaling, and secret-management friction.

## Qualifications
The evidence is a 2017 first-party retrospective. Deployment volume and service count show adoption and activity but do not isolate causality, change-failure rate, recovery time, developer satisfaction, migration cost, platform-team burden, or long-term sustainability. The implementation depends on historical versions of Docker, ECS, Terraform, Jenkins, and the named observability services, so its durable contribution is the standard-interface and internal-product model rather than a current tool prescription.

## What Changed
- Created Rig as BuzzFeed's convention-driven internal developer platform.

## Relationships
- [[Buzzfeed]] - built Rig to support organizational growth and a shift toward service-oriented systems.
- [[InternalDeveloperPlatform]] - Rig is a concrete self-service platform case with measured adoption.
- [[DeveloperExperience]] - Rig treats development, validation, deployment, and operation as one designed experience.
- [[InfrastructureAsCode]] - Terraform provisions Rig clusters and exposes later workflow friction.
- [[DeploymentAutomation]] - Rig coordinates CI-built images, ECS placement, networking, TLS, and DNS.
- [[ServiceObservability]] - logging, metrics, monitoring, and notification routing are built-in defaults.
- [[SecretManagement]] - GPG-encrypted per-cluster secrets are a functional but unfriendly part of the service contract.
- [[Docker]] - container images are Rig's application packaging unit.
- [[AWS]] - supplies Rig's scheduler, compute, networking, load-balancing, database, and cache substrate.

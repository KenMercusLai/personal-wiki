---
title: "ZGent"
type: entity
tags: [ai, agents, operating-system, cloud-platform]
sources:
  - zgent-design-journey-3
last_updated: 2026-10-25
knowledge_schema: synthesis-v1
---

## Overview
[[ZGent]] is a project presented by [[WangZibo]] as a cloud-hosted, multi-user operating system for AI-agent applications.

## Current Profile
ZGent centralizes accounts, authentication, model API-key mediation, app installation and sharing, agent conversation, and account-owned storage with per-app authorization. Its apps remain conventional front-end and back-end programs, but use common platform services and implement distinct agent loops for tasks such as chat, coding, slide creation, research, and app construction. The source describes an intended architecture and existing project work, but does not provide a public security model, deployment measurements, or independent evaluation.

## Key Characteristics
- Cloud-hosted, multi-user platform with administrator-managed accounts and shared apps.
- Model gateway that lets users select configured models without receiving raw provider credentials.
- Installable and shareable apps whose official and third-party variants use the same interfaces.
- Account-owned storage with file- and folder-level grants scoped by user and app.
- Agent conversation as a common app capability, with task-specific loops implemented by each app.
- Cross-app artifact workflows, public read-only conversation sharing, and an app-building app named ZFactory.

## Evidence
- Platform scope: [[zgent-design-journey-3]] explicitly positions ZGent as a cloud-based, AI-era, multi-user operating system.
- Shared services: [[zgent-design-journey-3]] lists accounts, authentication, model-key management, app installation and sharing, agent conversations, and scoped storage access as framework responsibilities.
- App model: [[zgent-design-journey-3]] says apps use ordinary front-end and back-end code and differ chiefly in their task-specific agent loops.
- Workflow model: [[zgent-design-journey-3]] describes code and documents flowing from ZDev into ZSlide through an authorized account storage area.
- Authorization model: [[zgent-design-journey-3]] describes grants parameterized by storage owner, caller, app, and file or folder scope.

## Qualifications
The evidence is one project-authored design article. It gives scenarios and architectural intent rather than API specifications, threat models, isolation details, benchmark results, uptime data, adoption evidence, or an independent audit. The named apps and capabilities should therefore be treated as reported project status rather than externally verified production guarantees.

## What Changed
- Created the entity profile from the project's operating-system design article.
- Recorded the separation between shared platform services and app-specific agent loops.
- Recorded the proposed multi-dimensional storage permission model and cross-app artifact workflow.

## Relationships
- [[WangZibo]] - author presenting the project's design direction.
- [[AgentOperatingSystem]] - architectural category ZGent claims to instantiate.
- [[AgentNativeComputing]] - broader shift toward agent-centered software and shared execution infrastructure.
- [[AgentPermissionModel]] - supplies the authority model ZGent applies to apps and account-owned storage.
- [[AgentFilesystem]] - stores artifacts exchanged across ZGent app workflows.

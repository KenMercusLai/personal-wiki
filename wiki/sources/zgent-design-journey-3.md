---
title: "ZGent 设计之旅 #3 AI 时代的操作系统"
type: source
tags: [ai, agents, operating-systems, multi-user, permissions]
date: 2026-05-21
source_file: "/mnt/ken_personal_wiki/Articles/zgent-design-journey-3.md"
---

## Summary
[[WangZibo]] presents [[ZGent]] as a cloud-hosted, multi-user [[AgentOperatingSystem]] that supplies accounts, authentication, model-credential mediation, app installation and sharing, agent conversations, and per-app access to account-owned storage. The proposal separates common identity, model, storage, and authorization infrastructure from ordinary front-end and back-end apps that implement their own agent loops. It is a first-party design narrative and product description, not a security analysis, implementation audit, or measured deployment report.

## Key Claims
- An AI-era operating system should standardize the shared infrastructure that otherwise fragments across AI tools: identity, model-provider access, multi-user sharing, storage, and permissions.
- Administrators can install recommended apps and configure model API keys for a team while letting users choose models without exposing the underlying credentials.
- Users can install apps under their own accounts, let other people run them, and share read-only conversation links with unauthenticated viewers.
- Each account has a storage area whose files and folders can be authorized for particular accounts through particular apps.
- The proposed authorization model supports both user consent for an app to read the user's files and owner-defined grants that let other users write through one app into a narrowly scoped folder.
- Apps remain conventional front-end and back-end software, but each provides an agent conversation and implements its own task-specific agentic loop on top of common platform services.
- Official and third-party apps use the same interfaces and installation mechanism; examples include chat, coding, slides, research, and app-building tools.

## Key Quotes
> “ZGent 的定位是基于云端的、AI 时代的、多用户的操作系统。” — the project's stated platform position.

> “开发者不需要关心用户身份验证或者不同模型厂商的 API 格式不同这类问题，只需要实现自己独特的 agentic loop。” — on the boundary between shared infrastructure and app-specific behavior.

## Connections
- [[WangZibo]] - author describing ZGent's design and implementation direction.
- [[ZGent]] - cloud-hosted multi-user agent platform proposed in the article.
- [[AgentOperatingSystem]] - architectural category combining shared identity, model, app, storage, and permission services.
- [[AgentNativeComputing]] - ZGent retains apps while making agent conversations and cross-app artifacts part of the common computing substrate.
- [[AgentPermissionModel]] - access is scoped by account, app, storage object, and grant direction rather than reduced to one blanket approval.
- [[AgentFilesystem]] - account-owned storage carries code, documents, slides, and user-provided data between app workflows.
- [[AIApplicationFramework]] - ZGent removes repeated platform concerns while leaving each app developer responsible for its distinct agent loop.

## Contradictions
- The source's operating-system analogy is a design claim. It does not document isolation boundaries, credential storage, grant revocation, audit trails, confused-deputy defenses, malicious apps, prompt injection, recovery, or independent security review.
- The example in which an app restricts each participant to a personal record relies partly on app code while the platform rule blocks access through other apps; the article does not specify which row- or object-level guarantees are independently enforced by ZGent.
- Claims that the named apps already exist and that cloud execution yields a publicly accessible website are first-party product statements without availability, reliability, performance, or adoption measurements.
- The inspected local image is a decorative monitor-and-app-icons illustration with no additional labels, architecture, workflow, or evidence, so it was omitted and no asset manifest was required.

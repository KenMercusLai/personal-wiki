---
title: "Gavriel Cohen"
type: entity
tags: [ai, agents, security, software]
sources:
  - dont-trust-ai-agents-nanoclaw-blog
last_updated: 2026-09-27
knowledge_schema: synthesis-v1
---

## Overview
[[GavrielCohen]] is the author of the NanoClaw security-model article and identifies himself as the builder of [[NanoClaw]].

## Current Profile
In the available source, Cohen advocates treating AI agents, peer agents, and group participants as untrusted. His design position is that operating-system-enforced isolation, narrow mounts, and reviewable code should carry the security burden instead of expecting a probabilistic agent to honor prompts, confirmation rules, or allowlists.

## Key Characteristics
- Builds and advocates for the NanoClaw agent runtime.
- Frames agent security around assumed misbehavior and contained damage.
- Prefers small, auditable installations with selectively added integrations.

## Evidence
- Project role: [[dont-trust-ai-agents-nanoclaw-blog]] identifies Cohen as the article author and says he built NanoClaw on the stated principle.
- Security position: [[dont-trust-ai-agents-nanoclaw-blog]] argues for infrastructure-enforced containment outside the agentic surface.
- Auditability position: [[dont-trust-ai-agents-nanoclaw-blog]] favors a small core and code-reviewed skill additions.

## Qualifications
The wiki currently has one first-party source for Cohen, so this profile covers only his NanoClaw role and the views expressed in that article. It does not independently verify his biography, the product comparison, or NanoClaw's security guarantees.

## What Changed
- Established Cohen's NanoClaw role and distrust-by-architecture security position.

## Relationships
- [[NanoClaw]] - project Cohen says he built around infrastructure-enforced agent containment.
- [[OpenClaw]] - runtime he uses as the contrast case in his security argument.
- [[AgentPermissionModel]] - his argument treats permission checks as secondary to isolation boundaries.

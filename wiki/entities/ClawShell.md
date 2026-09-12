---
title: "ClawShell"
type: entity
tags: [ai, agents, security, open-source]
sources:
  - wei-shen-me-xian-you-de-agent-infra-wu-fa-zhi-cheng-sheng-chan-ji-ying-yong
last_updated: 2026-09-12
knowledge_schema: synthesis-v1
---

## Overview
[[ClawShell]] is an open-source project cited by [[Guanlan]] as a concrete practice related to scoped token and capability control for agents.

## Current Profile
The source references ClawShell only briefly, in the section on capability isolation. It appears as an example of implementing scoped, revocable capability boundaries so that an agent does not retain broad credentials after failure or malicious instruction injection.

## Key Characteristics
- Cited as open-source practice around agent capability control.
- Associated with scoped token behavior.
- Used to illustrate the [[CapabilityGateway]] idea.
- Relevant to reducing an agent's blast radius after crash or compromise.

## Evidence
- Project reference: [[wei-shen-me-xian-you-de-agent-infra-wu-fa-zhi-cheng-sheng-chan-ji-ying-yong]] names ClawShell in the capability-isolation section.
- Scoped-token context: [[wei-shen-me-xian-you-de-agent-infra-wu-fa-zhi-cheng-sheng-chan-ji-ying-yong]] describes scoped tokens expiring after crashes, then cites ClawShell as concrete practice.

## Qualifications
The article does not describe ClawShell's architecture, API, repository, or production adoption. The page should stay narrow until direct project documentation is ingested.

## What Changed
- Created the entity page for ClawShell.

## Relationships
- [[Guanlan]] - Guanlan cites ClawShell as open-source practice.
- [[CapabilityGateway]] - ClawShell illustrates scoped capability mediation.
- [[SemanticIsolation]] - ClawShell appears in the source's semantic-boundary discussion.

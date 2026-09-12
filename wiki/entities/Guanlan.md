---
title: "Guanlan"
type: entity
tags: [author, ai, infrastructure]
sources:
  - wei-shen-me-xian-you-de-agent-infra-wu-fa-zhi-cheng-sheng-chan-ji-ying-yong
last_updated: 2026-09-12
knowledge_schema: synthesis-v1
---

## Overview
[[Guanlan]] is the author of the source article arguing that production-grade agent systems need new infrastructure primitives for side effects, capabilities, and recovery.

## Current Profile
The source presents Guanlan as an infrastructure-oriented AI commentator and builder. Guanlan argues from experience with distributed execution systems at [[Cloudflare]] and [[Kong]], and cites [[ClawShell]] as an open-source practice related to scoped agent capabilities.

## Key Characteristics
- Frames agent reliability as a semantic infrastructure problem rather than a prompting problem.
- Argues that long-running autonomous agents need [[EffectLog]], [[CapabilityGateway]], and [[ForkRecovery]].
- Distinguishes execution isolation from [[SemanticIsolation]].
- Treats [[AgentResumability]] as a more relevant reliability target than uptime for agents.
- Bases the argument partly on distributed infrastructure experience at Cloudflare and Kong.

## Evidence
- Author role: [[wei-shen-me-xian-you-de-agent-infra-wu-fa-zhi-cheng-sheng-chan-ji-ying-yong]] names Guanlan as the article's author.
- Infrastructure thesis: [[wei-shen-me-xian-you-de-agent-infra-wu-fa-zhi-cheng-sheng-chan-ji-ying-yong]] argues that agent infra must reduce model uncertainty by creating deterministic boundaries.
- Experience claim: [[wei-shen-me-xian-you-de-agent-infra-wu-fa-zhi-cheng-sheng-chan-ji-ying-yong]] says Guanlan worked on previous-generation distributed execution systems at Cloudflare and Kong.
- Project reference: [[wei-shen-me-xian-you-de-agent-infra-wu-fa-zhi-cheng-sheng-chan-ji-ying-yong]] cites ClawShell as a concrete practice around scoped agent capability control.

## Qualifications
The wiki has only this source for Guanlan, so the profile is limited to the article's self-presentation and technical argument.

## What Changed
- Created the entity page for Guanlan as the article's author.

## Relationships
- [[ProductionAgentInfrastructure]] - Guanlan argues for this infrastructure frame.
- [[ClawShell]] - Guanlan cites it as open-source practice.
- [[Cloudflare]] - Guanlan says prior infrastructure experience there informs the argument.
- [[Kong]] - Guanlan says prior distributed-execution experience there informs the argument.

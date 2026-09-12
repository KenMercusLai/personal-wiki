---
title: "OpenClaw"
type: entity
tags: [ai, agents, security]
sources:
  - wei-shen-me-xian-you-de-agent-infra-wu-fa-zhi-cheng-sheng-chan-ji-ying-yong
  - mu-jiang-chui-zi-ding-zi
last_updated: 2026-09-12
knowledge_schema: synthesis-v1
---

## Overview
[[OpenClaw]] is an agent-related project referenced as both a visible example of real system-permission risk and, in a later source, a personal-assistant paradigm that contrasts with group-chat-oriented agents such as [[Bub]].

## Current Profile
The first source mentions OpenClaw briefly as a visible example that moved agent safety concerns from theory into practice. It uses OpenClaw to motivate the need for production-grade capability boundaries when models can operate real systems.

PsiACE's source adds product framing. It describes OpenClaw as a personal assistant: an agent that enters daily life, can be extended through skills, and opens an imaginative path toward everyday help such as ordering food, shopping, or document support. That same personal framing is also described as its limitation when compared with [[Bub]], which is designed for multi-person and multi-agent group-chat coexistence.

## Key Characteristics
- Used as an example of real system-permission risk in agent systems.
- Serves as a motivating case in one source and a product paradigm in another.
- Presented as a personal assistant entering everyday life.
- Associated with skill-based capability extension in PsiACE's source.
- Contrasted with [[Bub]]'s multi-person and multi-agent group-chat frame.
- Reinforces the need for [[CapabilityGateway]] and [[SemanticIsolation]].

## Evidence
- Safety signal: [[wei-shen-me-xian-you-de-agent-infra-wu-fa-zhi-cheng-sheng-chan-ji-ying-yong]] says OpenClaw pushed the issue of real system permissions into public attention.
- Capability framing: [[wei-shen-me-xian-you-de-agent-infra-wu-fa-zhi-cheng-sheng-chan-ji-ying-yong]] connects model permission expansion with larger safety risk.
- Personal-assistant frame: [[mu-jiang-chui-zi-ding-zi]] says OpenClaw is positioned as a personal assistant entering everyday life.
- Skills and imagination: [[mu-jiang-chui-zi-ding-zi]] says OpenClaw's abilities can be extended through skills and that it opens a broader product imagination.
- Bub contrast: [[mu-jiang-chui-zi-ding-zi]] says OpenClaw's personal orientation is also its limitation relative to Bub's group-chat design.

## Qualifications
Neither source provides a full technical description of OpenClaw's implementation. The safety source uses it mainly as a risk signal, while PsiACE's source uses it mainly as a product contrast.

## What Changed
- Created the entity page for OpenClaw as a motivating example in the article.
- Added OpenClaw's personal-assistant framing and contrast with Bub.

## Relationships
- [[CapabilityGateway]] - OpenClaw motivates hard capability control for real system permissions.
- [[SemanticIsolation]] - OpenClaw is cited as evidence that model access needs semantic boundaries.
- [[ProductionAgentInfrastructure]] - OpenClaw helps motivate production agent infrastructure.
- [[Bub]] - Bub is contrasted with OpenClaw's personal-assistant orientation.

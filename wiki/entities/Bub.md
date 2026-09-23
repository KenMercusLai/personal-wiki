---
title: "Bub"
type: entity
tags: [ai, agents, coding-agent, group-chat]
sources:
  - mu-jiang-chui-zi-ding-zi
  - tape-x-topic-wo-dui-zhi-neng-ti-shang-xia-wen-de-zu-zhi-fang-shi
last_updated: 2026-09-24
knowledge_schema: synthesis-v1
---

## Overview
[[Bub]] is presented as PsiACE's agent project, renewed from a simple coding agent into a group-chat-oriented agent system designed for multi-person or multi-agent coexistence.

## Current Profile
The sources position Bub as a contrasting paradigm to personal-assistant agents such as [[OpenClaw]]. Bub can still serve individual requests, but its distinctive design pressure is group chat: it must recognize participants and itself, work with incomplete context, infer fuzzy intent, keep parallel topics apart, communicate effectively, and sometimes choose not to answer. The newer article uses Bub as evidence that Tape is a design language rather than one fixed product: Bub applies it toward group-chat agents, while the author's Topic proposal applies the same core to enterprise knowledge-base support.

## Key Characteristics
- Began from a simple coding-agent shape.
- Shares the minimal coding-agent tool intuition behind [[CodingAgentMinimalTooling]].
- Designed for multi-person or multi-agent group-chat settings.
- Emphasizes identity awareness and communication rather than only task execution.
- Uses [[TapeAndAnchors]] as part of the source's broader context-management model.
- Illustrates how the Tape specification can support a vertical product distinct from topic-oriented enterprise support.

## Evidence
- Project evolution: [[mu-jiang-chui-zi-ding-zi]] says Bub moved from a simple coding agent toward an OpenClaw-like but different form.
- Group-chat frame: [[mu-jiang-chui-zi-ding-zi]] says Bub is designed for multi-person or multi-agent collaboration and lives from day one in group-chat scenarios.
- Identity need: [[mu-jiang-chui-zi-ding-zi]] says group-chat agents must distinguish or understand participants and themselves.
- Communication need: [[mu-jiang-chui-zi-ding-zi]] says such agents face incomplete context, fuzzy task intent, and parallel topics.
- Response selectivity: [[mu-jiang-chui-zi-ding-zi]] says an agent need not respond to every message.
- Design-language role: [[tape-x-topic-wo-dui-zhi-neng-ti-shang-xia-wen-de-zu-zhi-fang-shi]] cites Bub as an example of Tape being pulled toward a group-chat vertical rather than prescribing one product shape.

## Qualifications
The sources describe Bub at a product-and-model level rather than giving detailed architecture, implementation, benchmarks, or user evidence. The newer article links Bub to Tape but does not show how completely Bub implements entries, anchors, views, handoff, or topic boundaries.

## What Changed
- Created the initial entity page for Bub.
- Added Bub's role as the group-chat vertical demonstrating Tape's product-independent design language.

## Relationships
- [[PsiACE]] - Bub is PsiACE's central agent project in the source.
- [[OpenClaw]] - Bub is contrasted with OpenClaw's personal-assistant frame.
- [[CodingAgentMinimalTooling]] - Bub's first version used the same small tool surface discussed in the source.
- [[TapeAndAnchors]] - Bub motivates the source's context-reconstruction model.
- [[LLMContextManagement]] - Bub's group-chat setting exposes context inheritance limits.
- [[AgentTopicLifecycle]] - contrasts enterprise topic organization with Bub's group-chat specialization over the same Tape core.

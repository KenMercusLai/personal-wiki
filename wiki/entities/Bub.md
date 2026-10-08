---
title: "Bub"
type: entity
tags: [ai, agents, coding-agent, group-chat]
sources:
  - mu-jiang-chui-zi-ding-zi
  - tape-x-topic-wo-dui-zhi-neng-ti-shang-xia-wen-de-zu-zhi-fang-shi
  - chuang-zao-yi-zhi-long-xia-xu-yao-xie-shi-me-frosts-blog
last_updated: 2026-10-08
knowledge_schema: synthesis-v1
---

## Overview
[[Bub]] is [[PsiACE]]'s agent project, renewed from a simple coding agent into a group-chat-oriented system and then used with [[FrostMing]] to test a minimal, self-bootstrapping Telegram-agent runtime.

## Current Profile
The sources position Bub as a contrasting paradigm to personal-assistant agents such as [[OpenClaw]]. Bub can still serve individual requests, but its distinctive design pressure is group chat: it must recognize participants and itself, work with incomplete context, infer fuzzy intent, keep parallel topics apart, communicate effectively, and sometimes choose not to answer. The Tape article uses Bub as evidence that Tape is a design language rather than one fixed product: Bub applies it toward group-chat agents, while the author's Topic proposal applies the same core to enterprise knowledge-base support.

Frost Ming's experiment adds a separate architectural trajectory. Bub first gained Telegram handlers, message IDs, participant metadata, media, stickers, and reactions through ordinary code. It then created a Telegram-sending Skill, after which the team removed the built-in sender and proposed replacing the listener with an agent-authored startup script. A Docker startup fallback and one-shot CLI invocation let Bub participate in bootstrapping its own persistent runtime. This supports [[AINativeAgentArchitecture]] as an experimental use of Bub, but does not establish production reliability or safety.

## Key Characteristics
- Began from a simple coding-agent shape.
- Shares the minimal coding-agent tool intuition behind [[CodingAgentMinimalTooling]].
- Designed for multi-person or multi-agent group-chat settings.
- Emphasizes identity awareness and communication rather than only task execution.
- Uses [[TapeAndAnchors]] as part of the source's broader context-management model.
- Illustrates how the Tape specification can support a vertical product distinct from topic-oriented enterprise support.
- Serves as a prototype for moving messaging capabilities from framework code into agent-managed Skills and startup artifacts.

## Evidence
- Project evolution: [[mu-jiang-chui-zi-ding-zi]] says Bub moved from a simple coding agent toward an OpenClaw-like but different form.
- Group-chat frame: [[mu-jiang-chui-zi-ding-zi]] says Bub is designed for multi-person or multi-agent collaboration and lives from day one in group-chat scenarios.
- Identity need: [[mu-jiang-chui-zi-ding-zi]] says group-chat agents must distinguish or understand participants and themselves.
- Communication need: [[mu-jiang-chui-zi-ding-zi]] says such agents face incomplete context, fuzzy task intent, and parallel topics.
- Response selectivity: [[mu-jiang-chui-zi-ding-zi]] says an agent need not respond to every message.
- Design-language role: [[tape-x-topic-wo-dui-zhi-neng-ti-shang-xia-wen-de-zu-zhi-fang-shi]] cites Bub as an example of Tape being pulled toward a group-chat vertical rather than prescribing one product shape.
- Feature reproduction: [[chuang-zao-yi-zhi-long-xia-xu-yao-xie-shi-me-frosts-blog]] says Bub added Telegram identity, reply, media, sticker, and reaction behavior and approximated OpenClaw apart from memory and tool differences.
- Self-bootstrapping experiment: [[chuang-zao-yi-zhi-long-xia-xu-yao-xie-shi-me-frosts-blog]] reports an agent-created Telegram Skill and startup script executed through Docker and a one-shot agent command.

## Qualifications
The sources describe Bub at a product-and-model level rather than supplying a reproducible architecture, benchmarks, failure rates, or user study. The Tape article does not show how completely Bub implements entries, anchors, views, handoff, or topic boundaries. The self-bootstrapping account is a short first-person experiment; its prompt-only control and unread agent-written code should not be interpreted as evidence that external permission, verification, audit, and recovery mechanisms are unnecessary.

## What Changed
- Created the initial entity page for Bub.
- Added Bub's role as the group-chat vertical demonstrating Tape's product-independent design language.
- Added the Telegram feature-reproduction and self-bootstrapping runtime experiment.

## Relationships
- [[PsiACE]] - Bub is PsiACE's central agent project in the source.
- [[OpenClaw]] - Bub is contrasted with OpenClaw's personal-assistant frame.
- [[CodingAgentMinimalTooling]] - Bub's first version used the same small tool surface discussed in the source.
- [[TapeAndAnchors]] - Bub motivates the source's context-reconstruction model.
- [[LLMContextManagement]] - Bub's group-chat setting exposes context inheritance limits.
- [[AgentTopicLifecycle]] - contrasts enterprise topic organization with Bub's group-chat specialization over the same Tape core.
- [[FrostMing]] - collaborator who used Bub to explore the AI-native runtime thesis.
- [[AINativeAgentArchitecture]] - Bub is the prototype through which framework-owned behavior was moved into agent-managed artifacts.

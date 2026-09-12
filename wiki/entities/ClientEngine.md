---
title: "Client Engine"
type: entity
tags: [game-backend, leancloud, product]
sources:
  - 2018-nian-du-xiao-jie-ji-shu-fang-mian
last_updated: 2026-09-12
knowledge_schema: synthesis-v1
---

## Overview
[[ClientEngine]] is the [[LeanCloud]] product that emerged from Wang Ziting's demo for running server-side game logic as a participant in a game message service.

## Current Profile
In the source, Client Engine represents the productized version of an architectural choice: instead of tightly coupling server-side game logic to the message-forwarding service, run that logic as another client that joins the message system and interacts with player clients. This preserves logic reuse, keeps migration paths smoother, and decouples server execution from the message relay.

## Key Characteristics
- Productizes server-side game logic for anti-cheat and authoritative execution needs.
- Treats the server-side logic process as a client inside the message service.
- Supports reuse of game logic between client-side and server-side execution.
- Keeps the message-forwarding service decoupled from game-specific logic.

## Evidence
- Anti-cheat need: [[2018-nian-du-xiao-jie-ji-shu-fang-mian]] says LeanCloud needed a way to run game logic on the server.
- Architectural pattern: [[2018-nian-du-xiao-jie-ji-shu-fang-mian]] argues server-side game logic should join the message service as a client.
- Migration benefit: [[2018-nian-du-xiao-jie-ji-shu-fang-mian]] says the pattern smooths the move from single-player to action synchronization and state synchronization.
- Productization: [[2018-nian-du-xiao-jie-ji-shu-fang-mian]] says the demo pattern was later released officially as Client Engine.

## Qualifications
The source reports the product from the author's perspective and does not include performance, adoption, security, or competitive comparisons.

## What Changed
- Created the Client Engine entity page from the game-backend section.

## Relationships
- [[LeanCloud]] - company and platform that released Client Engine.
- [[ServerSideGameLogic]] - architectural pattern embodied by the product.
- [[GameServerScaleAndStability]] - related operational domain, though this source emphasizes architecture rather than launch scale.

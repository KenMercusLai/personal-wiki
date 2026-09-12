---
title: "Server-Side Game Logic"
type: concept
tags: [game-backend, architecture, realtime]
sources:
  - 2018-nian-du-xiao-jie-ji-shu-fang-mian
last_updated: 2026-09-12
knowledge_schema: synthesis-v1
---

## Definition
[[ServerSideGameLogic]] is the pattern of running game rules on a server-side process for authority, anti-cheat, or synchronization while coordinating with player clients through a backend messaging system.

## Current Synthesis
The source frames server-side game logic as a design response to anti-cheat needs in a message-forwarding game backend. Wang Ziting preferred to make the server-side logic process act like another client in the message service rather than embed game logic directly into the relay. That architecture reuses game logic across client and server contexts, keeps migration from single-player to action synchronization and state synchronization smoother, and decouples product infrastructure from game-specific code.

## Key Claims
- Anti-cheat requirements can force game logic to run on the server rather than only on player clients.
- Treating server-side logic as a client in the message service preserves reuse and decoupling.
- The pattern creates a smoother migration path from standalone play to action sync and state sync.
- A small demo can validate an architectural option before it becomes a productized platform feature.

## Evidence
- Anti-cheat motivation: [[2018-nian-du-xiao-jie-ji-shu-fang-mian]] says server-side game logic was needed because of anti-cheat concerns.
- Client-in-message-service pattern: [[2018-nian-du-xiao-jie-ji-shu-fang-mian]] says the preferred solution was to join server-side logic to the message service as a client.
- Reuse and migration: [[2018-nian-du-xiao-jie-ji-shu-fang-mian]] lists logic reuse and smooth migration from single-player to action sync and state sync as benefits.
- Product validation: [[2018-nian-du-xiao-jie-ji-shu-fang-mian]] says a turn-based card-game demo validated the pattern before official [[ClientEngine]] release.

## Counterevidence & Qualifications
The source is an architectural reflection from a simple demo and productization path. It does not compare alternative game-server frameworks, performance tradeoffs, or security guarantees.

## What Changed
- Created the concept page from the LeanCloud game-backend section.

## Related Concepts
- [[GameServerScaleAndStability]] - server-side logic becomes part of game backend reliability and correctness under real users.
- [[GameServerCloudNativeDelivery]] - productized game backend features need deployable service boundaries.
- [[ClientEngine]] - entity representing the productized implementation.
- [[SoftwareVerification]] - authoritative game logic requires behavioral validation to be trusted.

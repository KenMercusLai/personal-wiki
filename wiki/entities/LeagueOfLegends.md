---
title: "League of Legends"
type: entity
tags: [game-development, live-service-games]
sources:
  - automated-testing-for-league-of-legends-riot-games-technology
last_updated: 2026-09-14
knowledge_schema: synthesis-v1
---

## Overview
[[LeagueOfLegends]] is Riot Games' live multiplayer game used in the source as the production setting for large-scale automated functional testing.

## Current Profile
The source frames League of Legends as a fast-changing game whose release rhythm strains manual quality assurance. Its gameplay complexity makes automated tests valuable at the level of champion abilities, vision rules, minion rewards, asset loading, and client/server game-state control.

## Key Characteristics
- Changes quickly through daily code and content submissions.
- Ships on a two-week patch cadence.
- Requires tests that can control and observe both client and server game state.
- Contains gameplay behavior where small timing or state bugs can affect player experience.

## Evidence
- Release pressure: [[automated-testing-for-league-of-legends-riot-games-technology]] says League has more than 100 daily code/content changes and a patch every two weeks.
- Gameplay coverage: [[automated-testing-for-league-of-legends-riot-games-technology]] lists tests for champion abilities, vision rules, minion rewards, and champion/skin loading.
- Client/server control: [[automated-testing-for-league-of-legends-riot-games-technology]] says tests use RPC endpoints on the game client and server.
- Example behavior: [[automated-testing-for-league-of-legends-riot-games-technology]] describes a Kog'Maw Bio-Arcane Barrage test that checks physical and magic damage against enemy units.

## Qualifications
The source describes the game as a test-automation target rather than a full product, business, or player-community profile.

## What Changed
- Created the entity from the Riot Games Technology source.

## Relationships
- [[RiotGames]] - developer and operator of League of Legends.
- [[BuildVerificationSystem]] - automated testing framework used against the game.
- [[AutomatedGameTesting]] - practice applied to League gameplay behavior.
- [[ServerSideGameLogic]] - related game-engineering concept because tests coordinate game client and server state.

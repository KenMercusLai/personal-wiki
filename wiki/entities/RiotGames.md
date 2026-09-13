---
title: "Riot Games"
type: entity
tags: [game-development, software-engineering]
sources:
  - automated-testing-for-league-of-legends-riot-games-technology
last_updated: 2026-09-14
knowledge_schema: synthesis-v1
---

## Overview
[[RiotGames]] is the game company behind [[LeagueOfLegends]] and the engineering organization operating the [[BuildVerificationSystem]] described in the source.

## Current Profile
The source presents Riot as a live-game engineering organization managing rapid code and content change. For League of Legends, Riot invested in automated testing infrastructure because a two-week patch cadence and more than 100 daily source-control changes made full manual regression coverage impractical.

## Key Characteristics
- Operates a fast-changing live game with frequent patches and daily code/content changes.
- Uses automated CI testing to reduce late defects and developer context switching.
- Separates automation infrastructure from reporting, artifact tagging, and bug-ticket creation.
- Treats quality analysts as higher-value when freed from repetitive full-sweep regression work.

## Evidence
- Change cadence: [[automated-testing-for-league-of-legends-riot-games-technology]] says League saw well over 100 code and content changes per day and new patches every two weeks.
- Automation investment: [[automated-testing-for-league-of-legends-riot-games-technology]] says Riot ran about 100,000 test cases per day through BVS.
- Reporting separation: [[automated-testing-for-league-of-legends-riot-games-technology]] describes a separate reporting service that stores run data, creates tickets, tags artifacts, and emails committers.
- QA role: [[automated-testing-for-league-of-legends-riot-games-technology]] says automation lets quality analysts focus on creative testing and upstream defect prevention.

## Qualifications
The source is limited to Riot's automation work for League of Legends' in-game experience and does not describe every Riot engineering practice or later changes to the test system.

## What Changed
- Created the entity from the Riot Games Technology source.

## Relationships
- [[LeagueOfLegends]] - live game whose patch cadence motivates the testing infrastructure.
- [[BuildVerificationSystem]] - internal framework Riot uses for automated game testing.
- [[JimMerrill]] - Riot engineer and article author.
- [[AutomatedGameTesting]] - quality practice Riot applies at large scale.

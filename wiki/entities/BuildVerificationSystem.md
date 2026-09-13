---
title: "Build Verification System"
type: entity
tags: [testing, automation, game-development, continuous-integration]
sources:
  - automated-testing-for-league-of-legends-riot-games-technology
last_updated: 2026-09-14
knowledge_schema: synthesis-v1
---

## Overview
[[BuildVerificationSystem]] is Riot Games' Python-based automated test framework for League of Legends' game client and server.

## Current Profile
BVS handles the machinery around automated game tests: acquiring artifacts, deploying them to test machines, starting systems under test, executing test scripts, and reporting results. Its architecture separates a generic executor API, game-specific drivers, and scripts, while a separate reporting service owns run history, ticket creation, artifact tagging, and notifications.

## Key Characteristics
- Provides a functional-testing harness for League of Legends client/server behavior.
- Uses RPC endpoints to command game clients and servers and inspect game state.
- Separates executor, driver, and script layers so future drivers can reuse common utilities.
- Stages new tests for at least a week before promoting stable tests into blocker or core sets.
- Avoids pure sleeps by exposing conditional wait helpers that poll for game-state changes.
- Supports parallel execution through JSON-defined test sets and later load-balancing based on recent run times.

## Evidence
- Harness responsibilities: [[automated-testing-for-league-of-legends-riot-games-technology]] says BVS acquires artifacts, deploys them, starts systems, executes tests, and reports results.
- RPC control: [[automated-testing-for-league-of-legends-riot-games-technology]] says tests use client and server RPC endpoints for commands and state queries.
- Architecture: [[automated-testing-for-league-of-legends-riot-games-technology]] describes executor, driver, and script layers, with LOLGame as the active driver.
- Trust process: [[automated-testing-for-league-of-legends-riot-games-technology]] says tests enter BVSStaging for at least one week, then can move to BVSBlocker or BVSCore.
- Flake reduction: [[automated-testing-for-league-of-legends-riot-games-technology]] says the standard library has no pure sleep and instead uses conditional waits.
- Throughput: [[automated-testing-for-league-of-legends-riot-games-technology]] reports roughly 5,500 cases in 18 minutes per build and about 100,000 daily cases.

## Qualifications
BVS is described from a 2016 Riot engineering article. The source does not establish whether the exact architecture, throughput, or tool boundaries remain current.

## What Changed
- Created the entity from the Riot Games Technology source.

## Relationships
- [[RiotGames]] - organization that built and operated BVS.
- [[LeagueOfLegends]] - game tested by BVS.
- [[JimMerrill]] - BVS-Dev tech captain and source author.
- [[AutomatedGameTesting]] - broader practice instantiated by BVS.
- [[DeterministicTesting]] - BVS conditional waits and staging process reduce flaky test behavior.
- [[SoftwareVerification]] - BVS turns game behavior into repeatable CI feedback.

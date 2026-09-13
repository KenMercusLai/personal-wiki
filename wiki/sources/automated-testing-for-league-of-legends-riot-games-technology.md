---
title: "Automated Testing for League of Legends"
type: source
tags: [testing, automation, game-development]
date: 2026-03-30
source_file: /mnt/ken_personal_wiki/Articles/Automated Testing for League of Legends - Riot Games Technology.md
---

## Summary
Jim Merrill describes Riot Games' Build Verification System, a Python-based automation framework for testing the in-game experience of [[LeagueOfLegends]]. The system runs roughly 100,000 test cases per day, gives developers CI feedback within about an hour, and separates test execution, drivers, test scripts, and reporting services so game teams can write stable functional tests without managing the full environment.

## Key Claims
- [[RiotGames]] used large-scale automated testing to keep pace with more than 100 daily code and content changes and a two-week patch cadence for [[LeagueOfLegends]].
- The [[BuildVerificationSystem]] acquires artifacts, deploys them to test machines, starts client/server systems, executes Python tests, and reports results while hiding setup complexity from test writers.
- Tests use client and server RPC endpoints to issue commands and inspect game state, covering champion abilities, vision rules, minion rewards, and asset-loading behavior.
- Stable test promotion required process: tests entered BVSStaging for at least one week, then moved into BVSBlocker smoke tests or BVSCore functional coverage after demonstrating reliability.
- The framework avoids pure sleeps and exposes conditional waits, reducing hardware-dependent flakiness in automated game tests.
- BVS ran about 5,500 test cases in 18 minutes per build, about 100,000 test cases daily, and found roughly half of critical or blocker bugs.

## Key Quotes
> "We now run approximately 100,000 test cases a day" - Merrill on the scale of Riot's automated testing.

> "Our test system runs on continuous integration (CI) and reports back within about an hour of check-in." - Merrill on developer feedback speed.

## Connections
- [[JimMerrill]] - author and BVS-Dev tech captain explaining the automation system.
- [[RiotGames]] - company operating the game and testing infrastructure.
- [[LeagueOfLegends]] - live game whose fast code and content cadence created the automation need.
- [[BuildVerificationSystem]] - Riot's Python test framework and artifact/deployment/test/report harness.
- [[AutomatedGameTesting]] - broader practice illustrated by BVS.
- [[SoftwareVerification]] - BVS is a production-scale example of behavior verification through CI, RPC control, staged test trust, and reporting.
- [[DeterministicTesting]] - BVS avoids pure sleeps and requires staging stability to reduce flaky results.
- [[DeploymentAutomation]] - BVS tags artifacts and blocks unworthy builds from test-environment deployment.

## Contradictions
- No contradictions with existing wiki pages were found.

## Image Notes
- The available lead image shows a League in-game test scene with Kog'Maw facing level-18 enemy units in mid lane, matching the article's champion-ability testing example.
- The referenced local article assets `bvsheader.jpg`, `bvs_report.png`, `bvs_wardbug.png`, and `bvs_flowchart.png` were not present beside the source file, so their contents could not be inspected.

---
title: "Automated Game Testing"
type: concept
tags: [testing, game-development, automation, reliability]
sources:
  - automated-testing-for-league-of-legends-riot-games-technology
last_updated: 2026-09-14
knowledge_schema: synthesis-v1
---

## Definition
[[AutomatedGameTesting]] is the practice of using software-controlled clients, servers, test harnesses, and reporting systems to verify game behavior repeatedly without relying on humans to rerun every regression path.

## Current Synthesis
The Riot source presents automated game testing as a response to live-game change velocity. For [[LeagueOfLegends]], more than 100 daily code and content changes and a two-week patch cadence made exhaustive manual sweeps too slow, so [[RiotGames]] built the [[BuildVerificationSystem]] to run functional tests on CI and report back in about an hour.

The distinctive game-specific layer is environment control. Tests need to acquire build artifacts, deploy a playable game setup, start clients and servers, place champions and minions, issue commands through RPC endpoints, observe game state, and assert gameplay outcomes such as damage, vision, rewards, crashes, and asset loading. The source's Kog'Maw example shows a test treating combat behavior as measurable state rather than a manual playtest impression.

The source also treats test trust as an operational process. New tests spend at least one week in staging before entering blocker or core suites, and the standard library bans pure sleeps in favor of conditional waits. Automation therefore improves feedback only when the harness, reporting service, promotion process, and anti-flake conventions keep failures actionable.

## Key Claims
- Automated game testing becomes valuable when live-game change volume and release cadence exceed what manual regression sweeps can cover quickly.
- Game tests often need client/server control, artifact deployment, game-state setup, and RPC-driven observation rather than only isolated function calls.
- Stable feedback requires a harness that hides setup complexity from test writers while preserving local and test-farm parity.
- Flake prevention is a first-class concern; conditional waits and staged test promotion make failures more trustworthy.
- Reporting services matter because automated failures must become actionable tickets, artifact tags, notifications, and historical trends.
- Automation complements rather than replaces manual QA by freeing analysts for creative, destructive, and upstream testing.

## Evidence
- Scale pressure: [[automated-testing-for-league-of-legends-riot-games-technology]] says League changes quickly, ships every two weeks, and receives well over 100 daily code/content submissions.
- Harness role: [[automated-testing-for-league-of-legends-riot-games-technology]] says BVS acquires artifacts, deploys them, starts systems under test, runs tests, and reports results.
- Gameplay control: [[automated-testing-for-league-of-legends-riot-games-technology]] says tests use RPC endpoints and cover champion abilities, vision rules, minion rewards, and champion/skin loading.
- Flake controls: [[automated-testing-for-league-of-legends-riot-games-technology]] says tests stage for at least one week before promotion and BVS exposes no pure sleep in its standard library.
- Reporting loop: [[automated-testing-for-league-of-legends-riot-games-technology]] describes local result pages, test-farm ticket creation, artifact tagging, committer email, failure aggregation, and pass-history tracking.
- QA complement: [[automated-testing-for-league-of-legends-riot-games-technology]] says automation frees quality analysts to focus on creative testing and upstream defect prevention.

## Counterevidence & Qualifications
The source is a company-authored account of one Riot system and does not compare BVS with other game studios' automation strategies. Its strongest numbers are source-date-specific: about 5,500 cases in 18 minutes per build, about 100,000 cases per day, one-to-two-hour failure reporting, and roughly half of critical or blocker bugs found by BVS. It also says missed bugs generally reflected coverage gaps, so automated game testing still depends on deciding what behavior is worth encoding.

## What Changed
- Created the concept from Riot's League of Legends BVS article.

## Related Concepts
- [[SoftwareVerification]] - automated game testing is domain-specific behavioral verification.
- [[DeterministicTesting]] - reliable game automation depends on reducing flaky timing and environment noise.
- [[TestPyramid]] - game functional suites need to be balanced against faster lower-level checks where possible.
- [[DeploymentAutomation]] - build verification can gate whether artifacts advance to test environments.
- [[GameServerScaleAndStability]] - automated gameplay checks support confidence in live-game behavior.
- [[ServerSideGameLogic]] - game tests often validate interactions between clients, servers, and authoritative game state.

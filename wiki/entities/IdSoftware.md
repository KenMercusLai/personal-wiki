---
title: "Id Software"
type: entity
tags: [game-development, fps, software-engineering]
sources:
  - a-43-year-history-of-first-person-shooters-from-maze-war-to-destiny-2-gamesradar
  - john-carmack-on-inlined-code
last_updated: 2026-10-01
knowledge_schema: synthesis-v1
---

## Overview
[[IdSoftware]] is represented as a technically influential game developer whose FPS work and real-time engineering practices shaped both player-facing genre conventions and source-level reliability concerns.

## Current Profile
GamesRadar+ depicts Id Software as the central PC-era force that moved first-person shooters from experiments toward a mainstream genre through Wolfenstein 3D, Doom, and Quake. Carmack's internal coding-style email adds a narrower operating view: recurring 60 Hz frame work made execution order, latency, worst-case timing, hidden state updates, and subsystem nesting practical engineering concerns inside the studio.

## Key Characteristics
- Built a key early PC FPS lineage from technical experiments through Wolfenstein 3D, Doom, and Quake.
- Combined rendering progress with fast action pacing, tactile shooting, multiplayer, and modding.
- Helped establish competitive community practices around Quake.
- Worked under recurring real-time frame constraints where small ordering changes could add perceptible latency.
- Serves as the setting for Carmack's attempt to make stateful execution paths more visible and consistent.

## Evidence
- Genre development: [[a-43-year-history-of-first-person-shooters-from-maze-war-to-destiny-2-gamesradar]] traces Id's progression from Hovertank 3D and Catacomb 3-D through Wolfenstein 3D, Doom, and Quake.
- Multiplayer and community: [[a-43-year-history-of-first-person-shooters-from-maze-war-to-destiny-2-gamesradar]] credits Doom and Quake with modding, co-op, deathmatch, clans, advanced movement, and competitive culture.
- Real-time engineering context: [[john-carmack-on-inlined-code]] discusses Id's 60 Hz target, nested frame operations, user-command generation, worst-case performance, and input-latency risks.
- Coding practice: [[john-carmack-on-inlined-code]] says Carmack began applying source-level inlining and pure-function guidance to his Id code after an Armadillo Aerospace experiment.

## Qualifications
The FPS history is a broad journalistic retrospective, while the engineering source is one programmer's 2007 internal recommendation with 2014 commentary. Together they do not establish company-wide adoption, measured defect reduction, a complete studio engineering culture, or Id Software's later business and ownership history.

## What Changed
- Added a source-bounded view of Id Software's real-time engineering constraints.
- Connected frame ordering, latency, and state visibility to the studio's game-development context.

## Relationships
- [[FirstPersonShooterEvolution]] - Id Software is a central developer in the PC branch of the genre's evolution.
- [[JohnCarmack]] - Carmack supplies the source's internal engineering perspective on Id's frame-loop code.
- [[ExecutionPathTransparency]] - recurring frame execution makes ordering and hidden work operational concerns at Id.
- [[EpicGames]] - another PC FPS studio associated with arena multiplayer.
- [[Valve]] - another PC FPS studio whose work built on the mature post-Doom ecosystem.

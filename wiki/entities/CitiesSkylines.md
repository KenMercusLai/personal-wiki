---
title: "Cities: Skylines"
type: entity
tags: [game, city-builder, road-design, modding]
sources:
  - art-of-roads-in-games
last_updated: 2026-10-08
knowledge_schema: synthesis-v1
---

## Overview
[[CitiesSkylines]] is a city-building game series used by the source to illustrate both the expressive progress and geometric limitations of player-built road systems.

## Current Profile
The source positions the first Cities: Skylines as a major advance over earlier SimCity road tools because players could place freeform roads, merge them at arbitrary angles, and build multi-level interchanges. Community mods then enabled more realistic merge lanes, markings, transitions, and complex constructions such as a five-lane turbo roundabout.

Cities: Skylines 2 is presented as improving lane and marking realism enough to look convincing to an untrained observer. Yet the source's extreme examples still show tight turns producing pinched lane spacing, overlapping markings, and distorted intersection edges, which the author attributes to the underlying unconstrained spline model.

## Key Characteristics
- Gives players freeform road placement, arbitrary-angle intersections, and multi-elevation construction.
- Supports a modding community that extends road markings, merge geometry, and intersection control.
- Serves as a practical sandbox for elaborate roundabouts and interchanges.
- Improves visual realism across the series while retaining edge cases at tight curvature.
- Exposes the difference between flexible authoring controls and motion-constrained road geometry.

## Evidence
- Placement freedom: [[art-of-roads-in-games]] describes free placement, arbitrary-angle merging, and flyovers as the first game's largest road-building breakthrough.
- Modding depth: [[art-of-roads-in-games]] shows a detailed five-lane turbo roundabout with guided lanes and realistic markings.
- Persistent geometry limits: [[art-of-roads-in-games]] shows looping ramps, pinched tight turns, crossing markings, and distorted inner edges.
- Sequel refinement: [[art-of-roads-in-games]] says Cities: Skylines 2 improved lane and marking realism, while retaining failures in extreme curve layouts.

## Qualifications
This profile comes from one technically motivated player's retrospective rather than developer documentation, comparative testing, or a complete review of either game. The screenshots demonstrate possible constructions and failure cases, but do not establish how common they are or whether every shown artifact follows from Bézier offsets alone.

## What Changed
- Created a source-bounded profile of the series' road-authoring freedom, mod ecosystem, visual advances, and tight-curve limitations.

## Relationships
- [[ProceduralRoadGeometry]] - Cities: Skylines is the source's main case for the tradeoff between freeform editing and constrained road construction.
- [[IndieGameDevelopment]] - the series provides a quality benchmark that the source says independent road-system tools rarely match.
- [[RamerDouglasPeuckerAlgorithm]] - both involve computational geometry for paths, but solve construction and simplification problems respectively.

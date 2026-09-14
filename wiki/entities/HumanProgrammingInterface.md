---
title: "Human Programming Interface"
type: entity
tags: [personal-data, software, data-interface]
sources:
  - blog-beepb00p-map-of-my-personal-data-infrastructure
last_updated: 2026-09-14
knowledge_schema: synthesis-v1
---

## Overview
[[HumanProgrammingInterface]] is the personal-data access layer in beepb00p's infrastructure map, sitting between exported files and higher-level tools.

## Current Profile
The inspected diagram places HPI after the filesystem layer and before user-facing uses such as [[Promnesia]], [[Orger]], Memacs, Jupyter, HTTP APIs, spreadsheets, and InfluxDB. Its role is to turn many exported personal datasets into queryable modules for locations, messaging, social activity, reading, browser history, health, sleep, exercise, and related data.

## Key Characteristics
- Sits above filesystem exports rather than replacing them.
- Provides module-level access to many personal data domains.
- Feeds several different interfaces instead of one monolithic app.
- Accepts heterogeneous upstream formats including sqlite, json, zip/json, html, orgmode, tcx, workouts, and gpx tracks.
- Includes WIP integrations, showing the layer is continuously extended.
- Has parallel contribution or fork activity from Sean Breckenridge for some modules.

## Evidence
- Layer placement: [[blog-beepb00p-map-of-my-personal-data-infrastructure]] shows HPI between local files and downstream use cases.
- Module breadth: [[blog-beepb00p-map-of-my-personal-data-infrastructure]] lists HPI modules for location, messenger, VK, Twitter, Discord, Pinboard, GitHub, Pocket, Reddit, Instapaper, Hacker News, Kobo, Bluemaestro, body weight, blood, sleep, and exercise.
- Interface fan-out: [[blog-beepb00p-map-of-my-personal-data-infrastructure]] connects HPI to Promnesia, Orger, Memacs, Jupyter, an HTTP API, spreadsheets, and InfluxDB.
- Heterogeneous inputs: [[blog-beepb00p-map-of-my-personal-data-infrastructure]] shows filesystem artifacts in sqlite, json, zip/json, html, orgmode, tcx, workouts, and gpx formats.
- Collaboration note: [[blog-beepb00p-map-of-my-personal-data-infrastructure]] says some modules/packages marked in the diagram were developed by Sean Breckenridge, who forked HPI and works on it in parallel.

## Qualifications
The source does not benchmark HPI, document all modules, or prove correctness of the data transformations. The diagram marks some paths as WIP and says the map is incomplete.

## What Changed
- Created the entity as the central access-layer project in beepb00p's personal data infrastructure.

## Relationships
- [[DataLiberation]] - HPI makes exported personal data programmatically usable.
- [[PersonalDataInfrastructure]] - HPI is the middle access layer in the mapped stack.
- [[PersonalDataMirror]] - HPI helps local mirrors become queryable rather than merely archived.
- [[Promnesia]] - consumes HPI data for browsing and recall workflows.
- [[Orger]] - consumes HPI data for plaintext mirrors and queues.

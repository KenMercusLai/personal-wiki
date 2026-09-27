---
title: "Redux"
type: entity
tags: [software, state-management, javascript]
sources:
  - dissecting-twitters-redux-store-statuscode-medium
last_updated: 2026-09-27
knowledge_schema: synthesis-v1
---

## Overview
[[Redux]] is a JavaScript state container represented here through a reverse-engineered 2017 snapshot of Twitter's mobile-web client.

## Current Profile
The inspected [[Twitter]] store uses Redux to keep canonical entity records separate from the structures that order and load a timeline. Tweets are keyed by ID in an entity table, the home timeline holds ordered references to those IDs, top and bottom cursors identify loading boundaries, timestamps record recent fetches, and separate status maps track entity availability. This is a bounded example of Redux as an application-state coordination layer rather than evidence for every Redux design or version.

## Key Characteristics
- Centralizes several application state slices in one inspectable tree.
- Supports normalized entity tables keyed by stable identifiers.
- Separates canonical tweet payloads from timeline ordering and pagination state.
- Keeps request or availability status alongside entity collections.

## Evidence
- Store access and slices: [[dissecting-twitters-redux-store-statuscode-medium]] reaches the live state through the selected React root and shows multiple top-level slices.
- Normalized records: [[dissecting-twitters-redux-store-statuscode-medium]] shows tweet objects keyed by ID under `entities/tweets/entities`.
- Timeline coordination: [[dissecting-twitters-redux-store-statuscode-medium]] shows an ordered home-timeline array, top and bottom cursors, fetch timestamps, and per-ID status maps.

## Qualifications
The source is an unofficial DevTools inspection of one 2017 Twitter client. The screenshots establish visible state shape more strongly than runtime behavior: the author did not observe non-loaded fetch statuses and explicitly describes deduplication and partial-rendering behavior as guesses. This page does not describe Redux's full API, later toolkit conventions, or current Twitter/X architecture.

## What Changed
- Created the entity from Twitter's historical mobile-web state-store case.

## Relationships
- [[Twitter]] - application supplying the observed production-scale store example.
- [[ClientStateNormalization]] - design pattern used to separate entity payloads from timeline references.
- [[DeveloperExperience]] - live state inspection makes application structure visible during debugging.
- [[SystemArchitecturePrinciples]] - the store divides records, ordering, pagination boundaries, and loading state.

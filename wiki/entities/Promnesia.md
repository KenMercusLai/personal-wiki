---
title: "Promnesia"
type: entity
tags: [personal-data, browser-history, search]
sources:
  - blog-beepb00p-map-of-my-personal-data-infrastructure
last_updated: 2026-09-14
knowledge_schema: synthesis-v1
---

## Overview
[[Promnesia]] is a personal browsing-memory and search tool in beepb00p's mapped data infrastructure.

## Current Profile
The inspected diagram places Promnesia downstream of [[HumanProgrammingInterface]] and connected to a browser extension, ArchiveBox, and read-only data mirrors. It draws on sources such as Pocket, Reddit, Hacker News, Pinboard, Discord, Instapaper, Twitter, GitHub, Messenger, and VK to help the user rediscover previously encountered web material.

## Key Characteristics
- Uses personal data to augment browser-history recall.
- Consumes multiple HPI-backed sources rather than only browser-native history.
- Connects with a browser extension as a user-facing interface.
- Can feed or connect to ArchiveBox for web preservation.
- Operates over read-only data mirrors rather than treating upstream services as the only source of truth.

## Evidence
- Tool purpose: [[blog-beepb00p-map-of-my-personal-data-infrastructure]] links Promnesia to a post about fixing browser history.
- Source breadth: [[blog-beepb00p-map-of-my-personal-data-infrastructure]] shows HPI modules for Pocket, Reddit, Hacker News, Pinboard, Discord, Instapaper, Twitter, GitHub, Messenger, and VK feeding Promnesia.
- Browser interface: [[blog-beepb00p-map-of-my-personal-data-infrastructure]] connects Promnesia to a browser extension.
- Preservation path: [[blog-beepb00p-map-of-my-personal-data-infrastructure]] connects Promnesia to ArchiveBox.

## Qualifications
The source describes Promnesia inside a personal infrastructure map and does not independently test retrieval quality, browser support, or preservation behavior.

## What Changed
- Created the entity from the inspected infrastructure diagram.

## Relationships
- [[HumanProgrammingInterface]] - supplies the personal-data inputs Promnesia uses.
- [[PersonalDataMirror]] - Promnesia searches across local read-only mirrors of prior activity.
- [[PersonalDataInfrastructure]] - Promnesia is a downstream user-facing tool in the stack.
- [[Instapaper]] - one source feeding Promnesia.
- [[Twitter]] - one source feeding Promnesia.

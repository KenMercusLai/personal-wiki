---
title: "Orger"
type: entity
tags: [personal-data, plaintext, productivity]
sources:
  - blog-beepb00p-map-of-my-personal-data-infrastructure
last_updated: 2026-09-14
knowledge_schema: synthesis-v1
---

## Overview
[[Orger]] is a plaintext mirror and queue tool in beepb00p's mapped personal data infrastructure.

## Current Profile
The diagram presents Orger as a user-facing layer over [[HumanProgrammingInterface]] data. It creates plaintext reflections of sources such as Kobo, Twitter, Instapaper, YouTube, Hypothesis, GitHub, and Polar, and it supports queues such as Kobo-to-org, Instapaper-to-org, Reddit, and Hacker News.

## Key Characteristics
- Converts personal data into plaintext files.
- Works as both a mirror system and an inbound-content queue.
- Consumes data through [[HumanProgrammingInterface]] rather than talking only to upstream services.
- Bridges personal data infrastructure with tools such as Emacs, Doom Emacs, and Logseq.
- Handles reading, social, code, and web sources rather than a single domain.

## Evidence
- Plaintext role: [[blog-beepb00p-map-of-my-personal-data-infrastructure]] labels Orger as a plaintext reflection of one's digital self.
- Mirror sources: [[blog-beepb00p-map-of-my-personal-data-infrastructure]] lists Kobo, Twitter, Instapaper, YouTube, Hypothesis, GitHub, Polar, and more as Orger mirrors.
- Queue sources: [[blog-beepb00p-map-of-my-personal-data-infrastructure]] lists Kobo-to-org, Instapaper-to-org, Reddit, Hacker News, and more as Orger queues.
- HPI dependency: [[blog-beepb00p-map-of-my-personal-data-infrastructure]] shows HPI modules feeding Orger.

## Qualifications
The source does not evaluate Orger's completeness, usability, or maintenance state. Its representation comes from an infrastructure diagram intended as a map, not a formal product specification.

## What Changed
- Created the entity from the inspected infrastructure diagram.

## Relationships
- [[HumanProgrammingInterface]] - supplies the data Orger mirrors and queues.
- [[PersonalDataMirror]] - Orger provides plaintext reflections of personal data.
- [[PersonalDataInfrastructure]] - Orger is a user-facing output layer in the stack.
- [[Instapaper]] - one reading source mirrored or queued through Orger.
- [[Twitter]] - one social source mirrored through Orger.

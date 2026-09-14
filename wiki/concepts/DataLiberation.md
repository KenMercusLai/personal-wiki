---
title: "Data Liberation"
type: concept
tags: [personal-data, interoperability, data-ownership]
sources:
  - blog-beepb00p-map-of-my-personal-data-infrastructure
last_updated: 2026-09-14
knowledge_schema: synthesis-v1
---

## Definition
[[DataLiberation]] is the practice of extracting, preserving, and reusing personal data outside the platforms that originally collected or mediated it.

## Current Synthesis
The beepb00p source treats data liberation as practical infrastructure work under adversarial conditions. The user has to combine official APIs, private APIs, scraping, GDPR exports, archives, manual requests, direct sqlite access, phone-rooting, and custom scripts before data can become local files and reusable programmatic interfaces. The goal is not merely backup; it is continuity, search, analysis, and personal agency over records that platforms may hide, degrade, restrict, or abandon.

## Key Claims
- Data liberation requires many extraction methods because platforms expose data unevenly.
- Local filesystem storage is a key intermediate layer because it decouples personal records from service availability.
- Programmatic access layers such as [[HumanProgrammingInterface]] turn exports into reusable data rather than inert archives.
- Platform shutdowns are survivable when exported formats and local pipelines preserve compatibility.
- Interoperability failures create extra operational work for individuals.
- Security boundaries can conflict with ownership when users must root devices to access their own app data.

## Evidence
- Extraction variety: [[blog-beepb00p-map-of-my-personal-data-infrastructure]] shows APIs, scraping, archives, GDPR exports, manual downloads, manual input, local APIs, cloud APIs, and sqlite access.
- Local storage: [[blog-beepb00p-map-of-my-personal-data-infrastructure]] shows exported data accumulating as sqlite, json, zip/json, html, orgmode, tcx, workouts, and gpx files.
- Reuse layer: [[blog-beepb00p-map-of-my-personal-data-infrastructure]] shows HPI feeding search, notebooks, HTTP APIs, spreadsheets, InfluxDB, [[Promnesia]], and [[Orger]].
- Shutdown resilience: [[blog-beepb00p-map-of-my-personal-data-infrastructure]] uses Jawbone and Endomondo as dead-service examples whose data can still remain useful.
- Individual burden: [[blog-beepb00p-map-of-my-personal-data-infrastructure]] says the diagram highlights complexity caused by lack of interoperability.
- Device-access conflict: [[blog-beepb00p-map-of-my-personal-data-infrastructure]] says many phone apps require rooting Android to access app-private data.

## Counterevidence & Qualifications
The source is a practitioner map, not a general survey of platform export rights or a comparison of all possible personal data systems. Its examples are shaped by the author's own services, devices, tools, and technical ability.

## What Changed
- Created the concept from the personal data infrastructure source.

## Related Concepts
- [[PersonalDataMirror]] - data liberation's local-copy goal in the source.
- [[PersonalDataInfrastructure]] - the systems architecture needed to operationalize data liberation.
- [[PersonalKnowledgeManagement]] - overlaps when liberated data becomes searchable notes, queues, or memory aids.
- [[PrivacyProtectionResourceInequality]] - related because data self-defense requires scarce skill, time, and tooling.

---
title: "Map of my personal data infrastructure"
type: source
tags: [data-liberation, personal-infrastructure, personal-data, diagram]
date: 2023-08-19
source_file: /mnt/ken_personal_wiki/Articles/Blog - beepb00p - Map of My Personal Data Infrastructure.md
---

## Summary
[[Beepb00p]] maps a personal data liberation stack intended to approximate a [[PersonalDataMirror]] despite poor platform interoperability. The article and inspected SVG diagram show data moving from devices, phone apps, websites, cloud APIs, manual exports, and local databases into filesystem artifacts, then through [[HumanProgrammingInterface]] into downstream tools such as [[Promnesia]], [[Orger]], Emacs, Logseq, Jupyter, HTTP APIs, spreadsheets, and InfluxDB. The source argues that personal data autonomy currently requires a messy mix of scraping, GDPR exports, manual downloads, phone rooting, compatibility preservation, and ad hoc scripts because many services are hostile or indifferent to export.

## Key Claims
- [[DataLiberation]] in practice is less a single product than an infrastructure map: collection, export, filesystem storage, typed access, and user-facing tools have to be joined by many small adapters.
- [[PersonalDataMirror]] is the guiding goal: keeping a local, queryable, read-only reflection of one's digital life even when upstream platforms are fragmented or dead.
- [[PersonalDataInfrastructure]] becomes complex because data often travels device to phone to cloud to computer instead of moving directly to local storage.
- Anti-API, anti-scraping, fragile private APIs, manual requests, and closed services make export work adversarial rather than routine.
- The inspected diagram shows [[HumanProgrammingInterface]] as the central access layer over filesystem exports, feeding search, browser-history recall, plaintext mirrors, queues, notebooks, APIs, spreadsheets, and metrics stores.
- The Endomondo-to-RunnerUp example shows why format compatibility matters: preserved data shape can let a user switch away from a discontinued platform without losing analytic continuity.
- Android app sandboxing can conflict with personal data ownership when rooting becomes the only practical way to extract data from app-private directories.

## Key Quotes
> "personal data mirror" - goal the author wants to approximate.

> "indirection is crazy" - summary of device-phone-cloud-computer data paths.

## Connections
- [[Beepb00p]] - author and owner of the mapped infrastructure.
- [[DataLiberation]] - central practice of extracting and retaining usable personal data.
- [[PersonalDataMirror]] - goal of keeping local read-only reflections of digital activity.
- [[PersonalDataInfrastructure]] - broader stack pattern shown by the map.
- [[HumanProgrammingInterface]] - central access layer that normalizes exported personal data for reuse.
- [[Promnesia]] - browser-history and personal-search tool fed by HPI modules.
- [[Orger]] - plaintext mirror and queue layer for personal data.
- [[Android]] - platform context for phone-rooting and app-private data access constraints.
- [[Twitter]] - example service in the diagram with API, scraping, and archive paths.
- [[Instapaper]] - example readable-content source feeding exports, HPI, Promnesia, and Orger.

## Contradictions
- No direct contradictions found. The source qualifies the wiki's existing mobile-platform view by adding a user-sovereignty concern: Android's security sandbox can make personal data extraction harder even as Android remains a broad mobile ecosystem.

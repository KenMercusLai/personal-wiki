---
title: "Personal Data Infrastructure"
type: concept
tags: [personal-data, infrastructure, interoperability]
sources:
  - blog-beepb00p-map-of-my-personal-data-infrastructure
last_updated: 2026-09-14
knowledge_schema: synthesis-v1
---

## Definition
[[PersonalDataInfrastructure]] is a user-controlled stack for collecting, exporting, storing, normalizing, searching, and reusing personal data across devices, apps, websites, and services.

## Current Synthesis
The beepb00p map shows personal data infrastructure as a layered system: devices and services produce data, exporters pull or request it, the filesystem stores it in many formats, [[HumanProgrammingInterface]] normalizes access, and tools such as [[Promnesia]] and [[Orger]] make the data useful. Its main lesson is that personal infrastructure inherits the integration problems of the surrounding platform ecosystem. When services lack stable APIs or direct export, the stack fills with manual steps, scrapers, archive downloads, and WIP adapters.

## Key Claims
- The stack has distinct layers: sources, phone or cloud intermediaries, export mechanisms, local files, access modules, and use cases.
- Direct local ownership is often blocked by indirection through phones and clouds.
- Export tools are brittle because service APIs can be private, closed, rate-limited, or discontinued.
- A common access layer prevents each downstream use case from reinventing every exporter.
- User-facing value appears in search, browser memory, plaintext notes, queues, notebooks, dashboards, APIs, spreadsheets, and metrics stores.
- The system is permanently incomplete because personal data sources and platform behavior keep changing.

## Evidence
- Layered diagram: [[blog-beepb00p-map-of-my-personal-data-infrastructure]] shows devices, Android phone apps, cloud services, export scripts, filesystem formats, HPI, and downstream tools.
- Indirection: [[blog-beepb00p-map-of-my-personal-data-infrastructure]] describes device-to-phone-to-cloud-to-computer paths.
- Fragility: [[blog-beepb00p-map-of-my-personal-data-infrastructure]] marks private APIs, API limitations, closed APIs, scraping, archives, GDPR exports, dead services, and fragile paths.
- Common access: [[blog-beepb00p-map-of-my-personal-data-infrastructure]] places [[HumanProgrammingInterface]] between files and many use cases.
- Use-case breadth: [[blog-beepb00p-map-of-my-personal-data-infrastructure]] connects data to Promnesia, Orger, Emacs, Logseq, Jupyter, HTTP APIs, spreadsheets, InfluxDB, and personal analysis posts.
- Incompleteness: [[blog-beepb00p-map-of-my-personal-data-infrastructure]] says the map is incomplete and marks some integrations as WIP.

## Counterevidence & Qualifications
This infrastructure pattern is source-scoped to a technically sophisticated user's personal stack. It may be too labor-intensive for ordinary users and does not solve legal, account-access, or platform-policy constraints by itself.

## What Changed
- Created the concept from the article and inspected SVG diagram.

## Related Concepts
- [[DataLiberation]] - the motivating practice for the infrastructure.
- [[PersonalDataMirror]] - the local read-only representation the infrastructure approximates.
- [[PersonalKnowledgeManagement]] - one downstream use for searchable personal data.
- [[CentralizedLogging]] - analogous infrastructure pattern for bringing distributed records into queryable storage.

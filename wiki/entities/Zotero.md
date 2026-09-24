---
title: "Zotero"
type: entity
tags: [software, reference-management, research]
sources:
  - alexandra-phelan-an-updated-academic-workflow-zotero-and-obsidian
last_updated: 2026-09-24
knowledge_schema: synthesis-v1
---

## Overview
[[Zotero]] is the reference-management application that owns source metadata, PDF attachments, annotations, citekeys, and citation data in the documented [[AcademicResearchWorkflow]].

## Current Profile
The source presents Zotero as the research library at the front of the workflow. Browser connectors or manual entry create bibliographic records; attached PDFs can be read and annotated in the application; Better BibTeX supplies consistent citekeys and an automatically updated bibliography file; and downstream integrations send references, annotations, and citations into Obsidian or Pandoc-based manuscripts.

## Key Characteristics
- Stores bibliographic metadata and attached source files in a persistent research library.
- Supports in-application PDF reading, highlights, and notes in the source's Zotero 6 setup.
- Can insert formatted citations and switch among publication styles.
- Uses Better BibTeX in this workflow to create stable author-year citekeys and a `.bib` library.
- Exposes metadata and annotations to Obsidian through Zotero Integration.
- Acts as the citation-data source for Pandoc manuscript export.

## Evidence
- Library and annotation role: [[alexandra-phelan-an-updated-academic-workflow-zotero-and-obsidian]] describes a 15-year library of metadata-linked PDFs read and annotated inside Zotero.
- Citation role: [[alexandra-phelan-an-updated-academic-workflow-zotero-and-obsidian]] reports switching among APA, Bluebook, and Nature styles.
- Interoperability: [[alexandra-phelan-an-updated-academic-workflow-zotero-and-obsidian]] uses Better BibTeX, Zotero Integration, and Pandoc to connect the library to notes and manuscripts.

## Qualifications
This profile reflects a personal workflow documented in 2023 and explicitly refers to Zotero 6. Plugin compatibility and current product behavior are not established by the source, and the source does not compare Zotero with other reference managers.

## What Changed
- Created a profile for Zotero's role as the source and citation system in an academic writing pipeline.

## Relationships
- [[AcademicResearchWorkflow]] - Zotero owns collection, source metadata, annotation, and citation data in the workflow.
- [[Obsidian]] - receives imported metadata, links, annotations, and citation material from Zotero.
- [[Pandoc]] - consumes the exported BibTeX library and citekeys during manuscript conversion.
- [[ReadingNoteWorkflow]] - Zotero annotations become source material inside per-reference literature notes.
- [[AlexandraPhelan]] - documents using Zotero as a long-lived academic research library.

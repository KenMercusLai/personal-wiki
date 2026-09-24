---
title: "Pandoc"
type: entity
tags: [software, document-conversion, citations]
sources:
  - alexandra-phelan-an-updated-academic-workflow-zotero-and-obsidian
last_updated: 2026-09-24
knowledge_schema: synthesis-v1
---

## Overview
[[Pandoc]] is the document-conversion and citation-processing tool used to turn citekey-bearing Markdown drafts into formatted DOCX manuscripts in the documented [[AcademicResearchWorkflow]].

## Current Profile
The source positions Pandoc as the bridge between a low-friction Markdown drafting environment and publication workflows that expect word-processor files and prescribed citation styles. An exported BibTeX file supplies reference data, Pandoc citations remain style-neutral in the draft, and a CSL file can select the output style during conversion.

## Key Characteristics
- Converts Markdown manuscripts to DOCX for collaboration or submission.
- Resolves `[@citekey]` references against a BibTeX bibliography.
- Defers citation formatting so the same draft can target different journal styles.
- Accepts optional CSL configuration, with Chicago author-date described as the default in the source's setup.
- Can be invoked through an Obsidian plugin or directly from a terminal.

## Evidence
- Conversion pipeline: [[alexandra-phelan-an-updated-academic-workflow-zotero-and-obsidian]] specifies exporting Zotero data to `.bib`, pointing Pandoc to it, selecting an optional CSL style, and exporting DOCX.
- Draft portability: [[alexandra-phelan-an-updated-academic-workflow-zotero-and-obsidian]] recommends Pandoc citations because formatting can change without rewriting in-text citations.
- Invocation options: [[alexandra-phelan-an-updated-academic-workflow-zotero-and-obsidian]] describes both an Obsidian command and direct terminal use on macOS.

## Qualifications
The source gives a practitioner setup rather than a full Pandoc capability review. Exact defaults, plugin behavior, and compatibility are tied to the author's 2023 environment and may not generalize to current installations.

## What Changed
- Created a profile for Pandoc's conversion and citation-processing role in a Markdown-first manuscript workflow.

## Relationships
- [[AcademicResearchWorkflow]] - Pandoc bridges note-centered drafting and submission-oriented document formats.
- [[Zotero]] - supplies the BibTeX bibliography and stable citekeys consumed at export.
- [[Obsidian]] - hosts the Markdown draft and plugin command that invokes conversion.
- [[AlexandraPhelan]] - recommends Pandoc citations for switching publication styles.

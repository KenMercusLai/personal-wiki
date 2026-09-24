---
title: "Academic Research Workflow"
type: concept
tags: [research, writing, note-taking, citations]
sources:
  - alexandra-phelan-an-updated-academic-workflow-zotero-and-obsidian
last_updated: 2026-09-24
knowledge_schema: synthesis-v1
---

## Definition
[[AcademicResearchWorkflow]] is an end-to-end system for collecting sources, preserving metadata, reading and annotating, synthesizing notes, drafting manuscripts, managing citations, tracking publication work, and exporting required deliverables.

## Current Synthesis
The available workflow assigns distinct ownership to interoperable tools. [[Zotero]] is the source-of-record for bibliography data, PDFs, annotations, and citekeys; [[Obsidian]] imports that material into linked literature notes and supports synthesis, Markdown drafting, and project tracking; [[Pandoc]] resolves style-neutral citations against an exported bibliography and converts manuscripts to DOCX. Stable citekeys join these layers: the same key names a source record, an internal note, and an in-text citation while syntax distinguishes links from citations. The design reduces duplicate entry and keeps early drafting portable, but its value depends on disciplined templates, plugin compatibility, and enough repeated publication work to justify setup cost.

## Key Claims
- Clear ownership boundaries among source management, note synthesis, drafting, and conversion can make an academic toolchain coherent.
- Stable citekeys provide the shared identifier that connects bibliographic records, literature notes, citations, and exports.
- Source-linked literature notes can centralize metadata and annotations, but they remain inputs to synthesis rather than completed intellectual output.
- Markdown separates drafting from final presentation and preserves a durable, portable working format.
- Style-neutral Pandoc citations reduce rework when a manuscript moves among journals with different citation requirements.
- Indexes, templates, autocomplete, and publication trackers make repeated research work easier to navigate after initial setup.

## Evidence
- Tool boundaries: [[alexandra-phelan-an-updated-academic-workflow-zotero-and-obsidian]] assigns collection, PDF annotation, and citation data to Zotero; linked notes and drafting to Obsidian; and output conversion to Pandoc.
- Identifier continuity: [[alexandra-phelan-an-updated-academic-workflow-zotero-and-obsidian]] uses author-year citekeys in Zotero, `@citekey` note titles, internal wikilinks, Pandoc citations, and BibTeX export.
- Literature-note automation: [[alexandra-phelan-an-updated-academic-workflow-zotero-and-obsidian]] imports metadata, Zotero links, PDF highlights, and notes into templated per-reference pages.
- Publication flexibility: [[alexandra-phelan-an-updated-academic-workflow-zotero-and-obsidian]] uses CSL and Pandoc to change citation style and produce DOCX without abandoning the Markdown draft.
- Workflow support: [[alexandra-phelan-an-updated-academic-workflow-zotero-and-obsidian]] uses Dataview indexes, a reference sidebar, and Obsidian project tracking around the core writing loop.

## Counterevidence & Qualifications
The evidence is one academic's self-reported setup, not a controlled comparison of tools or outcomes. Plugin dependencies can introduce compatibility and maintenance risk, imported annotations can become an accumulation layer rather than synthesis, and the source acknowledges a steeper learning curve for people with limited programming experience. Product versions and plugin recommendations are historically scoped to 2023. The workflow is most justified when repeated citation-style changes, substantial source libraries, and Markdown drafting are real constraints.

## What Changed
- Created a concept for the complete collection-to-submission workflow rather than treating its tools as independent note applications.
- Distinguished automated source-linked literature notes from synthesized claims ready for writing.

## Related Concepts
- [[ReadingNoteWorkflow]] - imported literature notes supply traceable reading material that still requires selection and synthesis.
- [[PersonalKnowledgeManagement]] - the workflow is a research-specific PKM system organized around manuscript output.
- [[AcademicWriting]] - the toolchain supports drafting and evidence handling while academic writing supplies the reasoning practice.
- [[NoteToolFit]] - the workflow depends on matching distinct applications to collection, synthesis, drafting, and export tasks.
- [[KnowledgeOutput]] - manuscript production is the practical output test for the research system.

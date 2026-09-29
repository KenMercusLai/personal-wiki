---
title: "File Over App"
type: concept
tags: [files, portability, digital-ownership, knowledge-management]
sources:
  - how-i-use-obsidian
last_updated: 2026-09-29
knowledge_schema: synthesis-v1
---

## Definition
[[FileOverApp]] is the principle that durable digital artifacts should live in files the user controls and can retrieve and read independently of the application currently used to edit them.

## Current Synthesis
The source applies this principle to a personal knowledge vault: [[Obsidian]] is valuable partly because a vault is an ordinary folder of Markdown files. The application supplies linking, properties, templates, graph navigation, and publishing conveniences, while the underlying artifacts remain accessible outside it. File control improves custody and creates migration options, but format readability alone does not guarantee preservation of application-specific behavior, metadata fidelity, synchronization, or a maintainable organization.

## Key Claims
- Durable digital work should be stored in user-controlled files rather than existing only inside an application's proprietary boundary.
- Common readable formats reduce basic retrieval dependence on a particular vendor or interface.
- An application can add substantial workflow value without becoming the sole custodian of the underlying artifacts.
- File ownership supports external versioning, transformation, and publishing pipelines.
- Portability remains conditional when plugins, metadata conventions, or application behaviors are not represented completely in the files.

## Evidence
- Vault substrate: [[how-i-use-obsidian]] emphasizes that an Obsidian vault is simply a folder of files and connects this property to artifact longevity.
- Readable format: [[how-i-use-obsidian]] recommends standard Markdown and avoids non-standard syntax where possible.
- External pipeline: [[how-i-use-obsidian]] pushes notes through GitHub and compiles Markdown with Jekyll and Netlify, illustrating reuse outside the editor.
- Application layer: [[how-i-use-obsidian]] still relies on Obsidian features and plugins for properties, category views, maps, synchronization, clipping, and navigation.

## Counterevidence & Qualifications
The concept is supported here by one author's design principle and workflow, not a migration study or preservation audit. Plain files can still depend on undocumented naming, links, folder layout, frontmatter, attachments, plugins, or external services. User custody also transfers responsibility for backups, integrity, security, synchronization, and format maintenance to the user.

## What Changed
- Created the concept from the source's explicit rationale for using an ordinary Markdown-file vault.

## Related Concepts
- [[PersonalKnowledgeManagement]] - file custody provides a durable substrate for a personal archive.
- [[KnowledgeAsCode]] - repository operations can validate, version, derive, and publish file-based knowledge.
- [[NoteToolFit]] - an application's suitability includes how well it exposes and preserves the user's underlying material.
- [[DigitalArchiveOrganization]] - long-lived file custody still requires workable retrieval, structure, and preservation practices.
- [[Obsidian]] - exemplifies an application whose vault content remains ordinary files.

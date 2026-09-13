---
title: "Commuter"
type: entity
tags: [open-source, notebooks, sharing]
sources:
  - beyond-interactive-notebook-innovation-at-netflix-netflix-techblog-medium
last_updated: 2026-09-14
knowledge_schema: synthesis-v1
---

## Overview
[[Commuter]] is Netflix's lightweight notebook viewing and sharing service for safely inspecting notebooks stored locally or on S3.

## Current Profile
The Netflix source frames Commuter as a collaboration and safety layer. As users shared active notebook URLs, concurrent access created accidental overwrite risks. Commuter responds by letting users view notebooks in a read-only state through Jupyter-compatible contents APIs.

Its role is therefore narrower than notebook execution. Commuter makes notebooks discoverable and inspectable without turning every viewer into a writer or risking modification of production jobs and live-running notebooks.

## Key Characteristics
- Provides read-only notebook viewing and sharing.
- Offers a directory explorer for finding notebooks.
- Reads notebooks stored locally or on Amazon S3.
- Exposes Jupyter-compatible contents APIs for files, directory listings, and metadata.
- Reduces overwrite risk when collaborators share notebook URLs.

## Evidence
- Service definition: [[beyond-interactive-notebook-innovation-at-netflix-netflix-techblog-medium]] calls Commuter a lightweight vertically scalable service for viewing and sharing notebooks.
- Storage reach: [[beyond-interactive-notebook-innovation-at-netflix-netflix-techblog-medium]] says Commuter can read notebooks stored locally or on S3.
- API compatibility: [[beyond-interactive-notebook-innovation-at-netflix-netflix-techblog-medium]] says Commuter surfaces Jupyter APIs for `/files` and `/api/contents`.
- Collaboration trigger: [[beyond-interactive-notebook-innovation-at-netflix-netflix-techblog-medium]] says accidental overwrites from shared notebook URLs led to the need for read-only active notebook sharing.

## Qualifications
This page is limited to Netflix's 2018 description. It does not evaluate Commuter's current project status, access-control model, or fit outside Netflix-style notebook storage.

## What Changed
- Created the entity profile for Commuter as a notebook collaboration and viewing layer.

## Relationships
- [[Jupyter]] - Commuter exposes Jupyter-compatible contents APIs.
- [[NotebookWorkflowInfrastructure]] - Commuter supplies read-only sharing and inspection.
- [[DeveloperExperience]] - safe sharing improves collaboration ergonomics.
- [[AWS]] - Commuter can view notebooks stored on S3 in the source.

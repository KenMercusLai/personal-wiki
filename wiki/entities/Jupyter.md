---
title: "Jupyter"
type: entity
tags: [open-source, notebooks, data-science]
sources:
  - beyond-interactive-notebook-innovation-at-netflix-netflix-techblog-medium
last_updated: 2026-09-14
knowledge_schema: synthesis-v1
---

## Overview
[[Jupyter]] is the open-source notebook ecosystem that Netflix uses as the protocol, file-format, and interaction foundation for its notebook platform.

## Current Profile
The Netflix source presents Jupyter as a modular architecture rather than only a web notebook UI. Its language-agnostic messaging protocol lets a notebook interface talk to kernels that execute code in different languages. Its file format stores code, outputs, and prose together, which makes a notebook useful as both an executable workspace and a later communication artifact.

That separation lets Netflix adapt notebooks to many data-platform roles. The UI can be [[Nteract]], kernels can supply language-specific execution, and supporting services can parameterize, schedule, view, and share notebooks without abandoning the Jupyter artifact model.

## Key Characteristics
- Provides a language-agnostic protocol for communicating with execution kernels.
- Separates the writing interface from the code runtime.
- Stores code, outputs, and Markdown context in one editable file format.
- Supports computational narratives that combine analysis, assumptions, conclusions, and results.
- Serves as the open standard beneath Netflix's notebook platform choices.

## Evidence
- Protocol role: [[beyond-interactive-notebook-innovation-at-netflix-netflix-techblog-medium]] says Jupyter supplies a messaging API for introspecting and executing code through kernels.
- Runtime separation: [[beyond-interactive-notebook-innovation-at-netflix-netflix-techblog-medium]] says the architecture separates where content is written from where code is executed.
- File artifact: [[beyond-interactive-notebook-innovation-at-netflix-netflix-techblog-medium]] says notebooks store code, output, and prose together so results can be revisited without rerunning code.
- Communication role: [[beyond-interactive-notebook-innovation-at-netflix-netflix-techblog-medium]] says notebook prose can document context, assumptions, conclusions, and business framing.
- Ecosystem role: [[beyond-interactive-notebook-innovation-at-netflix-netflix-techblog-medium]] says Netflix relies heavily on the Jupyter ecosystem while choosing modular components that fit its environment.

## Qualifications
This page is source-scoped to Netflix's 2018 use of Jupyter. It does not summarize the full Jupyter project history, current governance, later JupyterLab evolution, security model, or all language kernels.

## What Changed
- Created the entity profile for Jupyter as Netflix's notebook standard.

## Relationships
- [[NotebookWorkflowInfrastructure]] - Jupyter supplies the protocol and artifact model.
- [[Nteract]] - Netflix chose nteract as its notebook UI.
- [[Papermill]] - Papermill parameterizes and executes Jupyter notebooks.
- [[Commuter]] - Commuter views and shares stored notebooks through Jupyter-compatible APIs.
- [[IndustryDataScience]] - Jupyter notebooks support data-science and analytics workflows.

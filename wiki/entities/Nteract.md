---
title: "nteract"
type: entity
tags: [open-source, notebooks, ui]
sources:
  - beyond-interactive-notebook-innovation-at-netflix-netflix-techblog-medium
last_updated: 2026-09-14
knowledge_schema: synthesis-v1
---

## Overview
[[Nteract]] is the React-based notebook UI that Netflix selected for its Jupyter notebook interface.

## Current Profile
The Netflix source presents nteract as a composable, simpler alternative to the classic Jupyter UI. Its role in the notebook platform is to make notebooks approachable for a wider range of data-platform users while still fitting Netflix's frontend stack and design philosophy.

The article's inspected UI images show nteract as more than a code-cell surface. The Data Explorer screenshot includes chart controls, palette adjustment, region coloring, and selectable visualization types, while the parameterization screenshot shows notebook parameters edited directly in a visible cell.

## Key Characteristics
- React-based notebook interface chosen for Netflix's notebook platform.
- Emphasizes simplicity and composability.
- Improves notebook ergonomics through inline cell tooling, drag-and-drop cells, and built-in data exploration.
- Supports language-agnostic data visualization through Data Explorer.
- Provides a UI surface for notebook parameterization.

## Evidence
- UI choice: [[beyond-interactive-notebook-innovation-at-netflix-netflix-techblog-medium]] says Netflix chose nteract as its notebook UI.
- Design fit: [[beyond-interactive-notebook-innovation-at-netflix-netflix-techblog-medium]] says nteract's simplicity and composability align with Netflix's desired interface direction.
- Feature examples: [[beyond-interactive-notebook-innovation-at-netflix-netflix-techblog-medium]] names inline cell toolbars, draggable cells, and a built-in data explorer.
- Visualization evidence: [[beyond-interactive-notebook-innovation-at-netflix-netflix-techblog-medium]] includes a Data Explorer GIF with scatter/contour-style visual exploration controls for generosity, life expectancy, region, multiclass, and chart type.
- Parameter evidence: [[beyond-interactive-notebook-innovation-at-netflix-netflix-techblog-medium]] includes a parameterized-notebook GIF showing editable runtime values such as `alpha` and `ratio`.

## Qualifications
The source describes Netflix's 2018 choice and planned investments. It does not compare nteract with later JupyterLab interfaces, current nteract maintenance status, or adoption outside Netflix.

## What Changed
- Created the entity profile for nteract as Netflix's notebook UI layer.

## Relationships
- [[Jupyter]] - nteract is a UI over the Jupyter notebook model.
- [[NotebookWorkflowInfrastructure]] - nteract supplies the interactive user interface.
- [[DeveloperExperience]] - nteract is used to lower notebook interaction friction.
- [[DataScienceTechnologyAdoption]] - nteract is part of Netflix's organization-wide notebook adoption.

---
title: "Ken Thompson"
type: entity
tags: [software-history, unix, text-editors]
sources:
  - where-vim-came-from
last_updated: 2026-10-19
knowledge_schema: synthesis-v1
---

## Overview
[[KenThompson]] is the Bell Labs computer scientist presented in the source as a Unix co-creator and the developer of the QED-derived `ed` editor at the start of [[UnixEditorLineage]].

## Current Profile
The source connects Thompson's editor work directly to modern Vim behavior. After using QED at Berkeley, he reimplemented and extended it for CTSS and Multics, then built a smaller `ed` while assembling early Unix in 1969. `ed` was adapted to paper-teleprinter interaction, yet its modal commands, write/quit vocabulary, and substitution grammar survived through `vi` into [[Vim]].

## Key Characteristics
- Used and reimplemented QED before creating Unix `ed`.
- Extended QED with regular-expression search and substitution in the Multics era.
- Co-created Unix after Bell Labs withdrew from Multics.
- Simplified QED into a single-buffer line editor suited to paper-teleprinter interaction.
- Established editor commands and grammar that remain recognizable in Vim.

## Evidence
- QED background: [[where-vim-came-from]] says Thompson used QED at Berkeley and rewrote it for CTSS and Multics.
- Unix origin: [[where-vim-came-from]] places `ed` among the operating system, shell, editor, and assembler work Thompson scheduled while bootstrapping Unix in 1969.
- Constraint fit: [[where-vim-came-from]] explains that `ed` exposed selected lines because a paper teletype could not clear or continuously redraw a screen; its retained photograph shows Thompson and Dennis Ritchie working at teletypes beside a PDP-11 installation.
- Durable grammar: [[where-vim-came-from]] traces `w`, `q`, `wq`, modal insert/append/change commands, and `s/foo/bar/g` from `ed` into Vim.

## Qualifications
This profile is based on one translated secondary history whose footnotes point to contemporary and first-person sources. It focuses narrowly on editor and Unix origins rather than Thompson's broader work in operating systems, programming languages, or later research.

## What Changed
- Created a canonical profile linking Thompson's QED and `ed` work to Unix editor conventions that persist in Vim.

## Relationships
- [[UnixEditorLineage]] - Thompson's QED and `ed` work begins the source's documented editor chain.
- [[Vim]] - Vim retains commands and interaction grammar inherited from `ed`.
- [[BillJoy]] - Joy later extended the `ed` family into `ex` and visual `vi`.
- [[ConstraintShapedInterfaceDesign]] - Thompson's line editor reflects the limits of paper-teleprinter interaction.

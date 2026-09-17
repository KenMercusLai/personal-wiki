---
title: "Email Table Layout"
type: concept
tags: [email-design, html-email, web-development]
sources:
  - understanding-email-layout-and-structure
last_updated: 2026-09-17
knowledge_schema: synthesis-v1
---

## Definition
Email table layout is the practice of building HTML email with tables - full-width rows, columns, and container "boxes", often nested inside one another - because email clients, and Microsoft Outlook in particular, do not reliably support modern web layout techniques.

## Current Synthesis
The [[Chamaileon]] tutorial treats table-based layout as a historical necessity rather than a preference: responsive HTML email is still assembled from tables, and templates usually nest several tables so a design holds together in Outlook. Rows, called full-width elements, divide the message into horizontal bands; columns place content side by side; invisible container tables, called boxes, wrap elements to carry padding, margin, border, and background; and spacers or dividers are empty boxes used only for spacing. Because these structural elements can be embedded inside one another, reasonably complex designs can be reproduced without hand-coding.

## Key Claims
- HTML email layout is still table-based and frequently nests tables inside tables to render correctly in Outlook.
- Rows are full-width horizontal elements that organize a template into stacked bands and can be split into one or two cells.
- Columns place content side by side and can be configured for count, width, and mobile behavior.
- Container tables, or boxes, are invisible frames that give elements spacing, borders, and background, and can hide their content per device.
- Spacer and divider elements are empty boxes used purely for spacing, which makes them useful when recreating a supplied design.
- Structural elements can be embedded in one another to build complex layouts without writing code.

## Evidence
Table-based and nested layout:
- [[understanding-email-layout-and-structure]] says responsive HTML email is still based on tables and usually nests many tables so the design looks right in Microsoft Outlook.

Rows as full-width bands:
- [[understanding-email-layout-and-structure]] describes each building block as a separate row, or full-width element, that can be divided into one or two cells with distinct backgrounds.

Columns:
- [[understanding-email-layout-and-structure]] shows columns placing images and text side by side, with control over column count, width, and mobile display.

Container boxes:
- [[understanding-email-layout-and-structure]] presents boxes as invisible tables that frame elements with pixel-level spacing, borders, and backgrounds and can be hidden on mobile or desktop.

Spacers and dividers:
- [[understanding-email-layout-and-structure]] calls a divider or spacer an empty box with spacing, background, and border properties used to customize or rebuild a design.

Embedding structural elements:
- [[understanding-email-layout-and-structure]] builds a boxed three-column block by nesting a second box inside the middle column, showing that layout elements can be embedded in each other.

## Counterevidence & Qualifications
The source is a 2016 vendor tutorial, and numeric limits such as five columns in one structure describe [[Chamaileon]] rather than HTML email as a whole. The author is a marketer who disclaims technical precision, and client rendering behavior has changed since 2016, so the table model should be read as the source's account of the constraints of its time.

## What Changed
- Created the concept from the Chamaileon email-design tutorial.

## Related Concepts
- [[EmailLayoutAndStructure]] - the design layer this table model implements.
- [[ResponsiveEmailDesign]] - reflow and hiding behavior applied to rows and columns.
- [[EmailRenderingConstraints]] - the client limits that force a table-based approach.
- [[HTMLEmailButton]] - a content element placed inside rows and boxes.
- [[Chamaileon]] - the builder whose row, column, and box model the source documents.
- [[EmailMarketingAtScale]] - large-scale sending, where template robustness matters.

---
title: "Chamaileon"
type: entity
tags: [saas, email-design, email-marketing]
sources:
  - understanding-email-layout-and-structure
last_updated: 2026-09-17
knowledge_schema: synthesis-v1
---

## Overview
[[Chamaileon]] is the drag-and-drop email-builder product whose "Email Design Basics for Email Marketers" blog series supplies the wiki's account of how responsive HTML email templates are laid out and structured.

## Current Profile
The source is first-party: it advertises that users can build the designs in its layout editor without writing code, and it explains the editor's rows, columns, boxes, and divider elements while noting where another builder, such as [[Mailchimp]], exposes less control. The tutorial positions Chamaileon around pixel-level control of column width, spacing, borders, and backgrounds, mobile visibility and reordering settings, and a library of free responsive template blocks that users can adapt instead of building from scratch.

## Key Characteristics
- Drag-and-drop email builder: presented as letting marketers create responsive HTML email without coding.
- First-party teaching voice: publishes an "Email Design Basics for Email Marketers" series on its blog.
- Structural element model: organizes templates into full-width rows, columns, boxes, and spacer or divider elements.
- Pixel-level control: emphasizes configurable padding, margin, borders, backgrounds, and column widths.
- Mobile controls: exposes per-element hiding and column reordering for mobile.
- Template library: offers free responsive email templates and predesigned blocks.
- Comparative positioning: describes limited row and column control in [[Mailchimp]]'s editor while recommending HTML buttons and web-safe fonts.

## Evidence
Drag-and-drop builder:
- [[understanding-email-layout-and-structure]] says the article's example layouts were created in Chamaileon with no hand-coding and that readers can build similar designs without coding.

First-party teaching voice:
- [[understanding-email-layout-and-structure]] is the fourth article in Chamaileon's "Email Design Basics for Email Marketers" series.

Structural element model:
- [[understanding-email-layout-and-structure]] describes Chamaileon's rows, columns, boxes, and divider or spacer elements and how they nest.

Pixel-level control:
- [[understanding-email-layout-and-structure]] says the layout editor gives complete control over column count, width, spacing, borders, and backgrounds.

Mobile controls:
- [[understanding-email-layout-and-structure]] says rows and boxes can be hidden per device and columns can be reordered to a single column on mobile.

Template library:
- [[understanding-email-layout-and-structure]] offers free responsive email templates and predesigned blocks so users do not have to recreate blocks from scratch.

Comparative positioning:
- [[understanding-email-layout-and-structure]] says Mailchimp's editor gives less control over rows and columns and instead offers built-in multi-column elements.

## Qualifications
The wiki knows Chamaileon only through its own marketing blog. The article is a 2016 tutorial by a self-described marketer rather than a developer, so product capabilities, limitations, and the comparison with [[Mailchimp]] are source-scoped and may be outdated.

## What Changed
- Created the entity as the publisher and product behind the email-design tutorial.

## Relationships
- [[EmailLayoutAndStructure]] - the design model the product teaches and implements.
- [[EmailTableLayout]] - Chamaileon exposes rows, columns, and boxes as its structural elements.
- [[HTMLEmailButton]] - the product supports HTML-based buttons in templates.
- [[ResponsiveEmailDesign]] - the editor exposes mobile visibility and reordering controls.
- [[EmailRenderingConstraints]] - the tutorial frames its controls as answers to client limitations.
- [[Mailchimp]] - used as the comparison point for a builder with fewer row and column controls.

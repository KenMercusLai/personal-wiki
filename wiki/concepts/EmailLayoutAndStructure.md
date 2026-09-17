---
title: "Email Layout and Structure"
type: concept
tags: [email-design, html-email, information-design]
sources:
  - understanding-email-layout-and-structure
last_updated: 2026-09-17
knowledge_schema: synthesis-v1
---

## Definition
Email layout and structure is the distinction between a template's layout - its overall look and feel - and its structure - the order in which its elements are arranged - together with the small set of reusable building blocks from which marketers assemble a message.

## Current Synthesis
The [[Chamaileon]] tutorial treats email design as a small compositional system rather than a blank canvas. Layout is appearance, structure is sequence, and the conventional marketing sequence runs greeting, headline, body content, call to action, and closing, arranged so that even a reader who only scans can still follow the message. Templates are then built from a short kit of elements - titles, text, images, buttons, rows, and columns - and the governing rule is that content comes first: the goal, target audience, and copy must be settled before any layout is chosen.

## Key Claims
- Layout and structure are separate concerns: layout is the look and feel, while structure is the order in which elements are arranged so the email reads as one connected message.
- Marketing email follows a repeatable structural order of greeting, headline, content, call to action, and closing.
- Templates are assembled from a small kit of building blocks: titles, text, images, buttons, rows, and columns.
- Structure should suit scanning, so emails are broken into bite-sized chunks that still make sense to readers who do not read every word.
- Content precedes design: goal, target audience, and email copy must be written before the layout is chosen, and placeholder text is a bad practice.

## Evidence
Layout versus structure:
- [[understanding-email-layout-and-structure]] defines layout as the email's overall appearance and structure as the arrangement order that makes it feel connected.

Repeatable structural order:
- [[understanding-email-layout-and-structure]] lists greetings, headline, content, call to action, and closing as the usual marketing-email structure.

Building-block kit:
- [[understanding-email-layout-and-structure]] names titles, texts, images, buttons, rows, and columns as the basic building blocks of responsive templates.

Scannable structure:
- [[understanding-email-layout-and-structure]] advises breaking emails into bite-sized chunks for readers who scan rather than read fully.

Content precedes design:
- [[understanding-email-layout-and-structure]] says a template cannot be designed before the goal, audience, and copy are known, and warns against Lorem ipsum.

## Counterevidence & Qualifications
The guidance is a vendor tutorial published on [[Chamaileon]]'s marketing blog, so its conventions describe one email builder's model rather than a validated standard, and the author states he is a marketer who may not use technically precise terms. The "usual structure" is a default for promotional email and may not fit transactional, editorial, or plain-text messages.

## What Changed
- Created the concept from the Chamaileon email-design tutorial.

## Related Concepts
- [[EmailTableLayout]] - implements this structure with rows, columns, and container tables.
- [[ResponsiveEmailDesign]] - rearranges the same structure for small screens.
- [[EmailRenderingConstraints]] - client limits bound how the layout can be expressed.
- [[HTMLEmailButton]] - the call-to-action building block the source recommends.
- [[EmailMarketingAtScale]] - the delivery context these templates are designed to serve.
- [[MobileEmailEngagement]] - device behavior that motivates scannable, responsive structure.

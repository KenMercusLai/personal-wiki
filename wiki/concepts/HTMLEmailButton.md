---
title: "HTML Email Button"
type: concept
tags: [email-design, html-email, call-to-action]
sources:
  - understanding-email-layout-and-structure
last_updated: 2026-09-17
knowledge_schema: synthesis-v1
---

## Definition
An HTML email button is a call-to-action control built from HTML and CSS rather than an image, so that it renders even when a client blocks images and can resize on smaller screens.

## Current Synthesis
The [[Chamaileon]] tutorial recommends HTML-based buttons over image-based buttons for responsive email. Because many clients block images by default, a linked image used as a button can disappear, while an HTML button always shows and can be sized or made fluid on mobile. HTML buttons are also versatile enough for calls to action, menu items, and social-share actions, and they expose ordinary text and box styling such as link target, typography, color, alignment, size, spacing, border, radius, and background.

## Key Claims
- HTML-based buttons are preferred over image-based buttons because they still render when images are blocked.
- HTML buttons can resize, including scaling to full screen width on mobile, which image buttons cannot.
- Buttons are reusable beyond calls to action, serving as menu items and social-share controls.
- Button appearance is configurable through link, typography, color, alignment, size, spacing, border and radius, and background.
- Linking an image and treating it as a button is a common but discouraged practice.

## Evidence
Prefer HTML over image buttons:
- [[understanding-email-layout-and-structure]] says HTML buttons always show, even if images are blocked, while image buttons fail when images are not displayed.

Mobile resizing:
- [[understanding-email-layout-and-structure]] says HTML buttons can resize to the needed size on mobile and can be configured to become full width.

Versatility:
- [[understanding-email-layout-and-structure]] says buttons are used for call-to-actions as well as for menu elements and social-share buttons.

Configurable styling:
- [[understanding-email-layout-and-structure]] lists button properties including link, font type, font size, line height, color, alignment, size behavior, margin, padding, border, radius, and background.

Discouraged image-button practice:
- [[understanding-email-layout-and-structure]] notes that many companies still use images instead of HTML buttons and calls this against best practice.

## Counterevidence & Qualifications
The recommendation comes from [[Chamaileon]]'s marketing tutorial and is not backed by rendered-client testing. The source itself concedes that HTML buttons may look less "fancy" than image buttons, so the tradeoff is reliability and responsiveness against visual polish.

## What Changed
- Created the concept from the Chamaileon email-design tutorial.

## Related Concepts
- [[EmailRenderingConstraints]] - image blocking is the constraint that motivates HTML buttons.
- [[ResponsiveEmailDesign]] - fluid buttons are part of mobile adaptation.
- [[EmailLayoutAndStructure]] - the call-to-action building block within a template.
- [[EmailTableLayout]] - the table structure buttons are placed inside.
- [[Chamaileon]] - the builder whose button options the source documents.

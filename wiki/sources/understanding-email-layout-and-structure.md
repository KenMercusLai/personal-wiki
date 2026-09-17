---
title: "Understanding Email Layout and Structure"
type: source
tags: [email-design, html-email, responsive-design]
date: 2016-12-15
source_file: '/mnt/ken_personal_wiki/Articles/Understanding Email Layout and Structure.md'
---

## Summary
[[Chamaileon]]'s "Email Design Basics for Email Marketers" tutorial separates an email template's layout - its overall look and feel - from its structure - the order in which its elements are arranged - and argues that responsive HTML email is still built from tables, rows, and columns. It inventories the building blocks of a template: the email body background, full-width rows, columns, invisible container "boxes", and the text, image, and button content elements. The article recommends HTML-based buttons over image-based ones because images may be blocked while HTML buttons still render and can resize on mobile, and it closes by showing how a boxed three-column block is assembled by nesting structural elements.

## Key Claims
- Layout is the look and feel of an email, while structure is the order in which elements are arranged so that the message feels connected.
- The usual structure of a marketing email template is greeting, headline, content, call to action, and closing, and emails should be broken into bite-sized chunks for readers who scan.
- Responsive HTML email is still built from tables, and templates often nest many tables inside one another to render correctly in Microsoft Outlook.
- Templates are assembled from rows, columns, and container "boxes": rows are full-width elements, columns place content side by side, boxes carry pixel-level spacing, borders, and backgrounds, and spacers or dividers are empty boxes used for spacing.
- Structural elements can be embedded inside one another, so complex layouts can be reproduced without writing code.
- Content must come before design: the goal, target audience, and email copy have to be known before a layout is chosen, and placeholder text is a bad practice.
- Text styling is limited to web-safe fonts, some effects such as wrapping text around images and rounded images are unreliable, and background images are not supported in Outlook, so fallback colors are required.
- HTML-based buttons are preferred over image-based buttons because they always show even when images are blocked and can be made fluid on mobile.
- Responsive controls let rows, boxes, and columns be hidden per device and let columns reorder into a single column on small screens.

## Key Quotes
> "The layout is the look and feel of the email (i.e. overall appearance), while the structure is the order in which the elements are arranged." - the article's core distinction.

> "HTML emails are 'only' the combination of rows and columns" - the simplified framing the article then complicates.

> "HTML buttons will always show up (even if images are blocked), and they can easily resize to the needed size on mobile screens too." - on preferring HTML buttons over image buttons.

> "You cannot start designing an email template without knowing: Goal of the email, Target audience, Email copy." - on content coming before layout.

## Connections
- [[Chamaileon]] - the email-builder product whose blog published the tutorial and whose editor implements the described elements.
- [[EmailLayoutAndStructure]] - the layout-versus-structure distinction and building-block inventory drawn from this source.
- [[EmailTableLayout]] - the table, row, column, and box model the article documents.
- [[EmailRenderingConstraints]] - the client limits on fonts, images, and backgrounds that constrain email design.
- [[HTMLEmailButton]] - the article's recommendation to use HTML buttons instead of image buttons.
- [[ResponsiveEmailDesign]] - the mobile hiding, reordering, and fluid-element controls the article describes.
- [[Mailchimp]] - cited as an email editor with less control over rows and columns, and as a source of built-in multi-column elements.
- [[MobileEmailEngagement]] - the cross-device reading behavior that motivates responsive templates.
- [[EmailMarketingAtScale]] - the delivery context these templates are built to serve.

## Contradictions
- No direct contradiction with existing wiki pages. The source qualifies image-led or design-first workflows by insisting that content precedes layout and that a call to action should not depend on an image that may be blocked.
- The tutorial is first-party marketing content for [[Chamaileon]], so its claims about builder capabilities and its comparison with [[Mailchimp]] are source-scoped rather than independent product reviews.
- The remote lead image (a chamaileon.io hero illustration) returned HTTP 403 and could not be inspected; the "test yourself" layout illustrations are referenced in the prose but are not embedded in the extracted Markdown, so they could not be used as visual evidence.

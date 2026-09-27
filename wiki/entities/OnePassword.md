---
title: "1Password"
type: entity
tags: [password-manager, security, macos, ios]
sources:
  - dave-teare-at-wwdc-how-one-month-for-1password-became-8-years-the-mac-observer
last_updated: 2026-09-27
knowledge_schema: synthesis-v1
---

## Overview
[[OnePassword]] is the flagship [[AgileBits]] password-management product whose origin and 2013 Mac-to-iOS evolution are described in the source.

## Current Profile
The product began as OS X Form, a one-month internal utility for saving repetitive web-test data; password storage was initially an adjacent form-field capability. External feedback turned it into a long-running product. On iOS, it moved from a bookmarklet through repeated native iterations to a complete 1Password 4 rewrite, adding desktop-free Dropbox and iCloud synchronization as support requests exposed users who did not own computers.

## Key Characteristics
- Originated in repetitive website-testing work rather than as a fully formed password-manager plan.
- Became a sustained commercial product after early users supplied enthusiastic direct feedback.
- Adapted to iOS incrementally before receiving a complete iOS 6-targeted rewrite.
- Supported desktop-free synchronization through Dropbox and iCloud in version 4.
- Reached less-technical and mobile-first customers beyond its original MacUpdate and VersionTracker audience.
- Used document-based iCloud synchronization rather than Core Data sync in the described version.

## Evidence
- Origin: [[dave-teare-at-wwdc-how-one-month-for-1password-became-8-years-the-mac-observer]] traces the product from saved form scenarios to password fields and the OS X Form name.
- Feedback-driven continuation: [[dave-teare-at-wwdc-how-one-month-for-1password-became-8-years-the-mac-observer]] says user responses led the team to keep extending a planned one-month project.
- Rewrite: [[dave-teare-at-wwdc-how-one-month-for-1password-became-8-years-the-mac-observer]] describes 1Password 4 for iOS as a complete rewrite targeting iOS 6.
- Desktop-free use: [[dave-teare-at-wwdc-how-one-month-for-1password-became-8-years-the-mac-observer]] connects support requests from iPod and iPad owners without desktops to standalone synchronization.
- Sync design: [[dave-teare-at-wwdc-how-one-month-for-1password-became-8-years-the-mac-observer]] records Shiner identifying document sync and Teare describing collaboration with Apple on the document format.

## Qualifications
This is a June 2013 product profile, not current documentation or a security review. The source provides no independent code, reliability, cryptographic, retention, or sales analysis, and it acknowledges continuing synchronization support complaints despite describing the experience as successful.

## What Changed
- Created a historical profile linking the product's form-filling origin, customer feedback, iOS rewrite, and desktop-free synchronization.

## Relationships
- [[AgileBits]] - developer and vendor in the source.
- [[DaveTeare]] - cofounder who recounts the product's origin and evolution.
- [[RoustemKarimov]] - cofounder associated with the product's origin.
- [[JeffShiner]] - interview participant who describes sync implementation and the Mac roadmap.
- [[CustomerLedProductDevelopment]] - early feedback and later support cases redirected investment and functionality.
- [[ProductUserSegmentation]] - mobile-first, desktop-free, technical, and less-technical users needed different paths.
- [[PrivacyPreservingProductMeasurement]] - company data-minimization choices limited insight into usage segments.

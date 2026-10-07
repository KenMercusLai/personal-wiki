---
title: "干饭手册"
type: entity
tags: [product, ios, cooking, personal-software, image-catalog]
sources:
  - 95-zhi-zuo-wo-de-di-yi-kuan-ios-app-gan-fan-shou-ce
last_updated: 2026-10-07
knowledge_schema: synthesis-v1
---

## Overview
[[GanFanShouCe|干饭手册]] is [[Fenx]]'s first released iOS app, built to record a household's cookable dishes and make deciding what to eat easier.

## Current Profile
The product evolved from dish photos and a Feishu-table MVP into an image-first personal catalog. Its basic experience supports adding, editing, searching, grouping, collapsing, counting, and sharing dishes. The shipped scope also includes AI ingredient recognition and image enhancement, eating history, image background removal, iCloud synchronization, CKShare-based sharing, widgets, subscriptions and one-time purchase, four-language localization, alternate icons, configurable launch art, and account settings. SwiftUI provides the interface, SwiftData and CloudKit support private data, and custom CloudKit zones support sharing. The source documents release after a long App Review but supplies no adoption, reliability, revenue, or retention results.

## Key Characteristics
- Records dishes a household knows how to cook through an image-first grid.
- Supports groups, search, bulk management, eating counts, and ingredient preferences.
- Uses local and AI-assisted image processing, including AVIF storage, enhancement, and background removal.
- Synchronizes through iCloud and shares selected content through CloudKit zones and Universal Links.
- Extends beyond its core catalog with widgets, payments, localization, alternate icons, launch templates, and playful visual details.
- Embodies both the value and lifecycle cost of broad solo-product scope.

## Evidence
- User need and MVP: [[95-zhi-zuo-wo-de-di-yi-kuan-ios-app-gan-fan-shou-ce]] links the app to forgotten household dishes, inefficient random choice, photo albums, and a Feishu-table prototype.
- Core catalog: [[95-zhi-zuo-wo-de-di-yi-kuan-ios-app-gan-fan-shou-ce]] shows image upload, title and duplicate-name prompts, descriptions, grouping, search, collapse, and bulk operations.
- Image and AI features: [[95-zhi-zuo-wo-de-di-yi-kuan-ios-app-gan-fan-shou-ce]] describes Core Image filters, AVIF encoding, VisionKit foreground masks, AI enhancement, ingredient recognition, and version selection.
- Synchronization and sharing: [[95-zhi-zuo-wo-de-di-yi-kuan-ios-app-gan-fan-shou-ce]] describes SwiftData private storage, CloudKit containers, CKShare zones, participant profiles, QR codes, and Universal Links.
- Commercial and ecosystem scope: [[95-zhi-zuo-wo-de-di-yi-kuan-ios-app-gan-fan-shou-ce]] covers StoreKit products, widgets, localization, sign-in, alternate icons, launch imagery, privacy and AI disclosures, and App Store review.

## Qualifications
All claims come from the creator's retrospective. The source does not report active users, retention, crashes, synchronization success rates, old-device benchmarks, subscription conversion, revenue, support load, accessibility testing, privacy review, or independent product evaluation. Several described issues may have changed after release, and the article itself says at least one onboarding photo permission was probably unnecessary.

## What Changed
- Created the product profile from its first-version design, engineering, and release retrospective.

## Relationships
- [[Fenx]] - creator, designer, and developer of the app.
- [[IOS]] - native platform and design environment on which the app runs.
- [[AppStore]] - distribution and review channel for the release.
- [[MobileAppLifecycleEngineering]] - the app exposes coupled data, cloud, image, entitlement, and release constraints.
- [[InspirationDrivenProductDesign]] - visual exploration produced many of the app's distinctive surfaces and details.
- [[PersonalSoftware]] - the product began as a tool for one household's specific memory and decision need.
- [[FeatureCreep]] - its expanded scope created acknowledged performance and execution costs.

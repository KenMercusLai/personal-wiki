---
title: "IntelliJ IDEA"
type: entity
tags: [developer-tools, ide]
sources:
  - a-seamless-way-to-keep-track-of-technical-debt-in-your-source-code-philippe-bourgaus-blog
last_updated: 2026-09-13
knowledge_schema: synthesis-v1
---

## Overview
[[IntelliJIDEA]] is an IDE cited in the Bourgau source as a built-in TODO discovery surface whose commit checks may need adjustment for lasting technical-debt markers.

## Current Profile
The source uses IntelliJ IDEA to show both sides of generic TODO tooling. Its TODO tab can make TODO comments visible during daily development, but its commit-window "Check TODO" option can warn on every commit when the team intentionally keeps some TODOs as long-lived debt markers.

## Key Characteristics
- IDE with built-in TODO comment visibility.
- Commit workflow can warn about TODO comments before changes are committed.
- Configuration can be adjusted when TODOs are used for durable debt tracking rather than short-lived reminders.

## Evidence
- TODO visibility: [[a-seamless-way-to-keep-track-of-technical-debt-in-your-source-code-philippe-bourgaus-blog]] names IntelliJ among tools that support TODO comments out of the box.
- Commit-warning behavior: [[a-seamless-way-to-keep-track-of-technical-debt-in-your-source-code-philippe-bourgaus-blog]] warns that IDEs may assume TODOs should be fixed before commit.
- Configuration example: [[a-seamless-way-to-keep-track-of-technical-debt-in-your-source-code-philippe-bourgaus-blog]] shows IntelliJ's commit window with a "Check TODO" checkbox and recommends unchecking it to avoid repeated warnings.

## Qualifications
The source uses IntelliJ IDEA as a workflow example rather than a full evaluation of the IDE, and its UI details may have changed since the article.

## What Changed
- Created the entity for IntelliJ IDEA as an IDE example in TODO-based technical-debt tracking.

## Relationships
- [[TodoComments]] - comments IntelliJ can display and check before commit.
- [[TechnicalDebtTracking]] - workflow IntelliJ can support when configured appropriately.
- [[PhilippeBourgau]] - author who cites IntelliJ as an example.

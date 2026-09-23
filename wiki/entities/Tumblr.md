---
title: "Tumblr"
type: entity
tags: [company, social-media, software-engineering]
sources:
  - cyle-how-i-review-code
last_updated: 2026-09-23
knowledge_schema: synthesis-v1
---

## Overview
[[Tumblr]] is the company and engineering environment in which [[Cyle]] developed the code-review practices described in the source.

## Current Profile
The 2018 essay presents Tumblr as operating old, shared codebases with hundreds of contributors across backend, mobile, infrastructure, database, and other projects. Changes moved through pull requests on an internal [[GitHub]] instance, required peer approval before merging and production deployment, and were commonly routed to reviewers by automated round-robin assignment.

## Key Characteristics
- Maintained large, long-lived codebases shared by hundreds of engineers.
- Used many languages across backend, mobile, infrastructure, database, and supporting projects.
- Required pull requests and peer approval before merging changes to the main production branch.
- Automated coding-standard checks so reviewers could concentrate on context and maintainability.
- Used round-robin reviewer assignment and email notifications to support prompt review follow-up.

## Evidence
- Engineering scale: [[cyle-how-i-review-code]] describes hundreds of engineers contributing to shared repositories.
- Technical breadth: [[cyle-how-i-review-code]] lists PHP, Swift, Objective-C, Java, Kotlin, Go, C, C++, Lua, Ruby, Perl, Scala, Node.js, and Python across project types.
- Change control: [[cyle-how-i-review-code]] says changes used pull requests, peer approval, merge to the main branch, and production deployment.
- Review workflow: [[cyle-how-i-review-code]] describes automated style checks, round-robin assignment, email subscription, and reviewer follow-up after author revisions.

## Qualifications
This profile reflects one engineer's description of Tumblr in 2018, not a current audit of the company's repositories, staffing, languages, branch naming, review policy, or deployment process. It documents the source's engineering context rather than Tumblr's broader product or corporate history.

## What Changed
- Established Tumblr as the organizational setting for Cyle's code-review practice.
- Added the source's historical repository, approval, automation, and reviewer-assignment workflow.

## Relationships
- [[Cyle]] - engineer whose first-person account supplies the profile.
- [[GitHub]] - platform Tumblr used through an internal instance for pull-request review.
- [[CodeReviewPractice]] - shared engineering practice emphasized in the source.
- [[PRReviewHygiene]] - small changes and responsive review supported Tumblr's delivery flow.

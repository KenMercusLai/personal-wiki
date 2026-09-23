---
title: "Cyle"
type: entity
tags: [person, software-engineering, code-review]
sources:
  - cyle-how-i-review-code
last_updated: 2026-09-23
knowledge_schema: synthesis-v1
---

## Overview
[[Cyle]] is a Tumblr engineer and the author of a practitioner essay on reviewing code in a large shared codebase.

## Current Profile
The source presents Cyle as an engineer whose review practice changed after moving from mostly solo development to [[Tumblr]]'s hundreds-of-contributors environment. Cyle reports reviewing about 25 pull requests per week and emphasizes understandable code, durable decision context, small changes, timely follow-up, and humane feedback.

## Key Characteristics
- Learned large-scale review practice after earlier experience with mostly solo or small-group coding.
- Adapts review guidance to an author's seniority and familiarity with the codebase.
- Treats review history as documentation for engineers who encounter a change later.
- Prefers clear, documented code over terse or clever implementation.
- Treats prompt follow-up and respectful communication as part of technical review quality.

## Evidence
- Experience shift: [[cyle-how-i-review-code]] contrasts earlier occasional reviews with a reported average of 25 pull requests per week at Tumblr.
- Context-aware coaching: [[cyle-how-i-review-code]] describes giving junior engineers examples and references while asking experienced engineers to explain abstraction and performance-oriented complexity.
- Durable explanation: [[cyle-how-i-review-code]] argues that future engineers should be able to recover a change's motivation and reasoning from its pull request.
- Review values: [[cyle-how-i-review-code]] favors clear, documented code, prompt review cycles, and language that treats the author as a fallible person.

## Qualifications
This profile is based on one first-person essay published in 2018. The reported review volume, role, organizational setting, and practices are historical and self-described rather than independently measured or current.

## What Changed
- Established Cyle as a practitioner source on large-codebase review.
- Captured his author-aware, future-reader-aware, and human-centered review principles.

## Relationships
- [[Tumblr]] - employer and engineering environment described in the source.
- [[CodeReviewPractice]] - primary practice Cyle explains.
- [[PRReviewHygiene]] - operational discipline reflected in his small-PR and timely-follow-up advice.
- [[WorkplaceLearning]] - review history is treated as a learning resource for other engineers.

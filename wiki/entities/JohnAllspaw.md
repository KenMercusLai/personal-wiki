---
title: "John Allspaw"
type: entity
tags: [software-engineering, devops, reliability, leadership]
sources:
  - etsy-cto-q-a-we-need-software-engineers-not-developers-the-new-stack
last_updated: 2026-09-27
knowledge_schema: synthesis-v1
---

## Overview
[[JohnAllspaw]] is represented here as [[Etsy]]'s CTO in a 2016 interview about technology choice, deployment, production responsibility, multidisciplinary engineering, and human judgment in machine learning.

## Current Profile
Allspaw's engineering philosophy joins restraint with broad responsibility. Teams should prefer a small number of well-understood tools, make the long-term operating cost of novelty explicit, and keep deployment simple enough that a new hire can use it early. That simplicity is not permission to ignore infrastructure: the person deploying code should also care how it fails, how failure becomes visible, and which application, database, network, or platform expert can deepen the team's shared understanding.

His machine-learning comments apply the same human-centered boundary. Etsy used inference and heuristics to improve discovery across unique long-tail inventory, but Allspaw rejects the idea that automated decisions escape judgment or that failures alone reveal how a system works. The profile therefore reflects an articulated 2016 leadership stance, not a complete biography or independently evaluated operating record.

## Key Characteristics
- Advocates a small set of familiar tools so engineering attention remains on the product.
- Treats new technology as a continuing organizational ownership cost rather than a free local choice.
- Connects simple deployment with responsibility for observing and operating production code.
- Defines engineering as multidisciplinary learning and shared understanding across specialist boundaries.
- Takes a human-centered view of automation and machine learning as software that still encodes judgment.

## Evidence
- Technology restraint: [[etsy-cto-q-a-we-need-software-engineers-not-developers-the-new-stack]] records Allspaw favoring a straightforward core stack and explicit architecture review of novel-tool costs.
- Deployment and operation: [[etsy-cto-q-a-we-need-software-engineers-not-developers-the-new-stack]] says difficult first-week deployment indicates a deployment or onboarding problem and links deploy authority to monitoring, alerting, and metrics.
- Learning across boundaries: [[etsy-cto-q-a-we-need-software-engineers-not-developers-the-new-stack]] says engineers should seek domain experts and continually explore the edge of their knowledge.
- Human judgment: [[etsy-cto-q-a-we-need-software-engineers-not-developers-the-new-stack]] argues that software decisions contain opinions and that engineering should study why systems succeed as well as why they fail.

## Qualifications
The evidence is one edited interview tied to Allspaw's Etsy role in 2016. It does not document his broader career, later work, incident record, organizational outcomes, or the views of other Etsy engineers. The contrast between “engineer” and “developer” is best read as a claim about responsibility and curiosity, not as an objective title hierarchy.

## What Changed
- Created a source-scoped profile of Allspaw's Etsy engineering philosophy.

## Relationships
- [[Etsy]] - company whose 2016 engineering practices he describes as CTO.
- [[ProductionOwnership]] - his deploy-and-operate argument is a direct instance of this responsibility model.
- [[DevOpsCulture]] - his account joins development, deployment, observability, and operational learning.
- [[BoringTechnology]] - his tool-restraint argument protects product attention from novelty costs.
- [[SoftwareEngineering]] - he defines the field through multidisciplinary understanding beyond coding alone.
- [[MachineLearning]] - he discusses long-tail recommendations while preserving human judgment and accountability.

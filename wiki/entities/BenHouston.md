---
title: "Ben Houston"
type: entity
tags: [software-engineering, infrastructure, author]
sources:
  - ben-houston-i-didnt-need-kubernetes
last_updated: 2026-09-14
knowledge_schema: synthesis-v1
---

## Overview
[[BenHouston]] is a software practitioner and author represented here by an infrastructure essay about leaving [[Kubernetes]] for [[GoogleCloudRun]].

## Current Profile
The source presents Houston as someone who has operated 3D web platforms across bare metal, Kubernetes, and managed serverless container infrastructure. His argument is pragmatic rather than anti-container: he keeps [[Docker]] containers but prefers a narrower managed platform when Kubernetes' cost, staffing, scaling, and abstraction burden exceed the benefits.

## Key Characteristics
- Has experience operating infrastructure for online 3D platforms.
- Treats platform choice as an operations and cost tradeoff, not only a technical preference.
- Values simple managed abstractions when they fit the workload.
- Distinguishes container portability from Kubernetes-specific operating models.

## Evidence
- Platform history: [[ben-houston-i-didnt-need-kubernetes]] says Houston moved from bare-metal OVH infrastructure for [[ClaraIO]] toward managed compute for [[Threekit]].
- Kubernetes critique: [[ben-houston-i-didnt-need-kubernetes]] says Kubernetes became expensive, slow to autoscale, and complex enough to require dedicated operations expertise.
- Cloud Run preference: [[ben-houston-i-didnt-need-kubernetes]] says Cloud Run simplified container deployment, scaling, downtime management, and task execution.
- Container portability: [[ben-houston-i-didnt-need-kubernetes]] says the stack remains Docker-based and could be moved to another major cloud with limited migration work.

## Qualifications
The page reflects Houston only through this one infrastructure essay. It does not independently verify the cost numbers, the staffing claim, or his broader professional history.

## What Changed
- Created the entity from the Cloud Run migration source.

## Relationships
- [[Kubernetes]] - platform Houston argues he no longer needed for his workload.
- [[GoogleCloudRun]] - managed service Houston favors for container deployment and tasks.
- [[ClaraIO]] - earlier platform context in Houston's infrastructure story.
- [[Threekit]] - enterprise 3D platform context for the original Kubernetes move.
- [[CloudCostOptimization]] - Houston's platform choice is partly driven by cost and utilization.

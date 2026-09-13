---
title: "Threekit"
type: entity
tags: [3d, enterprise-software, infrastructure]
sources:
  - ben-houston-i-didnt-need-kubernetes
last_updated: 2026-09-14
knowledge_schema: synthesis-v1
---

## Overview
[[Threekit]] is the enterprise-focused 3D platform context in [[BenHouston]]'s essay, used to explain why his team moved from bare metal toward [[Kubernetes]] around 2018.

## Current Profile
The source presents Threekit as a remake or successor direction after [[ClaraIO]], with infrastructure requirements that pushed the team toward managed compute. Kubernetes appeared attractive at that point because major providers and Docker were converging around it, but the later experience led Houston to prefer [[GoogleCloudRun]] for his current workloads.

## Key Characteristics
- Enterprise-focused re-imagining of the earlier Clara.io platform.
- Motivated a move away from bare-metal operations toward managed compute.
- Adopted Kubernetes during the 2018 period when it was becoming the industry default.
- Serves as the historical case before the author's later Cloud Run preference.

## Evidence
- Platform role: [[ben-houston-i-didnt-need-kubernetes]] calls Threekit an enterprise-focused re-imagining of Clara.io.
- Managed-compute shift: [[ben-houston-i-didnt-need-kubernetes]] says the team looked for managed compute while remaking the platform.
- Kubernetes timing: [[ben-houston-i-didnt-need-kubernetes]] says Kubernetes was emerging as the industry solution around 2018 as Azure, AWS, and Docker converged on it.
- Later reassessment: [[ben-houston-i-didnt-need-kubernetes]] says years of Kubernetes operation revealed cost and complexity problems.

## Qualifications
The page reflects only the infrastructure context supplied by the essay, not Threekit's full product or company history.

## What Changed
- Created the entity as context for the Kubernetes adoption and Cloud Run reassessment source.

## Relationships
- [[ClaraIO]] - earlier platform that Threekit re-imagined for enterprise use.
- [[BenHouston]] - author describing the Threekit infrastructure transition.
- [[Kubernetes]] - managed compute platform adopted in the Threekit context.
- [[GoogleCloudRun]] - later platform Houston prefers for simpler workloads.

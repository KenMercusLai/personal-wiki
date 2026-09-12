---
title: "Kelsey Hightower"
type: entity
tags: [software-engineering, infrastructure, containers]
sources:
  - 12-fractured-apps-kelsey-hightower-medium
last_updated: 2026-09-12
knowledge_schema: synthesis-v1
---

## Overview
[[KelseyHightower]] is the software infrastructure author of "12 Fractured Apps," where he argues that containerized applications should own their startup and configuration behavior instead of pushing those responsibilities onto deployment scripts.

## Current Profile
In this source, Hightower writes as a pragmatic deployment engineer connecting [[TwelveFactorApp]] ideas to [[Docker]] practice. His argument is less that Docker solves application design and more that containers expose application assumptions: if software cannot start cleanly without exact file, directory, service-order, and database availability conditions, it remains operationally fragile even inside a container.

## Key Characteristics
- Presents Docker and twelve-factor practices as mutually reinforcing when the application participates in the model.
- Critiques legacy lift-and-shift containerization that treats containers like virtual machines.
- Treats startup behavior as application design, not merely deployment automation.
- Prefers simple application code for defaults, env overrides, directory creation, retry, and logging over custom wrapper scripts for owned code.

## Evidence
- Docker and twelve-factor fit: [[12-fractured-apps-kelsey-hightower-medium]] uses stdout logging and environment variables as examples where Docker naturally supports twelve-factor behavior.
- Lift-and-shift critique: [[12-fractured-apps-kelsey-hightower-medium]] warns that many Dockerized applications are subtly broken because they preserve VM-era assumptions.
- Startup design: [[12-fractured-apps-kelsey-hightower-medium]] walks through missing config, missing data directories, and unreachable databases as application-level startup problems.
- Wrapper-script qualification: [[12-fractured-apps-kelsey-hightower-medium]] allows entrypoint scripts for applications developers do not control, but rejects them as the main solution for applications they write.

## Qualifications
This page reflects Hightower only through the 2015 "12 Fractured Apps" essay. It does not summarize his broader work in cloud infrastructure, Kubernetes, public speaking, or engineering education.

## What Changed
- Created the entity page for Hightower as the author of the container-startup design source.

## Relationships
- [[Docker]] - Hightower uses Docker to demonstrate deployment-friendly and fractured application behavior.
- [[TwelveFactorApp]] - Hightower adapts twelve-factor principles to container startup and runtime configuration.
- [[ContainerApplicationStartup]] - Hightower's central design concern in the source.
- [[RuntimeConfiguration]] - Hightower argues that runtime configuration belongs near application code and runtime inputs.

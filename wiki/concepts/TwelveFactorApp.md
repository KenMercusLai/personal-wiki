---
title: "Twelve-Factor App"
type: concept
tags: [software-engineering, deployment, operations]
sources:
  - 12-fractured-apps-kelsey-hightower-medium
last_updated: 2026-09-12
knowledge_schema: synthesis-v1
---

## Definition
[[TwelveFactorApp]] is an application-design methodology for building deployable, manageable services; in this wiki source, it is used mainly for its stdout logging and environment-variable configuration principles.

## Current Synthesis
The source treats twelve-factor design as especially compatible with container deployment. Logging to stdout makes application logs available through Docker's logging surface, and configuration through environment variables lets runtime systems supply environment-specific settings without rebuilding images.

The article's important qualification is that using Docker does not automatically make an application twelve-factor. Applications can still be "fractured" when they require local config files, assume directories already exist, exit immediately when a dependency is temporarily unavailable, or outsource their own startup responsibilities to shell wrappers.

## Key Claims
- Twelve-factor logging maps naturally to container stdout event streams.
- Environment-variable configuration fits container runtime configuration better than image-bundled config files.
- Docker can reveal twelve-factor benefits but cannot retrofit them into application code by itself.
- Applications remain operationally brittle when startup depends on exact external preconditions.
- Twelve-factor-style deployment requires application participation, not only container packaging.

## Evidence
- Logging fit: [[12-fractured-apps-kelsey-hightower-medium]] points to `docker logs` as an example of stdout logging as an event stream.
- Configuration fit: [[12-fractured-apps-kelsey-hightower-medium]] notes that Docker makes environment variables easy to set when containers are created.
- Image-sprawl warning: [[12-fractured-apps-kelsey-hightower-medium]] warns against baking deployment-specific configuration files into many container image variants.
- Fragile startup: [[12-fractured-apps-kelsey-hightower-medium]] shows that missing config, missing data directories, and unreachable databases still break a containerized app.
- Application responsibility: [[12-fractured-apps-kelsey-hightower-medium]] concludes that bootstrapping tasks should be handled close to the application.

## Counterevidence & Qualifications
The source discusses only a subset of the twelve-factor manifesto and uses Docker-era examples from 2015. It does not provide a complete evaluation of all twelve factors or of later orchestration patterns.

## What Changed
- Created the twelve-factor application concept as the methodological frame for Docker-friendly startup and configuration.

## Related Concepts
- [[ContainerApplicationStartup]] - startup resilience is the source's concrete extension of twelve-factor thinking.
- [[RuntimeConfiguration]] - env vars and optional config files are the main configuration mechanism discussed.
- [[SystemReliability]] - twelve-factor-style behavior supports reliability but does not cover every reliability layer.
- [[CLIApplicationDesign]] - the wiki also contains a later "12 Factor CLI Apps" analogy for developer-tool UX.

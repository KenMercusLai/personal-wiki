---
title: "12 Fractured Apps"
type: source
tags: [docker, twelve-factor-app, deployment, reliability]
date: 2015-12-14
source_file: /mnt/ken_personal_wiki/Articles/12 Fractured Apps - Kelsey Hightower - Medium.md
---

## Summary
[[KelseyHightower]] argues that many applications moved into [[Docker]] containers without becoming truly deployment-friendly. The essay uses a small Go application to show how mandatory config files, missing working directories, and one-shot database connections create fragile startup behavior, then argues that developers should handle defaults, environment overrides, directory creation, and dependency retry logic inside the application rather than in Docker entrypoint wrapper scripts.

## Key Claims
- [[TwelveFactorApp]] practices become especially visible in Docker because stdout logging and environment-variable configuration map cleanly to container operation.
- "Lift and shift" containerization can preserve legacy assumptions, producing large images and brittle startup behavior even when deployment looks modern.
- [[ContainerApplicationStartup]] should tolerate missing optional config files, create required local directories, and retry temporarily unavailable dependencies with backoff.
- [[RuntimeConfiguration]] should be managed at runtime through environment variables and optional config files, not by baking deployment-specific config into a growing set of images.
- Custom Docker entrypoint scripts can be useful for third-party applications, but relying on them for owned applications moves bootstrapping logic away from the code that best understands it.

## Key Quotes
> "Deal with application bootstrapping tasks as close to the application as possible" - summary principle for keeping deployment concerns near application code.

## Connections
- [[KelseyHightower]] - author of the essay.
- [[Docker]] - deployment environment used to demonstrate both better twelve-factor fit and fragile lift-and-shift behavior.
- [[TwelveFactorApp]] - methodology whose configuration and logging guidance frames the article.
- [[ContainerApplicationStartup]] - core design pattern advocated by the source.
- [[RuntimeConfiguration]] - configuration layer the article wants handled without image sprawl.
- [[DependencyDegradation]] - related reliability concern around dependency failure, retry behavior, and startup order.

## Contradictions
- None identified.

---
title: "Runtime Configuration"
type: concept
tags: [software-engineering, deployment, configuration]
sources:
  - 12-fractured-apps-kelsey-hightower-medium
last_updated: 2026-09-12
knowledge_schema: synthesis-v1
---

## Definition
[[RuntimeConfiguration]] is the practice of supplying environment-specific settings when an application runs, rather than baking those settings permanently into the application artifact or container image.

## Current Synthesis
The source frames runtime configuration as a central reason Docker and twelve-factor practices work well together. Environment variables can inject deployment-specific hostnames, ports, credentials, databases, and directory paths while the same image moves across environments.

The anti-pattern is image sprawl: building separate container images for every environment or date-stamped deployment because config files are bundled into the image. Hightower's preferred pattern is layered and application-owned: optional config files may exist, defaults should be sane, and environment variables should override settings at startup.

## Key Claims
- Runtime settings should be separable from the container image artifact.
- Environment variables are a practical runtime configuration channel for containerized applications.
- Optional config files and sane defaults reduce hard startup coupling to local files.
- Baking environment-specific config into images creates unnecessary image variants and management overhead.
- Applications should understand and apply their own configuration inputs instead of delegating all translation to shell wrappers.

## Evidence
- Env var channel: [[12-fractured-apps-kelsey-hightower-medium]] shows Docker passing app settings through `APP_*` environment variables at `docker run` time.
- Optional files: [[12-fractured-apps-kelsey-hightower-medium]] changes the app to use default config when `/etc/config.json` is absent.
- Image-sprawl warning: [[12-fractured-apps-kelsey-hightower-medium]] warns that bundling deployment config leads to many images such as production and development variants.
- Application-owned config: [[12-fractured-apps-kelsey-hightower-medium]] moves env-var override logic from `docker-entrypoint.sh` into Go code.
- Artifact clarity: [[12-fractured-apps-kelsey-hightower-medium]] argues for shipping artifacts rather than build environments.

## Counterevidence & Qualifications
The source's examples are deliberately simple and do not cover secret management, dynamic configuration systems, config schema validation, rotation, or policy controls. It also does not claim that config files are always bad; it argues that they should not be mandatory or baked into environment-specific images.

## What Changed
- Created the concept page for runtime configuration as a container deployment design pattern.

## Related Concepts
- [[TwelveFactorApp]] - runtime configuration is one of the article's twelve-factor anchors.
- [[ContainerApplicationStartup]] - startup code loads, defaults, and overrides runtime settings.
- [[NextJSDeployment]] - deployment model choices also shape how configuration reaches running applications.
- [[LowOpsGameServer]] - both treat configuration design as part of operational cost.

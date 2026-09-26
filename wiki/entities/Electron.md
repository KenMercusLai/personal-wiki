---
title: "Electron"
type: entity
tags: [desktop, javascript, packaging, runtime]
sources:
  - blog-innei-lobehub-performance-and-dx-optimization
  - building-hybrid-applications-with-electron-several-people-are-coding
last_updated: 2026-09-25
knowledge_schema: synthesis-v1
---

## Overview
[[Electron]] is a Chromium-and-Node.js desktop runtime represented by [[Slack]]'s shared cross-platform client architecture and [[LobeHub]]'s later packaging and typed-IPC work.

## Current Profile
The Slack account supplies Electron's runtime architecture: a main application and renderer processes, a separate GPU process, WebView-hosted remote content, preload scripts, and IPC. Slack used those surfaces to unify its macOS, Windows, and Linux clients while keeping remote code away from ambient Node.js access. The later LobeHub article supplies the distribution side: localization resources can be pruned if a supported locale remains, bundled JavaScript can avoid shipping the full `node_modules` tree, native bindings need explicit treatment, and typed decorators can improve IPC authoring.

## Key Characteristics
- Combines Chromium rendering with the Node.js runtime and module system.
- Uses multiple processes for the main application, renderers, GPU work, and supporting services.
- Supports preload scripts and IPC for controlled communication between privileged local code and renderer content.
- Bundles framework localization directories that can materially affect application size.
- Uses ASAR packaging while native modules may require explicit unpacking.
- Can support a shared desktop codebase across macOS, Windows, and Linux.

## Evidence
- Localization pruning: [[blog-innei-lobehub-performance-and-dx-optimization]] says Electron Framework language bundles occupied about 34 MB and warns that deleting all of them causes startup failure.
- Dependency packaging: [[blog-innei-lobehub-performance-and-dx-optimization]] excludes `node_modules` after bundling non-native dependencies and adds explicit patterns for native bindings.
- Size result: [[blog-innei-lobehub-performance-and-dx-optimization]] reports about 100 MB removed and a resulting application size near 260 MB.
- IPC surface: [[blog-innei-lobehub-performance-and-dx-optimization]] replaces stringly typed dispatch-and-subscribe code with `electron-ipc-decorator`.
- Runtime model: [[building-hybrid-applications-with-electron-several-people-are-coding]] describes Chromium renderer separation, a main application process, a GPU process, WebView-hosted content, preload scripts, and IPC.
- Cross-platform use: [[building-hybrid-applications-with-electron-several-people-are-coding]] says Slack consolidated its macOS, Windows, and Linux desktop clients on one Electron codebase.
- Security boundary: [[building-hybrid-applications-with-electron-several-people-are-coding]] keeps remote content away from direct Node.js access and exposes selected methods through a preload bridge.

## Qualifications
The sources document two application-specific cases rather than universal Electron requirements. Slack's account dates to 2016 and predates later Electron APIs and security guidance; it offers no comparative performance, memory, exploit-resistance, or incident evidence. Exact process behavior, bridge hardening, bundle layout, required locales, native-module behavior, signing, and size savings depend on Electron version, builder, operating system, architecture, dependencies, and release policy.

## What Changed
- Expanded Electron from packaging and typed IPC into its multi-process runtime, hybrid delivery, preload boundary, and shared cross-platform role.

## Relationships
- [[LobeHub]] - desktop application using Electron in the source.
- [[DesktopApplicationPackaging]] - practice applied to Electron resources and dependencies.
- [[DeveloperExperience]] - typed IPC improves the process-integration authoring experience.
- [[Innei]] - engineer who reports the packaging and IPC changes.
- [[Slack]] - production application using Electron for a shared hybrid desktop client.
- [[HybridDesktopApplicationArchitecture]] - local-shell and remote-code pattern implemented with Electron.
- [[PreloadBridgeSecurity]] - security discipline for Electron's renderer-to-host capability surface.

---
title: "Hybrid Desktop Application Architecture"
type: concept
tags: [desktop, electron, web, architecture]
sources:
  - building-hybrid-applications-with-electron-several-people-are-coding
last_updated: 2026-09-25
knowledge_schema: synthesis-v1
---

## Definition
[[HybridDesktopApplicationArchitecture]] combines a locally installed desktop shell and privileged integration layer with application assets or code delivered from a remote web service.

## Current Synthesis
Slack's 2016 Electron client used the installed application as a trusted host while loading most product code remotely. The pattern joins rapid web deployment and a shared cross-platform codebase with access to operating-system features, but creates a sharp trust boundary: remote content must run without ambient Node.js authority and request desktop actions through a narrow bridge. Chromium renderer separation further limits crash propagation by placing each signed-in team in its own process, while asynchronous IPC connects those processes to application state and native integration.

## Key Claims
- Local and remote delivery can be divided by trust and update cadence rather than forcing an application to be entirely bundled or entirely browser-hosted.
- A shared Electron codebase can replace separate platform clients while still reaching native desktop capabilities.
- Renderer-process separation can contain an individual remote view's crashes and memory space, although it does not by itself validate requested actions.
- A hybrid architecture is only as safe as the API and IPC capabilities exposed across the local-remote boundary.
- Asynchronous message passing and proxy abstractions can simplify cross-process integration without making remote authority harmless.

## Evidence
- Delivery split: [[building-hybrid-applications-with-electron-several-people-are-coding]] says Slack shipped some assets locally while loading most assets and code remotely.
- Cross-platform consolidation: [[building-hybrid-applications-with-electron-several-people-are-coding]] describes replacing the aging MacGap client with one Electron codebase across macOS, Windows, and Linux.
- Fault containment: [[building-hybrid-applications-with-electron-several-people-are-coding]] says every signed-in Slack team occupied a separate renderer process that could be restarted independently.
- Capability bridge: [[building-hybrid-applications-with-electron-several-people-are-coding]] exposes selected native actions through a preload API and proxy-based asynchronous IPC.

## Counterevidence & Qualifications
The evidence is a first-party 2016 account and provides no controlled comparison of performance, reliability, development speed, memory cost, or security outcomes against fully bundled Electron, browser, or native clients. Process separation contains some failures but does not enforce semantic least privilege. Remote delivery adds availability, version-skew, supply-chain, origin-authentication, and compromise risks, while a unified codebase does not guarantee identical platform behavior.

## What Changed
- Created the concept from Slack's local-shell and remote-code Electron architecture.

## Related Concepts
- [[PreloadBridgeSecurity]] - controls authority crossing from remote content into the privileged local shell.
- [[Electron]] - runtime implementing the source's multi-process hybrid client.
- [[DesktopApplicationPackaging]] - determines which runtime resources and dependencies remain locally shipped.
- [[DeveloperExperience]] - shared application code and IPC abstractions can reduce platform-specific development work.
- [[Slack]] - production case used to describe the architecture.

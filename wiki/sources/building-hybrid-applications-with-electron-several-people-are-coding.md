---
title: "Building Hybrid Applications with Electron"
type: source
tags: [electron, desktop-apps, security, ipc, slack]
date: 2016-10-26
source_file: "/mnt/ken_personal_wiki/Articles/Building Hybrid Applications with Electron - Several People Are Coding.md"
---

## Summary
[[Slack]] describes replacing its aging MacGap-based macOS client with a shared [[Electron]] codebase for macOS, Windows, and Linux. Its [[HybridDesktopApplicationArchitecture]] bundles a trusted local shell while loading most application code remotely, isolates each signed-in team in a separate renderer process, and exposes selected desktop capabilities through a constrained preload API. The account presents [[PreloadBridgeSecurity]] and asynchronous IPC as the critical controls, but it is a 2016 first-party architecture description rather than a current security audit or comparative performance study.

## Key Claims
- A hybrid desktop application can combine a locally shipped privileged shell with remotely loaded product code, preserving web-deployment speed while retaining operating-system integration.
- Electron enabled Slack to replace separate Mac and Windows histories with one macOS, Windows, and Linux codebase built on Chromium and Node.js.
- Chromium process isolation places the main application and each signed-in Slack team in separate memory spaces, allowing an individual team renderer to restart without taking down the entire application.
- Remote web content should not receive direct Node.js or desktop access; Slack places it in Electron's WebView and uses a preload script to expose only a deliberately designed API.
- Preload APIs must avoid leaking Node.js objects, validate file-path operations, and treat remote-object capabilities as security-sensitive authority.
- Slack's `electron-remote` library used ES6 proxies and asynchronous message passing to avoid synchronous IPC and remote-event-handler problems while making cross-process objects easier to use.
- Proxy convenience does not remove the trust boundary: remote objects require the same audit discipline as objects exposed directly by a preload script.

## Key Quotes
> "most of the assets and code are loaded remotely" - the defining distribution choice in Slack's hybrid architecture.

> "being able to ask another process to do something malicious is just as bad as doing it in-process" - warning that IPC capability is part of the security boundary.

## Connections
- [[Slack]] - production desktop application and first-party architecture case.
- [[Electron]] - Chromium-and-Node.js runtime used for the shared desktop codebase.
- [[HybridDesktopApplicationArchitecture]] - pattern combining a local privileged shell with remotely delivered application code.
- [[PreloadBridgeSecurity]] - least-authority API boundary between remote content and desktop capabilities.
- [[DesktopApplicationPackaging]] - complementary concern for assets and dependencies shipped inside an Electron release.
- [[DeveloperExperience]] - shared code, proxy-based async IPC, React, TypeScript migration, and open-source tooling reduce cross-platform implementation friction.

## Contradictions
- No direct contradiction found. The source complements the later [[Electron]] packaging case by describing runtime architecture rather than artifact size, while qualifying any broad claim that hybrid delivery is automatically safe: its security depends on narrow APIs, validation, isolation, and continued auditing.

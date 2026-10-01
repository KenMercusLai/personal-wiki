---
title: "Puppeteer"
type: entity
tags: [browser-automation, javascript, developer-tools]
sources:
  - mario-zechner-what-if-you-dont-need-mcp-at-all
last_updated: 2026-10-01
knowledge_schema: synthesis-v1
---

## Overview
[[Puppeteer]] is the browser automation library used beneath Mario Zechner's small command-line browser toolkit.

## Current Profile
The source uses `puppeteer-core` to connect to Chrome through the Chrome DevTools Protocol. Thin Node.js wrappers start a debug-enabled browser, navigate tabs, evaluate JavaScript in the active page, capture screenshots, inject an interactive element picker, and read cookies through browser-level APIs.

## Key Characteristics
- Connects to a running Chrome instance through a remote-debugging endpoint.
- Supports page navigation, DOM execution, screenshots, and browser-level cookie access.
- Can sit beneath narrow CLI commands so an agent need not manipulate its full API directly.

## Evidence
- Browser connection: [[mario-zechner-what-if-you-dont-need-mcp-at-all]] shows scripts connecting to Chrome on port 9222 with `puppeteer-core`.
- Bounded wrappers: [[mario-zechner-what-if-you-dont-need-mcp-at-all]] implements navigation, evaluation, screenshot, picker, and cookie commands as small Node.js programs.
- API boundary: [[mario-zechner-what-if-you-dont-need-mcp-at-all]] distinguishes page-context JavaScript from Puppeteer/CDP access to HTTP-only cookies.

## Qualifications
The source demonstrates Puppeteer through one Chrome-based scraping and frontend workflow. It does not evaluate cross-browser coverage, test-runner features, long-term API stability, anti-bot behavior, isolation, or authenticated-profile security.

## What Changed
- Created a source-bounded profile of Puppeteer's role as the browser layer behind a minimal agent CLI.

## Relationships
- [[MarioZechner]] - uses Puppeteer as the implementation substrate for his browser commands.
- [[Playwright]] - alternative browser automation project discussed through its MCP server.
- [[CodingAgentMinimalTooling]] - Puppeteer is hidden behind a small model-facing command surface.

---
title: "Who is listening on a given TCP port on Mac OS X?"
type: source
tags: [macos, networking, tcp, ports, diagnostics, lsof]
date: 2010-12-12
source_file: /mnt/ken_personal_wiki/Articles/Who is listening on a given TCP port on Mac OS X.md
---

## Summary
This Stack Overflow community answer set uses `lsof` to identify processes listening on TCP ports in macOS, either across all listeners or for a selected port and address family. Its durable contribution to [[DefensivePortTriage]] is local socket-to-process attribution with numeric, non-resolving output; its version claims, textual `grep` filters, privilege guidance, and immediate `kill -9` example need operational qualification.

## Key Claims
- `sudo lsof -iTCP -sTCP:LISTEN -n -P` lists TCP listeners while suppressing hostname and service-name resolution.
- `sudo lsof -nP -i4TCP:$PORT | grep LISTEN` narrows inspection to IPv4 TCP sockets associated with a selected port, while `-iTCP:$PORT` includes both supported address families.
- `-n` keeps addresses numeric and avoids potentially slow hostname lookups; `-P` keeps port numbers numeric instead of translating them to service names.
- A shell helper can expose either the full listener inventory or a case-insensitive textual search over that output.
- Listener discovery should precede process intervention; the source's `kill -9` example is a forceful termination mechanism, not a generally safe first response.

## Key Quotes
> "Every version of macOS supports this:"

> "The `-n` flag is for displaying IP addresses instead of host names."

> "The `-P` flag is for displaying raw port numbers instead of resolved names"

## Connections
- [[DefensivePortTriage]] - `lsof` adds macOS listener inventory and process attribution to the triage workflow.
- [[CommandLineUX]] - numeric output avoids slow or misleading name resolution during interactive diagnosis.
- [[AutomationFriendlyCLI]] - non-resolving, numeric output is more stable for scripts than translated host and service names.
- [[Apple]] - The commands and version claims are scoped to Apple's macOS desktop operating system.

## Contradictions
- The source recommends `grep :$PORT` in one command, but this is textual matching rather than an exact socket filter and can match other port numbers or unrelated fields; the `lsof -iTCP:$PORT` selector is the more precise part of the recipe.
- The `sudo` guidance is simplified: visibility depends on process ownership, permissions, and macOS behavior rather than only whether the numeric port is above 1023.
- `kill -9` bypasses normal graceful shutdown and cleanup; identifying a PID does not establish that force-killing it is safe or necessary.
- The Big Sur-versus-older-version distinction is asserted by a community-edited answer without versioned test evidence in the supplied document.

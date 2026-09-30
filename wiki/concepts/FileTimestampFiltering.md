---
title: "File Timestamp Filtering"
type: concept
tags: [linux, filesystems, command-line, automation]
sources:
  - linux-using-find-to-locate-files-older-than
last_updated: 2026-10-01
knowledge_schema: synthesis-v1
---

## Definition
[[FileTimestampFiltering]] is the selection of filesystem entries by comparing a chosen file timestamp with an absolute, relative, or reference-file cutoff.

## Current Synthesis
The source presents timestamp selection as predicate composition. A reference file supplies a portable-looking comparison target, while `-newermt` lets a supporting `find` implementation parse the cutoff directly. The positive predicate selects modification times strictly newer than the reference; negation selects its complement, and paired lower and upper predicates form a range.

The apparent simplicity hides boundary choices that matter in automation. “Older than” must be translated into an explicit comparison, negation includes equality, and a human-readable date depends on parser, timezone, locale, and date-only conventions. The source also conflates creation time with modification time in its workaround, so scripts must choose the intended timestamp field rather than inherit that wording.

## Key Claims
- A timestamped reference file lets `find -newer` compare candidate modification times without embedding a natural-language date parser in the query.
- `-newermt` expresses the reference directly as a parsed time string when the installed `find` supports that predicate.
- Negation turns a strict newer-than test into an at-or-before test, so boundary equality is part of the result.
- Combining a positive lower-bound predicate with a negated upper-bound predicate expresses a time window.
- Reliable automation requires explicit timestamp type, parser availability, timezone, locale, and interval-boundary decisions.

## Evidence
- Reference-file comparison: [[linux-using-find-to-locate-files-older-than]] uses `touch -t 201003160120 some_file` and then `find . -newer some_file`.
- Direct and relative cutoffs: [[linux-using-find-to-locate-files-older-than]] shows `-newermt` with a calendar date, `yesterday`, and a date plus clock time.
- Range composition: [[linux-using-find-to-locate-files-older-than]] combines `-newermt` for a lower boundary with `-not -newermt` for an upper boundary.
- Timestamp-type distinction: [[linux-using-find-to-locate-files-older-than]] reproduces the `-newerXY` selectors for access, birth, inode-change, modification, and directly interpreted time references.

## Counterevidence & Qualifications
The evidence is a brief community Q&A excerpt rather than a complete portability guide or tested runbook. It does not name the `find` implementation, demonstrate a standalone older-than invocation, define inclusive versus exclusive calendar-day intent, or test timezone, locale, daylight-saving, filename, permission, and traversal behavior. Its reference-file comment incorrectly calls the assigned timestamp a creation date even though the shown default comparison concerns modification time.

## What Changed
- Created the initial synthesis of reference-file and direct-date timestamp filtering.
- Made negation's equality boundary and the source's creation-time versus modification-time mismatch explicit.
- Added portability and date-parsing constraints absent from the captured examples.

## Related Concepts
- [[CLICommandGrammar]] - `find` represents selection as composable predicates, operators, and negation.
- [[AutomationFriendlyCLI]] - timestamp filters become scriptable only when parsing and boundary behavior are controlled.
- [[FilesystemUnmounting]] - both require precise reasoning about filesystem state, though one filters metadata and the other manages active mounts.

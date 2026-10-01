---
title: "Linux: Using find to Locate Files Older Than a Date"
type: source
tags: [linux, find, filesystems, command-line]
date: 2010-03-16
source_file: "/mnt/ken_personal_wiki/Articles/Linux using find to locate files older than.md"
---

## Summary
This short Server Fault capture explains two ways to filter files around an absolute timestamp with Unix `find`: compare file modification times with a timestamped reference file, or use GNU-style `-newermt` to parse a date string directly. Negating the newer-than predicate produces the older side of a cutoff, while combining a positive lower bound with a negated upper bound produces a date range.

## Key Claims
- `touch -t` can assign a chosen timestamp, including an optional century and seconds, to a reference file for use with `find -newer`.
- `find -newermt "mar 03, 2010"` compares candidate modification times with a directly parsed absolute time and avoids creating a reference file.
- Relative expressions such as `yesterday` can also serve as the time reference in implementations that support `-newermt`.
- A bounded interval can be formed by requiring files newer than the lower timestamp and not newer than the upper timestamp.
- Negating `-newer` or `-newermt` selects the complementary side of the cutoff, including exact equality with the reference instant.

## Key Quotes
> "No, you can use a date/time string." - introducing direct timestamp parsing rather than a synthetic reference file.

> "reference is interpreted directly as a time" - the supplied manual excerpt's definition of the `t` selector in `-newerXY`.

## Connections
- [[FileTimestampFiltering]] - captures the reference-file, direct-date, negation, and range-selection patterns.
- [[CLICommandGrammar]] - `find` composes predicates and negation into a compact query grammar.
- [[AutomationFriendlyCLI]] - timestamp predicates make filesystem selection reusable in scripts, subject to implementation and parsing constraints.

## Contradictions
- The workaround labels the timestamp on `some_file` a creation date, but ordinary `find -newer` compares modification times; the example therefore demonstrates an mtime reference rather than file birth time.
- The direct examples demonstrate “newer than,” relative time, and a bounded range but do not print a standalone older-than command. That operation follows by negating the newer-than predicate, with equality included in the complement.
- The capture does not identify the portability boundary of `-newermt` or specify timezone, locale, daylight-saving, and date-only boundary behavior, so scripts should not treat its natural-language examples as universally identical across environments.

---
title: "What does \"3>&1 1>&2 2>&3\" do in a script?"
type: source
tags: [bash, shell, redirection, file-descriptors]
date: 2012-07-10
source_file: "/mnt/ken_personal_wiki/Articles/What does 3&1 1&2 2&3 do in a script.md"
---

## Summary
This Unix & Linux Stack Exchange discussion explains how [[ShellRedirection]] uses an extra file descriptor as temporary storage to swap standard output and standard error. In `3>&1 1>&2 2>&3`, descriptor 3 first preserves standard output's current destination, descriptor 1 is redirected to standard error's destination, and descriptor 2 is then redirected to the saved destination; with `dialog`, this makes its result available on standard output for command substitution while its interactive display remains on standard error.

## Key Claims
- File descriptors 0, 1, and 2 conventionally represent standard input, standard output, and standard error; higher descriptor numbers can hold other open destinations.
- In `n>&m`, the `&` tells the shell to duplicate file descriptor `m` onto descriptor `n` rather than treat `m` as a filename.
- Redirections are evaluated from left to right, so `3>&1` saves descriptor 1's current destination before either standard stream is changed.
- The sequence `3>&1 1>&2 2>&3` swaps the destinations of standard output and standard error for the invoked command, while leaving descriptor 3 as an additional duplicate unless it is later closed.
- The `dialog` example uses the swap because dialog widgets conventionally return their selected value on standard error; after the swap, command substitution captures that value from standard output while the screen-oriented output goes to standard error.

## Key Quotes
> "The numbers are file descriptors and only the first three (starting with zero) have a standardized meaning" — Ulrich Dangel on why descriptor 3 can be used as temporary storage

> "It's swapping stdout and stderr." — Mikel's concise description of the sequence

## Connections
- [[ShellRedirection]] - extends the ordered-duplication model from combining streams to swapping their destinations through a temporary descriptor.
- [[AutomationFriendlyCLI]] - shows why a program's choice of output stream affects what command substitution or redirection can capture.
- [[CommandLineUX]] - separates a terminal-facing interactive display from the value returned to a calling script.

## Contradictions
- No direct contradiction with the existing wiki was identified. The example reinforces the existing left-to-right, point-in-time duplication model.

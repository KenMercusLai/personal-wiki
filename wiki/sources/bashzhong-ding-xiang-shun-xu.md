---
title: "Order of redirections - Unix & Linux Stack Exchange"
type: source
tags: [bash, linux, shell, redirection]
date: 2012-04-30
source_file: "/mnt/ken_personal_wiki/Articles/bash重定向顺序.md"
---

## Summary
This Unix & Linux Stack Exchange discussion explains [[ShellRedirection]] as an ordered sequence of file-descriptor changes rather than a simultaneous declaration of final destinations. In `> file.txt 2>&1`, standard output is first sent to the file and standard error then duplicates that destination; reversing the clauses leaves standard error attached to the terminal while only standard output moves to the file.

## Key Claims
- Shell redirections are evaluated from left to right, so changing their order can change observable behavior.
- `2>&1` duplicates file descriptor 1's current destination onto file descriptor 2 at that point in evaluation; it does not create a permanent link that follows later changes to descriptor 1.
- `command >somefile 2>&1` sends both standard output and standard error to `somefile` because descriptor 1 already targets the file when descriptor 2 is duplicated from it.
- `command 2>&1 >somefile` leaves standard error at descriptor 1's earlier destination, normally the terminal, and redirects only standard output to `somefile`.
- In Bash, `command &>somefile` is a compact way to redirect both standard output and standard error to the same file.

## Key Quotes
> "The order of redirection is important, and they should be read left to right." — shawn-j-goff's evaluation rule

> "stderr: redirect to whatever stdout is currently set to." — the duplication model described in Answer 3

## Connections
- [[ShellRedirection]] - captures the source's left-to-right file-descriptor model and its order-sensitive outcomes.
- [[BashAsMetaTool]] - redirection is one of the shell composition mechanisms that makes Bash useful as a general orchestration surface.
- [[CommandLineUX]] - separating normal output from diagnostics, or deliberately combining them, affects interactive and automated command behavior.

## Contradictions
- No direct contradiction with the existing wiki was identified. The source instead corrects the common misconception that `2>&1` means standard error will follow any later reassignment of standard output.

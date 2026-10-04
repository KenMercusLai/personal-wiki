---
title: "Shell Redirection"
type: concept
tags: [bash, shell, file-descriptors, command-line]
sources:
  - bashzhong-ding-xiang-shun-xu
last_updated: 2026-10-03
knowledge_schema: synthesis-v1
---

## Definition
[[ShellRedirection]] is the shell mechanism for changing where a command's numbered file descriptors read from or write to before the command runs.

## Current Synthesis
Redirection clauses are operational instructions evaluated from left to right, not an unordered description of final routing. A clause such as `2>&1` duplicates descriptor 1's destination as it exists at that moment onto descriptor 2. It therefore captures the current destination rather than establishing a live dependency that tracks later changes to descriptor 1.

This explains the practical difference between two superficially similar commands. In `command >file 2>&1`, descriptor 1 first moves to the file and descriptor 2 then duplicates that file destination, so both streams enter the file. In `command 2>&1 >file`, descriptor 2 first duplicates descriptor 1's original destination, normally the terminal, before descriptor 1 moves to the file; errors remain visible on the terminal while normal output is saved.

## Key Claims
- Shell redirections are applied from left to right.
- Descriptor duplication copies the referenced descriptor's current destination at the point of evaluation.
- `>file 2>&1` routes standard output and standard error to the same file.
- `2>&1 >file` normally keeps standard error on the terminal while routing standard output to the file.
- Bash's `&>file` provides a compact combined-output form, but the ordered descriptor model remains the clearer way to reason about more complex redirections.

## Evidence
- Evaluation rule: [[bashzhong-ding-xiang-shun-xu]] states that redirections should be read left to right and demonstrates the resulting descriptor states.
- Shared-file outcome: [[bashzhong-ding-xiang-shun-xu]] models `1>file 2>&1` as assigning descriptor 1 to the file and then duplicating that destination onto descriptor 2.
- Reversed-order outcome: [[bashzhong-ding-xiang-shun-xu]] shows that `2>&1 >file` copies the terminal destination to descriptor 2 before descriptor 1 is reassigned.
- Bash shorthand: [[bashzhong-ding-xiang-shun-xu]] identifies `&>file` as an equivalent combined redirection for the example discussed.

## Counterevidence & Qualifications
The source is a concise Stack Exchange explanation centered on Bash-like syntax and the usual initial terminal destinations. It does not cover input descriptors, append and here-document forms, pipelines, subshell scope, descriptor closing, portability across shells, or cases where descriptors 1 and 2 already point somewhere other than a terminal. Its syscall explanation is a useful mental model, but a shell's exact implementation need not be reduced to one literal `dup` call.

## What Changed
- Created the initial concept and made point-in-time descriptor duplication the central explanation for redirection order.

## Related Concepts
- [[BashAsMetaTool]] - redirection helps Bash compose commands, files, diagnostics, and downstream processing.
- [[CommandLineUX]] - output-stream routing determines what users see interactively and what automation captures.
- [[AutomationFriendlyCLI]] - predictable separation of standard output and standard error makes command-line tools easier to script.

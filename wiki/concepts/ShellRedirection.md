---
title: "Shell Redirection"
type: concept
tags: [bash, shell, file-descriptors, command-line]
sources:
  - bashzhong-ding-xiang-shun-xu
  - what-does-3-1-1-2-2-3-do-in-a-script
last_updated: 2026-10-04
knowledge_schema: synthesis-v1
---

## Definition
[[ShellRedirection]] is the shell mechanism for changing where a command's numbered file descriptors read from or write to before the command runs.

## Current Synthesis
Redirection clauses are operational instructions evaluated from left to right, not an unordered description of final routing. A clause such as `2>&1` duplicates descriptor 1's destination as it exists at that moment onto descriptor 2. It therefore captures the current destination rather than establishing a live dependency that tracks later changes to descriptor 1. The `&` distinguishes a descriptor operand from a filename, and descriptors above the conventional 0, 1, and 2 can preserve destinations temporarily.

This explains the practical difference between two superficially similar commands. In `command >file 2>&1`, descriptor 1 first moves to the file and descriptor 2 then duplicates that file destination, so both streams enter the file. In `command 2>&1 >file`, descriptor 2 first duplicates descriptor 1's original destination, normally the terminal, before descriptor 1 moves to the file; errors remain visible on the terminal while normal output is saved.

The same model explains a stream swap. In `3>&1 1>&2 2>&3`, descriptor 3 saves standard output's original destination, descriptor 1 takes standard error's destination, and descriptor 2 takes the destination saved in descriptor 3. In the documented `dialog` command, this routes the widget's returned value onto standard output so command substitution captures it, while the interactive display uses standard error.

## Key Claims
- Shell redirections are applied from left to right.
- Descriptor duplication copies the referenced descriptor's current destination at the point of evaluation.
- A spare descriptor can preserve one destination while standard output and standard error are swapped.
- `>file 2>&1` routes standard output and standard error to the same file.
- `2>&1 >file` normally keeps standard error on the terminal while routing standard output to the file.

## Evidence
- Evaluation rule: [[bashzhong-ding-xiang-shun-xu]] states that redirections should be read left to right and demonstrates the resulting descriptor states.
- Descriptor syntax and temporary storage: [[what-does-3-1-1-2-2-3-do-in-a-script]] explains that `>&` duplicates an existing descriptor and uses descriptor 3 to preserve standard output's initial destination.
- Shared-file outcome: [[bashzhong-ding-xiang-shun-xu]] models `1>file 2>&1` as assigning descriptor 1 to the file and then duplicating that destination onto descriptor 2.
- Reversed-order outcome: [[bashzhong-ding-xiang-shun-xu]] shows that `2>&1 >file` copies the terminal destination to descriptor 2 before descriptor 1 is reassigned.
- Stream swap and capture: [[what-does-3-1-1-2-2-3-do-in-a-script]] traces `3>&1 1>&2 2>&3` and applies it to capturing `dialog`'s result through command substitution.
- Combined-output shorthand: [[bashzhong-ding-xiang-shun-xu]] identifies `&>file` as an equivalent Bash form for routing both standard streams to one file.

## Counterevidence & Qualifications
The evidence consists of two concise Stack Exchange explanations centered on Bash-like syntax and usual initial terminal destinations. It does not comprehensively cover input descriptors, append and here-document forms, pipelines, subshell scope, descriptor lifecycle, portability across shells, or cases where descriptors 1 and 2 already point somewhere other than a terminal. The swap leaves descriptor 3 open for the command unless it is explicitly closed, a lifecycle detail the source does not discuss. The earlier source's syscall explanation is a useful mental model, but a shell's exact implementation need not be reduced to one literal `dup` call. The `dialog` behavior is program-specific rather than a general convention that interactive results belong on standard error.

## What Changed
- Extended the ordered-duplication model to explain how a spare descriptor enables a true standard-output/standard-error destination swap.
- Added the `dialog` command-substitution case as a concrete example of stream routing adapting a program's interface for automation.

## Related Concepts
- [[BashAsMetaTool]] - redirection helps Bash compose commands, files, diagnostics, and downstream processing.
- [[CommandLineUX]] - output-stream routing determines what users see interactively and what automation captures.
- [[AutomationFriendlyCLI]] - predictable separation of standard output and standard error makes command-line tools easier to script.

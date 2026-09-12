---
title: "Windows Subsystem for Linux"
type: entity
tags: [developer-tools, windows, linux, virtualization]
sources:
  - 4wk-clean-uninstall-then-reinstall-of-wsl-on-windows-10-with-systemd-support
last_updated: 2026-09-12
knowledge_schema: synthesis-v1
---

## Overview
[[WindowsSubsystemForLinux]] is the Windows developer-environment layer discussed in the source as something that can be cleanly removed, reinstalled, configured with native systemd support, and switched between Linux distributions.

## Current Profile
The source presents Windows Subsystem for Linux as a practical local development platform whose state spans registered distributions, installed distribution apps, Windows optional features, per-distribution `/etc/wsl.conf`, and system-wide `.wslconfig`. The author's goal is to move from a long-running genie-based setup to Microsoft's native systemd path on Windows 10, using a clean reinstall to clear old distro and feature state before reinstalling WSL and enabling systemd inside the Linux distribution.

## Key Characteristics
- Supports multiple Linux distributions that can be listed, unregistered, installed, and set as default.
- Depends on Windows feature state such as Virtual Machine Platform and Windows Subsystem for Linux.
- Can be reinstalled through a short `wsl --install` flow followed by reboot and first-run distribution setup.
- Supports distribution-level boot and interop settings through `/etc/wsl.conf`.
- Keeps system-wide `.wslconfig` separate from distro cleanup, so it may need manual review after reinstall.

## Evidence
- Distribution lifecycle: [[4wk-clean-uninstall-then-reinstall-of-wsl-on-windows-10-with-systemd-support]] uses `wsl -l -v`, `wsl --unregister`, `wsl --list --online`, `wsl --install -d Debian`, and `wsl --set-default Debian`.
- Windows feature dependency: [[4wk-clean-uninstall-then-reinstall-of-wsl-on-windows-10-with-systemd-support]] disables Virtual Machine Platform and Windows Subsystem for Linux before rebooting.
- Reinstall flow: [[4wk-clean-uninstall-then-reinstall-of-wsl-on-windows-10-with-systemd-support]] describes `wsl --install`, reboot, and Ubuntu first-run username setup.
- Configuration surface: [[4wk-clean-uninstall-then-reinstall-of-wsl-on-windows-10-with-systemd-support]] enables systemd and optionally disables Windows PATH append through `/etc/wsl.conf`.
- Separate global config: [[4wk-clean-uninstall-then-reinstall-of-wsl-on-windows-10-with-systemd-support]] warns that `.wslconfig` is not deleted or reset by these steps.

## Qualifications
This page is currently grounded in one procedural note. It does not compare WSL versions, document Windows 11 behavior, cover backup/export workflows before unregistering distributions, or verify current Microsoft support policy beyond what the source reports.

## What Changed
- Created the Windows Subsystem for Linux entity page from the clean reinstall and systemd setup note.

## Relationships
- [[NativeSystemdInWSL]] - WSL is the platform whose native systemd boot behavior is configured.
- [[DeveloperTooling]] - WSL is used here as a developer environment that benefits from repeatable setup and recovery procedures.
- [[RuntimeConfiguration]] - WSL behavior is shaped by configuration files such as `/etc/wsl.conf` and `.wslconfig`.
- [[ContainerApplicationStartup]] - both topics concern boot-time behavior and the boundary between platform configuration and runtime process initialization.

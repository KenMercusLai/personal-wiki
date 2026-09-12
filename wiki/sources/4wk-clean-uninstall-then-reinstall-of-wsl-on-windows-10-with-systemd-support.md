---
title: "4wk - Clean Uninstall Then Reinstall of WSL on Windows 10 with systemD Support"
type: source
tags: [wsl, windows, developer-environment, systemd]
date: 2026-09-12
source_file: "/mnt/ken_personal_wiki/Articles/4wk - Clean Uninstall Then Reinstall of WSL on Windows 10 with systemD Support.md"
---

## Summary
This procedural note explains how to remove old [[WindowsSubsystemForLinux]] distributions and Windows feature state, reinstall WSL on Windows 10, and enable [[NativeSystemdInWSL]] without the older genie workaround. It treats the cleanup as a fix for a stale or problematic WSL setup, including an infinite Windows RemoteApp error, then gives the verification command for checking systemd inside the Linux distribution.

## Key Claims
- Windows 10 WSL can use native systemd support, making genie unnecessary for this setup.
- A clean reinstall means unregistering existing WSL distributions, uninstalling Linux distribution apps, disabling the Virtual Machine Platform and Windows Subsystem for Linux Windows features, and rebooting.
- The current WSL install path can be as simple as running `wsl --install`, rebooting, and completing Ubuntu's first-run account setup.
- Users can install and switch to another distribution such as Debian with `wsl --list --online`, `wsl --install -d Debian`, and `wsl --set-default Debian`.
- Native systemd support is enabled inside the distribution through `/etc/wsl.conf`, while system-wide `.wslconfig` remains a separate file that is not reset by the distro cleanup.

## Key Quotes
> "I wanted to use the new \"right way\" to enable systemD on Windows Subsystem for Linux (without genie)" - motivation

> "`wsl --set-default-version 2` is not needed anymore." - distribution setup note

## Connections
- [[WindowsSubsystemForLinux]] - the source is a hands-on uninstall, reinstall, distribution selection, and shutdown procedure for WSL.
- [[NativeSystemdInWSL]] - the source's main configuration goal is enabling native systemd support through `/etc/wsl.conf`.
- [[DeveloperTooling]] - WSL is treated as a developer environment whose setup and recovery steps should be explicit and repeatable.
- [[RuntimeConfiguration]] - `/etc/wsl.conf` and `.wslconfig` separate distribution-level boot/interop settings from broader WSL-wide configuration.

## Contradictions
- None identified.

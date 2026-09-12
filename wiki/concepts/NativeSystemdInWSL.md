---
title: "Native systemd in WSL"
type: concept
tags: [wsl, systemd, developer-environment, configuration]
sources:
  - 4wk-clean-uninstall-then-reinstall-of-wsl-on-windows-10-with-systemd-support
last_updated: 2026-09-12
knowledge_schema: synthesis-v1
---

## Definition
[[NativeSystemdInWSL]] is the use of WSL's built-in support for starting systemd inside a Linux distribution, configured through that distribution's `/etc/wsl.conf` instead of an external workaround such as genie.

## Current Synthesis
The source frames native systemd in WSL as the "right way" to replace a long-running genie-based setup once Windows 10 gained support comparable to the Windows 11 WSL path. The practical configuration is small: inside the distribution, create or edit `/etc/wsl.conf`, add `[boot]` with `systemd=true`, optionally use `[interop] appendWindowsPath = false`, then shut down WSL from PowerShell so the next launch reads the new configuration.

The note also treats native systemd enablement as part of environment repair. Because old distributions, Store-installed Linux apps, Windows feature state, and global `.wslconfig` can all persist separately, the author first cleans WSL state before reinstalling and enabling systemd.

## Key Claims
- Native WSL systemd support can replace genie for this Windows 10 setup.
- Enabling systemd is a distribution-level setting in `/etc/wsl.conf`.
- WSL should be cleanly shut down after configuration so the setting is applied on the next launch.
- Optional interop configuration can remove Windows paths from the Linux `PATH`.
- Global `.wslconfig` is outside the distro cleanup path and needs separate manual attention when troubleshooting.

## Evidence
- Native replacement: [[4wk-clean-uninstall-then-reinstall-of-wsl-on-windows-10-with-systemd-support]] says the author wanted to enable systemd natively without genie after Windows 10 gained the feature.
- Boot setting: [[4wk-clean-uninstall-then-reinstall-of-wsl-on-windows-10-with-systemd-support]] sets `[boot]` and `systemd=true` in `/etc/wsl.conf`.
- Restart boundary: [[4wk-clean-uninstall-then-reinstall-of-wsl-on-windows-10-with-systemd-support]] runs `wsl --shutdown` from PowerShell before testing systemd.
- Interop setting: [[4wk-clean-uninstall-then-reinstall-of-wsl-on-windows-10-with-systemd-support]] optionally sets `[interop] appendWindowsPath = false`.
- Global config warning: [[4wk-clean-uninstall-then-reinstall-of-wsl-on-windows-10-with-systemd-support]] notes that `.wslconfig` is not deleted or reset by the uninstall/reinstall steps.

## Counterevidence & Qualifications
The source is a personal operational note, not a comprehensive WSL systemd reference. It does not cover backup/export before unregistering distributions, enterprise-managed Windows machines, alternate distributions beyond Debian and Ubuntu examples, or failure modes when systemd still does not start after configuration.

## What Changed
- Created the native systemd in WSL concept page from the clean reinstall source.

## Related Concepts
- [[RuntimeConfiguration]] - native systemd behavior is controlled by runtime configuration files.
- [[DeveloperTooling]] - WSL systemd support affects the reliability and fidelity of local development environments.
- [[ContainerApplicationStartup]] - both topics involve process startup expectations and platform boot semantics.
- [[SystemReliability]] - clean shutdown, explicit configuration, and verification are small-scale reliability practices for a local environment.

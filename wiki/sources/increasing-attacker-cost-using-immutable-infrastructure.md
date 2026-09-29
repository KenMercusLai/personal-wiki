---
title: "Increasing Attacker Cost Using Immutable Infrastructure"
type: source
tags: [docker, immutable-infrastructure, container-security, incident-response]
date: 2016-11-19
source_file: "/mnt/ken_personal_wiki/Articles/Increasing Attacker Cost Using Immutable Infrastructure.md"
---

## Summary
[[DiogoMonica]] uses a deliberately vulnerable PHP application and MariaDB stack to show how [[Docker]] image immutability can support investigation and rapid replacement after compromise. `docker diff` exposes changes in the container's copy-on-write layer, `docker commit` preserves the compromised state for later inspection, and a fresh container restores the known application artifact. Running the root filesystem read-only raises the cost of persistence and toolkit installation, but it does not fix remote code execution or prevent credential theft, database access, exfiltration, or abuse of deliberately writable mounts.

## Key Claims
- Docker's copy-on-write model keeps the base image unchanged while recording runtime filesystem additions and modifications in a separate container layer.
- `docker diff` can identify changed and added paths after an incident; in the demonstration it reveals a modified `index.html` and an added `shell.php`.
- Committing the compromised container before replacing it preserves a filesystem snapshot for later examination while a new container restores service from the known image.
- The `--read-only` flag blocks writes to the container root filesystem, preventing the demonstrated website defacement and PHP-shell download.
- A read-only root filesystem is a containment and persistence-resistance control, not a vulnerability fix: the demonstrated remote-code-execution path still permits code execution and may expose credentials and database data.
- Minimal images, sandboxing, and narrowly scoped writable paths can further reduce the tools and persistence options available after compromise.

## Key Quotes
> "Until we fix this RCE vulnerability, the attacker will still be able to execute code on our host, steal our credentials, and exfiltrate the data in our database." - explicit limit of the read-only-filesystem control.

> "The security of our applications will never be perfect, but having immutable infrastructure helps with incident response, allows fast-recovery, and makes the attacker's jobs harder." - the article's defense-in-depth conclusion.

## Connections
- [[DiogoMonica]] - practitioner-author presenting the vulnerable-container demonstration.
- [[Docker]] - supplies the image, copy-on-write diff, snapshot, replacement, and read-only-root mechanisms.
- [[ImmutableInfrastructure]] - known artifacts and replacement support recovery while runtime write restrictions raise persistence cost.
- [[IncidentManagement]] - investigation and restore-first response are separated by preserving the compromised state before replacement.
- [[ContainerNativePractice]] - read-only roots require explicit writable mounts for legitimate runtime paths.
- [[StartupSecurityDebt]] - the intentional `eval` vulnerability illustrates why infrastructure hardening cannot substitute for repairing application code.

## Contradictions
- The article informally calls containers immutable, but its own `docker diff` output demonstrates that an ordinary running container has a mutable copy-on-write layer. The base image is immutable; the root filesystem becomes read-only only when the separate `--read-only` control is applied.
- Restarting from the original image restores the application files shown in the demo, but it does not establish that credentials, database contents, external systems, or writable mounts remain trustworthy after compromise.
- A committed compromised container preserves a convenient filesystem snapshot, not a complete forensic record. The source does not discuss volatile memory, network activity, external logs, chain of custody, or attacker tampering.

## Image Notes
- All five Obsidian embeds resolve to the same file. Despite its `.png` name, the file contains an HTML application shell for Diogo Mónica's website rather than image bytes.
- The intended architecture, application, defacement, and recovery visuals therefore could not be opened or interpreted and were not retained. No claim above relies on inferred visual content.

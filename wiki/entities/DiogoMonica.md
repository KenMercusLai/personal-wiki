---
title: "Diogo Mónica"
type: entity
tags: [security, containers, infrastructure]
sources:
  - increasing-attacker-cost-using-immutable-infrastructure
last_updated: 2026-09-30
knowledge_schema: synthesis-v1
---

## Overview
[[DiogoMonica]] is a security practitioner represented in the wiki by a Docker demonstration that separates rapid recovery and persistence resistance from remediation of the underlying application vulnerability.

## Current Profile
Mónica presents immutable container artifacts as both an operational recovery mechanism and a security boundary whose value depends on precise runtime controls. His example preserves a compromised container for inspection, replaces it from a known image, and then applies a read-only root filesystem to block the demonstrated file writes. He explicitly rejects treating this hardening as complete protection because remote code execution still permits credential theft and data exfiltration.

## Key Characteristics
- Uses executable demonstrations to connect container filesystem mechanics with incident response.
- Treats fast restoration and later investigation as separable response objectives.
- Frames read-only filesystems, minimal images, and sandboxing as defense-in-depth controls.
- Preserves the distinction between raising attacker cost and fixing the vulnerable application.

## Evidence
- Incident workflow: [[increasing-attacker-cost-using-immutable-infrastructure]] uses `docker diff`, `docker commit`, container replacement, and later snapshot inspection after a simulated compromise.
- Persistence resistance: [[increasing-attacker-cost-using-immutable-infrastructure]] demonstrates `--read-only` blocking the attacker's attempted `index.html` write.
- Security boundary: [[increasing-attacker-cost-using-immutable-infrastructure]] says the unresolved remote-code-execution flaw still permits execution, credential theft, and database exfiltration.

## Qualifications
The profile is based on one 2016 practitioner article and one deliberately simple PHP/MySQL demonstration. It does not establish comparative incident outcomes, comprehensive container isolation, or Mónica's broader body of work. The article's intended visuals were unavailable because every embedded `.png` path contained the same HTML application shell rather than an image.

## What Changed
- Established the entity from the article's container-security and incident-response argument.

## Relationships
- [[Docker]] - platform used for the compromise, diff, snapshot, replacement, and read-only-root demonstration.
- [[ImmutableInfrastructure]] - operating model Mónica connects to investigation, recovery, and higher persistence cost.
- [[IncidentManagement]] - response context for preserving compromised state and restoring a known artifact.
- [[ContainerNativePractice]] - runtime design context for explicit writable paths and constrained container behavior.

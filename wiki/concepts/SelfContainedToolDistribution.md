---
title: "Self-Contained Tool Distribution"
type: concept
tags: [software-distribution, offline-systems, packaging, infrastructure]
sources:
  - self-contained-dist-tools
last_updated: 2026-10-13
knowledge_schema: synthesis-v1
---

## Definition
[[SelfContainedToolDistribution]] is the packaging and delivery of an operational tool with its application code, compatible dependencies, auxiliary executables, integrity metadata, and output viewer inside an isolated artifact set that avoids modifying the target's package-managed environment.

## Current Synthesis
The [[BareMetalCheck]] case shows that self-containment is layered and conditional, not synonymous with one native executable or zero prerequisites. A guaranteed Python runtime can justify a compact shiv zipapp instead of an embedded interpreter. The same archive can expose multiple console entry points, allowing the product CLI and [[Ansible]] to share one dependency set. Native tools require a different boundary: compatible binaries and selected shared libraries travel in archives whose rpaths resolve relative to their own location.

Delivery completes the pattern. A manifest states compatibility and required paths, build outputs carry separately generated checksums, the controller selects packages by OS, architecture, role, and test prerequisites, and the target receives only necessary archives. Digest comparison and temporary verified extraction make repeat execution cheaper and safer. A single-file report extends self-containment to consumption by embedding code, styles, and encoded result data without network requests.

## Key Claims
- Self-containment must cover execution, orchestration, auxiliary tools, verification, and result consumption across the whole workflow.
- Reusing a guaranteed host runtime can reduce artifact size, but converts runtime version, ABI, platform, and architecture into explicit compatibility requirements.
- One packaged dependency environment can safely expose multiple program entry points when their invocation boundary is controlled.
- Native archives become location-independent through private libraries and relative runtime lookup, while host-bound drivers and kernel components remain external prerequisites.
- Compatibility manifests and artifact checksums serve different purposes and should be generated and validated at their appropriate lifecycle stages.
- Conditional, digest-aware distribution reduces transfer and target mutation, especially for role-specific or load-generating tools.
- Single-file reports preserve offline portability only when scripts, styles, and data require no external fetches.

## Evidence
- Layered artifact boundary: [[self-contained-dist-tools]] packages the CLI and Ansible in a `.pyz`, native tools in tar archives, and the report template in the delivery bundle.
- Runtime reuse and entry switching: [[self-contained-dist-tools]] relies on Python 3.10+ and uses `SHIV_CONSOLE_SCRIPT` for the embedded Ansible entry point.
- Relocatable native execution: [[self-contained-dist-tools]] copies selected shared libraries and uses `$ORIGIN/../lib` rpaths.
- Controlled distribution: [[self-contained-dist-tools]] filters manifests, verifies checksums, gates active tests, and skips matching installations.
- Offline output: [[self-contained-dist-tools]] injects base64 JSON into an all-inline HTML template and supports both `file://` and temporary HTTP access.

## Counterevidence & Qualifications
The evidence is one first-person architecture account without released code, reproducible builds, signatures, a software bill of materials, security analysis, or compatibility test matrix. A compressed delivery containing several archives is operationally self-contained but not literally one executable. `$ORIGIN` resolves packaged libraries but cannot erase glibc, kernel, driver, GPU, firmware, CPU-architecture, or licensing constraints. Bundling dependencies also transfers patching, provenance, vulnerability response, and update responsibility to the distributor. Base64 makes JSON safe to embed in the described placeholder but is encoding rather than encryption or authenticity protection.

## What Changed
- Established self-containment as a layered compatibility contract rather than a claim of absolute dependency independence.
- Connected packaging choices to integrity, qualification gates, idempotent delivery, and offline report consumption.

## Related Concepts
- [[DeploymentAutomation]] - performs selective transfer, verification, installation, and execution across target nodes.
- [[ImmutableInfrastructure]] - shares the preference for versioned isolated artifacts over ad hoc mutation of system-managed state.
- [[InfrastructureAsCode]] - manifests and playbooks encode repeatable compatibility and operational intent.
- [[DesktopApplicationPackaging]] - adjacent dependency-bundling practice with a different desktop-runtime and release boundary.
- [[ExternalServiceDependency]] - offline self-containment deliberately removes network-service requirements from execution and report viewing.
- [[SupplyChainSecurity]] - bundled wheels, binaries, libraries, checksums, and build provenance create a security and maintenance boundary.

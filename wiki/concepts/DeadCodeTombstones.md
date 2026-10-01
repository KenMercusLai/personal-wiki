---
title: "Dead Code Tombstones"
type: concept
tags: [software-engineering, dead-code, instrumentation, code-maintenance]
sources:
  - nestoria-dev-blog-tombstones-for-dead-code
last_updated: 2026-10-01
knowledge_schema: synthesis-v1
---

## Definition
[[DeadCodeTombstones]] are lightweight runtime probes placed in code suspected of being unused so maintainers can observe real execution before deleting or refactoring it.

## Current Synthesis
The Nestoria implementation treats apparent deadness as a hypothesis rather than a static fact. A developer places a tombstone call at the suspect path and supplies the date and author. If production reaches it, the probe records time, source location, subroutine, and a stack trace; the live path becomes a “vampire.” Separate files, scheduled collection, expiry, and a web report turn those events into a cleanup queue.

The probe sits below application correctness in priority. It returns on setup, file, size, or lock problems; uses a non-blocking lock; caps each tombstone file; and drops later events once evidence of execution is sufficient. This makes the method a form of bounded observability for a maintenance decision, not an exact analytics system.

Absence of events remains conditional evidence. A tombstone is credible only after an observation window spans the path's realistic triggers, hosts, schedules, feature states, and failure modes, while the telemetry path itself is known to be working. Stack traces help distinguish callers and may support safe refactoring even when deletion is not justified.

## Key Claims
- Suspected dead code should be treated as a falsifiable production hypothesis before deletion.
- Invocation existence and call-path diversity are often more useful than exact event volume for deciding whether code is live.
- Probe metadata should identify ownership, age, location, time, and calling context so evidence leads to an actionable cleanup decision.
- Instrumentation must have bounded storage, concurrency, latency, and failure effects when it runs inside production requests.
- Central collection, retention, and reporting turn isolated probes into a repeatable maintenance workflow.
- A quiet probe supports deletion only when coverage and telemetry reliability make the observation window representative.

## Evidence
- Runtime falsification: [[nestoria-dev-blog-tombstones-for-dead-code]] reports preserving code that looked dead after tombstone events showed it still executed.
- Actionable context: [[nestoria-dev-blog-tombstones-for-dead-code]] records the author, tombstone date, invocation time, file, line, subroutine, and full stack trace.
- Bounded impact: [[nestoria-dev-blog-tombstones-for-dead-code]] uses one file per tombstone, a file-size threshold, non-blocking locks, and return-on-error behavior.
- Maintenance workflow: [[nestoria-dev-blog-tombstones-for-dead-code]] describes scheduled central collection and expiry plus a report separating uncalled tombstones, vampires, and deleted probes.
- Report semantics: the retained screenshot in [[nestoria-dev-blog-tombstones-for-dead-code]] shows commit context, time since placement, first and last sightings, locations, and stack-trace access for decisions.

## Counterevidence & Qualifications
The evidence is one unquantified company retrospective and a partial implementation; Nestoria did not publish the collection jobs or report code. Non-observation can be a false negative when traffic is unrepresentative, rare jobs or recovery paths have not run, feature flags hide the path, some hosts are not collected, logging fails, or retention is too short. Fail-open behavior protects the product but weakens evidentiary completeness. The approach also records stack traces and process context, so implementations need appropriate access controls, retention, redaction, and storage review.

## What Changed
- Established dead-code tombstones as bounded production instrumentation for evidence-led deletion and refactoring.
- Made observation coverage and telemetry reliability explicit limits on interpreting silence as deadness.

## Related Concepts
- [[ServiceObservability]] - supplies runtime evidence about whether and how marked code executes.
- [[CentralizedLogging]] - aggregates local tombstone events for shared analysis and reporting.
- [[TechnicalDebt]] - dead-code removal reduces maintenance burden when evidence supports deletion.
- [[SoftwareVerification]] - production probes complement tests and static analysis for rare paths.
- [[ChangeSafety]] - evidence before deletion reduces the risk of removing indirectly used behavior.

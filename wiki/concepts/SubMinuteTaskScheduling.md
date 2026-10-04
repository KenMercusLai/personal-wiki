---
title: "Sub-Minute Task Scheduling"
type: concept
tags: [scheduling, cron, systemd, linux]
sources:
  - running-a-cron-every-30-seconds
last_updated: 2026-10-04
knowledge_schema: synthesis-v1
---

## Definition
[[SubMinuteTaskScheduling]] is the triggering of recurring work at intervals shorter than one minute, including the choice of scheduler and the rules for timing, overlap, delay, and recovery.

## Current Synthesis
Traditional cron cannot directly represent a 30-second interval because its finest schedule field is minutes. The source offers two cron-adjacent approximations: launch the same command every minute twice, delaying one copy by 30 seconds, or keep a loop alive that coordinates the payload with a 30-second sleep. On a systemd-based Linux host, a timer unit provides a more explicit sub-minute trigger by activating a service unit after boot and after prior activation.

The scheduler choice does not remove execution semantics. The two-entry cron pattern can overlap when work lasts longer than its interval, while the shown coordinated loop delays the next cycle after an overrun. A systemd timer separates triggering from service execution, but the source does not establish a universal policy for missed runs, concurrent starts, clock changes, restart recovery, or failure notification.

## Key Claims
- Conventional cron has minute-level granularity and cannot directly express a 30-second interval.
- Two per-minute cron entries, one delayed by 30 seconds, approximate two evenly offset triggers per minute.
- Offset cron entries require duplicated commands to remain synchronized and may overlap when execution exceeds the interval.
- A coordinated loop can prevent catch-up overlap by letting an overlong payload delay the next cycle.
- A systemd timer separates the recurring trigger from the service and can request sub-minute intervals.
- Requested cadence and accuracy are not complete reliability guarantees; overrun, failure, restart, and observation policies still matter.

## Evidence
- Cron boundary: [[running-a-cron-every-30-seconds]] says cron does not provide sub-minute resolution and that `*/30` in the minute field means every 30 minutes.
- Offset approximation: [[running-a-cron-every-30-seconds]] supplies two every-minute entries, with the second sleeping for 30 seconds before invoking the same command.
- Loop behavior: [[running-a-cron-every-30-seconds]] starts the sleep before the payload and waits afterward, preserving the remaining portion of the interval when execution takes at most 30 seconds and delaying the next cycle after an overrun.
- Timer model: [[running-a-cron-every-30-seconds]] shows a systemd timer activating a service through `OnBootSec=10`, `OnUnitActiveSec=10`, and `AccuracySec=1ms`.
- Precision tradeoff: [[running-a-cron-every-30-seconds]] notes that reducing `AccuracySec` below its default increases CPU wakeups.

## Counterevidence & Qualifications
The source is a compact community answer set rather than a complete scheduler comparison. Its claim that systemd timers theoretically support nanosecond granularity should not be read as a guarantee of nanosecond execution precision under real kernel, clock, load, power-management, and service-start conditions. The examples omit locking, idempotency, timeout, monitoring, failure alerts, persistent catch-up, time-zone and daylight-saving behavior, randomized delay, privileges, environment differences, and shutdown handling. The loop also requires independent supervision to recover after process or host failure.

## What Changed
- Created a model that separates sub-minute trigger expression from overrun and recovery behavior.
- Added offset cron entries, a coordinated loop, and systemd timers as distinct implementation choices.
- Qualified configured timer accuracy as different from guaranteed execution precision.

## Related Concepts
- [[TaskQueueDesign]] - adds durable scheduling, retries, worker separation, and recoverable state beyond a local recurring trigger.
- [[SystemReliability]] - requires periodic work to expose failures, overruns, missed executions, and recovery behavior.
- [[BashAsMetaTool]] - shell loops and `sleep` can compose a lightweight recurring runner.
- [[RemoteVideoRecording]] - uses cron for minute-level periodic capture and illustrates a workload shaped by scheduler cadence.

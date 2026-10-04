---
title: "Running a cron every 30 seconds"
type: source
tags: [cron, linux, scheduling, systemd]
date: 2012-03-08
source_file: "/mnt/ken_personal_wiki/Articles/Running a cron every 30 seconds.md"
---

## Summary
This [[StackOverflow]] answer set explains that conventional cron schedules have one-minute granularity, so a nominal 30-second cadence requires either two minute-based entries with one delayed by `sleep 30`, a long-running loop, or a different scheduler. It presents a systemd timer as the cleaner Linux alternative while exposing important distinctions among trigger cadence, completion time, overlap, and actual execution accuracy.

## Key Claims
- `*/30` in cron's minute field means every 30 minutes, not every 30 seconds.
- Traditional cron cannot directly express a sub-minute interval.
- Two per-minute cron entries can approximate a 30-second cadence when one invocation waits 30 seconds before running.
- A loop that starts `sleep 30` in the background before executing the payload and then waits keeps starts near a 30-second cadence when the payload completes within that interval; longer work delays the next cycle instead of creating catch-up starts.
- A systemd timer can trigger a service at a sub-minute interval through `OnBootSec`, `OnUnitActiveSec`, and an appropriately small `AccuracySec`.
- Scheduling a trigger does not by itself define what should happen when an earlier invocation is still running.

## Key Quotes
> "Cron does not go down to sub-minute resolutions." — Answer 1

> "timers are units that start service units when a timer elapses." — Answer 2

## Connections
- [[SubMinuteTaskScheduling]] - captures the choice among offset cron entries, an interval loop, and a systemd timer.
- [[StackOverflow]] - hosts the question and community answers summarized here.
- [[TaskQueueDesign]] - addresses durable state, retries, concurrency, and recovery beyond a local periodic trigger.
- [[SystemReliability]] - repeated work needs explicit overlap, failure, monitoring, and recovery behavior in addition to a cadence.

## Contradictions
- No direct contradiction with the existing wiki was identified. The source instead qualifies the cron-based recording examples elsewhere in the wiki by showing that cron itself cannot express intervals shorter than one minute.

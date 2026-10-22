---
title: "Leap-Second Smearing"
type: concept
tags: [time-synchronization, leap-seconds, distributed-systems, clocks]
sources:
  - ntp-service
last_updated: 2026-10-22
knowledge_schema: synthesis-v1
---

## Definition
[[LeapSecondSmearing]] changes clock rate in small increments over a bounded interval so systems absorb a leap second without an abrupt repeated, skipped, or stepped second.

## Current Synthesis
Smearing trades short-lived divergence from unsmeared UTC for smoother application-visible time. In Facebook's design, GNSS supplies a leap indicator to chrony, Stratum 2 servers begin a synchronized smooth smear when the event occurs at 00:00 UTC, and Stratum 3 servers consume the result without special leap awareness. The selected policy takes approximately 18 hours and uses a sine-shaped transition intended to reduce application risk.

Coordination is part of correctness. If several Stratum 2 servers expose materially different smear phases or curves, clients can receive inconsistent time depending on which server they query. A service must therefore define the signal source, start time, duration, shape, serving tier, and compatibility boundary as one policy rather than treating smearing as a local daemon option.

## Key Claims
- A smear preserves continuous-looking server time by distributing one second of adjustment across many small rate changes.
- Applying the policy at an intermediate tier lets downstream serving nodes remain unaware of leap events.
- Multiple smear servers must use closely matched curves and timing to avoid disagreement inside the service.
- Different providers or clients may use incompatible leap handling, so smeared time is temporarily not identical to unsmeared UTC.

## Evidence
- Policy placement: [[ntp-service]] assigns leap-second handling to Stratum 2 and presents Stratum 3 as already-smeared serving capacity.
- Trigger and duration: [[ntp-service]] says chrony uses the GNSS leap indicator and Facebook chose an approximately 18-hour post-event smear.
- Curve shape: [[ntp-service]] retains a chart in which the Stratum 1 appliance steps while the chrony tier follows a smooth transition toward the new second.

## Counterevidence & Qualifications
The source explains one operator's policy but provides no cross-provider interoperability test, application-failure study, maximum rate error, synchronization tolerance among smear nodes, client behavior, negative-leap handling, or comparison with pre-event and symmetric smear windows. Continuous time is safer for many applications but is not identical to strict UTC during the smear, and mixing smeared and unsmeared sources can create disagreement.

## What Changed
- Established leap smearing as a distributed service policy spanning reference signal, curve, tier, and client compatibility.
- Added the temporary UTC-divergence and multi-server-consistency boundaries.

## Related Concepts
- [[NetworkTimeSynchronization]] - distributes the adjusted clock through the service hierarchy.
- [[Chrony]] - implements the described GNSS-triggered post-event smear.
- [[ChangeSafety]] - frames a coordinated time-policy transition as a staged production change with compatibility risk.
- [[HardwareTimestamping]] - improves packet measurement but does not determine leap policy.

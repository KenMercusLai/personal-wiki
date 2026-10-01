---
title: "Learning from the Post-Mortem"
type: source
tags: [postmortem, network-engineering, incident-management, observability]
date: 2020-05-18
source_file: "/mnt/ken_personal_wiki/Articles/Rule 11 Reader - Learning from the Post-Mortem.md"
---

## Summary
[[RussWhite]] argues that useful [[BlamelessPostmortem|postmortems]] should move beyond configuration mistakes, vendor defects, blame displacement, and one-time action lists to examine the systems and workflows that shaped an incident. His proposed review maps the setup, detection, and troubleshooting processes so [[IncidentManagement]] can change organizational conditions, reduce detection dwell time without uncontrolled false positives, and preserve diagnostic reasoning for faster future response.

## Key Claims
- Postmortems can become repetitive rituals when teams produce a whiteboard list and a promise of non-recurrence without changing the conditions that reproduce failure.
- Narrow focus on an incorrect configuration, defective appliance, or individual innocence can produce safe conclusions while avoiding organizational, political, and process causes.
- The setup workflow should reconstruct why hardware, software, or a protocol was deployed and which commitments or political drivers made the failure consequential.
- The detection workflow should reconstruct how the problem surfaced, where it could have been caught earlier, and how lower dwell time must be balanced against false-positive cost.
- The troubleshooting workflow should record what responders checked, why and how they checked it, and what each check taught them.
- Preserved troubleshooting flowcharts can reveal missing instrumentation and hard-to-find evidence, shortening later diagnosis and root-cause discovery.

## Key Quotes
> "We focus so much on mean time to innocence" - on blame displacement obstructing learning.

> "map out three distinct workflows" - on reviewing setup, detection, and troubleshooting rather than searching only for one root cause.

> "focus on systems and workflows" - on the proposed level of postmortem analysis.

## Connections
- [[RussWhite]] - network engineer and Rule 11 Reader author proposing the three-workflow review.
- [[BlamelessPostmortem]] - gains a concrete method for moving from nominal blame avoidance to system and workflow learning.
- [[IncidentManagement]] - gains preserved response reasoning and upstream setup analysis as inputs to future preparation and response.
- [[ServiceObservability]] - gains detection-path reconstruction, dwell-time reduction, false-positive qualification, and instrumentation improvement.
- [[FailureOwnership]] - the article contrasts actionable system responsibility with efforts to establish individual innocence.
- [[SystemReliability]] - recurring incidents are treated as products of interacting organizational, deployment, detection, and diagnostic conditions.

## Contradictions
- The article calls its suggestions only part of a solution and provides no worked incident, comparison group, outcome data, implementation detail, or evidence that workflow mapping reduces recurrence, dwell time, or repair time.
- Root-cause analysis and workflow mapping need not be alternatives: technical causal detail can remain necessary for containment and repair, while broader setup, detection, and troubleshooting analysis prevents the proximate error from becoming the whole explanation.
- The account generalizes from the author's network-engineering experience and may not establish how common or ineffective postmortems are across organizations.

---
title: "Automation Error Tolerance"
type: concept
tags: [ai, automation, trust, accountability]
sources:
  - dhh-its-easier-to-forgive-a-human-than-a-robot
last_updated: 2026-09-26
knowledge_schema: synthesis-v1
---

## Definition
[[AutomationErrorTolerance]] is the acceptable failure threshold applied to automated systems, especially when people judge machine-caused mistakes more harshly than equivalent or more frequent human mistakes.

## Current Synthesis
The source proposes a gap between comparative accuracy and deployable accuracy. An AI system can outperform the average human and still fail the social test for adoption because its errors appear designed, replicated, and attributable to one provider. Autonomous driving makes that concentration visible in deaths; medical diagnosis adds malpractice exposure; customer support turns it into trust and reputation damage. On this account, evaluation must consider error severity, who bears harm, who is blamed, and whether users can forgive the apparent agent—not only the aggregate error rate.

The mechanism is plausible but not established by the source. Its driving arithmetic, medical questions, and customer-support thresholds are illustrative thought experiments. The author also leaves open a competing dynamic: repeated exposure may normalize AI fallibility and make users more sympathetic to machines. The current judgment is therefore that asymmetric tolerance is a credible adoption constraint that requires domain-specific measurement, not a universal law or a reason to prefer objectively worse human performance.

## Key Claims
- Human-level or better average performance may be insufficient when automated failures receive disproportionate blame.
- Higher stakes and more concentrated provider liability can push the required machine error rate closer to zero.
- Aggregate benefit does not by itself settle legitimacy because harms, responsibility, and perceived agency may be distributed differently.
- Low-stakes domains still face trust costs when confident machine errors can damage customer relationships and word of mouth.
- Familiarity and widespread adoption may narrow the forgiveness gap, but the source offers no evidence about whether that occurs.

## Evidence
- Driving legitimacy: [[dhh-its-easier-to-forgive-a-human-than-a-robot]] uses a hypothetical autonomous fleet to show how fewer total deaths could still leave one provider visibly responsible for many deaths.
- Medical liability: [[dhh-its-easier-to-forgive-a-human-than-a-robot]] asks whether residual AI misdiagnoses could generate enough concentrated malpractice exposure to make a superior average system commercially untenable.
- Customer trust: [[dhh-its-easier-to-forgive-a-human-than-a-robot]] reports mixed AI-support results at 37signals and speculates that machine error might need to fall far below human error before customers accept it.
- Adaptation possibility: [[dhh-its-easier-to-forgive-a-human-than-a-robot]] explicitly considers whether widespread adoption could produce sympathy for fallible automated helpers.

## Counterevidence & Qualifications
The source is a short practitioner argument, not a behavioral study, legal analysis, medical evaluation, or controlled support benchmark. It does not separate intolerance of automation from novelty, media salience, opacity, lack of appeal, product overclaiming, unequal harm, or the fact that organizations can prevent one design defect from scaling across many cases. Its liability framing does not compare jurisdictions or current doctrines, and its suggested error rates are guesses. Human error is also institutional rather than purely individual, so responsibility may already be concentrated in employers, hospitals, regulators, and product makers. Domain-specific comparisons should therefore include severity distributions, human oversight, recourse, transparency, responsibility, and total system outcomes.

## What Changed
- Created a cross-domain concept separating comparative AI accuracy from socially acceptable machine accuracy.
- Treated concentrated accountability, liability, and trust as possible causes of asymmetric error tolerance.
- Preserved normalization through familiarity as an unresolved counter-hypothesis.

## Related Concepts
- [[AutonomousDrivingSafety]] - machine-caused deaths can face a stricter legitimacy threshold even when automation reduces aggregate harm.
- [[SystemReliability]] - acceptable error depends on consequence, detection, containment, and recovery rather than one average rate.
- [[AlgorithmicDecisionOpacity]] - poorly explained automated decisions can intensify distrust and make errors harder to contest.
- [[BeautifullyBrokenProducts]] - users sometimes forgive product defects when core value is strong, providing a contrasting account of tolerated imperfection.

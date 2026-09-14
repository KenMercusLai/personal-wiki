---
title: "Architecture Alignment Forces"
type: concept
tags: [architecture, governance, organizational-design]
sources:
  - blog-martin-fowler-the-strong-and-weak-forces-of-architecture
last_updated: 2026-09-14
knowledge_schema: synthesis-v1
---

## Definition
[[ArchitectureAlignmentForces]] is a governance model that adjusts architecture rules, coupling tolerance, and decision formality according to the strength of social and organizational alignment around the systems being changed.

## Current Synthesis
The source argues that architecture governance fails when it applies one rule across every level of a large organization. Strict central governance can disempower teams and slow ordinary local change, while total local autonomy can leave teams without useful shared constraints. The better question is the blast radius of the decision and the alignment strength among the people affected.

Inside a domain, teams usually share business concepts, domain expertise, related systems, and change priorities. That strong alignment can make negotiation fast enough that some tighter coupling, shared code, informal technology leadership, and cross-team contribution are tolerable. Across a vertical, alignment weakens and the same practices require more monitoring, proposal sharing, or coordination. Across the whole organization, alignment is weak enough that published APIs, events, infrastructure, and shared libraries need loose coupling, self-service boundaries, versioning, backward compatibility, and explicit deprecation strategies.

## Key Claims
- Architecture governance should vary with organizational scope and decision blast radius.
- Strong domain-level alignment can justify faster local decisions and some tighter coupling.
- Weaker vertical-level alignment requires more formal coordination and more careful shared assets.
- Whole-organization decisions need the strongest encapsulation, versioning, and contract discipline.
- Coupling is not intrinsically bad; its cost depends on who must coordinate changes and how easily they can align.
- Technology choice, shared code, code contribution, and integration patterns all need different rules at domain, vertical, and organization scope.

## Evidence
- Organization model: [[blog-martin-fowler-the-strong-and-weak-forces-of-architecture]] describes [[MYOB]] teams grouped into domains and domains grouped into verticals.
- Strong-force diagram: [[blog-martin-fowler-the-strong-and-weak-forces-of-architecture]] shows a domain containing teams with close alignment, rapid change, and tolerance for tighter coupling.
- Weaker-force diagram: [[blog-martin-fowler-the-strong-and-weak-forces-of-architecture]] shows multiple domains inside a vertical where alignment is weaker and change is slower.
- Weak-force diagram: [[blog-martin-fowler-the-strong-and-weak-forces-of-architecture]] shows all of MYOB as a set of verticals where change needs negotiation and very loose coupling.
- Technology-choice example: [[blog-martin-fowler-the-strong-and-weak-forces-of-architecture]] says domain choices can be governed informally, vertical choices need proposal sharing, and whole-organization choices use radar-style direction.
- Integration example: [[blog-martin-fowler-the-strong-and-weak-forces-of-architecture]] says domain-local interfaces can spend less effort on backward compatibility, while whole-organization APIs and events need schemas, contracts, versioning, and deprecation strategy.

## Counterevidence & Qualifications
The model does not excuse careless coupling inside a domain. Fowler says database-level integration still should not be deliberately designed in, even though its damage is more contained when the affected systems sit inside one domain. The source is also a practitioner model grounded in MYOB's structure, not a universal measurement of how many teams or domains create a given force strength.

## What Changed
- Created the concept from Fowler's strong/weak forces model for architecture governance.

## Related Concepts
- [[DefaultTrialRetire]] - local technology-choice limits work best where alignment forces are strong.
- [[TechnologyRadar]] - radar-style guidance fits weaker organization-wide technology-choice alignment.
- [[IntegrationStrategy]] - integration contracts need stricter evolution discipline as alignment weakens.
- [[CapabilityOrientedIntegration]] - capability boundaries help reduce consumer coordination when systems cross organizational distance.
- [[TechnologyStackComplexity]] - unmanaged technology variation becomes more costly as it crosses more teams and verticals.
- [[ScalingCommunication]] - architecture governance needs communication mechanisms matched to organizational scale.

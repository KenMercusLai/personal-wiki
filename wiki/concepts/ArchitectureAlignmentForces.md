---
title: "Architecture Alignment Forces"
type: concept
tags: [architecture, governance, organizational-design]
sources:
  - blog-martin-fowler-the-strong-and-weak-forces-of-architecture
  - blog-andrew-harmel-law-martinfowler-com-scaling-the-practice-of-architecture-conversationally
last_updated: 2026-09-25
knowledge_schema: synthesis-v1
---

## Definition
[[ArchitectureAlignmentForces]] is a governance model that adjusts architecture rules, coupling tolerance, and decision formality according to the strength of social and organizational alignment around the systems being changed.

## Current Synthesis
The source argues that architecture governance fails when it applies one rule across every level of a large organization. Strict central governance can disempower teams and slow ordinary local change, while total local autonomy can leave teams without useful shared constraints. The better question is the blast radius of the decision and the alignment strength among the people affected.

Inside a domain, teams usually share business concepts, domain expertise, related systems, and change priorities. That strong alignment can make negotiation fast enough that some tighter coupling, shared code, informal technology leadership, and cross-team contribution are tolerable. Across a vertical, alignment weakens and the same practices require more monitoring, proposal sharing, or coordination. Across the whole organization, alignment is weak enough that published APIs, events, infrastructure, and shared libraries need loose coupling, self-service boundaries, versioning, backward compatibility, and explicit deprecation strategies.

The [[AdviceProcess]] supplies a decision-process counterpart by requiring consultation with everyone meaningfully affected and relevant experts. As a decision's blast radius grows, its advice scope grows too; this coordination cost can reveal that the proposal should be narrowed or split. An [[ArchitectureAdvisoryForum]] can reduce search cost and spread context, but it does not erase the need to match participation and formality to the affected scope.

## Key Claims
- Architecture governance should vary with organizational scope and decision blast radius.
- Strong domain-level alignment can justify faster local decisions and some tighter coupling.
- Weaker vertical-level alignment requires more formal coordination and more careful shared assets.
- Whole-organization decisions need the strongest encapsulation, versioning, and contract discipline.
- Coupling is not intrinsically bad; its cost depends on who must coordinate changes and how easily they can align.
- Technology choice, shared code, code contribution, and integration patterns all need different rules at domain, vertical, and organization scope.
- Consultation scope is a practical signal of decision blast radius and can encourage smaller decisions.

## Evidence
- Organization model: [[blog-martin-fowler-the-strong-and-weak-forces-of-architecture]] describes [[MYOB]] teams grouped into domains and domains grouped into verticals.
- Strong-force diagram: [[blog-martin-fowler-the-strong-and-weak-forces-of-architecture]] shows a domain containing teams with close alignment, rapid change, and tolerance for tighter coupling.
- Weaker-force diagram: [[blog-martin-fowler-the-strong-and-weak-forces-of-architecture]] shows multiple domains inside a vertical where alignment is weaker and change is slower.
- Weak-force diagram: [[blog-martin-fowler-the-strong-and-weak-forces-of-architecture]] shows all of MYOB as a set of verticals where change needs negotiation and very loose coupling.
- Technology-choice example: [[blog-martin-fowler-the-strong-and-weak-forces-of-architecture]] says domain choices can be governed informally, vertical choices need proposal sharing, and whole-organization choices use radar-style direction.
- Integration example: [[blog-martin-fowler-the-strong-and-weak-forces-of-architecture]] says domain-local interfaces can spend less effort on backward compatibility, while whole-organization APIs and events need schemas, contracts, versioning, and deprecation strategy.
- Advice scope: [[blog-andrew-harmel-law-martinfowler-com-scaling-the-practice-of-architecture-conversationally]] requires decision-takers to consult affected parties and relevant experts, with longer lists indicating larger decisions.
- Decision subdivision: [[blog-andrew-harmel-law-martinfowler-com-scaling-the-practice-of-architecture-conversationally]] says consultation effort often causes a proposal to be reconsidered or split into smaller choices.

## Counterevidence & Qualifications
The model does not excuse careless coupling inside a domain. Fowler says database-level integration still should not be deliberately designed in, even though its damage is more contained when the affected systems sit inside one domain. Both sources are practitioner models, not universal measurements of how many teams, domains, or consultees create a given force strength. Advice scope may also understate blast radius when affected groups are overlooked, lack voice, or cannot predict second-order effects.

## What Changed
- Created the concept from Fowler's strong/weak forces model for architecture governance.
- Added consultation breadth as a decision-sizing signal and a mechanism for subdividing high-blast-radius proposals.

## Related Concepts
- [[DefaultTrialRetire]] - local technology-choice limits work best where alignment forces are strong.
- [[TechnologyRadar]] - radar-style guidance fits weaker organization-wide technology-choice alignment.
- [[IntegrationStrategy]] - integration contracts need stricter evolution discipline as alignment weakens.
- [[CapabilityOrientedIntegration]] - capability boundaries help reduce consumer coordination when systems cross organizational distance.
- [[TechnologyStackComplexity]] - unmanaged technology variation becomes more costly as it crosses more teams and verticals.
- [[ScalingCommunication]] - architecture governance needs communication mechanisms matched to organizational scale.
- [[AdviceProcess]] - operationalizes affected-party and expert consultation for a specific decision.
- [[ArchitectureAdvisoryForum]] - lowers the coordination cost of cross-team architectural conversations.

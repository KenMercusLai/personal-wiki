---
title: "Algorithmic Complexity Vulnerabilities"
type: concept
tags: [security, denial-of-service, algorithms, resource-exhaustion]
sources:
  - denial-of-service-with-a-fistful-of-packets-exploiting-algorithmic-complexity-vulnerabilities
last_updated: 2026-10-03
knowledge_schema: synthesis-v1
---

## Definition
[[AlgorithmicComplexityVulnerabilities]] are security weaknesses in which attacker-controlled input drives an algorithm or resource-management path toward unacceptable worst-case time or space consumption, producing denial of service without requiring malformed input or a large attack volume.

## Current Synthesis
The defining asymmetry is cheap input versus expensive processing. A parser, logger, matcher, or other valid feature can behave acceptably on ordinary data yet amplify a carefully structured input into excessive CPU, memory, disk use, or repeated error handling. This makes average-case benchmarks insufficient for exposed paths and shifts security review toward input-controlled dimensions, worst-case bounds, and failure behavior near resource ceilings.

The talk's three cases show different amplification mechanisms. PDF filter composition alternates expansion and contraction so many decompression workloads can fit under a memory ceiling. VNC connection logging lets each unauthenticated connection increase the work and disk written for later connections, with file-descriptor exhaustion opening a second infinite-loop path. zxcvbn combines long passwords, ambiguous l33t substitutions, and quadratic dictionary matching to extend request time. Defenses therefore need layers: algorithm selection, structural and length limits, connection bounds, CPU and memory budgets, controlled failure, and adversarial test generation.

## Key Claims
- Valid input and intended functionality can still create a denial-of-service vulnerability when worst-case resource use is disproportionate.
- Attackers can compose individually legitimate operations so expansion, contraction, repeated logging, substitution enumeration, or error handling amplifies work.
- Small inputs and unauthenticated requests can be operationally dangerous when cost grows quadratically, combinatorially, or without a terminating recovery path.
- Average-case design and testing are insufficient for attacker-controlled paths; explicit worst-case construction is required.
- Mitigation is layered across algorithm choice, input and structure limits, connection caps, resource budgets, and bounded failure handling.

## Evidence
- Cross-case mechanism: [[denial-of-service-with-a-fistful-of-packets-exploiting-algorithmic-complexity-vulnerabilities]] defines the class through unacceptable worst-case time or space behavior reached with valid input.
- Parser amplification: [[denial-of-service-with-a-fistful-of-packets-exploiting-algorithmic-complexity-vulnerabilities]] describes PDF streams that combine FlateDecode expansion with repeated ASCIIHexDecode contraction and multiply the work across one page.
- Stateful amplification: [[denial-of-service-with-a-fistful-of-packets-exploiting-algorithmic-complexity-vulnerabilities]] attributes quadratic VNC log growth to accumulating unauthenticated connections and a separate infinite loop to file-descriptor exhaustion.
- Combinatorial matching: [[denial-of-service-with-a-fistful-of-packets-exploiting-algorithmic-complexity-vulnerabilities]] reports sharply rising zxcvbn runtime from long passwords containing multiply ambiguous l33t characters.
- Defensive layers: [[denial-of-service-with-a-fistful-of-packets-exploiting-algorithmic-complexity-vulnerabilities]] recommends improved algorithms, input restrictions, connection limits, and processing or memory controls, and presents ACsploit for worst-case generation.

## Counterevidence & Qualifications
The archived source is a presentation summary rather than full exploit code, vendor advisories, patches, benchmarks, or independent reproductions. Its PDF, VNC, and zxcvbn claims are historically and implementation specific; the listed products and language ports should not be assumed currently vulnerable. The PDF case is described as a specification-level risk but does not establish identical behavior across every compliant parser. The zxcvbn timings omit hardware, implementation, version, and measurement method. Finally, saying these vulnerabilities are "not bugs" is rhetorical rather than definitive: intended control flow and valid syntax do not prevent unacceptable amplification from being classified as a design or security defect.

## What Changed
- Created a common model for denial of service caused by worst-case behavior on valid attacker-controlled input.
- Distinguished parser composition, stateful logging, combinatorial substitution, and resource-exhaustion error loops as separate amplification paths.
- Added layered mitigation and adversarial worst-case generation as the corresponding defensive practice.

## Related Concepts
- [[SystemReliability]] - resource ceilings, overload control, and bounded failure determine whether pathological input becomes an outage.
- [[ChaosEngineering]] - tests adverse operating conditions, while complexity testing constructs adversarial inputs for specific computational paths.
- [[EssentialAndAccidentalComplexity]] - addresses difficulty in software design rather than asymptotic resource consumption, despite the shared word complexity.
- [[BackOfEnvelopeEstimation]] - rough cost models can expose dangerous growth before implementation or benchmarking.
- [[PasswordHashing]] - password-processing endpoints also require explicit cost bounds, though zxcvbn estimates strength rather than hashing credentials.

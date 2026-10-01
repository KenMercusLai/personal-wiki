---
title: "Research: Off-Path TCP Attacks"
type: source
tags: [networking, security, tcp, wireless, side-channel]
source_file: "/mnt/ken_personal_wiki/Articles/Rule 11 Reader - Research Off-Path TCP Attacks.md"
---

## Summary
Rule 11 Reader summarizes an off-path [[OffPathTCPInjection]] technique that combines TCP's duplicate-ACK response to an out-of-window sequence number with wireless channel contention. By comparing the timing of two required victim responses around a spoofed TCP segment, an attacker can infer whether a guessed sequence number is inside the receive window, repeat the test, and use the recovered state to attempt stream injection. The example motivates [[ProtocolMetadataSideChannels]]: protocol control behavior can reveal hidden state even when an attacker cannot directly observe the target flow.

## Key Claims
- A TCP receiver answers a segment whose sequence number is outside the current receive window with a duplicate of its latest ACK.
- A shared wireless channel permits only one transmission at a time, so a device that encounters competing traffic backs off before retrying.
- The attacker brackets a spoofed TCP segment with two probes that force victim responses and compares their response times.
- An out-of-window guess triggers a duplicate ACK that contends with the second probe response, while an in-window guess avoids that additional transmission and delay.
- Repeated timing tests can reveal the current TCP receive window sufficiently to support an attempted off-path stream injection.
- Flow-control and error-recovery metadata can become security-relevant observable behavior rather than harmless protocol overhead.

## Key Quotes
> "data exhaust" - the article's term for control and flow information that can reveal otherwise hidden communication state.

> "If the second probe response is slower" - the timing signal used to classify a guessed sequence number as outside the window.

## Connections
- [[OffPathTCPInjection]] - models the article's concrete spoofed-segment, duplicate-ACK, contention, and timing-inference sequence.
- [[ProtocolMetadataSideChannels]] - generalizes the attack as hidden-state inference from externally observable protocol control behavior.
- [[AbstractionLeakage]] - TCP and wireless implementation behavior becomes visible across abstraction boundaries through timing.
- [[CleartextProtocolExposure]] - distinguishes direct plaintext disclosure from an off-path attack that infers state and attempts injection.
- [[QUIC]] - provides a contrasting modern transport whose integrated cryptography changes injection and integrity boundaries while leaving some traffic metadata observable.

## Contradictions
- The source is a short secondary summary: it does not identify the paper's authors or venue, define the wireless protocol and attacker prerequisites precisely, report measurements or success rates, or discuss implementation-specific ACK rate limiting and mitigations.
- A timing distinction does not by itself establish reliable end-to-end injection; an attacker may also need the connection tuple, acceptable acknowledgment state, repeatable signal separation, and an application action that tolerates injected bytes.
- The conclusion that secure communication always requires “encryption” is too broad. Authenticated integrity is the control that rejects forged content; confidentiality is related but distinct, and encrypted transports can still expose timing, length, direction, and loss behavior.
- The supplied Markdown contains no effective image references, so no visual assets or manifest were required.

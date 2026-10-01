---
title: "Off-Path TCP Injection"
type: concept
tags: [networking, security, tcp, wireless, injection]
sources:
  - rule-11-reader-research-off-path-tcp-attacks
last_updated: 2026-10-02
knowledge_schema: synthesis-v1
---

## Definition
[[OffPathTCPInjection]] is an attempt to insert attacker-chosen data into an existing TCP connection without directly observing that connection, by inferring enough hidden connection state to forge an acceptable segment.

## Current Synthesis
The source describes a timing oracle built by composing two ordinary behaviors. TCP sends a duplicate ACK when a received sequence number falls outside the current receive window. A wireless station sharing a channel must defer when another transmission occupies that channel. An attacker sends a response-provoking probe, a spoofed TCP segment containing a guessed sequence number, and then a second probe. If the guess is outside the window, the victim's duplicate ACK competes with the second response and makes that response slower; a similar response time indicates that the guess was within the window.

Repeating the classification can locate the receive window and reduce the uncertainty blocking a forged segment. The attack is therefore not based on reading the target traffic directly: it converts victim-generated control traffic into an externally measurable wireless delay. The source does not, however, specify all state required for successful injection or demonstrate that the oracle remains distinguishable under real congestion, jitter, ACK rate limiting, or modern authenticated transports.

## Key Claims
- An off-path attacker needs a substitute for direct packet observation to recover TCP connection state.
- Out-of-window TCP segments can elicit duplicate ACKs whose transmission becomes an observable side effect.
- Shared-medium wireless backoff can convert that extra transmission into a response-time difference.
- Bracketed probes let the attacker compare a baseline response with a response exposed to the guessed segment's side effect.
- Repeated in-window versus out-of-window classifications can narrow the receive-window search and support attempted injection.
- Cryptographic authentication can reject forged stream content even when network timing still leaks metadata.

## Evidence
- TCP oracle: [[rule-11-reader-research-off-path-tcp-attacks]] says an out-of-window sequence number causes the receiver to send a duplicate of its latest ACK.
- Wireless amplifier: [[rule-11-reader-research-off-path-tcp-attacks]] says channel contention forces the victim to back off when its duplicate ACK collides with the second probe exchange.
- Attack sequence: [[rule-11-reader-research-off-path-tcp-attacks]] orders two response-provoking probes around a source-spoofed TCP segment and classifies the guess from their relative timing.
- Intended result: [[rule-11-reader-research-off-path-tcp-attacks]] says repetition can reveal the current receive window and enable information injection into the TCP stream.

## Counterevidence & Qualifications
The evidence is one brief secondary account without a paper citation, experimental setup, measurements, success distribution, affected implementations, or mitigation analysis. The source compresses “recover the receive window” and “inject information” into one transition even though a real attack may also require a known connection tuple, acceptable acknowledgment values, stable timing separation, source spoofing, and application-level tolerance. Network jitter, unrelated contention, duplicate-ACK throttling, challenge-ACK behavior, and implementation changes may weaken the oracle. Encryption is not by itself the precise boundary: authenticated transport integrity is what rejects forged content, while timing and packet-shape leakage can remain.

## What Changed
- Established the attack as a cross-layer timing oracle joining TCP duplicate ACKs to wireless contention and backoff.
- Separated receive-window inference from the additional prerequisites needed for successful stream injection.
- Qualified the source's broad encryption conclusion by distinguishing confidentiality, integrity, and residual metadata leakage.

## Related Concepts
- [[ProtocolMetadataSideChannels]] - supplies the general hidden-state inference mechanism used by this attack.
- [[AbstractionLeakage]] - explains why behavior below a transport abstraction can become relevant to security.
- [[CleartextProtocolExposure]] - concerns directly observable plaintext rather than inferred state and forged segments.
- [[QUIC]] - integrates cryptographic protection into transport while retaining observable traffic timing and shape.
- [[DefensivePortTriage]] - identifies reachable transport endpoints but cannot by itself establish susceptibility to this off-path oracle.

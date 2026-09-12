---
title: "HTTP 402 Payment Required"
type: concept
tags: [http, payments, web]
sources:
  - 402-payment-required-david-humphrey-medium
last_updated: 2026-09-12
knowledge_schema: synthesis-v1
---

## Definition
[[HTTP402PaymentRequired]] is the reserved HTTP status code that Humphrey proposes using as a browser-readable signal for paid access.

## Current Synthesis
The source treats HTTP status codes as a shared vocabulary for browser behavior: users already encounter success, not-found, unauthorized, forbidden, and method-not-allowed responses. Humphrey argues that the reserved 402 code could become the missing payment response if sites return enough metadata for browsers to present transaction options. In that model, a 402 would not merely block access; it would invite a browser-mediated purchase, rental, or subscription through the user's configured payment provider.

## Key Claims
- HTTP status codes can shape browser behavior because clients already interpret success and failure responses.
- 402's reserved status makes it a plausible semantic hook for future web-payment infrastructure.
- Payment metadata alongside a 402 response could let browsers turn denied access into a transaction prompt.
- The proposal depends on browser support, site conventions, payment-provider integration, and user trust.

## Evidence
- Status-code framing: [[402-payment-required-david-humphrey-medium]] contrasts 200, 404, 401, 403, and 405 with the reserved 402.
- Future-use claim: [[402-payment-required-david-humphrey-medium]] notes that the status code is reserved for future use.
- Movie-rental example: [[402-payment-required-david-humphrey-medium]] imagines a shared movie URL returning 402 and offering a $1.99 rental.
- Wireframe evidence: [[402-payment-required-david-humphrey-medium]] includes a mocked "Payment Required" browser prompt with provider options.

## Counterevidence & Qualifications
The article is speculative and publication-date bound to 2015. It does not document adoption, specify a complete response schema, or address all security, privacy, and interoperability requirements of a real payment standard.

## What Changed
- Created the HTTP 402 Payment Required concept as the protocol-specific node for the article.

## Related Concepts
- [[HTTP]] - 402 belongs to HTTP's response-code vocabulary.
- [[BrowserPaymentBroker]] - the browser broker would act on 402 responses.
- [[WebAdEconomics]] - 402 is proposed as part of explicit web monetization.
- [[AdBlocking]] - the proposal responds to ad blocking's pressure on ad revenue.

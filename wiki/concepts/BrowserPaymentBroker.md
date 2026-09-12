---
title: "Browser Payment Broker"
type: concept
tags: [web, payments, browsers]
sources:
  - 402-payment-required-david-humphrey-medium
last_updated: 2026-09-12
knowledge_schema: synthesis-v1
---

## Definition
[[BrowserPaymentBroker]] is Humphrey's proposed role for the web browser as a trusted user agent that can mediate payments between users, payment providers, and sites.

## Current Synthesis
The source argues that browsers are already trusted with passwords, history, and constant cross-site presence, yet do little to help users purchase content and services outside bespoke checkout forms and paywalls. A browser payment broker would let users configure providers such as Visa, PayPal, or [[Stripe]], then respond to a site's [[HTTP402PaymentRequired]] metadata by offering clear options to buy, rent, or subscribe. The accompanying wireframes show this as a browser-level payment settings panel, a payment-required response page, and a prompt with provider buttons.

## Key Claims
- Browsers can be more than renderers because they already act on behalf of users across every site.
- User trust in the browser may be higher than trust in an unfamiliar site's custom payment form.
- Configured payment providers could make web purchases feel as routine as browser search defaults or app-store purchases.
- The browser could reduce implementation burden for small publishers by handling payment options, taxes, currencies, and regional complexity.
- Browser-mediated payment should be opt-in and coexist with free content rather than force every site behind a paywall.

## Evidence
- Trust argument: [[402-payment-required-david-humphrey-medium]] says users trust browsers with passwords, history, and every site visit.
- Provider configuration: [[402-payment-required-david-humphrey-medium]] imagines browser settings for Visa, PayPal, [[Stripe]], or another processor.
- Wireframe evidence: [[402-payment-required-david-humphrey-medium]] includes browser UI sketches for a 402 page, payment-provider settings, and a payment prompt.
- Use-case range: [[402-payment-required-david-humphrey-medium]] discusses purchases, streamed rentals, blog subscriptions, regional taxes, and currency exchange.

## Counterevidence & Qualifications
The source offers a product and standards imagination rather than an implementation spec. It does not resolve payment-provider competition, browser-vendor power, fraud prevention, privacy of purchase history, or publisher revenue-share terms.

## What Changed
- Created the browser payment broker concept from Humphrey's HTTP 402 proposal and wireframes.

## Related Concepts
- [[HTTP402PaymentRequired]] - supplies the status-code signal that the browser would interpret.
- [[WebAdEconomics]] - browser payment brokerage is meant to create explicit alternatives to advertising.
- [[AdBlocking]] - the proposal responds to the ad-blocking controversy.
- [[HTTP]] - HTTP response semantics are the protocol setting for the proposal.

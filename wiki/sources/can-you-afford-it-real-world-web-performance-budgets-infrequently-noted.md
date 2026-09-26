---
title: "Can You Afford It?: Real-world Web Performance Budgets"
type: source
tags: [web-performance, pwa, javascript, performance-budget]
date: 2017-10-22
source_file: "/mnt/ken_personal_wiki/Articles/Can You Afford It-- Real-world Web Performance Budgets – Infrequently Noted.md"
---

## Summary
[[AlexRussell]] argues that [[PerformanceBudget]] discipline is essential for building web products that work on real devices and networks rather than only on high-end developer hardware. The article proposes a global baseline of a roughly $200 Android phone on a 400ms RTT, 400Kbps connection, then works backward from a five-second first-load [[TimeToInteractive]] target to a 130-170KB critical-path transfer budget. Its strongest warning is that JavaScript-heavy SPA and PWA choices can silently spend that budget before teams have validated whether the product reaches its intended audience.

## Key Claims
- [[PerformanceBudget]]s should be set early, measured against a representative device and network, and enforced through tooling and CI instead of treated as late-stage tuning.
- [[TimeToInteractive]] is the central user-facing metric because a page that has painted but cannot respond to input has not actually become usable.
- JavaScript is more expensive than images of similar transfer size because it must be fetched, decompressed, parsed, compiled, and executed, often delaying the main thread and the [[CriticalRenderingPath]].
- The proposed default baseline is a roughly $200 Android device on a 400ms RTT, 400Kbps slow-3G connection, reflecting affordability and global median-device constraints rather than developer environments.
- Working backward from a five-second first load leaves about 170KB for critical-path resources on low-JS sites and about 130KB for JavaScript-heavy sites after accounting for parse and evaluation time.
- Subsequent loads should target two seconds or less by using Service Workers and offline-first architecture to avoid refetching the application shell.
- Performance crises can damage product launches, business learning, executive trust, and developer morale when stack choices make the product unusable for the intended market.

## Key Quotes
> "Living on a budget means constantly asking yourself 'can I really afford this?'" - on treating each framework, router, data layer, and critical-path resource as an explicit budget tradeoff.

> "JavaScript is the single most expensive part of any page" - on why byte budgets need to distinguish script from images or other resources.

## Connections
- [[AlexRussell]] - author and practitioner voice behind the performance-budget argument.
- [[PerformanceBudget]] - central operating discipline for constraining page-load work to real-world affordability.
- [[WebPerformanceOptimization]] - broader practice that the article makes more objective through budgets, baselines, RUM, and CI enforcement.
- [[CriticalRenderingPath]] - article explains how script loading and execution delay critical user interactivity.
- [[TimeToInteractive]] - metric used to define whether the page is ready for real user input.
- [[HTTP2]] - appears as one protocol feature that can support PRPL-style route-aware loading and smaller critical paths.
- [[NextJS]] - named as one recommended starting stack when paired with a lighter runtime such as Preact.

## Contradictions
- No direct contradiction found. The source sharpens the existing [[WebPerformanceOptimization]] and [[CriticalRenderingPath]] pages by making JavaScript cost, device affordability, and explicit transfer budgets more central than the prior Baqend ecommerce case study.

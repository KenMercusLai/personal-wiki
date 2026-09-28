---
title: "For E-Commerce Data Scientists: Lessons Learned Scraping 100 Billion Product Pages"
type: source
tags: [web-scraping, ecommerce, data-quality, distributed-systems]
date: 2018-07-02
source_file: /mnt/ken_personal_wiki/Articles/For E-Commerce Data Scientists- Lessons Learned Scraping 100 Billion Products Pages.md
---

## Summary
[[Scrapinghub]] presents [[LargeScaleWebScraping]] as a joint throughput-and-quality problem rather than a matter of running more requests. Drawing on its claimed experience scraping more than 100 billion product pages, the company emphasizes resilient extraction across changing storefronts, separation of discovery from extraction, resource-efficient crawling, managed anti-bot operations, and automated quality monitoring.

## Key Claims
- Large-scale product scraping is constrained by both speed and data quality: a system must finish within its collection window without silently degrading the feed.
- Changing layouts, regional variants, A/B tests, malformed markup, misleading HTTP behavior, broken JavaScript, and awkward Ajax usage create continuous crawler-maintenance work.
- One configurable product extractor that handles multiple layouts can be easier to maintain than separate spiders for every variation, even if the unified spider is internally complex.
- Product discovery and product extraction should be separate stages connected by a crawl frontier, because category traversal produces URLs faster than product pages can usually be processed.
- Throughput depends on minimizing work per item: use shelf-page data when sufficient, avoid unnecessary images, and reserve JavaScript-rendering browsers for cases that cannot be handled more cheaply.
- Proxy rotation, throttling, sessions, and blacklisting are necessary operational controls, but sophisticated anti-bot systems may still require site-specific investigation rather than blanket browser rendering.
- Automated QA should detect schema or value violations, inconsistent supposedly fixed product attributes, abnormal record-volume changes, spider errors, and target-site structural changes.

## Key Quotes
> "At its core, these challenges can be boiled down to two things: speed and data quality." - on the coupled objectives of scraping at scale.

> "Separate Product Discovery From Product Extraction" - on the central pipeline boundary.

> "it is impossible to manually verify that all your data is clean and intact" - on the need for automated QA at high volume.

## Connections
- [[Scrapinghub]] - vendor and author reporting the large-scale operating lessons.
- [[LargeScaleWebScraping]] - combined architecture, throughput, maintenance, anti-bot, and quality discipline described by the article.
- [[Scrapy]] - Scrapinghub's open-source crawling framework and part of the article's technical context.
- [[Frontera]] - crawl-frontier example for decoupling product discovery from extraction.
- [[Crawlera]] - managed downloader presented as an alternative to operating proxy infrastructure internally.
- [[WebScrapingProxyPool]] - proxy lifecycle broadened here to rotation, throttling, sessions, blacklisting, and managed services.
- [[AIGuidedWebScraping]] - adjacent extraction approach whose browser-heavy execution inherits the article's throughput and anti-bot constraints.

## Contradictions
- Qualifies browser-first scraping approaches by arguing that JavaScript rendering should be a last resort when throughput matters, while recognizing that Ajax-heavy sites can make rendering unavoidable.
- Qualifies simple public-proxy-pool workflows: at large request volumes, proxy quality, rotation, session state, throttling, and blacklisting become a dedicated operating system that the author recommends outsourcing.
- The staffing figures, failure rates, serial-request threshold, page-bucket heuristic, volume claims, and vendor recommendations are first-party historical examples rather than independently verified universal benchmarks.

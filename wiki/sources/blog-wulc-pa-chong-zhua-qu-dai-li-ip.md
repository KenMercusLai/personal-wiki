---
title: "爬虫抓取代理 IP"
type: source
tags: [web-scraping, proxy, python, redis]
date: 2016-07-05
source_file: /mnt/ken_personal_wiki/Articles/Blog - wulc - 爬虫抓取代理 IP.md
---

## Summary
[[Wulc]] explains a practical [[WebScrapingProxyPool]] workflow for hiding a scraper's real IP address by collecting public proxy addresses, storing them in [[Redis]], and validating them against the target site before use. The article uses Python `requests` and BeautifulSoup examples against Xici Daili, then adds operational cautions about removing failed proxies and slowing proxy-source scraping to avoid blocks and excess load.

## Key Claims
- Public proxy sites can be scraped by parsing table rows for IP and port pairs, but one-page collection is insufficient for a usable pool.
- Proxy candidates should be persisted outside process memory because scraper programs may fail, exit, or need to reuse proxies across runs.
- [[Redis]] sets can store proxy strings and return random candidates for later validation.
- A proxy should be tested against the actual target site before use because public proxies fail or get blocked quickly.
- Invalid proxies should be removed from storage so future requests do not keep retrying dead entries.
- Proxy-source scraping should be rate-limited; the article suggests sleeping roughly two minutes after each page to reduce block risk and avoid overloading free proxy sites.

## Key Quotes
> "尝试通过代理 ip 是否能连到我们需要访问的目标网站" - on validating a proxy against the target before use.

> "采用一个可持续爬取的策略非常有必要" - on slowing proxy-source scraping.

## Connections
- [[Wulc]] - author of the practical scraping note.
- [[WebScrapingProxyPool]] - central workflow of collection, persistence, random selection, validation, eviction, and crawl pacing.
- [[Redis]] - persistent set storage used for reusable proxy candidates.
- [[Python]] - implementation context through `requests`, BeautifulSoup, and Redis client code.

## Contradictions
- No direct contradictions found. The source adds a scraper-operations pattern rather than changing existing Redis, Python, or web-automation claims.

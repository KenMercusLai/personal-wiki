---
title: "Image Stacks and iPhone Racks - Building an Internet Scale Meme Search Engine"
type: source
tags: [meme-search, ocr, ios, elasticsearch, infrastructure]
date: 2023-01-08
source_file: "/mnt/ken_personal_wiki/Articles/Image Stacks and iPhone Racks - Building an Internet Scale Meme Search Engine.md"
---

## Summary
The pseudonymous author IAmMandatory describes building [[FindThatMeme]], a search engine that extracts text from varied meme images and sampled video frames, stores canonical records in [[PostgreSQL]], and serves full-text retrieval through a rebuildable Elasticsearch index. The central engineering move was to turn Apple's accurate on-device Vision OCR into an HTTP service and then a low-cost cluster of used iPhones behind Raspberry Pi and NGINX load balancing. The account connects [[VisualTextIndexing]], [[CostConstrainedInfrastructure]], and [[RebuildableDerivedIndex]] while remaining a first-person 2023 architecture report rather than an independently reproduced benchmark.

## Key Claims
- Tesseract handled a meme with regular high-contrast type but badly misread a remixed game meme whose captions, label overlays, font sizes, colors, and image content varied.

![A meme with large regular black text that Tesseract transcribed accurately](../../wiki-assets/image-stacks-and-iphone-racks-building-an-internet-scale-meme-search-engine/easy-tesseract-meme.png)

![A remixed Escape from Tarkov meme whose mixed fonts, overlays, and game labels defeated Tesseract](../../wiki-assets/image-stacks-and-iphone-racks-building-an-internet-scale-meme-search-engine/remixed-meme-ocr-challenge.png)

- iOS could select and correctly copy the deliberately distorted words “Levelers critics” from an old reCAPTCHA, motivating automated use of the Vision framework for harder meme text.

![iOS text selection highlighting the intentionally warped words in an old reCAPTCHA image](../../wiki-assets/image-stacks-and-iphone-racks-building-an-internet-scale-meme-search-engine/ios-selecting-warped-captcha.png)

![An iPhone Notes screen showing the correctly copied CAPTCHA text Levelers critics](../../wiki-assets/image-stacks-and-iphone-racks-building-an-internet-scale-meme-search-engine/ios-captcha-recognition-result.png)

- A Swift app exposed Vision OCR through GCDWebServer; the pictured prototype reports an HTTP endpoint, 2,833 images processed, 405 MB memory use, and a last health check.

![An iPhone running a basic Vision OCR HTTP server with processing and memory statistics](../../wiki-assets/image-stacks-and-iphone-racks-building-an-internet-scale-meme-search-engine/iphone-vision-ocr-server.png)

- The phone app leaked memory and typically crashed after 20,000–40,000 images, so iOS Guided Access was used as an automatic restart mechanism that also recovered from corrupt-image crashes.
- [[PostgreSQL]] remained the canonical store for text and metadata; PGSync mirrored selected columns through Redis into a single-node Elasticsearch cluster that could be deleted and rebuilt after index loss.

![Diagram with PostgreSQL as the source of truth, PGSync and Redis feeding a single-node Elasticsearch cluster, and the FindThatMeme API server](../../wiki-assets/image-stacks-and-iphone-racks-building-an-internet-scale-meme-search-engine/postgres-pgsync-elasticsearch-architecture.png)

- Generated-data testing and the running service reportedly supported sub-second text search across about 17 million memes on a shared six-core, 16 GB RAM Linode instance; the article supplies no benchmark protocol or latency distribution.
- Video memes were converted into ten evenly spaced screenshots with ffmpeg, then each frame was sent to the same phone OCR service; this made each video roughly ten times the image-OCR work.
- The author scaled OCR with cosmetically damaged, carrier-locked, or IMEI-blocklisted older iPhones whose compute and Wi-Fi remained usable, placing them behind an NGINX load balancer on a Raspberry Pi.

![A physical OCR cluster of five wired iPhones stacked above a Raspberry Pi and power adapters](../../wiki-assets/image-stacks-and-iphone-racks-building-an-internet-scale-meme-search-engine/iphone-ocr-cluster.jpg)

- A pictured second-generation iPhone SE sold for $39.99; at the article's quoted Google Cloud Vision rate of $1.50 per thousand images, its purchase price would equal about 26,660 cloud OCR requests before electricity, cooling, maintenance, networking, development, depreciation, or utilization were counted.

![A sold listing for a carrier-locked second-generation iPhone SE priced at 39 dollars and 99 cents](../../wiki-assets/image-stacks-and-iphone-racks-building-an-internet-scale-meme-search-engine/used-iphone-se-listing.png)

- The final diagram separates scraping and ingestion, OCR, object storage, canonical and search databases, and a search API/client, making the low-cost hardware choice part of a larger recoverable pipeline.

![Final architecture linking meme sites, a scraping ingestion server, an iPhone OCR farm, Elasticsearch and PostgreSQL databases, object storage, and the meme search service](../../wiki-assets/image-stacks-and-iphone-racks-building-an-internet-scale-meme-search-engine/final-meme-search-architecture.png)

## Key Quotes
> “Finally it seemed there was a scalable OCR solution” - on discovering that Apple's Vision framework exposed the recognition capability for automation.

> “I could blow ElasticSearch away” - on treating the search store as a derivative that PGSync could reconstruct from PostgreSQL.

## Connections
- [[FindThatMeme]] - the meme retrieval project and architecture described by the author.
- [[VisualTextIndexing]] - images and sampled video frames become searchable text through OCR.
- [[CostConstrainedInfrastructure]] - cheap impaired phones, a Raspberry Pi, single-node search, and recoverability trade reliability for sustainable side-project cost.
- [[RebuildableDerivedIndex]] - PostgreSQL is authoritative while Elasticsearch is disposable and reconstructable.
- [[PostgreSQL]] - canonical store for meme text, context, and source metadata.
- [[SystemReliability]] - restarts, load balancing, and rebuild paths contain faults without claiming high availability.
- [[Apple]] - its iOS Vision framework and Guided Access feature make the phone-based OCR service possible.

## Contradictions
- The performance, OCR-quality, crash-frequency, corpus-size, and cost claims are self-reported point observations without source data, reproducible benchmarks, comparison methodology, or current verification.
- The $39.99 device-versus-cloud comparison is a break-even illustration, not total cost of ownership: it omits labor, power, cooling, accessories, failed devices, throughput, queueing, utilization, and service-level differences.
- A single Elasticsearch node and automatic app restart reduce cost and recovery effort but do not provide uninterrupted service, eliminate data loss windows, or substitute for measured reliability.
- Ten evenly spaced frames can miss brief captions, scene changes, and audio-only meaning, so the video pipeline indexes a sample rather than the complete semantic content.

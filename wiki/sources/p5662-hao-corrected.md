---
title: "LiquidCache: Efficient Pushdown Caching for Cloud-Native Data Analytics"
type: source
tags: [database-systems, cloud-analytics, caching, parquet, filter-pushdown]
date: 2025-08-01
source_file: "/mnt/ken_personal_wiki/Articles/p5662-hao-corrected.md"
---

## Summary
[[XiangpengHao]], [[AndrewLamb]], [[YiboWu]], [[AndreaArpaciDusseau]], and [[RemziArpaciDusseau]] present [[LiquidCache]], a [[DisaggregatedCaching|disaggregated cache]] that applies [[FilterPushdown]] before returning analytical data to compute nodes. Its central observation is that Parquet decoding and decompression, rather than predicate evaluation, dominate cache-server CPU time, so the system progressively transcodes cached [[ApacheParquet]] data into an ephemeral, filter-aware representation while preserving Parquet at the durable storage boundary. ClickBench and TPC-H results report Arrow-like latency and CPU use with Parquet-like space use, subject to selective-workload, prototype, and first-party evaluation limits.

## Key Claims
- Parquet filter pushdown can move a network bottleneck into limited cache-server CPU: in ClickBench Q22, decoding and decompression account for more than 90% of the baseline time.

![ClickBench Q22 CPU-time breakdown showing Parquet dominated by decoding and decompression while LiquidCache sharply reduces both](../../wiki-assets/p5662-hao-corrected/q22-decoding-time-breakdown.png)

- LiquidCache places an independently scalable cache close to compute nodes and uses Arrow Flight to return filtered batches, while object storage remains the durable Parquet source.

![LiquidCache positioned between a remote object store and nearby shared compute nodes](../../wiki-assets/p5662-hao-corrected/liquidcache-architecture.png)

- A cold query obtains schema, splits scan work from later operators, downloads and caches Parquet bytes if necessary, returns filtered output, and schedules Arrow-to-Liquid transcoding outside the critical path.

![LiquidCache query lifecycle from plan splitting and object-store download through filtering, network return, and background transcoding](../../wiki-assets/p5662-hao-corrected/query-lifecycle.png)

- The Liquid representation cascades independently decodable encodings: strings use dictionary encoding, bit-packed keys, and FSST-compressed values; integers use frame-of-reference plus FastLanes bit packing; floating-point values use ALP.

![Liquid string encoding pipeline from Arrow through dictionary keys, bit packing, and FSST-compressed dictionary values](../../wiki-assets/p5662-hao-corrected/string-encoding-pipeline.png)

- Element-level selective decoding avoids Parquet's page-granularity penalty, and late filter materialization uses earlier predicates to reduce the rows decoded and tested by later predicates.

![Parquet page-level decoding compared with LiquidCache element-selective decoding under a three-of-eight row mask](../../wiki-assets/p5662-hao-corrected/selective-decoding-comparison.png)

![Eager Parquet filtering compared with LiquidCache late materialization that uses the first filter mask to reduce later decoding](../../wiki-assets/p5662-hao-corrected/late-filter-materialization.png)

- Encoding-aware predicates can compare encoded dictionary values directly, while incompatible operations decode only as far as necessary; this co-design requires the decoder and embedded query engine to share filter knowledge.
- On the selected ClickBench queries, LiquidCache stays below 0.5 seconds, approaches Arrow-pushdown CPU time, uses memory near compressed Parquet, and sends orders of magnitude less data than a Parquet file server on highly selective queries.

![ClickBench latency, network traffic, cache CPU time, and cache memory for LiquidCache, Arrow pushdown, Parquet pushdown, and a Parquet file server](../../wiki-assets/p5662-hao-corrected/clickbench-system-comparison.png)

- With an 8 GB cache on TPC-H SF100, Arrow is fastest when the scan fits but degrades sharply when it does not; Liquid reports the best latency on the evaluated larger-than-cache inputs.

![TPC-H SF100 query latency with an eight-gigabyte cache comparing Liquid, Parquet, ORC, and Arrow across scan sizes](../../wiki-assets/p5662-hao-corrected/tpch-cache-latency.png)

- Q22 profiling reports about 27 seconds of cache CPU time for Parquet pushdown versus 2.7 seconds for LiquidCache; Arrow reaches similar total time but spends more of it stalled on a representation four times larger.

![ClickBench Q22 filter evaluation, decoding, and memory-stall time for Parquet pushdown, LiquidCache, Arrow pushdown, and a theoretical optimum](../../wiki-assets/p5662-hao-corrected/q22-cpu-breakdown.png)

- For ClickBench's largest string column, full Liquid occupies 2.0 GB versus 2.4 GB for Parquet and 12.9 GB for Arrow; the chart also shows faster Liquid decoding than Parquet and cheap bit packing relative to dictionary construction.

![ClickBench Title-column size and bidirectional transcoding time across Parquet, Arrow, dictionary, bit-packed, and fully encoded Liquid representations](../../wiki-assets/p5662-hao-corrected/encoding-size-transcoding-cost.png)

- Background transcoding progressively cuts Q21 cache memory by about fourfold with roughly 20% higher latency than Arrow pushdown and is largely hidden by storage I/O except when input arrives at memory speed.

![LiquidCache background transcoding lowers Q21 cache memory about fourfold while query latency remains near Arrow pushdown](../../wiki-assets/p5662-hao-corrected/background-transcoding.png)

![Cold- and warm-run latency showing background transcoding hidden by remote and local storage I/O but exposed by memory-speed input](../../wiki-assets/p5662-hao-corrected/cold-run-transcoding-overlap.png)

- The ablation attributes gains to multiple mechanisms rather than faster decoding alone; selective decoding helps projection-heavy selective queries, late materialization helps multi-filter queries, and compatible encoded evaluation can remove most remaining decode work.

![ClickBench ablation across full decoding, selective decoding, late materialization, and encoded predicate evaluation](../../wiki-assets/p5662-hao-corrected/decoding-optimization-ablation.png)

## Key Quotes
> "data decoding, not filter evaluation, is the primary bottleneck" - the paper's central diagnosis.

> "the cache server is the only producer and consumer of Liquid data" - why the ephemeral representation can evolve without a durable interoperability contract.

## Connections
- [[LiquidCache]] - proposed pushdown-enabled cache and ephemeral data representation.
- [[FilterPushdown]] - query optimization co-designed with selective and encoding-aware decoding.
- [[DisaggregatedCaching]] - system architecture separating cache capacity from compute nodes.
- [[ApacheParquet]] - durable interoperable format and transcoding input whose decoding cost motivates the design.
- [[ApacheDataFusion]] - embedded query engine and implementation substrate for the prototype.
- [[ColumnarStorageTradeoffs]] - compression, random access, decoding cost, and compatibility tradeoffs exposed by the evaluation.

## Contradictions
- Pushdown is not universally beneficial: ClickBench Q27 has 99% selectivity and a 31% compression ratio, causing LiquidCache to run about three times slower than the Parquet file server because it sends filtered data uncompressed.
- The prototype always pushes supported filters, projections, and simple aggregations; cost-based pushdown, automatic local-mode placement, joins, better cache replacement, Substrait interoperability, and non-selective-filter adaptation remain future work.
- The headline gains come from a first-party prototype evaluated on selected ClickBench filters and scan-heavy TPC-H queries on one CloudLab hardware setup. The paper does not establish multi-tenant behavior, failure recovery, TLS cost, production tail latency, transcode-energy cost, or independent reproducibility.
- LiquidCache's best results generally assume fully transcoded warm data. Cold-run overhead is hidden when I/O is slower than transcoding, but becomes visible for memory-speed input.
- Comparison quality depends on implementation maturity: the paper itself notes that Parquet beats similarly compressed ORC partly because DataFusion and DuckDB integrate with Parquet more deeply.

## Image Notes
All 13 effective local image references were opened and retained at their semantic positions. They cover the architecture and query flow, encoding and decoding mechanisms, four-way system comparisons, TPC-H behavior, transcoding costs, cold-run overlap, and the optimization ablation; no referenced figure was decorative or redundant.

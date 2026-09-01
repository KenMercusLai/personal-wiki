---
title: "Structured CLI output"
description: "为命令行表格和机器可读格式建立稳定、可过滤、可排序、可管道处理的输出方式。"
type: "concept"
updated: "2026-09-01"
source_keys: ["jeff-dickey-twelve-factor-cli-apps"]
---

来源：[12 Factor CLI Apps]({{< relref "/wiki/sources/jeff-dickey-twelve-factor-cli-apps.md" >}})

Structured CLI output 指 CLI 在展示集合数据时，同时照顾人类扫描和机器处理。Jeff Dickey 认为，表格是 CLI 的常见输出形式，但表格不应使用边框，因为边框会增加噪音，也会让 `wc`、`grep` 等工具更难按行处理数据。

在这篇来源中，良好的表格输出应保持每行对应一条数据。默认列数要适应屏幕宽度，长内容应可截断，也应允许用户通过 `--no-truncate` 关闭截断；列头默认显示，但可通过 `--no-headers` 隐藏；用户还应能通过 `--columns` 选择列、通过 `--filter` 过滤列值、通过 `--sort` 排序，并支持反向和多列排序。

来源同时强调 CSV 和 JSON。JSON 适合表达结构化对象并交给 `jq` 等工具处理，CSV 则更适合 `cut`、`awk` 等传统文本工具。这个概念的核心是，CLI 表格不是孤立展示，而是 shell 数据流中的一个可组合节点。

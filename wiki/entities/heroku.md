---
title: "Heroku"
description: "Cloud platform company whose Twelve-Factor App methodology, CLI examples, and oclif framework provide the background for 12 Factor CLI Apps."
type: "entity"
updated: "2026-09-01"
source_keys: ["jeff-dickey-twelve-factor-cli-apps"]
entity_kind: "company"
---

来源：[12 Factor CLI Apps]({{< relref "/wiki/sources/jeff-dickey-twelve-factor-cli-apps.md" >}})

Heroku 是这篇来源中的主要组织背景。Jeff Dickey 说明，Heroku 曾提出 Twelve-Factor App 方法论，文章则借用这种“因素”框架来整理 CLI 应用的设计原则。

来源还多次使用 Heroku CLI 作为例子。`heroku fork` 的参数设计展示了位置参数可能带来的歧义，改用 `--from` 和 `--to` 让源应用和目标应用更清楚；`heroku run` 则展示了 CLI 需要用 `--` 停止自身解析，以便把后续参数传给下游进程。

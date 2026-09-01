---
title: "oclif"
description: "A Node CLI framework mentioned by Jeff Dickey as a way to provide help, documentation, autocomplete, plugins, and low startup overhead."
type: "entity"
updated: "2026-09-01"
source_keys: ["jeff-dickey-twelve-factor-cli-apps"]
entity_kind: "software"
---

来源：[12 Factor CLI Apps]({{< relref "/wiki/sources/jeff-dickey-twelve-factor-cli-apps.md" >}})

oclif 是这篇来源中提到的 CLI framework。Jeff Dickey 介绍它是用于构建 Node CLI 的框架，并称它被设计为符合文章列出的 CLI 设计原则。

在来源中，oclif 主要承担示例角色：它可以生成在线文档、命令内帮助和 autocomplete，框架层也适合统一解决 man page、插件系统和描述字段 lint 等问题。作者还提到 oclif 通过只加载即将执行的命令来降低启动开销，使拥有许多命令的 CLI 仍能维持较低基础成本。

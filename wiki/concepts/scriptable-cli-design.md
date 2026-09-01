---
title: "Scriptable CLI design"
description: "设计可以被 shell 管道、脚本和下游进程可靠组合的命令行工具。"
type: "concept"
updated: "2026-09-01"
source_keys: ["jeff-dickey-twelve-factor-cli-apps"]
---

来源：[12 Factor CLI Apps]({{< relref "/wiki/sources/jeff-dickey-twelve-factor-cli-apps.md" >}})

Scriptable CLI design 指 CLI 在面向交互用户的同时，也必须能被脚本、管道和其他进程稳定调用。Jeff Dickey 的文章多次把自动化能力作为 CLI 设计边界：提示可以出现，但不能成为必需；装饰性输出可以存在，但不能污染重定向结果；下游命令参数可以传递，但需要明确停止当前解析的位置。

来源中的关键做法包括：用 flags 覆盖交互式 prompt，让自动化脚本无需人工输入；在 stdin 不是 tty 时避免强制询问；用 `--` 表示 CLI 自身停止解析，后续参数原样交给被调用进程；把机器可消费的输出保留在 stdout，把消息、进度、警告和错误放在 stderr。

这个概念强调，CLI 的强大来自可组合性。一个适合脚本化的工具不要求所有用户都写脚本，但它不能把交互式便利建立在破坏 shell 约定、文件重定向或批处理可预测性的基础上。

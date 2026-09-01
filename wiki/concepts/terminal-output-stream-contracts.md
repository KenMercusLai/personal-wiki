---
title: "Terminal output stream contracts"
description: "在 CLI 中区分 stdout、stderr 和 tty 能力，保证人类消息与机器输出不会互相污染。"
type: "concept"
updated: "2026-09-01"
source_keys: ["jeff-dickey-twelve-factor-cli-apps"]
---

来源：[12 Factor CLI Apps]({{< relref "/wiki/sources/jeff-dickey-twelve-factor-cli-apps.md" >}})

Terminal output stream contracts 指 CLI 与终端、shell 管道和文件重定向之间的输出约定。Jeff Dickey 将规则概括为 stdout 用于输出结果，stderr 用于消息。这样用户把 stdout 重定向到文件时，警告、错误和进度仍能显示在屏幕上，而 JSON、二进制或其他结构化结果不会被人类提示污染。

来源还指出，stderr 不只用于错误。下载进度、spinner 和警告都可能属于 stderr，因为它们面向用户观察，而不是结果数据。若 CLI 启动子命令，也应把子命令的 stderr 传给用户，避免重要故障信息被隐藏。

这个输出契约还包括 tty 检测。颜色、弱化、spinner 和进度条依赖终端能力；当 stdout 或 stderr 不是 tty，或用户通过 `TERM=dumb`、`NO_COLOR`、`--no-color`、应用级禁色变量表达偏好时，CLI 应关闭这些装饰性输出。

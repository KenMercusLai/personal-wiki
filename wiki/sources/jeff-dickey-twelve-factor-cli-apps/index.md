---
title: "12 Factor CLI Apps"
description: "Jeff Dickey adapts Heroku's Twelve-Factor App spirit to command-line tools, arguing that good CLIs need discoverable help, clear flags, predictable streams, actionable errors, scriptability, speed, and standard file placement."
type: "source"
updated: "2026-09-01"
source_key: "jeff-dickey-twelve-factor-cli-apps"
image_status: "not_selected"
author: "Jeff Dickey"
source_date: "2018-10-10"
---

## 摘要

这篇文章把 Heroku 的 Twelve-Factor App 思路迁移到命令行工具设计。Jeff Dickey 认为，CLI 比 Web 应用更快构建，也更容易被用户组合进高级工作流，但它要求使用者具备更多技术背景。因此，一个好 CLI 必须把可发现性、错误处理、自动化兼容和终端环境差异作为产品体验的一部分，而不是只把命令解析成函数调用。

文章首先强调帮助系统。CLI 没有图形界面引导用户，所以应同时提供命令内帮助和 Web/README 文档，并让空命令、`--help`、`-h`、`help` 以及子命令帮助都能可靠显示说明。帮助内容不应只列语法，还要解释命令、参数、标志和常见示例；自动补全也是一种重要的帮助形式。

在输入设计上，作者偏好 flags 而不是多个不同类型的位置参数。位置参数虽然短，但当一个命令接受源对象、目标对象等多个不同含义时，用户很容易混淆；`--from`、`--to` 这类显式标志能让命令含义自解释。对于会把参数继续传给下游进程的 CLI，还应支持 `--` 作为停止解析的分隔符。

文章还把输出和故障处理视为 CLI 的核心契约。stdout 应用于机器可消费的结果，stderr 应用于警告、错误和进度消息，这样重定向 stdout 时不会污染结构化输出。错误消息要给出错误码、标题、描述、修复方法和更多信息链接；未预期错误则需要 debug 环境变量、完整 trace 和可轮转的日志辅助诊断。

作者同时主张现代 CLI 可以使用颜色、弱化、spinner、进度条、系统通知、交互式提示、确认框、复选框和单选项改善体验，但这些能力都必须服从脚本化和终端能力检测。stdin/stdout/stderr 不是 tty、`TERM=dumb`、`NO_COLOR`、`--no-color` 或应用级禁色变量出现时，CLI 应退回到朴素输出；提示也必须能被 flag 覆盖，不能阻止自动化。

后半部分讨论表格、性能、开源协作、子命令组织和文件位置。表格每行应表示一条数据，不应使用边框，并应支持列选择、截断控制、隐藏表头、过滤、排序、CSV 和 JSON。CLI 启动速度应以 `time` 直接测量，普通命令最好落在 100-500ms 区间。复杂工具通常适合多命令结构，而配置、数据和缓存文件应遵循 XDG Base Directory 以及各平台缓存目录惯例。

## 关键观点

- CLI 是产品界面，不能只按内部实现暴露命令；帮助、示例、补全和版本信息是用户理解工具的入口。
- 多个不同含义的位置参数会降低可读性，显式 flags 更适合表达复杂操作。
- stdout、stderr、tty 检测和禁色约定共同构成 CLI 与 shell、文件、管道和脚本之间的兼容契约。
- 好的 CLI 错误消息需要告诉用户发生了什么、如何修复，以及在哪里获得更多诊断信息。
- 交互式提示、颜色和进度反馈可以提升体验，但必须能被脚本和非交互环境绕过。
- 表格输出要保持每行一条数据，并为机器处理提供 CSV、JSON、过滤和排序能力。
- CLI 启动速度直接影响使用意愿；大多数命令应把冷启动时间控制在用户可感知的快速范围内。
- 文件落点应遵循 XDG Base Directory 和平台缓存惯例，避免把配置、数据和缓存混在一起。

## 相关知识

- [Command-line interface user experience]({{< relref "/wiki/concepts/command-line-interface-user-experience.md" >}})
- [Scriptable CLI design]({{< relref "/wiki/concepts/scriptable-cli-design.md" >}})
- [CLI help and discoverability]({{< relref "/wiki/concepts/cli-help-and-discoverability.md" >}})
- [Terminal output stream contracts]({{< relref "/wiki/concepts/terminal-output-stream-contracts.md" >}})
- [CLI error message design]({{< relref "/wiki/concepts/cli-error-message-design.md" >}})
- [Structured CLI output]({{< relref "/wiki/concepts/structured-cli-output.md" >}})
- [CLI startup performance]({{< relref "/wiki/concepts/cli-startup-performance.md" >}})
- [XDG-based CLI file layout]({{< relref "/wiki/concepts/xdg-based-cli-file-layout.md" >}})
- [Jeff Dickey]({{< relref "/wiki/entities/jeff-dickey.md" >}})
- [Heroku]({{< relref "/wiki/entities/heroku.md" >}})
- [oclif]({{< relref "/wiki/entities/oclif.md" >}})
- [Twelve-Factor App]({{< relref "/wiki/entities/twelve-factor-app.md" >}})

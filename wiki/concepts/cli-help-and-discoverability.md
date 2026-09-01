---
title: "CLI help and discoverability"
description: "通过命令内帮助、Web 文档、示例和自动补全降低命令行工具的发现成本。"
type: "concept"
updated: "2026-09-01"
source_keys: ["jeff-dickey-twelve-factor-cli-apps"]
---

来源：[12 Factor CLI Apps]({{< relref "/wiki/sources/jeff-dickey-twelve-factor-cli-apps.md" >}})

CLI help and discoverability 指用户在没有图形界面引导时，仍能从命令本身和外部文档快速理解工具能力。Jeff Dickey 认为，帮助文档对 CLI 比对 Web 应用更重要，因为命令行界面无法靠可见按钮和表单提示用户下一步。

这篇来源提出，CLI 应同时提供命令内帮助和 Web/README 文档。常见入口都应显示帮助，包括空命令、`--help`、`-h`、`help` 以及子命令帮助。`-h,--help` 应作为保留 help flag 使用，避免和业务参数混淆；对于可能存在名为 `help` 的参数或资源的子命令，则应避免过早把它解释成帮助请求。

好的帮助内容不只是 usage 字符串。来源要求说明命令描述、参数含义、flag 含义，并重点提供常见示例，因为示例往往是用户最常查阅的部分。Shell completion 也被视为帮助系统的一部分，它让用户在输入过程中发现可用命令、参数和值。

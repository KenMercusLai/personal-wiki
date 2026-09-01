---
title: "CLI error message design"
description: "让命令行错误同时说明问题、诊断线索和用户可以采取的修复动作。"
type: "concept"
updated: "2026-09-01"
source_keys: ["jeff-dickey-twelve-factor-cli-apps"]
---

来源：[12 Factor CLI Apps]({{< relref "/wiki/sources/jeff-dickey-twelve-factor-cli-apps.md" >}})

CLI error message design 指命令行工具在失败时提供可执行的诊断反馈。Jeff Dickey 认为，CLI 出错比 Web 应用更常见，因为它没有图形界面逐步约束用户输入；因此错误消息本身就是产品体验的一部分。

来源给出的错误消息要素包括错误码、错误标题、可选描述、修复方法和更多信息链接。这样的错误不是只宣布失败，而是帮助用户判断错误类型、定位对象、理解原因，并看到下一步可尝试的命令或文档。

对于未预期错误，文章建议提供完整 traceback 和 debug 输出机制。按组件分组的 debug 环境变量、带时间戳的日志、定期截断日志以及去除 ANSI 颜色码，都是为了让用户和维护者能在事后复盘问题，同时避免日志本身变成新的维护负担。

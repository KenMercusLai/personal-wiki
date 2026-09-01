---
title: "Platform-native product strategy"
description: "Platform-native product strategy treats important client apps as separate platform products when mobile operating systems diverge too much for one shared codebase to preserve the best experience."
type: "concept"
updated: "2026-09-02"
source_keys: ["hallway-debates-2016-product-manager-discussion-guide"]
---

来源：[Hallway Debates]({{< relref "/wiki/sources/hallway-debates-2016-product-manager-discussion-guide.md" >}})

Platform-native product strategy 指当客户端体验是产品价值的重要部分时，团队应认真管理每个平台自己的产品与工程选择，而不是默认追求一个代码库覆盖所有设备。来源认为，跨平台方案的吸引力会长期存在，但移动平台演进越快，共享抽象越容易被现实差异击穿。

文章列出的差异包括 Swift 等语言变化、语音和多任务等界面模型差异、force touch 和不同平板尺寸等硬件能力，以及支付、身份和服务集成等平台服务。产品经理的工作因此不只是决定“做不做某个功能”，还要决定哪些能力应共享，哪些能力应成为平台特定体验。

来源还把桌面封装应用作为相邻案例。把浏览器版套进原生窗口可以提供应用切换、窗口管理和登录保持等基础便利，但通常很难获得真正深入的桌面集成。除非团队愿意承担原生体验的长期承诺，否则这类投入可能不能带来足够市场优势。

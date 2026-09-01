---
title: "HTTP 402 Payment Required"
description: "HTTP 402 Payment Required 在来源中被设想为浏览器、网站和支付服务协商内容访问费用的协议入口。"
type: "concept"
updated: "2026-09-02"
source_keys: ["david-humphrey-402-payment-required"]
---

HTTP 402 Payment Required 在 David Humphrey 的文章中不是普通错误提示，而是重新想象 Web 付费基础设施的入口。

来源：[402: Payment Required]({{< relref "/wiki/sources/david-humphrey-402-payment-required.md" >}})

来源指出，网站可以在用户请求付费资源时返回 402，并附带价格、购买、租用或订阅所需的信息。浏览器识别这个响应后，不只是告诉用户访问被拒绝，而是展示交易选项，并和用户选择的支付服务一起完成访问授权。

这个设想把 HTTP 状态码从“请求成功或失败”的提示扩展为“访问条件需要协商”的信号。它并不要求所有网页收费，而是让付费成为用户可见、可拒绝、可比较的选择，替代广告网络和追踪脚本带来的隐性经济交换。

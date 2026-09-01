---
title: "402: Payment Required"
description: "David Humphrey 以 iOS 9 Safari 内容过滤和圣保罗户外广告禁令为引子，主张浏览器应提供广告之外的 Web 付费机制。"
type: "source"
updated: "2026-09-02"
source_key: "david-humphrey-402-payment-required"
image_status: "not_selected"
author: "David Humphrey"
source_date: "2015-09-28"
---

## 摘要

David Humphrey 借 iOS 9 的 Safari 内容过滤 API 和圣保罗 Clean City Law 作类比，说明规则改变会重塑广告占据公共空间的方式。文章的重点不是简单支持或反对广告拦截，而是指出 Web 长期依赖广告收入后，一旦浏览器开始让用户更容易屏蔽广告，内容生产者和平台就需要更明确、可信、普遍的替代收入机制。

文章把 Web 的“免费”和“收费”描述成连续谱。用户以为免费访问内容，但广告网络、追踪脚本、数据收集、页面膨胀、安全风险和隐私成本已经让访问行为带有隐性经济交换。移动时代的 App Store、Google Play、应用内支付和订阅也已经训练用户为软件、服务和内容支付小额费用，因此作者认为 Web 不应只在广告和封闭付费墙之间二选一。

Humphrey 的核心设想是让浏览器作为用户代理参与交易。网站可以用 HTTP 402 Payment Required 这样的响应表达资源需要付费，并附带足够的价格、租用、购买或订阅信息；浏览器则根据用户信任的支付提供方呈现交易选项，让用户显式决定是否购买访问权。这样一来，浏览器不只是“渲染或不渲染”页面，还可以帮助用户、网站和支付服务完成安全、低摩擦的内容交易。

## 关键观点

- iOS 9 的内容过滤能力没有直接内置广告拦截器，却改变了移动 Web 上广告展示的规则。
- 广告资助的 Web 并不真正免费，用户常常用注意力、行为数据、下载性能、隐私和安全风险隐性支付。
- 移动平台已经通过应用商店、应用内购买和订阅让小额数字内容付费变得日常化。
- 浏览器比随机网站更受用户信任，因此可以承担跨站点支付、身份和交易确认的中介角色。
- HTTP 402 Payment Required 可以被设想为网站和浏览器协商付费访问的协议入口，而不只是保留状态码。
- 显式支付机制不要求所有内容收费，但能让用户在付费、订阅、租用和不购买之间做出清楚选择。

## 相关知识

- [HTTP 402 Payment Required]({{< relref "/wiki/concepts/http-402-payment-required.md" >}})
- [浏览器中介的 Web 支付]({{< relref "/wiki/concepts/browser-mediated-web-payments.md" >}})
- [广告资助 Web 的隐性交易]({{< relref "/wiki/concepts/ad-funded-web-economics.md" >}})
- [HTTP 协议演进]({{< relref "/wiki/concepts/http-protocol-evolution.md" >}})
- [David Humphrey]({{< relref "/wiki/entities/david-humphrey.md" >}})
- [Apple]({{< relref "/wiki/entities/apple.md" >}})
- [iPhone]({{< relref "/wiki/entities/iphone.md" >}})
- [Amazon]({{< relref "/wiki/entities/amazon.md" >}})
- [Google]({{< relref "/wiki/entities/google.md" >}})

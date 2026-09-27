---
title: "Boring Technology"
type: concept
tags: [software-architecture, tooling, startups, operations]
sources:
  - wenbin-fang-the-boring-technology-behind-a-one-person-internet-company
  - etsy-cto-q-a-we-need-software-engineers-not-developers-the-new-stack
last_updated: 2026-09-27
knowledge_schema: synthesis-v1
---

## Definition
[[BoringTechnology]] is the deliberate choice of mature, widely used, well-understood tools over newer or more fashionable alternatives, so that a builder's scarce attention goes to the product rather than to the stack that runs it.

## Current Synthesis
The [[ListenNotes]] account makes the concept concrete at one-person scale. The author runs a multi-product internet business on Django and Python, uWSGI and NGINX, [[PostgreSQL]], [[Redis]], Elasticsearch, Celery, Celery Beat, and Supervisord, and reports that the stack contains no AI, deep learning, or blockchain. A solo company pays for every tool in money and in learning, debugging, and operating attention, so proven components can be cheaper even when newer ones have local technical advantages.

The Etsy interview extends the same judgment to a much larger organization. [[JohnAllspaw]] describes a relatively straightforward PHP, Linux, Apache, MySQL, search, and data stack and says proposed novelty should carry an explicit account of its long-term organizational cost. Architecture review is not presented simply as veto power: it can reveal that another team already solved the problem and keep product freedom from being consumed by redundant infrastructure ownership.

Together the sources make boring technology an attention-allocation and governance principle, not nostalgia. Docker, Kubernetes, serverless, specialized data systems, or a new language may be justified when requirements and operating capacity support them. The decision should include team learning, support, deployment, observability, and retirement costs, while familiar tools still require disciplined operations rather than neglect.

## Key Claims
- Conventional, long-tested components can support both a one-person internet business and a large marketplace when they fit the workload.
- Newness is not a proxy for product value, while novelty creates continuing learning, support, and operational obligations.
- Containers, orchestration, serverless systems, or specialized tools are stage- and requirement-dependent choices rather than universal defaults.
- Architecture review can reveal existing internal solutions and force the ownership cost of a proposed tool into the decision.
- Choosing boring technology is attention budgeting: scarce engineering effort goes to products and customers instead of redundant infrastructure novelty.
- Familiar tools still need disciplined deployment, monitoring, alerting, and operational ownership.

## Evidence
- Stack inventory: [[wenbin-fang-the-boring-technology-behind-a-one-person-internet-company]] names Django, Python 3, Ubuntu, uWSGI, NGINX, PostgreSQL, Redis, Elasticsearch, Celery, Celery Beat, and Supervisord as the production system.
- Explicit rejection of novelty: [[wenbin-fang-the-boring-technology-behind-a-one-person-internet-company]] states that the stack uses no AI, deep learning, or blockchain and contrasts that with the expectation that a modern company should have them.
- Stage-dependent orchestration: [[wenbin-fang-the-boring-technology-behind-a-one-person-internet-company]] argues that Docker suits a billion-dollar mid-size startup while possibly being over-engineering for a one-person company, and reports no Docker, Kubernetes, or serverless in use.
- Familiarity as reliability: [[wenbin-fang-the-boring-technology-behind-a-one-person-internet-company]] keeps PostgreSQL as the main store because years of experience with it make it battle-tested enough to rely on.
- Attention budget: [[wenbin-fang-the-boring-technology-behind-a-one-person-internet-company]] frames the choice as knowing when not to over-engineer, and describes the operator's goal as spending less time and earning more rather than spending more time to save money.
- Operational discipline: [[wenbin-fang-the-boring-technology-behind-a-one-person-internet-company]] pairs the boring stack with Ansible configuration management, a parameterized release script, Datadog and PagerDuty monitoring, Rollbar exception tracking, and Slack webhooks.
- Capacity over tuning: [[wenbin-fang-the-boring-technology-behind-a-one-person-internet-company]] says servers are deliberately over-provisioned for traffic spikes rather than finely orchestrated.
- Organizational scale: [[etsy-cto-q-a-we-need-software-engineers-not-developers-the-new-stack]] describes Etsy's preference for a relatively straightforward core stack so teams can focus on product work.
- Explicit novelty cost: [[etsy-cto-q-a-we-need-software-engineers-not-developers-the-new-stack]] says introducing a new technology can create a large long-term organizational burden.
- Reuse through review: [[etsy-cto-q-a-we-need-software-engineers-not-developers-the-new-stack]] presents architecture review as a place where another engineer can identify an already-solved analogous problem.

## Counterevidence & Qualifications
The sources are self-reported practitioner accounts, not comparisons showing that stack restraint caused reliability or product focus. Listen Notes reflects one infrastructure-experienced founder; Etsy reflects one executive's 2016 description of a larger organization. Managed platforms can remove work for teams without that expertise, and specialized databases or orchestration can be justified once scale, compliance, latency, or coordination requirements become real. Review can also become status-preserving bureaucracy, while familiarity can become a liability if a team avoids necessary migration, excludes available talent, or keeps a tool whose risk now exceeds its switching cost.

## What Changed
- Extended the concept from solo-founder attention budgeting to organization-level governance of novelty and internal reuse.
- Made architecture review's constructive role explicit: expose prior solutions and continuing ownership cost before adoption.

## Related Concepts
- [[TechnologyStackComplexity]] - boring technology is one response to the learning and operational cost of each added tool.
- [[DistributedSystemRestraint]] - both concepts defer architecture until scale and team capacity justify it.
- [[ToolFamiliarity]] - the concept favors tools the operator already knows and can debug.
- [[DeploymentAutomation]] - a boring stack still needs a repeatable, trustworthy release path.
- [[MicroCompany]] - the concept is stated from the perspective of a one-person company protecting its attention.
- [[BootstrappedSaaS]] - lean self-funded businesses are a natural context for conventional tool choices.
- [[MonolithConsolidation]] - collapsing services back into one system is a related simplification move.
- [[ContainerNativePractice]] - the container-and-orchestration practice this source deliberately declines.
- [[SimpleMadeEasy]] - both distinguish simple, understandable systems from merely familiar or easy ones.
- [[SystemReliability]] - a proven stack may reduce failure modes, but reliability still depends on monitoring and operations.
- [[ProductionOwnership]] - familiar tools still require people who observe and operate them after deployment.
- [[DevOpsCulture]] - shared operational responsibility determines whether stack restraint produces usable simplicity.

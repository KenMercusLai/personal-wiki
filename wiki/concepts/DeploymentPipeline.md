---
title: "Deployment Pipeline"
type: concept
tags: [continuous-delivery, deployment, release-engineering]
sources:
  - architecting-for-continuous-delivery-thoughtworks
last_updated: 2026-09-14
knowledge_schema: synthesis-v1
---

## Definition
[[DeploymentPipeline]] is an automated, visible model of the build, deploy, test, and release path that moves a software revision from source control toward production while increasing release confidence at each stage.

## Current Synthesis
The Thoughtworks source treats the deployment pipeline as the central abstraction that makes continuous delivery operational. Disconnected CI jobs can automate phases but still hide the whole production flow, making it hard to answer whether a particular revision is releasable.

A pipeline turns release work into an inspectable production process. Each commit passes through staged checks and deployments; failures stop the line for fix or revert decisions; production deploy failure can route back to the last successful deploy stage. The article also uses Go.CD's value-stream map to show that pipelines can represent component dependencies, microservice integration requirements, and end-to-end production confidence rather than only a simple linear build.

## Key Claims
- A deployment pipeline gives release confidence by connecting build, test, deploy, and release stages into one visible flow.
- CI and deployment automation can remain insufficient when build configurations are disconnected.
- Each passing stage should increase confidence in a specific code revision.
- Pipeline stops support immediate fix, revert, or rollback decisions.
- Value-stream visualization exposes bottlenecks and component dependencies in the production path.
- Pipeline design can support trunk-based development and microservice integration testing when dependency flow is explicit.

## Evidence
- CI limit: [[architecting-for-continuous-delivery-thoughtworks]] says disconnected build configurations make production confidence hard to assess.
- Flow model: [[architecting-for-continuous-delivery-thoughtworks]] describes the pipeline as a flow chart from source repository to production.
- Stage confidence: [[architecting-for-continuous-delivery-thoughtworks]] says each commit advances through stages, gaining confidence with each passing stage.
- Failure handling: [[architecting-for-continuous-delivery-thoughtworks]] says a failed stage stops the pipeline for fix or revert, and production deploy failure can roll back to the last successful production deploy.
- Dependency view: [[architecting-for-continuous-delivery-thoughtworks]] says the Go.CD value-stream map displays application dependencies and commit states on the way to production.

## Counterevidence & Qualifications
The source advocates pipelines strongly but does not detail failure modes of pipeline design, such as overly slow stages, excessive manual gates, weak production monitoring, or false confidence from low-quality tests. A pipeline represents confidence only to the extent that its stages are fast, meaningful, and maintained.

## What Changed
- Created the concept from Thoughtworks' deployment-pipeline discussion and image captions.

## Related Concepts
- [[ContinuousDelivery]] - the pipeline is presented as CD's backbone.
- [[DeploymentAutomation]] - automated deployment phases become more useful when connected into a visible flow.
- [[TestPyramid]] - fast staged feedback depends on an appropriate test mix.
- [[CDComponentization]] - component dependencies can be represented inside pipeline flow.
- [[ChangeSafety]] - stops, reverts, and rollbacks are release-safety mechanisms.
- [[TrunkBasedDevelopment]] - the article names trunk-based development as a practice pipelines can support.

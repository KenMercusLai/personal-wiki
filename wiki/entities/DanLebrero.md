---
title: "Dan Lebrero"
type: entity
tags: [software-testing, tdd, software-engineering]
sources:
  - the-tragedy-of-100-code-coverage
last_updated: 2026-10-02
knowledge_schema: synthesis-v1
---

## Overview
[[DanLebrero]] is represented in the wiki as a software practitioner who supports unit testing and test-first development while arguing against universal coverage targets and mandatory use of one test tool at every behavioral boundary.

## Current Profile
Lebrero describes fifteen years of advocating TDD or at least some unit testing, then explains why he increasingly asks what a proposed test is meant to accomplish. His two workplace examples criticize a Mockito test for branch-free callback glue and a Cucumber stack for a map lookup, treating both as cases where organizational rules displaced proportionate engineering judgment.

His position is not anti-testing. He recommends experiencing the 100% coverage extreme on one project to learn its limit, then distinguishing useful tests from counterproductive ones by their confidence, cost, tool fit, and future maintenance burden.

## Key Characteristics
- Long-term advocate of unit testing and test-first development in the source's first-person account.
- Evaluates tests by behavioral information and maintenance cost rather than coverage or class counts alone.
- Criticizes organization-wide mandates to use Mockito or Cucumber irrespective of the test boundary.
- Treats one deliberately extreme 100%-coverage project as a learning exercise rather than a universal operating rule.

## Evidence
- Testing background and shift: [[the-tragedy-of-100-code-coverage]] says Lebrero had promoted TDD for fifteen years but increasingly asked why a test was being written.
- Proportionality judgment: [[the-tragedy-of-100-code-coverage]] contrasts simple glue and map-lookup code with the machinery built to test it.
- Tool-fit judgment: [[the-tragedy-of-100-code-coverage]] rejects mandatory Mockito and Cucumber use when simpler checks communicate the behavior better.
- Learning through extremes: [[the-tragedy-of-100-code-coverage]] recommends one 100%-coverage project as experience that can reveal the limit of the practice.

## Qualifications
This profile comes from one 2016 first-person practitioner essay. The article gives no project sizes, defect rates, suite timings, maintenance measurements, interview transcripts, or later outcomes, and its two selected examples cannot establish which testing mix is optimal across languages, architectures, teams, or failure costs. The wiki therefore records Lebrero's argument as a proportionate-testing heuristic rather than a general exemption for simple-looking code.

## What Changed
- Created the profile around Lebrero's qualified defense of testing and critique of mechanical coverage and tool mandates.

## Relationships
- [[ConfidenceBasedTesting]] - formalizes the risk, information, and lifecycle-cost judgment behind Lebrero's examples.
- [[SoftwareVerification]] - broader practice that Lebrero supports while disputing low-information checks.
- [[TestPyramid]] - helps locate behavior at a cheaper test boundary when high-level tooling is disproportionate.
- [[InternalSoftwareQuality]] - test maintenance is part of the future change cost Lebrero asks teams to count.
- [[ExtremeProgramming]] - practice tradition connected to the TDD approach Lebrero endorses with qualifications.

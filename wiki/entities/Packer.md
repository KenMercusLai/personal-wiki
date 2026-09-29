---
title: "Packer"
type: entity
tags: [infrastructure, images, automation, aws]
sources:
  - immutable-infrastructure-using-packer-ansible-and-terraform
last_updated: 2026-09-30
knowledge_schema: synthesis-v1
---

## Overview
[[Packer]] is an automated machine-image builder used in the source to bake an [[AWS]] AMI whose operating-system and application configuration is supplied by [[Ansible]].

## Current Profile
The example positions Packer between Terraform-managed network provisioning and Terraform-managed EC2 creation. Its Amazon EBS builder launches a temporary instance from a base AMI inside a supplied subnet, gives that instance a public IP for the build, invokes an Ansible playbook, and emits a timestamp-named AMI tagged `Packer-Ansible`.

Packer's role is therefore artifact construction rather than long-lived infrastructure ownership. It moves Nginx installation and static-site setup into the build path so new EC2 instances can start from a prepared image. Terraform later discovers the output by tag rather than receiving an explicitly promoted image ID from the build.

## Key Characteristics
- Builds an AMI from a declared base image and builder configuration.
- Uses an Ansible provisioner to apply application configuration during the image build.
- Runs its temporary builder inside a Terraform-created AWS subnet.
- Tags the resulting image so Terraform can discover it for instance creation.
- Moves installation latency and failure from each server launch into a reusable image-build step.

## Evidence
- Builder role: [[immutable-infrastructure-using-packer-ansible-and-terraform]] configures an `amazon-ebs` builder with a base AMI, instance type, SSH user, region, and subnet.
- Configuration handoff: [[immutable-infrastructure-using-packer-ansible-and-terraform]] invokes an Ansible playbook as the Packer provisioner.
- Artifact identity: [[immutable-infrastructure-using-packer-ansible-and-terraform]] names the AMI with a timestamp and applies the `Name=Packer-Ansible` tag used by Terraform.
- Immutable-delivery purpose: [[immutable-infrastructure-using-packer-ansible-and-terraform]] uses the baked AMI so launched instances do not repeat the Nginx configuration step.

## Qualifications
This profile comes from one 2018 tutorial. It does not compare Packer with other image builders, measure build reproducibility or duration, show artifact testing or signing, or provide current AWS credential and networking guidance. A timestamped name and shared tag identify output, but the example does not demonstrate explicit promotion of an approved image digest or ID.

## What Changed
- Established Packer as the image-construction boundary connecting Terraform-provisioned networking, Ansible configuration, and Terraform-launched EC2 capacity.

## Relationships
- [[ImmutableInfrastructure]] - Packer constructs the replaceable machine artifact used by the operating model.
- [[Ansible]] - Ansible is the configuration provisioner inside the image build.
- [[Terraform]] - Terraform supplies the subnet and later consumes the tagged AMI.
- [[AWS]] - the example uses Packer's Amazon EBS builder to produce an AMI.
- [[ConfigurationManagement]] - Packer bounds configuration convergence to image construction rather than every application-server launch.

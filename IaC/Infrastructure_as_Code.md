# Infrastructure as Code

## What problem needs solving?

* At the moment, still manually having to provision servers
  
What's meant by "provision"?
    * setting up & configuring servers
## What have we automated?

VMs
* Creation of the VMs? No
* Creation of the infrastructure they live in? No
* Setup & configuring of software on the VMs? Yes
  * Bash scripting
  * User data
  * AMIs
  
## Solving the problem

IaC -> can automate all of it  
How? Codify our requirements
* Do not always define the steps (imperative) in the code
* Instead can be declarative (declare what you want)

## What is IaC?

* A ways to manage and provision resources (often computers) through a machine-readable definition of the infrastructure

## Benefits of IaC?

* Speed & simplicity
* Consistency & accuracy
* Version control
* Scalability

## When/where to use IaC

* Return on investment? Is it worth it?

## What are the tools available for IaC?

2 types:
* Configuration management (software configuration)
    * Chef
    * Puppet
    * Ansible
* Orchestration (managing infrastructure)
  * Terraform (cloud-agnostic)
  * Cloud-specific:
    * Azure - ARM/Bicep templates
    * AWS - CloudFormation

## What is provisioning of infrastructure? Do CM tools do it?

## What is configuration management (CM)?
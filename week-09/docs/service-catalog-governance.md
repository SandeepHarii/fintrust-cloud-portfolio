# Service Catalog Governance

## Overview

AWS Service Catalog can be used to provide FinTrust teams with a controlled catalogue of approved cloud products.

Instead of allowing teams to provision infrastructure without governance, approved products can be made available through a central portfolio with defined configuration options and constraints.

Because the Week 9 practical work was completed without directly provisioning or configuring AWS services, no live Service Catalog screenshot or `list_portfolios` output is included in this portfolio.

## FinTrust Service Catalog Design

A production FinTrust environment could use a Service Catalog portfolio owned by the cloud platform or FinOps team.

The portfolio could contain approved products such as:

* Standard compute environments
* Approved application infrastructure
* Database configurations
* Development environments
* Production application environments
* Approved networking components

Each product would use an approved infrastructure definition and expose only the configuration options that FinTrust teams are permitted to change.

## Governance Model

A simplified governance model would be:

```text
FinTrust Cloud Governance Team
            ↓
Service Catalog Portfolio
            ↓
Approved Products
            ↓
Product Constraints
            ↓
FinTrust Development / Application Teams
```

The governance team would remain responsible for maintaining the portfolio and ensuring that products comply with FinTrust security, cost, and operational requirements.

## Tagging Constraints

Mandatory tagging should be incorporated into the product configuration and governance process.

Example FinTrust tags could include:

| Tag                | Purpose                                        |
| ------------------ | ---------------------------------------------- |
| Application        | Identifies the application or workload         |
| Environment        | Identifies development, testing, or production |
| Owner              | Identifies the responsible team                |
| CostCenter         | Supports cost allocation                       |
| DataClassification | Identifies the sensitivity of the workload     |

The exact tag values would be determined by FinTrust's production governance standards.

Where supported by the implementation, users should not be able to provision an approved product without supplying the required governance information.

## Cost Governance

Service Catalog can also support FinTrust's cost-management objectives by controlling which configurations users can provision.

For example, an approved product could restrict users to predefined instance types or configurations rather than allowing unrestricted resource selection.

This reduces the risk of teams provisioning unnecessarily expensive infrastructure.

Service Catalog therefore complements the Week 9 cost-management activities involving:

* Cost Explorer
* AWS Budgets
* Compute Optimizer
* Savings Plans
* Cost allocation and tagging

## Python Verification

A production implementation could use the AWS SDK for Python (`boto3`) to retrieve Service Catalog portfolio information.

A `list_portfolios` request could be used to identify the portfolios available to the account.

Additional Service Catalog API operations could then be used to inspect:

* Portfolios
* Products
* Provisioning artefacts
* Principal associations
* Constraints

The API interaction would require an authorised AWS environment and appropriate IAM permissions.

## Required Evidence

The Week 9 deliverable calls for evidence showing at least one Service Catalog portfolio and its products.

The live console screenshot or `list_portfolios` output was not produced because direct AWS service configuration was outside the scope of the practical work.

No fabricated portfolio names, products, screenshots, or API output have been included.

## FinTrust Use Case

For FinTrust, Service Catalog could provide a controlled self-service model.

Application teams could select approved infrastructure products while the central cloud team maintains control over:

* Security requirements
* Approved configurations
* Cost controls
* Required tags
* Access permissions
* Operational standards

This would allow FinTrust to balance developer self-service with centralised cloud governance.

## Outcome

The exercise demonstrated how Service Catalog can support standardisation and governance in a larger AWS environment.

For the FinTrust 2,847-server migration, a governed catalogue could also help standardise the cloud environments created as workloads are migrated, while reducing configuration drift between teams.
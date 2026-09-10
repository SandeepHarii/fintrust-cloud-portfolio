# AWS Budget Configuration

## Overview

AWS Budgets can be used to establish spending limits and receive alerts when actual or forecasted AWS costs reach defined thresholds.

For FinTrust, a monthly cost budget would provide an additional layer of cost governance alongside Cost Explorer reporting.

Because the Week 9 practical work was completed without directly provisioning or configuring AWS services, no live AWS Budgets configuration or console screenshot is included in this portfolio.

## Required Configuration

A production FinTrust budget would include:

* A monthly spending limit
* A defined budget period
* A cost scope covering the relevant AWS account or workloads
* A percentage-based alert threshold
* Notification recipients for the alert

For example, the alert could be configured to trigger when actual or forecasted spending reaches a defined percentage of the monthly budget.

No specific monetary limit or threshold percentage is recorded here because no live FinTrust AWS budget was configured.

## Budget Alert Workflow

A production configuration could follow this workflow:

```text
AWS Budgets
    ↓
Monthly cost monitoring
    ↓
Threshold reached
    ↓
Budget notification
    ↓
FinTrust cost owner
    ↓
Investigation and corrective action
```

The notification could be used to trigger a review of recent deployments, service usage, resource sizing, or unexpected changes in consumption.

## Python / boto3 Alternative

AWS Budgets can also be managed programmatically using `boto3`.

A production implementation could use the AWS Budgets API to:

* Create a budget
* Define the monthly limit
* Configure notification thresholds
* Retrieve existing budget configurations
* Review budget status

A `describe_budgets` operation could also be used to retrieve existing budget configuration for reporting or verification.

The API interaction would require appropriate AWS credentials and permissions, which were outside the scope of this week's practical work.

## FinTrust Use Case

Budget alerts would complement the other Week 9 cost-management controls.

For example:

* **Cost Explorer** provides visibility into actual spending.
* **Budgets** provide threshold-based alerts.
* **Compute Optimizer** can identify potential resource optimisation opportunities.
* **Savings Plans** can help reduce eligible compute costs.
* **Tagging and governance** can improve cost allocation and accountability.

Together, these controls provide a more structured approach to FinTrust cloud cost management.

## Portfolio Scope

The required live AWS Budget screenshot was not produced because direct AWS service configuration was outside the scope of the practical work.

No fabricated AWS budget values, alerts, or screenshots have been included.

The configuration described above represents the intended production design and demonstrates how FinTrust could implement monthly spending controls once an authorised AWS environment is available.

## Outcome

The exercise demonstrated how AWS Budgets can be used as a preventative cost-governance mechanism.

For FinTrust, combining monthly budgets with Cost Explorer reporting would provide both **visibility into current expenditure** and **early warning when spending approaches an agreed limit**.
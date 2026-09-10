# AWS Cost Reporting

## Overview

This document describes the Python-based cost reporting approach developed for the FinTrust portfolio during Week 9.

The solution is designed around AWS Cost Explorer and the AWS Cost Management APIs. It demonstrates how a Python script could retrieve monthly AWS spending data, group costs by service, calculate each service's percentage of total spend, and identify the top five services contributing to the monthly bill.

No live AWS cost data was queried as part of this portfolio work. The AWS API integration is therefore documented as a production approach rather than presented as live cost evidence.

## What the Report Queries

A production implementation would query AWS Cost Explorer for:

* Total AWS spend for a selected monthly period
* Cost grouped by AWS service
* Individual service costs
* Percentage contribution of each service to total spend
* The top five services by cost

The report could use the Cost Explorer `GetCostAndUsage` API with a monthly time range and service-based grouping.

A simplified query would conceptually request:

```text
Time period: Start of month → End of month
Granularity: MONTHLY
Metrics: UnblendedCost
Group by: SERVICE
```

The Python implementation would use `boto3` to communicate with the AWS Cost Explorer API.

## Report Output

The resulting report is intended to provide a simple view of monthly cloud expenditure.

Example output structure:

```text
FinTrust AWS Cost Report
------------------------

Reporting Period: 2026-08-01 to 2026-08-31

Total Spend: R XX,XXX.XX

Top Services:
1. Amazon EC2          R X,XXX.XX    XX.X%
2. Amazon S3           R X,XXX.XX    XX.X%
3. Amazon RDS          R X,XXX.XX    XX.X%
4. AWS Lambda          R X,XXX.XX    XX.X%
5. Amazon DynamoDB     R X,XXX.XX    XX.X%

Other Services:        R X,XXX.XX    XX.X%
```

The exact values would come from the AWS Cost Explorer response when executed against an AWS account with the required permissions.

## Percentage Calculation

For each service, its percentage of total spend can be calculated as:

```text
Service Percentage =
(Service Cost / Total Cost) × 100
```

This makes it easier to identify which services are responsible for the majority of the monthly cloud spend.

## Production Scheduling

In a production FinTrust environment, the Python reporting logic could be deployed as an AWS Lambda function.

An Amazon EventBridge scheduled rule could trigger the Lambda function automatically, for example once per month after the billing period closes.

A possible production flow would be:

```text
EventBridge
     ↓
AWS Lambda
     ↓
Cost Explorer API
     ↓
Python Cost Report
     ↓
Amazon S3 / SNS / Email
```

The report could be stored in Amazon S3 for historical records and optionally distributed through Amazon SNS or another notification mechanism.

## FinTrust Use Case

For FinTrust, automated cost reporting would provide visibility into the cost of the cloud workloads introduced throughout the portfolio.

The report could be used to:

* Track monthly cloud expenditure
* Identify high-cost services
* Monitor changes in service usage
* Support cost optimisation decisions
* Provide input into Savings Plans and workload optimisation
* Support financial governance and budgeting

The report would complement the TCO and Savings Plan analysis implemented elsewhere in Week 9.

## AWS Integration

The portfolio keeps the live AWS API integration separate from the local analysis logic.

The intended production implementation would use `boto3` and AWS Cost Explorer permissions. Since live AWS resource interaction was not performed for this portfolio exercise, no live Cost Explorer results are claimed.

The implementation therefore demonstrates the reporting logic and production architecture without fabricating AWS account data.
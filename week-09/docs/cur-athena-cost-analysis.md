# CUR to Athena Cost Analysis

## Overview

AWS Cost and Usage Reports (CUR) provide detailed billing and usage data that can be stored in Amazon S3 and queried using Amazon Athena.

For FinTrust, this approach would provide a more granular view of cloud costs than a high-level Cost Explorer report.

No live CUR data was queried during this portfolio exercise. The query below represents the type of analysis that would be performed against a production CUR dataset.

## What the Query Would Return

An Athena query against CUR could be used to analyse:

* AWS service costs
* Usage quantities
* Usage types
* AWS account
* Region
* Availability Zone
* Resource identifiers
* Cost allocation tags
* Discounts and credits
* Individual line items

This allows FinTrust to investigate costs at a much more detailed level than simply viewing total spend by service.

## Example Athena Query

A simplified query could look like:

```sql
SELECT
    line_item_product_code AS service,
    line_item_usage_type AS usage_type,
    SUM(line_item_unblended_cost) AS total_cost
FROM fintrust_cur
WHERE
    line_item_usage_start_date >= DATE '2026-08-01'
    AND line_item_usage_start_date < DATE '2026-09-01'
GROUP BY
    line_item_product_code,
    line_item_usage_type
ORDER BY
    total_cost DESC;
```

The exact table and column names depend on the CUR configuration and Athena table generated for the AWS account.

## Why CUR Is More Granular Than Cost Explorer

Cost Explorer is useful for quickly reviewing and visualising AWS spending. It can group costs by dimensions such as service, account, region, and usage type.

CUR provides the underlying detailed billing and usage records. This makes it better suited to deeper analysis where FinTrust needs to investigate individual usage records, resources, tags, discounts, or other billing attributes.

The two services therefore serve different purposes:

| Tool          | Primary Use                                  |
| ------------- | -------------------------------------------- |
| Cost Explorer | Quick cost analysis and visualisation        |
| CUR + Athena  | Detailed billing analysis and custom queries |

For example, Cost Explorer could identify that Amazon EC2 is one of FinTrust's highest-cost services. CUR and Athena could then be used to investigate the underlying usage and billing records contributing to that cost.

## FinTrust Use Case

FinTrust could use CUR with Athena to support:

* Detailed monthly cost analysis
* Cost allocation between teams and workloads
* Investigation of unexpected charges
* Resource-level cost analysis where available
* Tag-based cost reporting
* Discount and Savings Plan analysis
* Historical cost analysis
* Financial governance and optimisation

This would complement the Cost Explorer reporting and TCO analysis developed during Week 9.

## Production Architecture

A production implementation could follow this flow:

```text
AWS Billing Data
       ↓
Cost & Usage Report
       ↓
Amazon S3
       ↓
AWS Glue Data Catalog
       ↓
Amazon Athena
       ↓
SQL Cost Analysis
       ↓
FinTrust Cost Reports / Dashboards
```

This architecture allows the raw billing data to be retained in S3 while Athena provides serverless SQL-based analysis without requiring a dedicated database server.

## Portfolio Scope

This portfolio documents the CUR-to-Athena approach and example query rather than claiming a live CUR query result.

The implementation demonstrates how FinTrust could extend its cost-management capability from high-level Cost Explorer reporting into detailed billing analysis using CUR, S3, Glue, and Athena.

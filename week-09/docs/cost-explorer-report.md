# Cost Explorer Report

## Overview

AWS Cost Explorer provides visibility into cloud spending over time and allows costs to be grouped by dimensions such as AWS service, account, region, and usage type.

For the FinTrust portfolio, Cost Explorer would be used to monitor monthly AWS expenditure and identify the services contributing most to the overall cloud spend.

Because the Week 9 practical work was completed without directly provisioning or accessing AWS services, no live Cost Explorer data or console screenshot is included in this portfolio.

## Required Cost Explorer View

The required Cost Explorer analysis would cover at least one month of AWS expenditure and provide a service-level breakdown.

The expected view would include:

* Total monthly AWS spend
* Spend grouped by AWS service
* The top five services by cost
* Each top-five service's percentage of total monthly spend
* The selected month or date range

The percentage for each service can be calculated as:

```text
Service Percentage =
(Service Cost / Total Monthly Cost) × 100
```

## Example Analysis Structure

A production Cost Explorer report would present the results in a structure similar to:

| Rank | AWS Service | Monthly Cost | Percentage of Total |
| ---: | ----------- | -----------: | ------------------: |
|    1 | Service A   |  Actual Cost |        Calculated % |
|    2 | Service B   |  Actual Cost |        Calculated % |
|    3 | Service C   |  Actual Cost |        Calculated % |
|    4 | Service D   |  Actual Cost |        Calculated % |
|    5 | Service E   |  Actual Cost |        Calculated % |

These values are intentionally not populated because no live FinTrust AWS billing data was available.

## FinTrust Use Case

For FinTrust, this analysis would help identify where cloud expenditure is concentrated across the platform.

The results could then be used to:

* Identify high-cost services
* Investigate unexpected increases in spending
* Evaluate opportunities for rightsizing
* Determine whether Savings Plans or other pricing models would provide value
* Support monthly cloud-cost reviews
* Improve cost governance across development and production workloads

Cost data should be reviewed alongside workload utilisation rather than considering cost in isolation. A service with high expenditure may be justified if it supports a critical workload and is being used efficiently.

## Production Implementation

In a production AWS environment, the Cost Explorer API could be queried programmatically using Python and `boto3`.

The report-generation process could be automated using:

```text
EventBridge
    ↓
AWS Lambda
    ↓
Cost Explorer API
    ↓
Cost aggregation and analysis
    ↓
Report output
    ↓
S3 / email / notification system
```

The generated report could be scheduled monthly or weekly depending on FinTrust's reporting requirements.

## Portfolio Scope

This document represents the analysis methodology and intended production implementation rather than live AWS billing evidence.

No AWS spend figures have been fabricated for the portfolio.

A real Cost Explorer screenshot and service-level cost breakdown would require access to an AWS environment containing billing data. This was outside the scope of the Week 9 practical work.

## Outcome

The exercise demonstrated how Cost Explorer can support cloud financial management by breaking total expenditure down into individual AWS services.

For FinTrust, the same approach could be incorporated into an automated cost-reporting workflow to provide regular visibility into cloud expenditure and support ongoing cost optimisation.
# Week 9 — Cost Management, Governance, Migration & Resilience

## Overview

Week 9 focused on AWS cost management, cost governance, migration planning, resilience and disaster recovery.

The week extended the FinTrust cloud solution beyond application and data architecture by introducing financial governance, workload migration strategy, cost optimisation and migration monitoring.

Practical work included AWS pricing and TCO analysis, cost reporting, AWS Budgets, CUR and Athena analysis, tagging governance, Service Catalog, Savings Plans, 7Rs migration classification, DMS monitoring and large-scale data transfer planning.

---

## What I Learned This Week

* AWS pricing models should be selected according to workload usage patterns and business requirements.
* TCO analysis needs to consider both on-premises and cloud costs, including migration and operational costs.
* Cost Explorer can be used to analyse AWS spending by service and identify major cost contributors.
* AWS Budgets can establish spending limits and percentage-based alerts.
* Cost and Usage Reports provide more granular cost and usage information than Cost Explorer.
* Athena can be used to query CUR data for detailed cost analysis.
* Resource tagging supports cost allocation, ownership and governance.
* AWS Service Catalog can provide a controlled catalogue of approved cloud products.
* Savings Plans can help reduce predictable compute costs.
* The 7Rs framework provides a structured approach to classifying migration workloads.
* Different workload groups may require different migration strategies rather than applying one approach across an entire fleet.
* DMS task monitoring can identify active and terminal migration states.
* Large-scale data transfers require consideration of bandwidth, transfer time, logistics and operational constraints.
* Resilience and disaster recovery should be considered as part of migration planning.

---

## Week Activities

| Day       | Morning                                                                                                                                            | Afternoon                                                                                                                                                                                                       |
| --------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Day 1** | AWS Pricing Models and TCO Reference<br>AWS Pricing Models and TCO<br>AWS SimuLearn: Data Ingestion Methods [LAB]                                  | AWS SimuLearn: Data Lakes [LAB]<br>AWS Cost Estimation with Python - Pricing API and TCO Scripting                                                                                                              |
| **Day 2** | Cost Management Tools Reference<br>Cost Management Tools and Compute Optimizer                                                                     | Lab - Amazon DynamoDB - Implement Performance and Cost Optimization Best Practices<br>AWS SimuLearn: Data Lakes for Financial Services<br>Automating Cost Reporting with Python - Cost Explorer and Budgets API |
| **Day 3** | Cost Governance and Migration Planning Reference<br>Cost Governance and Migration Planning<br>Resilient and Compliant Loan Processing Applications | Cost Governance Automation - Service Catalog and Tag Compliance in Python                                                                                                                                       |
| **Day 4** | Migration Execution and DR Architecture Reference<br>Migration Execution, Resilience and DR                                                        | DMS task monitor<br>Snow transfer planning<br>FIS experiment status                                                                                                                                             |
| **Day 5** | Mock Assessment                                                                                                                                    | —                                                                                                                                                                                                               |

---

## Practical Work

### Pricing and TCO

Developed Python-based exercises covering AWS cost estimation, FinTrust TCO comparison and break-even analysis.

The work considered:

* On-premises infrastructure costs
* AWS compute costs
* Storage
* Networking and data transfer
* Managed services
* Migration costs
* Operational costs
* Long-term cost considerations

**Scripts:**

* `aws_cost_estimator.py`
* `fintrust_tco_break_even.py`
* `savings_plan_calculator.py`

**Documentation:**

* `fintrust-tco-comparison.md`

No fabricated AWS pricing or FinTrust financial figures were used.

### Cost Reporting and Budgets

Developed Python exercises covering monthly service spend analysis, AWS Budgets and automated monthly cost reporting.

The reporting approach considers:

* Monthly AWS spend
* Spend by service
* Top five services
* Percentage contribution to total spend
* Budget thresholds
* Automated reporting

**Scripts:**

* `monthly_spend_by_service.py`
* `aws_budget_manager.py`
* `fintrust_monthly_cost_report.py`

**Documentation:**

* `cost-report.md`
* `cost-explorer-report.md`
* `aws-budget-configuration.md`

### Cost and Usage Analysis

Documented how AWS Cost and Usage Reports could be queried using Athena for more detailed cost analysis.

The work included a representative query approach and an explanation of why CUR provides more granular information than a high-level Cost Explorer analysis.

**Documentation:**

* `cur-athena-cost-analysis.md`

### Cost Governance

Developed Python exercises for resource tag compliance, Service Catalog product inspection and FinTrust governance reporting.

The proposed FinTrust tagging model includes:

* `Application`
* `Environment`
* `Owner`
* `CostCenter`
* `DataClassification`

**Scripts:**

* `tag_compliance_auditor.py`
* `service_catalog_products.py`
* `fintrust_governance_report.py`

**Documentation:**

* `service-catalog-governance.md`

### Migration Planning

Applied the 7Rs framework to the FinTrust 2,847-server fleet.

The workload groups were classified across:

* Rehost
* Replatform
* Refactor
* Repurchase
* Retire
* Retain
* Relocate

The classification considers application dependencies, business value, technical complexity, compliance requirements and migration risk.

**Documentation:**

* `7rs-classification.md`

### Migration Monitoring and Data Transfer

Developed practical Python exercises for migration monitoring, Snow transfer planning and FIS experiment status.

The DMS monitoring work covers replication task identifiers, task status, migration type and terminal states.

The Snow planning work models the transfer of a 3 PB FinTrust regulatory archive and compares physical transfer planning with an internet-based transfer scenario.

**Scripts:**

* `dms_task_monitor.py`
* `snow_transfer_planner.py`
* `fis_experiment_status.py`

**Documentation:**

* `dms-task-monitor.md`
* `snow-transfer-planner.md`

---

## Repository Contents

```text
week-09/
├── README.md
├── reflection.md
├── scripts/
│   ├── aws_budget_manager.py
│   ├── aws_cost_estimator.py
│   ├── dms_task_monitor.py
│   ├── fintrust_governance_report.py
│   ├── fintrust_monthly_cost_report.py
│   ├── fintrust_tco_break_even.py
│   ├── fis_experiment_status.py
│   ├── monthly_spend_by_service.py
│   ├── savings_plan_calculator.py
│   ├── service_catalog_products.py
│   ├── snow_transfer_planner.py
│   └── tag_compliance_auditor.py
└── docs/
    ├── 7rs-classification.md
    ├── aws-budget-configuration.md
    ├── cost-explorer-report.md
    ├── cost-report.md
    ├── cur-athena-cost-analysis.md
    ├── dms-task-monitor.md
    ├── fintrust-tco-comparison.md
    ├── service-catalog-governance.md
    └── snow-transfer-planner.md
```

---

## Key Takeaways

1. Cost management is an ongoing part of cloud architecture rather than a once-off pricing exercise.
2. TCO comparisons need to account for migration, operational and infrastructure costs.
3. Cost Explorer, CUR and Athena provide different levels of cost visibility.
4. Budgets and tagging provide practical controls for managing cloud spending.
5. Service Catalog can help enforce approved products and governance requirements.
6. Savings Plans are most useful where predictable baseline compute usage exists.
7. The 7Rs framework helps match migration strategy to individual workload characteristics.
8. Migration monitoring is important for identifying failed or unexpectedly stopped database migrations.
9. Physical data transfer can be more practical than internet transfer for very large datasets.
10. Cost governance and migration planning should be considered together because migration decisions influence long-term operating costs.

---

## Week Deliverables

| #      | Deliverable                                                  | Portfolio Evidence                                                     |
| ------ | ------------------------------------------------------------ | ---------------------------------------------------------------------- |
| **1**  | AWS Pricing Calculator or Migration Evaluator TCO comparison | `docs/fintrust-tco-comparison.md`                                      |
| **2**  | Cost Explorer service spend analysis                         | `docs/cost-explorer-report.md`                                         |
| **3**  | Python cost report                                           | `docs/cost-report.md` and related cost reporting scripts               |
| **4**  | AWS Budget configuration                                     | `docs/aws-budget-configuration.md` and `aws_budget_manager.py`         |
| **5**  | CUR-to-Athena cost analysis                                  | `docs/cur-athena-cost-analysis.md`                                     |
| **6**  | Service Catalog governance                                   | `docs/service-catalog-governance.md` and `service_catalog_products.py` |
| **7**  | 7Rs classification for 2,847 servers                         | `docs/7rs-classification.md`                                           |
| **8**  | DMS task monitor                                             | `dms_task_monitor.py` and `docs/dms-task-monitor.md`                   |
| **9**  | Snow transfer planning for 3 PB archive                      | `docs/snow-transfer-planner.md`                                        |
| **10** | FinTrust cost and migration narrative extension              | FinTrust portfolio documentation                                       |
| **11** | Meaningful GitHub commit history                             | Git history                                                            |

Where a deliverable normally requires live AWS console evidence, the portfolio documents the required configuration or analysis without presenting simulated information as live AWS evidence.

---

## FinTrust Architecture Extension

Week 9 extends the FinTrust architecture with a financial governance and migration planning layer.

### Cost Management

Predictable FinTrust compute workloads from Weeks 6–8 can be considered for Compute Savings Plan coverage, including analytics and core banking workloads running on EC2 and Fargate.

Cost reporting can be automated through a production workflow such as:

```text
EventBridge
    ↓
Lambda
    ↓
Cost Explorer API
    ↓
Cost Aggregation
    ↓
Monthly Cost Report
    ↓
S3 / Notification
```

### Governance

FinTrust resources are governed through consistent tagging and controlled cloud products.

```text
FinTrust Workloads
        ↓
Tagging Standards
        ↓
Cost Allocation + Ownership
        ↓
Service Catalog
        ↓
Approved Cloud Products
```

### Migration Strategy

The 2,847-server fleet is classified using the 7Rs framework rather than applying a single migration strategy to every workload.

```text
FinTrust 2,847-Server Fleet
            ↓
   Workload Assessment
            ↓
         7Rs
            ↓
 ┌──────────┼──────────┐
 ↓          ↓          ↓
Rehost   Replatform  Refactor
 ↓          ↓          ↓
Repurchase / Retire / Retain / Relocate
```

### Migration and Resilience

Migration execution is supported through DMS monitoring and large-scale transfer planning.

```text
Migration Planning
        ↓
7Rs Classification
        ↓
Migration Execution
   ┌────┴────┐
   ↓         ↓
DMS       Snow Transfer
   ↓         ↓
Monitoring  Large Data Migration
        ↓
Resilience + DR Planning
```

This extends the existing FinTrust architecture by connecting workload migration decisions, cost governance, operational monitoring and resilience planning.

---

## Outcome

Week 9 added a financial, governance and migration-focused layer to the FinTrust cloud portfolio.

The completed work demonstrates the ability to:

* Analyse cloud pricing and TCO
* Plan cost reporting
* Define budget governance
* Analyse detailed cost and usage data
* Apply tagging standards
* Govern approved cloud products
* Evaluate Savings Plan coverage
* Classify workloads using the 7Rs
* Monitor DMS migration tasks
* Plan large-scale data transfers
* Consider resilience and disaster recovery during migration

The portfolio maintains a clear distinction between **practical implementations, documented planning exercises and live AWS evidence**. No simulated output is presented as actual AWS console data.

Week 9 therefore moves the FinTrust solution from simply designing and deploying cloud workloads toward managing their **cost, governance, migration and operational resilience**.
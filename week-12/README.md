# Week 12 - Cost Optimisation, Governance & Performance Tuning

## Overview

Week 12 focused on AWS cost optimisation, organisational governance, infrastructure management, monitoring, automated reporting, and SQL performance tuning.

The week strengthened understanding of AWS cost-management services, AWS Organizations and SCPs, CloudFormation governance concepts, monitoring services, disaster recovery decision-making, and SQL performance tuning.

The practical portfolio work included automated cost reporting, SQL tuning, governance troubleshooting scenarios, a Week 12 reflection and self-assessment, and Portfolio Check-In #12.

## What I Learned This Week

* Savings Plans and the distinction between Compute Savings Plans and EC2 Instance Savings Plans.
* Cost Explorer, AWS Budgets, and Trusted Advisor and their different purposes.
* AWS Organizations and Service Control Policies (SCPs).
* SCP evaluation concepts and Deny-List vs Allow-List strategies.
* CloudFormation structure and required template sections.
* CloudFormation `DeletionPolicy` options, including `Snapshot` and `Retain`.
* Preventive, detective, and proactive governance guardrails.
* The differences between CloudWatch, CloudTrail, and AWS Config.
* IAM, KMS, security groups, NACLs, and VPC endpoint decision signals.
* Disaster recovery strategies and the relationship between RPO and RTO.
* Automated Python cost reporting.
* SQL indexing based on filtering, joining, and ordering requirements.
* The importance of measured evidence when evaluating SQL performance improvements.

## Week Activities

| Day   | Focus                                                                                           |
| ----- | ----------------------------------------------------------------------------------------------- |
| Day 1 | Cost Optimisation fundamentals and automated Python cost reporting                              |
| Day 2 | AWS Organizations, SCPs, multi-account governance, and IAM/SCP troubleshooting                  |
| Day 3 | CloudFormation, Control Tower, infrastructure monitoring, governance automation, and SQL tuning |
| Day 4 | Public Holiday                                                                                  |
| Day 5 | Mock Exam and Capstone Brief                                                                    |

## Practical Work

### Automated Cost Reporting

The `fintrust_migration` package was extended with a `cost_reporting.py` module for automated cost reporting.

Supporting Python files were also included for report generation and Lambda-based execution.

### SQL Performance Tuning

Three FinTrust transaction query scenarios were prepared for performance tuning:

1. Monthly transaction summary by customer
2. Transactions exceeding account credit limits
3. Audit logging for transactions associated with deleted accounts

Three indexes were prepared based on the filtering, joining, and ordering requirements of each query.

Before-and-after `EXPLAIN ANALYZE` statements were included in `sql/fintrust_views.sql`.

A PostgreSQL database environment was not available, so the queries were not executed and no performance measurements or execution-plan results were claimed.

### Governance Troubleshooting

The `lab_notes/w11d2_access_denied_scenarios.md` file documents access-denied troubleshooting scenarios related to AWS IAM and governance concepts.

### Self-Assessment

The Week 12 self-assessment used confidence ratings from 1–5 to identify knowledge gaps.

The main topics identified for further review were:

* Cost Explorer API vs Budgets vs Trusted Advisor
* SCP policy evaluation order
* SCP Deny-List vs Allow-List
* Preventive vs Detective vs Proactive guardrails
* CloudWatch vs CloudTrail vs Config
* Disaster recovery strategies and RPO/RTO

### Mock Exam Progress

Mock Exam 9 achieved a score of **60.49%**, an improvement of **6.74 percentage points** from Mock Exam 8's 53.75%.

The result was included in Portfolio Check-In #12 together with the identified review areas.

## Repository Contents

| File / Folder                                | Description                                                                |
| -------------------------------------------- | -------------------------------------------------------------------------- |
| `generate_report.py`                         | Python report-generation functionality                                     |
| `lambda_function.py`                         | Lambda function entry point for automated reporting                        |
| `portfolio_checkin_12`                       | Week 12 Portfolio Check-In                                                 |
| `README.md`                                  | Week 12 overview, activities, practical work, and outcomes                 |
| `sql_tuning_lab.md`                          | SQL tuning scenarios, index rationale, and testing status                  |
| `sql/fintrust_views.sql`                     | SQL tuning queries, indexes, and before/after `EXPLAIN ANALYZE` statements |
| `lab_notes/w11d2_access_denied_scenarios.md` | Access-denied and IAM/SCP troubleshooting scenarios                        |
| `fintrust_migration/cost_reporting.py`       | Automated cost-reporting functionality                                     |
| `fintrust_migration/__init__.py`             | Python package initialisation                                              |

## Key Takeaways

* AWS cost-management services have different purposes and need to be selected based on the question being asked.
* SCPs provide organisation-level permission guardrails rather than granting permissions themselves.
* CloudWatch, CloudTrail, and Config address different monitoring, logging, and configuration requirements.
* RPO and RTO are important decision signals when selecting disaster recovery strategies.
* SQL indexes should be selected according to the query's filtering, joining, and ordering patterns.
* Automated reporting can be structured into reusable Python modules and Lambda-based execution.
* Performance improvements should not be claimed without actual execution evidence.

## Week Deliverables

| Deliverable                          | Status                  |
| ------------------------------------ | ----------------------- |
| SQL Tuning Lab                       | ✅ Complete              |
| Week 12 Reflection + Self-Assessment | ✅ Complete              |
| Portfolio Check-In #12               | ✅ Complete              |

## FinTrust Architecture Extension

The Week 12 work extends FinTrust with cost reporting, governance, and performance considerations.

The `cost_reporting.py` module introduces automated cost-reporting functionality, while the SQL tuning work introduces indexing considerations for transaction queries.

The governance and troubleshooting work adds further consideration for access control and organisational policies.

Together, these additions extend FinTrust beyond its core transaction-processing functionality toward a more operationally aware cloud application.

## Outcome

Week 12 strengthened the connection between AWS cost optimisation, governance, monitoring, disaster recovery, automated reporting, and application performance.

The portfolio now includes automated cost-reporting functionality, documented SQL tuning work, governance troubleshooting scenarios, a structured self-assessment of certification knowledge gaps, and Portfolio Check-In #12.

Mock Exam 9 reached **60.49%**, while the self-assessment identified specific AWS topics for focused review before continuing with certification preparation.

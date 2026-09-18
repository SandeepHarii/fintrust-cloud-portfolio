# Week 11 - Well-Architected Framework, SQL & Python Engineering

## Overview

Week 11 focused on the AWS Well-Architected Framework, AWS architecture and governance, advanced SQL analysis, and Python engineering techniques.

The practical work extended the FinTrust Cloud portfolio with SQL window functions and CTEs for transaction analysis, Python decorators for retry and logging behaviour, and Python concurrency patterns for parallel data access.

## What I Learned This Week

* The AWS Well-Architected Framework and its six pillars.

* How Operational Excellence and Security principles apply to cloud workloads.

* How Reliability and Performance Efficiency influence AWS architecture decisions.

* How the Well-Architected Tool can be used to review workloads against AWS best practices.

* How Cost Optimisation and Sustainability influence cloud architecture and resource usage.

* How CloudFront can support dynamic content acceleration.

* How Trusted Advisor and Cost Explorer support AWS cost management and optimisation.

* The role of multi-account governance in managing AWS environments.

* How AWS Systems Manager and AWS Config can support resource auditing and configuration management.

* How SQL window functions use `OVER`, `PARTITION BY`, and `ORDER BY` for analytical calculations.

* How `ROW_NUMBER()`, `RANK()`, and `DENSE_RANK()` can be used to rank transaction data.

* How `LAG()` and `LEAD()` can compare values across rows.

* How Common Table Expressions can break complex SQL logic into multiple stages.

* How recursive CTEs can represent hierarchical relationships.

* How Python decorators can add reusable behaviour around existing functions.

* How `functools.wraps` preserves function metadata when using decorators.

* How retry decorators can use exponential backoff to handle temporary failures.

* How `ThreadPoolExecutor` and `asyncio` support concurrent I/O-bound workloads.

* How to select an appropriate concurrency model based on the type of workload.

## Week Activities

| Day   | AM                                                                                          | PM                                                         |
| ----- | ------------------------------------------------------------------------------------------- | ---------------------------------------------------------- |
| Day 1 | WAF Overview, Operational Excellence & Security Pillar                                      | SQL Window Functions                                       |
| Day 2 | Reliability, Performance Efficiency & the Well-Architected Tool                             | AWS SimuLearn: Highly Available Web Applications, SQL CTEs |
| Day 3 | Cost Optimisation & Sustainability, CloudFront Dynamic Content Acceleration Lab             | Python Decorators                                          |
| Day 4 | Trusted Advisor, Cost Explorer & Multi-Account Governance, Systems Manager & AWS Config Lab | Python Concurrency                                         |
| Day 5 | Mock                                                                                        | —                                                          |

## Practical Work

The SQL work was organised into two practice files covering analytical and multi-step transaction queries.

The `window_function_practice.sql` file includes:

* Window function syntax using `OVER`, `PARTITION BY`, and `ORDER BY`.

* Account-level totals and running totals.

* `ROW_NUMBER()`, `RANK()`, `DENSE_RANK()`, and `NTILE()`.

* Moving averages.

* `LAG()` and `LEAD()` comparisons.

* Month-over-month transaction analysis.

* Top-three transaction analysis.

* A comparison between `ROW_NUMBER()` and `DENSE_RANK()` for handling tied transaction amounts.

The `cte_practice.sql` file includes:

* Basic CTE syntax.

* Multiple chained CTEs.

* Monthly transaction analysis.

* Month-over-month growth calculations.

* Recursive CTEs for account hierarchies.

* CTEs combined with window functions.

* A multi-step anomaly detection query using multiple named CTEs.

The `decorators_practice.py` file includes:

* Timer decorators.

* Logging decorators.

* Decorators with arguments.

* Memoization.

* Stacking decorators.

* `functools.wraps`.

* Retry logic with exponential backoff.

* A FinTrust boto3 S3 API retry example.

The `concurrency_practice.py` file includes:

* `ThreadPoolExecutor`.

* `as_completed()`.

* `asyncio`.

* `asyncio.gather()`.

* Sequential and concurrent DynamoDB-style processing.

* Concurrency model selection examples.

* Sequential versus concurrent S3 object metadata fetching.

The AWS-dependent examples are documented as implementation examples or simulations where live AWS resources are not required.

## Repository Contents

| Path                               | Description                                                       |
| ---------------------------------- | ----------------------------------------------------------------- |
| `README.md`                        | Week 11 overview, activities, learning outcomes, and deliverables |
| `reflection.md`                    | Weekly learning reflection                                        |
| `sql/`                             | SQL window function and CTE practice                              |
| `sql/window_function_practice.sql` | SQL window functions and transaction analysis                     |
| `sql/cte_practice.sql`             | SQL CTEs, recursive queries, and anomaly detection                |
| `python/`                          | Python decorators and concurrency practice                        |
| `python/decorators_practice.py`    | Python decorators, retry logic, and boto3 example                 |
| `python/concurrency_practice.py`   | Threading, asyncio, and S3 metadata concurrency                   |

## Key Takeaways

The AWS Well-Architected Framework provides a structured approach for evaluating cloud architectures across Operational Excellence, Security, Reliability, Performance Efficiency, Cost Optimisation, and Sustainability.

The framework helps identify architectural considerations beyond simply selecting AWS services. FinTrust can use these pillars to evaluate areas such as security controls, availability, performance, cost, operational processes, and resource efficiency.

SQL window functions provide a way to perform analytical calculations while retaining individual transaction rows. This is useful for transaction ranking, running totals, previous-period comparisons, and identifying changes in account activity.

CTEs provide a structured way to divide complex SQL analysis into logical stages. Combining CTEs with window functions makes multi-step transaction analysis and anomaly detection easier to organise.

Python decorators provide reusable functionality such as logging, timing, validation, and retry handling without modifying the core function implementation.

Concurrency is particularly useful for I/O-bound workloads where operations spend time waiting for network, database, or file operations. `ThreadPoolExecutor` is useful for synchronous I/O such as boto3 calls, while `asyncio` is suited to high-concurrency asynchronous workloads.

## Week Deliverables

* `window_function_practice.sql` with top-three transaction analysis using `ROW_NUMBER()` and `DENSE_RANK()` comparison.

* `cte_practice.sql` with multi-step anomaly detection using at least three named CTEs.

* `decorators_practice.py` with a retry decorator using exponential backoff, `@wraps`, logging, and a boto3 API example.

* `concurrency_practice.py` with a parallel S3 object metadata fetch benchmark using `ThreadPoolExecutor`.

* Well-Architected Framework pillar mapping for FinTrust scenarios.

## FinTrust Architecture Extension

Week 11 extends the FinTrust architecture with Well-Architected Framework considerations and improved data-processing patterns.

The Well-Architected review provides a structured way to evaluate FinTrust across the six pillars, including security controls, operational processes, reliability, performance, cost management, and sustainability.

The SQL work adds transaction-analysis capabilities that can support FinTrust monitoring and anomaly detection. Window functions provide ranking and period-comparison capabilities, while chained CTEs provide a structured approach for identifying unusual transaction activity.

The Python work adds reusable retry handling for transient AWS API failures and concurrency patterns for I/O-bound operations. These techniques could support FinTrust data-processing workflows involving AWS APIs, S3 metadata, and other independent network operations.

## Outcome

Week 11 expanded the FinTrust portfolio from AWS service knowledge and migration architecture into Well-Architected architectural analysis, advanced SQL analytics, and Python engineering patterns.

The resulting work demonstrates an understanding of how AWS architectures can be evaluated against the Well-Architected Framework and how SQL and Python techniques can be applied to practical FinTrust data-processing scenarios.

The portfolio now includes analytical transaction queries, multi-step anomaly detection, reusable retry logic, boto3 integration patterns, and concurrent S3 metadata processing.
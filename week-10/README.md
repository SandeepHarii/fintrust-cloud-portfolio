# Week 10 - Migration, Data Transfer & Cost Optimisation

## Overview

Week 10 focused on AWS migration strategies, database and data transfer services, migration automation with Python, transfer cost optimisation, and infrastructure deployment concepts using AWS CloudFormation.

The practical work extended the FinTrust Cloud portfolio with a Python migration package covering migration classification, AWS Database Migration Service (DMS), AWS DataSync, S3 transfer helpers, and migration-related SQL views.

## What I Learned This Week

* The AWS 6Rs migration strategy and how to select an appropriate approach for different workloads.
* The differences between Rehost, Replatform, Refactor, Repurchase, Retire, and Retain.
* How AWS DMS supports controlled database migrations and replication.
* How AWS DataSync supports secure and automated large-scale data transfers.
* How S3 can be incorporated into migration and data movement workflows.
* How migration workloads can be classified and organised into migration waves.
* How Python can be used to support migration automation and monitoring.
* How transfer volume, network capacity, migration duration, and destination architecture affect migration costs.
* The role of AWS CloudFormation in infrastructure deployment and management.
* How monitoring and observability can support migration and microservice architectures.

## Week Activities

| Day   | AM                                                                         | PM                                     |
| ----- | -------------------------------------------------------------------------- | -------------------------------------- |
| Day 1 | 6Rs Migration Decision Framework, AWS Migration Strategies, Data Lakes Lab | Python Migration Scripts               |
| Day 2 | AWS DMS Architecture, AWS DMS Deep Dive, DMS Migration Lab                 | Python DMS Automation                  |
| Day 3 | AWS DataSync, Secure Data Transfer, X-Ray & CloudWatch Lab                 | Python DataSync Automation             |
| Day 4 | Transfer Cost Decision, Transfer Cost Optimisation                         | CloudFormation Lab, Python KC & SQL KC |
| Day 5 | Mock                                                                       | —                                      |

## Practical Work

The `fintrust_migration` package was developed to organise migration-related Python functionality into reusable modules.

The package includes:

* Migration workload classification.
* AWS DMS health-check functionality.
* AWS DataSync transfer monitoring.
* DataSync transfer throttling and scheduling.
* S3 synchronisation helpers.
* Migration-related SQL views.
* AWS session utilities.
* Migration wave and transfer audit support.

The architecture narrative documents the proposed migration strategy for FinTrust and explains how the AWS 6Rs framework, DMS, DataSync, physical transfer options, and transfer cost considerations fit together.

## Repository Contents

| Path                                  | Description                                                               |
| ------------------------------------- | ------------------------------------------------------------------------- |
| `README.md`                           | Week 10 overview, activities, learning outcomes, and deliverables         |
| `reflection.md`                       | Weekly learning reflection                                                |
| `architecture_narrative.md`           | Migration architecture strategy and rationale                             |
| `fintrust_migration/`                 | Python migration package                                                  |
| `fintrust_migration/scripts/`         | Migration classification, DMS monitoring, and DataSync automation scripts |
| `fintrust_migration/s3/`              | S3 migration and synchronisation helpers                                  |
| `fintrust_migration/rds/`             | DMS and database migration helpers                                        |
| `fintrust_migration/ec2/`             | Migration workload classification                                         |
| `fintrust_migration/utils/`           | Shared AWS session utilities                                              |
| `fintrust_migration/sql/`             | Migration and reporting SQL views                                         |
| `fintrust_migration/requirements.txt` | Python package dependency definition                                      |

## Key Takeaways

Migration is not simply the process of moving existing workloads into AWS. The migration strategy needs to consider the workload's business value, technical constraints, required level of change, operational complexity, and long-term cloud requirements.

The AWS 6Rs framework provides a structured way to make these decisions. DMS and DataSync then provide specialised services for database and data movement, while monitoring and cost analysis help control migration risk and operational expenditure.

Python can also be used to support migration activities through automation, classification, monitoring, and reusable AWS service helpers.

## Week Deliverables

* `fintrust_migration` Python package
* `architecture_narrative.md`
* Migration-related SQL views within the package

The requested standalone consolidated SQL file was not added because the SQL views are already organised within the Week 10 migration package.

## FinTrust Architecture Extension

Week 10 extends the FinTrust architecture with a migration layer focused on workload assessment, database migration, data transfer, monitoring, and cost optimisation.

The proposed approach uses the AWS 6Rs framework to determine the most suitable migration strategy for each workload. AWS DMS supports database migration, while AWS DataSync supports large-scale data movement. Migration monitoring and transfer-cost considerations provide additional controls around the migration process.

This creates a migration approach that can be applied alongside the existing FinTrust cloud architecture rather than treating migration as a separate activity.

## Outcome

Week 10 expanded the FinTrust portfolio from cloud application development into migration architecture and automation.

The resulting work demonstrates an understanding of how migration strategies are selected, how AWS services can support different migration scenarios, and how Python can be used to automate and support migration operations.
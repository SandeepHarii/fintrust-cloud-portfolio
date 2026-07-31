# Week 4 — AWS Database Services & Cloud Data Pipelines

## Overview

Week 4 focused on designing scalable, highly available database solutions on AWS and building modular Python data pipelines using the FinTrust banking case study. Morning (AM) sessions explored purpose-built AWS database services, high availability, analytics, and migration strategies, while afternoon (PM) sessions concentrated on Python packaging, custom exceptions, debugging, virtual environments, and data analysis with boto3 and pandas.

---

## What I Learned This Week

### AWS (AM Sessions)

* Explored Amazon RDS and managed relational database services.
* Configured Amazon RDS Multi-AZ deployments for high availability.
* Learnt how Read Replicas improve read scalability and disaster recovery.
* Compared automated backups and manual snapshots for database protection.
* Explored Amazon Aurora, Aurora Global Database, and Aurora Serverless v2.
* Built and queried Amazon DynamoDB tables.
* Learnt DynamoDB partition keys, sort keys, LSIs, GSIs, DAX, and Global Tables.
* Studied purpose-built AWS database services, including Amazon QLDB, Amazon Neptune, Amazon DocumentDB, Amazon Keyspaces, and Amazon ElastiCache.
* Explored Amazon Redshift, Amazon Athena, and Amazon EMR for analytics workloads.
* Learnt how AWS Database Migration Service (DMS) and AWS Schema Conversion Tool (SCT) support database migrations.
* Applied database selection principles to choose the most appropriate AWS service for different workloads.

### Python (PM Sessions)

* Created custom exception classes to improve application error handling.
* Applied debugging techniques to identify and resolve software defects.
* Refactored the ETL pipeline into a modular Python package.
* Organised Python code using modules and virtual environments.
* Used boto3 to interact with AWS services programmatically.
* Analysed transactional data using pandas DataFrames.
* Built a complete ETL pipeline that validates, stores, analyses, and reports on banking transaction data.

---

## Repository Contents

| File / Folder                         | Description                                                                                                     |
| ------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| `fintrust_pipeline/loader.py`         | Loads CSV transaction data, validates records, and prepares them for processing.                                |
| `fintrust_pipeline/database.py`       | Creates the SQLite database and inserts validated transaction records.                                          |
| `fintrust_pipeline/reporter.py`       | Generates summary reports from processed transaction data.                                                      |
| `analyse.py`                          | Uses pandas to analyse transaction data with DataFrames, `groupby()`, and enriched exports.                     |
| `requirements.txt`                    | Project dependencies with pinned versions for boto3 and pandas.                                                 |
| `diagrams/db-architecture-diagram.md` | Seven-layer FinTrust database architecture documentation and design.                                            |
| `weekly-reflection.md`                | Reflection covering AWS database selection, ETL architecture, Python packaging, and Week 5 networking concepts. |

---

## Key Takeaways

* Designed a seven-layer AWS database architecture using purpose-built database services.
* Understood the differences between Amazon RDS Multi-AZ, Read Replicas, and Amazon Aurora Global Database.
* Built a modular Python ETL pipeline using packages, boto3, and pandas.
* Applied AWS database selection principles based on workload characteristics, scalability, availability, and compliance requirements.
* Explored database migration, analytics, and caching services to support modern cloud-native applications.

---

## Outcome

By the end of Week 4, I understood how AWS purpose-built database services address different application requirements and how they work together within a cloud architecture. I also transformed a single-file ETL application into a modular Python package, gaining practical experience with cloud automation, data processing, debugging, and dependency management. These skills strengthened my understanding of designing secure, scalable, and maintainable data platforms for real-world financial applications.
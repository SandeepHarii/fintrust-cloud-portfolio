# Week 8 — Analytics, Streaming & Machine Learning

## Overview

Week 8 expanded the FinTrust Cloud Portfolio beyond core infrastructure and security into analytics, real-time streaming, data engineering, machine learning, identity verification, and data privacy.

The week covered Amazon Athena, AWS Glue, Amazon Kinesis, Amazon OpenSearch, Amazon EMR, Amazon QuickSight, Amazon SageMaker, Amazon Rekognition, and Amazon Comprehend.

The practical portfolio work focused primarily on Python implementations, AWS service integration patterns, data engineering workflows, and architecture design. AWS API calls were retained in the scripts but commented out where AWS resources and permissions had not been provisioned.

This approach keeps the code representative of the intended AWS integrations without claiming that resources were deployed when deployment evidence does not exist.

## What I Learned This Week

* Querying data with Amazon Athena and understanding the AWS Glue Data Catalog.
* Working with asynchronous AWS APIs and polling long-running operations.
* Building real-time data pipelines with Amazon Kinesis Data Streams.
* Selecting partition keys and balancing ordering requirements against shard distribution.
* Understanding Amazon OpenSearch for security-event analysis and visualisation.
* Understanding Amazon EMR for large-scale data processing.
* Using Amazon QuickSight for analytics dashboards.
* Comparing Pandas-based analysis with Athena-based serverless analytics.
* Working with CSV, Parquet, partitioning, and S3-based data workflows.
* Understanding machine learning service selection with Amazon SageMaker.
* Using Amazon Rekognition for facial comparison and identity verification.
* Using Amazon Comprehend for PII detection, redaction, and sentiment analysis.
* Designing Lambda-based event-driven architectures with API Gateway, Comprehend, and SQS.
* Applying least-privilege IAM principles to Lambda workloads.

## Week Activities

| Day       | Morning Session                                                                                       | Afternoon Session                                                                                                             |
| --------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| **Day 1** | Week 7 Mock Exam, Analytics Data Lake Architecture, Analytics Foundations, Amazon Athena and AWS Glue | Querying Athena and Glue with Python, three-tier architecture security, AWS Root Account and IAM                              |
| **Day 2** | Kinesis Streaming and OpenSearch Architecture, Amazon Kinesis and OpenSearch                          | Real-time data pipelines with Kinesis and OpenSearch                                                                          |
| **Day 3** | Amazon EMR and QuickSight                                                                             | Event-driven architecture with API Gateway, EventBridge and Lambda, Data Engineering with Python using Pandas, Parquet and S3 |
| **Day 4** | ML Service Selection and Integration Patterns, SageMaker, Rekognition and Comprehend, Quiz            | AI pipelines with Rekognition and Comprehend, AWS SimuLearn Container Services Lab, AWS SimuLearn Federated Queries Lab       |
| **Day 5** | Mock Exam and exam preparation                                                                        | —                                                                                                                             |

## Practical Work

During the week, the portfolio work focused on:

* Athena and Glue querying with Python.
* Kinesis producer and consumer workflows.
* Kinesis partition-key strategy using `account_id`.
* ETL and data transformation with Pandas.
* Parquet and S3 data workflows.
* Rekognition facial comparison workflows.
* Comprehend PII detection and sentiment analysis workflows.
* Lambda-based support-ticket processing architecture.
* FinTrust analytics and machine learning architecture.

The Python scripts retain commented AWS API calls to demonstrate the intended service integrations while avoiding unnecessary AWS resource provisioning and associated costs.

## Repository Contents

| Path                     | Description                                                                     |
| ------------------------ | ------------------------------------------------------------------------------- |
| [`docs/`](./docs/)       | Week 8 reflections and FinTrust architecture documentation.                     |
| [`scripts/`](./scripts/) | Python implementations covering analytics, streaming, ETL, and AI/ML workflows. |

## Key Takeaways

### Analytics

Amazon Athena provides serverless SQL analytics over data stored in Amazon S3, while AWS Glue provides cataloguing capabilities for analytics datasets.

Pandas is better suited to local analysis, prototyping, exploratory work, and feature engineering, while Athena is more appropriate for querying large datasets in S3 without managing analytics infrastructure.

These tools can complement each other within the same data workflow rather than being direct replacements for one another.

### Streaming

Amazon Kinesis Data Streams supports real-time transaction processing.

Using `account_id` as the partition key preserves ordering for transactions belonging to the same account because records with the same partition key are routed to the same shard.

The trade-off is that a high-volume account can create uneven shard utilisation. A more distributed partitioning strategy could improve load distribution, but may sacrifice the per-account ordering guarantee.

### Data Engineering

Parquet provides columnar storage that is well suited to analytical workloads. Combined with appropriate partitioning and query design, it can reduce the amount of data Athena needs to scan and improve analytical query efficiency.

Pandas can be used to transform, validate, and prepare datasets before they are stored for larger-scale cloud analytics.

### Machine Learning & AI

Amazon SageMaker can host machine learning models for use cases such as fraud detection.

Amazon Rekognition can support identity verification through facial comparison.

Amazon Comprehend can detect PII, support redaction workflows, and analyse the sentiment of customer text.

These services were evaluated and incorporated into the FinTrust target architecture. The portfolio does not claim that AWS resources were deployed where deployment evidence does not exist.

## Week Deliverables

| Deliverable                                                  | Status                          |
| ------------------------------------------------------------ | ------------------------------- |
| Athena successful query screenshot                           | Pending AWS access/provisioning |
| Kinesis producer Python script and partition-key explanation | **Completed**                   |
| OpenSearch security-log dashboard screenshot                 | Pending AWS access/provisioning |
| EMR cluster configuration screenshot                         | Pending AWS access/provisioning |
| QuickSight dashboard with completed SPICE dataset            | Pending AWS access/provisioning |
| SageMaker fraud endpoint in `InService` state                | Pending AWS access/provisioning |
| Rekognition CompareFaces API output                          | Partially completed             |
| Comprehend PII detection and redaction output                | Partially completed             |
| FinTrust Week 8 narrative extension                          | **Completed**                   |
| Meaningful Week 8 GitHub commit history                      | **Completed**                   |

AWS resources were not provisioned for the outstanding console-based deliverables. The portfolio therefore distinguishes between Python implementations, architecture designs, simulated or commented AWS integrations, and AWS resources that were actually configured.

## FinTrust Architecture Extension

Week 8 extends the FinTrust platform with an analytics and AI layer.

Real-time transaction events can enter through Amazon Kinesis Data Streams, with `account_id` used as the partition key to maintain per-account ordering.

Curated transaction data can be stored in Amazon S3 and queried through Amazon Athena, with AWS Glue providing catalog information.

Amazon EMR can support large-scale processing and feature engineering, while Amazon QuickSight can provide analytics dashboards.

Amazon SageMaker can support real-time fraud-risk predictions.

Amazon Rekognition can support customer identity verification, while Amazon Comprehend can detect and redact PII in support-ticket data.

Amazon OpenSearch can support security-event analysis and visualisation.

Together, these services extend FinTrust beyond transaction processing into analytics, fraud detection, compliance, identity verification, and operational intelligence.

## Outcome

Week 8 expanded the FinTrust portfolio from core cloud infrastructure and security into analytics, streaming, data engineering, and machine learning.

The week produced Python implementations covering Athena, Glue, Kinesis, ETL, Pandas, Rekognition, and Comprehend workflows, together with architecture reflections and the Week 8 FinTrust narrative extension.

The work also strengthened my understanding of architectural trade-offs, including synchronous versus asynchronous processing, ordering versus shard distribution, local data processing versus serverless analytics, and selecting specialised AI services based on business requirements.

AWS console evidence remains pending where actual resource provisioning was not performed. This keeps the portfolio technically honest while still demonstrating how the services would fit into the FinTrust architecture.
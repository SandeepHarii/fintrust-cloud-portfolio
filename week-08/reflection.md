# Week 8 — Weekly Reflection

## Overview

Week 8 expanded my understanding of cloud architecture beyond core infrastructure and security into analytics, real-time data processing, data engineering, and machine learning.

The week covered services including Amazon Athena, AWS Glue, Amazon Kinesis, Amazon OpenSearch, Amazon EMR, Amazon QuickSight, Amazon SageMaker, Amazon Rekognition, and Amazon Comprehend. I also worked with Python to explore how these services could fit into the FinTrust platform.

One of the biggest lessons from the week was that cloud architecture is not just about knowing what each AWS service does. It is about understanding how services work together and selecting the right tool for a specific requirement.

## Analytics and Data Processing

I learned how Athena and Glue can be used together to analyse data stored in Amazon S3. Athena provides serverless SQL querying, while Glue provides the Data Catalog that helps organise and describe datasets.

I also compared Athena with Pandas. Pandas is useful for local analysis, experimentation, data transformation, and feature engineering, while Athena is better suited to querying large datasets in S3 without managing servers.

This helped me understand that these tools are not necessarily alternatives. They can form part of the same data workflow.

For FinTrust, Pandas could be used to prepare and validate transaction data, while S3, Glue, and Athena could support larger-scale analytics, compliance reporting, and historical investigations.

## Asynchronous Processing

Another important lesson was understanding the difference between synchronous and asynchronous operations.

Athena queries are asynchronous because a query may take time to complete. Instead of keeping a connection open while waiting for the result, the API returns a `QueryExecutionId`, which can then be used to monitor the query status.

I also learned that the same concept applies to services such as EMR, where cluster provisioning happens in the background while the client monitors the cluster state.

This showed me why asynchronous processing is important for long-running cloud operations.

## Real-Time Streaming

Kinesis introduced another side of data processing, real-time streaming.

For FinTrust, I used `account_id` as the partition key. This allows transactions for the same customer to be routed consistently and preserves ordering for that account.

However, I also learned that this design has a trade-off. A customer generating a very high number of transactions could create a hot shard while other shards remain underutilised.

Using a more distributed key could improve load distribution, but it could also sacrifice the ordering guarantee required for transactions belonging to the same account.

This was a useful architecture lesson because there is not always one perfect design. The correct choice depends on the business requirement being prioritised.

## Data Engineering

The data engineering work introduced me to the relationship between Pandas, CSV data, Parquet, S3, and Athena.

I learned why columnar formats such as Parquet are useful for analytics workloads and how partitioning can reduce the amount of data Athena needs to scan.

This connected the Python work with the AWS architecture. Instead of thinking about Python and AWS as separate areas, I could see how Python can prepare and transform data before it enters a cloud-based analytics pipeline.

## AI and Machine Learning

Week 8 also introduced several AWS AI and machine learning services.

SageMaker can be used to host machine learning models for use cases such as fraud detection. Rekognition can support identity verification through facial comparison, while Comprehend can analyse text, detect PII, and support privacy-focused workflows.

For FinTrust, these services provide different capabilities rather than solving the same problem.

A fraud model could generate transaction risk predictions, Rekognition could support customer identity verification, and Comprehend could protect sensitive information contained in support tickets.

This helped me understand the importance of service selection. The goal is not to use as many AWS services as possible, but to select services that solve specific business problems.

## Lambda, APIs and IAM

The Lambda architecture work showed how API Gateway, Lambda, Comprehend, SQS, and CloudWatch could be combined into an event-driven support-ticket workflow.

I also considered the IAM permissions required by the Lambda function.

The main security lesson was least privilege. A Lambda function should only receive the permissions required to perform its job, such as detecting PII, analysing sentiment, sending messages to specific SQS queues, and writing logs.

This reinforced the security principles covered earlier in the programme and showed how IAM decisions become part of application architecture.

## FinTrust Architecture

Week 8 significantly expanded the FinTrust architecture.

The platform can now be viewed as having several connected capabilities:

**Real-time ingestion → Data processing → Analytics → Machine Learning → Identity & Privacy → Security Monitoring**

Kinesis can ingest transaction events in real time. S3, Glue, and Athena can support analytics. EMR can handle larger-scale processing and feature engineering. QuickSight can present analytical results.

SageMaker can support fraud prediction, Rekognition can support identity verification, Comprehend can protect sensitive text data, and OpenSearch can support security monitoring and visualisation.

These additions make FinTrust more than a basic banking application. They demonstrate how cloud services can be combined to support operational processing, analytics, security, compliance, and intelligent decision-making.

## Overall Reflection

The biggest takeaway from Week 8 was understanding how different data and AI services fit into a larger architecture.

Earlier weeks focused heavily on networking, security, and core cloud infrastructure. Week 8 showed what can happen after that foundation is in place.

I also became more aware of architectural trade-offs. Examples include synchronous versus asynchronous processing, ordering versus shard distribution in Kinesis, local Pandas processing versus serverless Athena analytics, and selecting specialised AI services based on the actual problem.

Most importantly, I learned that knowing an AWS service exists is not enough. I need to understand **why I would use it, what problem it solves, what trade-offs it introduces, and how it fits with the rest of the architecture**.

The Week 8 work therefore strengthened both my technical understanding and my ability to think about FinTrust as an integrated cloud platform rather than a collection of individual services.
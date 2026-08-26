# Week 8 Analytics and Machine Learning Enhancements

The FinTrust platform has been extended with analytics, machine learning, and security services to improve fraud detection, reporting, and compliance.

## Data Ingestion

Amazon Kinesis Data Streams receives real-time transaction events from banking applications. The account_id field is used as the partition key to preserve transaction ordering for individual customers.

## Analytics

Amazon Athena provides serverless SQL analytics on curated transaction datasets stored in Amazon S3. Analysts can use Athena to investigate transaction trends and identify suspicious activity.

Amazon QuickSight connects to analytics datasets and presents dashboards showing transaction volumes, fraud rates, and operational metrics.

## Big Data Processing

Amazon EMR enables large-scale Spark processing for transaction analysis and feature engineering. Processed data can be used for reporting and machine learning workloads.

## Machine Learning

Amazon SageMaker hosts fraud detection models that analyse transaction patterns and generate risk predictions in real time.

## Identity Verification

Amazon Rekognition supports customer identity verification by comparing facial images during onboarding and authentication workflows.

## Compliance and Privacy

Amazon Comprehend helps detect and redact personally identifiable information (PII) from customer support tickets and other text-based records.

## Security Monitoring

Amazon OpenSearch stores and analyses security events, making it possible to monitor suspicious activity and visualise risk indicators through dashboards.

## Platform Overview

The FinTrust architecture combines streaming, analytics, machine learning, security monitoring, and compliance services to provide a modern cloud-native banking platform.
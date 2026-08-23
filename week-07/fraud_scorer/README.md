# FinTrust Lambda Fraud Scorer

## Overview

The FinTrust Fraud Scorer is an AWS Lambda function designed to process payment transactions from an Amazon SQS FIFO queue and calculate a fraud risk score.

Transactions that meet or exceed the configured risk threshold are published to an Amazon SNS topic for downstream compliance or notification services.

### Pipeline

```text
Flask API
    ↓
SQS FIFO
payment-events
    ↓
Lambda
fintrust-fraud-scorer
    ↓
SNS
transaction-alerts
    ↓
Compliance / Email
```

## Purpose

The Lambda function provides an event-driven fraud scoring component for the FinTrust transaction processing pipeline.

It:

1. Receives transaction events from SQS.
2. Extracts the transaction data.
3. Calculates a fraud risk score.
4. Logs the transaction and calculated score.
5. Publishes high-risk transactions to SNS.
6. Returns a successful processing response.

## Fraud Scoring Logic

The risk score starts at `0` and increases based on transaction characteristics.

| Condition                                                    | Score |
| ------------------------------------------------------------ | ----: |
| Amount > R50,000                                             |   +40 |
| Amount > R10,000                                             |   +20 |
| Amount > R1,000                                              |    +5 |
| Currency is not ZAR                                          |   +20 |
| Description contains `crypto`, `wire`, `urgent`, or `casino` |   +15 |

The final score is capped at `100`.

### Example

A transaction containing:

```json
{
  "amount": 75000,
  "currency": "USD",
  "description": "crypto wire transfer urgent"
}
```

receives:

```text
Amount > R50,000      +40
Non-ZAR currency      +20
Risk keyword          +15
--------------------------
Total                  75
```

With the default threshold of `75`, this transaction is classified as high risk and an SNS alert is published.

## SQS Event

The Lambda expects transactions to be delivered through an SQS event.

Example transaction:

```json
{
  "id": "TXN-001",
  "account_id": "ACC-999",
  "amount": 75000,
  "currency": "USD",
  "description": "crypto wire transfer urgent"
}
```

The transaction is expected inside the SQS record body:

```json
{
  "Records": [
    {
      "body": "{\"id\":\"TXN-001\",\"account_id\":\"ACC-999\",\"amount\":75000,\"currency\":\"USD\",\"description\":\"crypto wire transfer urgent\"}"
    }
  ]
}
```

The Lambda parses the `body` field and passes the transaction to the scoring function.

## SNS Alerts

When the calculated score is greater than or equal to the configured threshold, the Lambda publishes a message to the configured SNS topic.

Example alert:

```json
{
  "transaction_id": "TXN-001",
  "account_id": "ACC-999",
  "amount": 75000,
  "currency": "USD",
  "risk_score": 75.0,
  "reason": "Score exceeds threshold"
}
```

The SNS message also includes the following message attribute:

```text
risk_level = HIGH
```

## Configuration

The Lambda uses environment variables for configuration.

| Variable              | Description                                    | Default  |
| --------------------- | ---------------------------------------------- | -------- |
| `ALERT_TOPIC_ARN`     | ARN of the SNS topic used for high-risk alerts | Required |
| `HIGH_RISK_THRESHOLD` | Minimum score required to trigger an alert     | `75.0`   |

AWS credentials are not stored in the source code. When deployed to Lambda, Boto3 uses the credentials provided through the Lambda execution role.

## AWS Services

This component is designed to use the following AWS services:

* **AWS Lambda** — runs the fraud scoring function.
* **Amazon SQS FIFO** — provides the transaction event queue.
* **Amazon SNS** — distributes high-risk transaction alerts.
* **Amazon CloudWatch** — stores Lambda execution logs.
* **AWS IAM** — provides permissions to access AWS services.

## Project Structure

```text
fraud_scorer/
└── lambda_function.py
```

## Local Testing

The scoring logic can be tested locally without deploying the Lambda function.

A mock SQS event can be passed to `lambda_handler()` containing a transaction in the same format expected from Amazon SQS.

The scoring logic should verify:

* Large transactions receive additional risk points.
* Non-ZAR transactions receive additional risk points.
* Risk keywords increase the score.
* Scores cannot exceed `100`.
* Transactions meeting the configured threshold trigger the SNS publishing logic.

Actual SNS publishing requires AWS credentials and an available SNS topic.

## AWS Deployment

The intended AWS deployment consists of:

```text
SQS FIFO Queue
        ↓
Lambda Event Source Mapping
        ↓
FinTrust Fraud Scorer
        ↓
SNS Topic
```

The Lambda requires an IAM execution role with permissions to:

* Write logs to CloudWatch.
* Receive messages from the SQS queue.
* Delete successfully processed SQS messages.
* Publish high-risk alerts to the SNS topic.

The production implementation should follow the principle of least privilege rather than granting broad service permissions.

## Current Status

The Lambda fraud scorer code has been implemented for the FinTrust event-driven transaction pipeline.

The AWS deployment and end-to-end integration are currently pending AWS account access.

Once AWS access is available, the remaining steps are:

1. Create the SQS FIFO queue.
2. Create the SNS alert topic.
3. Create the Lambda function.
4. Configure the Lambda environment variables.
5. Configure the IAM execution role.
6. Create the SQS event source mapping.
7. Test the pipeline using the Flask transaction API.
8. Verify Lambda execution through CloudWatch.
9. Verify high-risk alerts through SNS.

## Deliverable

**Lambda fraud scorer function committed to GitHub**

Status: **Code implementation ready. AWS deployment pending account access.**
# FinTrust Narrative, Week 7 Additions

## Week 7 Overview

In Week 7, FinTrust was extended from a primarily API-driven application into a more event-driven transaction processing architecture.

The main goal was to separate transaction submission from fraud analysis. Instead of having the Flask API perform fraud scoring directly, transactions can be placed onto an Amazon SQS FIFO queue and processed asynchronously by an AWS Lambda function.

High-risk transactions can then be sent to Amazon SNS for notification and downstream compliance processing.

The resulting flow is:

```text
Flask API
    ↓
SQS FIFO
payment-events
    ↓
Lambda
fraud-scorer
    ↓
SNS
transaction-alerts
    ↓
Compliance / Notification
```

This approach reduces the dependency between the transaction API and the fraud detection process.

## New Services Added

### Amazon SQS FIFO

Amazon Simple Queue Service was introduced as the transaction event queue.

The Flask API publishes payment events to the `fintrust-payment-events.fifo` queue instead of requiring the fraud scoring process to happen immediately.

A FIFO queue was selected because transaction processing may require messages from the same account to remain in order. The implementation uses the account ID as the message group ID.

SQS also provides buffering between the API and the fraud scoring system. If the scorer is temporarily unavailable, transactions can remain in the queue instead of being lost or forcing the API to wait.

### AWS Lambda

AWS Lambda was introduced as the fraud scoring component.

The `fintrust-fraud-scorer` function reads transactions from SQS and calculates a fraud risk score based on transaction characteristics such as:

* Transaction amount
* Currency
* Risk-related description keywords

Transactions that reach the configured high-risk threshold are passed to SNS.

Lambda was chosen because fraud scoring is an event-driven workload. The function only needs to run when transactions are available, removing the need for a continuously running application server dedicated to fraud scoring.

### Amazon SNS

Amazon Simple Notification Service was added for high-risk transaction alerts.

When the Lambda fraud scorer identifies a transaction that meets or exceeds the configured risk threshold, it publishes an alert to the `fintrust-transaction-alerts` SNS topic.

SNS allows multiple downstream consumers to receive the same alert. For example, a compliance Lambda, email notification system, or another monitoring service could subscribe to the topic.

This keeps the fraud scorer separate from the systems responsible for handling the alert.

### Boto3

Boto3 was introduced as the AWS SDK used by the Python components.

It allows the application to interact with AWS services programmatically.

In Week 7, Boto3 is used to:

* Send transaction messages to SQS.
* Publish high-risk alerts to SNS.

The Lambda function uses the AWS execution role for authentication rather than storing AWS access keys in the source code.

### IAM

AWS Identity and Access Management is used to control access between the services.

The Lambda execution role is intended to provide only the permissions required by the fraud scorer, including access to:

* CloudWatch Logs
* SQS messages
* SNS publishing

This follows the principle of least privilege and avoids giving the Lambda unnecessary access to other AWS resources.

## Why the Architecture Changed

The main architectural change in Week 7 is the move toward asynchronous, event-driven processing.

Previously, the transaction API was responsible for accepting transaction data and performing its application logic directly.

With the Week 7 architecture, the responsibilities are separated:

```text
Flask API
Accept transaction
       ↓
SQS
Store transaction event
       ↓
Lambda
Calculate fraud score
       ↓
SNS
Distribute high-risk alert
```

This separation provides several advantages.

### Decoupling

The Flask API does not need to directly communicate with the fraud scoring logic.

The API can submit the transaction to SQS and continue processing while the fraud scorer handles the event separately.

### Scalability

Lambda can process transactions as messages arrive without requiring a dedicated fraud scoring server to run continuously.

SQS also provides a buffer when transaction volume increases.

### Reliability

If the fraud scorer cannot immediately process a transaction, the event remains in SQS for later processing.

This is more resilient than relying on a synchronous request between the API and fraud scoring service.

### Extensibility

SNS creates a clean separation between detecting fraud and responding to fraud.

Additional consumers can subscribe to the SNS topic without changing the fraud scoring Lambda.

For example:

```text
                 ┌── Compliance Lambda
                 │
Lambda Scorer → SNS ── Email Notification
                 │
                 └── Monitoring System
```

This allows the FinTrust platform to grow without tightly coupling the fraud scorer to every downstream system.

## Example Transaction

A high-risk transaction might look like:

```json
{
  "id": "TXN-001",
  "account_id": "ACC-999",
  "amount": 75000,
  "currency": "USD",
  "description": "crypto wire transfer urgent"
}
```

The transaction is submitted through the Flask API and published to SQS.

The Lambda fraud scorer then calculates the risk:

```text
Amount > R50,000      +40
Non-ZAR currency      +20
Risk keyword          +15
--------------------------
Risk score              75
```

Because the score reaches the configured threshold of `75`, the Lambda publishes a high-risk alert to SNS.

This creates an automated path from transaction submission to fraud detection and alerting without requiring the API to handle the entire process synchronously.

## Week 7 Architectural Outcome

Week 7 moves FinTrust closer to a production-style cloud architecture by introducing asynchronous processing and event-driven communication.

The addition of SQS, Lambda and SNS creates clear boundaries between:

* Transaction submission
* Event queuing
* Fraud analysis
* Alert distribution

The architecture is also designed to support future improvements such as a dead-letter queue, more advanced fraud scoring, additional SNS subscribers, and improved monitoring.

The AWS implementation is currently pending AWS account access. The application and Lambda code can still be developed and tested locally, with the AWS infrastructure to be deployed once account access is available.

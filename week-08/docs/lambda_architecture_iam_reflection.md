# Reflection: Lambda Architecture and IAM

## Architecture Overview

The FinTrust support ticket processing workflow can be triggered through Amazon API Gateway.

Customer support applications submit tickets through an API endpoint. API Gateway invokes a Lambda function that processes the ticket.

The Lambda function performs the following actions:

1. Receives the support ticket.
2. Detects and redacts PII using Amazon Comprehend.
3. Analyses sentiment using Amazon Comprehend.
4. Routes high-priority tickets to an urgent SQS queue.
5. Routes normal tickets to a standard SQS queue.
6. Returns a processing summary.

### Architecture Flow

```text
API Gateway
    ↓
AWS Lambda
    ↓
Amazon Comprehend
    ↓
Amazon SQS
```

## IAM Permissions Required

### Amazon Comprehend

```text
comprehend:DetectPIIEntities
comprehend:DetectSentiment
```

#### Resource Scope

```text
*
```

These actions are used to identify PII and analyse customer sentiment.

### Amazon SQS

```text
sqs:SendMessage
```

#### Resource Scope

```text
arn:aws:sqs:af-south-1:ACCOUNT_ID:fintrust-support-urgent
arn:aws:sqs:af-south-1:ACCOUNT_ID:fintrust-support-standard
```

These permissions allow Lambda to place messages into the appropriate support queues.

### Amazon CloudWatch Logs

```text
logs:CreateLogGroup
logs:CreateLogStream
logs:PutLogEvents
```

#### Resource Scope

```text
arn:aws:logs:af-south-1:ACCOUNT_ID:*
```

These permissions enable Lambda logging and monitoring.

## Security Considerations

The Lambda function should follow the principle of least privilege and only be granted permissions required for Comprehend analysis, SQS message delivery, and logging. Broad wildcard permissions should be avoided wherever possible.
# Week 7 — Event-Driven Architecture, APIs & Serverless

## Overview

Week 7 focused on event-driven architecture, APIs, serverless computing, infrastructure as code, disaster recovery, monitoring, and AWS security.

The week covered Amazon SQS, Amazon EventBridge, AWS Step Functions, Amazon SWF, API Gateway, AWS AppSync, AWS Lambda, AWS CloudFormation, AWS Systems Manager, and disaster recovery strategies.

The practical FinTrust work included building Python APIs with Flask and FastAPI, exploring Python Lambda handlers and event processing, and designing an event-driven transaction scoring pipeline using Boto3, SQS, Lambda and SNS.

Day 3 was spent attending the AWS Summit, so no regular training sessions were completed that day.

AWS account access was not yet available for the FinTrust AWS deployment activities. As a result, AWS console evidence such as the SQS queue, SNS subscribers and CloudWatch Lambda logs could not be captured during the week. The application code, Lambda fraud scoring logic, architecture diagram and documentation were developed independently of the AWS environment.

---

## What I Learned This Week

### AWS (AM Sessions)

* Completed the JAWS Lab on monitoring infrastructure.

* Worked with AWS CloudTrail and explored its role in recording AWS API activity for monitoring, auditing and investigation.

* Explored messaging, event-driven architecture and workflow patterns.

* Learnt how Amazon SQS provides asynchronous messaging between application components.

* Explored SQS visibility timeouts and how they control the period during which a received message remains hidden from other consumers.

* Learnt the difference between standard and FIFO SQS queues.

* Explored Dead-Letter Queues (DLQs) for handling messages that repeatedly fail processing.

* Studied fan-out patterns using Amazon SNS and SQS.

* Explored Amazon EventBridge event patterns and event routing.

* Compared AWS Step Functions Standard and Express workflows and their appropriate use cases.

* Explored Amazon SWF and the types of long-running workflows where it may still be appropriate.

* Explored Amazon API Gateway and its role in exposing APIs to applications and clients.

* Compared API Gateway HTTP APIs, REST APIs and WebSocket APIs.

* Learnt how API Gateway authorizers can control access to APIs.

* Explored API Gateway caching and its role in reducing backend requests.

* Explored AWS AppSync and its use of GraphQL APIs.

* Learnt how AppSync can support real-time subscriptions for applications that require live updates.

* Explored AWS Lambda execution concepts including handlers, events and context.

* Learnt how Lambda cold starts can affect execution latency.

* Explored Provisioned Concurrency as a way to reduce cold-start latency for latency-sensitive workloads.

* Explored Lambda memory and CPU allocation and how increasing memory also increases available CPU resources.

* Learnt how Lambda can integrate with VPC resources when private network access is required.

* Explored Lambda Layers for sharing dependencies and common code between functions.

* Studied Lambda failure handling and Dead-Letter Queue configuration.

* Explored AWS CloudFormation as an Infrastructure as Code service for defining and managing AWS resources.

* Learnt the mandatory sections of a CloudFormation template.

* Explored CloudFormation Change Sets for reviewing proposed infrastructure changes before execution.

* Compared Nested Stacks and StackSets and their different use cases.

* Explored CloudFormation `DeletionPolicy` and how it can control what happens to resources when stacks are deleted or updated.

* Explored the Strangler Fig pattern for gradually replacing or modernising existing applications.

* Studied disaster recovery strategies and how recovery requirements influence AWS architecture.

* Completed the JAWS Lab on AWS Systems Manager.

### Python & SQL (PM Sessions)

* Built Python APIs using Flask and FastAPI.

* Explored the differences between Flask and FastAPI when building Python-based APIs.

* Learnt how Python applications can interact with AWS services using Boto3.

* Explored Python in AWS Lambda, including Lambda handlers, events and context.

* Built the fraud scoring logic for the FinTrust event-driven transaction pipeline.

* Designed the transaction flow from the Flask API through SQS, Lambda and SNS.

* Used JSON transaction data as the event payload for the fraud scoring process.

* Applied environment variables for configuration such as the SNS topic ARN and fraud-risk threshold.

* Continued SQL development through the programme's practical exercises.

---

## Repository Contents

| File / Folder                                                          | Description                                                                                             |
| ---------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| [`fraud_scorer/`](./fraud_scorer/)                                     | Lambda fraud scorer implementation for processing transaction events and calculating fraud risk scores. |
| [`fraud_scorer/lambda_function.py`](./fraud_scorer/lambda_function.py) | Python Lambda handler and fraud scoring logic.                                                          |
| [`fraud_scorer/README.md`](./fraud_scorer/README.md)                   | Documentation for the Lambda fraud scorer, including scoring rules, configuration and AWS integration.  |
| [`architecture/`](./architecture/)                                     | Week 7 event-driven architecture diagram showing the Flask → SQS → Lambda → SNS pipeline.               |
| [`narrative.md`](./narrative.md)                                       | Extended FinTrust narrative describing the Week 7 services and why they were introduced.                |

---

## Key Takeaways

* Messaging services allow application components to communicate asynchronously without being tightly coupled.

* SQS visibility timeouts help control message processing and retry behaviour.

* FIFO queues are useful when message ordering is important.

* Dead-Letter Queues provide a mechanism for isolating messages that repeatedly fail processing.

* SNS and SQS can be combined to implement fan-out architectures where one event needs to reach multiple consumers.

* EventBridge provides event-based routing using event patterns and rules.

* Step Functions provides managed orchestration for workflows, with Standard and Express workflows designed for different workload requirements.

* API Gateway provides different API options depending on the application requirement, including HTTP, REST and WebSocket APIs.

* API Gateway authorizers can be used to control access to APIs.

* AppSync provides GraphQL capabilities and supports real-time subscriptions.

* Lambda execution behaviour is affected by cold starts, memory allocation, networking and dependencies.

* Provisioned Concurrency can be used when reducing Lambda cold-start latency is important.

* Lambda Layers can help share common dependencies between functions.

* CloudFormation allows infrastructure to be defined and managed as code.

* Change Sets provide a safer way to review infrastructure changes before applying them.

* Nested Stacks and StackSets solve different infrastructure management requirements.

* `DeletionPolicy` can help protect important resources from unintended deletion.

* The Strangler Fig pattern provides a controlled approach for gradually replacing legacy application components.

* Disaster recovery strategies should be selected according to business requirements such as recovery time and recovery point objectives.

* AWS Systems Manager provides tools for securely managing AWS resources and instances.

* CloudTrail provides an important source of evidence for AWS activity and auditing.

* Event-driven architecture allows FinTrust to separate transaction submission, processing and notification into independent components.

---

## Outcome

By the end of Week 7, I developed a broader understanding of how AWS services can be combined to build event-driven, serverless and resilient applications.

The week covered messaging and workflow services, API technologies, Lambda architecture, Infrastructure as Code and disaster recovery. These concepts helped build a clearer understanding of how different AWS services solve different architectural problems rather than treating them as isolated technologies.

The practical FinTrust work extended the application with Python API development and an event-driven transaction scoring design. The proposed pipeline uses Flask to receive transactions, SQS FIFO to queue transaction events, Lambda to calculate fraud risk scores, and SNS to distribute high-risk alerts to downstream consumers.

The Lambda fraud scorer uses transaction amount, currency and description keywords to calculate a risk score. Transactions meeting the configured threshold can then be published to the SNS notification layer.

The week also reinforced the importance of reliability and failure handling. SQS visibility timeouts, Dead-Letter Queues, Lambda retry behaviour and appropriate workflow services all play a role in designing systems that can recover from failures.

AWS account access was not available for the FinTrust deployment during this week. Therefore, the SQS queue, SNS topic, Lambda deployment and CloudWatch evidence remain pending. The portfolio distinguishes between implemented code, proposed architecture and AWS resources that have not yet been deployed.

Overall, Week 7 moved the FinTrust project toward a more event-driven and loosely coupled architecture while strengthening my understanding of APIs, serverless computing, messaging, Infrastructure as Code and disaster recovery.

---

## Week 7 Activities

| Day   | Topic                                                       | Outcome                                                                                                                                              |
| ----- | ----------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| Day 1 | Monitoring, CloudTrail, Messaging & APIs                    | Completed the JAWS monitoring lab, worked with CloudTrail, explored messaging and event architecture, and built Python APIs using Flask and FastAPI. |
| Day 2 | API Gateway, AppSync & Lambda                               | Explored API Gateway and AppSync, then studied Python Lambda handlers, events and context.                                                           |
| Day 3 | AWS Summit                                                  | Attended the AWS Summit for the full day.                                                                                                            |
| Day 4 | CloudFormation, DR, Systems Manager & Event-Driven Pipeline | Explored Infrastructure as Code and DR, completed the Systems Manager lab, and worked on the Boto3 transaction scoring pipeline.                     |
| Day 5 | Exam Preparation & Security                                 | Covered AWS exam preparation and tips, followed by AWS SimuLearn Core Security Concepts.                                                             |

---

## Week 7 Deliverables

| Deliverable                        | Description                                                                                                           |
| ---------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| SQS FIFO Queue Screenshot          | Screenshot showing the FinTrust SQS FIFO queue with at least one transaction message. Pending AWS account access.     |
| SNS Subscriber List Screenshot     | Screenshot showing the SNS topic with at least one subscriber. Pending AWS account access.                            |
| Flask/FastAPI Application + README | Python API committed to GitHub with documentation describing each endpoint and its purpose. Completed.                |
| Lambda Fraud Scorer                | Python Lambda function for calculating transaction fraud risk scores. Code implementation prepared for GitHub.        |
| CloudWatch Logs Screenshot         | Screenshot showing at least one scored transaction with the score visible in CloudWatch Logs. Pending AWS deployment. |
| Event-Driven Architecture Diagram  | Architecture diagram showing Flask → SQS → Lambda → SNS. Completed.                                                   |
| Mock Exam Self-Assessment          | Screenshot or photo from the Day 5 AM exam preparation/self-assessment session. Not available.                        |
| FinTrust Narrative Extension       | Extended FinTrust narrative explaining the Week 7 services and why they were introduced. Completed.                   |
| GitHub Commit History              | At least three meaningful Week 7 commits demonstrating development progress. Pending final commit review.             |

---

## Week 7 Event-Driven Architecture

The FinTrust Week 7 architecture introduces an asynchronous transaction processing pipeline:

**Flask API → SQS FIFO → Lambda Fraud Scorer → SNS → Downstream Consumers**

The Flask API accepts transaction requests and publishes transaction events.

Amazon SQS provides the messaging and buffering layer between transaction submission and fraud processing.

AWS Lambda processes the queued transaction events and calculates a fraud risk score.

Amazon SNS distributes high-risk transaction alerts to downstream consumers such as compliance services or notification systems.

The architecture separates the responsibilities of each component:

**Transaction Submission → Event Queue → Fraud Detection → Alert Distribution**

This reduces coupling between the API and fraud processing while providing a foundation for scaling the individual components independently.

---

## Practical vs Theoretical Coverage

Not every service covered during Week 7 was deployed as part of the FinTrust environment.

The week included a mixture of hands-on labs, practical development, architecture design and theoretical AWS service coverage.

Hands-on activities included:

* JAWS Lab – Monitoring Infrastructure.

* Working with AWS CloudTrail.

* Building Python APIs with Flask and FastAPI.

* Python Lambda handlers, events and context.

* JAWS Lab – Using AWS Systems Manager.

* Event-driven transaction scoring design using Boto3.

The following FinTrust AWS deployment activities require an active AWS account and therefore remain pending:

* Creating the SQS FIFO queue.

* Publishing a transaction message to SQS and capturing the required console screenshot.

* Creating the SNS topic and subscriber.

* Deploying the fraud scorer Lambda function.

* Connecting SQS to Lambda through an event source mapping.

* Viewing the scored transaction in CloudWatch Logs.

* Capturing the required AWS console evidence.

The portfolio does not claim that AWS resources were deployed where deployment evidence is unavailable. Architecture designs and code are documented separately from AWS resources that remain pending.

---

## Links

* [Fraud Scorer](./fraud_scorer/)

* [Lambda Function](./fraud_scorer/lambda_function.py)

* [Fraud Scorer README](./fraud_scorer/README.md)

* [Event-Driven Architecture](./architecture/)

* [Week 7 FinTrust Narrative](./narrative.md)
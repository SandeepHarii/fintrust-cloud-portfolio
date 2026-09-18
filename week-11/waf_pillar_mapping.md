# FinTrust Well-Architected Framework Pillar Mapping

## Overview

This document maps FinTrust scenarios from Week 11 to the AWS Well-Architected Framework six pillars.

Each scenario is assigned to the pillar that most directly addresses its primary architectural objective. Some scenarios can relate to multiple pillars, but the mapping focuses on the main concern.

## Pillar Mapping

| FinTrust Scenario                                                                             | WAF Pillar             | Justification                                                                                                                |
| --------------------------------------------------------------------------------------------- | ---------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| Establishing operational processes and reviewing the workload using the Well-Architected Tool | Operational Excellence | Focuses on running, monitoring, and continually improving the workload through defined operational processes and reviews.    |
| Protecting FinTrust resources and auditing AWS configurations                                 | Security               | Focuses on protecting data, systems, and resources through security controls, access management, and configuration auditing. |
| Designing highly available FinTrust application components                                    | Reliability            | Focuses on ensuring the workload can operate correctly, handle failures, and recover from disruptions.                       |
| Improving application delivery and handling changing workload demand efficiently              | Performance Efficiency | Focuses on using appropriate resources and architecture patterns to maintain efficient performance as requirements change.   |
| Reviewing FinTrust AWS usage with Trusted Advisor and Cost Explorer                           | Cost Optimisation      | Focuses on avoiding unnecessary expenditure and understanding how AWS resources and usage contribute to costs.               |
| Reducing unnecessary resource consumption and improving resource efficiency                   | Sustainability         | Focuses on reducing the environmental impact of cloud workloads through efficient use of resources.                          |
| Accelerating dynamic FinTrust content delivery using CloudFront                               | Performance Efficiency | The primary objective is improving content delivery performance and reducing latency for users.                              |
| Using concurrent processing for independent S3 metadata operations                            | Performance Efficiency | Parallel I/O processing can reduce unnecessary waiting time and improve the efficiency of data-processing workloads.         |
| Applying retry logic with exponential backoff to AWS API operations                           | Reliability            | Retry handling helps a workload tolerate temporary failures and recover from transient AWS API errors.                       |
| Using SQL anomaly detection to identify unusual transaction activity                          | Operational Excellence | Automated analysis can support operational monitoring and help FinTrust identify issues requiring investigation.             |

## Six Pillars Summary

### 1. Operational Excellence

FinTrust should establish processes for operating, monitoring, and improving the workload. The Well-Architected Tool and operational analysis can help identify areas that require improvement.

### 2. Security

FinTrust handles financial transaction data, making protection of data, identities, resources, and configurations an important architectural consideration. Security controls and resource auditing support this pillar.

### 3. Reliability

FinTrust should be designed to continue operating during component failures and recover from disruptions. Highly available architectures and retry mechanisms support this objective.

### 4. Performance Efficiency

FinTrust should use appropriate resources and architecture patterns to maintain efficient performance. CloudFront and concurrent I/O processing are examples of techniques that can improve workload performance.

### 5. Cost Optimisation

FinTrust should monitor AWS usage and identify opportunities to eliminate unnecessary expenditure. Trusted Advisor and Cost Explorer provide tools that can support this process.

### 6. Sustainability

FinTrust should consider resource efficiency and the environmental impact of its cloud workloads. Efficient resource utilisation can help reduce unnecessary consumption.

## Key Takeaways

The six Well-Architected Framework pillars address different aspects of cloud architecture. A single AWS service or design decision can contribute to multiple pillars, so the primary objective of the scenario should be identified before assigning a pillar.

For FinTrust, the framework provides a structured method for evaluating operational practices, security, availability, performance, cost, and resource efficiency. The mapping can be used as a starting point for future architecture reviews as the portfolio develops.
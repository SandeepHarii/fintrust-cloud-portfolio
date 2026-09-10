# FinTrust TCO Comparison

## Overview

This document outlines how a Total Cost of Ownership (TCO) comparison could be performed when evaluating the migration of FinTrust workloads from on-premises infrastructure to AWS.

The Week 9 coursework covered AWS pricing models, TCO analysis, cost optimisation, and migration planning.

No live AWS Pricing Calculator or Migration Evaluator assessment was performed for this portfolio, and no real FinTrust financial data is available. Therefore, this document does not present invented cost figures as if they were real results.

## On-Premises vs AWS

A proper TCO comparison would evaluate the expected cost of operating an equivalent workload in both environments.

| Cost Area         | On-Premises                                   | AWS                                               |
| ----------------- | --------------------------------------------- | ------------------------------------------------- |
| Compute           | Physical or virtual server infrastructure     | EC2, ECS/Fargate or other compute services        |
| Database          | Database servers, licensing and maintenance   | Managed database or database infrastructure       |
| Storage           | Data-centre storage infrastructure            | S3, EBS or other storage services                 |
| Networking        | Network hardware and connectivity             | AWS networking and data transfer                  |
| Facilities        | Data-centre space, power and cooling          | Included indirectly through cloud service pricing |
| Operations        | Infrastructure administration and maintenance | Cloud operations and service management           |
| Scaling           | Additional hardware capacity                  | Elastic cloud capacity                            |
| Disaster Recovery | Secondary infrastructure and associated costs | AWS-based backup and DR architecture              |

The actual comparison would require workload-specific measurements and current pricing.

## Required Inputs

A meaningful TCO model would require information such as:

### On-Premises

* Number and type of servers
* CPU and memory requirements
* Storage capacity
* Network requirements
* Hardware purchase costs
* Hardware refresh cycle
* Software and database licensing
* Data-centre costs
* Power and cooling
* Maintenance costs
* Infrastructure staffing
* Disaster recovery costs

### AWS

* AWS Region
* Compute instance or container requirements
* Database requirements
* Storage requirements
* Data transfer requirements
* Availability requirements
* Backup and disaster recovery requirements
* Expected utilisation
* On-Demand or commitment-based pricing
* Savings Plan eligibility

Without these inputs, producing a numerical comparison would create false precision.

## AWS Pricing Models

AWS provides several purchasing models that can affect the final TCO:

* On-Demand pricing for flexible workloads
* Savings Plans for predictable compute usage
* Reserved Instances for eligible services
* Spot Instances for suitable interruptible workloads

The appropriate model depends on workload characteristics and operational requirements.

For FinTrust, predictable baseline workloads could potentially benefit from a Compute Savings Plan, while variable workloads may benefit from more flexible purchasing options.

## TCO Analysis Process

A production TCO assessment could follow this process:

```text
Identify Workload
       ↓
Measure Current Infrastructure
       ↓
Document On-Premises Costs
       ↓
Design Equivalent AWS Architecture
       ↓
Estimate AWS Costs
       ↓
Include Migration Costs
       ↓
Compare Multi-Year TCO
       ↓
Calculate Break-Even Point
       ↓
Evaluate Business and Technical Factors
```

This prevents the migration decision from being based solely on the headline price of individual AWS services.

## Migration Costs

Initial migration costs should also be included in a complete TCO analysis.

These may include:

* Data migration
* Application remediation
* Testing
* Architecture changes
* Staff training
* Temporary parallel environments
* Migration tooling
* Professional services
* Downtime or business disruption

These costs can make the initial AWS investment higher even when the long-term operating cost is lower.

## Break-Even Analysis

Once the required cost figures are available, the break-even point can be calculated by comparing cumulative costs over time.

Conceptually:

```text
Cumulative On-Premises Cost
            vs
Cumulative AWS Cost + Migration Cost
```

The break-even point is reached when the cumulative AWS option becomes less expensive than continuing with the on-premises environment.

The actual result depends entirely on the workload and financial assumptions used.

## FinTrust Considerations

Cost should not be the only factor used when deciding whether a FinTrust workload should move to AWS.

The assessment should also consider:

1. Security
2. Regulatory compliance
3. Performance
4. Resilience
5. Scalability
6. Operational complexity
7. Migration effort
8. Business criticality
9. Long-term architecture
10. Cost

The Week 9 7Rs analysis can then be used alongside the TCO assessment to determine the most appropriate migration strategy for each workload.

## Portfolio Scope and Limitations

This portfolio demonstrates the **TCO evaluation methodology** rather than claiming a completed live pricing assessment.

Specifically:

* No AWS Pricing Calculator result is claimed.
* No Migration Evaluator result is claimed.
* No real FinTrust financial information is used.
* No live AWS resources were provisioned for this exercise.
* No unsupported cost figures have been invented.

A production FinTrust assessment would replace these limitations with actual infrastructure measurements, current AWS pricing, migration costs, and validated workload requirements.
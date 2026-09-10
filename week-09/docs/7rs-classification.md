# 7Rs Migration Classification

## Overview

The 7Rs framework provides a structured way to assess workloads before migration and determine the most appropriate migration strategy.

For FinTrust, the framework was applied to the **2,847-server fleet** rather than assuming that every workload should simply be rehosted.

The classification considers workload complexity, business value, technical constraints, modernisation opportunities, and whether a workload should continue operating after the migration programme.

## FinTrust 2,847-Server Fleet

| Migration Strategy | Server Group                                                      | Justification                                                                                                                                                                   |
| ------------------ | ----------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Rehost**         | Standard application servers                                      | Stable workloads with limited dependencies can be migrated to AWS with minimal application changes.                                                                             |
| **Replatform**     | Database-backed application servers                               | Workloads can move to managed AWS services with limited application changes, reducing infrastructure management overhead.                                                       |
| **Refactor**       | High-value core banking and customer-facing applications          | Critical applications may benefit from architectural changes to improve scalability, resilience, and cloud-native operation.                                                    |
| **Repurchase**     | Legacy commercial software workloads                              | Where an existing application can be replaced by an appropriate SaaS or managed product, purchasing the replacement may be more practical than migrating the existing platform. |
| **Retire**         | Obsolete and unused servers                                       | Workloads with no current business requirement should be decommissioned instead of generating unnecessary migration and operating costs.                                        |
| **Retain**         | Workloads with regulatory or technical constraints                | Some workloads may need to remain in their existing environment until regulatory, technical, or business constraints are resolved.                                              |
| **Relocate**       | Virtualised workloads suitable for infrastructure-level migration | Where the workload can be moved with minimal architectural change, an infrastructure relocation approach can reduce migration effort.                                           |

## Classification Principles

The 7Rs classification should not be treated as a permanent decision.

Each server group should be reassessed during migration planning as more information becomes available.

The following factors should influence the final decision:

* Business criticality
* Application dependencies
* Regulatory requirements
* Current infrastructure condition
* Technical debt
* Expected cloud operating costs
* Required migration effort
* Performance requirements
* Availability and resilience requirements
* Long-term application strategy

## Why Not Everything Should Be Rehosted

Rehosting can provide a relatively straightforward migration path, but applying it to the entire FinTrust fleet would ignore differences between workloads.

Some applications may be suitable for a direct migration, while others could benefit from managed services or architectural modernisation.

Similarly, workloads that are obsolete should not consume migration resources, while workloads affected by regulatory or technical constraints may need to remain in their current environment temporarily.

The 7Rs framework therefore provides a decision-making structure rather than a single migration strategy for the entire fleet.

## FinTrust Migration Approach

A practical migration programme could use the following sequence:

```text
2,847-Server Fleet
        ↓
Application and Dependency Assessment
        ↓
7Rs Classification
        ↓
Migration Wave Planning
        ↓
Migration Execution
        ↓
Validation and Monitoring
        ↓
Post-Migration Optimisation
```

The classification would be reviewed as part of each migration wave.

## Relationship to Cost Governance

The 7Rs assessment also connects migration planning with FinTrust's cost-management objectives.

For example:

* **Retire** removes unnecessary operating costs.
* **Replatform** can reduce infrastructure management overhead.
* **Refactor** can improve resource efficiency and scalability.
* **Rehost** can provide a lower-effort migration path where modernisation is not immediately justified.
* **Repurchase** can replace expensive legacy infrastructure with an alternative commercial model.
* **Retain** prevents premature migration where the business case or constraints do not support it.
* **Relocate** can reduce migration effort for suitable infrastructure.

Migration decisions should therefore consider both technical suitability and the expected long-term business and operating impact.

## Portfolio Scope

This classification is a planning model for the FinTrust 2,847-server fleet.

The server groups are represented at a strategic level because detailed application inventory, dependency mapping, regulatory classification, and workload-level financial data were not available in the portfolio exercise.

No individual server assignments or unsupported workload counts have been fabricated.

## Outcome

Applying the 7Rs framework prevents FinTrust from treating its entire server estate as one homogeneous migration problem.

The framework provides a basis for grouping workloads into appropriate migration paths and can then be combined with dependency analysis, cost modelling, resilience requirements, and migration-wave planning.
# Week 9 Reflection

## Overview

Week 9 focused on AWS cost management, governance, migration planning, resilience and disaster recovery. The week added another important layer to the FinTrust Cloud Portfolio by looking beyond application architecture and into how a large cloud environment can be managed financially and operationally.

A major focus this week was understanding how AWS pricing models, cost management tools and governance controls can support a large-scale migration. I also worked through migration strategies using the 7Rs framework and looked at how migration services such as AWS DMS and Snow Family can support different parts of the migration process.

Because the training environment did not require or permit direct interaction with AWS services, the practical portfolio work was implemented locally or documented as design exercises. I kept the portfolio honest by not creating fake AWS screenshots, live resource results or FinTrust financial figures.

## What I Learned

One of the main lessons this week was that cloud cost optimisation is not simply about finding the cheapest service. The pricing model needs to match the workload and its usage pattern. I looked at On-Demand pricing, Reserved Instances, Savings Plans and other cost considerations when planning workloads for AWS.

I also learned how tools such as Cost Explorer, AWS Budgets and the Cost and Usage Report can provide different levels of visibility into cloud spending. Cost Explorer is useful for analysing spending trends and service-level costs, while CUR provides more granular usage and billing data that can be queried through services such as Athena.

Another important area was cost governance. Tagging, Service Catalog and automated compliance checks can help organisations maintain control over how resources are provisioned and how costs are allocated. This becomes especially important in an environment like FinTrust where multiple workloads and teams could be operating across AWS.

The 7Rs migration framework was another major takeaway. Not every workload should simply be rehosted. Different applications have different technical, business and regulatory requirements, so migration decisions need to consider whether a workload should be rehosted, replatformed, refactored, repurchased, retired, retained or relocated.

I also gained a better understanding of migration monitoring and large-scale data transfer planning. DMS task monitoring provides visibility into database migration tasks, while Snow Family devices can be considered when moving very large datasets where transferring everything over the network would be impractical.

## Practical Work

The practical work this week focused on local Python implementations and written architecture documentation.

I developed Python implementations covering areas such as:

* AWS cost estimation and TCO planning
* Monthly cost reporting
* Cost Explorer-style service analysis
* AWS Budgets management
* Savings Plan calculations
* Tag compliance
* Service Catalog governance
* DMS task monitoring
* Migration governance reporting
* Snow transfer planning
* FIS experiment status monitoring

The AWS-related scripts include commented production guidance where appropriate. This allowed me to demonstrate how the solutions would interact with AWS APIs without falsely claiming that live AWS resources were used.

The documentation expanded the FinTrust scenario with cost management, governance and migration planning. This included a 7Rs classification for the 2,847-server fleet, a TCO comparison approach, CUR and Athena analysis, budget governance, Service Catalog controls and DMS migration monitoring.

## Challenges

One of the biggest challenges this week was working with AWS concepts that normally depend heavily on live console data while not having the ability to interact directly with AWS services.

This meant I had to distinguish between what could realistically be implemented locally and what would require live AWS access. Instead of creating artificial screenshots or filling reports with made-up numbers, I documented the expected production workflow and used simulations where appropriate.

Another challenge was understanding the relationship between cost optimisation and migration strategy. A migration decision is not purely technical. Rehosting may provide a faster migration path, while replatforming or refactoring may provide better long-term value but require more effort and investment.

The 7Rs exercise helped reinforce this because the correct migration strategy depends on the characteristics of each workload rather than applying one approach to the entire fleet.

## How This Extends FinTrust

Week 9 extended FinTrust from a primarily technical cloud architecture into a more complete enterprise cloud strategy.

The cost management layer considers how core banking and analytics workloads deployed in earlier weeks could be managed using appropriate AWS pricing models and Savings Plans. Cost reporting, budgets and tagging provide mechanisms for monitoring and controlling ongoing expenditure.

The governance layer introduces controls around resource ownership, tagging and approved services. This helps ensure that cloud growth remains controlled as more workloads are migrated.

The migration layer applies the 7Rs framework to FinTrust's 2,847-server fleet rather than assuming every workload should follow the same migration path. DMS monitoring and large-scale data transfer planning then provide supporting mechanisms for executing and monitoring parts of that migration.

## Key Takeaways

1. Cloud cost optimisation requires choosing pricing models based on workload behaviour.
2. Cost Explorer and CUR provide different levels of cost visibility.
3. Budgets and tagging are important parts of ongoing cloud governance.
4. Service Catalog can help control which products and configurations teams can provision.
5. Savings Plans can support predictable compute workloads across services such as EC2 and Fargate.
6. The 7Rs framework provides a structured way to evaluate migration strategies.
7. Not every workload should automatically be rehosted.
8. Migration monitoring is important for identifying failed or completed DMS tasks.
9. Large datasets require careful transfer planning and comparison against network-based migration.
10. Cloud architecture needs to consider cost, governance, migration and resilience alongside technical design.

## Overall Reflection

Week 9 helped me understand that building a cloud solution is only part of the problem. Once an organisation operates at scale, it also needs mechanisms to control costs, govern resources, plan migrations and maintain operational resilience.

The biggest takeaway for me was the connection between these areas. Migration strategy affects cost, architecture affects cost, governance affects how resources are consumed, and resilience affects how much an organisation needs to invest in its infrastructure.

For FinTrust, these considerations are particularly important because the environment involves a large server fleet, financial workloads and regulatory data. The work this week helped me think about the portfolio less as a collection of individual AWS services and more as a complete cloud transformation strategy.
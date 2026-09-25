# Week 12 Reflection

## What I Learned

This week focused on AWS cost optimisation, organisational governance, SCPs, CloudFormation, monitoring, and architecture decision-making. A major takeaway was that AWS governance and cost management require understanding which service or control is appropriate for a specific requirement rather than treating the services as interchangeable.

I strengthened my understanding of Savings Plans, including the distinction between Compute Savings Plans and EC2 Instance Savings Plans. I also worked with concepts around Cost Explorer, Budgets, Trusted Advisor, AWS Organizations, SCPs, CloudFormation, and governance guardrails.

The week also reinforced several AWS monitoring and architecture distinctions. CloudWatch, CloudTrail, and Config serve different purposes, while IAM, KMS, security groups, NACLs, and VPC endpoints address different layers of security and access control. Disaster recovery strategies also reinforced the importance of Recovery Point Objective (RPO) and Recovery Time Objective (RTO) when selecting an appropriate architecture.

## Practical Experience

The practical work included preparing the FinTrust SQL performance tuning lab with three transaction-related query scenarios and corresponding indexes.

The SQL tuning work focused on identifying which columns should be indexed based on filtering, joining, and ordering requirements. The before-and-after `EXPLAIN ANALYZE` queries were prepared in `sql/fintrust_views.sql`.

A PostgreSQL database environment was not available, so the queries could not be executed and no performance measurements or execution-plan comparisons were recorded. This meant the tuning exercise focused on preparing the SQL and documenting the reasoning without claiming unmeasured performance improvements.

## Challenges

The main challenge this week was distinguishing between AWS services and governance concepts that can appear similar in exam questions.

Cost Explorer, Budgets, and Trusted Advisor have related cost-management functions, while CloudWatch, CloudTrail, and Config each provide different types of monitoring and auditing capabilities. SCP evaluation order and Deny-List vs Allow-List strategies also require more precise understanding than simple memorisation.

The self-assessment also highlighted gaps around preventive, detective, and proactive guardrails, as well as disaster recovery strategies and the relationship between RPO and RTO.

## Self-Assessment

| Topic                                                |  Rating | Notes / Gap                                                                                  |
| ---------------------------------------------------- | ------: | -------------------------------------------------------------------------------------------- |
| Savings Plans: Compute vs EC2 Instance               | **3/5** | Important cost distinction, but relatively narrow.                                           |
| Cost Explorer API vs Budgets vs Trusted Advisor      | **2/5** | The three overlap enough to cause exam mistakes. Worth drilling.                             |
| SCP policy evaluation order                          | **2/5** | More than simple memorization, and SCP questions can be tricky.                              |
| SCP Deny-List vs Allow-List                          | **2/5** | Specific organisational-policy concept. Needs clean recognition.                             |
| CloudFormation: Resources mandatory + other sections | **3/5** | Useful knowledge, but probably lower priority than core architecture.                        |
| DeletionPolicy: Snapshot vs Retain                   | **3/5** | Worth knowing the exact distinction.                                                         |
| Preventive vs Detective vs Proactive guardrails      | **2/5** | High priority. The terminology is easy to mix up.                                            |
| CloudWatch vs CloudTrail vs Config                   | **2/5** | High priority. Classic exam discrimination question.                                         |
| Domain 1: IAM/KMS/SG vs NACL/VPC endpoints           | **3/5** | Broader topic, with existing familiarity from previous work.                                 |
| Domain 2: DR strategies, RPO/RTO                     | **2/5** | High priority. This can affect several architecture questions rather than one isolated fact. |

## What I Would Improve

I would prioritise reviewing the topics that received a **2/5** confidence rating, especially CloudWatch vs CloudTrail vs Config, SCP evaluation and strategy, governance guardrails, and DR strategies involving RPO and RTO.

I would also spend more time drilling Cost Explorer, Budgets, and Trusted Advisor so that I can quickly identify which tool answers a particular cost-management question.

For the SQL tuning lab, I would like to repeat the exercise in a PostgreSQL environment so that I can capture actual `EXPLAIN ANALYZE` execution plans and compare the queries before and after indexing.

## Overall Reflection

Week 12 helped strengthen the connection between AWS cost management, governance, monitoring, and architecture decisions. The week also made it clearer which areas I understand reasonably well and which concepts still require focused exam preparation.

The self-assessment showed that several AWS governance, monitoring, and disaster recovery topics remain areas for improvement. The six topics rated 2/5 will be the main focus for weekend review before progressing further with the certification preparation.

The SQL tuning exercise also reinforced the importance of separating theoretical optimisation from measured performance. Without a PostgreSQL environment, I could prepare and document the indexing approach, but I did not claim performance improvements without actual execution evidence.
# FinTrust Migration Architecture Narrative

The FinTrust migration approach uses AWS migration strategies based on the characteristics, business value, technical constraints, and future requirements of each workload rather than applying one strategy to the entire environment. The AWS 6Rs framework provides the basis for these decisions: Rehost, Replatform, Refactor, Repurchase, Retire, and Retain.

Rehosting is appropriate for workloads that need to move to AWS with minimal changes. This approach reduces migration complexity and allows workloads to be moved quickly while maintaining their existing architecture. Replatforming is preferred where a workload can benefit from a managed AWS service without requiring a complete redesign. For example, a relational database can be moved towards Amazon RDS to reduce infrastructure management while retaining the relational database model.

Refactoring is considered for workloads where cloud-native capabilities provide significant long-term benefits. This may involve redesigning components to take advantage of services such as serverless computing, messaging, or managed databases. Retiring is used for obsolete or duplicated workloads that no longer provide business value, while retaining is appropriate when a workload has constraints that make immediate migration impractical.

AWS Database Migration Service (DMS) supports the database migration process by providing a controlled method for moving database workloads while reducing disruption to the existing environment. DMS can also support ongoing replication during migration, allowing a cutover to be planned rather than requiring an immediate move.

For large-scale file and data movement, AWS DataSync provides an automated and secure transfer approach over the network. It is suitable when data needs to be transferred between existing storage and AWS without relying on manual copying. For extremely large datasets where network transfer would be impractical or cost-prohibitive, physical transfer options such as AWS Snowball can be considered instead.

Transfer costs are also part of the migration decision. The fastest technical option is not necessarily the most cost-effective option, so transfer volume, network capacity, migration duration, and the destination architecture must be considered together.

Overall, the FinTrust migration architecture combines workload-specific 6R decisions with DMS for database migration and DataSync or physical transfer options for data movement. This approach aims to balance migration speed, operational effort, cost, risk, and the long-term benefits of running workloads on AWS.
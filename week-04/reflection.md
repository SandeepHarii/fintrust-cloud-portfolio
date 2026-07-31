# Week 4 Reflection

## 1. AWS Database Selection

FinTrust originally used a single on-premises PostgreSQL database to handle transactions, customer sessions, trade documents, and analytics. Splitting these workloads across multiple AWS database services is justified because each workload has different performance, scalability, and consistency requirements. Amazon RDS PostgreSQL Multi-AZ is best suited for transactional banking data, Amazon Aurora Global Database supports globally distributed applications with low-latency reads, Amazon DynamoDB provides single-digit millisecond performance for session data, Amazon QLDB maintains an immutable ledger for audit records, Amazon ElastiCache improves application performance by caching frequently accessed data, and Amazon Redshift is optimised for analytical reporting. Although this architecture increases operational complexity, monitoring requirements, and overall cost, each service is optimised for its specific workload, resulting in better performance, scalability, resilience, and regulatory compliance than a single database could provide.

---

## 2. ETL Pipeline

If two processes ran this pipeline at exactly the same time using the same SQLite database file, they could interfere with each other. SQLite allows multiple processes to read from the database simultaneously, but it only allows one process to write at a time. This means one process could temporarily lock the database while inserting data, causing the other process to wait or fail with a **"database is locked"** error if it cannot obtain the write lock.

In this pipeline, duplicate transactions would still be prevented because `transaction_id` is the primary key and duplicate inserts are caught using `sqlite3.IntegrityError`. However, the pipeline is not designed to coordinate multiple writers, so concurrent execution could still lead to delays or locking issues.

Amazon RDS Multi-AZ addresses a different problem. It provides high availability by synchronously replicating data to a standby instance in another Availability Zone. This results in a near-zero Recovery Point Objective (RPO) and automatic failover with a typical Recovery Time Objective (RTO) of around 60–120 seconds if the primary instance fails. However, Multi-AZ does **not** improve read scalability or support database migrations. Those requirements are addressed by **Read Replicas**, which distribute read traffic across multiple database instances, and **AWS Database Migration Service (AWS DMS)**, which supports live migrations and continuous data replication with minimal downtime.

---

## 3. Python Packaging

Refactoring `pipeline.py` into the `fintrust_pipeline` package made the application significantly easier to organise and maintain. Instead of placing every function inside one large file, related functionality was separated into dedicated modules such as `loader.py`, `database.py`, and `reporter.py`, each with a single responsibility. This structure makes the code easier to test, debug, and extend because individual modules can be imported independently without executing the entire application. As the project grows, new functionality can be added without making a single file difficult to manage, resulting in a more scalable and maintainable codebase.

---

## 4. Week 4 to Week 5 Bridge

As the FinTrust database architecture moves into a Virtual Private Cloud (VPC), several network-level configurations become essential. First, Amazon RDS should be deployed within private subnets so that the database cannot be accessed directly from the internet. Access should only be permitted from authorised application servers through carefully configured Security Groups, reducing the attack surface while protecting sensitive financial data.

Second, a DynamoDB Gateway Endpoint should be configured to allow EC2 instances within the VPC to communicate with Amazon DynamoDB over the AWS private network instead of traversing the public internet. This improves both security and performance while eliminating the need for internet gateways or NAT gateways for DynamoDB traffic. Similarly, services such as Amazon ElastiCache should only accept connections from approved application instances through Security Groups, ensuring that cached data remains protected within the private network.

---

## Additional Reflection

### What does boto3 use instead of `?` placeholders for parameterised queries?

Unlike SQLite, boto3 does not use SQL, so it does not use `?` placeholders for parameterised queries. Services such as Amazon DynamoDB and Amazon S3 are accessed through the AWS SDK by passing structured Python dictionaries and objects directly to API methods rather than constructing SQL statements. This approach eliminates string interpolation, reduces the risk of injection vulnerabilities, and provides a safer, more structured way to interact with AWS services.

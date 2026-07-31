# FinTrust Database Architecture Diagram

```text
                                     FINTRUST DATABASE ARCHITECTURE

                                        Legacy Flat-file NAS
                                                │
                                                │ AWS Database Migration Service (DMS)
                                                │ Continuous Data Capture (CDC)
                                                ▼

──────────────────────────────────── AWS Region: af-south-1 ────────────────────────────────────

        ┌──────────────────────────────────────────────────────────────────────────────┐
        │ Amazon RDS PostgreSQL (Multi-AZ)                                             │
        │ Primary + Synchronous Standby                                                │
        │ Core banking transactions, account balances and payments                     │
        └──────────────────────────────────────────────────────────────────────────────┘
                                              │
                    ┌─────────────────────────┴─────────────────────────┐
                    │                                                   │
                    ▼                                                   ▼

      ┌────────────────────────────────┐            ┌─────────────────────────────────────┐
      │ Amazon Aurora Read Replica     │            │ Amazon DynamoDB Global Tables       │
      │ Region: af-south-1             │            │ Regions: af-south-1 + eu-west-1     │
      │ Reporting and read workloads   │            │ Active login sessions & tokens      │
      └────────────────────────────────┘            └─────────────────────────────────────┘

                    ┌─────────────────────────┬─────────────────────────┐
                    │                         │                         │
                    ▼                         ▼                         ▼

      ┌──────────────────────────┐  ┌──────────────────────────┐  ┌──────────────────────────┐
      │ Amazon QLDB              │  │ Amazon DocumentDB        │  │ Amazon ElastiCache Redis │
      │ Region: af-south-1       │  │ Region: af-south-1       │  │ Region: af-south-1       │
      │ Immutable audit ledger   │  │ JSON trade documents     │  │ FX rates & leaderboards  │
      └──────────────────────────┘  └──────────────────────────┘  └──────────────────────────┘
                                              │
                                              ▼
                     ┌──────────────────────────────────────────────────────┐
                     │ Amazon Redshift                                      │
                     │ Region: af-south-1                                   │
                     │ Historical analytics and BI reporting                │
                     └──────────────────────────────────────────────────────┘
```

> **Note:** Unless otherwise stated, all services are deployed in the AWS Africa (Cape Town) Region (`af-south-1`). Amazon DynamoDB Global Tables replicate data across both `af-south-1` and `eu-west-1` to provide active-active multi-Region availability.

---

## Database Services

| Layer             | AWS Service                          | Region(s)                                             | FinTrust Use Case                                           | Why this service was chosen                                                                                                                          |
| ----------------- | ------------------------------------ | ----------------------------------------------------- | ----------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| Core Transactions | **Amazon RDS PostgreSQL (Multi-AZ)** | **af-south-1 (Primary & Standby Availability Zones)** | Account balances and payment processing                     | Provides **ACID-compliant transactions**, automated backups, and **synchronous Multi-AZ replication** with automatic failover for high availability. |
| Read Scaling      | **Amazon Aurora Read Replica**       | **af-south-1**                                        | Reporting and read-heavy queries                            | Offloads reporting traffic from the primary database while delivering high-performance read scalability.                                             |
| Session Store     | **Amazon DynamoDB Global Tables**    | **af-south-1 and eu-west-1**                          | Active login sessions and authentication tokens             | Provides low-latency performance with **active-active multi-Region replication** for globally distributed applications.                              |
| Audit Ledger      | **Amazon QLDB**                      | **af-south-1**                                        | Regulatory transaction history                              | Maintains an **immutable, cryptographically verifiable ledger** to satisfy financial auditing and compliance requirements.                           |
| Document Store    | **Amazon DocumentDB**                | **af-south-1**                                        | JSON trade documents and confirmations                      | Supports flexible document storage while remaining compatible with MongoDB applications.                                                             |
| Cache Layer       | **Amazon ElastiCache for Redis**     | **af-south-1**                                        | Frequently accessed foreign exchange rates and leaderboards | Delivers **sub-millisecond in-memory performance** to reduce database load and improve application responsiveness.                                   |
| Analytics         | **Amazon Redshift**                  | **af-south-1**                                        | Historical analytics and business intelligence              | Uses **columnar storage** and **massively parallel processing (MPP)** to optimise large-scale analytical queries.                                    |

---

## Data Migration

```text
Legacy Flat-file NAS
        │
        ▼
AWS Database Migration Service (DMS)
Continuous Data Capture (CDC)
        │
        ▼
Amazon RDS PostgreSQL (Multi-AZ)
```

---

## Architecture Summary

The FinTrust platform uses a **purpose-built database architecture**, where each workload is assigned to the AWS database service best suited to its requirements. Amazon RDS PostgreSQL manages transactional banking data, Aurora supports read-intensive workloads, DynamoDB Global Tables provides globally distributed session management, QLDB maintains an immutable audit trail, DocumentDB stores flexible JSON trade documents, ElastiCache accelerates frequently accessed data, and Redshift powers analytical reporting. Legacy data is migrated from the on-premises flat-file NAS environment using **AWS Database Migration Service (DMS)** with **Continuous Data Capture (CDC)**, enabling a low-downtime migration while keeping source and target data synchronised.

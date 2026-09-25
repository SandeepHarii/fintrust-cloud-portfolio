# SQL Tuning Lab

## Overview

This lab focused on identifying suitable indexes for common FinTrust transaction queries and preparing before-and-after `EXPLAIN ANALYZE` statements for performance comparison.

The SQL was prepared in `sql/fintrust_views.sql`.

No PostgreSQL database environment was available during this lab, so the queries and indexes could not be executed. No execution plans, timings, or measured performance improvements have been recorded.

## Scenario 1: Monthly Transaction Summary by Customer

### Query Pattern

The query:

* Filters transactions by `transaction_date`
* Joins transactions to customers using `customer_id`
* Groups results by customer and month

### Index

```sql
CREATE INDEX IF NOT EXISTS idx_transactions_date_customer
ON transactions (transaction_date, customer_id);
```

### Rationale

The index places `transaction_date` first because it is used directly by the query's date filter.

`customer_id` is included to support the subsequent join between `transactions` and `customers`.

### Testing Status

A before-index and after-index `EXPLAIN ANALYZE` query has been included in `sql/fintrust_views.sql`.

The queries were **not executed** because no PostgreSQL database was available.

Therefore, no actual execution-plan or performance comparison is reported.

---

## Scenario 2: Flagging Transactions Over Account Limit

### Query Pattern

The query:

* Filters transactions from the previous seven days
* Joins transactions to accounts using `account_id`
* Compares the transaction amount against the account credit limit

### Index

```sql
CREATE INDEX IF NOT EXISTS idx_transactions_date_account
ON transactions (transaction_date, account_id);
```

### Rationale

`transaction_date` is the directly indexable filter because the query restricts results to recent transactions.

`account_id` is included to support the subsequent join to the `accounts` table.

The comparison:

```sql
t.amount > a.credit_limit * 0.9
```

depends on values from two tables, so it was not used as the primary index condition.

### Testing Status

A before-index and after-index `EXPLAIN ANALYZE` query has been included in `sql/fintrust_views.sql`.

The queries were **not executed** because no PostgreSQL database was available.

Therefore, no actual execution-plan or performance comparison is reported.

---

## Scenario 3: Audit Log for Compliance

### Query Pattern

The query:

* Performs a `LEFT JOIN` between transactions and accounts
* Identifies transactions where no matching account exists
* Orders the results by transaction date in descending order

### Index

```sql
CREATE INDEX IF NOT EXISTS idx_transactions_account_date
ON transactions (account_id, transaction_date DESC);
```

### Rationale

`account_id` supports the account matching performed by the join.

`transaction_date DESC` reflects the ordering requirement of the query and can support retrieval in the required date order.

### Testing Status

A before-index and after-index `EXPLAIN ANALYZE` query has been included in `sql/fintrust_views.sql`.

The queries were **not executed** because no PostgreSQL database was available.

Therefore, no actual execution-plan or performance comparison is reported.

---

## Evidence Status

| Scenario                        | Index Prepared | Before `EXPLAIN ANALYZE` | After `EXPLAIN ANALYZE` | Measured Results |
| ------------------------------- | -------------- | ------------------------ | ----------------------- | ---------------- |
| Monthly transaction summary     | ✅              | Prepared                 | Prepared                | Not available    |
| Transactions over account limit | ✅              | Prepared                 | Prepared                | Not available    |
| Deleted-account audit log       | ✅              | Prepared                 | Prepared                | Not available    |

## Outcome

The three SQL tuning scenarios were prepared with indexes selected according to their filtering, joining, and ordering patterns.

The required before-and-after `EXPLAIN ANALYZE` statements are present in `sql/fintrust_views.sql`, but execution evidence could not be captured because no PostgreSQL database environment was available.

No performance improvement has been claimed without measured evidence.

# FinTrust Cloud Portfolio
## Week 2 Summary

This week focused on building Python programs that model common banking business logic and writing SQL queries to retrieve, analyze, and summarize banking data from a relational database.

---

# Python

## Overview

Built a collection of small banking applications that demonstrate decision-making using `if`, `elif`, and `else` statements.

### Exercises Completed

### Transaction Classifier
- Classified transactions into:
  - MICRO
  - SMALL
  - STANDARD
  - LARGE
  - INVALID

**Concepts**
- Conditional logic
- Functions
- Return values

---

### Interest Rate Calculator
Calculated loan interest rates based on customer credit scores.

**Concepts**
- Range comparisons
- Multiple conditions
- Business rules

---

### ATM Withdrawal Logic
Simulated ATM withdrawals by validating:
- Invalid amounts
- Daily ATM withdrawal limit
- Insufficient funds
- Successful withdrawals

**Concepts**
- Input validation
- Financial business logic
- Boolean return values
- Formatted output

---

### Transaction Tagger
Automatically tagged transactions based on:
- Refunds
- Gambling merchants
- Grocery purchases
- Large purchases
- Standard transactions

**Concepts**
- Multiple conditional branches
- Rule prioritisation
- Transaction categorisation

---

### Transaction Decision Engine
Built a more realistic banking transaction processor that evaluates transactions using multiple security checks.

The engine validates:
- Blocked destination countries
- Daily transaction limits
- Invalid amounts
- Large transfers
- Trusted vs untrusted devices

Possible outcomes include:
- APPROVED
- REVIEW
- PENDING
- BLOCKED

**Concepts**
- Nested conditionals
- Constants
- Dictionaries
- Function design
- Business rule implementation
- Automated decision making

---

# SQL

## Overview

Worked with a relational banking database containing Customers, Accounts and Transactions tables.

---

## Joins

Practised retrieving related information using:
- INNER JOIN
- LEFT JOIN

Built queries to:
- Display customer accounts and balances
- Filter customers by province and balance
- Combine customers, accounts and transactions
- Find customers with no transactions

---

## Filtering

Used:
- WHERE
- IN
- IS NULL

to retrieve specific banking records.

---

## Aggregation

Used aggregate functions including:
- COUNT()
- SUM()
- AVG()

to analyse customer and account data.

---

## Grouping

Practised:
- GROUP BY
- HAVING

to produce summaries such as:
- Transactions per customer
- Average balance per account type
- Total deposits by province

---

## Date Functions

Used:
- YEAR()
- MONTH()
- DATE()

to generate monthly transaction summaries and daily transaction reports.

---

## Fraud Detection

Created a query that identifies customers making more than three debit transactions in a single day, demonstrating a simple fraud detection pattern.

---

# Skills Practised

## Python
- Functions
- Conditional statements
- Nested logic
- Dictionaries
- Boolean logic
- Input validation
- Banking business rules

## SQL
- INNER JOIN
- LEFT JOIN
- WHERE
- GROUP BY
- HAVING
- ORDER BY
- Aggregate functions
- Date functions
- Multi-table queries

---

## Outcome

By the end of the week, a small banking portfolio was built that demonstrates both application logic in Python and relational data analysis using SQL. The exercises simulate real-world financial systems by applying business rules, validating transactions, querying customer data, generating reports, and identifying potential fraud patterns.
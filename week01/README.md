# Week 1 — Cloud & SQL Foundations

## Overview

Week 1 introduced the fundamentals of AWS cloud networking and SQL database design using the FinTrust banking case study. Morning (AM) sessions focused on AWS global infrastructure and networking concepts, while afternoon (PM) sessions covered relational database design and SQL fundamentals through practical exercises.

---

## What I Learned This Week

### AWS (AM Sessions)

* Explored AWS global infrastructure, including Regions and Availability Zones.
* Learnt the fundamentals of Amazon VPC and virtual networking.
* Designed a secure three-tier VPC architecture for the FinTrust environment.
* Configured public and private subnets, Internet Gateway (IGW), and NAT Gateway.
* Compared Security Groups (stateful) and Network ACLs (stateless) for network security.

### SQL (PM Sessions)

* Learnt the fundamentals of relational database design.
* Created tables using appropriate data types and constraints.
* Designed the FinTrust banking database schema.
* Inserted sample banking data into database tables.
* Retrieved data using `SELECT` statements.
* Applied the `WHERE` clause to filter records using:

  * `=`
  * `!=`
  * `>`
  * `<`
  * `LIKE`
  * `IN`
  * `BETWEEN`
  * `IS NULL`

---

## Repository Contents

| File                            | Description                                                                                 |
| ------------------------------- | ------------------------------------------------------------------------------------------- |
| `sql/day2_basic_select.sql`     | Basic SQL `SELECT` statement exercises for retrieving data from database tables.            |
| `sql/day2_explore.sql`          | Exploratory SQL queries used to examine and understand the FinTrust database.               |
| `sql/day3_fintrust_schema.sql`  | Core FinTrust banking database schema, including table definitions and relationships.       |
| `sql/day4_where_challenges.sql` | Practice exercises demonstrating the use of the `WHERE` clause to solve business scenarios. |
| `sql/day4_where_filtering.sql`  | SQL queries demonstrating filtering techniques using comparison and logical operators.      |
| `sql/fintrust_schema.sql`       | Consolidated FinTrust database schema used throughout the week's SQL practical exercises.   |

---

## Outcome

By the end of Week 1, I had developed a solid foundation in AWS networking concepts and relational database design. Through the FinTrust case study, I successfully designed a banking database schema, wrote SQL queries to retrieve and filter data, and gained practical experience with core AWS networking components that form the basis of secure cloud infrastructure.
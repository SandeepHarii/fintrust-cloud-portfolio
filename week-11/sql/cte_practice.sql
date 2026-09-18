/*
==========================================================
FinTrust Cloud Portfolio
Week 11 Day 2 PM
SQL Common Table Expressions

Topics:
- CTE syntax
- Chaining CTEs
- Recursive CTEs
- CTE + Window Functions
==========================================================
*/


/*
==========================================================
A01 - CTE SYNTAX AND PURPOSE
==========================================================
*/

/*
Calculate monthly transaction totals per account,
then return accounts with monthly totals above 50,000.
*/

WITH monthly_totals AS (
    SELECT
        account_id,
        DATE_TRUNC('month', transaction_date) AS txn_month,
        SUM(amount) AS total_amount,
        COUNT(*) AS txn_count
    FROM transactions
    GROUP BY
        account_id,
        DATE_TRUNC('month', transaction_date)
)

SELECT
    account_id,
    txn_month,
    total_amount
FROM monthly_totals
WHERE total_amount > 50000
ORDER BY total_amount DESC;


/*
==========================================================
A02 - CHAINING MULTIPLE CTEs
==========================================================
*/

/*
Step 1:
Calculate 30-day transaction activity per account.
*/

WITH recent_activity AS (
    SELECT
        account_id,
        COUNT(*) AS txn_count_30d,
        SUM(amount) AS total_30d
    FROM transactions
    WHERE transaction_date >= CURRENT_DATE - INTERVAL '30 days'
    GROUP BY account_id
),

/*
Step 2:
Calculate the average and standard deviation
of transaction counts.
*/

avg_velocity AS (
    SELECT
        AVG(txn_count_30d) AS avg_count,
        STDDEV(txn_count_30d) AS stddev_count
    FROM recent_activity
),

/*
Step 3:
Flag accounts more than two standard deviations
above the average.
*/

flagged_accounts AS (
    SELECT
        r.account_id,
        r.txn_count_30d,
        r.total_30d
    FROM recent_activity r
    CROSS JOIN avg_velocity a
    WHERE r.txn_count_30d >
          a.avg_count + (2 * a.stddev_count)
)

/*
Step 4:
Join flagged accounts to account details.
*/

SELECT
    f.account_id,
    a.customer_name,
    f.txn_count_30d,
    f.total_30d
FROM flagged_accounts f
JOIN accounts a
    ON f.account_id = a.account_id
ORDER BY f.txn_count_30d DESC;


/*
==========================================================
A03 - RECURSIVE CTE
==========================================================
*/

/*
Walk through an organisational/account hierarchy.

The anchor starts with accounts that have no parent.
The recursive section finds children of accounts
already found by the CTE.
*/

WITH RECURSIVE account_hierarchy AS (

    /*
    Anchor member
    */

    SELECT
        account_id,
        parent_account_id,
        account_name,
        0 AS depth
    FROM accounts
    WHERE parent_account_id IS NULL

    UNION ALL

    /*
    Recursive member
    */

    SELECT
        a.account_id,
        a.parent_account_id,
        a.account_name,
        h.depth + 1
    FROM accounts a
    JOIN account_hierarchy h
        ON a.parent_account_id = h.account_id
    WHERE h.depth < 10
)

SELECT
    account_id,
    account_name,
    depth
FROM account_hierarchy
ORDER BY
    depth,
    account_name;


/*
==========================================================
A04 - PRACTICE QUERY 1
==========================================================
Exercise 1:

Calculate month-over-month growth for each account.

Step 1:
Calculate monthly transaction totals.

Step 2:
Use LAG to get the previous month's total.

Step 3:
Calculate percentage change.

Step 4:
Flag growth greater than 100%.
*/


WITH monthly_totals AS (
    SELECT
        account_id,
        DATE_TRUNC('month', transaction_date) AS txn_month,
        SUM(amount) AS monthly_total
    FROM transactions
    GROUP BY
        account_id,
        DATE_TRUNC('month', transaction_date)
),

monthly_with_previous AS (
    SELECT
        account_id,
        txn_month,
        monthly_total,
        LAG(monthly_total) OVER (
            PARTITION BY account_id
            ORDER BY txn_month
        ) AS previous_month_total
    FROM monthly_totals
),

growth_calculated AS (
    SELECT
        account_id,
        txn_month,
        monthly_total,
        previous_month_total,
        CASE
            WHEN previous_month_total IS NULL
                 OR previous_month_total = 0
            THEN NULL
            ELSE (
                (monthly_total - previous_month_total)
                / previous_month_total
            ) * 100
        END AS growth_percent
    FROM monthly_with_previous
)

SELECT
    account_id,
    txn_month,
    monthly_total,
    previous_month_total,
    growth_percent,
    CASE
        WHEN growth_percent > 100
        THEN 'GREATER THAN 100%'
        ELSE '100% OR LESS'
    END AS growth_flag
FROM growth_calculated
ORDER BY
    account_id,
    txn_month;


/*
==========================================================
A04 - PRACTICE QUERY 2
==========================================================
Exercise 2:

Rank all accounts by total transaction value using
DENSE_RANK().

Then identify the top 10% of distinct rank values.
*/


WITH account_totals AS (
    SELECT
        account_id,
        SUM(amount) AS total_transaction_value
    FROM transactions
    GROUP BY account_id
),

ranked_accounts AS (
    SELECT
        account_id,
        total_transaction_value,
        DENSE_RANK() OVER (
            ORDER BY total_transaction_value DESC
        ) AS account_rank,
        COUNT(DISTINCT total_transaction_value) OVER () AS distinct_total_values
    FROM account_totals
)

SELECT
    account_id,
    total_transaction_value,
    account_rank
FROM ranked_accounts
WHERE account_rank <= CEIL(distinct_total_values * 0.10)
ORDER BY
    account_rank,
    total_transaction_value DESC;


/*
==========================================================
CTE + WINDOW FUNCTION PATTERN
==========================================================
*/

/*
A simpler example of the standard pattern.

The window function is calculated inside the CTE.
The outer query then filters the result.
*/

WITH ranked_transactions AS (
    SELECT
        account_id,
        transaction_date,
        amount,
        ROW_NUMBER() OVER (
            PARTITION BY account_id
            ORDER BY amount DESC
        ) AS transaction_rank
    FROM transactions
)

SELECT
    account_id,
    transaction_date,
    amount,
    transaction_rank
FROM ranked_transactions
WHERE transaction_rank = 1
ORDER BY account_id;


/*
==========================================================
A05 - PORTFOLIO DELIVERABLE
==========================================================
MULTI-STEP ANOMALY DETECTION

The query uses multiple named CTEs to identify accounts
with unusual month-over-month transaction growth.

The process is:

1. Calculate monthly transaction totals.
2. Retrieve the previous month's total using LAG().
3. Calculate the growth percentage and running total.
4. Flag accounts where month-over-month growth exceeds
   100%.

The CTE chain separates each analytical step and makes
the anomaly detection logic easier to understand.
*/


/*
----------------------------------------------------------
A05.1 - Multi-step anomaly detection
----------------------------------------------------------
*/

WITH monthly_totals AS (

    /*
    CTE 1:
    Aggregate transactions into monthly totals per account.
    */

    SELECT
        account_id,
        DATE_TRUNC('month', transaction_date) AS txn_month,
        SUM(amount) AS monthly_total,
        COUNT(*) AS transaction_count
    FROM transactions
    GROUP BY
        account_id,
        DATE_TRUNC('month', transaction_date)
),

monthly_with_previous AS (

    /*
    CTE 2:
    Retrieve the previous month's total for each account.
    */

    SELECT
        account_id,
        txn_month,
        monthly_total,
        transaction_count,

        LAG(monthly_total) OVER (
            PARTITION BY account_id
            ORDER BY txn_month
        ) AS previous_month_total

    FROM monthly_totals
),

anomaly_metrics AS (

    /*
    CTE 3:
    Calculate month-over-month growth and the cumulative
    transaction value for each account.
    */

    SELECT
        account_id,
        txn_month,
        monthly_total,
        previous_month_total,
        transaction_count,

        CASE
            WHEN previous_month_total IS NULL
                 OR previous_month_total = 0
            THEN NULL
            ELSE (
                (monthly_total - previous_month_total)
                / previous_month_total
            ) * 100
        END AS growth_percent,

        SUM(monthly_total) OVER (
            PARTITION BY account_id
            ORDER BY txn_month
            ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
        ) AS running_transaction_total

    FROM monthly_with_previous
),

flagged_anomalies AS (

    /*
    CTE 4:
    Flag accounts where transaction value increased by
    more than 100% compared with the previous month.
    */

    SELECT
        account_id,
        txn_month,
        monthly_total,
        previous_month_total,
        transaction_count,
        growth_percent,
        running_transaction_total,

        CASE
            WHEN growth_percent > 100
            THEN 'ANOMALY'
            ELSE 'NORMAL'
        END AS anomaly_status

    FROM anomaly_metrics
)

SELECT
    account_id,
    txn_month,
    monthly_total,
    previous_month_total,
    transaction_count,
    growth_percent,
    running_transaction_total,
    anomaly_status
FROM flagged_anomalies
WHERE anomaly_status = 'ANOMALY'
ORDER BY
    growth_percent DESC,
    account_id,
    txn_month;


/*
----------------------------------------------------------
A05.2 - Anomaly summary by account
----------------------------------------------------------
*/

WITH monthly_totals AS (

    SELECT
        account_id,
        DATE_TRUNC('month', transaction_date) AS txn_month,
        SUM(amount) AS monthly_total
    FROM transactions
    GROUP BY
        account_id,
        DATE_TRUNC('month', transaction_date)
),

monthly_with_previous AS (

    SELECT
        account_id,
        txn_month,
        monthly_total,

        LAG(monthly_total) OVER (
            PARTITION BY account_id
            ORDER BY txn_month
        ) AS previous_month_total

    FROM monthly_totals
),

anomaly_metrics AS (

    SELECT
        account_id,
        txn_month,
        monthly_total,
        previous_month_total,

        CASE
            WHEN previous_month_total IS NULL
                 OR previous_month_total = 0
            THEN NULL
            ELSE (
                (monthly_total - previous_month_total)
                / previous_month_total
            ) * 100
        END AS growth_percent

    FROM monthly_with_previous
),

flagged_anomalies AS (

    SELECT
        account_id,
        txn_month,
        monthly_total,
        previous_month_total,
        growth_percent,

        CASE
            WHEN growth_percent > 100
            THEN 1
            ELSE 0
        END AS anomaly_flag

    FROM anomaly_metrics
)

SELECT
    account_id,
    COUNT(*) AS months_analyzed,
    SUM(anomaly_flag) AS anomaly_count,
    MAX(growth_percent) AS highest_growth_percent
FROM flagged_anomalies
GROUP BY account_id
HAVING SUM(anomaly_flag) > 0
ORDER BY
    anomaly_count DESC,
    highest_growth_percent DESC;
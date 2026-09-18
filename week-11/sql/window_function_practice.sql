/*
==========================================================
FinTrust Cloud Portfolio
Week 11 Day 1 PM
SQL Window Functions

Topics:
- OVER
- PARTITION BY
- ORDER BY
- ROW_NUMBER
- RANK
- DENSE_RANK
- NTILE
- SUM / AVG window functions
- LAG / LEAD
- Running totals
- Moving averages
==========================================================
*/


/*
==========================================================
A01 - WINDOW FUNCTION SYNTAX
==========================================================
*/

/*
Basic window function.

Calculates the total transaction amount for each account
while keeping every individual transaction row.
*/

SELECT
    account_id,
    transaction_date,
    amount,
    SUM(amount) OVER (
        PARTITION BY account_id
    ) AS account_total
FROM transactions;


/*
Window function with ordering.

Calculates a running total for each account based on
transaction date.
*/

SELECT
    account_id,
    transaction_date,
    amount,
    SUM(amount) OVER (
        PARTITION BY account_id
        ORDER BY transaction_date
        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    ) AS running_total
FROM transactions;


/*
==========================================================
A02 - RANKING FUNCTIONS
==========================================================
*/


/*
ROW_NUMBER()

Assigns a unique sequential number to each transaction
within each account.
*/

SELECT
    account_id,
    transaction_date,
    amount,
    ROW_NUMBER() OVER (
        PARTITION BY account_id
        ORDER BY amount DESC
    ) AS row_number_rank
FROM transactions;


/*
RANK()

Transactions with the same amount receive the same rank.
Gaps are created after ties.
*/

SELECT
    account_id,
    transaction_date,
    amount,
    RANK() OVER (
        PARTITION BY account_id
        ORDER BY amount DESC
    ) AS transaction_rank
FROM transactions;


/*
DENSE_RANK()

Transactions with the same amount receive the same rank.
Unlike RANK(), no gaps are created after ties.
*/

SELECT
    account_id,
    transaction_date,
    amount,
    DENSE_RANK() OVER (
        PARTITION BY account_id
        ORDER BY amount DESC
    ) AS dense_transaction_rank
FROM transactions;


/*
NTILE(4)

Divides each account's transactions into four buckets.
*/

SELECT
    account_id,
    transaction_date,
    amount,
    NTILE(4) OVER (
        PARTITION BY account_id
        ORDER BY amount DESC
    ) AS transaction_quartile
FROM transactions;


/*
Top transaction per account per month.

The CTE is required because a window-function result
cannot be filtered directly in the WHERE clause.
*/

WITH ranked_transactions AS (
    SELECT
        account_id,
        transaction_date,
        amount,
        ROW_NUMBER() OVER (
            PARTITION BY
                account_id,
                DATE_TRUNC('month', transaction_date)
            ORDER BY amount DESC
        ) AS rank_in_month
    FROM transactions
)

SELECT
    account_id,
    transaction_date,
    amount,
    rank_in_month
FROM ranked_transactions
WHERE rank_in_month = 1;


/*
==========================================================
A03 - AGGREGATE WINDOWS AND LEAD/LAG
==========================================================
*/


/*
Running total per account.
*/

SELECT
    account_id,
    transaction_date,
    amount,
    SUM(amount) OVER (
        PARTITION BY account_id
        ORDER BY transaction_date
        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    ) AS running_total
FROM transactions;


/*
Seven-row moving average per account.
*/

SELECT
    account_id,
    transaction_date,
    amount,
    AVG(amount) OVER (
        PARTITION BY account_id
        ORDER BY transaction_date
        ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
    ) AS seven_transaction_avg
FROM transactions;


/*
Previous transaction amount using LAG.
*/

SELECT
    account_id,
    transaction_date,
    amount,
    LAG(amount, 1, 0) OVER (
        PARTITION BY account_id
        ORDER BY transaction_date
    ) AS previous_amount
FROM transactions;


/*
Next transaction amount using LEAD.
*/

SELECT
    account_id,
    transaction_date,
    amount,
    LEAD(amount, 1, 0) OVER (
        PARTITION BY account_id
        ORDER BY transaction_date
    ) AS next_amount
FROM transactions;


/*
Combined window-function example.

Includes:
- Running total
- Seven-row moving average
- Previous transaction
- Next transaction
*/

SELECT
    account_id,
    transaction_date,
    amount,
    SUM(amount) OVER (
        PARTITION BY account_id
        ORDER BY transaction_date
        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    ) AS running_total,
    AVG(amount) OVER (
        PARTITION BY account_id
        ORDER BY transaction_date
        ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
    ) AS seven_transaction_avg,
    LAG(amount, 1, 0) OVER (
        PARTITION BY account_id
        ORDER BY transaction_date
    ) AS previous_amount,
    LEAD(amount, 1, 0) OVER (
        PARTITION BY account_id
        ORDER BY transaction_date
    ) AS next_amount
FROM transactions;


/*
==========================================================
A04 - PRACTICE QUERY 1
==========================================================
Exercise 1:

Return the top 3 transactions by amount for each
customer.

Include:
- customer ID
- transaction date
- amount
- rank within customer's transaction history
*/


WITH ranked_customer_transactions AS (
    SELECT
        customer_id,
        transaction_date,
        amount,
        ROW_NUMBER() OVER (
            PARTITION BY customer_id
            ORDER BY amount DESC
        ) AS transaction_rank
    FROM transactions
)

SELECT
    customer_id,
    transaction_date,
    amount,
    transaction_rank
FROM ranked_customer_transactions
WHERE transaction_rank <= 3
ORDER BY
    customer_id,
    transaction_rank;


/*
==========================================================
A04 - PRACTICE QUERY 2
==========================================================
Exercise 2:

Calculate the month-over-month change in total
transaction value per account.

Use LAG to retrieve the previous month's total.

Calculate:
- current month total
- previous month total
- percentage change
- flag when change is greater than 50%
*/


WITH monthly_totals AS (
    SELECT
        account_id,
        DATE_TRUNC('month', transaction_date) AS transaction_month,
        SUM(amount) AS monthly_total
    FROM transactions
    GROUP BY
        account_id,
        DATE_TRUNC('month', transaction_date)
),

monthly_with_previous AS (
    SELECT
        account_id,
        transaction_month,
        monthly_total,
        LAG(monthly_total) OVER (
            PARTITION BY account_id
            ORDER BY transaction_month
        ) AS previous_month_total
    FROM monthly_totals
)

SELECT
    account_id,
    transaction_month,
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
    END AS month_over_month_change_percent,
    CASE
        WHEN previous_month_total IS NULL
             OR previous_month_total = 0
        THEN 'N/A'
        WHEN (
            (monthly_total - previous_month_total)
            / previous_month_total
        ) * 100 > 50
        THEN 'MORE THAN 50%'
        ELSE '50% OR LESS'
    END AS change_flag
FROM monthly_with_previous
ORDER BY
    account_id,
    transaction_month;


/*
==========================================================
A04 - PRACTICE QUERY 3
==========================================================
Exercise 3:

Calculate each account's total transaction volume for
the current year.

Then divide all accounts into four quartiles using
NTILE(4).

The top 10% of accounts are identified by ranking the
account totals from highest to lowest.

Finally, return the accounts that fall within the top
10%, along with their quartile.
*/


WITH current_year_account_totals AS (
    SELECT
        account_id,
        SUM(amount) AS total_transaction_volume
    FROM transactions
    WHERE transaction_date >= DATE_TRUNC('year', CURRENT_DATE)
      AND transaction_date < DATE_TRUNC('year', CURRENT_DATE) + INTERVAL '1 year'
    GROUP BY account_id
),

account_quartiles AS (
    SELECT
        account_id,
        total_transaction_volume,
        NTILE(4) OVER (
            ORDER BY total_transaction_volume DESC
        ) AS quartile,
        ROW_NUMBER() OVER (
            ORDER BY total_transaction_volume DESC
        ) AS overall_rank,
        COUNT(*) OVER () AS total_accounts
    FROM current_year_account_totals
)

SELECT
    account_id,
    total_transaction_volume,
    quartile,
    overall_rank,
    total_accounts
FROM account_quartiles
WHERE overall_rank <= CEIL(total_accounts * 0.10)
ORDER BY
    overall_rank;


/*
==========================================================
OPTIONAL CHECK
==========================================================
Shows how many accounts are in each quartile.
*/


WITH current_year_account_totals AS (
    SELECT
        account_id,
        SUM(amount) AS total_transaction_volume
    FROM transactions
    WHERE transaction_date >= DATE_TRUNC('year', CURRENT_DATE)
      AND transaction_date < DATE_TRUNC('year', CURRENT_DATE) + INTERVAL '1 year'
    GROUP BY account_id
),

account_quartiles AS (
    SELECT
        account_id,
        total_transaction_volume,
        NTILE(4) OVER (
            ORDER BY total_transaction_volume DESC
        ) AS quartile
    FROM current_year_account_totals
)

SELECT
    quartile,
    COUNT(*) AS account_count
FROM account_quartiles
GROUP BY quartile
ORDER BY quartile;


/*
==========================================================
A05 - PORTFOLIO DELIVERABLE
==========================================================
Top 3 transactions per account using ROW_NUMBER()
and DENSE_RANK().

ROW_NUMBER() gives every transaction a unique position.
This guarantees a maximum of three rows per account.

DENSE_RANK() gives transactions with the same amount
the same rank. This means an account can return more than
three rows when there are ties within the top three ranks.
*/


/*
----------------------------------------------------------
A05.1 - Top 3 transactions using ROW_NUMBER()
----------------------------------------------------------
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
WHERE transaction_rank <= 3
ORDER BY
    account_id,
    transaction_rank;


/*
----------------------------------------------------------
A05.2 - Top 3 transaction amounts using DENSE_RANK()
----------------------------------------------------------
*/

WITH ranked_transactions AS (
    SELECT
        account_id,
        transaction_date,
        amount,
        DENSE_RANK() OVER (
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
WHERE transaction_rank <= 3
ORDER BY
    account_id,
    transaction_rank,
    amount DESC;


/*
----------------------------------------------------------
A05.3 - ROW_NUMBER() vs DENSE_RANK() comparison
----------------------------------------------------------

ROW_NUMBER():
- Every transaction receives a unique number.
- Tied amounts receive different numbers.
- Returns at most three transactions per account.

DENSE_RANK():
- Transactions with the same amount receive the same rank.
- No rank numbers are skipped after ties.
- Can return more than three transactions per account
  when tied amounts occur within the top three ranks.

Example:

Amount     ROW_NUMBER     DENSE_RANK
1000       1              1
1000       2              1
900        3              2
800        4              3

Therefore:

ROW_NUMBER() treats each transaction as a separate row
for the top-3 limit.

DENSE_RANK() treats equal transaction amounts as the same
rank and can therefore return additional tied transactions.
*/
USE Fintrust;

ALTER TABLE transactions
ADD suspicious_flag ENUM('Y','N');

ALTER TABLE accounts
ADD branch_code VARCHAR(20);

# Query 1: Top 10 Customers by Suspicious Transaction Ratio

-- Find customers where more than 5% of their transactions this year were flagged as suspicious. 
-- Show their total transaction count, flagged count, and ratio, sorted by ratio descending.

WITH total_transactions AS (
    SELECT
        a.customer_id,
        COUNT(*) AS total_count
    FROM accounts a
    JOIN transactions t
        ON a.account_id = t.account_id
    WHERE YEAR(t.transaction_date) = YEAR(CURDATE())
    GROUP BY a.customer_id
),

flagged_transactions AS (
    SELECT
        a.customer_id,
        COUNT(*) AS flagged_count
    FROM accounts a
    JOIN transactions t
        ON a.account_id = t.account_id
    WHERE YEAR(t.transaction_date) = YEAR(CURDATE())
      AND t.suspicious_flag = 'Y'
    GROUP BY a.customer_id
)

SELECT
    t.customer_id,
    t.total_count,
    COALESCE(f.flagged_count, 0) AS flagged_count,
    ROUND(
        COALESCE(f.flagged_count, 0) / t.total_count,
        4
    ) AS ratio
FROM total_transactions t
LEFT JOIN flagged_transactions f
    ON t.customer_id = f.customer_id
WHERE COALESCE(f.flagged_count, 0) / t.total_count > 0.05
ORDER BY ratio DESC
LIMIT 10;

# Query 2: Branch Month-on-Month Suspicious Amount Change

-- For each branch, compare the total suspicious transaction value in June 2024 to May 2024. Show branches where June exceeds May by more than 20%.

WITH may_totals AS (
    SELECT
        a.branch_code,
        SUM(t.amount) AS may_amount
    FROM accounts a
    JOIN transactions t
        ON a.account_id = t.account_id
    WHERE t.suspicious_flag = 'Y'
      AND t.transaction_date >= '2024-05-01'
      AND t.transaction_date < '2024-06-01'
    GROUP BY a.branch_code
),

june_totals AS (
    SELECT
        a.branch_code,
        SUM(t.amount) AS june_amount
    FROM accounts a
    JOIN transactions t
        ON a.account_id = t.account_id
    WHERE t.suspicious_flag = 'Y'
      AND t.transaction_date >= 
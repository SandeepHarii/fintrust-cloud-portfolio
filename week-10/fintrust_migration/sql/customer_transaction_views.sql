-- Task 1: Customer account summary
CREATE OR REPLACE VIEW v_customer_accounts AS
SELECT
    c.customer_id,
    c.first_name || ' ' || c.last_name AS full_name,
    c.segment,
    c.region,
    COUNT(a.account_id) AS account_count,
    SUM(a.balance) AS total_balance,
    SUM(
        CASE
            WHEN a.currency = 'ZAR' THEN a.balance
            ELSE 0
        END
    ) AS zar_balance,
    MIN(c.onboarded_date) AS onboarded_date
FROM customers c
LEFT JOIN accounts a
    ON c.customer_id = a.customer_id
    AND a.status = 'active'
GROUP BY
    c.customer_id,
    c.first_name,
    c.last_name,
    c.segment,
    c.region;


-- Task 2: Monthly transaction summary
CREATE OR REPLACE VIEW v_monthly_txn_summary AS
SELECT
    DATE_TRUNC('month', t.txn_date) AS txn_month,
    c.segment,
    t.channel,
    t.txn_type,
    COUNT(*) AS txn_count,
    SUM(t.amount) AS total_amount,
    AVG(t.amount) AS avg_amount,
    MAX(t.amount) AS max_amount
FROM transactions t
JOIN accounts a
    ON t.account_id = a.account_id
JOIN customers c
    ON a.customer_id = c.customer_id
GROUP BY
    DATE_TRUNC('month', t.txn_date),
    c.segment,
    t.channel,
    t.txn_type
ORDER BY
    txn_month DESC,
    total_amount DESC;


-- Verification 1: Top 5 customers by total balance
SELECT
    full_name,
    segment,
    account_count,
    total_balance
FROM v_customer_accounts
ORDER BY total_balance DESC
LIMIT 5;


-- Verification 2: Digital channel volume for the last 3 months
SELECT
    txn_month,
    txn_count,
    total_amount
FROM v_monthly_txn_summary
WHERE channel = 'digital'
ORDER BY txn_month DESC
LIMIT 3;
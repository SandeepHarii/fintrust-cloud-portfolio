-- ============================================================
-- FinTrust SQL Performance Tuning
-- W12 D3 PM
-- ============================================================


-- ============================================================
-- Scenario 1
-- Monthly transaction summary by customer
-- ============================================================

EXPLAIN ANALYZE
SELECT
    c.customer_name,
    DATE_TRUNC('month', t.transaction_date) AS month,
    COUNT(*) AS transaction_count,
    SUM(t.amount) AS total_amount
FROM transactions t
JOIN customers c
    ON t.customer_id = c.customer_id
WHERE t.transaction_date BETWEEN '2024-01-01' AND '2024-12-31'
GROUP BY
    c.customer_name,
    DATE_TRUNC('month', t.transaction_date)
ORDER BY
    month,
    total_amount DESC;


-- Fix:
-- The query filters transactions by transaction_date and then
-- joins them using customer_id.
CREATE INDEX IF NOT EXISTS idx_transactions_date_customer
ON transactions (transaction_date, customer_id);


-- Re-run after creating the index
EXPLAIN ANALYZE
SELECT
    c.customer_name,
    DATE_TRUNC('month', t.transaction_date) AS month,
    COUNT(*) AS transaction_count,
    SUM(t.amount) AS total_amount
FROM transactions t
JOIN customers c
    ON t.customer_id = c.customer_id
WHERE t.transaction_date BETWEEN '2024-01-01' AND '2024-12-31'
GROUP BY
    c.customer_name,
    DATE_TRUNC('month', t.transaction_date)
ORDER BY
    month,
    total_amount DESC;


-- ============================================================
-- Scenario 2
-- Flagging transactions over account limit
-- ============================================================

EXPLAIN ANALYZE
SELECT
    t.*,
    a.credit_limit
FROM transactions t
JOIN accounts a
    ON t.account_id = a.account_id
WHERE t.amount > a.credit_limit * 0.9
  AND t.transaction_date >= CURRENT_DATE - INTERVAL '7 days';


-- Fix:
-- The recent transaction date is the directly indexable filter.
-- account_id supports the subsequent account join.
CREATE INDEX IF NOT EXISTS idx_transactions_date_account
ON transactions (transaction_date, account_id);


-- Re-run after creating the index
EXPLAIN ANALYZE
SELECT
    t.*,
    a.credit_limit
FROM transactions t
JOIN accounts a
    ON t.account_id = a.account_id
WHERE t.amount > a.credit_limit * 0.9
  AND t.transaction_date >= CURRENT_DATE - INTERVAL '7 days';


-- ============================================================
-- Scenario 3
-- Audit log for compliance
-- All transactions from deleted accounts
-- ============================================================

EXPLAIN ANALYZE
SELECT
    t.*
FROM transactions t
LEFT JOIN accounts a
    ON t.account_id = a.account_id
WHERE a.account_id IS NULL
ORDER BY
    t.transaction_date DESC;


-- Fix:
-- The query must inspect transactions by account_id to determine
-- whether a matching account exists, and then sort by date.
CREATE INDEX IF NOT EXISTS idx_transactions_account_date
ON transactions (account_id, transaction_date DESC);


-- Re-run after creating the index
EXPLAIN ANALYZE
SELECT
    t.*
FROM transactions t
LEFT JOIN accounts a
    ON t.account_id = a.account_id
WHERE a.account_id IS NULL
ORDER BY
    t.transaction_date DESC;
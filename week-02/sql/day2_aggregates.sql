USE Fintrust_DB;

# Exercise 1 — Count transactions per customer (15 min)
# Write a query that shows each customer's name, province, total number of transactions, and total transaction amount. Include only customers with at least 1 transaction. Sort by total amount descending.

SELECT
    c.first_name,
    c.last_name,
    c.province,
    COUNT(t.transaction_id) AS total_transactions,
    SUM(t.amount) AS total_transaction_amount
FROM Customers c
INNER JOIN Accounts a
    ON c.customer_id = a.customer_id
INNER JOIN Transactions t
    ON a.account_id = t.account_id
GROUP BY
    c.first_name,
    c.last_name,
    c.province
HAVING COUNT(t.transaction_id) >= 1
ORDER BY total_transaction_amount DESC;

# Exercise 2 — Average balance by account type (10 min)
# Show each account type (savings, cheque, etc.), the number of accounts of that type, and the average balance. Sort by average balance descending.

SELECT
    account_type,
    COUNT(account_id) AS number_of_accounts,
    AVG(balance) AS average_balance
FROM Accounts
GROUP BY account_type
ORDER BY average_balance DESC;

# Exercise 3 — HAVING filter (10 min)
# Find all provinces where the total deposits (credit transactions) exceed R 100,000. Show: province, total deposit amount, and number of credit transactions. Use HAVING to filter.

SELECT
    c.province,
    SUM(t.amount) AS total_deposit_amount,
    COUNT(t.transaction_id) AS credit_transaction_count
FROM Customers c
INNER JOIN Accounts a
    ON c.customer_id = a.customer_id
INNER JOIN Transactions t
    ON a.account_id = t.account_id
WHERE t.transaction_type = 'CREDIT'
GROUP BY c.province
HAVING SUM(t.amount) > 100000;

# Exercise 4 — Monthly summary (10 min)
# Show the total transaction amount and count per month (for all transaction types). Use YEAR() and MONTH() functions. Sort by year then month.

SELECT
    YEAR(transaction_date) AS transaction_year,
    MONTH(transaction_date) AS transaction_month,
    COUNT(transaction_id) AS transaction_count,
    SUM(amount) AS total_transaction_amount
FROM Transactions
GROUP BY
    YEAR(transaction_date),
    MONTH(transaction_date)
ORDER BY
    transaction_year,
    transaction_month;
    
# Exercise 5 — Challenge: Fraud signal (10 min)
# Find customers who have made more than 3 debit transactions in a single day. This is a fraud detection pattern. Show: customer name, transaction date, and count of debits that day.

SELECT
    c.first_name,
    c.last_name,
    DATE(t.transaction_date) AS transaction_day,
    COUNT(t.transaction_id) AS debit_count
FROM Customers c
INNER JOIN Accounts a
    ON c.customer_id = a.customer_id
INNER JOIN Transactions t
    ON a.account_id = t.account_id
WHERE t.transaction_type = 'DEBIT'
GROUP BY
    c.first_name,
    c.last_name,
    DATE(t.transaction_date)
HAVING COUNT(t.transaction_id) > 3
ORDER BY debit_count DESC;
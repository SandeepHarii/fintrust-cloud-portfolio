USE Fintrust_DB;

# Exercise 1 — Basic INNER JOIN (15 min)
# Write a query that returns: customer first name, last name, account type, and current balance for all customers. Sort by balance descending. Expected: each customer-account combination as one row.

SELECT
    c.first_name,
    c.last_name,
    a.account_type,
    a.balance
FROM customers c
INNER JOIN accounts a ON c.customer_id = a.customer_id
ORDER BY a.balance DESC;

# Exercise 2 — Filtered JOIN (10 min)
# Find all customers from Gauteng with a balance greater than R 25,000. Show: name, province, account type, balance.

SELECT
	c.first_name,
	c.last_name,
	c.province,
	a. account_type,
	a.balance
FROM Customers c
INNER JOIN accounts a 
	ON c.customer_id = a.customer_id
WHERE c.province = 'Gauteng'
	AND a.balance > 25000;
    
# Exercise 3 — 3-Table JOIN (15 min)
# Write a query joining all three tables. Show: customer name, account type, transaction amount, and transaction date. Filter to only debit transactions. Sort by transaction date descending.

SELECT
    c.first_name,
    c.last_name,
    a.account_type,
    t.amount,
    t.transaction_date
FROM Customers c
INNER JOIN Accounts a
    ON c.customer_id = a.customer_id
INNER JOIN Transactions t
    ON a.account_id = t.account_id
WHERE t.transaction_type = 'DEBIT'
ORDER BY t.transaction_date DESC;

# Exercise 4 — LEFT JOIN Anti-Pattern (10 min)
# Find any customers who have never made a transaction. Use a LEFT JOIN from customers → accounts → transactions with an IS NULL filter.

SELECT
    c.first_name,
    c.last_name,
    c.customer_id
FROM Customers c
LEFT JOIN Accounts a
    ON c.customer_id = a.customer_id
LEFT JOIN Transactions t
    ON a.account_id = t.account_id
WHERE t.transaction_id IS NULL;

# Exercise 5 — Challenge Query (5 min)
# Find all transactions greater than R 10,000 for customers in Western Cape or KwaZulu-Natal. Show customer name, province, and transaction amount. Sort by amount descending.

SELECT
    c.first_name,
    c.last_name,
    c.province,
    t.amount
FROM Customers c
INNER JOIN Accounts a
    ON c.customer_id = a.customer_id
INNER JOIN Transactions t
    ON a.account_id = t.account_id
WHERE t.amount > 10000
  AND c.province IN ('Western Cape', 'KwaZulu-Natal')
ORDER BY t.amount DESC;

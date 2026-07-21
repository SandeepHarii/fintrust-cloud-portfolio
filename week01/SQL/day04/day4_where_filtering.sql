USE fintrust_db;

# Exercise 1 — Basic Equality
# Find all customers from Gauteng.

SELECT * FROM CUSTOMERS
WHERE PROVINCE = 'Gauteng';

# Exercise 2 — Numeric Comparison
# Find all accounts with a balance greater than R5,000.

SELECT *
FROM ACCOUNTS
WHERE BALANCE > 5000;

# Exercise 3 — LIKE Pattern
# Find all customers whose email address ends in '.co.za'.

SELECT * FROM CUSTOMERS
WHERE EMAIL
LIKE '%.co.za';

# Exercise 4 — IN Operator
# Find all transactions of type DEBIT or PAYMENT (using IN, not multiple ORs).

SELECT * FROM TRANSACTIONS
WHERE TRANSACTION_TYPE IN ('DEBIT','PAYMENT'); 

# Exercise 5 — AND Combination
# Find all SAVINGS accounts with a balance between R1,000 and R50,000.

SELECT * FROM ACCOUNTS
WHERE ACCOUNT_TYPE = 'SAVINGS'
AND BALANCE 
BETWEEN 1000 AND 50000;

# Exercise 6 — IS NULL / IS NOT NULL
# Find all transactions that DO have a merchant_category recorded (not NULL).

SELECT * FROM TRANSACTIONS
WHERE MERCHANT_CATEGORY IS NOT NULL

USE Fintrust_DB

# Challenge 1 — Easy
# Find all customers NOT from Gauteng or Western Cape.

SELECT * FROM customers
WHERE province 
NOT IN ('Gauteng', 'Western Cape');

# Challenge 2 — Easy-Medium
# Find all accounts with a balance between R1,000 and R20,000 (inclusive) of type CHEQUE or SAVINGS.

SELECT * FROM accounts
WHERE balance BETWEEN 1000 AND 20000
AND account_type IN ('CHEQUE', 'SAVINGS');

# Challenge 3 — Medium
# Find all transactions with a merchant_category that contains the word 'Food' OR 'Groceries', for amounts over R200.

SELECT * FROM Transactions
WHERE (
    merchant_category LIKE '%Food%'
    OR merchant_category LIKE '%Groceries%'
)
AND amount > 200;

# Challenge 4 — Medium-Hard
# Find all DEBIT transactions where no merchant_category was recorded AND the amount is greater than R100.

SELECT * FROM Transactions
WHERE transaction_type = 'DEBIT'
  AND merchant_category IS NULL
  AND amount > 100;
  
# Challenge 5 — Hard
# Find all customers whose email address ends in either '.co.za' or '.com', ordered by last_name ascending, and who have their province recorded.

SELECT * FROM customers
WHERE (
    email LIKE '%.co.za'
    OR email LIKE '%.com'
)
AND province IS NOT NULL
ORDER BY last_name ASC;
  


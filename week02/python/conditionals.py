# Exercise 1 — Transaction Classifier

def classify_transaction(amount):
    if 0 < amount <= 100:
        return "MICRO"
    elif 100 < amount <= 1000:
        return "SMALL"
    elif 1000< amount <= 10000:
        return "STANDARD"
    elif amount > 10000:
        return "LARGE"
    else:
        return "INVALID"
    
print(classify_transaction(50))    # Output: MICRO
print(classify_transaction(9999))  # Output: STANDARD
print(classify_transaction(-50))   # Output: INVALID

# Exercise 2 — Interest Rate Calculator

def get_interest_rate(credit_score):
    if credit_score >= 750:
        return 7.5
    elif 700 <= credit_score < 750:
        return 9.5
    elif 650 <= credit_score < 700:
        return 12.0
    elif credit_score < 650:
        return 18.5
    else:
        return 0.00

print(get_interest_rate(720))  # Output: 9.5
print(get_interest_rate(800))  # Output: 7.5

# Exercise 3 — ATM Withdrawal Logic

def atm_withdraw(balance, amount):
    if amount <= 0:
        return (False, "Invalid amount")
    elif amount > 5000:
        return (False, "ATM daily limit is R5 000")
    elif amount > balance:
        return (False, "Insufficient funds")
    else:
        return (True, f"Dispensing R{amount:.2f}")
    
print(atm_withdraw(3000, 1500))   # Output: (True, "Dispensing R1500.00")
print(atm_withdraw(500, 600))   # Output: (False, "Insufficient funds")

# Exercise 4 — Transaction Tagger

def tag_transaction(tx_type, merchant_category, amount):
    if tx_type == "REFUND":
        return "REFUND"
    elif merchant_category == "GAMBLING":
        return "HIGH_RISK"
    elif merchant_category == "GROCERY" and amount < 500:
        return "ROUTINE"
    elif amount > 10000:
        return "LARGE_PURCHASE"
    else:
        return "STANDARD"
    
print(tag_transaction("REFUND", "GROCERY", 250))
# REFUND

print(tag_transaction("PURCHASE", "GAMBLING", 100))
# HIGH_RISK

print(tag_transaction("PURCHASE", "GROCERY", 450))
# ROUTINE

print(tag_transaction("PURCHASE", "ELECTRONICS", 15000))
# LARGE_PURCHASE

print(tag_transaction("PURCHASE", "RESTAURANT", 250))
# STANDARD
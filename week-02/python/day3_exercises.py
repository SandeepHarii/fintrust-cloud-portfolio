# Exercise 1 — Account Formatter

# Expected output:
# Customer: Thabo Nkosi
# Account:  SAVINGS
# Balance:  R 52,750.00
# Status:   ACTIVE

customer_name = "Thabo Nkosi"
account_type = "SAVINGS"
balance = 52750.00
status = "ACTIVE"


def format_account_summary(customer_name, account_type, balance):
    from decimal import Decimal
    d_balance = Decimal(str(balance))
    return (
        f"Customer: {customer_name.title()}\n"
        f"Account:  {account_type.upper()}\n"
        f"Balance:  R {d_balance:,.2f}\n"
        f"Status:   ACTIVE"
    )

print(format_account_summary(customer_name, account_type, balance))

# Exercise 2 — Compound Interest

from decimal import Decimal
import math

def calculate_compound_interest(principal, annual_rate, years, n=12):
    """
    principal: initial amount (Decimal)
    annual_rate: e.g. 0.085 for 8.5%
    years: number of years
    n: compounding periods per year (default 12 = monthly)
    """
    p = float(principal)
    amount = p * (1 + annual_rate / n) ** (n * years)
    interest_earned = amount - p
    return Decimal(str(round(amount, 2))), Decimal(str(round(interest_earned, 2)))

# Test it:
principal = Decimal("50000.00")
amount, interest = calculate_compound_interest(principal, 0.085, 3)
print(f"After 3 years: R {amount:,.2f} (interest earned: R {interest:,.2f})")

# Exercise 3 — List operations

from decimal import Decimal

transactions = [
    Decimal("250.00"), Decimal("12500.00"), Decimal("750.50"),
    Decimal("88000.00"), Decimal("1200.00"), Decimal("3450.00"),
    Decimal("55000.00"), Decimal("125.00"), Decimal("9800.00")
]

total = sum(transactions)
average = total / len(transactions)
maximum = max(transactions)
minimum = min(transactions)
count_above_10000 = sum(1 for t in transactions if t > Decimal("10000.00")) 

# Your code here: calculate total, average, max, min, count_above_5000

print(f"Total: R {total:,.2f}")
print(f"Average: R {average:,.2f}")
print(f"Maximum: R {maximum:,.2f}")
print(f"Minimum: R {minimum:,.2f}")
print(f"Count of transactions above R 10,000: {count_above_10000}")
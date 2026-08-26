"""
Week 8 - Pandas Transaction Analysis

This script demonstrates how FinTrust analysts can
query transaction data using Pandas before data is
loaded into Athena.

The same business questions can later be answered
using Athena SQL against data stored in S3.
"""

import pandas as pd

data = {
    "account_id": [
        "ACC-0001",
        "ACC-0002",
        "ACC-0001",
        "ACC-0003"
    ],
    "amount": [
        1500.00,
        87000.00,
        250.00,
        12500.00
    ],
    "currency": [
        "ZAR",
        "ZAR",
        "ZAR",
        "USD"
    ],
    "is_high_value": [
        False,
        True,
        False,
        False
    ]
}

df = pd.DataFrame(data)

print("Transaction Dataset")
print(df)

print("\nHigh Value Transactions")

high_value = df[
    df["is_high_value"] == True
]

print(
    high_value[
        ["account_id", "amount", "currency"]
    ]
)

print("\nTotal Amount by Currency")

by_currency = (
    df.groupby("currency")["amount"]
      .sum()
      .reset_index()
)

by_currency.columns = [
    "currency",
    "total_amount"
]

print(by_currency)

# Future workflow:
# 1. Read Parquet files from S3
# 2. Analyse processed transaction data
# 3. Validate analytics
"""
Week 8 - FinTrust ETL Pipeline

This script demonstrates the ETL process used by
FinTrust to transform transaction data before
loading it into the analytics platform.

AWS upload steps will be enabled once cloud
resources have been configured.
"""

import pandas as pd
from io import StringIO

csv_data = """
transaction_id,account_id,amount,currency,timestamp,status
txn-001,ACC-0001,1500.00,ZAR,2024-06-01 09:15:33,COMPLETED
txn-002,ACC-0002,87000.00,ZAR,2024-06-01 09:22:11,COMPLETED
txn-003,ACC-0001,250.00,ZAR,2024-06-02 14:05:02,COMPLETED
txn-004,ACC-0003,12500.00,USD,2024-06-02 16:44:55,PENDING
"""

df = pd.read_csv(StringIO(csv_data))

df["timestamp"] = pd.to_datetime(df["timestamp"])
df["year"] = df["timestamp"].dt.year.astype(str)
df["month"] = df["timestamp"].dt.month.astype(str).str.zfill(2)
df["is_high_value"] = df["amount"] > 50000

print("Transformed Dataset")
print(df)

print("\nData Types")
print(df.dtypes)

# Future ETL steps:
# 1. Write Parquet files using PyArrow
# 2. Partition by year/month
# 3. Upload to S3
# 4. Register tables in Glue Catalog
# 5. Query with Athena
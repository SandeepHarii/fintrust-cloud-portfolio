"""
Week 8 - Parquet Partition Simulator

This script demonstrates the Hive-style partition
structure used by Athena, Glue, and EMR.

The partition structure helps reduce query costs
by allowing partition pruning.
"""

transactions = [
    {
        "year": "2024",
        "month": "06",
        "transaction_id": "txn-001"
    },
    {
        "year": "2024",
        "month": "06",
        "transaction_id": "txn-002"
    },
    {
        "year": "2024",
        "month": "07",
        "transaction_id": "txn-003"
    }
]

for txn in transactions:

    parquet_path = (
        f"fintrust_processed/"
        f"year={txn['year']}/"
        f"month={txn['month']}/"
        f"transactions.parquet"
    )

    print(parquet_path)

# Future workflow:
# 1. Generate Parquet files
# 2. Store them in partitioned directories
# 3. Upload partitions to S3
# 4. Register partitions in Glue
# 5. Query with Athena
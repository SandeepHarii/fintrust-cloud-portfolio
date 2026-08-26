"""
Week 8 - S3 Parquet Upload Utility

AWS upload operations have been commented out until
AWS resources and permissions are configured.

This script demonstrates how FinTrust would upload
partitioned Parquet data while preserving the
year/month folder structure.
"""

# import boto3
from pathlib import Path

# s3 = boto3.client(
#     "s3",
#     region_name="af-south-1"
# )

BUCKET = "fintrust-processed"


def upload_parquet_partition(local_path, s3_key):

    # s3.upload_file(
    #     local_path,
    #     BUCKET,
    #     s3_key
    # )

    print(
        f"AWS upload disabled:\n"
        f"Local File: {local_path}\n"
        f"S3 Path: s3://{BUCKET}/{s3_key}\n"
    )


files = [
    Path(
        "fintrust_processed/year=2024/month=06/transactions.parquet"
    ),
    Path(
        "fintrust_processed/year=2024/month=07/transactions.parquet"
    )
]

for file in files:

    s3_key = (
        "transactions/"
        + str(file).replace(
            "fintrust_processed/",
            ""
        )
    )

    upload_parquet_partition(
        str(file),
        s3_key
    )

# Future workflow:
# 1. Generate partitioned Parquet files
# 2. Upload partitions to S3
# 3. Register partitions with Glue
# 4. Query via Athena